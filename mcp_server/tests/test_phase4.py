"""Phase 4 — Quality & Customisation tests (TDD: red first, then green).

Covers:
  IMP6 — Confidence scoring on search/answer results
  IMP9 — Template customisation API (fill placeholders, list placeholders)
  IMP7 — Frontmatter enrichment utilities (last_reviewed, decision_framework)
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest


# ── Helpers ───────────────────────────────────────────────────────────────────


def _extract_json(result: str) -> dict:
    assert "```json" in result, f"No JSON block in: {result!r}"
    return json.loads(result.split("```json\n")[1].split("\n```")[0])


# ── IMP6: ConfidenceScorer ────────────────────────────────────────────────────


class TestConfidenceScorerImport:
    def test_confidence_scorer_importable(self):
        from blueprint_mcp.confidence import ConfidenceScorer  # noqa: F401

    def test_score_result_importable(self):
        from blueprint_mcp.confidence import score_result  # noqa: F401


class TestConfidenceScorerBasic:
    @pytest.fixture
    def scorer(self):
        from blueprint_mcp.confidence import ConfidenceScorer
        return ConfidenceScorer()

    def test_score_returns_float(self, scorer):
        score = scorer.score(query="risk classification", title="Risk Framework", body="Classify risk levels.")
        assert isinstance(score, float)

    def test_score_is_between_0_and_1(self, scorer):
        score = scorer.score(query="risk classification", title="Risk Framework", body="Classify risk levels.")
        assert 0.0 <= score <= 1.0

    def test_exact_title_match_scores_higher(self, scorer):
        high = scorer.score(query="risk classification", title="Risk Classification", body="Some text.")
        low = scorer.score(query="risk classification", title="Unrelated Topic", body="Some text.")
        assert high > low

    def test_keyword_in_body_raises_score(self, scorer):
        with_kw = scorer.score(query="gate review", title="Process", body="The gate review is important.")
        without_kw = scorer.score(query="gate review", title="Process", body="Nothing relevant here.")
        assert with_kw > without_kw

    def test_empty_query_scores_zero(self, scorer):
        score = scorer.score(query="", title="Any Title", body="Some body text.")
        assert score == 0.0

    def test_empty_title_and_body_scores_zero_or_low(self, scorer):
        score = scorer.score(query="risk", title="", body="")
        assert score == 0.0

    def test_multiple_keyword_occurrences_score_higher(self, scorer):
        single = scorer.score(query="risk", title="Risk", body="One risk mention.")
        multiple = scorer.score(query="risk", title="Risk", body="Risk, risk, and more risk assessment.")
        assert multiple >= single

    def test_answers_boost_score(self, scorer):
        with_answer = scorer.score(
            query="how to classify risk",
            title="Risk",
            body="General info.",
            answers=["How to classify risk?", "What are risk levels?"],
        )
        without_answer = scorer.score(
            query="how to classify risk",
            title="Risk",
            body="General info.",
            answers=[],
        )
        assert with_answer > without_answer


class TestScoreResultFunction:
    """score_result() is a convenience wrapper around ConfidenceScorer."""

    def test_score_result_takes_doc_and_query(self):
        from blueprint_mcp.confidence import score_result
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        doc = idx.docs[0]
        result = score_result(query="risk", doc=doc)
        assert isinstance(result, float)
        assert 0.0 <= result <= 1.0


class TestSearchContentConfidence:
    """search_content decision data includes confidence_scores."""

    @pytest.fixture(autouse=True)
    def _load_index(self):
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import set_index
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        set_index(ContentIndex.load(docs_root, language="en"))

    def test_search_content_decision_has_confidence_scores(self):
        from blueprint_mcp.server import search_content
        result = search_content("risk classification")
        parsed = _extract_json(result)
        assert "confidence_scores" in parsed["data"]

    def test_confidence_scores_is_list(self):
        from blueprint_mcp.server import search_content
        result = search_content("risk")
        parsed = _extract_json(result)
        assert isinstance(parsed["data"]["confidence_scores"], list)

    def test_confidence_scores_are_floats_between_0_and_1(self):
        from blueprint_mcp.server import search_content
        result = search_content("gate review")
        parsed = _extract_json(result)
        for s in parsed["data"]["confidence_scores"]:
            assert 0.0 <= s <= 1.0


class TestAnswerQuestionConfidence:
    """answer_question decision data includes top_confidence."""

    @pytest.fixture(autouse=True)
    def _load_index(self):
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import set_index, set_semantic_index
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        set_index(ContentIndex.load(docs_root, language="en"))
        set_semantic_index(None)

    def test_answer_question_decision_has_top_confidence(self):
        from blueprint_mcp.server import answer_question
        result = answer_question("How do I classify risk?")
        parsed = _extract_json(result)
        assert "top_confidence" in parsed["data"]

    def test_top_confidence_is_float_between_0_and_1(self):
        from blueprint_mcp.server import answer_question
        result = answer_question("risk classification")
        parsed = _extract_json(result)
        val = parsed["data"]["top_confidence"]
        assert isinstance(val, float)
        assert 0.0 <= val <= 1.0


# ── IMP9: Template customisation API ─────────────────────────────────────────


class TestPlaceholderParserImport:
    def test_parse_placeholders_importable(self):
        from blueprint_mcp.template_engine import parse_placeholders  # noqa: F401

    def test_fill_placeholders_importable(self):
        from blueprint_mcp.template_engine import fill_placeholders  # noqa: F401


class TestParsePlaceholders:
    def test_finds_double_brace_placeholders(self):
        from blueprint_mcp.template_engine import parse_placeholders
        text = "Hello {{name}}, your project is {{project}}."
        result = parse_placeholders(text)
        assert set(result) == {"name", "project"}

    def test_no_placeholders_returns_empty(self):
        from blueprint_mcp.template_engine import parse_placeholders
        assert parse_placeholders("No placeholders here.") == []

    def test_duplicate_placeholders_deduped(self):
        from blueprint_mcp.template_engine import parse_placeholders
        text = "{{name}} and {{name}} again."
        result = parse_placeholders(text)
        assert result.count("name") == 1

    def test_single_brace_ignored(self):
        from blueprint_mcp.template_engine import parse_placeholders
        result = parse_placeholders("{not_a_placeholder}")
        assert result == []

    def test_placeholder_names_stripped(self):
        from blueprint_mcp.template_engine import parse_placeholders
        result = parse_placeholders("{{ name }}")
        assert "name" in result


class TestFillPlaceholders:
    def test_fills_all_values(self):
        from blueprint_mcp.template_engine import fill_placeholders
        text = "Project: {{project_name}}, Type: {{project_type}}"
        filled, missing = fill_placeholders(text, {"project_name": "Atlas", "project_type": "NLP"})
        assert "Atlas" in filled
        assert "NLP" in filled
        assert missing == []

    def test_unfilled_placeholders_in_missing(self):
        from blueprint_mcp.template_engine import fill_placeholders
        text = "Hello {{name}}, your role is {{role}}."
        filled, missing = fill_placeholders(text, {"name": "Anna"})
        assert "Anna" in filled
        assert "role" in missing

    def test_extra_values_ignored(self):
        from blueprint_mcp.template_engine import fill_placeholders
        text = "Hello {{name}}."
        filled, missing = fill_placeholders(text, {"name": "Bob", "unused": "x"})
        assert filled == "Hello Bob."
        assert missing == []

    def test_empty_values_dict_all_missing(self):
        from blueprint_mcp.template_engine import fill_placeholders
        text = "{{a}} and {{b}}"
        filled, missing = fill_placeholders(text, {})
        assert set(missing) == {"a", "b"}

    def test_no_placeholders_unchanged(self):
        from blueprint_mcp.template_engine import fill_placeholders
        text = "No placeholders."
        filled, missing = fill_placeholders(text, {"x": "y"})
        assert filled == text
        assert missing == []


class TestListTemplatePlaceholdersTool:
    @pytest.fixture(autouse=True)
    def _load_index(self):
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import set_index
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        set_index(ContentIndex.load(docs_root, language="en"))

    def test_list_template_placeholders_importable(self):
        from blueprint_mcp.server import list_template_placeholders  # noqa: F401

    def test_list_template_placeholders_returns_string(self):
        from blueprint_mcp.server import list_template_placeholders
        # Use a template that exists — get first template from index
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        templates = [d for d in idx.docs if d.type == "template"]
        if not templates:
            pytest.skip("No templates found in index")
        result = list_template_placeholders(templates[0].path)
        assert isinstance(result, str)

    def test_list_template_placeholders_decision_block(self):
        from blueprint_mcp.server import list_template_placeholders
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        templates = [d for d in idx.docs if d.type == "template"]
        if not templates:
            pytest.skip("No templates found in index")
        result = list_template_placeholders(templates[0].path)
        parsed = _extract_json(result)
        assert parsed["tool"] == "list_template_placeholders"
        assert "placeholders" in parsed["data"]

    def test_list_template_placeholders_unknown_returns_not_found(self):
        from blueprint_mcp.server import list_template_placeholders
        result = list_template_placeholders("nonexistent/template.md")
        parsed = _extract_json(result)
        assert parsed["status"] == "not_found"

    def test_list_template_placeholders_json_mode(self):
        from blueprint_mcp.server import list_template_placeholders
        result = list_template_placeholders("nonexistent/template.md", output_format="json")
        parsed = json.loads(result)
        assert parsed["tool"] == "list_template_placeholders"


class TestFillTemplateTool:
    @pytest.fixture(autouse=True)
    def _load_index(self):
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import set_index
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        set_index(ContentIndex.load(docs_root, language="en"))

    def test_fill_template_importable(self):
        from blueprint_mcp.server import fill_template  # noqa: F401

    def test_fill_template_unknown_returns_not_found(self):
        from blueprint_mcp.server import fill_template
        result = fill_template("nonexistent/template.md", values={})
        parsed = _extract_json(result)
        assert parsed["status"] == "not_found"

    def test_fill_template_decision_block(self):
        from blueprint_mcp.server import fill_template
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        templates = [d for d in idx.docs if d.type == "template"]
        if not templates:
            pytest.skip("No templates found in index")
        result = fill_template(templates[0].path, values={})
        parsed = _extract_json(result)
        assert parsed["tool"] == "fill_template"
        assert "filled_content" in parsed["data"]
        assert "missing_placeholders" in parsed["data"]

    def test_fill_template_values_applied(self):
        from blueprint_mcp.server import fill_template
        from pathlib import Path
        from blueprint_mcp.content_index import ContentIndex
        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        templates = [d for d in idx.docs if d.type == "template"]
        if not templates:
            pytest.skip("No templates found in index")
        # Pass many plausible values; at minimum the tool should not raise
        values = {
            "project_name": "TestProject",
            "team": "Team Alpha",
            "date": "2026-04-04",
        }
        result = fill_template(templates[0].path, values=values)
        parsed = _extract_json(result)
        assert parsed["status"] == "ok"

    def test_fill_template_json_mode(self):
        from blueprint_mcp.server import fill_template
        result = fill_template("nonexistent/template.md", values={}, output_format="json")
        parsed = json.loads(result)
        assert parsed["tool"] == "fill_template"


# ── IMP7: Frontmatter enrichment utilities ────────────────────────────────────


class TestFrontmatterEnricherImport:
    def test_parse_frontmatter_importable(self):
        from blueprint_mcp.frontmatter_utils import parse_frontmatter  # noqa: F401

    def test_update_frontmatter_importable(self):
        from blueprint_mcp.frontmatter_utils import update_frontmatter  # noqa: F401

    def test_render_frontmatter_importable(self):
        from blueprint_mcp.frontmatter_utils import render_frontmatter  # noqa: F401


class TestParseFrontmatter:
    def test_parses_simple_yaml(self):
        from blueprint_mcp.frontmatter_utils import parse_frontmatter
        text = "---\ntitle: My Doc\ntype: guide\n---\n\n# Body"
        meta, body = parse_frontmatter(text)
        assert meta["title"] == "My Doc"
        assert meta["type"] == "guide"
        assert "# Body" in body

    def test_no_frontmatter_returns_empty_meta(self):
        from blueprint_mcp.frontmatter_utils import parse_frontmatter
        text = "# Just a heading\n\nSome content."
        meta, body = parse_frontmatter(text)
        assert meta == {}
        assert "# Just a heading" in body

    def test_body_without_leading_newline(self):
        from blueprint_mcp.frontmatter_utils import parse_frontmatter
        text = "---\ntitle: X\n---\n# Body"
        meta, body = parse_frontmatter(text)
        assert "# Body" in body

    def test_frontmatter_with_list_value(self):
        from blueprint_mcp.frontmatter_utils import parse_frontmatter
        text = "---\ntags: [a, b, c]\n---\n# Content"
        meta, body = parse_frontmatter(text)
        assert meta["tags"] == ["a", "b", "c"]


class TestUpdateFrontmatter:
    def test_adds_new_key(self):
        from blueprint_mcp.frontmatter_utils import update_frontmatter
        meta = {"title": "Doc"}
        updated = update_frontmatter(meta, {"last_reviewed": "2026-04-04"})
        assert updated["last_reviewed"] == "2026-04-04"
        assert updated["title"] == "Doc"  # existing key preserved

    def test_overwrites_existing_key(self):
        from blueprint_mcp.frontmatter_utils import update_frontmatter
        meta = {"last_reviewed": "2025-01-01"}
        updated = update_frontmatter(meta, {"last_reviewed": "2026-04-04"})
        assert updated["last_reviewed"] == "2026-04-04"

    def test_empty_updates_unchanged(self):
        from blueprint_mcp.frontmatter_utils import update_frontmatter
        meta = {"title": "Doc"}
        updated = update_frontmatter(meta, {})
        assert updated == meta

    def test_original_not_mutated(self):
        from blueprint_mcp.frontmatter_utils import update_frontmatter
        meta = {"title": "Doc"}
        update_frontmatter(meta, {"new_key": "value"})
        assert "new_key" not in meta


class TestRenderFrontmatter:
    def test_round_trip(self):
        from blueprint_mcp.frontmatter_utils import parse_frontmatter, render_frontmatter
        original = "---\ntitle: My Doc\ntype: guide\n---\n\n# Body\n\nContent here."
        meta, body = parse_frontmatter(original)
        rendered = render_frontmatter(meta, body)
        re_meta, re_body = parse_frontmatter(rendered)
        assert re_meta["title"] == "My Doc"
        assert re_meta["type"] == "guide"
        assert "# Body" in re_body

    def test_renders_yaml_fence(self):
        from blueprint_mcp.frontmatter_utils import render_frontmatter
        rendered = render_frontmatter({"title": "X"}, "# Body")
        assert rendered.startswith("---\n")
        assert "---" in rendered
        assert "title:" in rendered

    def test_empty_meta_renders_no_fence(self):
        from blueprint_mcp.frontmatter_utils import render_frontmatter
        rendered = render_frontmatter({}, "# Body\n")
        assert not rendered.startswith("---")
        assert "# Body" in rendered


class TestEnrichFrontmatterScript:
    """The enrichment function reads a file and adds missing keys."""

    def test_enrich_file_importable(self):
        from blueprint_mcp.frontmatter_utils import enrich_file  # noqa: F401

    def test_enrich_file_adds_last_reviewed(self, tmp_path):
        from blueprint_mcp.frontmatter_utils import enrich_file
        md = tmp_path / "doc.md"
        md.write_text("---\ntitle: Test\n---\n\n# Content\n")
        changed = enrich_file(md, updates={"last_reviewed": "2026-04-04"})
        assert changed is True
        content = md.read_text()
        assert "last_reviewed: '2026-04-04'" in content or "last_reviewed: 2026-04-04" in content

    def test_enrich_file_no_change_when_key_exists(self, tmp_path):
        from blueprint_mcp.frontmatter_utils import enrich_file
        md = tmp_path / "doc.md"
        md.write_text("---\ntitle: Test\nlast_reviewed: '2025-01-01'\n---\n\n# Content\n")
        changed = enrich_file(md, updates={"last_reviewed": "2026-04-04"}, overwrite=False)
        assert changed is False
        content = md.read_text()
        assert "2025-01-01" in content  # original preserved

    def test_enrich_file_overwrite_true_updates_key(self, tmp_path):
        from blueprint_mcp.frontmatter_utils import enrich_file
        md = tmp_path / "doc.md"
        md.write_text("---\ntitle: Test\nlast_reviewed: '2025-01-01'\n---\n\n# Content\n")
        changed = enrich_file(md, updates={"last_reviewed": "2026-04-04"}, overwrite=True)
        assert changed is True
        content = md.read_text()
        assert "2026-04-04" in content

    def test_enrich_file_adds_decision_framework(self, tmp_path):
        from blueprint_mcp.frontmatter_utils import enrich_file
        md = tmp_path / "doc.md"
        md.write_text("---\ntitle: Risk Guide\ntype: guide\n---\n\n# Risk\n")
        enrich_file(md, updates={"decision_framework": "risk-based"})
        content = md.read_text()
        assert "decision_framework" in content

    def test_enrich_file_no_frontmatter_creates_it(self, tmp_path):
        from blueprint_mcp.frontmatter_utils import enrich_file
        md = tmp_path / "doc.md"
        md.write_text("# Just a heading\n\nBody text.\n")
        changed = enrich_file(md, updates={"last_reviewed": "2026-04-04"})
        assert changed is True
        content = md.read_text()
        assert "---" in content
        assert "last_reviewed" in content
