"""Structured evidence schema for Gate Review workflows.

Evidence items represent artefacts a team brings to a Gate Review.
They carry a type, optional quality score, and gate association so that
agents can reason about completeness and quality programmatically.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class EvidenceType:
    DOCUMENT = "document"
    TEST_RESULT = "test_result"
    REVIEW_SIGN_OFF = "review_sign_off"
    ARTIFACT = "artifact"


# Keywords that trigger type inference from a free-text evidence string
_TYPE_HINTS: list[tuple[str, str]] = [
    ("test result", EvidenceType.TEST_RESULT),
    ("test report", EvidenceType.TEST_RESULT),
    ("golden set", EvidenceType.TEST_RESULT),
    ("benchmark", EvidenceType.TEST_RESULT),
    ("validation report", EvidenceType.TEST_RESULT),
    ("sign-off", EvidenceType.REVIEW_SIGN_OFF),
    ("sign off", EvidenceType.REVIEW_SIGN_OFF),
    ("guardian approval", EvidenceType.REVIEW_SIGN_OFF),
    ("approved by", EvidenceType.REVIEW_SIGN_OFF),
    ("legal review", EvidenceType.REVIEW_SIGN_OFF),
    ("diagram", EvidenceType.ARTIFACT),
    ("model card", EvidenceType.ARTIFACT),
    ("architecture", EvidenceType.ARTIFACT),
    ("prototype", EvidenceType.ARTIFACT),
    ("demo", EvidenceType.ARTIFACT),
]


@dataclass
class EvidenceItem:
    """A single piece of evidence submitted for a Gate Review.

    Attributes:
        title: Human-readable name of the evidence item.
        type: One of the EvidenceType constants.
        gate: Gate number this evidence belongs to (1–4).
        quality_score: Optional 0.0–1.0 quality indicator.
        path: Optional file or document path.
    """

    title: str
    type: str
    gate: int
    quality_score: float | None = None
    path: str | None = None


def _infer_type(text: str) -> str:
    """Infer EvidenceType from free text using keyword matching."""
    lower = text.lower()
    for keyword, etype in _TYPE_HINTS:
        if keyword in lower:
            return etype
    return EvidenceType.DOCUMENT


def parse_evidence(items: list[str], gate: int) -> list[EvidenceItem]:
    """Convert a list of free-text evidence strings into EvidenceItem objects.

    Args:
        items: List of evidence description strings.
        gate: Gate number to attach to each item.

    Returns:
        List of EvidenceItem instances with inferred types.
    """
    return [
        EvidenceItem(title=item.strip(), type=_infer_type(item), gate=gate)
        for item in items
        if item.strip()
    ]


def evidence_summary(items: list[EvidenceItem]) -> dict:
    """Produce a summary dict for a list of EvidenceItem objects.

    Args:
        items: Evidence items to summarise.

    Returns:
        Dict with ``count``, ``by_type`` (type → count), and
        ``avg_quality`` (None if no scores present).
    """
    by_type: dict[str, int] = {}
    scores: list[float] = []

    for item in items:
        by_type[item.type] = by_type.get(item.type, 0) + 1
        if item.quality_score is not None:
            scores.append(item.quality_score)

    return {
        "count": len(items),
        "by_type": by_type,
        "avg_quality": round(sum(scores) / len(scores), 2) if scores else None,
    }
