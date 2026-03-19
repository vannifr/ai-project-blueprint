---
versie: '1.1'
type: technical
layer: 3
roles: [Data Scientist, Tech Lead]
tags: [governance]
---

# 1. Model Governance

## 1. Purpose

This module defines how we manage AI models throughout their lifecycle: from development to production and eventual retirement. Good model governance ensures traceability, controllability and safe releases.

______________________________________________________________________

## 2. Core Principles

### Every Model Has an Owner

- Every AI solution has one designated **Tech Lead** responsible for technical quality.
- The owner is the point of contact for incidents, updates and decommissioning.

### Everything Is Version-Controlled

- Model weights, configurations and System Prompts are in version control.
- Changes are traceable: who changed what and when?

### No Change Without Review

- Changes to production models require review by at least one other team member.
- For High Risk: Guardian review mandatory.

______________________________________________________________________

## 3. Model Registry

A central location where all models are registered with their metadata.

### Minimum Metadata per Model

| Field               | Description                                     | Example                     |
| ------------------- | ----------------------------------------------- | --------------------------- |
| Model ID            | Unique identification                           | `invoice-classifier-v2.1`   |
| Version             | Semantic version or hash                        | `2.1.0` or `abc123`         |
| Status              | Development / Staging / Production / Deprecated | Production                  |
| Owner               | Responsible person/team                         | Team Finance AI             |
| Creation date       | When trained/deployed                           | 2026-01-15                  |
| Data source version | Which data used for training                    | `invoices-2025-q4`          |
| System Prompt       | Link to prompt/config version                   | `prompts/invoice-v2.1.yaml` |
| Validation Report   | Link to accompanying evidence                   | `reports/invoice-v2.1.md`   |
| Risk level          | Classification according to EU AI Act           | Limited                     |

### Implementation Options

| Option                       | Suitable for                          | Complexity |
| ---------------------------- | ------------------------------------- | ---------- |
| Spreadsheet/Wiki             | Starting teams, few models            | Low        |
| Git repository with YAML     | Engineering teams                     | Medium     |
| Experiment tracking platform | Mature MLOps environment, many models | High       |

______________________________________________________________________

## 4. Approval Workflow

### Standard Flow (Limited Risk)

```
[Development] → [Code Review] → [Staging Test] → [Gate Review] → [Production]
```

- **Code Review:** At least one peer review
- **Staging Test:** Golden Set test on staging environment
- **Gate Review:** Validation Report meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)

### Extended Flow (High Risk)

```
[Development] → [Code Review] → [Guardian Review] → [Staging Test] → [Fairness Check] → [Gate Review] → [Phased Rollout] → [Production]
```

- **Guardian Review:** Independent assessment against Hard Boundaries
- **Fairness Check:** Quantitative bias analysis
- **Phased Rollout:** Start with limited user group, monitor, then full rollout

______________________________________________________________________

## 5. Model Lifecycle

| Phase       | Characteristics          | Actions                               |
| ----------- | ------------------------ | ------------------------------------- |
| Development | Experiments, prototypes  | No production data, no external users |
| Staging     | Candidate for production | Full Golden Set test, review          |
| Production  | Live, actively used      | Monitoring, incident procedure active |
| Deprecated  | Being phased out         | No new users, migration plan active   |
| Retired     | No longer available      | Archiving, documentation preserved    |

______________________________________________________________________

## 6. Change Management

### Types of Changes

| Type                 | Example                             | Required Approval             |
| -------------------- | ----------------------------------- | ----------------------------- |
| Configuration change | Temperature from 0.7 to 0.5         | Peer review                   |
| Prompt change        | Rewriting instruction               | Peer review + regression test |
| Model version update | New base model (e.g. GPT-4 → GPT-5) | Full Gate Review              |
| Data source change   | Coupling new knowledge base         | Guardian review (High Risk)   |

### Rollback Procedure

- Every production release has a documented rollback plan.
- Rollback must be executable within 30 minutes.
- After rollback: incident analysis and documentation.

______________________________________________________________________

## 7. Model Governance Checklist

!!! check "Model Governance Checklist"
    - [ ] Model registry is set up and up to date
    - [ ] All production models have an owner
    - [ ] Approval workflow is documented and followed
    - [ ] Change management is set up with rollback procedure
    - [ ] Models are linked to Validation Reports

______________________________________________________________________

## 8. Related Modules

- [Technical Standards & Delivery Criteria](01-mloops-standaarden.md)
- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Risk Management & Compliance](../07-compliance-hub/index.md)
