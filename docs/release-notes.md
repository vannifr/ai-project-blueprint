---
versie: '1.8'
type: meta
layer: 3
---

# Versiegeschiedenis

Samenvatting van de belangrijkste wijzigingen per versie.

______________________________________________________________________

## v1.8 — 2026-03-19

Grote inhoudelijke en terminologische revisie over 222 bestanden (NL + EN).

### Terminologie

- "Rode Lijnen" → **Harde Grenzen** (EN: Hard Boundaries)
- "normatief" → **toetsbaar**, "richtsnoer" → **leidraad**
- "Data Pijplijnen" → **Data Pipelines**, "Afleveringen" → **Opleveringen**
- "Context Engineering" → **Context Management**, "Model Gezondheid" → **Model Health**
- SDD-afkortingen verwijderd uit titels
- Dubbele termen gededupliceerd (Fairness Audit, Waarderealisatie, Guardian)

### Inhoud

- **Toetsingscriteria** herschreven met 5 AI-native principes: gedragssturing, proportionele governance, bewijs boven aannames, mens in de regie, continue validatie
- **Homepage & Management Samenvatting** verduidelijkt met "Wat is dit?" blok en vraag-antwoord navigatietabel
- **Governance flowcharts** verbeterd met beschrijvende gate-labels
- **Retrospectives** uitgebreid met oorzaakanalyse en veranderexperimenten
- **Hybride Methodologie** uitgebreid: sprint planning in AI-projecten, omgaan met AI-onzekerheid
- **Validatie Diepgang** uitgebreid met 3 niveaus en praktijkvoorbeelden
- **RACI Matrix** aangevuld met Context Builder en AI Security Officer
- ~124 pagina's voorzien van **Doel/Purpose** sectie
- **p95-uitleg** toegevoegd op 18 bestanden

### Structuur & Technisch

- Navigatievolgorde geoptimaliseerd (Project Initiatie vóór Hybride Methodologie)
- Scaffold code volledig verwijderd (bestanden + referenties)
- Compliance Hub en Rollen-index ingekort (dubbele content verwijderd)
- Drie Tracks en Accelerators voorzien van scope-verduidelijking (organisatie vs. project)
- Type A/B callout en AI PM Onboarding entry point toegevoegd
- Navigator links gefixt (broken anchors, trailing slashes)
- Feedback buttons server-side per taal (Jinja2 ipv CSS toggle)
- GitHub Pages-compatibele relatieve URLs
- Disclaimer op homepage
- Build: 0 warnings, 0 INFO-meldingen in strict mode

______________________________________________________________________

## v1.7 — 2026-03-15

Drie uitbreidingen: (1) Agentic AI Engineering — 8 nieuwe modules (NL + EN) voor orkestratiepatronen, MCP/A2A-protocollen, agent-faalpatronen, observeerbaarheid en kostenbeheersing. Engineering Patterns, Valkuilencatalogus (21 valkuilen) en Experimentele Coördinatiemodellen. (2) Aanname-management geïntegreerd in bestaande artefacten — Doelkaart sectie E met 6 AI-specifieke assumptiecategorieën en Riskantste Aanname Test (RAT) in het Experiment Ticket. Gate Reviews uitgebreid met aanname-validatie per gate. Aanname-drift als nieuw drifttype in Drift Detectie. (3) Cross-links versterkt over 26 bestaande modules, About-pagina en release notes als samenvatting. DORA + AI-specifieke metrics toegevoegd aan Metrics & Dashboards. 30 frontmatter-fouten opgelost. 7 nieuwe termenlijst-items.

______________________________________________________________________

## v1.6 — 2026-03-14

Grootste inhoudelijke uitbreiding: 5 nieuwe sjablonen (Experiment Ticket, Model Health Review, Stakeholder Communicatie, AI PM Onboarding, FAQ), architectuurspecifieke moduskeuze, acceptatiecriteria Modus 4-5 en projecttype-classificatie (Type A/B). Kwaliteitsslag: 68 validatiewaarschuwingen opgelost en terminologie-naleving Stijlgids v2.3 projectbreed doorgevoerd.

## v1.5 — 2026-03-13

Migratie naar [ai-delivery.io](https://ai-delivery.io/) als productie-URL. Engels als primaire taal voor internationale bezoekers. SEO-optimalisatie met Schema.org JSON-LD en per-pagina meta descriptions. Stijlgids v2.3 met terminologiedomeinen Agentische AI en AI-Projectmanagement. Nieuwe bestanden: Information Architecture en AI Copywriter Constitution.

## v1.4 — 2026-03-09

Stijlgids v2.2 met bijgewerkte terminologietabel en publicatiechecklist. NL: Green AI-sectie in Doelkaart, Decommissioning in Fase 5. EN vertaalpariteit: 9 modules uitgebreid met onder andere OWASP LLM Top 10 2025, AI Productivity Paradox, Green AI en EU AI Act aanvullende wetgeving. 11 nieuwe primaire bronnen (\[so-40\] t/m \[so-50\]).

## v1.3 — 2026-03-08

Blueprint Navigator: interactieve wizard die gebruikers in 5 minuten naar hun startpunt leidt (12 unieke routes). Verkenner Kit: 30-dagen startprogramma met dag-tot-dag plan, lichtgewicht sjablonen en werkende Python-startcode voor 3 use cases.

## v1.2 — 2026-03-07

Volledige Engelstalige vertaling van alle documentatie. Single-file exports (Markdown) voor offline gebruik en LLM-ingestie. Inhoudelijke correcties en infrastructuurvereenvoudiging.

## v1.1 — 2026-03-02

Fase 4 (Realisatie) en Fase 5 (Levering) pagina's uitgewerkt. Hosting overgestapt naar Netlify via GitHub Actions. PDF-export geautomatiseerd.

## v1.0 — 2026-02-01

**Initiële release.** Volledig strategisch kader, AI-native fundamenten, 5 levenscyclusfasen, compliance hub (EU AI Act), technische standaarden, complete sjabloontoolkit, transformatie-roadmap en naslagmateriaal. Gate 2 en Gate 3 vereisen vanaf deze versie het Doelkaart Validatierapport.
