"""IMP10 — Escalation hook system tests (TDD: red first, then green).

Escalation hooks allow callers to register callbacks that fire when
specific workflow events occur (e.g. gate review failed, risk level high).
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock

# ── Import tests ──────────────────────────────────────────────────────────────


class TestEscalationImport:
    def test_escalation_registry_importable(self):
        from blueprint_mcp.escalation import EscalationRegistry  # noqa: F401

    def test_escalation_event_importable(self):
        from blueprint_mcp.escalation import EscalationEvent  # noqa: F401

    def test_event_constants_importable(self):
        from blueprint_mcp.escalation import EventType  # noqa: F401


# ── EscalationEvent dataclass ─────────────────────────────────────────────────


class TestEscalationEvent:
    def test_event_has_type_and_data(self):
        from blueprint_mcp.escalation import EscalationEvent

        e = EscalationEvent(
            event_type="gate_review_failed", data={"gate": 1, "gaps": ["missing charter"]}
        )
        assert e.event_type == "gate_review_failed"
        assert e.data["gate"] == 1

    def test_event_timestamp_auto_set(self):
        from blueprint_mcp.escalation import EscalationEvent

        e = EscalationEvent(event_type="test", data={})
        assert e.timestamp is not None
        assert isinstance(e.timestamp, str)
        assert len(e.timestamp) > 0


class TestEventType:
    def test_gate_review_failed_constant(self):
        from blueprint_mcp.escalation import EventType

        assert EventType.GATE_REVIEW_FAILED == "gate_review_failed"

    def test_gate_review_passed_constant(self):
        from blueprint_mcp.escalation import EventType

        assert EventType.GATE_REVIEW_PASSED == "gate_review_passed"

    def test_risk_level_high_constant(self):
        from blueprint_mcp.escalation import EventType

        assert EventType.RISK_LEVEL_HIGH == "risk_level_high"


# ── EscalationRegistry ────────────────────────────────────────────────────────


class TestEscalationRegistryBasic:
    def test_register_and_fire(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()
        callback = MagicMock()
        registry.register(EventType.GATE_REVIEW_FAILED, callback)
        registry.fire(EventType.GATE_REVIEW_FAILED, data={"gate": 1})
        callback.assert_called_once()

    def test_fired_callback_receives_event(self):
        from blueprint_mcp.escalation import EscalationEvent, EscalationRegistry, EventType

        registry = EscalationRegistry()
        received: list[EscalationEvent] = []
        registry.register(EventType.GATE_REVIEW_FAILED, received.append)
        registry.fire(EventType.GATE_REVIEW_FAILED, data={"gate": 2, "gaps": ["x"]})
        assert len(received) == 1
        assert received[0].data["gate"] == 2

    def test_multiple_callbacks_for_same_event(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()
        cb1, cb2 = MagicMock(), MagicMock()
        registry.register(EventType.GATE_REVIEW_PASSED, cb1)
        registry.register(EventType.GATE_REVIEW_PASSED, cb2)
        registry.fire(EventType.GATE_REVIEW_PASSED, data={})
        cb1.assert_called_once()
        cb2.assert_called_once()

    def test_fire_unknown_event_is_noop(self):
        from blueprint_mcp.escalation import EscalationRegistry

        registry = EscalationRegistry()
        registry.fire("nonexistent_event", data={})  # must not raise

    def test_no_callbacks_registered_is_noop(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()
        registry.fire(EventType.GATE_REVIEW_FAILED, data={"gate": 1})  # must not raise

    def test_clear_removes_all_callbacks(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()
        callback = MagicMock()
        registry.register(EventType.GATE_REVIEW_FAILED, callback)
        registry.clear()
        registry.fire(EventType.GATE_REVIEW_FAILED, data={})
        callback.assert_not_called()

    def test_clear_event_type_removes_only_that_type(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()
        cb_fail = MagicMock()
        cb_pass = MagicMock()
        registry.register(EventType.GATE_REVIEW_FAILED, cb_fail)
        registry.register(EventType.GATE_REVIEW_PASSED, cb_pass)
        registry.clear(EventType.GATE_REVIEW_FAILED)
        registry.fire(EventType.GATE_REVIEW_FAILED, data={})
        registry.fire(EventType.GATE_REVIEW_PASSED, data={})
        cb_fail.assert_not_called()
        cb_pass.assert_called_once()

    def test_callback_exception_does_not_stop_others(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()

        def bad_callback(event):
            raise RuntimeError("oops")

        good = MagicMock()
        registry.register(EventType.GATE_REVIEW_FAILED, bad_callback)
        registry.register(EventType.GATE_REVIEW_FAILED, good)
        registry.fire(EventType.GATE_REVIEW_FAILED, data={})  # must not raise
        good.assert_called_once()

    def test_list_hooks_returns_registered_event_types(self):
        from blueprint_mcp.escalation import EscalationRegistry, EventType

        registry = EscalationRegistry()
        registry.register(EventType.GATE_REVIEW_FAILED, MagicMock())
        registry.register(EventType.RISK_LEVEL_HIGH, MagicMock())
        hooks = registry.list_hooks()
        assert EventType.GATE_REVIEW_FAILED in hooks
        assert EventType.RISK_LEVEL_HIGH in hooks


class TestFileLogHandler:
    """Built-in file-logging escalation handler."""

    def test_file_log_handler_importable(self):
        from blueprint_mcp.escalation import FileLogHandler  # noqa: F401

    def test_file_log_handler_writes_on_event(self, tmp_path):
        from blueprint_mcp.escalation import EscalationEvent, FileLogHandler

        log_file = tmp_path / "escalation.log"
        handler = FileLogHandler(log_path=log_file)
        event = EscalationEvent(event_type="gate_review_failed", data={"gate": 1})
        handler(event)
        assert log_file.exists()
        content = log_file.read_text()
        assert "gate_review_failed" in content

    def test_file_log_handler_appends(self, tmp_path):
        from blueprint_mcp.escalation import EscalationEvent, FileLogHandler

        log_file = tmp_path / "escalation.log"
        handler = FileLogHandler(log_path=log_file)
        handler(EscalationEvent(event_type="gate_review_failed", data={"gate": 1}))
        handler(EscalationEvent(event_type="gate_review_passed", data={"gate": 2}))
        lines = log_file.read_text().strip().splitlines()
        assert len(lines) == 2


# ── Module-level registry + server integration ────────────────────────────────


class TestModuleLevelRegistry:
    def test_get_escalation_registry_importable(self):
        from blueprint_mcp.server import get_escalation_registry  # noqa: F401

    def test_get_escalation_registry_returns_registry(self):
        from blueprint_mcp.escalation import EscalationRegistry
        from blueprint_mcp.server import get_escalation_registry

        assert isinstance(get_escalation_registry(), EscalationRegistry)

    def test_register_escalation_hook_importable(self):
        from blueprint_mcp.server import register_escalation_hook  # noqa: F401

    def test_register_escalation_hook_works(self):
        from blueprint_mcp.escalation import EventType
        from blueprint_mcp.server import get_escalation_registry, register_escalation_hook

        cb = MagicMock()
        register_escalation_hook(EventType.GATE_REVIEW_FAILED, cb)
        get_escalation_registry().fire(EventType.GATE_REVIEW_FAILED, data={"gate": 1})
        cb.assert_called_once()
        # cleanup
        get_escalation_registry().clear(EventType.GATE_REVIEW_FAILED)


class TestGateReviewFiresEscalation:
    """gate_review_report fires escalation events."""

    def _extract_json(self, result: str) -> dict:
        return json.loads(result.split("```json\n")[1].split("\n```")[0])

    def setup_method(self):
        from pathlib import Path

        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import get_escalation_registry, set_index

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        set_index(ContentIndex.load(docs_root, language="en"))
        get_escalation_registry().clear()

    def teardown_method(self):
        from blueprint_mcp.server import get_escalation_registry

        get_escalation_registry().clear()

    def test_gate_review_passed_fires_event(self):
        from blueprint_mcp.escalation import EventType
        from blueprint_mcp.server import gate_review_report, get_escalation_registry

        fired: list = []
        get_escalation_registry().register(EventType.GATE_REVIEW_PASSED, fired.append)
        # Pass with sufficient evidence
        gate_review_report(1, ["project charter", "risk scan", "stakeholder sign-off"], [])
        assert len(fired) == 1

    def test_gate_review_failed_fires_event(self):
        from blueprint_mcp.escalation import EventType
        from blueprint_mcp.server import gate_review_report, get_escalation_registry

        fired: list = []
        get_escalation_registry().register(EventType.GATE_REVIEW_FAILED, fired.append)
        # Explicit gaps → ready=False → fires GATE_REVIEW_FAILED
        gate_review_report(1, [], ["missing project charter"])
        assert len(fired) == 1

    def test_escalation_event_contains_gate_data(self):
        from blueprint_mcp.escalation import EventType
        from blueprint_mcp.server import gate_review_report, get_escalation_registry

        fired: list = []
        get_escalation_registry().register(EventType.GATE_REVIEW_FAILED, fired.append)
        gate_review_report(2, [], ["missing risk scan"])
        assert fired[0].data["gate"] == 2
