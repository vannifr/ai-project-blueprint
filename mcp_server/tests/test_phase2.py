"""Phase 2 tests: JSON output mode (IMP1), evidence schema (IMP3),
get_guidance_for_profile (IMP4), select_template (IMP5)."""

import json
from pathlib import Path

import pytest

from blueprint_mcp.content_index import ContentIndex
from blueprint_mcp.response_utils import (
    DecisionStatus,
    build_decision,
    format_response,
    wrap_response,
)
from blueprint_mcp.server import set_index

DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "docs"


@pytest.fixture(scope="module", autouse=True)
def _load_index():
    idx = ContentIndex.load(DOCS_ROOT, language="en")
    set_index(idx)
    yield
    set_index(None)


def _extract_json(result: str) -> dict:
    assert "```json" in result, f"No JSON block in:\n{result[:300]}"
    return json.loads(result.split("```json\n")[1].split("\n```")[0])


# ── IMP1: format_response / JSON output mode ──────────────────────────────────


class TestFormatResponse:
    """format_response(markdown, decision, output_format) replaces wrap_response."""

    def _decision(self, **kwargs):
        defaults = {
            "tool": "my_tool",
            "status": DecisionStatus.OK,
            "primary_action": "Do it",
            "data": {},
        }
        defaults.update(kwargs)
        return build_decision(
            defaults["tool"], defaults["status"], defaults["primary_action"], defaults["data"]
        )

    def test_markdown_mode_same_as_wrap_response(self):
        d = self._decision()
        assert format_response("hello", d, "markdown") == wrap_response("hello", d)

    def test_markdown_is_default(self):
        d = self._decision()
        assert format_response("hello", d) == wrap_response("hello", d)

    def test_json_mode_returns_only_json(self):
        d = self._decision(tool="search_content", data={"result_count": 3})
        result = format_response("some markdown prose", d, "json")
        parsed = json.loads(result)
        assert parsed["tool"] == "search_content"
        assert parsed["data"]["result_count"] == 3

    def test_json_mode_no_markdown_present(self):
        d = self._decision()
        result = format_response("## Lots of markdown", d, "json")
        assert "##" not in result
        assert "Lots of markdown" not in result

    def test_json_mode_valid_json_string(self):
        d = self._decision(data={"gate": 2, "gaps": ["missing doc"]})
        result = format_response("ignored", d, "json")
        parsed = json.loads(result)
        assert parsed["data"]["gaps"] == ["missing doc"]

    def test_invalid_format_raises_value_error(self):
        d = self._decision()
        with pytest.raises(ValueError, match="output_format"):
            format_response("text", d, "xml")

    def test_json_mode_includes_all_decision_keys(self):
        d = build_decision(
            "check_gate_readiness", DecisionStatus.OK, "action", {"gate": 1}, "gate_review_report"
        )
        result = format_response("text", d, "json")
        parsed = json.loads(result)
        assert set(parsed.keys()) == {"tool", "status", "primary_action", "data", "next_tool"}


class TestToolsAcceptOutputFormat:
    """Tools pass output_format through to format_response."""

    def test_get_phase_guidance_json_mode(self):
        from blueprint_mcp.server import get_phase_guidance

        result = get_phase_guidance(1, "objectives", output_format="json")
        parsed = json.loads(result)
        assert parsed["tool"] == "get_phase_guidance"
        assert "```json" not in result  # no markdown wrapper

    def test_search_content_json_mode(self):
        from blueprint_mcp.server import search_content

        result = search_content("risk", output_format="json")
        parsed = json.loads(result)
        assert "result_count" in parsed["data"]

    def test_check_gate_readiness_json_mode(self):
        from blueprint_mcp.server import check_gate_readiness

        result = check_gate_readiness(1, ["charter"], output_format="json")
        parsed = json.loads(result)
        assert parsed["data"]["gate"] == 1

    def test_can_enter_phase_json_mode(self):
        from blueprint_mcp.server import can_enter_phase

        result = can_enter_phase(2, [1], output_format="json")
        parsed = json.loads(result)
        assert parsed["data"]["can_enter"] is True

    def test_markdown_mode_still_works(self):
        from blueprint_mcp.server import get_phase_guidance

        result = get_phase_guidance(1, "objectives", output_format="markdown")
        assert "```json" in result

    def test_default_is_markdown(self):
        from blueprint_mcp.server import get_phase_guidance

        result_default = get_phase_guidance(1, "objectives")
        result_md = get_phase_guidance(1, "objectives", output_format="markdown")
        assert result_default == result_md


# ── IMP3: Evidence schema ─────────────────────────────────────────────────────


class TestEvidenceType:
    def test_evidence_type_constants_exist(self):
        from blueprint_mcp.evidence import EvidenceType

        assert EvidenceType.DOCUMENT == "document"
        assert EvidenceType.TEST_RESULT == "test_result"
        assert EvidenceType.REVIEW_SIGN_OFF == "review_sign_off"
        assert EvidenceType.ARTIFACT == "artifact"

    def test_evidence_item_dataclass(self):
        from blueprint_mcp.evidence import EvidenceItem

        e = EvidenceItem(title="Project Charter", type="document", gate=1)
        assert e.title == "Project Charter"
        assert e.gate == 1
        assert e.quality_score is None

    def test_evidence_item_with_quality_score(self):
        from blueprint_mcp.evidence import EvidenceItem

        e = EvidenceItem(title="Golden set", type="test_result", gate=2, quality_score=0.9)
        assert e.quality_score == 0.9

    def test_parse_evidence_list_strings(self):
        from blueprint_mcp.evidence import parse_evidence

        items = parse_evidence(["project charter", "risk scan"], gate=1)
        assert len(items) == 2
        assert all(i.gate == 1 for i in items)

    def test_parse_evidence_infers_type_from_keyword(self):
        from blueprint_mcp.evidence import parse_evidence

        items = parse_evidence(["test results", "sign-off"], gate=2)
        types = {i.type for i in items}
        assert "test_result" in types
        assert "review_sign_off" in types

    def test_parse_evidence_defaults_to_document(self):
        from blueprint_mcp.evidence import parse_evidence

        items = parse_evidence(["project charter"], gate=1)
        assert items[0].type == "document"

    def test_evidence_summary_dict(self):
        from blueprint_mcp.evidence import EvidenceItem, evidence_summary

        items = [
            EvidenceItem("Charter", "document", 1),
            EvidenceItem("Test results", "test_result", 1),
        ]
        summary = evidence_summary(items)
        assert summary["count"] == 2
        assert "document" in summary["by_type"]

    def test_gate_review_intake_uses_evidence_schema(self):
        from blueprint_mcp.server import gate_review_intake

        result = gate_review_intake(1, ["project charter", "risk scan"])
        parsed = _extract_json(result)
        assert "evidence_summary" in parsed["data"]
        assert parsed["data"]["evidence_summary"]["count"] == 2

    def test_gate_review_report_uses_evidence_schema(self):
        from blueprint_mcp.server import gate_review_report

        result = gate_review_report(1, ["project charter"], [])
        parsed = _extract_json(result)
        assert "evidence_summary" in parsed["data"]
        assert parsed["data"]["ready"] is True


# ── IMP4: get_guidance_for_profile ────────────────────────────────────────────


class TestGetGuidanceForProfile:
    def test_returns_non_empty_result(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("A", "green", 1)
        assert len(result) > 100

    def test_decision_block_present(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("A", "green", 1)
        parsed = _extract_json(result)
        assert parsed["tool"] == "get_guidance_for_profile"

    def test_decision_data_has_expected_keys(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("B", "amber", 2)
        parsed = _extract_json(result)
        data = parsed["data"]
        assert "project_type" in data
        assert "risk_level" in data
        assert "phase" in data
        assert "doc_count" in data

    def test_filters_by_project_type(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result_a = get_guidance_for_profile("A", "green", 1)
        result_b = get_guidance_for_profile("B", "green", 1)
        # Both should return results but may differ
        assert len(result_a) > 50
        assert len(result_b) > 50

    def test_invalid_project_type_returns_error(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("C", "green", 1)
        parsed = _extract_json(result)
        assert parsed["status"] == "error"

    def test_invalid_risk_level_returns_error(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("A", "purple", 1)
        parsed = _extract_json(result)
        assert parsed["status"] == "error"

    def test_invalid_phase_returns_error(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("A", "green", 9)
        parsed = _extract_json(result)
        assert parsed["status"] == "error"

    def test_optional_role_filter(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("A", "green", 1, role="Guardian")
        assert len(result) > 50

    def test_json_mode(self):
        from blueprint_mcp.server import get_guidance_for_profile

        result = get_guidance_for_profile("A", "green", 1, output_format="json")
        parsed = json.loads(result)
        assert parsed["tool"] == "get_guidance_for_profile"


# ── IMP5: select_template ─────────────────────────────────────────────────────


class TestSelectTemplate:
    def test_returns_non_empty_result(self):
        from blueprint_mcp.server import select_template

        result = select_template("gate review")
        assert len(result) > 50

    def test_decision_block_present(self):
        from blueprint_mcp.server import select_template

        result = select_template("gate review")
        parsed = _extract_json(result)
        assert parsed["tool"] == "select_template"

    def test_decision_data_has_expected_keys(self):
        from blueprint_mcp.server import select_template

        result = select_template("project charter")
        parsed = _extract_json(result)
        data = parsed["data"]
        assert "goal" in data
        assert "match_count" in data

    def test_finds_relevant_template(self):
        from blueprint_mcp.server import select_template

        result = select_template("project charter")
        assert "charter" in result.lower() or "project" in result.lower()

    def test_no_match_returns_not_found(self):
        from blueprint_mcp.server import select_template

        result = select_template("xyznonexistentgoal12345")
        parsed = _extract_json(result)
        assert parsed["status"] == "not_found"

    def test_phase_filter(self):
        from blueprint_mcp.server import select_template

        result = select_template("template", phase=1)
        parsed = _extract_json(result)
        assert parsed["status"] in ("ok", "not_found")

    def test_role_filter(self):
        from blueprint_mcp.server import select_template

        result = select_template("template", role="Guardian")
        assert len(result) > 50

    def test_json_mode(self):
        from blueprint_mcp.server import select_template

        result = select_template("gate review", output_format="json")
        parsed = json.loads(result)
        assert parsed["tool"] == "select_template"
