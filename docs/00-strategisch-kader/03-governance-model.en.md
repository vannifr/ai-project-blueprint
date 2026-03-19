---
versie: '1.1'
description: 'AI governance model: decision rights, oversight structures, and accountability frameworks for responsible AI deployment — aligned with EU AI Act and PMI-CPMAI requirements.'
type: strategic
layer: 1
roles: [Data Scientist]
tags: [governance]
---

# 1. Governance Model

!!! abstract "Purpose"
    Definition of the decision-making structures, roles and oversight layers that steer AI projects safely and effectively.

## 1. Objective

Defining the decision-making structures, roles and responsibilities to steer AI projects safely and effectively.

______________________________________________________________________

## 2. Structure

The governance model consists of three layers that work together to connect strategy, operations and technology:

1. **Strategic Level:** Focus on vision and **Cost Overview**.
1. **Operational Level:** Focus on execution and priority.
1. **Technical Level:** Focus on quality and **Go-live**.

______________________________________________________________________

## 3. Responsibilities

| Role                         | Level       | Core Responsibilities                                                          |
| :--------------------------- | :---------- | :----------------------------------------------------------------------------- |
| **CAIO** (Chief AI Officer)  | Strategic   | Strategy, ROI oversight, Governance ultimate accountability.                   |
| **Executive Committee**      | Strategic   | Budget approval, strategic alignment.                                          |
| **AI Product Manager**       | Operational | Use case priority, Stakeholder management, Backlog owner.                      |
| **AI Transformation Office** | Operational | Process oversight, standardisation, training.                                  |
| **Data Scientist**           | Technical   | Model development, validation, experimentation.                                |
| **ML Engineering**           | Technical   | **Go-live** pipelines, monitoring, infrastructure.                             |
| **Guardian**                 | Supporting  | Safeguards all boundaries: Fairness Audits, Compliance checks, ethical review. |
| **Security Officer**         | Supporting  | Security measures, Privacy safeguarding.                                       |

______________________________________________________________________

## 4. Decision-Making Process (Gate Model)

```mermaid
flowchart TD
 A["🟢 Initiative\nIdea or business case"] --> B{"Gate 1\nProblem clear?\nData available?"}
 B -->|"✅ Go"| C["Phase 2: Validation\nRun validation pilot"]
 B -->|"❌ No Go"| X["⏹ Stop"]
 C --> D{"Gate 2\nInvestment Decision\nBusiness case approved?"}
 D -->|"✅ Go"| E["Phase 3: Realisation\nBuild production-ready"]
 D -->|"❌ No Go"| X
 E --> F{"Gate 3\nProduction-Ready?\nAll tests passed?"}
 F -->|"✅ Go"| G["Phase 4: Management\n& Optimisation"]
 F -->|"❌ No Go"| X
 G --> H{"Gate 4\nQuarterly Review\nContinue?"}
 H -->|"✅ Yes"| A
 H -->|"❌ No"| I["Closure"]
```

## 5. Gate Reviews

Each gate acts as a hard stop/go decision. See the [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) for specific criteria per phase.

______________________________________________________________________
