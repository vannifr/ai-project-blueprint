"""Tests for scripts/blueprint_lint.py — artefact-completeness per fase.

Tests run against the real docs/ directory.
All tests are read-only; nothing is modified.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"
SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "blueprint_lint.py"


# ── Import / CLI smoke tests ──────────────────────────────────────────────────


class TestBlueprintLintImport:
    def test_script_exists(self):
        assert SCRIPT.exists(), f"Expected script at {SCRIPT}"

    def test_can_import_lint_functions(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("blueprint_lint", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        assert hasattr(mod, "lint_phase")
        assert hasattr(mod, "lint_all")

    def test_cli_help_exits_zero(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "phase" in result.stdout.lower() or "usage" in result.stdout.lower()

    def test_cli_runs_without_args(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT.parent.parent),
        )
        # Exit 0 (all good) or 1 (issues found) — never a crash (2+)
        assert result.returncode in (0, 1)


# ── lint_phase function ───────────────────────────────────────────────────────


class TestLintPhase:
    @pytest.fixture
    def lint_phase(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("blueprint_lint", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.lint_phase

    def test_lint_phase_returns_list(self, lint_phase):
        result = lint_phase(1, docs_root=DOCS_ROOT)
        assert isinstance(result, list)

    def test_lint_phase_items_have_required_keys(self, lint_phase):
        result = lint_phase(1, docs_root=DOCS_ROOT)
        for item in result:
            assert "phase" in item
            assert "check" in item
            assert "status" in item  # "ok" or "missing"
            assert "detail" in item

    def test_lint_phase_all_phases_valid(self, lint_phase):
        for phase in range(1, 6):
            result = lint_phase(phase, docs_root=DOCS_ROOT)
            assert isinstance(result, list), f"Phase {phase} returned non-list"

    def test_lint_phase_unknown_phase_returns_error(self, lint_phase):
        result = lint_phase(99, docs_root=DOCS_ROOT)
        assert any(item["status"] == "error" for item in result)

    def test_lint_phase_statuses_are_valid(self, lint_phase):
        for phase in range(1, 6):
            for item in lint_phase(phase, docs_root=DOCS_ROOT):
                assert item["status"] in ("ok", "missing", "warning", "error")

    def test_real_docs_have_objectives_for_all_phases(self, lint_phase):
        for phase in range(1, 6):
            items = lint_phase(phase, docs_root=DOCS_ROOT)
            objectives = [i for i in items if "objectives" in i["check"].lower()]
            if objectives:
                assert any(i["status"] == "ok" for i in objectives), \
                    f"Phase {phase} missing objectives"

    def test_real_docs_have_templates_for_all_phases(self, lint_phase):
        for phase in range(1, 6):
            items = lint_phase(phase, docs_root=DOCS_ROOT)
            templates = [i for i in items if "template" in i["check"].lower()]
            if templates:
                assert any(i["status"] == "ok" for i in templates), \
                    f"Phase {phase} missing templates"


# ── lint_all function ─────────────────────────────────────────────────────────


class TestLintAll:
    @pytest.fixture
    def lint_all(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("blueprint_lint", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.lint_all

    def test_lint_all_returns_dict(self, lint_all):
        result = lint_all(docs_root=DOCS_ROOT)
        assert isinstance(result, dict)

    def test_lint_all_has_phases_key(self, lint_all):
        result = lint_all(docs_root=DOCS_ROOT)
        assert "phases" in result

    def test_lint_all_has_summary(self, lint_all):
        result = lint_all(docs_root=DOCS_ROOT)
        assert "summary" in result
        assert "total_checks" in result["summary"]
        assert "ok" in result["summary"]
        assert "missing" in result["summary"]

    def test_lint_all_covers_5_phases(self, lint_all):
        result = lint_all(docs_root=DOCS_ROOT)
        assert len(result["phases"]) == 5

    def test_lint_all_total_checks_positive(self, lint_all):
        result = lint_all(docs_root=DOCS_ROOT)
        assert result["summary"]["total_checks"] > 0

    def test_lint_all_real_docs_mostly_ok(self, lint_all):
        result = lint_all(docs_root=DOCS_ROOT)
        summary = result["summary"]
        ok = summary["ok"]
        total = summary["total_checks"]
        assert ok / total >= 0.7, f"Less than 70% checks passing: {ok}/{total}"


# ── Cross-reference integrity ─────────────────────────────────────────────────


class TestCrossReferenceCheck:
    @pytest.fixture
    def check_links(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("blueprint_lint", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.check_links

    def test_check_links_importable(self, check_links):
        assert callable(check_links)

    def test_check_links_returns_list(self, check_links):
        result = check_links(docs_root=DOCS_ROOT)
        assert isinstance(result, list)

    def test_check_links_items_have_required_keys(self, check_links):
        result = check_links(docs_root=DOCS_ROOT)
        for item in result[:10]:  # spot-check first 10
            assert "source" in item
            assert "target" in item
            assert "status" in item

    def test_check_links_status_values(self, check_links):
        result = check_links(docs_root=DOCS_ROOT)
        valid_statuses = {"ok", "broken", "external", "anchor"}
        for item in result[:20]:
            assert item["status"] in valid_statuses

    def test_real_docs_have_mostly_valid_links(self, check_links):
        result = check_links(docs_root=DOCS_ROOT)
        if not result:
            return  # no links found — acceptable
        broken = [r for r in result if r["status"] == "broken"]
        total = len(result)
        # Allow up to 10% broken links (anchors drift)
        assert len(broken) / total <= 0.10, \
            f"Too many broken links: {len(broken)}/{total}"


# ── CLI --phase filter ────────────────────────────────────────────────────────


class TestCLIPhaseFilter:
    def test_cli_phase_flag(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--phase", "1"],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT.parent.parent),
        )
        assert result.returncode in (0, 1)
        assert "phase 1" in result.stdout.lower() or "1" in result.stdout

    def test_cli_verbose_flag(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--phase", "1", "--verbose"],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT.parent.parent),
        )
        assert result.returncode in (0, 1)

    def test_cli_invalid_phase_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--phase", "99"],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT.parent.parent),
        )
        assert result.returncode != 0

    def test_cli_output_contains_ok_or_missing(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--phase", "2"],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT.parent.parent),
        )
        combined = result.stdout + result.stderr
        assert "ok" in combined.lower() or "missing" in combined.lower() or "✓" in combined or "✗" in combined
