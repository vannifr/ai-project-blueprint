"""Tests for response_utils — structured decision dict alongside markdown."""

import json

import pytest

from blueprint_mcp.response_utils import (
    DecisionStatus,
    build_decision,
    wrap_response,
)

# ── build_decision ────────────────────────────────────────────────────────────


class TestBuildDecision:
    def test_returns_dict_with_all_required_keys(self):
        d = build_decision("my_tool", DecisionStatus.OK, "Proceed to next step", {})
        assert set(d.keys()) == {"tool", "status", "primary_action", "data", "next_tool"}

    def test_ok_status(self):
        d = build_decision("check_gate_readiness", DecisionStatus.OK, "All good", {"gate": 1})
        assert d["status"] == "ok"
        assert d["tool"] == "check_gate_readiness"
        assert d["primary_action"] == "All good"
        assert d["data"] == {"gate": 1}
        assert d["next_tool"] is None

    def test_error_status(self):
        d = build_decision(
            "get_phase_guidance", DecisionStatus.ERROR, "Fix the input", {}, next_tool=None
        )
        assert d["status"] == "error"
        assert d["next_tool"] is None

    def test_not_found_status(self):
        d = build_decision("get_template", DecisionStatus.NOT_FOUND, "Template missing", {})
        assert d["status"] == "not_found"

    def test_next_tool_populated(self):
        d = build_decision(
            "project_setup_intake",
            DecisionStatus.OK,
            "Run risk scan",
            {},
            next_tool="project_setup_risk",
        )
        assert d["next_tool"] == "project_setup_risk"

    def test_data_dict_preserved(self):
        data = {"gate": 2, "evidence_count": 3, "gaps": ["missing charter"]}
        d = build_decision("check_gate_readiness", DecisionStatus.OK, "Review gaps", data)
        assert d["data"]["gate"] == 2
        assert d["data"]["gaps"] == ["missing charter"]

    def test_decision_status_values(self):
        assert DecisionStatus.OK == "ok"
        assert DecisionStatus.ERROR == "error"
        assert DecisionStatus.NOT_FOUND == "not_found"


# ── wrap_response ─────────────────────────────────────────────────────────────


class TestWrapResponse:
    def _make_decision(self, **kwargs):
        defaults = {
            "tool": "my_tool",
            "status": DecisionStatus.OK,
            "primary_action": "Do something",
            "data": {},
        }
        defaults.update(kwargs)
        return build_decision(
            defaults["tool"],
            defaults["status"],
            defaults["primary_action"],
            defaults["data"],
        )

    def test_markdown_is_preserved(self):
        result = wrap_response("## Hello\n\nSome content.", self._make_decision())
        assert "## Hello" in result
        assert "Some content." in result

    def test_json_block_appended_at_end(self):
        result = wrap_response("Markdown content", self._make_decision())
        assert result.index("Markdown content") < result.index("```json")

    def test_json_block_is_parseable(self):
        result = wrap_response("text", self._make_decision())
        json_part = result.split("```json\n")[1].split("\n```")[0]
        parsed = json.loads(json_part)
        assert isinstance(parsed, dict)

    def test_json_block_has_all_keys(self):
        decision = self._make_decision(tool="search_content", data={"result_count": 5})
        result = wrap_response("results here", decision)
        json_part = result.split("```json\n")[1].split("\n```")[0]
        parsed = json.loads(json_part)
        assert "tool" in parsed
        assert "status" in parsed
        assert "primary_action" in parsed
        assert "data" in parsed
        assert "next_tool" in parsed

    def test_json_values_correct(self):
        decision = build_decision(
            "classify_risk",
            DecisionStatus.OK,
            "Risk classified",
            {"level": "amber"},
            "project_setup_risk",
        )
        result = wrap_response("risk info", decision)
        json_part = result.split("```json\n")[1].split("\n```")[0]
        parsed = json.loads(json_part)
        assert parsed["tool"] == "classify_risk"
        assert parsed["status"] == "ok"
        assert parsed["data"]["level"] == "amber"
        assert parsed["next_tool"] == "project_setup_risk"

    def test_empty_markdown_still_has_json_block(self):
        result = wrap_response("", self._make_decision())
        assert "```json" in result

    def test_json_block_separator(self):
        result = wrap_response("content", self._make_decision())
        # JSON block must be separated from markdown
        assert "\n\n---\n\n```json" in result


# ── integration: tools return parseable JSON blocks ───────────────────────────


@pytest.fixture(scope="module", autouse=True)
def _load_index():
    """Load the real content index once for all integration tests in this module."""
    from pathlib import Path

    from blueprint_mcp.content_index import ContentIndex
    from blueprint_mcp.server import set_index

    docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
    set_index(ContentIndex.load(docs_root, language="en"))
    yield
    set_index(None)


class TestToolsReturnDecisionBlock:
    """Verify that tool outputs contain a parseable JSON decision block."""

    def _extract_json(self, result: str) -> dict:
        assert "```json" in result, f"No JSON block found in:\n{result[:300]}"
        json_part = result.split("```json\n")[1].split("\n```")[0]
        return json.loads(json_part)

    def test_get_phase_guidance_has_decision_block(self):
        from blueprint_mcp.server import get_phase_guidance

        result = get_phase_guidance(1, "objectives")
        parsed = self._extract_json(result)
        assert parsed["tool"] == "get_phase_guidance"
        assert parsed["status"] in ("ok", "not_found", "error")

    def test_get_template_has_decision_block(self):
        from blueprint_mcp.server import get_template

        result = get_template("gate-review")
        parsed = self._extract_json(result)
        assert parsed["tool"] == "get_template"

    def test_check_gate_readiness_has_decision_block(self):
        from blueprint_mcp.server import check_gate_readiness

        result = check_gate_readiness(1, ["project charter"])
        parsed = self._extract_json(result)
        assert parsed["tool"] == "check_gate_readiness"
        assert "gate" in parsed["data"]

    def test_classify_risk_has_decision_block(self):
        from blueprint_mcp.server import classify_risk

        result = classify_risk("A fraud detection model")
        parsed = self._extract_json(result)
        assert parsed["tool"] == "classify_risk"

    def test_search_content_has_decision_block(self):
        from blueprint_mcp.server import search_content

        result = search_content("risk")
        parsed = self._extract_json(result)
        assert parsed["tool"] == "search_content"
        assert "result_count" in parsed["data"]

    def test_error_response_has_decision_block(self):
        from blueprint_mcp.server import get_phase_guidance

        result = get_phase_guidance(99, "objectives")
        parsed = self._extract_json(result)
        assert parsed["status"] == "error"

    def test_not_found_response_has_decision_block(self):
        from blueprint_mcp.server import get_template

        result = get_template("xyznonexistent12345")
        parsed = self._extract_json(result)
        assert parsed["status"] == "not_found"
