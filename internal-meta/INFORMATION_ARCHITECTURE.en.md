# Information Architecture — AI Project Blueprint

**Version:** 1.0
**Date:** 10 March 2026
**Status:** Final

This document describes the structure, placement logic and linking conventions of the AI Project Blueprint. It is the first reference when adding, restructuring or evaluating new content.

______________________________________________________________________

## 1. Site Mission

The Blueprint is a **modular, practical methodology** for AI project management. The site serves two public purposes:

1. **Free reference** for AI Project Managers — searchable, not read linearly
1. **Credibility foundation** for a paid consulting offer

The site is **not an academic publication**, **not product documentation** and **not an LLM training set**. Content that does not directly help an AI PM make better decisions or manage risk does not belong here.

______________________________________________________________________

## 2. Primary Audience

| Persona                   | Reading goal                            | Entry path              |
| ------------------------- | --------------------------------------- | ----------------------- |
| **AI Project Manager**    | Working method, tools, governance       | Navigator → phase guide |
| **Tech Lead**             | Architecture decisions, standards       | Technical Standards     |
| **Guardian / Compliance** | Oversight, gate reviews, EU AI Act      | Compliance Hub          |
| **Executive / Sponsor**   | Value assessment, risk, decision-making | Executive Summary       |

The **AI PM** is the primary user. All content is evaluated against the question: *does this help an AI PM make a better decision?*

______________________________________________________________________

## 3. Content Layers

The site has three layers. Each layer has its own purpose and writing register.

```
Layer 1 — Strategic Framework      (why and what)
  → Principles, governance, roles, lifecycle
  → Register: persuasive, concise, executive-level

Layer 2 — Operational Phases       (how, when, who)
  → Phase-by-phase workflow with activities, deliverables, gates
  → Register: instructional, step-by-step, team-oriented

Layer 3 — Toolkit & Reference      (fill in and look up)
  → Templates, checklists, sources, compliance details
  → Register: functional, scannable, no prose
```

______________________________________________________________________

## 4. Section Structure and Placement Rules

### 4.1 Section Overview

| Section                  | Directory                                  | Layer | Contains                                             |
| ------------------------ | ------------------------------------------ | ----- | ---------------------------------------------------- |
| Navigator                | `docs/00-navigator/`                       | 1     | Interactive wizard — NO new modules                  |
| Explorer Kit             | `docs/00-explorer-kit/`                    | 2     | Accelerated onboarding for Explorers                 |
| Strategic Framework      | `docs/00-strategisch-kader/`               | 1     | Lifecycle, governance, roles, methodology            |
| AI-Native Foundations    | `docs/01-ai-native-fundamenten/`           | 1     | Normative principles, validation model, SDD          |
| Phase 1 — Discovery      | `docs/02-fase-ontdekking/`                 | 2     | Discovery activities, Collaboration Modes, Fast Lane |
| Phase 2 — Validation     | `docs/03-fase-validatie/`                  | 2     | PoV, risk assessment, business case                  |
| Phase 3 — Development    | `docs/04-fase-ontwikkeling/`               | 2     | Development, SDD, testing                            |
| Phase 4 — Delivery       | `docs/05-fase-levering/`                   | 2     | Deployment, traceability, handover                   |
| Phase 5 — Monitoring     | `docs/06-fase-monitoring/`                 | 2     | Drift, monitoring, optimisation                      |
| Continuous Improvement   | `docs/10-doorlopende-verbetering/`         | 2     | Retrospective, Kaizen, KPI                           |
| Project Closure          | `docs/11-project-afsluiting/`              | 2     | Lessons learned, decommissioning                     |
| Compliance Hub           | `docs/07-compliance-hub/`                  | 3     | EU AI Act, Red Teaming, Safety Checklist             |
| Technical Standards      | `docs/08-technische-standaarden/`          | 3     | MLOps, architecture, costs, Green AI                 |
| Roles & Responsibilities | `docs/08-rollen-en-verantwoordelijkheden/` | 1     | Role definitions, RACI                               |
| Toolkit & Templates      | `docs/09-sjablonen/`                       | 3     | All fillable templates                               |
| 90-Day Roadmap           | `docs/12-90-dagen-roadmap/`                | 2     | Week-by-week execution guide                         |
| Organisation Profiles    | `docs/13-organisatieprofielen/`            | 1     | Explorer / Builder / Visionary                       |
| Three Tracks             | `docs/14-drie-tracks/`                     | 1     | Transformation directions                            |
| Accelerators             | `docs/15-accelerators/`                    | 2     | Fast-start tools per track                           |
| Sources                  | `docs/16-bronnen/`                         | 3     | Bibliography `[so-XX]`                               |
| Appendices               | `docs/17-bijlagen/`                        | 3     | External research integration                        |
| Glossary                 | `docs/termenlijst/`                        | 3     | Central terminology                                  |

### 4.2 Decision Tree for New Content

```
Is the new material about an EXISTING topic?
  → Yes: add to the existing document. Do not create a new file.

Is it a PRINCIPLE or GOVERNANCE decision?
  → Yes: belongs in Layer 1 (00-strategisch-kader or 01-ai-native-fundamenten)

Is it a WORKING METHOD per phase?
  → Yes: belongs in the relevant phase directory (02 through 06)

Is it a fillable TEMPLATE or checklist?
  → Yes: belongs in docs/09-sjablonen/ with its own subdirectory

Is it COMPLIANCE-specific or legal?
  → Yes: belongs in docs/07-compliance-hub/

Is it a TECHNICAL architecture decision?
  → Yes: belongs in docs/08-technische-standaarden/

Does it fit nowhere?
  → Stop. Ask: "Does this help an AI PM make a better decision?"
  → No: don't write it.
```

______________________________________________________________________

## 5. File Naming

### Fixed Conventions

| Situation             | Name format                      | Example                                              |
| --------------------- | -------------------------------- | ---------------------------------------------------- |
| Dutch (default)       | `[sequence]-[kebab-case].md`     | `03-ai-architectuur.md`                              |
| English (translation) | `[same name].en.md`              | `03-ai-architectuur.en.md`                           |
| Template              | `template.md` / `template.en.md` | `docs/09-sjablonen/16-rag-design-canvas/template.md` |
| Section index         | `index.md` / `index.en.md`       | `docs/09-sjablonen/index.md`                         |
| Cheatsheet            | `cheatsheet-[topic].md`          | `cheatsheet-red-lines.md`                            |

### Rules

- **Always kebab-case** — no spaces, no underscores, no uppercase
- **Always a sequence number** within a section directory (ensures nav order)
- **Never** create a file without adding it to `mkdocs.yml`
- **Never** create a NL file without immediately planning an EN equivalent (may be filled later, but must be in nav)

______________________________________________________________________

## 6. Nav Management (mkdocs.yml)

Navigation is fully hardcoded in `mkdocs.yml`. MkDocs auto-discovery is disabled.

### When adding a new file

1. Add it to the correct position in `nav:` (NL section)
1. Add a translation in `plugins.i18n.languages[en].nav_translations`
1. Verify that the section index (`index.md`) contains a link to the new file

### Nav Depth

- **Maximum 3 levels deep** in the nav
- Level 1: Section group (e.g. "⚙️ Operational Phases")
- Level 2: Module or phase (e.g. "3. Development")
- Level 3: Page (e.g. "SDD Pattern")
- Deeper than 3 levels: reconsider whether it should be a separate template

______________________________________________________________________

## 7. Cross-linking

### Mandatory Links

Every document must include:

- A `**Related modules:**` block at the end with 2–5 relevant links
- Links to associated templates where they exist
- A backlink to the phase index if it is an activities page

### Link Format

Always use **relative paths**:

```markdown
[Goal Card template](../../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
```

**Never** use absolute URLs for internal links.

### Language Boundary

NL files link to NL files. EN files link to EN files.
Exception: if an EN version does not exist, a link to the NL file is permitted with a `(NL)` suffix.

______________________________________________________________________

## 8. Template–Phase Relationship

Every template in `docs/09-sjablonen/` is primarily linked to one or more phases. This linkage must be explicit in both directions.

| Template                  | Primary phase         | Secondary phase      |
| ------------------------- | --------------------- | -------------------- |
| Project Charter           | Phase 1 — Discovery   | —                    |
| Risk Pre-Scan             | Phase 1 — Discovery   | Phase 2 — Validation |
| Business Case             | Phase 2 — Validation  | —                    |
| Goal Card (Doelkaart)     | Phase 1               | Phase 2, 3           |
| Prompt Engineering        | Phase 3 — Development | Phase 5 — Monitoring |
| Validation Report         | Phase 2               | Phase 3              |
| Guardian Review Checklist | All gates             | —                    |
| RAG Design Canvas         | Phase 3 — Development | —                    |
| RACI Matrix               | Phase 1               | All phases           |

**Rule:** When creating a new template, always update the relevant phase activities page with a reference to the new template.

______________________________________________________________________

## 9. What Does NOT Belong on the Site

- **Product reviews or comparisons** of specific AI tools (ages quickly, no governance value)
- **Framework-specific implementation guides** (e.g. "how to install LangChain") — these belong in external documentation
- **Opinion pieces or blog posts** without direct methodological value
- **Incomplete stubs** — no page is better than an empty page. Use a `!!! info "Coming soon"` admonition as a placeholder for a maximum of 30 days.
- **Duplicate content** — if a concept already exists, deepen or link to it; do not create a second version

______________________________________________________________________

## 10. Methodology Versioning

The Blueprint itself has a version number. Each document has `versie: '1.x'` in the frontmatter.

| Change                                         | Version impact                                     |
| ---------------------------------------------- | -------------------------------------------------- |
| New module or template                         | Minor bump of the relevant document                |
| Change to governance decision or gate criteria | Major bump + entry in BACKLOG.md                   |
| Typo or style correction                       | No version bump required                           |
| Removal of a module                            | Major bump + deprecation notice 30 days in advance |

See `internal-meta/BACKLOG.md` for the roadmap of planned extensions.

______________________________________________________________________

**Related documents:**

- [STYLE_GUIDE.en.md](STYLE_GUIDE.en.md) — tone, terminology, formatting
- [AI_COPYWRITER_CONSTITUTION.en.md](AI_COPYWRITER_CONSTITUTION.en.md) — content principles
- [MODULE_BESCHRIJVINGEN.md](MODULE_BESCHRIJVINGEN.md) — per-module descriptions (NL)
- [BACKLOG.md](BACKLOG.md) — planned extensions
