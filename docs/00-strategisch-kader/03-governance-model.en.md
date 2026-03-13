---
versie: '1.1'
description: 'AI governance model: decision rights, oversight structures, and accountability frameworks for responsible AI deployment — aligned with EU AI Act and PMI-CPMAI requirements.'
---

# 1. Governance Model

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

| Role                         | Level       | Core Responsibilities                                        |
| :--------------------------- | :---------- | :----------------------------------------------------------- |
| **CAIO** (Chief AI Officer)  | Strategic   | Strategy, ROI oversight, Governance ultimate accountability. |
| **Executive Committee**      | Strategic   | Budget approval, strategic alignment.                        |
| **AI Product Manager**       | Operational | Use case priority, Stakeholder management, Backlog owner.    |
| **AI Transformation Office** | Operational | Process oversight, standardisation, training.                |
| **Data Scientist**           | Technical   | Model development, validation, experimentation.              |
| **ML Engineering**           | Technical   | **Go-live** pipelines, monitoring, infrastructure.           |
| **Guardian (Ethicist)**      | Supporting  | Fairness checks, Bias audits, Compliance checks.             |
| **Security Officer**         | Supporting  | Security measures, Privacy safeguarding.                     |

______________________________________________________________________

## 4. Decision-Making Process (Gate Model)

```mermaid
flowchart TD
 A[Initiative] --> B{Gate 1 (Go/No-Go Discovery): Discovery}
 B -->|Go| C[Validation]
 B -->|No Go| X[Stop]
 C --> D{Gate 2 (PoV Investment): Cost Overview}
 D -->|Go| E[Development]
 D -->|No Go| X
 E --> F{Gate 3 (Production-Ready): Go-live}
 F -->|Go| G[Monitoring & Optimisation]
 F -->|No Go| X
 G --> H{Gate 4 (Go-live): Continue?}
 H -->|Yes| A
 H -->|No| I[Closure]
```

## 5. Gate Reviews

Each gate acts as a hard stop/go decision. See the [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) for specific criteria per phase.

______________________________________________________________________
