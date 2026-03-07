---
versie: '1.0'
---

# 1. Technical Standards & Delivery Criteria

## 1. Purpose

This module defines what "production-ready" means for AI solutions, including a realistic pathway:

- **Basic** (manual governance, minimal automation)
- **Advanced** (more automation, CI/CD/quality gates)

## 2. Automation Ladder (Realistic Growth Path)

| Level                     | Description                       | For whom          | Example controls                        |
| ------------------------- | --------------------------------- | ----------------- | --------------------------------------- |
| **L0 Manual**             | Checklists + manual gates         | starting teams    | templates completed, signatures         |
| **L1 Semi**               | fixed test set + fixed reporting  | most teams        | Objective Card every release            |
| **L2 Automated testing**  | tests run automatically on change | engineering teams | regression test on Golden Set           |
| **L3 Governance-as-Code** | policy checks block release       | mature MLOps      | release fails without evidence/metadata |

## 3. Minimum Technical Baseline (Every Team Must Reach)

!!! check "Reproducibility & version control"
    - [ ] Code/instructions are in version control (repo)
    - [ ] Config (model version, settings) is traceable
    - [ ] Release is taggable (RC-1, v1.0) + rollback plan exists

!!! check "Security & access"
    - [ ] Secrets not hardcoded; access via secure storage
    - [ ] Role-based access (who may change prompts/config?)
    - [ ] Least privilege on data sources

!!! check "Observability (minimum)"
    - [ ] Logging in place (model version, prompt version, source IDs, output status)
    - [ ] Basic metrics: error rate, latency, volume
    - [ ] Incident process is known (who calls whom)

!!! check "Quality & evidence"
    - [ ] Golden Set exists and is used
    - [ ] [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md) available for pilot/RC
    - [ ] Meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md) norms for risk level

## 4. Basic Route (Without Heavy MLOps)

**Goal:** safely go live with minimal tooling.

- Use templates as "single source of truth"
- Plan fixed evaluation moments (e.g. weekly in pilot, monthly in management)
- Logging minimum: metadata + sampling output (where privacy allows)

## 5. Advanced Route (With More Automation)

**Goal:** scalable management with multiple use cases.

- Automatic regression tests on Golden Set at every change
- Automatic generation of Validation Report from test runs (where possible)
- Integration of policy checks: "no Validation Report = no release"

## 6. Definition of Done for Go-Live

!!! check "Go-Live Checklist"
    - [ ] Gate 3 (Production-Ready) approved (Validation Report RC meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md))
    - [ ] Logging/retention set up (incl. privacy measures)
    - [ ] Incident & rollback procedure tested (tabletop exercise or simulation)
    - [ ] Owner for management appointed + monitoring active
    - [ ] User instructions + transparency (if relevant) published
