"""MkDocs hook: hernummer koppen voor PDF-publicatie.

Alleen actief wanneer MKDOCS_EXPORTER_PDF=true.
Herschrijft H1/H2/H3 met doorlopende hoofdstuknummering
(bijv. "# 1. Titel" → "# 5. Titel", "## 2. Sub" → "## 5.2 Sub")
op basis van de navigatievolgorde uit mkdocs.yml.

De bronbestanden worden NIET gewijzigd — alleen de markdown die
naar de PDF-renderer gaat wordt aangepast.
"""

import os
import re

# Globale teller: wordt opgehoogd per pagina in nav-volgorde
_chapter_index = {}  # src_path -> chapter number


def _build_page_index(nav):
    """Loop door de volledige nav-boom en ken elk blad een volgnummer toe."""
    index = {}
    counter = [0]  # mutable wrapper voor nested function

    def _walk(items):
        if not items:
            return
        for item in items:
            if isinstance(item, str):
                counter[0] += 1
                index[item] = counter[0]
            elif isinstance(item, dict):
                for _key, val in item.items():
                    if isinstance(val, str):
                        counter[0] += 1
                        index[val] = counter[0]
                    elif isinstance(val, list):
                        _walk(val)

    _walk(nav)
    return index


def on_config(config):
    """Bouw de pagina-index op uit de nav-configuratie."""
    if not os.environ.get("MKDOCS_EXPORTER_PDF"):
        return config

    global _chapter_index
    _chapter_index = _build_page_index(config.get("nav", []))
    return config


def on_page_markdown(markdown, page, config, **kwargs):
    """Herschrijf kopnummers als PDF-export actief is."""
    if not os.environ.get("MKDOCS_EXPORTER_PDF"):
        return markdown
    if not _chapter_index:
        return markdown

    src = page.file.src_path
    chapter = _chapter_index.get(src)
    if chapter is None:
        return markdown

    lines = markdown.split("\n")
    result = []
    h2_counter = 0
    h3_counter = 0

    for line in lines:
        # H1: "# 1. Titel" of "# Titel" → "# {chapter}. Titel"
        m1 = re.match(r"^(# )\d+\.\s+(.*)", line)
        if m1:
            h2_counter = 0
            h3_counter = 0
            result.append(f"# {chapter}. {m1.group(2)}")
            continue

        # H2: "## 3. Titel" of "## Titel" → "## {chapter}.{h2} Titel"
        m2 = re.match(r"^(## )\d+\.\s+(.*)", line)
        if m2:
            h2_counter += 1
            h3_counter = 0
            result.append(f"## {chapter}.{h2_counter} {m2.group(2)}")
            continue

        # H2 zonder bestaand nummer: "## Titel"
        m2b = re.match(r"^(## )(?!\d)(.*)", line)
        if m2b:
            h2_counter += 1
            h3_counter = 0
            result.append(f"## {chapter}.{h2_counter} {m2b.group(2)}")
            continue

        # H3: "### Titel" → "### {chapter}.{h2}.{h3} Titel" (alleen als h2 > 0)
        m3 = re.match(r"^(### )\d+\.\s+(.*)", line)
        if m3 and h2_counter > 0:
            h3_counter += 1
            result.append(f"### {chapter}.{h2_counter}.{h3_counter} {m3.group(2)}")
            continue

        m3b = re.match(r"^(### )(?!\d)(.*)", line)
        if m3b and h2_counter > 0:
            h3_counter += 1
            result.append(f"### {chapter}.{h2_counter}.{h3_counter} {m3b.group(2)}")
            continue

        result.append(line)

    return "\n".join(result)
