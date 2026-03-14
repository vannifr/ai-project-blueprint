# AI Project Blauwdruk

![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-green)
![Version](https://img.shields.io/badge/version-1.5-blue)
![Build Status](https://github.com/vannifr/ai-project-blueprint/actions/workflows/deploy-ftp.yml/badge.svg)
![Languages](https://img.shields.io/badge/languages-NL%20%7C%20EN-informational)

De centrale documentatiehub voor AI-projectmanagement, gebaseerd op PMI-CPMAI standaarden, EU AI Act compliance en Agile-AI frameworks.

**Live site:** [https://ai-delivery.io/](https://ai-delivery.io/)

## Over dit project

Deze blauwdruk biedt een gestandaardiseerde, modulaire aanpak om AI-projecten te beheren van ideatie tot monitoring. Het is ontworpen om teams te helpen navigeren door de complexiteit van AI-native ontwikkeling, compliance en organisatie-adoptie.

### Kernmodules

| Module                       | Beschrijving                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------ |
| **Strategisch Kader**        | AI-levenscyclus, hybride methodologie, governance en Samenwerkingsmodi (5 niveaus)         |
| **AI-Native Fundamenten**    | Doelkaarten, bewijsstandaarden, risicoclassificatie en specificatie-gedreven validatie     |
| **Operationele Fasen (1-5)** | Van Verkenning tot Monitoring — met Gate Reviews, RACI-matrices en CTA-blokken             |
| **Compliance Hub**           | EU AI Act, risicobeheer, ethische richtlijnen, incidentrespons en red teaming              |
| **Toolkit & Sjablonen**      | 50+ invulbare templates, cheatsheets, Gate Review checklists en RAG Design Canvas          |
| **90-Dagen Roadmap**         | Uitvoerbaar startplan in 3 fasen (Focus → Pilot → Schaal) met risico-aangepaste tijdlijnen |
| **Organisatieprofielen**     | Drie volwassenheidsniveaus (Verkenner, Bouwer, Visionair) met groeigids                    |
| **Drie Tracks**              | Strategische heruitvinding, operationeel herontwerp en AI-first bedrijfsmodel              |
| **Explorer Kit**             | 30-dagenplan voor organisaties die starten met AI                                          |

### Architectuur

De documentatie is opgebouwd uit drie lagen:

- **Laag 1 — Strategisch:** Waarom en wat (executive-niveau, overtuigend)
- **Laag 2 — Operationeel:** Hoe, wanneer, wie (instructief, stap-voor-stap)
- **Laag 3 — Toolkit:** Invulbare templates en referentiemateriaal (functioneel, scanbaar)

## Aan de slag

### Online

Bezoek [ai-delivery.io](https://ai-delivery.io/) en gebruik de **Blueprint Navigator** om een gepersonaliseerd pad door de documentatie te vinden.

### Lokaal draaien

```bash
pip install -r requirements.txt
mkdocs serve
```

Open [http://localhost:8000](http://localhost:8000).

### LLM-toegang

De volledige documentatie is beschikbaar als platte tekst voor AI-assistenten:

- [llms.txt](https://ai-delivery.io/llms.txt) — Inhoudsopgave
- [llms-full.txt](https://ai-delivery.io/llms-full.txt) — Volledige inhoud (EN)
- [llms-full-nl.txt](https://ai-delivery.io/llms-full-nl.txt) — Volledige inhoud (NL)

## Taalondersteuning

De site wordt gebouwd in twee talen via de **bestandssuffix-strategie** (`mkdocs-static-i18n`):

| Taal                   | Suffix   | URL    | Status                |
| ---------------------- | -------- | ------ | --------------------- |
| Nederlands (standaard) | *(geen)* | `/`    | Volledig              |
| English                | `.en.md` | `/en/` | Kernpagina's vertaald |

Ontbrekende vertalingen vallen automatisch terug op de Nederlandse versie.

### Build per taal

```bash
# HTML-site (alle talen tegelijk)
mkdocs build --strict

# PDF per taal
MKDOCS_LANG=nl MKDOCS_EXPORTER_PDF=true MKDOCS_PDF_OUTPUT=pdf/ai-project-blauwdruk.nl.pdf mkdocs build --no-directory-urls
MKDOCS_LANG=en MKDOCS_EXPORTER_PDF=true MKDOCS_PDF_OUTPUT=pdf/ai-project-blauwdruk.en.pdf mkdocs build --no-directory-urls
```

## Ontwikkelworkflow

### Pre-commit hooks

```bash
pip install pre-commit
pre-commit install
```

Dit activeert automatische kwaliteitscontroles bij elke commit:

- Markdown formatting (mdformat)
- Trailing whitespace verwijderen
- YAML syntax validatie
- Documentatie kwaliteitsvalidatie (terminologie, CTA-blokken, frontmatter, Samenwerkingsmodi in gates)

### Handmatige kwaliteitscontrole

```bash
python3 scripts/validate_docs.py
```

Het validatiescript (v2.3) controleert op:

- Terminologie-naleving conform de Stijlgids
- Aanwezigheid van CTA-blokken in Laag 2-modules
- Samenwerkingsmodus-veld in Gate Review checklists
- Levenscyclus-redundantie (Single Source of Truth)
- Frontmatter met verplicht `versie`-veld
- Vertalingsdekking (NL → EN)
- Heading-hiërarchie en debug-markers

## Bijdragen

Dit project wordt beheerd volgens de Stijlgids v2.3 (`internal-meta/STYLE_GUIDE.md`). Zie `internal-meta/BACKLOG.md` voor de huidige roadmap.

**Voor het indienen van een PR:**

1. Voer `pre-commit run --all-files` uit
1. Controleer dat `mkdocs build --strict` slaagt
1. Verifieer dat `python3 scripts/validate_docs.py` geen errors geeft

## Licentie

© 2026 AI Project Blauwdruk.
Gelicenseerd onder de **Creative Commons Naamsvermelding-NietCommercieel-GelijkDelen 4.0 Internationaal (CC BY-NC-SA 4.0)**.
