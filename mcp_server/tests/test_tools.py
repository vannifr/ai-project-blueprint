"""Tests for MCP tools — verify each tool returns expected content."""

import pytest
from pathlib import Path

from blueprint_mcp.content_index import ContentIndex
from blueprint_mcp.server import (
    set_index,
    get_phase_guidance,
    get_template,
    check_gate_readiness,
    classify_risk,
    select_collaboration_mode,
    lookup_terminology,
    get_project_type,
    search_content,
)

DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "docs"


@pytest.fixture(scope="session", autouse=True)
def setup_index():
    """Load index once and set it as the module-level index for all tools."""
    index = ContentIndex.load(DOCS_ROOT, language="en")
    set_index(index)
    yield
    set_index(None)


class TestGetPhaseGuidance:
    def test_phase_1_objectives(self):
        result = get_phase_guidance(1, "objectives")
        assert len(result) > 100

    def test_phase_3_activities(self):
        result = get_phase_guidance(3, "activities")
        assert len(result) > 50

    def test_invalid_phase(self):
        result = get_phase_guidance(0, "objectives")
        assert "Error" in result

    def test_invalid_aspect(self):
        result = get_phase_guidance(1, "invalid")
        assert "Error" in result


class TestGetTemplate:
    def test_find_gate_review(self):
        result = get_template("gate-review")
        assert "gate" in result.lower() or "Gate" in result

    def test_find_privacy(self):
        result = get_template("privacy")
        assert len(result) > 50

    def test_not_found_lists_available(self):
        result = get_template("nonexistent-xyz-template")
        assert "not found" in result.lower() or "Available" in result


class TestCheckGateReadiness:
    def test_gate_1(self):
        evidence = ["project charter", "risk scan"]
        result = check_gate_readiness(1, evidence)
        assert "Gate 1" in result
        assert "project charter" in result
        assert "risk scan" in result

    def test_invalid_gate(self):
        result = check_gate_readiness(0, [])
        assert "Error" in result


class TestClassifyRisk:
    def test_returns_framework(self):
        result = classify_risk("A chatbot that answers HR questions")
        assert "chatbot" in result.lower() or "risk" in result.lower()
        assert len(result) > 200


class TestSelectCollaborationMode:
    def test_returns_framework(self):
        result = select_collaboration_mode("low", "high")
        assert "low" in result.lower()
        assert len(result) > 200


class TestLookupTerminology:
    def test_known_term(self):
        result = lookup_terminology("guardian")
        assert "guardian" in result.lower() or "Guardian" in result

    def test_unknown_term(self):
        result = lookup_terminology("xyznonexistent")
        assert len(result) > 0


class TestGetProjectType:
    def test_returns_framework(self):
        result = get_project_type("An email classification system using ML")
        assert len(result) > 100


class TestSearchContent:
    def test_search_risk(self):
        result = search_content("risk")
        assert "risk" in result.lower()

    def test_search_with_filters(self):
        result = search_content("", type="template")
        assert "template" in result.lower()

    def test_no_results(self):
        result = search_content("xyznonexistent12345")
        assert "No results" in result
