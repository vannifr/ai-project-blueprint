---
versie: '1.0'
---

# 1. Checklist: Operational Handover

Use this checklist for the formal handover of the AI system from the project team to the operations organisation (Gate 4 — Go-live). All items must be ticked and documented before the handover is officially complete.

______________________________________________________________________

## 1. Technical Readiness

- [ ] **Model documentation complete:** Technical Model Card is completed and approved by the Guardian.
- [ ] **Code repository delivered:** All source code, configurations and model definitions are in a repository accessible to the operations organisation (version control).
- [ ] **Environment documentation in place:** Infrastructure requirements (compute, storage, network, access rights) are documented.
- [ ] **Runbook available:** Step-by-step guide for daily operation, restart procedures and scaling has been written and tested by the operations organisation.
- [ ] **Monitoring active:** Dashboards, alerts and thresholds are set up and visible to the operations team.
- [ ] **Logging configured:** Input/output logging is active in line with the requirements of the risk level (minimum 30 days retention for Limited Risk, 12 months for High Risk).

______________________________________________________________________

## 2. Operational Readiness

- [ ] **Operations team assigned:** There is a designated owner (Accountable) for the system in the operations organisation.
- [ ] **Escalation path defined:** Incident procedures are documented: who to contact, when, how? → [Incident Response](../../07-compliance-hub/05-incidentrespons.md)
- [ ] **SLOs established:** Service norms (latency, availability, accuracy threshold) have been agreed in writing between the project team and the operations organisation.
- [ ] **Retraining protocol documented:** When and how is the model retrained? Who may initiate this?
- [ ] **Baseline recorded:** Baseline performance (accuracy, latency, usage costs) has been measured and documented as a reference for future performance degradation monitoring.

______________________________________________________________________

## 3. Governance & Compliance

- [ ] **Guardian transferred:** The Guardian role has been formally transferred to a person within the operations organisation or an independent party.
- [ ] **Hard Boundaries communicated:** The operations organisation knows and understands the system's Hard Boundaries. Written confirmation in place.
- [ ] **EU AI Act dossier complete:** For High Risk systems, the Technical Dossier is complete and approved by the Guardian. → [EU AI Act](../../07-compliance-hub/01-eu-ai-act/index.md)
- [ ] **Privacy & Data compliant:** Data & Privacy Sheet (GDPR/DPIA) is approved and included in the dossier.
- [ ] **Licences and contracts arranged:** All external API contracts, data licences and vendor agreements have been transferred to the operations organisation.

______________________________________________________________________

## 4. Knowledge Transfer

- [ ] **User training completed:** End users are trained. Training materials are available and up to date.
- [ ] **Administrator training completed:** Technical operations team has had a hands-on session with the MLOps engineer from the project team.
- [ ] **Lessons Learned transferred:** Insights from the project are documented and available for future projects. → [Lessons Learned](../../11-project-afsluiting/01-lessons-learned.md)
- [ ] **Contact list delivered:** Names and contact details of data providers, model vendors and technical contacts have been transferred.

______________________________________________________________________

## 5. Formal Closure

- [ ] **Handover acceptance signed:** Project team and operations organisation have signed the handover form.
- [ ] **Gate 4 (Go-live) approved:** All Gate Review criteria are ticked and documented. → [Gate Reviews](../../09-sjablonen/04-gate-reviews/checklist.md)
- [ ] **Benefit realisation plan activated:** The plan for measuring realised benefits has been transferred to the owner in the operations organisation. → [Benefit Realisation](../../11-project-afsluiting/03-batenrealisatie.md)
- [ ] **Project archive closed:** All project documents are archived at the agreed location.

______________________________________________________________________

## Signatures

| Role                          | Name | Date | Signature |
| :---------------------------- | :--- | :--- | :-------- |
| Project Lead (AI PM)          |      |      |           |
| Tech Lead                     |      |      |           |
| Guardian                      |      |      |           |
| Operations Organisation Owner |      |      |           |

______________________________________________________________________

**Related modules:**

- [Phase 4: Delivery — Overview](../01-doelstellingen.md)
- [Gate Reviews Checklist](../../09-sjablonen/04-gate-reviews/checklist.md)
- [Lessons Learned](../../11-project-afsluiting/01-lessons-learned.md)
- [Incident Response](../../07-compliance-hub/05-incidentrespons.md)

______________________________________________________________________

**Next step:** Complete this checklist together with the operations team before the formal handover
→ See also: [Gate 4](../../09-sjablonen/04-gate-reviews/checklist.md) | [Phase 5 Monitoring](../../06-fase-monitoring/01-doelstellingen.md)
