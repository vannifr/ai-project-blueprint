"""Build ChromaDB index from Blueprint documentation."""

from pathlib import Path

import chromadb
from openai import OpenAI

from .chunker import chunk_all_docs
from .config import settings


def build_index(
    docs_root: Path | str,
    chroma_path: str | None = None,
    languages: list[str] | None = None,
) -> dict[str, int]:
    """Build ChromaDB collections for the Blueprint documentation.

    Returns dict mapping language to number of chunks indexed.
    """
    docs_root = Path(docs_root)
    chroma_path = chroma_path or settings.chroma_path
    languages = languages or ["nl", "en"]

    client = chromadb.PersistentClient(path=chroma_path)
    openai_client = OpenAI(api_key=settings.openai_api_key)

    stats = {}

    for lang in languages:
        collection_name = f"blueprint_{lang}"

        # Delete existing collection if present (idempotent rebuild)
        try:
            client.delete_collection(collection_name)
        except ValueError:
            pass

        collection = client.create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

        chunks = chunk_all_docs(docs_root, language=lang)
        if not chunks:
            stats[lang] = 0
            continue

        # Batch embed and upsert
        batch_size = 100
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            texts = [c.text for c in batch]

            response = openai_client.embeddings.create(
                model=settings.embedding_model,
                input=texts,
            )
            embeddings = [e.embedding for e in response.data]

            collection.upsert(
                ids=[c.id for c in batch],
                documents=texts,
                embeddings=embeddings,
                metadatas=[
                    {
                        "doc_path": c.doc_path,
                        "doc_title": c.doc_title,
                        "section": c.section,
                        "language": c.language,
                        "type": c.metadata.get("type", ""),
                        "summary": c.metadata.get("summary", ""),
                    }
                    for c in batch
                ],
            )

        stats[lang] = len(chunks)

    return stats
