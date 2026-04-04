"""Glossary-aware answer enrichment for Blueprint MCP tools.

The GlossaryIndex loads term definitions from the docs directory and can
enrich answer text by appending a definitions section for any terms found
in the text.

Usage::

    idx = GlossaryIndex.load(docs_root)
    found = idx.find_terms_in_text("We need a gate review.")
    enriched = idx.enrich_answer("We need a gate review.")
"""

from __future__ import annotations

import re
from pathlib import Path


class GlossaryIndex:
    """Index of glossary terms and their definitions.

    Args:
        terms: Dict mapping lowercase term strings to their definitions.
    """

    def __init__(self, terms: dict[str, str]) -> None:
        # Normalise keys to lowercase for case-insensitive lookup
        self._terms: dict[str, str] = {k.lower(): v for k, v in terms.items()}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @classmethod
    def load(cls, docs_root: Path) -> "GlossaryIndex":
        """Load glossary terms from markdown files under *docs_root*.

        Searches for files named ``glossary*.md`` or files that contain
        a ``## Glossary`` section. Terms are extracted from definition-list
        style markdown (``**term**``: definition) or table rows.

        Args:
            docs_root: Root of the docs directory.

        Returns:
            A :class:`GlossaryIndex` instance (may have 0 terms if none found).
        """
        terms: dict[str, str] = {}

        # Find glossary files — by name or by content markers
        _GLOSSARY_MARKERS = ("glossary", "termenlijst", "woordenlijst")
        for path in sorted(docs_root.rglob("*.md")):
            name_lower = path.name.lower()
            parent_lower = path.parent.name.lower()
            is_glossary_file = any(m in name_lower or m in parent_lower for m in _GLOSSARY_MARKERS)
            if not is_glossary_file:
                # Check for in-content glossary markers (read only first 200 chars)
                try:
                    head = path.read_text(encoding="utf-8", errors="ignore")[:500]
                except OSError:
                    continue
                if not any(m in head.lower() for m in _GLOSSARY_MARKERS):
                    continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            terms.update(cls._parse_glossary_text(text))

        return cls(terms=terms)

    def lookup(self, term: str) -> str | None:
        """Return the definition for an exact *term* (case-insensitive), or ``None``."""
        return self._terms.get(term.lower())

    def term_count(self) -> int:
        """Return the number of terms in the index."""
        return len(self._terms)

    def find_terms_in_text(self, text: str) -> list[str]:
        """Return all glossary terms that appear in *text* (case-insensitive).

        Returns canonical lowercase term strings.
        """
        lower = text.lower()
        return [term for term in self._terms if term in lower]

    def enrich_answer(self, text: str) -> str:
        """Append a **Definitions** section to *text* for any recognised terms.

        If no glossary terms are found in *text*, the original text is returned
        unchanged.

        Args:
            text: Answer text to enrich.

        Returns:
            Original text, optionally extended with a definitions block.
        """
        found = self.find_terms_in_text(text)
        if not found:
            return text

        definitions = "\n".join(
            f"- **{term}**: {self._terms[term]}" for term in sorted(found)
        )
        return f"{text}\n\n**Definitions**\n\n{definitions}"

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_glossary_text(text: str) -> dict[str, str]:
        """Extract term→definition pairs from markdown text.

        Supports two common patterns:
        1. ``**term**: definition`` — bold definition-list style
        2. ``| term | definition |`` — markdown table rows
        """
        terms: dict[str, str] = {}

        # Pattern 1: **term**: definition
        for match in re.finditer(r"\*\*([^*]+)\*\*\s*[:\-]\s*(.+)", text):
            term = match.group(1).strip().lower()
            definition = match.group(2).strip()
            if term and definition:
                terms[term] = definition

        # Pattern 2: | term | definition | (skip header/separator rows)
        for line in text.splitlines():
            if line.startswith("|") and "---" not in line:
                parts = [p.strip() for p in line.strip("|").split("|")]
                if len(parts) >= 2 and parts[0] and parts[1]:
                    term = parts[0].lower()
                    definition = parts[1]
                    if not any(c in term for c in ("=", "#", "*")):
                        terms[term] = definition

        return terms
