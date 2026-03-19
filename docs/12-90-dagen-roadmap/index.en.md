---
versie: '1.0'
description: '90-day AI transformation roadmap: three structured phases — Focus, Pilot, and Scale — to move from AI ambition to production-ready deployment within a quarter.'
type: index
layer: 2
roles: [Business Sponsor]
---

# 1. Quick Start: AI Project in 90 Days

!!! abstract "Purpose"
    Structured roadmap to go from AI ambition to production-ready deployment in three phases (Focus, Pilot, Scale) within 90 days.

## 1. Prerequisites (Definition of Ready)

- Core team designated: **AI Product Manager**, **Tech Lead**, **Guardian**
- Access to relevant data arranged (minimum read rights)
- Workspace ready: repo/wiki + space for templates + decision log
- One use case selected (max 1) with a clear owner

______________________________________________________________________

## 2. Planning (Week by Week)

| Week | Goal                          | Deliverables (mandatory)                                                                                                               | Primary owner        | Gate/Output                                   |
| ---: | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------------- |
|    1 | Use case sharp + scope        | [Project Charter](../09-sjablonen/01-project-charter/template.md) (concept)                                                            | AI PM                | Go/no-go on problem definition                |
|    2 | Risk + data feasibility       | [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md), Data Evaluation summary                                                 | Guardian + Tech Lead | Gate 1 (Go/No-Go Discovery): continue?        |
|    3 | Objective + Hard Boundaries   | [Business Case](../09-sjablonen/02-business-case/template.md) (v1)                                                                     | AI PM + Guardian     | Hard Boundaries approved                      |
|    4 | Set up test basis             | [Golden Set Test](../09-sjablonen/07-validatie-bewijs/template.md) + Golden Set v1                                                     | AI PM + QA/Tech      | Test plan ready                               |
|    5 | Prototype (pilot)             | Prototype + [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) (concept)                                            | Tech Lead            | Internal demo                                 |
|    6 | Measure pilot                 | [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md) (pilot)                                                   | Tech Lead + AI PM    | Gate 2 (Validation Pilot Investment): to Dev? |
|    7 | Development: integration path | Integration plan + logging plan                                                                                                        | Tech Lead            | Ready for RC                                  |
|    8 | Privacy & security checks     | [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md)                                                                 | Guardian + Privacy   | "OK to proceed"                               |
|    9 | Build Release Candidate       | RC build + [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) (v1); *Batch size policy defined and communicated*    | Tech Lead            | RC ready                                      |
|   10 | Test RC & evidence            | [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md) (RC); *CI feedback SLOs established (agreed time window)* | QA + Guardian        | Gate 3 (Production-Ready): Go Live?           |
|   11 | Live pilot + monitoring       | Monitoring + incident process active; *AI-assisted development hard boundaries implemented (mandatory review, test coverage)*          | Tech Lead            | 1st production evaluation                     |
|   12 | Optimise + handover           | Management plan + baseline performance degradation; *Regression on Golden Set enforced before RC* — Source: \[so-28\]                  | Tech Lead + AI PM    | Handover Management & Optimisation            |
|   13 | Retrospective + standardise   | Lessons learned + blueprint updates                                                                                                    | AI CC                | v2.3 backlog                                  |

______________________________________________________________________

## 3. Minimum Decision Moments (Gates)

- **Gate 1 (Go/No-Go Discovery) (end of week 2):** risk + data feasibility confirmed
- **Gate 2 (Validation Pilot Investment) (end of week 6):** pilot result ([Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)) meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- **Gate 3 (Production-Ready) (end of week 10):** RC meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md) + logging/privacy arranged
- **Gate 4 (Go-Live) (week 12):** handover to management incl. baseline performance degradation

______________________________________________________________________

## 4. Timeline per Risk Level

The standard 13-week planning is suitable for **Limited Risk** applications. Adjust the timeline based on your risk classification:

### Minimal Risk (Fast Lane): 6-8 weeks

| Phase         | Weeks | Focus                                     |
| ------------- | ----: | ----------------------------------------- |
| Discovery     |   1-2 | Charter + Risk Pre-Scan + Objective Card  |
| Validation    |   3-4 | Prototype + Golden Set (20 cases) + Pilot |
| Go-Live       |   5-6 | Validation Report + Monitoring basics     |
| Stabilisation |   7-8 | Optimisation + Handover                   |

See [Fast Lane](../02-fase-ontdekking/06-fast-lane.md) for admission criteria.

### Limited Risk: 13 weeks (standard)

Follow the week-by-week planning in section 1 above.

### High Risk: 18-24 weeks

| Phase                   | Weeks | Additional activities vs standard                       |
| ----------------------- | ----: | ------------------------------------------------------- |
| Discovery               |   1-3 | Extended DPIA, legal review, Guardian approval          |
| Data Governance         |   4-6 | Data lineage, extended quality controls, bias analysis  |
| Validation              |  7-12 | Golden Set (150+ cases), Fairness Check, external audit |
| Development             | 13-18 | Extended technical dossier, CE preparation              |
| Go-Live & Stabilisation | 19-24 | Phased rollout, intensive monitoring, Guardian reviews  |

**Additional requirements High Risk:**

- Full EU AI Act compliance documentation
- Independent Guardian review at every Gate
- Quantitative Fairness Check with mitigation plan
- 100% input/output logging with 12-month retention

______________________________________________________________________

## Fast Lane

For systems with **Minimal Risk**, the 13-week roadmap can be shortened to **6–8 weeks**:

| Week | Fast Lane activity                                                     |
| :--- | :--------------------------------------------------------------------- |
| 1–2  | Project Charter + Risk Pre-Scan (no extended business case)            |
| 3–4  | Prototype + quick Validation Pilot (minimal Golden Set: 20 test cases) |
| 5–6  | Validation + direct go-live (Gate 1 + Gate 3 combined)                 |
| 7–8  | Set up monitoring + first drift measurement                            |

> **Fast Lane criteria:** Minimal Risk, Mode 1–2, no personal data, internal users only.

______________________________________________________________________

**Next step:** Start with [Phase 1: Set Focus & Rationalise](01-fase-1-richt-focus-rationaliseer.md)
→ See also: [Explorer Kit](../00-explorer-kit/index.md) | [Organisation Profiles](../13-organisatieprofielen/index.md)
