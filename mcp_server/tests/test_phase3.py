"""Phase 3 — State & Routing tests (TDD: red first, then green).

Covers:
  IMP8 — Persistent session state (SQLite-backed SessionStore)
  IMP11 — Multi-project scoping (list_sessions, list_projects tool)
  IMP12 — Glossary-aware answer improvement (GlossaryIndex)
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# ── IMP8: SessionStore ────────────────────────────────────────────────────────


class TestSessionStoreImport:
    def test_session_store_importable(self):
        from blueprint_mcp.session_store import SessionStore  # noqa: F401

    def test_session_result_importable(self):
        from blueprint_mcp.session_store import SessionState  # noqa: F401


class TestSessionStoreCreation:
    @pytest.fixture
    def store(self, tmp_path):
        from blueprint_mcp.session_store import SessionStore

        return SessionStore(db_path=str(tmp_path / "sessions.db"))

    def test_create_session_returns_string_id(self, store):
        sid = store.create_session(project_id="proj-1", project_type="NLP", language="nl")
        assert isinstance(sid, str)
        assert len(sid) > 0

    def test_create_session_ids_are_unique(self, store):
        sid1 = store.create_session(project_id="proj-1", project_type="NLP", language="nl")
        sid2 = store.create_session(project_id="proj-1", project_type="NLP", language="nl")
        assert sid1 != sid2

    def test_create_session_stores_metadata(self, store):
        sid = store.create_session(project_id="proj-x", project_type="CV", language="en")
        state = store.get_state(sid)
        assert state.project_id == "proj-x"
        assert state.project_type == "CV"
        assert state.language == "en"

    def test_get_state_unknown_session_returns_none(self, store):
        result = store.get_state("nonexistent-id")
        assert result is None


class TestSessionStoreState:
    @pytest.fixture
    def store_and_sid(self, tmp_path):
        from blueprint_mcp.session_store import SessionStore

        store = SessionStore(db_path=str(tmp_path / "sessions.db"))
        sid = store.create_session(project_id="p1", project_type="NLP", language="nl")
        return store, sid

    def test_initial_completed_gates_is_empty(self, store_and_sid):
        store, sid = store_and_sid
        state = store.get_state(sid)
        assert state.completed_gates == []

    def test_record_gate_completion_persists(self, store_and_sid):
        store, sid = store_and_sid
        store.record_gate_completion(sid, gate=1)
        state = store.get_state(sid)
        assert 1 in state.completed_gates

    def test_record_multiple_gates(self, store_and_sid):
        store, sid = store_and_sid
        store.record_gate_completion(sid, gate=1)
        store.record_gate_completion(sid, gate=2)
        state = store.get_state(sid)
        assert set(state.completed_gates) == {1, 2}

    def test_record_gate_idempotent(self, store_and_sid):
        store, sid = store_and_sid
        store.record_gate_completion(sid, gate=1)
        store.record_gate_completion(sid, gate=1)
        state = store.get_state(sid)
        assert state.completed_gates.count(1) == 1

    def test_initial_artifacts_is_empty(self, store_and_sid):
        store, sid = store_and_sid
        state = store.get_state(sid)
        assert state.artifacts == []

    def test_record_artifact_persists(self, store_and_sid):
        store, sid = store_and_sid
        store.record_artifact(sid, artifact_type="document", artifact_path="docs/charter.md")
        state = store.get_state(sid)
        assert len(state.artifacts) == 1
        assert state.artifacts[0]["type"] == "document"
        assert state.artifacts[0]["path"] == "docs/charter.md"

    def test_record_multiple_artifacts(self, store_and_sid):
        store, sid = store_and_sid
        store.record_artifact(sid, artifact_type="document", artifact_path="a.md")
        store.record_artifact(sid, artifact_type="test_result", artifact_path="b.json")
        state = store.get_state(sid)
        assert len(state.artifacts) == 2

    def test_set_and_get_custom_key(self, store_and_sid):
        store, sid = store_and_sid
        store.set_state_key(sid, "phase", 2)
        state = store.get_state(sid)
        assert state.extra.get("phase") == 2

    def test_set_state_key_unknown_session_is_noop(self, store_and_sid):
        store, _ = store_and_sid
        store.set_state_key("bad-id", "k", "v")  # must not raise


class TestSessionStorePersistence:
    def test_state_survives_store_restart(self, tmp_path):
        """A new SessionStore instance reads data written by a previous one."""
        from blueprint_mcp.session_store import SessionStore

        db = str(tmp_path / "sessions.db")

        store1 = SessionStore(db_path=db)
        sid = store1.create_session(project_id="p", project_type="NLP", language="en")
        store1.record_gate_completion(sid, gate=1)

        store2 = SessionStore(db_path=db)
        state = store2.get_state(sid)
        assert state is not None
        assert 1 in state.completed_gates


# ── IMP11: list_sessions + list_projects MCP tool ────────────────────────────


class TestListSessions:
    @pytest.fixture
    def store_with_sessions(self, tmp_path):
        from blueprint_mcp.session_store import SessionStore

        store = SessionStore(db_path=str(tmp_path / "sessions.db"))
        store.create_session(project_id="proj-a", project_type="NLP", language="nl")
        store.create_session(project_id="proj-b", project_type="CV", language="en")
        return store

    def test_list_sessions_returns_list(self, store_with_sessions):
        sessions = store_with_sessions.list_sessions()
        assert isinstance(sessions, list)

    def test_list_sessions_count(self, store_with_sessions):
        sessions = store_with_sessions.list_sessions()
        assert len(sessions) == 2

    def test_list_sessions_contains_project_ids(self, store_with_sessions):
        sessions = store_with_sessions.list_sessions()
        project_ids = [s["project_id"] for s in sessions]
        assert "proj-a" in project_ids
        assert "proj-b" in project_ids

    def test_list_sessions_empty_when_no_sessions(self, tmp_path):
        from blueprint_mcp.session_store import SessionStore

        store = SessionStore(db_path=str(tmp_path / "empty.db"))
        assert store.list_sessions() == []


class TestListProjectsMCPTool:
    def _extract_json(self, result: str) -> dict:
        assert "```json" in result, f"No JSON block in: {result!r}"
        return json.loads(result.split("```json\n")[1].split("\n```")[0])

    def test_list_projects_tool_importable(self):
        from blueprint_mcp.server import list_projects  # noqa: F401

    def test_list_projects_returns_string(self):
        import os
        import tempfile

        from blueprint_mcp.server import list_projects, set_session_store
        from blueprint_mcp.session_store import SessionStore

        with tempfile.TemporaryDirectory() as tmp:
            store = SessionStore(db_path=os.path.join(tmp, "s.db"))
            set_session_store(store)
            result = list_projects()
            assert isinstance(result, str)

    def test_list_projects_returns_decision_block(self):
        import os
        import tempfile

        from blueprint_mcp.server import list_projects, set_session_store
        from blueprint_mcp.session_store import SessionStore

        with tempfile.TemporaryDirectory() as tmp:
            store = SessionStore(db_path=os.path.join(tmp, "s.db"))
            set_session_store(store)
            result = list_projects()
            parsed = self._extract_json(result)
            assert parsed["tool"] == "list_projects"

    def test_list_projects_json_mode(self):
        import os
        import tempfile

        from blueprint_mcp.server import list_projects, set_session_store
        from blueprint_mcp.session_store import SessionStore

        with tempfile.TemporaryDirectory() as tmp:
            store = SessionStore(db_path=os.path.join(tmp, "s.db"))
            set_session_store(store)
            result = list_projects(output_format="json")
            parsed = json.loads(result)
            assert parsed["tool"] == "list_projects"

    def test_list_projects_no_store_returns_empty(self):
        from blueprint_mcp.server import list_projects, set_session_store

        set_session_store(None)
        result = list_projects()
        parsed = self._extract_json(result)
        assert parsed["data"]["projects"] == []


class TestSessionMCPTools:
    """session_start, session_get_state, session_record_artifact MCP tools."""

    def _extract_json(self, result: str) -> dict:
        assert "```json" in result
        return json.loads(result.split("```json\n")[1].split("\n```")[0])

    @pytest.fixture(autouse=True)
    def _inject_store(self, tmp_path):
        from blueprint_mcp.server import set_session_store
        from blueprint_mcp.session_store import SessionStore

        store = SessionStore(db_path=str(tmp_path / "sessions.db"))
        set_session_store(store)
        yield
        set_session_store(None)

    def test_session_start_importable(self):
        from blueprint_mcp.server import session_start  # noqa: F401

    def test_session_start_returns_session_id(self):
        from blueprint_mcp.server import session_start

        result = session_start(project_id="p1", project_type="NLP", language="nl")
        parsed = self._extract_json(result)
        assert "session_id" in parsed["data"]
        assert parsed["data"]["session_id"]

    def test_session_start_decision_status_ok(self):
        from blueprint_mcp.server import session_start

        result = session_start(project_id="p1", project_type="NLP", language="nl")
        parsed = self._extract_json(result)
        assert parsed["status"] == "ok"

    def test_session_get_state_importable(self):
        from blueprint_mcp.server import session_get_state  # noqa: F401

    def test_session_get_state_returns_state(self):
        from blueprint_mcp.server import session_get_state, session_start

        start_result = session_start(project_id="p1", project_type="NLP", language="nl")
        sid = self._extract_json(start_result)["data"]["session_id"]
        result = session_get_state(sid)
        parsed = self._extract_json(result)
        assert parsed["data"]["project_id"] == "p1"

    def test_session_get_state_unknown_returns_not_found(self):
        from blueprint_mcp.server import session_get_state

        result = session_get_state("nonexistent")
        parsed = self._extract_json(result)
        assert parsed["status"] == "not_found"

    def test_session_record_artifact_importable(self):
        from blueprint_mcp.server import session_record_artifact  # noqa: F401

    def test_session_record_artifact_ok(self):
        from blueprint_mcp.server import session_record_artifact, session_start

        start_result = session_start(project_id="p1", project_type="NLP", language="nl")
        sid = self._extract_json(start_result)["data"]["session_id"]
        result = session_record_artifact(
            sid, artifact_type="document", artifact_path="docs/charter.md"
        )
        parsed = self._extract_json(result)
        assert parsed["status"] == "ok"

    def test_session_record_artifact_reflected_in_state(self):
        from blueprint_mcp.server import session_get_state, session_record_artifact, session_start

        start_result = session_start(project_id="p1", project_type="NLP", language="nl")
        sid = self._extract_json(start_result)["data"]["session_id"]
        session_record_artifact(sid, artifact_type="document", artifact_path="docs/charter.md")
        state_result = session_get_state(sid)
        parsed = self._extract_json(state_result)
        assert len(parsed["data"]["artifacts"]) == 1


# ── IMP12: GlossaryIndex ──────────────────────────────────────────────────────


class TestGlossaryIndexImport:
    def test_glossary_index_importable(self):
        from blueprint_mcp.glossary import GlossaryIndex  # noqa: F401


class TestGlossaryIndexFromDocs:
    @pytest.fixture
    def glossary(self):
        from blueprint_mcp.glossary import GlossaryIndex

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        return GlossaryIndex.load(docs_root)

    def test_load_returns_glossary_instance(self, glossary):
        from blueprint_mcp.glossary import GlossaryIndex

        assert isinstance(glossary, GlossaryIndex)

    def test_term_count_is_positive(self, glossary):
        assert glossary.term_count() > 0

    def test_lookup_returns_string_or_none(self, glossary):
        result = glossary.lookup("gate")
        assert result is None or isinstance(result, str)

    def test_lookup_unknown_term_returns_none(self, glossary):
        result = glossary.lookup("zzznonsenseterm")
        assert result is None


class TestGlossaryIndexManual:
    @pytest.fixture
    def glossary(self):
        from blueprint_mcp.glossary import GlossaryIndex

        return GlossaryIndex(
            terms={"gate review": "A formal milestone review.", "risk scan": "Risk assessment."}
        )

    def test_lookup_exact_match(self, glossary):
        result = glossary.lookup("gate review")
        assert result == "A formal milestone review."

    def test_lookup_case_insensitive(self, glossary):
        result = glossary.lookup("Gate Review")
        assert result == "A formal milestone review."

    def test_lookup_partial_does_not_match(self, glossary):
        # "gate" alone should not match "gate review"
        result = glossary.lookup("gate")
        assert result is None

    def test_term_count(self, glossary):
        assert glossary.term_count() == 2

    def test_find_terms_in_text_returns_list(self, glossary):
        found = glossary.find_terms_in_text("We need a gate review before launch.")
        assert "gate review" in found

    def test_find_terms_in_text_empty_when_no_match(self, glossary):
        found = glossary.find_terms_in_text("Nothing relevant here.")
        assert found == []

    def test_find_terms_in_text_case_insensitive(self, glossary):
        found = glossary.find_terms_in_text("GATE REVIEW is required.")
        assert "gate review" in found

    def test_enrich_answer_adds_definitions(self, glossary):
        text = "Perform a gate review with a risk scan."
        enriched = glossary.enrich_answer(text)
        assert "gate review" in enriched.lower()
        assert "risk scan" in enriched.lower()
        # Enriched version should be longer (definitions appended)
        assert len(enriched) >= len(text)

    def test_enrich_answer_no_terms_unchanged(self, glossary):
        text = "Nothing relevant here."
        enriched = glossary.enrich_answer(text)
        assert text in enriched  # original text preserved


class TestAnswerQuestionGlossaryIntegration:
    """answer_question enriches response with glossary definitions when GlossaryIndex is set."""

    def _extract_json(self, result: str) -> dict:
        assert "```json" in result
        return json.loads(result.split("```json\n")[1].split("\n```")[0])

    def test_set_glossary_index_importable(self):
        from blueprint_mcp.server import set_glossary_index  # noqa: F401

    def test_set_glossary_index_accepts_none(self):
        from blueprint_mcp.server import set_glossary_index

        set_glossary_index(None)  # must not raise

    def test_answer_question_works_without_glossary(self):
        from pathlib import Path

        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import (
            answer_question,
            set_glossary_index,
            set_index,
            set_semantic_index,
        )

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        set_index(idx)
        set_semantic_index(None)
        set_glossary_index(None)

        result = answer_question("How do I classify risk?")
        assert len(result) > 100
        parsed = self._extract_json(result)
        assert parsed["tool"] == "answer_question"

    def test_answer_question_with_glossary_includes_glossary_flag(self):
        from pathlib import Path

        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.glossary import GlossaryIndex
        from blueprint_mcp.server import (
            answer_question,
            set_glossary_index,
            set_index,
            set_semantic_index,
        )

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        set_index(idx)
        set_semantic_index(None)

        glossary = GlossaryIndex(terms={"risk": "The potential for harm or negative impact."})
        set_glossary_index(glossary)

        result = answer_question("risk classification")
        assert len(result) > 100

        # cleanup
        set_glossary_index(None)
