"""
Export Blueprint documentation to single-file LLM-consumable text files.

Outputs:
  docs/llms-full.txt     — English version (uses .en.md when available)
  docs/llms-full-nl.txt  — Dutch version (always uses .md)
  FULL_PLAYBOOK_EXPORT.md — Legacy export (Dutch, repo root)
"""

import os
import re
import datetime as dt
import unicodedata
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
RE_STYLE_BLOCK = re.compile(r"<style[^>]*>.*?</style>", re.DOTALL | re.IGNORECASE)
RE_SCRIPT_BLOCK = re.compile(r"<script[^>]*>.*?</script>", re.DOTALL | re.IGNORECASE)
RE_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
RE_HTML_TAG = re.compile(r"<[^>]+>")
RE_BLANK_LINES = re.compile(r"\n{3,}")

# Typographic → ASCII substitution table (for AI-safe plain text)
TYPOGRAPHIC_REPLACEMENTS = [
    ("\u2014", " -- "),   # em dash         —
    ("\u2013", " - "),    # en dash         –
    ("\u2012", " - "),    # figure dash     ‒
    ("\u2011", "-"),      # non-breaking hyphen
    ("\u2010", "-"),      # hyphen          ‐
    ("\u2018", "'"),      # left single quote  '
    ("\u2019", "'"),      # right single quote '
    ("\u201a", "'"),      # single low-9 quote ‚
    ("\u201c", '"'),      # left double quote  "
    ("\u201d", '"'),      # right double quote "
    ("\u201e", '"'),      # double low-9 quote „
    ("\u2026", "..."),    # ellipsis        …
    ("\u00b7", "*"),      # middle dot      ·
    ("\u2022", "*"),      # bullet          •
    ("\u2023", "*"),      # triangular bullet▸
    ("\u2043", "-"),      # hyphen bullet   ⁃
    ("\u2192", "->"),     # right arrow     →
    ("\u2190", "<-"),     # left arrow      ←
    ("\u2191", "^"),      # up arrow        ↑
    ("\u2193", "v"),      # down arrow      ↓
    ("\u2194", "<->"),    # left-right arrow↔
    ("\u00d7", "x"),      # multiplication  ×
    ("\u2248", "~="),     # approximately   ≈
    ("\u2265", ">="),     # greater-or-equal≥
    ("\u2264", "<="),     # less-or-equal   ≤
    ("\u2260", "!="),     # not equal       ≠
    ("\u00a0", " "),      # non-breaking space
    ("\u2009", " "),      # thin space
    ("\u200b", ""),       # zero-width space
    ("\u00ac", "not "),   # logical not     ¬
    ("\u2713", "v"),      # check mark      ✓
    ("\u2717", "x"),      # ballot x        ✗
    ("\u2610", "[ ]"),    # ballot box      ☐
    ("\u2611", "[x]"),    # ballot box checked☑
    ("\u2612", "[x]"),    # ballot box with x☒
    ("\u2714", "v"),      # heavy check     ✔
    ("\u2718", "x"),      # heavy ballot x  ✘
    ("\u2620", "(!)"),    # skull           ☠
    ("\u26a0", "(!)"),    # warning sign    ⚠
    ("\u2139", "(i)"),    # information     ℹ
    ("\u00ae", "(R)"),    # registered      ®
    ("\u00a9", "(C)"),    # copyright       ©
    ("\u2122", "(TM)"),   # trade mark      ™
    ("\u20ac", "EUR"),    # euro sign       €
    ("\u00bc", "1/4"),    # fraction 1/4    ¼
    ("\u00bd", "1/2"),    # fraction 1/2    ½
    ("\u00be", "3/4"),    # fraction 3/4    ¾
    # Box-drawing characters → ASCII
    ("\u2500", "-"),  ("\u2501", "-"),  ("\u2502", "|"),  ("\u2503", "|"),
    ("\u250c", "+"),  ("\u2510", "+"),  ("\u2514", "+"),  ("\u2518", "+"),
    ("\u251c", "+"),  ("\u2524", "+"),  ("\u252c", "+"),  ("\u2534", "+"),
    ("\u253c", "+"),  ("\u2550", "="),  ("\u2551", "|"),  ("\u2554", "+"),
    ("\u2557", "+"),  ("\u255a", "+"),  ("\u255d", "+"),  ("\u256c", "+"),
]
# Emoji and other non-BMP symbols (codepoints > U+FFFF are almost exclusively emoji/symbols)
RE_EMOJI = re.compile(
    "[\U0001F000-\U0001FFFF"   # Misc symbols, emoji, transport, etc.
    "\U00002702-\U000027B0"    # Dingbats
    "\U0000FE00-\U0000FE0F"    # Variation selectors (emoji modifiers)
    "\U0001F1E0-\U0001F1FF"    # Regional indicator symbols (flags)
    "]+",
    flags=re.UNICODE,
)


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
    """Strip frontmatter, HTML blocks/tags, emoji; normalise Unicode to ASCII-safe text."""
    text = RE_FRONTMATTER.sub("", raw)
    text = RE_STYLE_BLOCK.sub("", text)
    text = RE_SCRIPT_BLOCK.sub("", text)
    text = RE_HTML_COMMENT.sub("", text)
    text = RE_HTML_TAG.sub("", text)
    text = RE_EMOJI.sub("", text)
    # NFC normalise (canonical composition) so accents stay as single code points
    text = unicodedata.normalize("NFC", text)
    # Replace typographic punctuation and symbols with ASCII equivalents
    for src, dst in TYPOGRAPHIC_REPLACEMENTS:
        text = text.replace(src, dst)
    # Strip trailing whitespace on every line (left after HTML removal)
    text = "\n".join(line.rstrip() for line in text.splitlines())
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

    parts = [
        f"# {site_name} — Full Export",
        f"Source: {url}",
        f"Generated: {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Language: {lang}",
        "License: CC BY-NC-SA 4.0 — https://creativecommons.org/licenses/by-nc-sa/4.0/",
        "",
        "=" * 72,
        "",
    ]

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

        stem = os.path.splitext(os.path.basename(abs_path))[0]
        stem = re.sub(r"\.en$", "", stem)
        label = stem.replace("-", " ").title()

        parts.append(f"## {label}")
        parts.append(f"<!-- source: {nav_path} -->")
        parts.append("")
        parts.append(content)
        parts.append("")
        parts.append("-" * 72)
        parts.append("")
        written += 1

    # Join and ensure exactly one trailing newline
    output = "\n".join(parts).rstrip("\n") + "\n"
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(output)

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
