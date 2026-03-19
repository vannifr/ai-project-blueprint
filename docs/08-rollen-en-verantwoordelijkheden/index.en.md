---
versie: '1.1'
description: 'Roles and responsibilities in AI projects: AI Project Manager, Data Scientist, Domain Expert, Guardian, and more — with RACI matrix and accountability per lifecycle phase.'
type: index
layer: 1
---

# 1. Roles & Responsibilities

!!! abstract "Purpose"
    Overview of all roles in an AI project and their responsibilities per lifecycle phase.

In AI projects the boundaries between business and IT blur. That is why we define roles based on responsibility, not job title.

______________________________________________________________________

## 2. The Core Team (The Squad)

| Role                   | Ownership                                                              | Focus                                                                                                             |
| :--------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **AI Product Manager** | [Objective Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) | "Are we solving the right problem?" — translates business needs into AI instructions                              |
| **Tech Lead**          | [Technical Model Card](../09-sjablonen/02-business-case/modelkaart.md) | "Is it robust and scalable?" — selects model, builds pipelines, safeguards stability                              |
| **Guardian** (duo)     | [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)          | "Is it safe and fair?" — veto rights on hard boundaries. Staffed by Privacy & Legal Officer + AI Quality Ethicist |

For High Risk projects, explicit approval from both Guardian members is required at Gate Reviews.

______________________________________________________________________

## 3. Supporting Roles

| Role                                                                             | Focus          | When to deploy                                                                        |
| :------------------------------------------------------------------------------- | :------------- | :------------------------------------------------------------------------------------ |
| **Data Engineer**                                                                | Data quality   | Always — ensures data arrives clean at the model                                      |
| **AI Tester (QA)**                                                               | Reliability    | From Phase 2 — adversarial testing and Golden Set management                          |
| **Adoption Manager**                                                             | Change         | From Phase 4 — ensures people use the tool (ADKAR)                                    |
| **[Context Builder](../08-technische-standaarden/09-agentic-ai-engineering.md)** | Knowledge mgmt | For RAG systems or multiple knowledge sources — manages what the model sees \[so-44\] |
| **[AI Security Officer](../07-compliance-hub/07-red-teaming.md)**                | Security       | For High/Limited Risk — OWASP LLM Top 10, red teaming, incident response \[so-45\]    |

______________________________________________________________________

## 4. Strategic Level

**Chief AI Officer (CAIO)** — Programme sponsor. Determines the strategy, allocates budget and decides at the Gates whether a project continues or stops.

______________________________________________________________________

## 5. Deep Dives

- [RACI Matrix](02-raci-matrix.md) — who is responsible per activity per phase
- [Stakeholder Communication](03-stakeholder-communicatie.md) — communication plan per audience
- [AI PM Onboarding](04-ai-pm-onboarding.md) — starter guide for new AI Project Managers
- [Decision Matrix](besluitvormingsmatrix.md) — escalation and veto rights per role
