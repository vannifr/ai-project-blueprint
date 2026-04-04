"""QW3 — Docstring quality tests for MCP tools.

Agents rely on docstrings for tool-discovery and selection.
These tests enforce minimum quality standards across all 31 tools.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

SERVER_SRC = Path(__file__).resolve().parent.parent / "src" / "blueprint_mcp" / "server.py"


def _get_tool_docstrings() -> dict[str, str]:
    """Parse server.py and return {tool_name: docstring} for all @mcp.tool() functions."""
    src = SERVER_SRC.read_text(encoding="utf-8")
    tree = ast.parse(src)
    tools: dict[str, str] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        for dec in node.decorator_list:
            is_tool = (
                isinstance(dec, ast.Call) and hasattr(dec.func, "attr") and dec.func.attr == "tool"
            )
            if is_tool:
                tools[node.name] = ast.get_docstring(node) or ""
    return tools


def _get_tool_signatures() -> dict[str, list[str]]:
    """Return {tool_name: [param_names]} excluding 'self' and 'output_format'."""
    src = SERVER_SRC.read_text(encoding="utf-8")
    tree = ast.parse(src)
    sigs: dict[str, list[str]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        for dec in node.decorator_list:
            is_tool = (
                isinstance(dec, ast.Call) and hasattr(dec.func, "attr") and dec.func.attr == "tool"
            )
            if is_tool:
                params = [a.arg for a in node.args.args if a.arg not in ("self", "output_format")]
                sigs[node.name] = params
    return sigs


TOOLS = _get_tool_docstrings()
SIGS = _get_tool_signatures()
TOOL_NAMES = list(TOOLS.keys())


# ── Completeness — every tool has a non-trivial docstring ────────────────────


class TestDocstringPresence:
    @pytest.mark.parametrize("name", TOOL_NAMES)
    def test_tool_has_docstring(self, name):
        assert TOOLS[name], f"{name}: missing docstring"

    @pytest.mark.parametrize("name", TOOL_NAMES)
    def test_docstring_min_length(self, name):
        doc = TOOLS[name]
        assert len(doc) >= 80, (
            f"{name}: docstring too short ({len(doc)} chars < 80). " f"Current: {doc!r}"
        )


# ── Args section — tools with params must document them ──────────────────────


class TestArgsSection:
    EXEMPT = {"reload_content"}  # no meaningful params beyond output_format

    @pytest.mark.parametrize("name", TOOL_NAMES)
    def test_tools_with_params_have_args_section(self, name):
        if name in self.EXEMPT:
            return
        params = SIGS.get(name, [])
        if not params:
            return  # no non-trivial params → skip
        doc = TOOLS[name]
        assert "Args:" in doc, f"{name}: has params {params} but no 'Args:' section in docstring"


# ── Workflow guidance — key workflow tools document the next step ─────────────


# Tools that are part of a defined workflow must state what comes next
WORKFLOW_TOOLS = {
    "answer_question",
    "check_gate_readiness",
    "classify_risk",
    "can_enter_phase",
    "gate_review_intake",
    "gate_review_report",
    "project_setup_intake",
    "project_setup_risk",
    "project_setup_charter",
    "compliance_intake",
    "compliance_checklist",
    "get_phase_guidance",
    "get_guidance_for_profile",
    "validate_project_context",
    "session_start",
    "session_get_state",
}


class TestWorkflowGuidance:
    @pytest.mark.parametrize("name", sorted(WORKFLOW_TOOLS))
    def test_workflow_tool_mentions_next_step(self, name):
        doc = TOOLS.get(name, "").lower()
        has_next = any(
            kw in doc for kw in ("next", "then call", "follow", "step", "proceed", "after")
        )
        assert has_next, (
            f"{name}: workflow tool should mention what comes next. "
            f"Add 'next step' or 'call X after this' guidance."
        )


# ── Specific tools that were critically weak ──────────────────────────────────


class TestCriticallyWeakTools:
    def test_can_enter_phase_has_args(self):
        doc = TOOLS["can_enter_phase"]
        assert "Args:" in doc
        assert "phase" in doc.lower()
        assert "gate" in doc.lower()

    def test_get_workflow_status_explains_purpose(self):
        doc = TOOLS["get_workflow_status"]
        assert len(doc) >= 120
        assert any(kw in doc.lower() for kw in ("workflow", "tool", "available"))

    def test_validate_project_context_has_args(self):
        doc = TOOLS["validate_project_context"]
        assert "Args:" in doc
        assert "data" in doc.lower()

    def test_get_template_mentions_next(self):
        doc = TOOLS.get("get_template", "").lower()
        assert any(kw in doc for kw in ("fill_template", "next", "then", "follow"))

    def test_list_projects_mentions_next(self):
        doc = TOOLS.get("list_projects", "").lower()
        assert any(kw in doc for kw in ("session_get_state", "next", "then", "follow"))

    def test_lookup_terminology_mentions_next(self):
        doc = TOOLS.get("lookup_terminology", "").lower()
        assert any(kw in doc for kw in ("answer_question", "next", "then", "follow"))

    def test_get_project_type_mentions_next(self):
        doc = TOOLS.get("get_project_type", "").lower()
        assert any(kw in doc for kw in ("classify_risk", "next", "then", "follow"))

    def test_select_collaboration_mode_mentions_next(self):
        doc = TOOLS.get("select_collaboration_mode", "").lower()
        assert any(kw in doc for kw in ("next", "then", "follow", "charter", "setup"))

    def test_session_record_artifact_mentions_next(self):
        doc = TOOLS.get("session_record_artifact", "").lower()
        assert any(kw in doc for kw in ("gate_review", "next", "then", "follow"))
