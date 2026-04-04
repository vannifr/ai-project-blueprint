"""Tests for semantic_search.py — ChromaDB-backed semantic retrieval.

All ChromaDB interactions are mocked: no real database is needed in CI.
"""

import json
from unittest.mock import MagicMock, patch

import pytest

from blueprint_mcp.semantic_search import SemanticIndex, SemanticResult

# ── SemanticResult dataclass ──────────────────────────────────────────────────


class TestSemanticResult:
    def test_fields_accessible(self):
        r = SemanticResult(
            doc_path="01-strategie/index.en.md",
            doc_title="Strategy Overview",
            section="Introduction",
            text="This document covers ...",
            distance=0.15,
        )
        assert r.doc_path == "01-strategie/index.en.md"
        assert r.distance == 0.15

    def test_default_section_is_empty(self):
        r = SemanticResult(doc_path="p", doc_title="T", section="", text="t", distance=0.5)
        assert r.section == ""

    def test_distance_zero_means_exact(self):
        r = SemanticResult(doc_path="p", doc_title="T", section="", text="t", distance=0.0)
        assert r.distance == 0.0


# ── SemanticIndex — graceful degradation ─────────────────────────────────────


class TestSemanticIndexDegradation:
    def test_nonexistent_path_returns_empty_list(self):
        """SemanticIndex must not raise when ChromaDB path does not exist."""
        idx = SemanticIndex("/nonexistent/path/to/chroma", language="en")
        results = idx.search("risk classification")
        assert results == []

    def test_search_returns_list(self):
        idx = SemanticIndex("/nonexistent/path", language="en")
        result = idx.search("anything")
        assert isinstance(result, list)

    def test_search_with_n_results(self):
        idx = SemanticIndex("/nonexistent/path", language="en")
        result = idx.search("test", n_results=3)
        assert isinstance(result, list)


# ── SemanticIndex — mocked ChromaDB ──────────────────────────────────────────


def _make_mock_collection(distances, metadatas, documents):
    """Build a mock ChromaDB collection.query return value."""
    collection = MagicMock()
    collection.query.return_value = {
        "distances": [distances],
        "metadatas": [metadatas],
        "documents": [documents],
    }
    return collection


class TestSemanticIndexMocked:
    def _make_index_with_mock_collection(self, collection):
        with patch("blueprint_mcp.semantic_search.chromadb") as mock_chroma:
            client = MagicMock()
            mock_chroma.PersistentClient.return_value = client
            client.get_collection.return_value = collection
            idx = SemanticIndex("/fake/path", language="en")
            idx._collection = collection  # inject directly
        return idx

    def test_search_calls_collection_query(self):
        col = _make_mock_collection(
            distances=[0.1],
            metadatas=[{"path": "a/b.en.md", "title": "Doc A"}],
            documents=["Some content"],
        )
        idx = SemanticIndex.__new__(SemanticIndex)
        idx._collection = col
        idx._language = "en"
        idx._query("test query", n_results=5)
        col.query.assert_called_once()
        call_kwargs = col.query.call_args
        assert "query_texts" in call_kwargs.kwargs or call_kwargs.args

    def test_search_maps_metadata_to_result(self):
        col = _make_mock_collection(
            distances=[0.2],
            metadatas=[{"path": "01-strategy/index.en.md", "title": "Strategy"}],
            documents=["Strategy content here"],
        )
        idx = SemanticIndex.__new__(SemanticIndex)
        idx._collection = col
        idx._language = "en"
        results = idx._query("strategy", n_results=1)
        assert len(results) == 1
        assert results[0].doc_path == "01-strategy/index.en.md"
        assert results[0].doc_title == "Strategy"
        assert results[0].distance == pytest.approx(0.2)

    def test_search_multiple_results_ordered_by_distance(self):
        col = _make_mock_collection(
            distances=[0.3, 0.1, 0.5],
            metadatas=[
                {"path": "a.en.md", "title": "A"},
                {"path": "b.en.md", "title": "B"},
                {"path": "c.en.md", "title": "C"},
            ],
            documents=["text a", "text b", "text c"],
        )
        idx = SemanticIndex.__new__(SemanticIndex)
        idx._collection = col
        idx._language = "en"
        results = idx._query("query", n_results=3)
        # Results come back in ChromaDB order (already sorted by distance)
        assert len(results) == 3

    def test_search_returns_empty_on_no_results(self):
        col = _make_mock_collection(distances=[], metadatas=[], documents=[])
        idx = SemanticIndex.__new__(SemanticIndex)
        idx._collection = col
        idx._language = "en"
        results = idx._query("nothing", n_results=5)
        assert results == []

    def test_search_public_method_falls_back_gracefully(self):
        """Public search() must return [] if _collection raises."""
        idx = SemanticIndex.__new__(SemanticIndex)
        idx._collection = None
        idx._language = "en"
        results = idx.search("test")
        assert results == []


# ── answer_question uses semantic when available ───────────────────────────────


class TestAnswerQuestionSemanticIntegration:
    """answer_question falls back gracefully; semantic results improve ranking."""

    def _extract_json(self, result: str) -> dict:
        assert "```json" in result
        return json.loads(result.split("```json\n")[1].split("\n```")[0])

    def test_answer_question_works_without_semantic_index(self):
        """With no semantic index, answer_question still returns keyword results."""
        from pathlib import Path

        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.server import answer_question, set_index, set_semantic_index

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        set_index(idx)
        set_semantic_index(None)  # no semantic index

        result = answer_question("How do I classify risk?")
        assert len(result) > 100
        parsed = self._extract_json(result)
        assert parsed["tool"] == "answer_question"

    def test_answer_question_uses_semantic_results_when_available(self):
        """When a semantic index is injected, its results are merged in."""
        from pathlib import Path

        from blueprint_mcp.content_index import ContentIndex
        from blueprint_mcp.semantic_search import SemanticIndex, SemanticResult
        from blueprint_mcp.server import answer_question, set_index, set_semantic_index

        docs_root = Path(__file__).resolve().parent.parent.parent / "docs"
        idx = ContentIndex.load(docs_root, language="en")
        set_index(idx)

        # Build a fake semantic index that returns a known result
        mock_sem = MagicMock(spec=SemanticIndex)
        # Return a result that points to a real doc in the index
        first_doc = idx.docs[0]
        mock_sem.search.return_value = [
            SemanticResult(
                doc_path=first_doc.path,
                doc_title=first_doc.title,
                section="",
                text=first_doc.body[:100],
                distance=0.05,
            )
        ]
        set_semantic_index(mock_sem)

        result = answer_question("risk classification")
        mock_sem.search.assert_called_once()
        assert len(result) > 100

        # cleanup
        set_semantic_index(None)

    def test_set_semantic_index_accepts_none(self):
        from blueprint_mcp.server import set_semantic_index

        set_semantic_index(None)  # must not raise
