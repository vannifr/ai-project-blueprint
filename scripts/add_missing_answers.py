#!/usr/bin/env python3
"""QW2 — Add missing 'answers:' frontmatter to Blueprint docs.

Scans docs/ for markdown files without an 'answers:' key and optionally
writes generated candidate questions back to the file.

Usage::

    # Show what would be added (dry run)
    python scripts/add_missing_answers.py --dry-run

    # Limit to first 10 missing docs
    python scripts/add_missing_answers.py --dry-run --limit 10

    # Write candidates to files (adds answers: frontmatter)
    python scripts/add_missing_answers.py --write

    # Only process a specific directory
    python scripts/add_missing_answers.py --dry-run --dir docs/01-ai-native-fundamenten

Exit codes:
    0 — success
    1 — error
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running from repo root without installing
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "mcp_server" / "src"))

from blueprint_mcp.missing_answers import (  # noqa: E402
    find_missing_answers,
    generate_candidate_answers,
)


def _write_answers_to_file(md_file: Path, candidates: list[str]) -> bool:
    """Inject 'answers:' key into the frontmatter of *md_file*.

    Returns True if the file was modified.
    """
    text = md_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        # No frontmatter — prepend one
        yaml_answers = _format_answers_yaml(candidates)
        new_text = f"---\n{yaml_answers}---\n\n{text}"
        md_file.write_text(new_text, encoding="utf-8")
        return True

    end = text.find("\n---", 3)
    if end == -1:
        return False

    frontmatter = text[4:end]
    if "answers:" in frontmatter:
        return False  # already present

    yaml_answers = _format_answers_yaml(candidates)
    new_frontmatter = frontmatter.rstrip() + "\n" + yaml_answers
    new_text = f"---\n{new_frontmatter}---{text[end + 4:]}"
    md_file.write_text(new_text, encoding="utf-8")
    return True


def _format_answers_yaml(candidates: list[str]) -> str:
    items = "\n".join(f"  - '{q}'" for q in candidates)
    return f"answers:\n{items}\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add missing 'answers:' frontmatter to Blueprint docs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Print what would be written without modifying files.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write generated answers back to files.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Process at most N missing docs (0 = no limit).",
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=None,
        help="Restrict scan to a sub-directory of docs/.",
    )
    parser.add_argument(
        "--docs",
        type=Path,
        default=None,
        help="Path to docs/ directory (default: auto-detect).",
    )
    args = parser.parse_args()

    if not args.dry_run and not args.write:
        args.dry_run = True  # default to dry-run for safety

    docs_root = args.docs or (_ROOT / "docs")
    if not docs_root.exists():
        print(f"Error: docs directory not found at {docs_root}", file=sys.stderr)
        return 1

    scan_root = args.dir if args.dir else docs_root
    if not scan_root.exists():
        print(f"Error: directory not found: {scan_root}", file=sys.stderr)
        return 1

    missing = find_missing_answers(scan_root, only_missing=True)
    if args.limit:
        missing = missing[: args.limit]

    if not missing:
        print("No docs without 'answers:' found.")
        return 0

    print(f"Found {len(missing)} doc(s) without 'answers:' frontmatter.\n")
    modified = 0

    for item in missing:
        candidates = generate_candidate_answers(item["title"], item["body"], max_results=3)
        path = scan_root / item["path"]

        print(f"  {item['path']}")
        for q in candidates:
            print(f"    - '{q}'")

        if args.write:
            changed = _write_answers_to_file(path, candidates)
            if changed:
                print("    → written")
                modified += 1

    if args.write:
        print(f"\nModified {modified} file(s).")
    else:
        print("\n(dry run — use --write to apply changes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
