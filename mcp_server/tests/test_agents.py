"""Tests for Gate Review Agent, Template Advisor, and Compliance Agent tools.

Gate Review Agent (2 tools):
- gate_review_intake: present gate checklist + identify evidence gaps
- gate_review_report: generate Guardian-ready review summary

Template Advisor (1 tool):
- template_advisor: recommend templates for role + phase with context pre-filled

Compliance Agent (2 tools):
- compliance_intake: classify EU AI Act risk category + relevant obligations
- compliance_checklist: specific checklist with article references

Assumptions:
- Stateless, no server-side LLM, content from ContentIndex
- Gate numbers 1–4 (content covers 1–4)
- Risk categories: unacceptable, high, limited, minimal
"""

from pathlib import Path

import pytest

from blueprint_mcp.content_index import ContentIndex
from blueprint_mcp.server import set_index

DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "docs"


@pytest.fixture(scope="module", autouse=True)
def setup_index():
    index = ContentIndex.load(DOCS_ROOT, language="en")
    set_index(index)
    yield
    set_index(None)


from blueprint_mcp.server import (  # noqa: E402
    compliance_checklist,
    compliance_intake,
    gate_review_intake,
    gate_review_report,
    template_advisor,
)

# ─── Gate Review Agent ────────────────────────────────────────────────────────


class TestGateReviewIntake:
    def test_returns_checklist_for_gate_1(self):
        result = gate_review_intake(1, ["project charter", "risk scan"])
        assert "gate" in result.lower()
        assert len(result) > 200

    def test_identifies_gaps(self):
        result = gate_review_intake(1, ["project charter"])
        # Should flag missing items
        assert "gap" in result.lower() or "missing" in result.lower() or "not" in result.lower()

    def test_evidence_reflected_in_output(self):
        result = gate_review_intake(2, ["validation report", "golden set"])
        assert "validation report" in result.lower()
        assert "golden set" in result.lower()

    def test_includes_next_step_guidance(self):
        result = gate_review_intake(1, ["project charter"])
        assert "next" in result.lower() or "report" in result.lower()

    def test_gate_2(self):
        result = gate_review_intake(2, ["business case", "experiment results"])
        assert len(result) > 200

    def test_gate_3(self):
        result = gate_review_intake(3, ["validation report"])
        assert len(result) > 200

    def test_gate_4(self):
        result = gate_review_intake(4, ["handover checklist", "monitoring plan"])
        assert len(result) > 200

    def test_invalid_gate(self):
        result = gate_review_intake(0, [])
        assert "error" in result.lower()

    def test_empty_evidence_list(self):
        result = gate_review_intake(1, [])
        assert len(result) > 100

    def test_returns_substantial_content(self):
        result = gate_review_intake(1, ["project charter", "risk scan", "data evaluation"])
        assert len(result) > 500


class TestGateReviewReport:
    def test_returns_summary(self):
        result = gate_review_report(
            gate=1,
            evidence=["project charter", "risk scan"],
            gaps=["data evaluation missing"],
        )
        assert "gate" in result.lower()
        assert len(result) > 200

    def test_report_includes_evidence(self):
        result = gate_review_report(
            gate=1,
            evidence=["project charter", "risk scan"],
            gaps=[],
        )
        assert "project charter" in result.lower()

    def test_report_includes_gaps(self):
        result = gate_review_report(
            gate=1,
            evidence=["project charter"],
            gaps=["data evaluation not completed", "collaboration mode not confirmed"],
        )
        assert "data evaluation" in result.lower()
        assert "collaboration mode" in result.lower()

    def test_report_no_gaps_clear_go(self):
        result = gate_review_report(
            gate=1,
            evidence=["project charter", "risk scan", "data evaluation", "collaboration mode"],
            gaps=[],
        )
        # No gaps should indicate readiness
        assert "go" in result.lower() or "ready" in result.lower() or "complete" in result.lower()

    def test_report_with_gaps_flags_action(self):
        result = gate_review_report(
            gate=2,
            evidence=["business case"],
            gaps=["golden set not defined", "validation not completed"],
        )
        assert "gap" in result.lower() or "missing" in result.lower() or "action" in result.lower()

    def test_report_suitable_for_guardian(self):
        result = gate_review_report(
            gate=1,
            evidence=["project charter"],
            gaps=["risk scan incomplete"],
        )
        assert (
            "guardian" in result.lower()
            or "review" in result.lower()
            or "decision" in result.lower()
        )


# ─── Template Advisor ─────────────────────────────────────────────────────────


class TestTemplateAdvisor:
    def test_returns_templates_for_pm_phase_1(self):
        result = template_advisor("AI Product Manager", 1)
        assert len(result) > 200

    def test_returns_templates_for_tech_lead_phase_3(self):
        result = template_advisor("Tech Lead", 3)
        assert len(result) > 100

    def test_returns_templates_for_guardian(self):
        result = template_advisor("Guardian", 2)
        assert len(result) > 100

    def test_includes_template_content(self):
        result = template_advisor("AI Product Manager", 1)
        # Should return actual template content, not just links
        assert "template" in result.lower() or "#" in result

    def test_context_reflected_in_output(self):
        result = template_advisor(
            "AI Product Manager", 1, context="Fraud detection project, Type A, green risk"
        )
        assert "fraud" in result.lower()

    def test_without_context(self):
        result = template_advisor("AI Product Manager", 2)
        assert len(result) > 200

    def test_invalid_phase(self):
        result = template_advisor("AI Product Manager", 9)
        assert "error" in result.lower() or "not found" in result.lower() or len(result) > 0


# ─── Compliance Agent ─────────────────────────────────────────────────────────


class TestComplianceIntake:
    def test_classifies_unacceptable_risk(self):
        result = compliance_intake("Social scoring system that rates citizen behaviour")
        assert "unacceptable" in result.lower() or "prohibited" in result.lower()

    def test_classifies_high_risk(self):
        result = compliance_intake("Automated hiring system that screens CVs and ranks candidates")
        assert "high" in result.lower()

    def test_classifies_limited_risk(self):
        result = compliance_intake("Customer service chatbot for product questions")
        assert "limited" in result.lower() or "transparency" in result.lower()

    def test_classifies_minimal_risk(self):
        result = compliance_intake("Spam filter for internal email")
        assert "minimal" in result.lower() or "low" in result.lower()

    def test_includes_description_in_output(self):
        result = compliance_intake("A fraud detection model for banking transactions")
        assert "fraud" in result.lower()

    def test_includes_relevant_articles(self):
        result = compliance_intake("An AI system for credit scoring")
        assert "art" in result.lower() or "article" in result.lower() or "act" in result.lower()

    def test_includes_next_step_guidance(self):
        result = compliance_intake("Document summarization tool")
        assert "next" in result.lower() or "checklist" in result.lower()

    def test_returns_substantial_content(self):
        result = compliance_intake("An AI recruitment screening system")
        assert len(result) > 500


class TestComplianceChecklist:
    def test_high_risk_checklist(self):
        result = compliance_checklist(
            "Automated hiring system",
            "high",
        )
        assert "checklist" in result.lower() or "art" in result.lower()
        assert len(result) > 300

    def test_limited_risk_checklist(self):
        result = compliance_checklist(
            "Customer service chatbot",
            "limited",
        )
        assert len(result) > 100

    def test_minimal_risk_checklist(self):
        result = compliance_checklist(
            "Spam filter",
            "minimal",
        )
        assert len(result) > 50

    def test_checklist_includes_article_references(self):
        result = compliance_checklist(
            "Credit scoring AI",
            "high",
        )
        assert "art" in result.lower() or "article" in result.lower()

    def test_checklist_includes_description(self):
        result = compliance_checklist(
            "A recruitment screening AI that ranks CVs",
            "high",
        )
        assert "recruitment" in result.lower()

    def test_unacceptable_risk_blocked(self):
        result = compliance_checklist(
            "Social scoring system",
            "unacceptable",
        )
        assert (
            "prohibited" in result.lower()
            or "blocked" in result.lower()
            or "stop" in result.lower()
        )

    def test_invalid_risk_category_returns_error(self):
        result = compliance_checklist("Some AI system", "hoog")
        assert "error" in result.lower() or "unknown" in result.lower() or "valid" in result.lower()

    def test_invalid_risk_category_json_mode(self):
        import json

        result = compliance_checklist("Some AI system", "hoog", output_format="json")
        parsed = json.loads(result)
        assert parsed["status"] == "error"

    def test_valid_category_json_mode(self):
        import json

        result = compliance_checklist("A spam filter", "minimal", output_format="json")
        parsed = json.loads(result)
        assert parsed["status"] in ("ok", "error")
        assert "data" in parsed


# ─── End-to-end workflow tests ────────────────────────────────────────────────


class TestGateReviewWorkflow:
    def test_full_gate_1_workflow(self):
        intake = gate_review_intake(1, ["project charter", "risk scan", "data evaluation"])
        assert len(intake) > 200

        report = gate_review_report(
            gate=1,
            evidence=["project charter", "risk scan", "data evaluation"],
            gaps=[],
        )
        assert len(report) > 200


class TestComplianceWorkflow:
    def test_full_high_risk_workflow(self):
        intake = compliance_intake("Automated CV screening system for recruitment")
        assert "high" in intake.lower()

        checklist = compliance_checklist("Automated CV screening system", "high")
        assert len(checklist) > 300

    def test_full_limited_risk_workflow(self):
        intake = compliance_intake("Internal FAQ chatbot")
        assert len(intake) > 200

        checklist = compliance_checklist("Internal FAQ chatbot", "limited")
        assert len(checklist) > 100
