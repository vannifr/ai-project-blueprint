"""SQLite-backed session store for persistent workflow state.

Each session tracks:
- project metadata (id, type, language)
- completed gate numbers
- recorded artifacts
- arbitrary extra key/value pairs

Usage::

    store = SessionStore("/path/to/sessions.db")
    sid = store.create_session(project_id="proj-1", project_type="NLP", language="nl")
    store.record_gate_completion(sid, gate=1)
    store.record_artifact(sid, artifact_type="document", artifact_path="docs/charter.md")
    state = store.get_state(sid)
    # state.completed_gates == [1]
"""

from __future__ import annotations

import json
import sqlite3
import uuid
from dataclasses import dataclass, field


@dataclass
class SessionState:
    """Snapshot of a session's current state.

    Attributes:
        session_id: Unique session identifier.
        project_id: Caller-supplied project identifier.
        project_type: E.g. ``"NLP"``, ``"CV"``.
        language: ``"nl"`` or ``"en"``.
        completed_gates: Sorted list of gate numbers marked complete.
        artifacts: List of ``{"type": str, "path": str}`` dicts.
        extra: Arbitrary key/value data set via :meth:`SessionStore.set_state_key`.
    """

    session_id: str
    project_id: str
    project_type: str
    language: str
    completed_gates: list[int] = field(default_factory=list)
    artifacts: list[dict] = field(default_factory=list)
    extra: dict = field(default_factory=dict)


class SessionStore:
    """SQLite-backed store for workflow session state.

    Args:
        db_path: Filesystem path for the SQLite database file.
            Use ``":memory:"`` for an in-memory database (useful in tests).
    """

    def __init__(self, db_path: str = ":memory:") -> None:
        self._db_path = db_path
        self._conn = sqlite3.connect(db_path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    # ------------------------------------------------------------------
    # Schema
    # ------------------------------------------------------------------

    def _init_schema(self) -> None:
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS sessions (
                session_id  TEXT PRIMARY KEY,
                project_id  TEXT NOT NULL,
                project_type TEXT NOT NULL,
                language    TEXT NOT NULL,
                extra_json  TEXT NOT NULL DEFAULT '{}'
            );

            CREATE TABLE IF NOT EXISTS gates (
                session_id  TEXT NOT NULL REFERENCES sessions(session_id),
                gate        INTEGER NOT NULL,
                PRIMARY KEY (session_id, gate)
            );

            CREATE TABLE IF NOT EXISTS artifacts (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id  TEXT NOT NULL REFERENCES sessions(session_id),
                artifact_type TEXT NOT NULL,
                artifact_path TEXT NOT NULL
            );
        """)
        self._conn.commit()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def create_session(self, project_id: str, project_type: str, language: str) -> str:
        """Create a new session and return its ID."""
        sid = str(uuid.uuid4())
        self._conn.execute(
            "INSERT INTO sessions (session_id, project_id, project_type, language) VALUES (?, ?, ?, ?)",
            (sid, project_id, project_type, language),
        )
        self._conn.commit()
        return sid

    def get_state(self, session_id: str) -> SessionState | None:
        """Return the current state for *session_id*, or ``None`` if not found."""
        row = self._conn.execute(
            "SELECT * FROM sessions WHERE session_id = ?", (session_id,)
        ).fetchone()
        if row is None:
            return None

        gates = [
            r["gate"]
            for r in self._conn.execute(
                "SELECT gate FROM gates WHERE session_id = ? ORDER BY gate", (session_id,)
            ).fetchall()
        ]

        artifacts = [
            {"type": r["artifact_type"], "path": r["artifact_path"]}
            for r in self._conn.execute(
                "SELECT artifact_type, artifact_path FROM artifacts WHERE session_id = ?",
                (session_id,),
            ).fetchall()
        ]

        extra = json.loads(row["extra_json"])

        return SessionState(
            session_id=row["session_id"],
            project_id=row["project_id"],
            project_type=row["project_type"],
            language=row["language"],
            completed_gates=gates,
            artifacts=artifacts,
            extra=extra,
        )

    def record_gate_completion(self, session_id: str, gate: int) -> None:
        """Mark *gate* as completed for *session_id* (idempotent)."""
        self._conn.execute(
            "INSERT OR IGNORE INTO gates (session_id, gate) VALUES (?, ?)",
            (session_id, gate),
        )
        self._conn.commit()

    def record_artifact(self, session_id: str, artifact_type: str, artifact_path: str) -> None:
        """Append an artifact to the session's artifact list."""
        self._conn.execute(
            "INSERT INTO artifacts (session_id, artifact_type, artifact_path) VALUES (?, ?, ?)",
            (session_id, artifact_type, artifact_path),
        )
        self._conn.commit()

    def set_state_key(self, session_id: str, key: str, value) -> None:
        """Store an arbitrary key/value in the session's extra JSON blob.

        No-op if *session_id* does not exist.
        """
        row = self._conn.execute(
            "SELECT extra_json FROM sessions WHERE session_id = ?", (session_id,)
        ).fetchone()
        if row is None:
            return
        extra = json.loads(row["extra_json"])
        extra[key] = value
        self._conn.execute(
            "UPDATE sessions SET extra_json = ? WHERE session_id = ?",
            (json.dumps(extra), session_id),
        )
        self._conn.commit()

    def list_sessions(self) -> list[dict]:
        """Return a summary list of all sessions.

        Each entry is a dict with ``session_id``, ``project_id``,
        ``project_type``, and ``language``.
        """
        rows = self._conn.execute(
            "SELECT session_id, project_id, project_type, language FROM sessions"
        ).fetchall()
        return [dict(r) for r in rows]
