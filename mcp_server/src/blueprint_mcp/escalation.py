"""Escalation hook system for Blueprint MCP workflow events.

Allows callers to register callbacks that fire when specific workflow
events occur (gate review failed/passed, high risk detected).

Usage::

    from blueprint_mcp.escalation import EscalationRegistry, EventType, FileLogHandler

    registry = EscalationRegistry()
    registry.register(EventType.GATE_REVIEW_FAILED, FileLogHandler("/var/log/blueprint.log"))
    registry.register(EventType.GATE_REVIEW_FAILED, lambda e: send_slack(e.data))

    # Fire from a tool:
    registry.fire(EventType.GATE_REVIEW_FAILED, data={"gate": 2, "gaps": ["missing charter"]})
"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class EventType:
    """Constants for built-in escalation event types."""

    GATE_REVIEW_FAILED = "gate_review_failed"
    GATE_REVIEW_PASSED = "gate_review_passed"
    RISK_LEVEL_HIGH = "risk_level_high"


@dataclass
class EscalationEvent:
    """A workflow event passed to registered callbacks.

    Attributes:
        event_type: One of the EventType constants (or a custom string).
        data: Arbitrary context dict (gate number, gaps list, etc.).
        timestamp: ISO-8601 UTC timestamp, set automatically on creation.
    """

    event_type: str
    data: dict
    timestamp: str = field(default_factory=lambda: datetime.now(UTC).isoformat())


class EscalationRegistry:
    """Registry of escalation callbacks keyed by event type.

    Thread-safety: callbacks are invoked synchronously. If a callback
    raises, the exception is logged and the remaining callbacks continue.
    """

    def __init__(self) -> None:
        self._hooks: dict[str, list[Callable[[EscalationEvent], None]]] = defaultdict(list)

    def register(self, event_type: str, callback: Callable[[EscalationEvent], None]) -> None:
        """Register *callback* to be called when *event_type* fires."""
        self._hooks[event_type].append(callback)

    def fire(self, event_type: str, data: dict) -> None:
        """Create an :class:`EscalationEvent` and call all registered callbacks.

        Exceptions in individual callbacks are logged but do not prevent
        other callbacks from running.
        """
        callbacks = self._hooks.get(event_type, [])
        if not callbacks:
            return
        event = EscalationEvent(event_type=event_type, data=data)
        for cb in callbacks:
            try:
                cb(event)
            except Exception:
                logger.exception("Escalation callback %r raised for event %r", cb, event_type)

    def clear(self, event_type: str | None = None) -> None:
        """Remove all callbacks, or only those for *event_type* if given."""
        if event_type is None:
            self._hooks.clear()
        else:
            self._hooks.pop(event_type, None)

    def list_hooks(self) -> list[str]:
        """Return a list of event types that have at least one callback."""
        return [et for et, cbs in self._hooks.items() if cbs]


class FileLogHandler:
    """Built-in escalation handler that appends events to a log file.

    Each event is written as a single JSON line.

    Args:
        log_path: Filesystem path for the log file (created if needed).
    """

    def __init__(self, log_path: str | Path) -> None:
        self._log_path = Path(log_path)

    def __call__(self, event: EscalationEvent) -> None:
        record = {
            "timestamp": event.timestamp,
            "event_type": event.event_type,
            "data": event.data,
        }
        with self._log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
