---
versie: '1.6'
---

# Changelog

Alle significante wijzigingen aan de AI Project Blauwdruk worden hier bijgehouden, nieuwste bovenaan.

______________________________________________________________________

## v1.6 — 2026-03-14

### Nieuwe Modules

- **Experiment Ticket** (`09-sjablonen/17-experiment-ticket/`): Time-boxed spike-sjabloon met hypothese, succes/faalcriteria en formeel beslispunt (Doorgaan / Pivoteren / Stoppen).
- **Modelgezondheid Review** (`09-sjablonen/18-modelgezondheid/`): Maandelijkse 1-uur review-agenda met statusniveaus afgestemd op Drift Detectie en communicatiescripts.
- **Stakeholder Communicatie Playbook** (`08-rollen/03-stakeholder-communicatie`): Communicatiecadans per rol, "Misschien-probleem"-framing, escalatieprocedure en trust-building technieken.
- **AI PM Onboarding Playbook** (`08-rollen/04-ai-pm-onboarding`): Week-voor-week opbouwplan met dagindeling en deliverable-checklist.
- **FAQ** (`00-navigator/faq`): Veelgestelde vragen — metrics per fase en story points bij AI-projecten.

### Inhoudelijke Uitbreidingen

- **Moduskeuze Beoordeling**: Architectuurspecifieke overwegingen toegevoegd (RAG, Fine-tuning, Agentisch) met sleutelvragen per architectuurtype.
- **AI-Samenwerkingsmodi**: Acceptatiecriteria voor Modus 4–5 toegevoegd (functioneel, veiligheid, audit, scope, governance).
- **Verkenning Activiteiten**: Projecttype Classificatie (Type A: bouwen *met* AI vs. Type B: AI *in* het product) met beslisheuristiek.
- **Levering Doelstellingen**: Ontbrekende tekst bij "Human-in-the-Loop Cultuur" aangevuld.
- **Normatieve Criteria EN**: Lege EN-pagina gevuld met vertaling van de kwalificatietabel.

### Kwaliteitsverbetering

- 68 validatiewaarschuwingen opgelost: CTA-blokken toegevoegd aan 36 bestanden, terminologie-overtredingen gecorrigeerd in 41 NL-bestanden, stale "in ontwikkeling"-banners vervangen door inhoud.
- Terminologie-naleving projectbreed doorgevoerd conform Stijlgids v2.3 — alle verouderde Engelstalige termen vervangen door de voorgeschreven Nederlandse equivalenten.
- Module 10 (Doorlopende Verbetering), Module 11 (Project Afsluiting) en Module 15 (Accelerators) uitgebreid van stubs naar volledige index-pagina's.

### Bronnen

- Monte Carlo — ML Observability (2024) en Writer — AI Governance & Communication (2025) toegevoegd aan bronnenlijst.

### README

- Bijgewerkt naar huidige staat: badges gecorrigeerd, moduletabel, 3-lagenarchitectuur, LLM-toegang (llms.txt) en validatiescript v2.3.

______________________________________________________________________

## v1.5 — 2026-03-13

### Migratie naar ai-delivery.io & SEO

- **Nieuwe productie-URL**: Site verhuisd naar <https://ai-delivery.io/>. Alle interne URL-referenties bijgewerkt (`site_url`, `url_nl`, `url_en`, `og_image`, sitemap).
- **Engels als primaire taal**: Bezoekers met een niet-Nederlandstalige browser worden automatisch doorgestuurd naar `/en/`. `x-default` hreflang wijst nu naar de Engelstalige versie.
- **robots.txt**: Sitemap-URL bijgewerkt naar `https://ai-delivery.io/sitemap.xml`.
- **Schema.org JSON-LD**: Elke pagina bevat nu gestructureerde data (`Organization`, `WebSite`, `Article`, `BreadcrumbList`) voor rich snippets in zoekmachines.
- **Per-pagina meta descriptions**: Unieke beschrijvingen toegevoegd aan de 20 belangrijkste pagina's in zowel NL als EN.
- **site_name / copyright**: Primaire site-identiteit bijgewerkt naar "AI Project Blueprint" (EN); het NL-taalblok behoudt "AI Project Blauwdruk".

### Stijlgids & Terminologie

- **STYLE_GUIDE v2.3** (NL + EN): Terminologietabellen uitgebreid met twee nieuwe kennisdomeinen: Agentische AI (14 termen) en AI-Projectmanagement als discipline (11 termen). Plaatsingsregels voor nieuwe content toegevoegd met verwijzingen naar INFORMATION_ARCHITECTURE en AI_COPYWRITER_CONSTITUTION.
- **INFORMATION_ARCHITECTURE.md / .en.md**: Nieuw bestand — beslisboom voor plaatsing van nieuwe content binnen de modulaire structuur.
- **AI_COPYWRITER_CONSTITUTION.md / .en.md**: Nieuw bestand — redactionele principes, toonrichtlijnen en eindtoets voor alle nieuwe content.

### Technische Backlog

| #     | Onderwerp                                               | Status      |
| :---- | :------------------------------------------------------ | :---------- |
| TB-01 | `site_url` instellen voor canonical URL-tags en sitemap | ✅ Gesloten |

______________________________________________________________________

## v1.4 — 2026-03-09

### Stijlgids & Kwaliteitsborging

- **STYLE_GUIDE v2.2** (NL + EN): Terminologietabel bijgewerkt (RAG, Drift, Fine-tunen, Prompts, PoV). Nieuwe secties voor bronvermeldingen `[so-XX]` en admonition-gebruik. Publicatiechecklist uitgebreid met vertaalpariteits-, bronvermeldings- en bronnenlijstcontrole.

### NL Inhoud

- **Homepage**: Typo hersteld ("Alle sjablonen op één plek").
- **Doelkaart template** (`docs/09-sjablonen/06-ai-native-artefacten/doelkaart.md`): Sectie E "Green AI & Duurzaamheid" toegevoegd — 4 velden: proportionaliteit, modelgrootte, groene infrastructuur en e-waste plan.
- **Fase Beheer & Optimalisatie** (`docs/06-fase-monitoring/02-activiteiten.md`): Subsectie "Stopzetting & Decommissioning" toegevoegd met triggertabel (technisch / economisch / ethisch-juridisch / strategisch) en 6-staps afsluitingsproces.

### EN Vertaalpariteit

- **Rollen & Verantwoordelijkheden** (`index.en.md`): Context Builder- en AI Security Officer-subsecties toegevoegd, inclusief tabelrijen in Supporting Roles. Citaties: \[so-44\], \[so-45\].
- **Red Teaming Playbook** (`07-red-teaming.en.md`): Sectie 3b OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10) en sectie 3c aanvalspatronen Deceptive Delight + HashJack toegevoegd, met MTTD/MTTR-tabel. Citaties: \[so-42\], \[so-43\].
- **Batenrealisatie** (`04-batenrealisatie.en.md`): AI Productivity Paradox warning box (Workday 2025) en volledige GAINS™-tabel toegevoegd. Citatie: \[so-46\].
- **Green AI & Sustainability** (`08-green-ai.en.md`): Nieuw bestand — volledige vertaling van de Green AI-module. Ecologische voetafdruk, reductiepotentieel (Cornell 2025), praktische maatregelen per fase en besliskader. Citaties: \[so-47\], \[so-48\].
- **EU AI Act** (`01-eu-ai-act/index.en.md`): Sectie 8 "Additional Legislation & Belgian Context" toegevoegd — AILD-intrekking \[so-40\], herziene PLD \[so-41\], toepasselijkheidstabel en Legal Fragmentation-waarschuwing.
- **Cloud vs On-Premise** (`06-cloud-vs-onpremise.en.md`): Cloud Cost Management-subsectie toegevoegd met 4 kostencategorieën.
- **Kostenoptimalisatie** (`07-kostenoptimalisatie.en.md`): Python routeringsvoorbeeld voor model-tiering toegevoegd (Haiku / Sonnet / Opus).
- **Doelkaart template EN** (`doelkaart.en.md`): Sectie E Green AI toegevoegd; "Knowledge Coupling" → "RAG" gecorrigeerd.
- **Fase Beheer EN** (`02-activiteiten.en.md`): Decommissioning-subsectie toegevoegd.

### Bronnen

- **Bronnenlijst NL + EN**: 11 nieuwe primaire bronnen toegevoegd (\[so-40\] t/m \[so-50\]): GDPR, NIST AI RMF 1.0, AILD-intrekking, herziene PLD, OWASP LLM Top 10 2025, Deceptive Delight/HashJack, Context Engineering, AAISM-certificering, AI Productivity Paradox, Cornell Carbon-Aware AI, IEA Datacenter Energy Reports.

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

- **Netlify livegang**: Hosting overgestapt van FTP naar Netlify via GitHub Actions.
- **PDF-export**: PDF automatisch gegenereerd bij handmatige CI-trigger.
- **CMS**: Decap CMS-configuratie verbeterd (bestandsnamen als weergavenaam).
- Auto-format Markdown via CI verwijderd (mdformat niet compatibel met CMS-output).

______________________________________________________________________

## v1.0 — 2026-02-01

### Initiële Release — Pre-Live Baseline

Eerste release van de gestandaardiseerde AI Project Blauwdruk. Versie op **1.0** tot de proefperiode en feedbackronde is afgerond.

### Inhoud

- **Strategisch Kader**: Managementsamenvatting, AI-levenscyclus, hybride Agile-AI methodologie, governance model, AI-samenwerkingsmodi, organisatorische heruitvinding.
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
