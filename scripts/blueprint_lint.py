#!/usr/bin/env python3
"""Blueprint Lint — artefact-completeness and link-integrity checker.

Validates that each lifecycle phase has the required document types present
in docs/ and checks internal Markdown link integrity.

Usage::

    python scripts/blueprint_lint.py                  # lint all phases
    python scripts/blueprint_lint.py --phase 2        # lint one phase
    python scripts/blueprint_lint.py --phase 2 --verbose
    python scripts/blueprint_lint.py --links-only     # only check links

Exit codes:
    0 — all checks passed
    1 — one or more checks failed (missing artefacts or broken links)
    2 — usage error (invalid phase number etc.)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Required document types per phase (minimum set)
_REQUIRED_TYPES: dict[int, list[str]] = {
    1: ["objectives", "activities", "deliverables", "template"],
    2: ["objectives", "activities", "deliverables", "template"],
    3: ["objectives", "activities", "deliverables", "template"],
    4: ["objectives", "activities", "deliverables", "template"],
    5: ["objectives", "activities", "deliverables", "template"],
}

_VALID_PHASES = set(_REQUIRED_TYPES.keys())

# Frontmatter type keyword → canonical type (lowercased)
_TYPE_ALIASES: dict[str, str] = {
    "objectives": "objectives",
    "activities": "activities",
    "deliverables": "deliverables",
    "template": "template",
    "guide": "guide",
    "index": "index",
    "cheatsheet": "cheatsheet",
    "assessment": "assessment",
    "pattern": "pattern",
    "compliance": "compliance",
}


# ── Public API (importable by tests) ─────────────────────────────────────────


def lint_phase(phase: int, docs_root: Path) -> list[dict]:
    """Check artefact completeness for a single *phase*.

    Args:
        phase: Lifecycle phase number (1–5).
        docs_root: Root of the docs directory.

    Returns:
        List of check result dicts with keys:
        ``phase``, ``check``, ``status`` (ok/missing/warning/error), ``detail``.
    """
    if phase not in _VALID_PHASES:
        return [
            {
                "phase": phase,
                "check": "phase_valid",
                "status": "error",
                "detail": f"Phase {phase} is not valid. Must be one of {sorted(_VALID_PHASES)}.",
            }
        ]

    found_types = _collect_types_for_phase(phase, docs_root)
    results: list[dict] = []

    for required_type in _REQUIRED_TYPES[phase]:
        if required_type in found_types:
            results.append(
                {
                    "phase": phase,
                    "check": f"{required_type}_present",
                    "status": "ok",
                    "detail": f"Found {found_types[required_type]} '{required_type}' document(s) for phase {phase}.",
                }
            )
        else:
            results.append(
                {
                    "phase": phase,
                    "check": f"{required_type}_present",
                    "status": "missing",
                    "detail": f"No '{required_type}' document found for phase {phase}.",
                }
            )

    return results


def lint_all(docs_root: Path) -> dict:
    """Run :func:`lint_phase` for all phases and return a summary.

    Returns:
        Dict with keys:
        - ``phases``: list of per-phase result lists
        - ``summary``: ``{total_checks, ok, missing, warning, error}``
    """
    phases: list[list[dict]] = []
    totals: dict[str, int] = {"total_checks": 0, "ok": 0, "missing": 0, "warning": 0, "error": 0}

    for phase in sorted(_VALID_PHASES):
        results = lint_phase(phase, docs_root)
        phases.append(results)
        for item in results:
            totals["total_checks"] += 1
            status = item["status"]
            if status in totals:
                totals[status] += 1

    return {"phases": phases, "summary": totals}


def check_links(docs_root: Path) -> list[dict]:
    """Check internal Markdown links across all docs.

    Skips external URLs (http/https), anchors-only links (#…), and
    mailto: links. Classifies each link as:

    - ``ok`` — target file exists
    - ``broken`` — target file not found
    - ``external`` — https?:// link (not checked)
    - ``anchor`` — anchor-only (#…) link (not checked)

    Args:
        docs_root: Root of the docs directory.

    Returns:
        List of dicts with ``source``, ``target``, ``status``.
    """
    results: list[dict] = []
    md_link_re = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

    for md_file in sorted(docs_root.rglob("*.md")):
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for match in md_link_re.finditer(text):
            raw_target = match.group(2).strip()

            # Strip anchor fragment
            target, _, _ = raw_target.partition("#")
            target = target.strip()

            # Classify
            if raw_target.startswith(("http://", "https://", "mailto:")):
                results.append(
                    {
                        "source": str(md_file.relative_to(docs_root)),
                        "target": raw_target,
                        "status": "external",
                    }
                )
                continue

            if not target:
                # Anchor-only link
                results.append(
                    {
                        "source": str(md_file.relative_to(docs_root)),
                        "target": raw_target,
                        "status": "anchor",
                    }
                )
                continue

            # Resolve relative to the source file's directory
            resolved = (md_file.parent / target).resolve()
            if resolved.exists():
                status = "ok"
            else:
                # Try with .md extension
                resolved_md = (
                    md_file.parent / (target if target.endswith(".md") else target + ".md")
                ).resolve()
                status = "ok" if resolved_md.exists() else "broken"

            results.append(
                {"source": str(md_file.relative_to(docs_root)), "target": target, "status": status}
            )

    return results


# ── Internal helpers ──────────────────────────────────────────────────────────


def _collect_types_for_phase(phase: int, docs_root: Path) -> dict[str, int]:
    """Return a dict of ``{doc_type: count}`` for docs that include *phase*."""
    type_counts: dict[str, int] = {}
    phase_re = re.compile(r"phase[s]?\s*[:\-]?\s*\[?([^\]\n]+)\]?", re.IGNORECASE)
    type_re = re.compile(r"^type\s*:\s*['\"]?(\w+)['\"]?", re.MULTILINE)

    for md_file in docs_root.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        if not text.startswith("---"):
            continue

        end = text.find("\n---", 3)
        if end == -1:
            continue
        frontmatter = text[:end]

        # Check if this doc's phase list includes our target phase
        phase_match = phase_re.search(frontmatter)
        if not phase_match:
            continue

        phase_raw = phase_match.group(1)
        if not _phase_in_raw(phase, phase_raw):
            continue

        # Extract type
        type_match = type_re.search(frontmatter)
        if not type_match:
            continue

        doc_type = type_match.group(1).lower()
        canonical = _TYPE_ALIASES.get(doc_type, doc_type)
        type_counts[canonical] = type_counts.get(canonical, 0) + 1

    return type_counts


def _phase_in_raw(phase: int, raw: str) -> bool:
    """Return True if *phase* number appears in the raw frontmatter phase string."""
    # Handles: "1", "[1, 2]", "[1,2,3]", "1 2 3", etc.
    numbers = re.findall(r"\d+", raw)
    return str(phase) in numbers


# ── CLI ───────────────────────────────────────────────────────────────────────


def _print_phase_results(results: list[dict], verbose: bool) -> int:
    """Print results for one phase. Returns number of non-ok items."""
    issues = 0
    for item in results:
        status = item["status"]
        icon = "✓" if status == "ok" else "✗" if status in ("missing", "error") else "~"
        if status != "ok" or verbose:
            print(f"  [{icon}] {item['check']}: {item['detail']}")
        if status != "ok":
            issues += 1
    return issues


def main() -> int:  # noqa: C901
    parser = argparse.ArgumentParser(
        description="Blueprint lint — artefact-completeness and link-integrity checker.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--phase",
        type=int,
        default=None,
        help="Lint a single phase (1–5). Omit to lint all phases.",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show all checks, not only failures."
    )
    parser.add_argument("--links-only", action="store_true", help="Only run link-integrity checks.")
    parser.add_argument(
        "--docs",
        type=Path,
        default=None,
        help="Path to docs/ directory (default: auto-detect).",
    )
    args = parser.parse_args()

    docs_root = args.docs or (Path(__file__).resolve().parent.parent / "docs")
    if not docs_root.exists():
        print(f"Error: docs directory not found at {docs_root}", file=sys.stderr)
        return 2

    total_issues = 0

    if not args.links_only:
        if args.phase is not None:
            if args.phase not in _VALID_PHASES:
                print(
                    f"Error: --phase must be one of {sorted(_VALID_PHASES)}, got {args.phase}",
                    file=sys.stderr,
                )
                return 2
            phases_to_lint = [args.phase]
        else:
            phases_to_lint = sorted(_VALID_PHASES)

        for phase in phases_to_lint:
            results = lint_phase(phase, docs_root)
            issues = sum(1 for r in results if r["status"] != "ok")
            status_str = "OK" if issues == 0 else f"{issues} issue(s)"
            print(f"\nPhase {phase}: {status_str}")
            total_issues += _print_phase_results(results, args.verbose)

    # Link check
    if args.links_only or (args.phase is None and not args.links_only):
        if not args.links_only:
            print("\nLink integrity check:")
        link_results = check_links(docs_root)
        broken = [r for r in link_results if r["status"] == "broken"]
        print(f"  Checked {len(link_results)} links — {len(broken)} broken")
        if broken and args.verbose:
            for r in broken[:20]:
                print(f"  [✗] {r['source']} → {r['target']}")
        total_issues += len(broken)

    print(f"\n{'All checks passed.' if total_issues == 0 else f'{total_issues} issue(s) found.'}")
    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
