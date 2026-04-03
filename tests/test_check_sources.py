"""Tests for scripts/check_sources.py."""

import json
import sys
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

# Make the scripts directory importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_sources as cs

from tests.conftest import write_doc


# ── Helpers ───────────────────────────────────────────────────────────────────

def _future(days: int) -> str:
    return (date.today() + timedelta(days=days)).strftime("%Y-%m-%d")


def _past(days: int) -> str:
    return (date.today() - timedelta(days=days)).strftime("%Y-%m-%d")


TODAY_STR = date.today().strftime("%Y-%m-%d")

VALID_SOURCE_BLOCK = f"""\
sources:
  - id: eu-ai-act
    ref: Verordening (EU) 2024/1689
    url: https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32024R1689
    date_verified: "{TODAY_STR}"
    next_review: "{_future(180)}"
"""

COMPLIANCE_FM = f"""\
versie: '1.1'
type: compliance
layer: 3
roles: [Guardian]
tags: [eu-ai-act, security]
summary: Test doc.
answers: [Test?]
{VALID_SOURCE_BLOCK}
"""


# ── parse_frontmatter ─────────────────────────────────────────────────────────

class TestParseFrontmatter:
    def test_parses_valid_yaml(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text("---\nversie: '1.0'\ntype: compliance\n---\n\n# Body")
        fm = cs.parse_frontmatter(p)
        assert fm["versie"] == "1.0"
        assert fm["type"] == "compliance"

    def test_returns_none_without_frontmatter(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text("# Just a heading\n\nNo frontmatter here.")
        assert cs.parse_frontmatter(p) is None

    def test_returns_none_on_invalid_yaml(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text("---\n: broken: yaml: [\n---\n")
        assert cs.parse_frontmatter(p) is None

    def test_parses_nested_sources_block(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text(
            "---\ntype: compliance\nsources:\n  - id: eu-ai-act\n    ref: Test\n---\n"
        )
        fm = cs.parse_frontmatter(p)
        assert isinstance(fm["sources"], list)
        assert fm["sources"][0]["id"] == "eu-ai-act"

    def test_empty_frontmatter_returns_empty_dict(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text("---\n---\n\n# Body")
        fm = cs.parse_frontmatter(p)
        assert fm == {} or fm is None  # yaml.safe_load("") → None


# ── check_doc ─────────────────────────────────────────────────────────────────

class TestCheckDoc:
    def test_clean_compliance_doc_no_issues(self, tmp_docs):
        path = write_doc(tmp_docs, "compliance.md", COMPLIANCE_FM)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        assert issues == []

    def test_compliance_without_sources_is_error(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
        """
        path = write_doc(tmp_docs, "no-sources.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        errors = [i for i in issues if i.severity == "error"]
        assert any("sources" in i.message for i in errors)

    def test_non_compliance_type_skipped(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: index
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
        """
        path = write_doc(tmp_docs, "index.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        assert issues == []

    def test_compliance_without_regulatory_tags_skipped(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [onboarding]
            summary: Test.
        """
        path = write_doc(tmp_docs, "no-tags.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        assert issues == []

    def test_overdue_next_review_is_warning(self, tmp_docs):
        fm = f"""\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources:
              - id: eu-ai-act
                ref: Test Ref
                url: https://example.com
                date_verified: "{_past(400)}"
                next_review: "{_past(10)}"
        """
        path = write_doc(tmp_docs, "overdue.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        warnings = [i for i in issues if i.severity == "warning"]
        assert any("overdue" in i.message for i in warnings)

    def test_upcoming_review_within_30_days_is_info(self, tmp_docs):
        fm = f"""\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources:
              - id: eu-ai-act
                ref: Test Ref
                url: https://example.com
                date_verified: "{_past(200)}"
                next_review: "{_future(15)}"
        """
        path = write_doc(tmp_docs, "upcoming.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        infos = [i for i in issues if i.severity == "info"]
        assert any("30 days" in i.message for i in infos)

    def test_future_review_beyond_30_days_no_issue(self, tmp_docs):
        path = write_doc(tmp_docs, "future.md", COMPLIANCE_FM)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        assert not any(i.severity in ("warning", "info") for i in issues)

    def test_missing_required_source_fields_is_error(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources:
              - id: eu-ai-act
                ref: Only ref, missing url/date_verified/next_review
        """
        path = write_doc(tmp_docs, "missing-fields.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        errors = [i for i in issues if i.severity == "error"]
        assert any("missing required fields" in i.message for i in errors)

    def test_invalid_date_verified_format_is_error(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources:
              - id: eu-ai-act
                ref: Test
                url: https://example.com
                date_verified: "15-03-2025"
                next_review: "2026-01-01"
        """
        path = write_doc(tmp_docs, "bad-date.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        errors = [i for i in issues if i.severity == "error"]
        assert any("date_verified" in i.message for i in errors)

    def test_invalid_next_review_format_is_error(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources:
              - id: eu-ai-act
                ref: Test
                url: https://example.com
                date_verified: "2025-03-20"
                next_review: "Q1 2026"
        """
        path = write_doc(tmp_docs, "bad-next-review.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        errors = [i for i in issues if i.severity == "error"]
        assert any("next_review" in i.message for i in errors)

    def test_unknown_source_id_is_warning(self, tmp_docs):
        fm = f"""\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources:
              - id: unknown-framework-xyz
                ref: Test
                url: https://example.com
                date_verified: "{_past(10)}"
                next_review: "{_future(180)}"
        """
        path = write_doc(tmp_docs, "unknown-id.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        warnings = [i for i in issues if i.severity == "warning"]
        assert any("unknown source id" in i.message for i in warnings)

    def test_sources_not_a_list_is_error(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            sources: "not-a-list"
        """
        path = write_doc(tmp_docs, "sources-string.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        errors = [i for i in issues if i.severity == "error"]
        assert any("list" in i.message for i in errors)

    def test_playbook_type_also_checked(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: playbook
            layer: 3
            roles: [Guardian]
            tags: [security]
            summary: Test.
        """
        path = write_doc(tmp_docs, "playbook.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        errors = [i for i in issues if i.severity == "error"]
        assert any("sources" in i.message for i in errors)

    def test_multiple_sources_all_validated(self, tmp_docs):
        fm = f"""\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act, ethics]
            summary: Test.
            sources:
              - id: eu-ai-act
                ref: Ref 1
                url: https://example.com/1
                date_verified: "{TODAY_STR}"
                next_review: "{_future(180)}"
              - id: hleg-ethics
                ref: Ref 2
                url: https://example.com/2
                date_verified: "{TODAY_STR}"
                next_review: "{_future(365)}"
        """
        path = write_doc(tmp_docs, "multi-source.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.check_doc(path)
        assert issues == []


# ── run_local_checks ──────────────────────────────────────────────────────────

class TestRunLocalChecks:
    def test_skips_en_files(self, tmp_docs):
        """EN mirror files should never be checked for sources."""
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
        """
        write_doc(tmp_docs, "doc.en.md", fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.run_local_checks()
        assert issues == []

    def test_detects_issues_across_multiple_docs(self, tmp_docs):
        good_fm = COMPLIANCE_FM
        bad_fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Bad doc.
        """
        write_doc(tmp_docs, "good.md", good_fm)
        write_doc(tmp_docs, "bad.md", bad_fm)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.run_local_checks()
        assert len(issues) >= 1
        docs_with_issues = {i.doc for i in issues}
        assert any("bad.md" in d for d in docs_with_issues)
        assert not any("good.md" in d for d in docs_with_issues)

    def test_clean_docs_produce_no_issues(self, tmp_docs):
        write_doc(tmp_docs, "clean.md", COMPLIANCE_FM)
        with patch.object(cs, "DOCS_ROOT", tmp_docs):
            issues = cs.run_local_checks()
        assert issues == []


# ── Remote check (mocked) ─────────────────────────────────────────────────────

class TestCheckRemoteEurlex:
    def test_no_newer_dates_no_warning(self):
        old_html = "<html>13/01/2024 some old date</html>"
        with patch("check_sources._fetch_url", return_value=old_html):
            warnings = cs.check_eurlex_celex("32024R1689", "2025-01-01")
        assert warnings == []

    def test_newer_date_triggers_warning(self):
        # A date that's in the future relative to date_verified
        future_html = "<html>01/06/2026 new document found here</html>"
        with patch("check_sources._fetch_url", return_value=future_html):
            warnings = cs.check_eurlex_celex("32024R1689", "2025-01-01")
        assert any("EUR-Lex shows related documents" in w for w in warnings)

    def test_unreachable_url_triggers_warning(self):
        with patch("check_sources._fetch_url", return_value=None):
            warnings = cs.check_eurlex_celex("32024R1689", "2025-01-01")
        assert any("not accessible" in w or "Could not reach" in w for w in warnings)

    def test_document_not_found_triggers_warning(self):
        not_found_html = "<html>Document not found on EUR-Lex</html>"
        with patch("check_sources._fetch_url", return_value=not_found_html):
            warnings = cs.check_eurlex_celex("32024R1689", "2025-01-01")
        assert any("not found" in w for w in warnings)


# ── Output formatters ─────────────────────────────────────────────────────────

class TestFormatReport:
    def _make_issues(self):
        return [
            cs.Issue("doc-a.md", "eu-ai-act", "error", "missing sources block"),
            cs.Issue("doc-b.md", "eu-ai-act", "warning", "review overdue by 5 days"),
            cs.Issue("doc-c.md", "hleg-ethics", "info", "review due within 30 days"),
        ]

    def test_report_contains_all_severities(self):
        report = cs.format_report(self._make_issues())
        assert "ERRORS" in report
        assert "WARNINGS" in report
        assert "INFO" in report

    def test_report_shows_counts(self):
        report = cs.format_report(self._make_issues())
        assert "Errors:    1" in report
        assert "Warnings:  1" in report
        assert "Info:      1" in report

    def test_clean_report_shows_all_clear(self):
        report = cs.format_report([])
        assert "✓ All sources are current" in report

    def test_report_contains_today(self):
        report = cs.format_report([])
        assert str(date.today()) in report


class TestFormatGithubIssue:
    def _make_issues(self):
        return [
            cs.Issue("doc.md", "eu-ai-act", "error", "missing sources"),
            cs.Issue("doc.md", "eu-ai-act", "warning", "overdue by 3 days"),
        ]

    def test_github_issue_has_markdown_headers(self):
        body = cs.format_github_issue(self._make_issues(), remote=True)
        assert "## Source Currency Report" in body
        assert "### Errors" in body
        assert "### Warnings" in body

    def test_github_issue_shows_remote_flag(self):
        body = cs.format_github_issue([], remote=True)
        assert "yes" in body
        body2 = cs.format_github_issue([], remote=False)
        assert "no" in body2

    def test_github_issue_contains_how_to_resolve(self):
        body = cs.format_github_issue(self._make_issues(), remote=False)
        assert "How to resolve" in body
        assert "date_verified" in body

    def test_github_issue_auto_generated_attribution(self):
        body = cs.format_github_issue([], remote=False)
        assert "source-review.yml" in body


class TestFormatJson:
    def test_json_is_valid(self):
        issues = [cs.Issue("doc.md", "eu-ai-act", "error", "test")]
        output = cs.format_json(issues)
        data = json.loads(output)
        assert data["errors"] == 1
        assert data["warnings"] == 0
        assert len(data["issues"]) == 1

    def test_json_contains_required_keys(self):
        output = cs.format_json([])
        data = json.loads(output)
        assert "generated" in data
        assert "total" in data
        assert "errors" in data
        assert "warnings" in data
        assert "issues" in data

    def test_json_issue_has_all_fields(self):
        issue = cs.Issue("a.md", "eu-ai-act", "warning", "review overdue")
        data = json.loads(cs.format_json([issue]))
        item = data["issues"][0]
        assert item["doc"] == "a.md"
        assert item["source_id"] == "eu-ai-act"
        assert item["severity"] == "warning"
        assert "overdue" in item["message"]
