#!/usr/bin/env python3
"""Source currency checker for authoritative external references.

Scans all docs/ files for a `sources:` frontmatter block and:
  1. Validates required fields (id, ref, url, date_verified, next_review).
  2. Flags sources whose next_review date has passed.
  3. With --remote: fetches each source URL and checks EUR-Lex for
     related amending/implementing documents newer than date_verified.

Exit codes:
  0  All sources are current and no reviews are overdue.
  1  One or more issues found (overdue reviews, missing fields, remote changes).

Usage:
    python scripts/check_sources.py
    python scripts/check_sources.py --remote
    python scripts/check_sources.py --remote --github-issue
    python scripts/check_sources.py --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

# ── Constants ─────────────────────────────────────────────────────────────────

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"
TODAY = date.today()

# Source types that must carry a `sources:` block
REQUIRED_SOURCE_TYPES = {"compliance", "playbook"}

# Authoritative source registry — maps id → EUR-Lex CELEX or canonical URL
KNOWN_SOURCES: dict[str, dict] = {
    "eu-ai-act": {
        "celex": "32024R1689",
        "title": "EU AI Act (Verordening (EU) 2024/1689)",
        "eurlex_url": "https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32024R1689",
        "oj_date": "2024-07-12",  # Official Journal publication date (fixed)
    },
    "hleg-ethics": {
        "title": "HLEG Ethics Guidelines for Trustworthy AI",
        "eurlex_url": None,
        "canonical_url": "https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai",
        "oj_date": None,
    },
    "iso-42001": {
        "title": "ISO/IEC 42001:2023 — AI Management Systems",
        "eurlex_url": None,
        "canonical_url": "https://www.iso.org/standard/81230.html",
        "oj_date": None,
    },
    "nist-ai-rmf": {
        "title": "NIST AI Risk Management Framework 1.0",
        "eurlex_url": None,
        "canonical_url": "https://www.nist.gov/artificial-intelligence/ai-risk-management-framework",
        "oj_date": None,
    },
}

REQUIRED_SOURCE_FIELDS = {"id", "ref", "url", "date_verified", "next_review"}


# ── Issue dataclass ───────────────────────────────────────────────────────────

class Issue:
    def __init__(self, doc: str, source_id: str, severity: str, message: str):
        self.doc = doc
        self.source_id = source_id
        self.severity = severity  # "error" | "warning" | "info"
        self.message = message

    def __repr__(self):
        return f"[{self.severity.upper()}] {self.doc} ({self.source_id}): {self.message}"


# ── Frontmatter parser ────────────────────────────────────────────────────────

def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    """Return parsed YAML frontmatter or None if absent/invalid."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None


# ── Local checks ──────────────────────────────────────────────────────────────

def check_doc(path: Path) -> list[Issue]:
    """Run all local checks on a single file."""
    issues: list[Issue] = []
    rel = str(path.relative_to(DOCS_ROOT))

    fm = parse_frontmatter(path)
    if fm is None:
        return issues

    doc_type = fm.get("type", "")
    tags = fm.get("tags", []) or []

    # Only enforce on compliance / playbook docs with regulatory tags
    if doc_type not in REQUIRED_SOURCE_TYPES:
        return issues
    if not any(t in tags for t in ("eu-ai-act", "security", "ethics", "validation")):
        return issues

    sources = fm.get("sources")
    if not sources:
        issues.append(Issue(rel, "-", "error",
                            f"type '{doc_type}' with regulatory tags must have a 'sources:' block"))
        return issues

    if not isinstance(sources, list):
        issues.append(Issue(rel, "-", "error", "'sources' must be a YAML list"))
        return issues

    for src in sources:
        if not isinstance(src, dict):
            issues.append(Issue(rel, "?", "error", "each source entry must be a mapping"))
            continue

        src_id = src.get("id", "?")

        # Required fields
        missing = REQUIRED_SOURCE_FIELDS - set(src.keys())
        if missing:
            issues.append(Issue(rel, src_id, "error",
                                f"missing required fields: {sorted(missing)}"))

        # next_review date check
        next_review_raw = src.get("next_review")
        if next_review_raw:
            try:
                next_review = datetime.strptime(str(next_review_raw), "%Y-%m-%d").date()
            except ValueError:
                issues.append(Issue(rel, src_id, "error",
                                    f"next_review '{next_review_raw}' is not a valid YYYY-MM-DD date"))
                continue

            days_overdue = (TODAY - next_review).days
            if days_overdue > 0:
                issues.append(Issue(rel, src_id, "warning",
                                    f"review overdue by {days_overdue} day(s) "
                                    f"(next_review: {next_review_raw})"))
            elif days_overdue > -30:
                issues.append(Issue(rel, src_id, "info",
                                    f"review due within 30 days (next_review: {next_review_raw})"))

        # date_verified format
        dv_raw = src.get("date_verified")
        if dv_raw:
            try:
                datetime.strptime(str(dv_raw), "%Y-%m-%d")
            except ValueError:
                issues.append(Issue(rel, src_id, "error",
                                    f"date_verified '{dv_raw}' is not a valid YYYY-MM-DD date"))

        # Known source id validation
        if src_id != "?" and src_id not in KNOWN_SOURCES:
            issues.append(Issue(rel, src_id, "warning",
                                f"unknown source id '{src_id}' — add to KNOWN_SOURCES registry "
                                f"in check_sources.py"))

    return issues


def run_local_checks() -> list[Issue]:
    """Scan all NL docs (skip .en.md) and run local source checks."""
    issues: list[Issue] = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        if path.name.endswith(".en.md"):
            continue  # EN files mirror NL — only check NL side
        issues.extend(check_doc(path))
    return issues


# ── Remote checks (EUR-Lex) ───────────────────────────────────────────────────

def _fetch_url(url: str, timeout: int = 15) -> str | None:
    """Fetch URL and return HTML text, or None on error."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AI-Project-Blueprint/1.0 source-checker"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError):
        return None


def check_eurlex_celex(celex: str, date_verified_str: str) -> list[str]:
    """
    Fetch EUR-Lex for CELEX and return list of warning strings if new related
    documents (amendments, corrigenda, implementing acts) are found newer than
    date_verified_str.
    """
    warnings: list[str] = []
    date_verified = datetime.strptime(date_verified_str, "%Y-%m-%d").date()

    # Search EUR-Lex for documents that reference/amend this act
    # The "RELA" search operator finds related documents
    search_url = (
        "https://eur-lex.europa.eu/search.html"
        f"?scope=EURLEX&lang=EN&type=quick&query=RELA+%3D+{celex}"
    )
    html = _fetch_url(search_url)
    if html is None:
        warnings.append(f"Could not reach EUR-Lex to check {celex}")
        return warnings

    # Extract dates from search results (format DD/MM/YYYY in EUR-Lex)
    date_pattern = re.compile(r"(\d{2}/\d{2}/\d{4})")
    found_dates: list[date] = []
    for match in date_pattern.finditer(html):
        try:
            d = datetime.strptime(match.group(1), "%d/%m/%Y").date()
            found_dates.append(d)
        except ValueError:
            pass

    newer = [d for d in found_dates if d > date_verified]
    if newer:
        newest = max(newer)
        warnings.append(
            f"EUR-Lex shows related documents as recent as {newest} "
            f"(your date_verified: {date_verified_str}) — manual review recommended"
        )

    # Also verify the act itself is still accessible
    act_url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}"
    act_html = _fetch_url(act_url)
    if act_html is None:
        warnings.append(f"Act CELEX:{celex} is not accessible on EUR-Lex — verify URL")
    elif "Document not found" in act_html or "No results" in act_html:
        warnings.append(f"EUR-Lex reports CELEX:{celex} as not found — document may have been replaced")

    return warnings


def run_remote_checks(issues: list[Issue]) -> list[Issue]:
    """Augment issues list with remote EUR-Lex findings."""
    remote_issues: list[Issue] = []

    # Collect all unique (celex, date_verified) pairs from all docs
    checked_celex: dict[str, str] = {}  # celex → date_verified

    for path in sorted(DOCS_ROOT.rglob("*.md")):
        if path.name.endswith(".en.md"):
            continue
        fm = parse_frontmatter(path)
        if not fm:
            continue
        sources = fm.get("sources")
        if not isinstance(sources, list):
            continue
        for src in sources:
            if not isinstance(src, dict):
                continue
            src_id = src.get("id", "")
            dv = src.get("date_verified", "")
            if not dv or not src_id or src_id not in KNOWN_SOURCES:
                continue
            known = KNOWN_SOURCES[src_id]
            celex = known.get("celex")
            if not celex:
                continue
            # Use the earliest date_verified for this celex across all docs
            if celex not in checked_celex or dv < checked_celex[celex]:
                checked_celex[celex] = dv

    for celex, date_verified in checked_celex.items():
        print(f"  Checking EUR-Lex CELEX:{celex} (verified: {date_verified}) …", file=sys.stderr)
        warnings = check_eurlex_celex(celex, date_verified)
        for w in warnings:
            remote_issues.append(Issue("EUR-Lex", celex, "warning", w))

    return remote_issues


# ── Output formatters ─────────────────────────────────────────────────────────

def format_report(all_issues: list[Issue]) -> str:
    errors = [i for i in all_issues if i.severity == "error"]
    warnings = [i for i in all_issues if i.severity == "warning"]
    infos = [i for i in all_issues if i.severity == "info"]

    lines = [
        "=" * 64,
        "  Source Currency Report",
        f"  Generated: {TODAY}",
        "=" * 64,
        f"  Errors:    {len(errors)}",
        f"  Warnings:  {len(warnings)}",
        f"  Info:      {len(infos)}",
        "",
    ]

    if errors:
        lines.append("  ERRORS (must fix):")
        for i in errors:
            lines.append(f"    [ERROR]  {i.doc}  [{i.source_id}]")
            lines.append(f"             {i.message}")
        lines.append("")

    if warnings:
        lines.append("  WARNINGS (action required):")
        for i in warnings:
            lines.append(f"    [WARN]   {i.doc}  [{i.source_id}]")
            lines.append(f"             {i.message}")
        lines.append("")

    if infos:
        lines.append("  INFO (upcoming):")
        for i in infos:
            lines.append(f"    [INFO]   {i.doc}  [{i.source_id}]")
            lines.append(f"             {i.message}")
        lines.append("")

    if not errors and not warnings:
        lines.append("  ✓ All sources are current and no reviews are overdue.")
        lines.append("")

    return "\n".join(lines)


def format_github_issue(all_issues: list[Issue], remote: bool) -> str:
    errors = [i for i in all_issues if i.severity == "error"]
    warnings = [i for i in all_issues if i.severity == "warning"]
    infos = [i for i in all_issues if i.severity == "info"]

    lines = [
        "## Source Currency Report",
        "",
        f"**Generated:** {TODAY}  ",
        f"**Remote check:** {'yes' if remote else 'no'}",
        "",
    ]

    if errors:
        lines += ["### Errors — must fix", ""]
        for i in errors:
            lines.append(f"- **`{i.doc}`** `[{i.source_id}]` — {i.message}")
        lines.append("")

    if warnings:
        lines += ["### Warnings — action required", ""]
        for i in warnings:
            lines.append(f"- **`{i.doc}`** `[{i.source_id}]` — {i.message}")
        lines.append("")

    if infos:
        lines += ["### Upcoming reviews", ""]
        for i in infos:
            lines.append(f"- **`{i.doc}`** `[{i.source_id}]` — {i.message}")
        lines.append("")

    lines += [
        "---",
        "",
        "### How to resolve",
        "",
        "1. Review the referenced document against the authoritative source.",
        "2. Update the content in the relevant markdown file.",
        "3. Update `date_verified` to today and set a new `next_review` date.",
        "4. Close this issue once all items are resolved.",
        "",
        "*This issue is auto-generated by `.github/workflows/source-review.yml`.*",
    ]

    return "\n".join(lines)


def format_json(all_issues: list[Issue]) -> str:
    return json.dumps(
        {
            "generated": str(TODAY),
            "total": len(all_issues),
            "errors": len([i for i in all_issues if i.severity == "error"]),
            "warnings": len([i for i in all_issues if i.severity == "warning"]),
            "issues": [
                {
                    "doc": i.doc,
                    "source_id": i.source_id,
                    "severity": i.severity,
                    "message": i.message,
                }
                for i in all_issues
            ],
        },
        indent=2,
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Check source currency for authoritative references in docs."
    )
    parser.add_argument("--remote", action="store_true",
                        help="Fetch EUR-Lex to check for new related documents")
    parser.add_argument("--github-issue", action="store_true",
                        help="Output markdown formatted for a GitHub issue body")
    parser.add_argument("--json", action="store_true",
                        help="Output structured JSON")
    args = parser.parse_args()

    print("Scanning docs for source metadata …", file=sys.stderr)
    all_issues = run_local_checks()

    if args.remote:
        print("Running remote EUR-Lex checks …", file=sys.stderr)
        all_issues.extend(run_remote_checks(all_issues))

    if args.json:
        print(format_json(all_issues))
    elif args.github_issue:
        print(format_github_issue(all_issues, remote=args.remote))
    else:
        print(format_report(all_issues))

    has_problems = any(i.severity in ("error", "warning") for i in all_issues)
    sys.exit(1 if has_problems else 0)


if __name__ == "__main__":
    main()
