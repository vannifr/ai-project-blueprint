"""Tests for the sources-block check added to scripts/validate_frontmatter.py."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_frontmatter as vf

from tests.conftest import write_doc


# ── parse_frontmatter (script's own simple parser) ────────────────────────────

class TestParseFrontmatter:
    def test_parses_simple_scalars(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text("---\nversie: '1.0'\ntype: compliance\nlayer: 3\n---\n")
        fm = vf.parse_frontmatter(p.read_text())
        assert fm["versie"] == "1.0"
        assert fm["type"] == "compliance"
        assert fm["layer"] == 3

    def test_parses_list_values(self, tmp_path):
        p = tmp_path / "doc.md"
        p.write_text("---\nroles: [Guardian, Data Scientist]\ntags: [eu-ai-act]\n---\n")
        fm = vf.parse_frontmatter(p.read_text())
        assert "Guardian" in fm["roles"]
        assert "Data Scientist" in fm["roles"]

    def test_returns_empty_dict_when_no_frontmatter(self):
        fm = vf.parse_frontmatter("# Just a heading")
        assert fm == {}

    def test_parses_boolean_values(self):
        fm = vf.parse_frontmatter("---\npdf: false\n---\n")
        assert fm["pdf"] is False


# ── validate_file — sources check (check 11) ──────────────────────────────────

class TestSourcesValidation:
    """Tests for check #11: compliance/playbook docs with regulatory tags need sources."""

    def _make_result(self) -> vf.ValidationResult:
        return vf.ValidationResult()

    def _write(self, tmp_docs, name, frontmatter, body="# Body"):
        return write_doc(tmp_docs, name, frontmatter, body)

    def test_compliance_eu_ai_act_with_sources_no_warning(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/doc.md", fm,
                           body="sources:\n  - id: eu-ai-act\n# Body")
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert source_warnings == []

    def test_compliance_eu_ai_act_without_sources_warns(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/doc.md", fm)
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert len(source_warnings) == 1

    def test_playbook_security_without_sources_warns(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: playbook
            layer: 3
            roles: [Guardian]
            tags: [security, eu-ai-act, playbook]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/playbook.md", fm)
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert len(source_warnings) == 1

    def test_en_file_not_checked_for_sources(self, tmp_docs):
        """EN mirror files should not trigger sources warnings."""
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/doc.en.md", fm)
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert source_warnings == []

    def test_index_type_not_checked_for_sources(self, tmp_docs):
        """index type docs are exempt even with eu-ai-act tag."""
        fm = """\
            versie: '1.1'
            type: index
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/index.md", fm)
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert source_warnings == []

    def test_compliance_with_non_regulatory_tags_not_checked(self, tmp_docs):
        """Compliance doc with only non-regulatory tags should not require sources."""
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [onboarding]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/doc.md", fm)
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert source_warnings == []

    def test_warning_mentions_check_sources_script(self, tmp_docs):
        """Warning message should point to the fix command."""
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            answers: [Q?]
        """
        path = self._write(tmp_docs, "07-compliance-hub/doc.md", fm)
        result = self._make_result()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        source_warnings = [w for w in result.warnings if "sources" in w]
        assert any("check_sources.py" in w for w in source_warnings)


# ── validate_file — existing checks (regression) ─────────────────────────────

class TestExistingChecksRegression:
    """Smoke tests to ensure pre-existing checks still work after our edit."""

    def _write_valid(self, tmp_docs):
        fm = """\
            versie: '1.1'
            type: compliance
            layer: 3
            roles: [Guardian]
            tags: [eu-ai-act]
            summary: Test.
            answers: [Q?]
        """
        return write_doc(tmp_docs, "07-compliance-hub/valid.md", fm,
                         body="sources:\n  - id: eu-ai-act\n# Body")

    def test_missing_versie_is_error(self, tmp_docs):
        fm = "type: compliance\nlayer: 3\nroles: [Guardian]\ntags: [eu-ai-act]\nsummary: T."
        path = write_doc(tmp_docs, "07-compliance-hub/no-versie.md", fm)
        result = vf.ValidationResult()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        assert any("versie" in e for e in result.errors)

    def test_invalid_type_is_error(self, tmp_docs):
        fm = "versie: '1.0'\ntype: bogus\nlayer: 3\nroles: [Guardian]\ntags: []\nsummary: T."
        path = write_doc(tmp_docs, "doc.md", fm)
        result = vf.ValidationResult()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        assert any("invalid type" in e for e in result.errors)

    def test_valid_doc_produces_no_errors(self, tmp_docs):
        path = self._write_valid(tmp_docs)
        result = vf.ValidationResult()
        with pytest.MonkeyPatch().context() as mp:
            mp.setattr(vf, "DOCS_ROOT", tmp_docs)
            vf.validate_file(path, result)
        assert result.errors == []

# ── answers: quality check ────────────────────────────────────────────────────

class TestAnswersQuality:
    """Tests for check_answers_quality() — written before implementation (TDD)."""

    BAD_ANSWERS: list[tuple[str, str]] = [
        ("Wat is Gate Review?", "Wat is X"),
        ("What is the Validation Phase?", "What is X"),
        ("Wat bevat het onderdeel Rollen?", "Wat bevat X"),
        ("What does the Compliance Hub section contain?", "What does X contain"),
        ("Wat houdt Samenwerkingsmodi in?", "Wat houdt X in"),
        ("What does The Explorer entail?", "What does X entail"),
        ("Hoe werkt Compliance Hub?", "Hoe werkt X (terminal ?)"),
        ("How does Validation work?", "How does X work (terminal ?)"),
    ]

    GOOD_ANSWERS: list[str] = [
        "Welke documenten moet ik aanleveren voor Gate 2?",
        "How do I classify the risk level of my AI system?",
        "Wanneer is de validatiefase succesvol afgerond?",
        "Who decides the Go/No-Go in a gate review?",
        "Hoe bereid ik een Gate 3 review voor?",
        "Which templates are required for phase 3?",
        "Wat zijn de verplichte opleveringen voor Gate 1?",
        "What are the required deliverables at Gate 4?",
        "Wie is verantwoordelijk voor de risico-assessment?",
        "When should I escalate to the Guardian?",
    ]

    @pytest.fixture(autouse=True)
    def import_check_fn(self):
        import validate_docs as vd
        self.check = vd.check_answers_quality

    @pytest.mark.parametrize("answer,label", BAD_ANSWERS)
    def test_rejects_generic_answer(self, answer: str, label: str) -> None:
        errors = self.check([answer, "Welke documenten voor Gate 2?"])
        assert errors, f"[{label}] Should have rejected: {answer!r}"

    @pytest.mark.parametrize("good", GOOD_ANSWERS)
    def test_accepts_specific_answer(self, good: str) -> None:
        errors = self.check([good, "Welke rollen zijn verplicht?"])
        assert not errors, f"Should have accepted: {good!r} — got: {errors}"

    def test_requires_minimum_two_answers(self) -> None:
        errors = self.check(["Welke documenten voor Gate 2?"])
        assert any("2" in e or "minimaal" in e.lower() or "minimum" in e.lower() for e in errors), (
            f"Expected minimum-2 error, got: {errors}"
        )

    def test_two_good_answers_pass(self) -> None:
        errors = self.check([
            "Welke documenten moet ik aanleveren voor Gate 2?",
            "Wanneer is de validatiefase afgerond?",
        ])
        assert not errors

    def test_one_bad_among_two_fails(self) -> None:
        errors = self.check([
            "Welke documenten voor Gate 2?",
            "Wat is Gate Review?",
        ])
        assert errors

    def test_error_names_offending_answer(self) -> None:
        bad = "Wat is Gate Review?"
        errors = self.check([bad, "Welke documenten voor Gate 2?"])
        assert any("Wat is Gate Review" in e for e in errors), (
            f"Expected error mentioning the answer, got: {errors}"
        )

    def test_empty_list_counts_as_too_few(self) -> None:
        errors = self.check([])
        assert errors

    def test_returns_list_of_strings(self) -> None:
        result = self.check(["Wat is X?", "Welke documenten voor Gate 2?"])
        assert isinstance(result, list)
        assert all(isinstance(e, str) for e in result)
