"""ChromaDB-backed semantic search for the Blueprint MCP server.

The MCP server accesses ChromaDB read-only; it never writes to the database.
If ChromaDB is unavailable (not installed, path missing, collection absent),
every public method returns an empty list — the caller falls back to keyword search.

Usage::

    idx = SemanticIndex("/path/to/chroma_data", language="en")
    results = idx.search("risk classification", n_results=5)
    # results is a list[SemanticResult], empty on any failure

Environment variable::

    BLUEPRINT_CHROMA_PATH — overrides the path passed to the constructor.
"""

from __future__ import annotations

from dataclasses import dataclass

try:
    import chromadb  # type: ignore
    _CHROMADB_AVAILABLE = True
except ImportError:
    chromadb = None  # type: ignore
    _CHROMADB_AVAILABLE = False


@dataclass
class SemanticResult:
    """A single semantic search hit from ChromaDB.

    Attributes:
        doc_path: Relative path of the source document (matches ContentIndex keys).
        doc_title: Human-readable title from the document metadata.
        section: Section heading within the document (may be empty).
        text: The chunk of text that was matched.
        distance: Embedding distance — lower is more relevant.
    """

    doc_path: str
    doc_title: str
    section: str
    text: str
    distance: float


class SemanticIndex:
    """Read-only wrapper around a ChromaDB collection for semantic search.

    Initialisation is lazy: the ChromaDB client is not opened until the first
    :meth:`search` call. If the client cannot be opened or the collection does
    not exist, :meth:`search` returns an empty list.

    Args:
        chroma_path: Filesystem path to the ChromaDB ``chroma_data`` directory.
        language: ``"en"`` (default) or ``"nl"`` — selects the collection.
    """

    _COLLECTION_NAMES = {"en": "blueprint_en", "nl": "blueprint_nl"}

    def __init__(self, chroma_path: str, language: str = "en") -> None:
        self._chroma_path = chroma_path
        self._language = language
        self._collection = None   # lazily initialised

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search(self, query: str, n_results: int = 5) -> list[SemanticResult]:
        """Search the ChromaDB collection for chunks semantically similar to *query*.

        Args:
            query: Natural language query string.
            n_results: Maximum number of results to return.

        Returns:
            List of :class:`SemanticResult` objects, empty on any failure.
        """
        try:
            return self._query(query, n_results=n_results)
        except Exception:
            return []

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get_collection(self):
        """Return the ChromaDB collection, initialising it on first call."""
        if self._collection is not None:
            return self._collection
        if not _CHROMADB_AVAILABLE:
            raise RuntimeError("chromadb is not installed")
        collection_name = self._COLLECTION_NAMES.get(self._language, "blueprint_en")
        client = chromadb.PersistentClient(path=self._chroma_path)
        self._collection = client.get_collection(name=collection_name)
        return self._collection

    def _query(self, query: str, n_results: int = 5) -> list[SemanticResult]:
        """Execute the ChromaDB query and map results to SemanticResult objects."""
        collection = self._get_collection()
        if collection is None:
            return []

        response = collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["distances", "metadatas", "documents"],
        )

        distances = response.get("distances", [[]])[0]
        metadatas = response.get("metadatas", [[]])[0]
        documents = response.get("documents", [[]])[0]

        results: list[SemanticResult] = []
        for dist, meta, doc_text in zip(distances, metadatas, documents):
            results.append(
                SemanticResult(
                    doc_path=meta.get("path", ""),
                    doc_title=meta.get("title", ""),
                    section=meta.get("section", ""),
                    text=doc_text or "",
                    distance=float(dist),
                )
            )
        return results
