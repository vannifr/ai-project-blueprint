---
versie: '1.0'
description: 'Quick reference card for the 5-phase AI lifecycle: goal per phase, gate criteria, core activity and primary template — everything on one page.'
type: strategic
layer: 1
summary: One-page overview of the five AI lifecycle phases with the goal, gate criteria, core activity and primary template per phase.
answers: [What does AI Project Cycle — Quick Reference entail?]
---

# AI Project Cycle — Quick Reference

!!! abstract "Purpose"
    One-page overview of the five AI lifecycle phases with the goal, gate criteria, core activity and primary template per phase.

> This is a navigation card, not an explanation. For the full methodology: see [AI Project Cycle](01-ai-levenscyclus.en.md).

______________________________________________________________________

| Phase                             | Goal                                             | Gate                          | Core Activity                                      | Primary Template                                                                |
| :-------------------------------- | :----------------------------------------------- | :---------------------------- | :------------------------------------------------- | :------------------------------------------------------------------------------ |
| **1 — Discovery & Strategy**      | Validate problem, evaluate data, assess risk     | Gate 1: Go/No-Go problem def. | Complete Goal card + Collaboration Mode Assessment | [Project Charter](../09-sjablonen/01-project-charter/template.en.md)            |
| **2 — Validation (PoV)**          | Test hypothesis at small scale, substantiate ROI | Gate 2: Investment decision   | Execute Proof of Value + Business Case             | [Validation report](../09-sjablonen/07-validatie-bewijs/validatierapport.en.md) |
| **3 — Realisation**               | Build system to spec, validate Golden Set        | Gate 3: Production readiness  | SDD pattern: spec → golden set → build → validate  | [Technical Model Card](../09-sjablonen/02-business-case/modelkaart.en.md)       |
| **4 — Delivery**                  | Deploy to production, hand over to operations    | Gate 3 (continued): Go-live   | Handover checklist + user training                 | [Handover Checklist](../09-sjablonen/index.en.md)                               |
| **5 — Operations & Optimisation** | Monitor drift, manage costs, process feedback    | Gate 4: Quarterly review      | Drift measurement + cost efficiency review         | [Operations Plan](../09-sjablonen/index.en.md)                                  |

______________________________________________________________________

## Timeline per risk class

| Risk class   | Typical lead time | Fast Lane? |
| :----------- | :---------------- | :--------- |
| Minimal Risk | 6–8 weeks         | ✅ Yes     |
| Limited Risk | 13 weeks          | Optional   |
| High Risk    | 18–24 weeks       | ❌ No      |

______________________________________________________________________

## Four Core Artefacts (always required)

| Artefact              | What it records                                | Created in |
| :-------------------- | :--------------------------------------------- | :--------- |
| **Goal definition**   | The human intent behind the system             | Phase 1    |
| **Hard Boundaries**   | What the system must never do                  | Phase 1    |
| **Prompts**           | The steering instructions for the AI system    | Phase 1–3  |
| **Validation report** | The evidence that the system works as intended | Phase 2–3  |

> For the full explanation of these artefacts: see [AI-Native Fundamentals](../01-ai-native-fundamenten/01-definitie.md).

______________________________________________________________________

**Related modules:**

- [Full AI Lifecycle](01-ai-levenscyclus.en.md)
- [Collaboration Modes](06-has-h-niveaus.en.md)
- [90-Day Roadmap](../12-90-dagen-roadmap/index.md)
- [All Templates](../09-sjablonen/index.en.md)

______________________________________________________________________

**Version:** 1.0
**Date:** 13 March 2026
**Status:** Final
