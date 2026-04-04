"""Confidence scoring for Blueprint search results.

Scores a document's relevance to a query on a 0.0–1.0 scale.
Used by search_content and answer_question to surface the most
relevant matches to calling agents.

Usage::

    scorer = ConfidenceScorer()
    score = scorer.score(query="risk classification", title="Risk Framework", body="...")

    # Or convenience wrapper for ContentIndex docs:
    from blueprint_mcp.confidence import score_result
    s = score_result(query="gate review", doc=some_doc)
"""

from __future__ import annotations

import re


class ConfidenceScorer:
    """Keyword-based confidence scorer.

    Scoring factors (all clamped to 0.0–1.0):

    - **Title exact match** (0.4 bonus) — all query keywords present in title
    - **Title partial match** (0.2 bonus) — any query keyword in title
    - **Body keyword density** (up to 0.4) — proportion of query keywords
      found in body, weighted by repetition (log-scaled, capped)
    - **Answers match** (0.2 bonus) — any query keyword in answers list
    """

    def score(
        self,
        query: str,
        title: str,
        body: str,
        answers: list[str] | None = None,
    ) -> float:
        """Return a confidence score in [0.0, 1.0]."""
        if not query:
            return 0.0
        if not title and not body:
            return 0.0

        keywords = _tokenise(query)
        if not keywords:
            return 0.0

        title_lower = title.lower()
        body_lower = body.lower()

        # Title match
        title_hits = sum(1 for kw in keywords if kw in title_lower)
        if title_hits == len(keywords):
            title_score = 0.4
        elif title_hits > 0:
            title_score = 0.2 * (title_hits / len(keywords))
        else:
            title_score = 0.0

        # Body keyword density
        body_score = 0.0
        if body_lower:
            total_hits = sum(body_lower.count(kw) for kw in keywords)
            # Cap at 10 hits to avoid over-rewarding keyword stuffing
            density = min(total_hits, 10) / 10
            body_score = 0.4 * density

        # Answers match
        answers_score = 0.0
        if answers:
            answers_text = " ".join(answers).lower()
            if any(kw in answers_text for kw in keywords):
                answers_score = 0.2

        raw = title_score + body_score + answers_score
        return round(min(raw, 1.0), 4)


def score_result(query: str, doc) -> float:
    """Convenience wrapper: score a ContentIndex document against a query.

    Args:
        query: Natural language query string.
        doc: A ``Doc`` object from ``ContentIndex``.

    Returns:
        Confidence score in [0.0, 1.0].
    """
    scorer = ConfidenceScorer()
    return scorer.score(
        query=query,
        title=getattr(doc, "title", ""),
        body=getattr(doc, "body", ""),
        answers=getattr(doc, "answers", []) or [],
    )


# ── Internal helpers ──────────────────────────────────────────────────────────


def _tokenise(text: str) -> list[str]:
    """Split text into lowercase tokens, removing stop words."""
    _STOPWORDS = {"how", "do", "i", "the", "a", "an", "is", "are", "to", "in", "of", "for", "what"}
    tokens = re.findall(r"[a-z]+", text.lower())
    return [t for t in tokens if t not in _STOPWORDS and len(t) > 1]
