#!/usr/bin/env python3
"""Add summary and answers fields to frontmatter of all docs/ markdown files.

Extracts summary from existing !!! abstract "Doel"/"Purpose" blocks.
Generates answers from H1 title and summary content.

Preserves all existing frontmatter fields. Only adds summary/answers if missing.
Processes NL files and mirrors to EN counterparts.

Usage:
    python scripts/enrich_summary_answers.py              # dry-run
    python scripts/enrich_summary_answers.py --apply       # write changes
"""

import argparse
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"

RE_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RE_H1 = re.compile(r"^#\s+(?:\d+\.\s+)?(.+)$", re.MULTILINE)
RE_DOEL_BLOCK = re.compile(
    r'!!! abstract "Doel"\s*\n((?:\s{4}.+\n?)+)', re.MULTILINE
)
RE_PURPOSE_BLOCK = re.compile(
    r'!!! abstract "Purpose"\s*\n((?:\s{4}.+\n?)+)', re.MULTILINE
)


def parse_frontmatter(content: str) -> tuple[str, str, str]:
    """Return (fm_text, body, raw_fm_block) from markdown content."""
    m = RE_FRONTMATTER.match(content)
    if not m:
        return "", content, ""
    return m.group(1), content[m.end():], m.group(0)


def extract_abstract(body: str, lang: str = "nl") -> str:
    """Extract text from !!! abstract block."""
    pattern = RE_DOEL_BLOCK if lang == "nl" else RE_PURPOSE_BLOCK
    m = pattern.search(body)
    if not m:
        return ""
    lines = m.group(1).strip().splitlines()
    return " ".join(line.strip() for line in lines).strip()


def extract_h1(body: str) -> str:
    """Extract first H1 title (without numbering prefix)."""
    m = RE_H1.search(body)
    return m.group(1).strip() if m else ""


def has_field(fm_text: str, field: str) -> bool:
    """Check if frontmatter already contains a field."""
    return bool(re.search(rf"^{field}:", fm_text, re.MULTILINE))


def truncate_summary(text: str, max_len: int = 200) -> str:
    """Truncate summary to max length at word boundary."""
    if len(text) <= max_len:
        return text
    truncated = text[:max_len].rsplit(" ", 1)[0]
    return truncated.rstrip(".,;:") + "…"


def generate_answers_nl(title: str, summary: str, file_type: str) -> list[str]:
    """Generate 1-3 question-form answers from title and summary."""
    answers = []
    title_lower = title.lower()

    # Type-specific question patterns
    if file_type == "objectives":
        answers.append(f"Wat is het doel van deze fase?")
    elif file_type == "activities":
        answers.append(f"Welke activiteiten voer ik uit in deze fase?")
    elif file_type == "deliverables":
        answers.append(f"Wat lever ik op aan het einde van deze fase?")
    elif file_type == "template":
        answers.append(f"Hoe gebruik ik het {title} sjabloon?")
    elif file_type == "cheatsheet":
        answers.append(f"Wat is de snelle referentie voor {title}?")
    elif file_type == "compliance":
        answers.append(f"Wat zijn de compliance-eisen voor {title}?")
    elif file_type == "playbook":
        answers.append(f"Hoe voer ik {title} uit?")
    elif file_type == "technical":
        answers.append(f"Wat zijn de technische standaarden voor {title}?")
    elif file_type in ("strategic", "foundation"):
        answers.append(f"Wat houdt {title} in?")
    elif file_type == "guide":
        answers.append(f"Hoe werkt {title}?")
    elif file_type == "index":
        answers.append(f"Wat bevat het onderdeel {title}?")
    else:
        answers.append(f"Wat is {title}?")

    # Add summary-derived question if summary is substantial
    if summary and len(summary) > 30:
        # Extract key concept from summary
        if "classificat" in summary.lower() or "risico" in summary.lower():
            answers.append("Hoe classificeer ik het risico van mijn AI-project?")
        elif "validat" in summary.lower() or "bewijs" in summary.lower():
            answers.append("Hoeveel validatie is voldoende?")
        elif "governance" in summary.lower() or "beslis" in summary.lower():
            answers.append("Wie beslist wat in een AI-project?")
        elif "team" in summary.lower() or "rol" in summary.lower():
            answers.append("Welke rollen heb ik nodig?")
        elif "kosten" in summary.lower() or "budget" in summary.lower():
            answers.append("Wat kost dit?")

    return answers[:3]


def generate_answers_en(title: str, summary: str, file_type: str) -> list[str]:
    """Generate 1-3 English question-form answers."""
    answers = []

    if file_type == "objectives":
        answers.append("What is the goal of this phase?")
    elif file_type == "activities":
        answers.append("What activities do I perform in this phase?")
    elif file_type == "deliverables":
        answers.append("What do I deliver at the end of this phase?")
    elif file_type == "template":
        answers.append(f"How do I use the {title} template?")
    elif file_type == "cheatsheet":
        answers.append(f"What is the quick reference for {title}?")
    elif file_type == "compliance":
        answers.append(f"What are the compliance requirements for {title}?")
    elif file_type == "playbook":
        answers.append(f"How do I execute {title}?")
    elif file_type == "technical":
        answers.append(f"What are the technical standards for {title}?")
    elif file_type in ("strategic", "foundation"):
        answers.append(f"What does {title} entail?")
    elif file_type == "guide":
        answers.append(f"How does {title} work?")
    elif file_type == "index":
        answers.append(f"What does the {title} section contain?")
    else:
        answers.append(f"What is {title}?")

    if summary and len(summary) > 30:
        if "classif" in summary.lower() or "risk" in summary.lower():
            answers.append("How do I classify the risk of my AI project?")
        elif "validat" in summary.lower() or "evidence" in summary.lower():
            answers.append("How much validation is sufficient?")
        elif "governance" in summary.lower() or "decis" in summary.lower():
            answers.append("Who decides what in an AI project?")
        elif "team" in summary.lower() or "role" in summary.lower():
            answers.append("What roles do I need?")
        elif "cost" in summary.lower() or "budget" in summary.lower():
            answers.append("What does this cost?")

    return answers[:3]


def format_yaml_list(items: list[str]) -> str:
    """Format a YAML list with proper quoting."""
    if not items:
        return "[]"
    escaped = []
    for item in items:
        item = item.replace('"', '\\"')
        escaped.append(f'"{item}"')
    return "[" + ", ".join(escaped) + "]"


def add_fields_to_frontmatter(fm_text: str, summary: str, answers: list[str]) -> str:
    """Add summary and answers fields to frontmatter text."""
    lines = fm_text.strip().splitlines()
    new_lines = []

    for line in lines:
        new_lines.append(line)

    # Add summary after description (or at end if no description)
    if summary and not has_field(fm_text, "summary"):
        # Escape quotes in summary
        escaped = summary.replace("'", "\\'")
        new_lines.append(f"summary: '{escaped}'")

    if answers and not has_field(fm_text, "answers"):
        new_lines.append(f"answers: {format_yaml_list(answers)}")

    return "---\n" + "\n".join(new_lines) + "\n---"


def process_file(nl_path: Path, dry_run: bool = True) -> dict:
    """Process a single NL file and its EN counterpart."""
    rel = str(nl_path.relative_to(DOCS_ROOT))
    content = nl_path.read_text(encoding="utf-8")
    fm_text, body, raw_block = parse_frontmatter(content)

    if not fm_text:
        return {"file": rel, "changed": False, "reason": "no frontmatter"}

    # Skip if already has both fields
    if has_field(fm_text, "summary") and has_field(fm_text, "answers"):
        return {"file": rel, "changed": False, "reason": "already has fields"}

    # Extract data
    h1 = extract_h1(body)
    abstract = extract_abstract(body, "nl")
    summary = truncate_summary(abstract) if abstract else ""

    # Get type from frontmatter
    file_type = ""
    for line in fm_text.splitlines():
        if line.strip().startswith("type:"):
            file_type = line.split(":", 1)[1].strip()
            break

    answers = generate_answers_nl(h1, summary, file_type) if h1 else []

    if not summary and not answers:
        return {"file": rel, "changed": False, "reason": "no abstract/title found"}

    # Build new frontmatter
    new_fm = add_fields_to_frontmatter(fm_text, summary, answers)
    new_content = new_fm + body

    changed = content.strip() != new_content.strip()

    if not dry_run and changed:
        nl_path.write_text(new_content, encoding="utf-8")

        # Process EN counterpart
        en_path = nl_path.with_name(nl_path.name.replace(".md", ".en.md"))
        if en_path.exists():
            en_content = en_path.read_text(encoding="utf-8")
            en_fm_text, en_body, _ = parse_frontmatter(en_content)
            if en_fm_text:
                en_h1 = extract_h1(en_body)
                en_abstract = extract_abstract(en_body, "en")
                en_summary = truncate_summary(en_abstract) if en_abstract else ""
                en_answers = generate_answers_en(en_h1, en_summary, file_type) if en_h1 else []
                en_new_fm = add_fields_to_frontmatter(en_fm_text, en_summary, en_answers)
                en_new_content = en_new_fm + en_body
                if en_content.strip() != en_new_content.strip():
                    en_path.write_text(en_new_content, encoding="utf-8")

    return {"file": rel, "changed": changed, "summary": summary[:60], "answers": len(answers)}


def main():
    parser = argparse.ArgumentParser(description="Add summary + answers to frontmatter")
    parser.add_argument("--apply", action="store_true", help="Write changes")
    args = parser.parse_args()

    dry_run = not args.apply
    results = []

    for filepath in sorted(DOCS_ROOT.rglob("*.md")):
        if filepath.name.endswith(".en.md"):
            continue
        result = process_file(filepath, dry_run=dry_run)
        if result:
            results.append(result)

    changed = sum(1 for r in results if r.get("changed"))
    skipped = sum(1 for r in results if not r.get("changed"))
    mode = "DRY RUN" if dry_run else "APPLIED"

    print(f"\n{'=' * 60}")
    print(f"  Summary & Answers Enrichment — {mode}")
    print(f"{'=' * 60}")
    print(f"  Total NL files scanned:  {len(results)}")
    print(f"  Files to update:         {changed}")
    print(f"  Already complete/skip:   {skipped}")
    print()

    if changed > 0:
        print("  Files to update:")
        for r in results:
            if r.get("changed"):
                s = r.get("summary", "")[:50]
                a = r.get("answers", 0)
                print(f"    {r['file']:<60} summary={bool(s)}, answers={a}")
        print()

    if dry_run:
        print("  Run with --apply to write changes.")
    print()


if __name__ == "__main__":
    main()
