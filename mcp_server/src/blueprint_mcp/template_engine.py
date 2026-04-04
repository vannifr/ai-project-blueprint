"""Template placeholder parsing and filling for Blueprint templates.

Templates use ``{{placeholder_name}}`` syntax. Whitespace inside
braces is stripped, so ``{{ name }}`` and ``{{name}}`` are equivalent.

Usage::

    placeholders = parse_placeholders(template_text)
    filled, missing = fill_placeholders(template_text, {"project_name": "Atlas"})
"""

from __future__ import annotations

import re

_PLACEHOLDER_RE = re.compile(r"\{\{\s*(\w+)\s*\}\}")


def parse_placeholders(text: str) -> list[str]:
    """Return a deduplicated list of placeholder names found in *text*.

    Args:
        text: Template body (may contain ``{{placeholder}}`` tokens).

    Returns:
        Sorted, unique list of placeholder name strings.
    """
    found = _PLACEHOLDER_RE.findall(text)
    # Deduplicate while preserving order
    seen: set[str] = set()
    result: list[str] = []
    for name in found:
        if name not in seen:
            seen.add(name)
            result.append(name)
    return result


def fill_placeholders(text: str, values: dict[str, str]) -> tuple[str, list[str]]:
    """Replace ``{{placeholder}}`` tokens in *text* with values from *values*.

    Args:
        text: Template body with ``{{placeholder}}`` tokens.
        values: Dict mapping placeholder names to replacement strings.

    Returns:
        A tuple ``(filled_text, missing_placeholders)`` where
        ``missing_placeholders`` lists names that were not in *values*.
    """
    placeholders = parse_placeholders(text)
    missing: list[str] = [p for p in placeholders if p not in values]

    def replacer(match: re.Match) -> str:
        name = match.group(1).strip()
        return values.get(name, match.group(0))  # leave token intact if missing

    filled = _PLACEHOLDER_RE.sub(replacer, text)
    return filled, missing
