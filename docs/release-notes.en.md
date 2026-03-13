---
versie: '1.5'
pdf: false
---

# Changelog

All significant changes to the AI Project Blueprint are tracked here, most recent first.

______________________________________________________________________

## v1.5 — 2026-03-13

### Migration to ai-delivery.io & SEO

- **New production URL**: Site migrated to <https://ai-delivery.io/>. All internal URL references updated (`site_url`, `url_nl`, `url_en`, `og_image`, sitemap).
- **English as primary language**: Visitors with a non-Dutch browser are automatically redirected to `/en/`. The `x-default` hreflang now points to the English version.
- **robots.txt**: Sitemap URL updated to `https://ai-delivery.io/sitemap.xml`.
- **Schema.org JSON-LD**: Every page now includes structured data (`Organization`, `WebSite`, `Article`, `BreadcrumbList`) for rich snippets in search engines.
- **Per-page meta descriptions**: Unique descriptions added to the 20 most important pages in both NL and EN.
- **site_name / copyright**: Primary site identity updated to "AI Project Blueprint" (EN); the NL language block retains "AI Project Blauwdruk".

### Style Guide & Terminology

- **STYLE_GUIDE v2.3** (NL + EN): Terminology tables extended with two new knowledge domains: Agentic AI (14 terms) and AI Project Management as a discipline (11 terms). Placement rules for new content added, referencing INFORMATION_ARCHITECTURE and AI_COPYWRITER_CONSTITUTION.
- **INFORMATION_ARCHITECTURE.md / .en.md**: New file — decision tree for placing new content within the modular structure.
- **AI_COPYWRITER_CONSTITUTION.md / .en.md**: New file — editorial principles, tone guidelines and final test for all new content.

### Technical Backlog

| #     | Topic                                             | Status    |
| :---- | :------------------------------------------------ | :-------- |
| TB-01 | Set `site_url` for canonical URL tags and sitemap | ✅ Closed |

______________________________________________________________________

## v1.4 — 2026-03-09

### Style Guide & Quality Assurance

- **STYLE_GUIDE v2.2** (NL + EN): Terminology table updated (RAG, Drift, Fine-tuning, Prompts, PoV). New sections for source citations `[so-XX]` and admonition usage. Publication checklist extended with translation parity, citation, and source list checks.

### NL Content

- **Homepage**: Typo fixed ("Alle sjablonen op één plek").
- **Objective Card template** (`docs/09-sjablonen/06-ai-native-artefacten/doelkaart.md`): Section E "Green AI & Sustainability" added — 4 fields: proportionality, model size, green infrastructure and e-waste plan.
- **Monitoring Phase** (`docs/06-fase-monitoring/02-activiteiten.md`): Subsection "Decommissioning" added with trigger table (technical / economic / ethical-legal / strategic) and 6-step shutdown process.

### EN Translation Parity

- **Roles & Responsibilities** (`index.en.md`): Context Builder and AI Security Officer subsections added, including table rows in Supporting Roles. Citations: \[so-44\], \[so-45\].
- **Red Teaming Playbook** (`07-red-teaming.en.md`): Section 3b OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10) and section 3c attack patterns Deceptive Delight + HashJack added, with MTTD/MTTR table. Citations: \[so-42\], \[so-43\].
- **Benefits Realisation** (`04-batenrealisatie.en.md`): AI Productivity Paradox warning box (Workday 2025) and full GAINS™ table added. Citation: \[so-46\].
- **Green AI & Sustainability** (`08-green-ai.en.md`): New file — full translation of the Green AI module. Ecological footprint, reduction potential (Cornell 2025), practical measures per phase and decision framework. Citations: \[so-47\], \[so-48\].
- **EU AI Act** (`01-eu-ai-act/index.en.md`): Section 8 "Additional Legislation & Belgian Context" added — AILD withdrawal \[so-40\], revised PLD \[so-41\], applicability table and Legal Fragmentation warning.
- **Cloud vs On-Premise** (`06-cloud-vs-onpremise.en.md`): Cloud Cost Management subsection added with 4 cost categories.
- **Cost Optimisation** (`07-kostenoptimalisatie.en.md`): Python routing example for model tiering added (Haiku / Sonnet / Opus).
- **Objective Card template EN** (`doelkaart.en.md`): Section E Green AI added; "Knowledge Coupling" → "RAG" corrected.
- **Monitoring Phase EN** (`02-activiteiten.en.md`): Decommissioning subsection added.

### Sources

- **Source list NL + EN**: 11 new primary sources added (\[so-40\] through \[so-50\]): GDPR, NIST AI RMF 1.0, AILD withdrawal, revised PLD, OWASP LLM Top 10 2025, Deceptive Delight/HashJack, Context Engineering, AAISM certification, AI Productivity Paradox, Cornell Carbon-Aware AI, IEA Datacenter Energy Reports.

______________________________________________________________________

## v1.3 — 2026-03-08

### New Content

- **Blueprint Navigator** (`🚀 Getting Started › Blueprint Navigator`): Interactive 4-step wizard guiding new users to their starting point within 5 minutes. Input: role (AI PM / Tech Lead / Guardian / CAIO), organisational context and a 10-question maturity scan. Output: personalised profile (Explorer / Builder / Visionary) + recommended starting module + first 3 actions with direct links. 12 unique routes (4 personas × 3 profiles). Works in light and dark mode.

- **Explorer Kit — 30-Day Starter Programme** (`🚀 Getting Started › Explorer Kit`): Complete package for organisations without AI experience:

    - **30-Day Day-by-Day Plan**: Daily checklist structured by week (Foundation → Discovery → Validation → Decision).
    - **Project Charter Light**: Simplified 1-page project framework (vs. the full 3-page charter).
    - **Quick Risk Pre-Scan**: 15-question risk scan with green/amber/red outcome.
    - **Minimal Validation Report**: 2-page validation report for Gate 1 Review.
    - **Scaffold Code**: Working Python starter code for three use cases: Document Q&A (RAG), Email Classification and Content Generation. Includes Docker-compose setup and troubleshooting guide.

### Navigation & Structure

- Home page updated: Blueprint Navigator and Explorer Kit are now the first two items in "Quick Start".
- `mkdocs.yml`: new navigation block `Explorer Kit (30 Days)` added under `🚀 Getting Started`, including English nav translations.

______________________________________________________________________

## v1.2 — 2026-03-07

### New Content

- **Full English translation**: All documentation available in English via the language selector (top right). Every module has an `.en.md` counterpart.
- **Single-file exports**: Complete blueprint as a single Markdown file (`export-nl.md`, `export-en.md`) for offline use and LLM ingestion.

### Content Corrections

- Phrasing of "referral to human expert" corrected in the SDD pattern (Phase 3).
- 5 stub EN translations completed for priority modules.

### Infrastructure

- FR/DE language support removed (not in use).
- Trunk-based development: no-commit-to-branch git hook removed.

______________________________________________________________________

## v1.1 — 2026-03-02

### New Content

- **Phase 4 (Development)** — Activities and Deliverables pages elaborated.
- **Phase 5 (Delivery)** — Activities page updated with missing content.

### Infrastructure

- **Netlify deployment**: Hosting switched from FTP to Netlify via GitHub Actions.
- **PDF export**: PDF automatically generated on manual CI trigger.
- **CMS**: Decap CMS configuration improved (file names as display names).
- Auto-format Markdown via CI removed (mdformat not compatible with CMS output).

______________________________________________________________________

## v1.0 — 2026-02-01

### Initial Release — Pre-Live Baseline

First release of the standardised AI Project Blueprint. Version set to **1.0** until the trial period and initial feedback round is completed.

### Content

- **Strategic Framework**: Executive summary, AI lifecycle, hybrid Agile-AI methodology, governance model, AI collaboration modes, organisational reinvention.
- **AI-Native Foundations**: Definition, normative criteria, artefact model, validation model, risk classification, SDD pattern, evidence standards.
- **Lifecycle Phases**: All 5 phases elaborated (Discovery & Strategy, Validation, Development, Delivery, Monitoring & Optimisation).
- **Compliance Hub**: EU AI Act, risk management, ethical guidelines, validation requirements, incident response.
- **Technical Standards**: MLOps, data pipelines, model governance, test frameworks, AI architecture.
- **Toolkit**: All templates — Project Charter, Business Case, Model Card, Risk Analysis, Gate Reviews, Validation Report, Traceability, Prompt Engineering, Privacy & Data.
- **Transformation & Growth**: 90-Day Roadmap, Organisation Profiles (Explorer / Builder / Visionary), Three Tracks, Accelerators.
- **Reference**: Glossary, Blueprint Methodology, Sources & Inspiration, DORA 2025 external evidence.

### Breaking Changes

- From v1.0: Gate 2 (PoV Investment) and Gate 3 (Production-ready) require the **Objective Card Validation Report**.
- Evidence must comply with evidence standards (factuality, relevance, completeness).

### Technical Backlog (open)

| #     | Topic                                             | Status |
| :---- | :------------------------------------------------ | :----- |
| TB-01 | Set `site_url` for canonical URL tags and sitemap | Open   |
