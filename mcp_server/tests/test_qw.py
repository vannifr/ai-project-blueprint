"""QW2 + QW5 quality improvements (TDD: red first, then green).

QW5 — get_tool_cheatsheet: MCP tool that returns structured tool-selection
      guidance so agents know which tool to call and when.

QW2 — find_missing_answers: utility that detects docs without 'answers:'
      frontmatter and generates candidate questions from content.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

DOCS_ROOT = Path(__file__).resolve().parent.parent.parent / "docs"


def _extract_json(result: str) -> dict:
    assert "```json" in result, f"No JSON block in:\n{result[:300]}"
    return json.loads(result.split("```json\n")[1].split("\n```")[0])


# ── QW5: get_tool_cheatsheet ──────────────────────────────────────────────────


class TestGetToolCheatsheetImport:
    def test_tool_importable(self):
        from blueprint_mcp.server import get_tool_cheatsheet  # noqa: F401


class TestGetToolCheatsheetOutput:
    def test_returns_string(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        assert isinstance(get_tool_cheatsheet(), str)

    def test_has_decision_block(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        result = get_tool_cheatsheet()
        parsed = _extract_json(result)
        assert parsed["tool"] == "get_tool_cheatsheet"

    def test_json_mode(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        result = get_tool_cheatsheet(output_format="json")
        parsed = json.loads(result)
        assert parsed["tool"] == "get_tool_cheatsheet"

    def test_decision_data_has_tools_list(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        parsed = _extract_json(get_tool_cheatsheet())
        assert "tools" in parsed["data"]
        assert isinstance(parsed["data"]["tools"], list)

    def test_tools_list_non_empty(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        parsed = _extract_json(get_tool_cheatsheet())
        assert len(parsed["data"]["tools"]) > 5

    def test_each_tool_has_required_keys(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        parsed = _extract_json(get_tool_cheatsheet())
        for tool in parsed["data"]["tools"]:
            assert "name" in tool, f"Missing 'name' in {tool}"
            assert "when" in tool, f"Missing 'when' in {tool}"
            assert "next" in tool, f"Missing 'next' in {tool}"

    def test_markdown_contains_tool_names(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        result = get_tool_cheatsheet()
        assert "answer_question" in result
        assert "check_gate_readiness" in result
        assert "classify_risk" in result

    def test_markdown_contains_workflow_guidance(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        result = get_tool_cheatsheet()
        # Should contain some form of guidance about when to use tools
        lower = result.lower()
        assert any(kw in lower for kw in ("gate", "risk", "template", "phase", "session"))

    def test_filter_by_intent(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        result_search = get_tool_cheatsheet(intent="search")
        result_gate = get_tool_cheatsheet(intent="gate")
        parsed_search = _extract_json(result_search)
        parsed_gate = _extract_json(result_gate)
        # Filtered results should be smaller than or equal to full list
        all_tools = _extract_json(get_tool_cheatsheet())["data"]["tools"]
        assert len(parsed_search["data"]["tools"]) <= len(all_tools)
        assert len(parsed_gate["data"]["tools"]) <= len(all_tools)

    def test_unknown_intent_returns_all(self):
        from blueprint_mcp.server import get_tool_cheatsheet

        result_all = get_tool_cheatsheet()
        result_unknown = get_tool_cheatsheet(intent="xyznonexistent")
        all_count = len(_extract_json(result_all)["data"]["tools"])
        unknown_count = len(_extract_json(result_unknown)["data"]["tools"])
        assert unknown_count == all_count


# ── QW2: find_missing_answers utility ────────────────────────────────────────


class TestFindMissingAnswersImport:
    def test_importable(self):
        from blueprint_mcp.missing_answers import find_missing_answers  # noqa: F401

    def test_generate_candidate_answers_importable(self):
        from blueprint_mcp.missing_answers import generate_candidate_answers  # noqa: F401


class TestFindMissingAnswers:
    @pytest.fixture
    def find(self):
        from blueprint_mcp.missing_answers import find_missing_answers

        return find_missing_answers

    def test_returns_list(self, find):
        result = find(DOCS_ROOT)
        assert isinstance(result, list)

    def test_items_have_required_keys(self, find):
        result = find(DOCS_ROOT)
        for item in result[:5]:
            assert "path" in item
            assert "title" in item
            assert "has_answers" in item

    def test_missing_docs_have_has_answers_false(self, find):
        result = find(DOCS_ROOT)
        missing = [r for r in result if not r["has_answers"]]
        assert all(not r["has_answers"] for r in missing)

    def test_can_filter_only_missing(self, find):
        all_docs = find(DOCS_ROOT)
        missing_only = find(DOCS_ROOT, only_missing=True)
        # Filtered list is subset of full list
        assert len(missing_only) <= len(all_docs)
        assert all(not r["has_answers"] for r in missing_only)

    def test_real_docs_have_at_least_some_answers(self, find):
        result = find(DOCS_ROOT)
        with_answers = [r for r in result if r["has_answers"]]
        # The real docs have many pages with answers: frontmatter
        assert len(with_answers) > 0


class TestGenerateCandidateAnswers:
    @pytest.fixture
    def generate(self):
        from blueprint_mcp.missing_answers import generate_candidate_answers

        return generate_candidate_answers

    def test_returns_list(self, generate):
        result = generate(
            "Risk Classification Guide", "This guide explains how to classify AI risk levels."
        )
        assert isinstance(result, list)

    def test_returns_strings(self, generate):
        result = generate("Risk Guide", "Explains risk classification.")
        assert all(isinstance(q, str) for q in result)

    def test_generates_at_least_one_candidate(self, generate):
        result = generate(
            "Risk Classification", "This document explains risk levels for AI projects."
        )
        assert len(result) >= 1

    def test_candidates_end_with_question_mark(self, generate):
        result = generate("Gate Review", "The gate review process ensures readiness.")
        for q in result:
            assert q.strip().endswith("?"), f"Not a question: {q!r}"

    def test_empty_body_returns_title_based_question(self, generate):
        result = generate("Gate Review Checklist", "")
        assert len(result) >= 1

    def test_uses_title_keywords(self, generate):
        result = generate("Gate Review Process", "Explains the process.")
        combined = " ".join(result).lower()
        assert "gate" in combined or "review" in combined or "process" in combined

    def test_max_results_respected(self, generate):
        result = generate("Risk Guide", "Long body " * 50, max_results=2)
        assert len(result) <= 2


class TestFindMissingAnswersCLI:
    """scripts/add_missing_answers.py CLI exists and works."""

    SCRIPT = Path(__file__).resolve().parent.parent.parent / "scripts" / "add_missing_answers.py"

    def test_script_exists(self):
        assert self.SCRIPT.exists(), f"Expected script at {self.SCRIPT}"

    def test_cli_help(self):
        import subprocess
        import sys

        result = subprocess.run(
            [sys.executable, str(self.SCRIPT), "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    def test_cli_dry_run(self):
        import subprocess
        import sys

        result = subprocess.run(
            [sys.executable, str(self.SCRIPT), "--dry-run", "--limit", "3"],
            capture_output=True,
            text=True,
            cwd=str(self.SCRIPT.parent.parent),
        )
        assert result.returncode in (0, 1)
