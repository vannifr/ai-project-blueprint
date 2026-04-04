"""Frontmatter parsing and enrichment utilities for Blueprint docs.

Provides pure functions for reading, updating, and writing YAML frontmatter
in markdown files.  The main entry point for batch enrichment is
:func:`enrich_file`.

Usage::

    meta, body = parse_frontmatter(text)
    updated = update_frontmatter(meta, {"last_reviewed": "2026-04-04"})
    new_text = render_frontmatter(updated, body)

    # Or directly on a file:
    changed = enrich_file(Path("docs/guide.md"), updates={"last_reviewed": "2026-04-04"})
"""

from __future__ import annotations

from pathlib import Path


try:
    import yaml  # type: ignore
    _YAML_AVAILABLE = True
except ImportError:
    yaml = None  # type: ignore
    _YAML_AVAILABLE = False


_FENCE = "---"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from *text*.

    Args:
        text: Full markdown file content.

    Returns:
        ``(meta_dict, body_string)`` where *meta_dict* is empty if no
        frontmatter was found and *body_string* is the content after the
        closing ``---`` fence (or the full text if no frontmatter).
    """
    if not text.startswith(_FENCE):
        return {}, text

    # Find the closing fence
    end = text.find(f"\n{_FENCE}", len(_FENCE))
    if end == -1:
        return {}, text

    yaml_block = text[len(_FENCE) + 1: end]
    body = text[end + len(_FENCE) + 1:]

    # Strip single leading newline from body
    if body.startswith("\n"):
        body = body[1:]

    if _YAML_AVAILABLE:
        try:
            meta = yaml.safe_load(yaml_block) or {}
        except yaml.YAMLError:
            meta = {}
    else:
        meta = _simple_parse(yaml_block)

    return meta, body


def update_frontmatter(meta: dict, updates: dict) -> dict:
    """Return a new dict with *updates* merged into *meta*.

    The original *meta* dict is not mutated.

    Args:
        meta: Existing frontmatter dict.
        updates: Key/value pairs to add or overwrite.

    Returns:
        New dict with all original keys plus *updates*.
    """
    return {**meta, **updates}


def render_frontmatter(meta: dict, body: str) -> str:
    """Render *meta* and *body* back to a markdown string.

    If *meta* is empty, returns *body* unchanged (no fence added).

    Args:
        meta: Frontmatter dict.
        body: Markdown body content.

    Returns:
        Full markdown string with ``---`` fences if meta is non-empty.
    """
    if not meta:
        return body

    if _YAML_AVAILABLE:
        yaml_text = yaml.dump(meta, allow_unicode=True, default_flow_style=False, sort_keys=True)
    else:
        yaml_text = _simple_dump(meta)

    return f"{_FENCE}\n{yaml_text}{_FENCE}\n\n{body}"


def enrich_file(path: Path, updates: dict, overwrite: bool = True) -> bool:
    """Add or update frontmatter keys in a markdown file on disk.

    Args:
        path: Path to the markdown file.
        updates: Frontmatter keys to add/update.
        overwrite: If ``False``, skip keys that already exist in the
            frontmatter (default ``True``).

    Returns:
        ``True`` if the file was modified, ``False`` if no changes were needed.
    """
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    effective_updates: dict = {}
    for key, value in updates.items():
        if not overwrite and key in meta:
            continue
        effective_updates[key] = value

    if not effective_updates:
        return False

    new_meta = update_frontmatter(meta, effective_updates)
    new_text = render_frontmatter(new_meta, body)
    path.write_text(new_text, encoding="utf-8")
    return True


# ── Fallback parsers (when PyYAML is not installed) ──────────────────────────


def _simple_parse(yaml_block: str) -> dict:
    """Minimal YAML parser for simple key: value and key: [list] lines."""
    import re
    result: dict = {}
    for line in yaml_block.splitlines():
        m = re.match(r"^(\w[\w_-]*):\s*(.*)", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            items = [x.strip().strip("'\"") for x in raw[1:-1].split(",") if x.strip()]
            result[key] = items
        elif raw.startswith("'") and raw.endswith("'"):
            result[key] = raw[1:-1]
        elif raw.startswith('"') and raw.endswith('"'):
            result[key] = raw[1:-1]
        else:
            result[key] = raw
    return result


def _simple_dump(meta: dict) -> str:
    """Minimal YAML serialiser for simple dicts."""
    lines = []
    for key in sorted(meta):
        val = meta[key]
        if isinstance(val, list):
            lines.append(f"{key}: [{', '.join(str(v) for v in val)}]")
        elif isinstance(val, str) and any(c in val for c in (":", "#", "'")):
            lines.append(f"{key}: '{val}'")
        else:
            lines.append(f"{key}: {val}")
    return "\n".join(lines) + "\n"
