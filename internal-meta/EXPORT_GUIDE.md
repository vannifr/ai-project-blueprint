# Handleiding voor Exporteren van Documentatie

Dit document beschrijft de methoden om de Markdown (.md) bestanden van het AI Project Playbook te exporteren naar andere formaten zoals HTML, PDF en Word (DOCX).

## Optie 1: HTML Website (Aanbevolen voor Teams)
Voor levende documentatie die makkelijk doorzoekbaar is, raden we aan om een statische website te genereren met **MkDocs**.

### Benodigdheden
*   Python geïnstalleerd
*   `pip` package manager

### Installatie
1.  Installeer MkDocs en het Material theme:
    ```bash
    pip install mkdocs mkdocs-material
    ```

### Configuratie
1.  Maak een bestand genaamd `mkdocs.yml` in de hoofdmap met de volgende inhoud:
    ```yaml
    site_name: AI Project Playbook
    theme:
      name: material
      features:
        - navigation.tabs
        - search.suggest
        - toc.integrate
    nav:
      - Home: index.md
      - Strategisch Kader: docs/00-strategisch-kader/
      - ... (voeg overige mappen toe)
    markdown_extensions:
      - admonition
      - pymdownx.details
      - pymdownx.superfences
      - pymdownx.tabbed
    ```

### Genereren
*   **Lokaal bekijken:** `mkdocs serve` (opent op http://127.0.0.1:8000)
*   **Bouwen voor publicatie:** `mkdocs build` (genereert een `site/` map met HTML bestanden)

---

## Optie 2: PDF en DOCX (Voor Rapportage)
Voor het delen van specifieke documenten of het genereren van formele rapporten gebruiken we **Pandoc**.

### Benodigdheden
*   [Pandoc](https://pandoc.org/installing.html)
*   Voor PDF: Een PDF engine zoals `wkhtmltopdf` of een LaTeX distributie (bijv. MiKTeX).

### Commando's

#### Naar Word (DOCX)
```bash
pandoc "docs/00-strategisch-kader/01-ai-levenscyclus.md" -o "AI_Levenscyclus.docx"
```
*Tip: Je kunt een 'reference doc' toevoegen voor huisstijl-opmaak:*
```bash
pandoc input.md -o output.docx --reference-doc=template.docx
```

#### Naar PDF
```bash
pandoc "docs/00-strategisch-kader/01-ai-levenscyclus.md" -o "AI_Levenscyclus.pdf" --pdf-engine=wkhtmltopdf
```

#### Meerdere bestanden samenvoegen
Je kunt een heel hoofdstuk naar één PDF exporteren:
```bash
pandoc docs/00-strategisch-kader/*.md -o Strategisch_Kader_Compleet.pdf --pdf-engine=wkhtmltopdf
```

---

## Optie 3: VS Code Extensies (Snel & Simpel)
Als je snel één bestand wilt exporteren zonder command line tools.

### Aanbevolen Extensie
*   **Markdown PDF** (yzane)

### Gebruik
1.  Open een `.md` bestand in VS Code.
2.  Rechtermuisklik in de editor.
3.  Kies `Markdown PDF: Export (pdf)`, `Export (html)` of `Export (docx)`.

---

© 2026 AI Project Playbook. Door **Frederik Vannieuwenhuyse** & **Hadrien-Joseph van Durme**. Gelicenseerd onder CC BY-NC-SA 4.0.



