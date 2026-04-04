#!/usr/bin/env python3
"""Generate question-answer index from frontmatter across all docs/.

Reads summary, answers, and metadata from frontmatter and produces:
  - docs/qa-index.yaml  (structured, for MCP / chatbot retrieval)
  - docs/llms-questions.txt (plain-text, for LLM ingestion)

Usage:
    python scripts/generate_qa_index.py               # NL (default)
    python scripts/generate_qa_index.py --lang en      # EN
    python scripts/generate_qa_index.py --output-dir build/
"""

import argparse
import re
from datetime import date
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"
RE_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RE_H1 = re.compile(r"^#\s+(?:\d+\.\s+)?(.+)$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter using simple regex (no PyYAML dependency)."""
    m = RE_FRONTMATTER.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # Parse list values: [a, b, c] or ["a", "b"]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = []
                # Handle quoted strings with commas inside
                in_quote = False
                current = []
                quote_char = None
                for ch in inner:
                    if ch in ('"', "'") and not in_quote:
                        in_quote = True
                        quote_char = ch
                    elif ch == quote_char and in_quote:
                        in_quote = False
                        quote_char = None
                    elif ch == "," and not in_quote:
                        items.append("".join(current).strip().strip("'\""))
                        current = []
                        continue
                    else:
                        current.append(ch)
                if current:
                    items.append("".join(current).strip().strip("'\""))
                # Try int conversion
                parsed = []
                for item in items:
                    try:
                        parsed.append(int(item))
                    except ValueError:
                        parsed.append(item)
                fm[key] = parsed
        else:
            value = value.strip("'\"")
            try:
                fm[key] = int(value)
            except ValueError:
                fm[key] = value
    return fm


def extract_title(text: str) -> str:
    """Extract first H1 heading."""
    m = RE_FRONTMATTER.match(text)
    body = text[m.end() :] if m else text
    h1 = RE_H1.search(body)
    return h1.group(1).strip() if h1 else ""


def yaml_escape(s: str) -> str:
    """Escape a string for YAML output."""
    if not s:
        return '""'
    if any(
        c in s
        for c in (
            ":",
            "#",
            '"',
            "'",
            "\n",
            "{",
            "}",
            "[",
            "]",
            ",",
            "&",
            "*",
            "?",
            "|",
            "-",
            "<",
            ">",
            "=",
            "!",
            "%",
            "@",
            "`",
        )
    ):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def generate(lang: str, output_dir: Path):
    """Generate qa-index.yaml and llms-questions.txt."""
    pages = []
    total_questions = 0

    for md_path in sorted(DOCS_ROOT.rglob("*.md")):
        rel = md_path.relative_to(DOCS_ROOT).as_posix()

        # Language filtering
        if lang == "en":
            if not rel.endswith(".en.md"):
                continue
        else:
            if rel.endswith(".en.md"):
                continue

        # Skip generated files
        if rel in (
            "llms.txt",
            "llms-full.txt",
            "llms-full-nl.txt",
            "llms-questions.txt",
            "qa-index.yaml",
            "robots.txt",
        ):
            continue

        text = md_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        title = extract_title(text)

        summary = fm.get("summary", "")
        answers = fm.get("answers", [])
        if isinstance(answers, str):
            answers = [answers]
        audience = fm.get("roles", [])
        if isinstance(audience, str):
            audience = [audience]
        phase = fm.get("phase", [])
        if isinstance(phase, int):
            phase = [phase]
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        doc_type = fm.get("type", "")

        total_questions += len(answers)

        pages.append(
            {
                "path": rel,
                "title": title,
                "summary": summary,
                "type": doc_type,
                "audience": audience,
                "phase": phase,
                "tags": tags,
                "answers": answers,
            }
        )

    # ── Generate qa-index.yaml ────────────────────────────────────────────
    yaml_lines = [
        f"# AI Project Blueprint — Question-Answer Index ({lang.upper()})",
        "# Auto-generated from frontmatter. Do not edit manually.",
        f"# Generated: {date.today().isoformat()}",
        f"# Pages: {len(pages)}, Questions: {total_questions}",
        "",
        "pages:",
    ]

    for page in pages:
        yaml_lines.append(f"  - path: {yaml_escape(page['path'])}")
        yaml_lines.append(f"    title: {yaml_escape(page['title'])}")
        if page["summary"]:
            yaml_lines.append(f"    summary: {yaml_escape(page['summary'])}")
        if page["audience"]:
            items = ", ".join(yaml_escape(a) for a in page["audience"])
            yaml_lines.append(f"    audience: [{items}]")
        if page["phase"]:
            items = ", ".join(str(p) for p in page["phase"])
            yaml_lines.append(f"    phase: [{items}]")
        if page["tags"]:
            items = ", ".join(yaml_escape(t) for t in page["tags"])
            yaml_lines.append(f"    tags: [{items}]")
        if page["answers"]:
            yaml_lines.append("    answers:")
            for ans in page["answers"]:
                yaml_lines.append(f"      - {yaml_escape(ans)}")

    yaml_path = output_dir / "qa-index.yaml"
    yaml_path.write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")

    # ── Generate llms-questions.txt ───────────────────────────────────────
    txt_lines = [
        f"# AI Project Blueprint — Question Index ({lang.upper()})",
        f"# Source: https://ai-delivery.io{'/' if lang == 'nl' else '/en/'}",
        f"# Generated: {date.today().isoformat()}",
        f"# Questions: {total_questions}",
        "",
    ]

    for page in pages:
        if not page["answers"]:
            continue
        for ans in page["answers"]:
            txt_lines.append(f"Q: {ans}")
            txt_lines.append(f"→ {page['path']}")
            if page["summary"]:
                txt_lines.append(f"  {page['summary']}")
            txt_lines.append("")

    txt_path = output_dir / "llms-questions.txt"
    txt_path.write_text("\n".join(txt_lines) + "\n", encoding="utf-8")

    # ── Summary ───────────────────────────────────────────────────────────
    with_summary = sum(1 for p in pages if p["summary"])
    with_answers = sum(1 for p in pages if p["answers"])

    print(f"\n{'=' * 60}")
    print(f"  QA Index Generation — {lang.upper()}")
    print(f"{'=' * 60}")
    print(f"  Pages processed:       {len(pages)}")
    print(f"  Pages with summary:    {with_summary}")
    print(f"  Pages with answers:    {with_answers}")
    print(f"  Total questions:       {total_questions}")
    print(f"  Output: {yaml_path}")
    print(f"  Output: {txt_path}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Generate QA index from frontmatter")
    parser.add_argument("--lang", choices=["nl", "en"], default="nl")
    parser.add_argument("--output-dir", type=Path, default=DOCS_ROOT)
    args = parser.parse_args()

    generate(args.lang, args.output_dir)


if __name__ == "__main__":
    main()
