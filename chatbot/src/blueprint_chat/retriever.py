"""Retrieve relevant chunks from ChromaDB based on user questions."""

from __future__ import annotations

import chromadb
from openai import OpenAI

from .config import settings
from .models import Source

# Dutch stop words for language detection
NL_STOP_WORDS = {
    "de", "het", "een", "van", "in", "is", "dat", "op", "te", "en", "voor",
    "zijn", "met", "niet", "aan", "er", "maar", "om", "ook", "als", "bij",
    "dit", "die", "wat", "hoe", "welke", "wanneer", "waar", "waarom", "kan",
    "moet", "hebben", "worden", "nog", "wel", "dan", "naar", "meer", "over",
    "uit", "tot", "door", "hun", "mijn", "we", "ze", "ik", "wij", "ons",
}


def detect_language(text: str) -> str:
    """Detect if text is Dutch or English based on stop word frequency."""
    words = set(text.lower().split())
    nl_matches = len(words & NL_STOP_WORDS)
    return "nl" if nl_matches >= 2 else "en"


def get_chroma_client() -> chromadb.PersistentClient:
    """Get or create a persistent ChromaDB client."""
    return chromadb.PersistentClient(path=settings.chroma_path)


def get_collection(client: chromadb.PersistentClient, language: str) -> chromadb.Collection:
    """Get a ChromaDB collection by language."""
    name = f"blueprint_{language}"
    return client.get_collection(name=name)


def embed_query(text: str) -> list[float]:
    """Embed a query string using OpenAI."""
    client = OpenAI(api_key=settings.openai_api_key)
    response = client.embeddings.create(
        model=settings.embedding_model,
        input=text,
    )
    return response.data[0].embedding


def doc_path_to_url(doc_path: str, language: str) -> str:
    """Convert a document path to a site URL."""
    # Remove .en.md or .md extension
    path = doc_path.replace(".en.md", "").replace(".md", "")
    # Remove index suffix (MkDocs serves index.md as directory)
    if path.endswith("/index"):
        path = path[:-6]
    elif path == "index":
        path = ""
    base = "https://ai-delivery.io"
    if language == "en":
        return f"{base}/en/{path}/" if path else f"{base}/en/"
    return f"{base}/{path}/" if path else f"{base}/"


class Retriever:
    """Retrieve relevant document chunks for a question."""

    def __init__(self, chroma_client: chromadb.PersistentClient | None = None):
        self.client = chroma_client or get_chroma_client()

    def retrieve(
        self,
        question: str,
        language: str = "auto",
        max_results: int | None = None,
    ) -> tuple[list[dict], str]:
        """Retrieve relevant chunks for a question.

        Returns (chunks, detected_language) where each chunk is a dict with
        keys: text, doc_path, doc_title, section, url, distance.
        """
        if language == "auto":
            language = detect_language(question)

        n = max_results or settings.max_chunks
        collection = get_collection(self.client, language)
        query_embedding = embed_query(question)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n,
            include=["documents", "metadatas", "distances"],
        )

        chunks = []
        if results["documents"] and results["documents"][0]:
            for i, text in enumerate(results["documents"][0]):
                meta = results["metadatas"][0][i] if results["metadatas"] else {}
                distance = results["distances"][0][i] if results["distances"] else 1.0
                doc_path = meta.get("doc_path", "")
                chunks.append({
                    "text": text,
                    "doc_path": doc_path,
                    "doc_title": meta.get("doc_title", ""),
                    "section": meta.get("section", ""),
                    "url": doc_path_to_url(doc_path, language),
                    "distance": distance,
                })

        return chunks, language

    def to_sources(self, chunks: list[dict]) -> list[Source]:
        """Convert retrieved chunks to Source models for the response."""
        seen = set()
        sources = []
        for chunk in chunks:
            url = chunk["url"]
            if url not in seen:
                seen.add(url)
                sources.append(Source(
                    title=chunk["doc_title"],
                    url=url,
                    section=chunk.get("section"),
                ))
        return sources
