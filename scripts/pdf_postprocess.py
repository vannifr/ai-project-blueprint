#!/usr/bin/env python3
"""Post-processing voor de geaggregeerde PDF: inhoudsopgave + bookmarks.

Gebruik:
    python scripts/pdf_postprocess.py [site_dir]

Standaard site_dir = "site". Het script:
  1. Opent de geaggregeerde PDF
  2. Extraheert H1/H2 koppen met paginanummers (via ¶ permalink-marker)
  3. Genereert TOC-pagina's (reportlab) en voegt ze in na de titelpagina
  4. Voegt PDF-bookmarks (outlines) toe voor alle H1/H2 koppen
"""

import os
import re
import io
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color


# ---------------------------------------------------------------------------
# Configuratie
# ---------------------------------------------------------------------------

PDF_RELPATH = "pdf/ai-project-blauwdruk.pdf"

# Kleuren
CLR_TITLE = Color(0x1F / 255, 0x2A / 255, 0x44 / 255)   # #1F2A44
CLR_H1 = Color(0x1F / 255, 0x2A / 255, 0x44 / 255)
CLR_H2 = Color(0x33 / 255, 0x33 / 255, 0x33 / 255)
CLR_DOTS = Color(0xBD / 255, 0xC3 / 255, 0xC7 / 255)

# A4 marges (matchen met pdf.scss: 28mm top/bottom, 20mm left/right)
M_TOP = 28 * mm
M_BOTTOM = 28 * mm
M_LEFT = 20 * mm
M_RIGHT = 20 * mm

# Fonts
FONT_BOLD = "Helvetica-Bold"
FONT_NORMAL = "Helvetica"

# TOC layout (eenheden in punten; 1pt = 1 in reportlab)
H2_INDENT = 15
LINE_H1 = 12 * 1.3    # 15.6pt
LINE_H2 = 11 * 1.3    # 14.3pt
EXTRA_H1 = 4           # extra ruimte boven H1


# ---------------------------------------------------------------------------
# Stap 1: Koppen extraheren uit de PDF
# ---------------------------------------------------------------------------

def extract_headings(pdf_path):
    """Extraheer H1/H2 koppen met paginanummers uit de PDF.

    H1 koppen worden gevonden via twee patronen:
      1. Chapter-start pagina's: eerste regel is "N. Titel" (zonder prefix)
      2. Continuation pagina's: running header "AI Project Blauwdruk N. Titel¶"

    H2 koppen worden geëxtraheerd uit content-regels (patroon: "N.M Titel")
    waarbij N een bekend H1-prefix moet zijn.

    Retourneert lijst van (level, prefix, title, page_1indexed),
    gesorteerd op hoofdstuknummer.
    """
    reader = PdfReader(pdf_path)

    # --- H1: extraheer uit chapter-start pagina's en running headers ---
    h1_map = {}  # prefix (str) -> (title, first_page)

    for page_idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        if not lines:
            continue

        first_line = lines[0]

        # Patroon 1: chapter-start pagina — eerste regel is "N. Titel"
        m1 = re.match(r"^(\d{1,3})\.\s+(.+)$", first_line)
        if m1 and not first_line.startswith("AI Project Blauwdruk"):
            prefix = m1.group(1)
            title = m1.group(2).strip()
            if prefix not in h1_map:
                h1_map[prefix] = (title, page_idx + 1)
            continue

        # Patroon 2: running header — "AI Project Blauwdruk N. Titel" (¶ optioneel,
        # wordt verborgen door CSS in nieuwere builds)
        m2 = re.match(
            r"^AI Project Blauwdruk\s+(\d{1,3})\.\s+(.+?)(?:\s*¶)?\s*$", first_line
        )
        if m2:
            prefix = m2.group(1)
            title = m2.group(2).strip()
            if prefix not in h1_map:
                # Running header pagina: het hoofdstuk begon al eerder,
                # maar zoek de H1-regel in de content voor de juiste pagina.
                # Als we hier komen heeft patroon 1 het al gevonden op een
                # eerdere pagina, dus we voegen alleen toe als het nog
                # ontbreekt.
                h1_map[prefix] = (title, page_idx + 1)
            continue

        # Patroon 3: chapter-start in content (niet eerste regel)
        # Voor het geval de H1 niet de eerste regel is (bijv. chapter 1
        # waar een running header boven de H1 staat)
        for line in lines[1:6]:  # kijk in eerste 6 regels
            if any(skip in line for skip in
                   ["AI Project Blauwdruk", "CC BY-NC-SA", "Vertrouwelijk",
                    "Versie 2026", "\u00b6"]):
                continue
            m3 = re.match(r"^(\d{1,3})\.\s+([A-Z].{2,})$", line)
            if m3:
                prefix = m3.group(1)
                title = m3.group(2).strip()
                if prefix not in h1_map:
                    h1_map[prefix] = (title, page_idx + 1)
                break  # slechts één H1 per pagina

    # --- Speciaal geval: "Release Notes" zonder nummer ---
    # Het heading-numbers hook kent dit chapter 99 toe
    for page_idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        first_line = text.split("\n")[0].strip() if text.strip() else ""
        if first_line == "Release Notes" and "99" not in h1_map:
            h1_map["99"] = ("Release Notes", page_idx + 1)
            break

    # --- H2: extraheer uit content ---
    content_skip = ["AI Project Blauwdruk", "CC BY-NC-SA", "Vertrouwelijk",
                    "Versie 2026", "\u00b6"]

    h2_list = []
    h2_seen = set()
    known_h1_prefixes = set(h1_map.keys())

    for page_idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for line in text.split("\n"):
            s = line.strip()
            if not s or any(f in s for f in content_skip):
                continue
            m = re.match(r"^(\d{1,3})\.(\d{1,3})\s+(.+)$", s)
            if m:
                h1_prefix = m.group(1)
                h2_num = m.group(2)
                full_prefix = f"{h1_prefix}.{h2_num}"
                title = m.group(3).strip()
                if h1_prefix not in known_h1_prefixes:
                    continue
                if not title or not title[0].isupper() or len(title) < 3:
                    continue
                if full_prefix not in h2_seen:
                    h2_seen.add(full_prefix)
                    h2_list.append((2, full_prefix, title, page_idx + 1))

    # --- Combineer en sorteer op chapter-nummer ---
    headings = []
    for prefix, (title, page) in h1_map.items():
        headings.append((1, prefix, title, page))

    headings.extend(h2_list)
    headings.sort(key=lambda h: _num_sort_key(h[1]))

    return headings


def _num_sort_key(prefix):
    """Sorteersleutel voor prefix "N" of "N.M" als tuple van ints."""
    parts = prefix.split(".")
    return tuple(int(p) for p in parts)


# ---------------------------------------------------------------------------
# Stap 2: TOC-pagina's genereren
# ---------------------------------------------------------------------------

def count_toc_pages(headings):
    """Bereken hoeveel pagina's de TOC nodig heeft."""
    _, height = A4
    usable = height - M_TOP - M_BOTTOM - 50  # 50pt ruimte na titel

    y = usable
    pages = 1

    for level, *_ in headings:
        needed = (LINE_H1 + EXTRA_H1) if level == 1 else LINE_H2
        if y - needed < 0:
            pages += 1
            y = height - M_TOP - M_BOTTOM
        y -= needed

    return pages


def generate_toc_pdf(headings, toc_page_count):
    """Genereer TOC-pagina's als PDF bytes.

    Paginanummers worden gecorrigeerd voor de ingevoegde TOC-pagina's.
    """
    width, height = A4
    usable_width = width - M_LEFT - M_RIGHT

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    y = height - M_TOP

    # --- Titel ---
    c.setFont(FONT_BOLD, 22)
    c.setFillColor(CLR_TITLE)
    c.drawString(M_LEFT, y - 22, "Inhoudsopgave")
    y -= 50

    page_num_space = 30
    dot_spacing = 3.5

    for level, prefix, title, orig_page in headings:
        adjusted_page = orig_page + toc_page_count

        if level == 1:
            needed = LINE_H1 + EXTRA_H1
        else:
            needed = LINE_H2

        # Nieuwe pagina indien nodig
        if y - needed < M_BOTTOM:
            c.showPage()
            y = height - M_TOP

        if level == 1:
            y -= EXTRA_H1
            font = FONT_BOLD
            font_size = 12
            color = CLR_H1
            indent = 0
            display = f"{prefix}. {title}"
        else:
            font = FONT_NORMAL
            font_size = 11
            color = CLR_H2
            indent = H2_INDENT
            display = f"{prefix} {title}"

        text_y = y - font_size
        x_start = M_LEFT + indent
        x_end = width - M_RIGHT

        # Tekst
        c.setFont(font, font_size)
        c.setFillColor(color)
        text_w = c.stringWidth(display, font, font_size)

        # Truncate als tekst te lang is
        max_text_w = usable_width - indent - page_num_space - 20
        if text_w > max_text_w:
            while text_w > max_text_w and len(display) > 10:
                display = display[:-1]
                text_w = c.stringWidth(display + "...", font, font_size)
            display += "..."
            text_w = c.stringWidth(display, font, font_size)

        c.drawString(x_start, text_y, display)

        # Paginanummer rechts
        page_str = str(adjusted_page)
        num_w = c.stringWidth(page_str, font, font_size)
        c.drawRightString(x_end, text_y, page_str)

        # Puntjeslijn
        dots_start = x_start + text_w + 4
        dots_end = x_end - num_w - 4
        if dots_end > dots_start + 10:
            c.setFillColor(CLR_DOTS)
            c.setFont(font, font_size)
            dot_x = dots_start
            while dot_x < dots_end:
                c.drawString(dot_x, text_y, ".")
                dot_x += dot_spacing

        if level == 1:
            y -= LINE_H1
        else:
            y -= LINE_H2

    c.save()
    buf.seek(0)
    return buf.read()


# ---------------------------------------------------------------------------
# Stap 3: PDF samenvoegen + bookmarks
# ---------------------------------------------------------------------------

def postprocess(pdf_path):
    """Voeg TOC en bookmarks toe aan de geaggregeerde PDF."""
    print(f"[pdf-postprocess] Openen: {pdf_path}")

    headings = extract_headings(pdf_path)
    if not headings:
        print("[pdf-postprocess] Geen koppen gevonden, overslaan.")
        return

    h1_count = sum(1 for h in headings if h[0] == 1)
    h2_count = sum(1 for h in headings if h[0] == 2)
    print(f"[pdf-postprocess] {len(headings)} koppen ({h1_count} H1, {h2_count} H2)")

    # Bereken TOC-pagina's
    toc_page_count = count_toc_pages(headings)
    print(f"[pdf-postprocess] TOC: {toc_page_count} pagina('s)")

    # Genereer TOC-PDF
    toc_bytes = generate_toc_pdf(headings, toc_page_count)
    toc_reader = PdfReader(io.BytesIO(toc_bytes))
    actual_toc_pages = len(toc_reader.pages)

    # Hergenereer als telling niet klopt
    if actual_toc_pages != toc_page_count:
        print(f"[pdf-postprocess] TOC-hertelling: {actual_toc_pages} pagina's")
        toc_bytes = generate_toc_pdf(headings, actual_toc_pages)
        toc_reader = PdfReader(io.BytesIO(toc_bytes))
        actual_toc_pages = len(toc_reader.pages)

    # Bouw nieuwe PDF
    original = PdfReader(pdf_path)
    writer = PdfWriter()

    # 1. Titelpagina
    writer.add_page(original.pages[0])

    # 2. TOC-pagina's
    for toc_page in toc_reader.pages:
        writer.add_page(toc_page)

    # 3. Rest van originele pagina's
    for i in range(1, len(original.pages)):
        writer.add_page(original.pages[i])

    total_pages = len(writer.pages)
    print(f"[pdf-postprocess] Nieuwe PDF: {total_pages} pagina's "
          f"(was {len(original.pages)}, +{actual_toc_pages} TOC)")

    # 4. Bookmarks toevoegen
    # Bookmark voor de inhoudsopgave
    writer.add_outline_item("Inhoudsopgave", 1)  # 0-indexed: pagina 2

    current_h1 = None
    for level, prefix, title, orig_page in headings:
        new_page_idx = orig_page - 1 + actual_toc_pages  # 0-indexed

        if new_page_idx < 0 or new_page_idx >= total_pages:
            continue

        if level == 1:
            display = f"{prefix}. {title}"
            current_h1 = writer.add_outline_item(display, new_page_idx)
        elif level == 2:
            display = f"{prefix} {title}"
            parent = current_h1 if current_h1 is not None else None
            writer.add_outline_item(display, new_page_idx, parent=parent)

    # 5. Metadata behouden
    if original.metadata:
        writer.add_metadata(original.metadata)

    # 6. Schrijf resultaat
    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"[pdf-postprocess] Klaar: {pdf_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    site_dir = sys.argv[1] if len(sys.argv) > 1 else "site"
    pdf_path = os.path.join(site_dir, PDF_RELPATH)

    if not os.path.exists(pdf_path):
        print(f"[pdf-postprocess] PDF niet gevonden: {pdf_path}")
        sys.exit(1)

    postprocess(pdf_path)
