"""QW2 — Utility for detecting docs without 'answers:' frontmatter.

Scans docs/ for markdown files that lack an ``answers:`` key in their
frontmatter and generates candidate questions from title + body text.

Usage::

    from blueprint_mcp.missing_answers import find_missing_answers, generate_candidate_answers

    missing = find_missing_answers(docs_root, only_missing=True)
    for doc in missing:
        candidates = generate_candidate_answers(doc["title"], doc["body"])
        print(doc["path"], candidates)
"""

from __future__ import annotations

import re
from pathlib import Path

# ── Public API ────────────────────────────────────────────────────────────────


def find_missing_answers(docs_root: Path, only_missing: bool = False) -> list[dict]:
    """Scan *docs_root* for markdown files with/without ``answers:`` frontmatter.

    Args:
        docs_root: Root of the docs directory.
        only_missing: If ``True``, return only docs that lack ``answers:``.

    Returns:
        List of dicts with keys ``path``, ``title``, ``has_answers``, ``body``.
    """
    results: list[dict] = []

    for md_file in sorted(docs_root.rglob("*.md")):
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        meta, body = _split_frontmatter(text)
        has_answers = bool(meta.get("answers"))
        title = meta.get("title", "") or _title_from_body(body)

        if only_missing and has_answers:
            continue

        results.append(
            {
                "path": str(md_file.relative_to(docs_root)),
                "title": title,
                "has_answers": has_answers,
                "body": body[:500],  # trim for performance
            }
        )

    return results


def generate_candidate_answers(
    title: str,
    body: str,
    max_results: int = 5,
) -> list[str]:
    """Generate candidate ``answers:`` questions from a document's title and body.

    Uses simple heuristics: question templates filled with title keywords,
    plus any existing question-shaped sentences extracted from the body.

    Args:
        title: Document title.
        body: Document body text (first ~500 chars is sufficient).
        max_results: Maximum number of candidates to return.

    Returns:
        List of question strings, each ending with ``?``.
    """
    candidates: list[str] = []

    keywords = _extract_keywords(title)

    # Template-based questions from title keywords
    templates = [
        "What is {kw}?",
        "How does {kw} work?",
        "When should I use {kw}?",
        "What are the requirements for {kw}?",
        "How do I complete {kw}?",
    ]

    for template in templates:
        if not keywords:
            break
        kw = " ".join(keywords[:3])
        candidates.append(template.format(kw=kw))
        if len(candidates) >= max_results:
            break

    # Extract question-shaped sentences from body
    if len(candidates) < max_results and body:
        for sentence in re.split(r"[.!]\s+", body):
            sentence = sentence.strip()
            if sentence.endswith("?") and 10 < len(sentence) < 120:
                candidates.append(sentence)
                if len(candidates) >= max_results:
                    break

    # Fallback: title → question
    if not candidates:
        clean = title.strip().rstrip("?")
        candidates.append(f"What is {clean}?" if clean else "What does this document cover?")

    return candidates[:max_results]


# ── Internal helpers ──────────────────────────────────────────────────────────


def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (meta_dict, body) — simple frontmatter splitter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    return _parse_simple_yaml(yaml_block), body


def _parse_simple_yaml(block: str) -> dict:
    """Minimal frontmatter parser — handles scalar and list values."""
    meta: dict = {}
    for line in block.splitlines():
        m = re.match(r"^(\w[\w_-]*):\s*(.*)", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("["):
            items = [x.strip().strip("'\"") for x in raw.strip("[]").split(",") if x.strip()]
            meta[key] = items
        elif raw.startswith("'") or raw.startswith('"'):
            meta[key] = raw.strip("'\"")
        else:
            meta[key] = raw
    return meta


def _title_from_body(body: str) -> str:
    """Extract the first heading from *body* as a fallback title."""
    m = re.search(r"^#{1,3}\s+(.+)", body, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _extract_keywords(title: str) -> list[str]:
    """Return significant words from *title* (skip stop words, short tokens)."""
    _STOP = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "for",
        "of",
        "in",
        "to",
        "is",
        "are",
        "how",
        "what",
        "when",
    }
    tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9\-]*", title)
    return [t.lower() for t in tokens if t.lower() not in _STOP and len(t) > 2]
