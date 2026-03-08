---
versie: '1.3'
pdf: false
---

# Changelog

All significant changes to the AI Project Blueprint are tracked here, most recent first.

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

- **Strategic Framework**: Executive summary, AI lifecycle, hybrid Agile-AI methodology, governance model, AI collaboration modes (HAS-H levels), organisational reinvention.
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
