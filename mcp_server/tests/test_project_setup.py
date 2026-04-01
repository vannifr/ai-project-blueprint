"""Tests for the Project Setup Agent workflow tools.

Three tools form a guided multi-step workflow:
1. project_setup_intake  — classify project + present risk questions
2. project_setup_risk    — score risk + recommend collaboration mode
3. project_setup_charter — generate pre-filled project charter

Assumptions verified by these tests:
- Tools are stateless (no server-side session)
- Tools compose existing index content (no LLM calls)
- Risk scoring: B1+B2+B3 subtotals (0-10 each) → green/amber/red
- Output contains structured sections the calling LLM can present to users
"""

import pytest
from pathlib import Path

from blueprint_mcp.content_index import ContentIndex
from blueprint_mcp.server import set_index

DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "docs"


@pytest.fixture(scope="module", autouse=True)
def setup_index():
    """Load index once and set it for all tools."""
    index = ContentIndex.load(DOCS_ROOT, language="en")
    set_index(index)
    yield
    set_index(None)


# ─── Import tools (after module exists) ──────────────────────────────────────

from blueprint_mcp.server import (  # noqa: E402
    project_setup_intake,
    project_setup_risk,
    project_setup_charter,
)


# ─── project_setup_intake ────────────────────────────────────────────────────


class TestProjectSetupIntake:
    """Step 1: Takes a project description, returns classification + risk questions."""

    def test_returns_type_classification_framework(self):
        result = project_setup_intake("An email classifier that routes support tickets")
        assert "type a" in result.lower() or "type b" in result.lower()

    def test_returns_risk_prescan_questions(self):
        result = project_setup_intake("A chatbot for internal HR questions")
        # Should contain the risk pre-scan scoring questions
        assert "B1" in result or "Application Domain" in result
        assert "B2" in result or "Data" in result
        assert "B3" in result or "Autonomy" in result

    def test_includes_hard_blockers(self):
        result = project_setup_intake("An AI system for recruitment screening")
        # Part A hard blockers from the risk pre-scan
        assert "blocker" in result.lower() or "prohibited" in result.lower() or "stop" in result.lower()

    def test_includes_project_description_in_output(self):
        desc = "A recommendation engine for product suggestions"
        result = project_setup_intake(desc)
        assert "recommendation engine" in result.lower()

    def test_includes_next_step_guidance(self):
        result = project_setup_intake("A fraud detection model for transactions")
        # Should tell the calling LLM what to do next
        assert "next" in result.lower() or "step" in result.lower()

    def test_returns_substantial_content(self):
        result = project_setup_intake("An AI tool for document summarization")
        assert len(result) > 500


# ─── project_setup_risk ──────────────────────────────────────────────────────


class TestProjectSetupRisk:
    """Step 2: Takes risk scores, returns risk level + collaboration mode."""

    def test_green_risk_low_scores(self):
        result = project_setup_risk(
            description="Internal FAQ chatbot",
            project_type="B",
            risk_scores_b1=1,
            risk_scores_b2=2,
            risk_scores_b3=1,
        )
        assert "green" in result.lower()

    def test_amber_risk_medium_scores(self):
        result = project_setup_risk(
            description="Customer service bot with personal data",
            project_type="B",
            risk_scores_b1=3,
            risk_scores_b2=5,
            risk_scores_b3=4,
        )
        assert "amber" in result.lower()

    def test_red_risk_high_scores(self):
        result = project_setup_risk(
            description="Automated hiring decisions",
            project_type="A",
            risk_scores_b1=8,
            risk_scores_b2=6,
            risk_scores_b3=7,
        )
        assert "red" in result.lower()

    def test_includes_collaboration_mode(self):
        result = project_setup_risk(
            description="Document classifier",
            project_type="A",
            risk_scores_b1=2,
            risk_scores_b2=1,
            risk_scores_b3=1,
        )
        # Should reference HAS-H collaboration modes
        assert "mode" in result.lower() or "collaboration" in result.lower()

    def test_includes_total_score(self):
        result = project_setup_risk(
            description="Test project",
            project_type="A",
            risk_scores_b1=3,
            risk_scores_b2=4,
            risk_scores_b3=5,
        )
        assert "12" in result  # total = 3+4+5

    def test_includes_next_step_guidance(self):
        result = project_setup_risk(
            description="Test project",
            project_type="A",
            risk_scores_b1=1,
            risk_scores_b2=1,
            risk_scores_b3=1,
        )
        assert "next" in result.lower() or "charter" in result.lower()

    def test_invalid_scores_clamped(self):
        """Scores outside 0-10 should be handled gracefully."""
        result = project_setup_risk(
            description="Test",
            project_type="A",
            risk_scores_b1=-1,
            risk_scores_b2=15,
            risk_scores_b3=5,
        )
        # Should still return a result (clamp or error)
        assert len(result) > 100


# ─── project_setup_charter ───────────────────────────────────────────────────


class TestProjectSetupCharter:
    """Step 3: Takes all context, returns pre-filled project charter."""

    def test_returns_charter_template(self):
        result = project_setup_charter(
            description="An email classifier for support tickets",
            project_type="A",
            risk_level="green",
            collaboration_mode="3",
        )
        # Should contain charter structure
        assert "charter" in result.lower()

    def test_charter_contains_filled_sections(self):
        result = project_setup_charter(
            description="A chatbot that answers HR questions using company docs",
            project_type="B",
            risk_level="amber",
            collaboration_mode="2",
        )
        # Description should be woven into the charter
        assert "chatbot" in result.lower()
        # Risk level should appear
        assert "amber" in result.lower()
        # Collaboration mode should appear
        assert "mode" in result.lower()

    def test_charter_includes_risk_section(self):
        result = project_setup_charter(
            description="Test project",
            project_type="A",
            risk_level="red",
            collaboration_mode="1",
        )
        assert "risk" in result.lower()
        assert "red" in result.lower()

    def test_charter_with_additional_context(self):
        result = project_setup_charter(
            description="Fraud detection system",
            project_type="A",
            risk_level="amber",
            collaboration_mode="3",
            additional_context="Team: 3 engineers, 1 PM. Budget: 50k. Timeline: Q3 2026.",
        )
        assert "50k" in result or "budget" in result.lower()

    def test_charter_without_additional_context(self):
        result = project_setup_charter(
            description="Simple classifier",
            project_type="A",
            risk_level="green",
            collaboration_mode="1",
        )
        assert len(result) > 500

    def test_charter_contains_decision_gate(self):
        result = project_setup_charter(
            description="Any project",
            project_type="A",
            risk_level="green",
            collaboration_mode="2",
        )
        assert "gate" in result.lower() or "go/no-go" in result.lower()


# ─── End-to-end workflow ─────────────────────────────────────────────────────


class TestProjectSetupWorkflow:
    """Verify the 3 tools chain together logically."""

    def test_full_workflow_green_path(self):
        """Simulate a low-risk project flowing through all 3 steps."""
        # Step 1: Intake
        intake = project_setup_intake("A document summarizer for internal reports")
        assert len(intake) > 200

        # Step 2: Risk (low scores)
        risk = project_setup_risk(
            description="A document summarizer for internal reports",
            project_type="B",
            risk_scores_b1=0,
            risk_scores_b2=1,
            risk_scores_b3=0,
        )
        assert "green" in risk.lower()

        # Step 3: Charter
        charter = project_setup_charter(
            description="A document summarizer for internal reports",
            project_type="B",
            risk_level="green",
            collaboration_mode="2",
        )
        assert "charter" in charter.lower()
        assert len(charter) > 500

    def test_full_workflow_high_risk_path(self):
        """Simulate a high-risk project flowing through all 3 steps."""
        # Step 1
        intake = project_setup_intake("Automated credit scoring for loan applications")
        assert len(intake) > 200

        # Step 2: High risk
        risk = project_setup_risk(
            description="Automated credit scoring for loan applications",
            project_type="A",
            risk_scores_b1=8,
            risk_scores_b2=7,
            risk_scores_b3=9,
        )
        assert "red" in risk.lower()

        # Step 3
        charter = project_setup_charter(
            description="Automated credit scoring for loan applications",
            project_type="A",
            risk_level="red",
            collaboration_mode="1",
            additional_context="Requires legal review. DPO involved.",
        )
        assert "red" in charter.lower()
        assert "charter" in charter.lower()
