"""
Export Blueprint documentation to single-file LLM-consumable text files.

Outputs:
  docs/llms-full.txt     — English version (uses .en.md when available)
  docs/llms-full-nl.txt  — Dutch version (always uses .md)
  FULL_PLAYBOOK_EXPORT.md — Legacy export (Dutch, repo root)
"""

import os
import re
import datetime
import datetime as dt
import yaml

REPO_ROOT = os.getcwd()
MKDOCS_YAML = os.path.join(REPO_ROOT, "mkdocs.yml")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

OUTPUTS = {
    "en": os.path.join(DOCS_DIR, "llms-full.txt"),
    "nl": os.path.join(DOCS_DIR, "llms-full-nl.txt"),
}
LEGACY_OUTPUT = os.path.join(REPO_ROOT, "FULL_PLAYBOOK_EXPORT.md")

# Patterns to strip
RE_FRONTMATTER = re.compile(r"^---.*?---\s*\n?", re.DOTALL)
RE_HTML_TAG = re.compile(r"<[^>]+>")
RE_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
RE_BLANK_LINES = re.compile(r"\n{3,}")


class CustomLoader(yaml.SafeLoader):
    pass


def _ignore_tag(loader, node):
    return None


CustomLoader.add_constructor(None, _ignore_tag)


def get_nav_files(nav):
    """Recursively extract all file paths from a MkDocs nav structure."""
    files = []
    if not nav:
        return files
    for item in nav:
        if isinstance(item, str):
            files.append(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    files.append(value)
                elif isinstance(value, list):
                    files.extend(get_nav_files(value))
    return files


def resolve_path(nav_path, lang):
    """Return the absolute file path to use for a nav entry and given language."""
    base = os.path.join(DOCS_DIR, nav_path)
    if lang == "en":
        en_path = re.sub(r"\.md$", ".en.md", base)
        if os.path.exists(en_path):
            return en_path
    return base


def clean_content(raw):
    """Strip frontmatter, HTML tags/comments, and collapse excess blank lines."""
    text = RE_FRONTMATTER.sub("", raw)
    text = RE_HTML_COMMENT.sub("", text)
    text = RE_HTML_TAG.sub("", text)
    text = RE_BLANK_LINES.sub("\n\n", text)
    return text.strip()


def nav_label(nav_item):
    """Extract the label string from a nav dict item key."""
    if isinstance(nav_item, dict):
        return next(iter(nav_item))
    return ""


def export(lang, nav_files, output_path):
    site_name = "AI Project Delivery Blueprint" if lang == "en" else "AI Project Blauwdruk"
    url = "https://ai-delivery.io/en/" if lang == "en" else "https://ai-delivery.io/"

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(f"# {site_name} — Full Export\n")
        out.write(f"Source: {url}\n")
        out.write(f"Generated: {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
        out.write(f"Language: {lang}\n")
        out.write(
            "License: CC BY-NC-SA 4.0 — https://creativecommons.org/licenses/by-nc-sa/4.0/\n"
        )
        out.write("\n" + "=" * 72 + "\n\n")

        written = 0
        for nav_path in nav_files:
            abs_path = resolve_path(nav_path, lang)
            if not os.path.exists(abs_path):
                print(f"  SKIP (not found): {nav_path}")
                continue

            with open(abs_path, "r", encoding="utf-8") as f:
                raw = f.read()

            content = clean_content(raw)
            if not content:
                continue

            # Derive a human-readable section header from the file path
            stem = os.path.splitext(os.path.basename(abs_path))[0]
            stem = re.sub(r"\.en$", "", stem)
            label = stem.replace("-", " ").title()

            out.write(f"## {label}\n")
            out.write(f"<!-- source: {nav_path} -->\n\n")
            out.write(content)
            out.write("\n\n" + "-" * 72 + "\n\n")
            written += 1

        print(f"  [{lang.upper()}] {written} pages → {output_path}")


def export_legacy(nav_files):
    """Write FULL_PLAYBOOK_EXPORT.md (NL, repo root) for backward compatibility."""
    with open(LEGACY_OUTPUT, "w", encoding="utf-8") as out:
        out.write(
            f"# AI Project Playbook - Full Export\n\nGenerated on: {dt.datetime.now()}\n\n---\n"
        )
        for nav_path in nav_files:
            abs_path = os.path.join(DOCS_DIR, nav_path)
            if not os.path.exists(abs_path):
                continue
            with open(abs_path, "r", encoding="utf-8") as f:
                raw = f.read()
            content = RE_FRONTMATTER.sub("", raw)
            stem = os.path.splitext(os.path.basename(abs_path))[0].replace("-", " ").title()
            out.write(f"\n# Document: {stem}\nSource: {nav_path}\n---")
            out.write(content)
            out.write("\n\n---\n")
    print(f"  [LEGACY] → {LEGACY_OUTPUT}")


def main():
    with open(MKDOCS_YAML, "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=CustomLoader)

    nav_files = get_nav_files(config.get("nav", []))
    # Deduplicate while preserving order
    seen = set()
    unique_nav = []
    for p in nav_files:
        if p not in seen:
            seen.add(p)
            unique_nav.append(p)

    print(f"Found {len(unique_nav)} unique nav pages.")

    for lang, output_path in OUTPUTS.items():
        export(lang, unique_nav, output_path)

    export_legacy(unique_nav)
    print("Done.")


if __name__ == "__main__":
    main()
