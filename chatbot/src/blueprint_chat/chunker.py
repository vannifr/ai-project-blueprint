"""Split Blueprint markdown documents into semantic chunks for RAG retrieval."""

import re
from dataclasses import dataclass, field
from pathlib import Path

RE_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RE_H1 = re.compile(r"^#\s+(.+)$", re.MULTILINE)
RE_H2 = re.compile(r"^##\s+(.+)$", re.MULTILINE)

# Rough token estimate: 1 token ≈ 4 characters for English/Dutch
TOKEN_ESTIMATE_RATIO = 4
MAX_CHUNK_TOKENS = 800
MAX_CHUNK_CHARS = MAX_CHUNK_TOKENS * TOKEN_ESTIMATE_RATIO


def parse_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter using simple regex (mirrors content_index.py)."""
    m = RE_FRONTMATTER.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = [item.strip().strip("'\"") for item in inner.split(",")]
                fm[key] = items
        else:
            fm[key] = value.strip("'\"")
    return fm


def extract_body(text: str) -> str:
    """Return markdown content without frontmatter."""
    m = RE_FRONTMATTER.match(text)
    return text[m.end():] if m else text


def extract_title(body: str) -> str:
    """Extract first H1 heading from markdown body."""
    m = RE_H1.search(body)
    return m.group(1).strip() if m else ""


@dataclass
class Chunk:
    id: str
    text: str
    doc_path: str
    doc_title: str
    section: str
    language: str
    metadata: dict = field(default_factory=dict)


def _split_at_paragraphs(text: str, max_chars: int) -> list[str]:
    """Split oversized text at paragraph boundaries."""
    paragraphs = text.split("\n\n")
    parts = []
    current = ""
    for para in paragraphs:
        if current and len(current) + len(para) + 2 > max_chars:
            parts.append(current.strip())
            current = para
        else:
            current = current + "\n\n" + para if current else para
    if current.strip():
        parts.append(current.strip())
    return parts if parts else [text]


def chunk_document(
    text: str,
    rel_path: str,
    language: str,
) -> list[Chunk]:
    """Split a markdown document into chunks at H2 boundaries.

    Each chunk inherits the document's frontmatter metadata.
    Oversized sections are split further at paragraph boundaries.
    """
    fm = parse_frontmatter(text)
    body = extract_body(text)
    title = extract_title(body)

    # Split body at H2 headings
    sections: list[tuple[str, str]] = []  # (heading, content)
    h2_matches = list(RE_H2.finditer(body))

    if not h2_matches:
        # No H2 headings — entire body is one chunk
        sections.append(("", body.strip()))
    else:
        # Content before first H2
        preamble = body[:h2_matches[0].start()].strip()
        if preamble:
            sections.append(("", preamble))

        # Each H2 section
        for i, match in enumerate(h2_matches):
            heading = match.group(1).strip()
            start = match.end()
            end = h2_matches[i + 1].start() if i + 1 < len(h2_matches) else len(body)
            content = body[start:end].strip()
            sections.append((heading, content))

    # Build chunks, splitting oversized sections
    chunks = []
    chunk_idx = 0
    for heading, content in sections:
        if not content:
            continue

        # Combine heading with content for context
        full_text = f"## {heading}\n\n{content}" if heading else content

        if len(full_text) > MAX_CHUNK_CHARS:
            sub_parts = _split_at_paragraphs(full_text, MAX_CHUNK_CHARS)
            for sub in sub_parts:
                chunks.append(Chunk(
                    id=f"{language}::{rel_path}::{chunk_idx}",
                    text=sub,
                    doc_path=rel_path,
                    doc_title=title,
                    section=heading,
                    language=language,
                    metadata={
                        "summary": fm.get("summary", ""),
                        "type": fm.get("type", ""),
                        "phase": fm.get("phase", []),
                        "roles": fm.get("roles", []),
                        "tags": fm.get("tags", []),
                    },
                ))
                chunk_idx += 1
        else:
            chunks.append(Chunk(
                id=f"{language}::{rel_path}::{chunk_idx}",
                text=full_text,
                doc_path=rel_path,
                doc_title=title,
                section=heading,
                language=language,
                metadata={
                    "summary": fm.get("summary", ""),
                    "type": fm.get("type", ""),
                    "phase": fm.get("phase", []),
                    "roles": fm.get("roles", []),
                    "tags": fm.get("tags", []),
                },
            ))
            chunk_idx += 1

    return chunks


def chunk_all_docs(docs_root: Path, language: str = "nl") -> list[Chunk]:
    """Chunk all markdown documents in a docs directory."""
    all_chunks = []
    docs_root = Path(docs_root)

    for md_path in sorted(docs_root.rglob("*.md")):
        rel = md_path.relative_to(docs_root).as_posix()

        # Language filtering
        if language == "en" and not rel.endswith(".en.md"):
            continue
        if language == "nl" and rel.endswith(".en.md"):
            continue

        # Skip non-content files
        if rel.startswith(("llms", "robots", "qa-index", "stylesheets")):
            continue
        if rel.endswith(".htaccess"):
            continue

        text = md_path.read_text(encoding="utf-8")
        chunks = chunk_document(text, rel, language)
        all_chunks.extend(chunks)

    return all_chunks
