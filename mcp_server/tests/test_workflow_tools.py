"""Tests for new workflow tools: can_enter_phase, get_workflow_status, validate_project_context."""

import json
import pytest

from blueprint_mcp.server import (
    can_enter_phase,
    get_workflow_status,
    validate_project_context,
    PHASE_PREREQUISITES,
)


def _extract_json(result: str) -> dict:
    assert "```json" in result, f"No JSON block in:\n{result[:300]}"
    return json.loads(result.split("```json\n")[1].split("\n```")[0])


# ── can_enter_phase ───────────────────────────────────────────────────────────


class TestCanEnterPhase:
    def test_phase_1_no_prerequisites(self):
        result = can_enter_phase(1, [])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is True
        assert parsed["data"]["missing_gates"] == []

    def test_phase_2_missing_gate_1(self):
        result = can_enter_phase(2, [])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is False
        assert 1 in parsed["data"]["missing_gates"]

    def test_phase_2_gate_1_completed(self):
        result = can_enter_phase(2, [1])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is True
        assert parsed["data"]["missing_gates"] == []

    def test_phase_3_partial_gates(self):
        result = can_enter_phase(3, [1])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is False
        assert 2 in parsed["data"]["missing_gates"]

    def test_phase_3_all_gates(self):
        result = can_enter_phase(3, [1, 2])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is True

    def test_phase_4_requires_gates_2_and_3(self):
        result = can_enter_phase(4, [1, 2])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is False
        assert 3 in parsed["data"]["missing_gates"]

    def test_phase_5_requires_gates_3_and_4(self):
        result = can_enter_phase(5, [1, 2])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is False
        missing = parsed["data"]["missing_gates"]
        assert 3 in missing
        assert 4 in missing

    def test_phase_5_all_prerequisites_met(self):
        result = can_enter_phase(5, [3, 4])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is True

    def test_invalid_phase_returns_error(self):
        result = can_enter_phase(9, [])
        parsed = _extract_json(result)
        assert parsed["status"] == "error"

    def test_extra_completed_gates_ignored(self):
        """Gates beyond what is required should not affect the result."""
        result = can_enter_phase(2, [1, 3, 4])
        parsed = _extract_json(result)
        assert parsed["data"]["can_enter"] is True

    def test_decision_block_has_required_keys(self):
        result = can_enter_phase(1, [])
        parsed = _extract_json(result)
        assert {"can_enter", "phase", "missing_gates", "completed_gates"} <= set(parsed["data"].keys())

    def test_phase_prerequisites_constant_exported(self):
        """PHASE_PREREQUISITES must be importable for parametrization."""
        assert isinstance(PHASE_PREREQUISITES, dict)
        assert 1 in PHASE_PREREQUISITES
        assert PHASE_PREREQUISITES[1] == []

    def test_tool_name_in_decision_block(self):
        result = can_enter_phase(2, [1])
        parsed = _extract_json(result)
        assert parsed["tool"] == "can_enter_phase"


# ── get_workflow_status ───────────────────────────────────────────────────────


class TestGetWorkflowStatus:
    def test_returns_all_three_workflows(self):
        result = get_workflow_status()
        assert "project_setup" in result
        assert "gate_review" in result
        assert "compliance" in result

    def test_decision_block_has_workflow_count(self):
        result = get_workflow_status()
        parsed = _extract_json(result)
        assert parsed["data"]["total_workflows"] == 3

    def test_all_step_tools_mentioned(self):
        result = get_workflow_status()
        assert "project_setup_intake" in result
        assert "gate_review_intake" in result
        assert "compliance_intake" in result

    def test_callable_without_parameters(self):
        result = get_workflow_status()
        assert len(result) > 100

    def test_tool_name_in_decision_block(self):
        result = get_workflow_status()
        parsed = _extract_json(result)
        assert parsed["tool"] == "get_workflow_status"

    def test_total_tools_in_decision(self):
        result = get_workflow_status()
        parsed = _extract_json(result)
        assert parsed["data"]["total_tools"] >= 6  # at least 2 steps per workflow


# ── validate_project_context ──────────────────────────────────────────────────


class TestValidateProjectContext:
    def test_valid_minimal_context(self):
        result = validate_project_context({"description": "fraud detection AI"})
        parsed = _extract_json(result)
        assert parsed["data"]["is_valid"] is True
        assert parsed["data"]["missing_required"] == []

    def test_missing_description(self):
        result = validate_project_context({})
        parsed = _extract_json(result)
        assert parsed["data"]["is_valid"] is False
        assert "description" in parsed["data"]["missing_required"]

    def test_invalid_project_type(self):
        result = validate_project_context({"description": "test", "project_type": "C"})
        parsed = _extract_json(result)
        assert "project_type" in parsed["data"]["invalid_values"]

    def test_invalid_risk_level(self):
        result = validate_project_context({"description": "test", "risk_level": "purple"})
        parsed = _extract_json(result)
        assert "risk_level" in parsed["data"]["invalid_values"]

    def test_valid_full_context(self):
        result = validate_project_context({
            "description": "fraud detection model",
            "project_type": "A",
            "risk_level": "green",
            "collaboration_mode": "2",
            "phase": 1,
            "gate": 1,
        })
        parsed = _extract_json(result)
        assert parsed["data"]["is_valid"] is True

    def test_next_tool_routing_intake(self):
        """Only description → recommend project_setup_intake."""
        result = validate_project_context({"description": "my project"})
        parsed = _extract_json(result)
        assert parsed["data"]["next_recommended_tool"] == "project_setup_intake"

    def test_next_tool_routing_gate_review(self):
        """Has gate → recommend gate_review_intake."""
        result = validate_project_context({"description": "my project", "gate": 1})
        parsed = _extract_json(result)
        assert parsed["data"]["next_recommended_tool"] == "gate_review_intake"

    def test_invalid_phase_value(self):
        result = validate_project_context({"description": "test", "phase": 9})
        parsed = _extract_json(result)
        assert "phase" in parsed["data"]["invalid_values"]

    def test_invalid_collaboration_mode(self):
        result = validate_project_context({"description": "test", "collaboration_mode": "9"})
        parsed = _extract_json(result)
        assert "collaboration_mode" in parsed["data"]["invalid_values"]

    def test_decision_block_parseable(self):
        result = validate_project_context({"description": "test"})
        parsed = _extract_json(result)
        assert "is_valid" in parsed["data"]

    def test_tool_name_in_decision(self):
        result = validate_project_context({"description": "test"})
        parsed = _extract_json(result)
        assert parsed["tool"] == "validate_project_context"
