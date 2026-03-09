---
versie: '1.3'
---

# Changelog

Alle significante wijzigingen aan de AI Project Blauwdruk worden hier bijgehouden, nieuwste bovenaan.

______________________________________________________________________

## v1.3 — 2026-03-08

### Nieuwe Inhoud

- **Blueprint Navigator** (`🚀 Aan de Slag › Blueprint Navigator`): Interactieve 4-staps wizard die nieuwe gebruikers binnen 5 minuten naar hun startpunt leidt. Invoer: rol (AI PM / Tech Lead / Guardian / CAIO), organisatiecontext en 10-vragen maturity scan. Uitvoer: persoonlijk profiel (Verkenner / Bouwer / Visionair) + aanbevolen startmodule + eerste 3 acties met directe links. 12 unieke routes (4 persona's × 3 profielen). Werkt in light- en dark mode.

- **Verkenner Kit — 30-Dagen Startprogramma** (`🚀 Aan de Slag › Verkenner Kit`): Volledig pakket voor organisaties zonder AI-ervaring:

    - **30-Dagen Dag-tot-Dag Plan**: Checklist per dag, gestructureerd per week (Fundament → Verkenning → Validatie → Beslissing).
    - **Project Charter Light**: Vereenvoudigd 1-pagina projectkader (vs. het volledige 3-pagina charter).
    - **Risk Pre-Scan Quick**: 15-vragen risicoscan met groen/oranje/rood uitkomst.
    - **Validatierapport Minimaal**: 2-pagina validatierapport voor Gate 1 Review.
    - **Scaffold Code**: Werkende Python-startcode voor drie use cases: Document Q&A (RAG), E-mailclassificatie en Contentgeneratie. Inclusief Docker-compose setup en probleemoplossingsgids.

### Navigatie & Structuur

- Startpagina bijgewerkt: Blueprint Navigator en Verkenner Kit zijn nu de eerste twee items in "Snel Starten".
- `mkdocs.yml`: nieuw navigatieblok `Verkenner Kit (30 Dagen)` toegevoegd onder `🚀 Aan de Slag`, inclusief Engelstalige nav-vertalingen.

______________________________________________________________________

## v1.2 — 2026-03-07

### Nieuwe Inhoud

- **Volledige Engelstalige vertaling**: Alle documentatie beschikbaar in het Engels via de taalkeuze rechtsboven. Elke module heeft een `.en.md` tegenhanger.
- **Single-file exports**: Volledige blauwdruk als één Markdown-bestand (`export-nl.md`, `export-en.md`) voor offline gebruik en LLM-ingestie.

### Inhoudelijke Correcties

- Formulering "verwijzing naar menselijk expert" gecorrigeerd in het SDD-patroon (Fase 3).
- 5 stub-vertalingen (EN) afgerond voor prioritaire modules.

### Infrastructuur

- FR/DE taalondersteuning verwijderd (niet in gebruik).
- Trunk-based development: no-commit-to-branch git hook verwijderd.

______________________________________________________________________

## v1.1 — 2026-03-02

### Nieuwe Inhoud

- **Fase 4 (Realisatie)** — Activiteiten en Afleveringen pagina's uitgewerkt.
- **Fase 5 (Levering)** — Activiteiten pagina bijgewerkt met ontbrekende inhoud.

### Infrastructuur

- **Netlify deployment**: Hosting overgestapt van FTP naar Netlify via GitHub Actions.
- **PDF-export**: PDF automatisch gegenereerd bij handmatige CI-trigger.
- **CMS**: Decap CMS-configuratie verbeterd (bestandsnamen als weergavenaam).
- Auto-format Markdown via CI verwijderd (mdformat niet compatibel met CMS-output).

______________________________________________________________________

## v1.0 — 2026-02-01

### Initiële Release — Pre-Live Baseline

Eerste release van de gestandaardiseerde AI Project Blauwdruk. Versie op **1.0** tot de proefperiode en feedbackronde is afgerond.

### Inhoud

- **Strategisch Kader**: Managementsamenvatting, AI-levenscyclus, hybride Agile-AI methodologie, governance model, AI-samenwerkingsmodi (HAS-H niveaus), organisatorische heruitvinding.
- **AI-Native Fundamenten**: Definitie, normatieve criteria, artefact model, validatie model, risicoclassificatie, SDD-patroon, bewijsstandaarden.
- **Levenscyclusfasen**: Alle 5 fases uitgewerkt (Verkenning & Strategie, Validatie, Realisatie, Levering, Beheer & Optimalisatie).
- **Compliance Hub**: EU AI Act, risicobeheer, ethische richtlijnen, validatie-eisen, incident respons.
- **Technische Standaarden**: MLOps, data pipelines, model governance, test frameworks, AI-architectuur.
- **Toolkit**: Alle sjablonen — Project Charter, Business Case, Modelkaart, Risicoanalyse, Gate Reviews, Validatierapport, Traceerbaarheid, Prompt Engineering, Privacy & Data.
- **Transformatie & Groei**: 90-Dagen Roadmap, Organisatieprofielen (Verkenner / Bouwer / Visionair), Drie Tracks, Accelerators.
- **Naslag**: Termenlijst, Blueprint Methodologie, Bronnen & Inspiratie, DORA 2025 externe evidentie.

### Breaking Changes

- Vanaf v1.0: Gate 2 (Investering PoV) en Gate 3 (Productie-klaar) vereisen het **Doelkaart (goal card) Validatierapport**.
- Bewijs moet voldoen aan de bewijsstandaarden (feitelijkheid, relevantie, volledigheid).

### Technische Backlog (openstaand)

| #     | Onderwerp                                               | Status |
| :---- | :------------------------------------------------------ | :----- |
| TB-01 | `site_url` instellen voor canonical URL-tags en sitemap | Open   |
