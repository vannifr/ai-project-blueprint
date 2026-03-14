---
versie: '1.0'
type: template
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [Guardian]
tags: [ethics, gate-review, template]
---

# Guardian Review Checklist

The Guardian safeguards the ethical and legal frameworks of an AI system. This checklist guides the Guardian through all formal review moments in the lifecycle — from Gate 1 through decommissioning.

!!! info "Two-Man Rule for High Risk"
    For AI systems with risk classification **High**, explicit approval is required from two people: the **Privacy & Legal Officer** (tests against GDPR + EU AI Act) and the **AI Quality Ethicist / QA Lead** (tests for bias, Golden Set quality, output safety).

______________________________________________________________________

## 1. Mandate & Independence

Ensure the mandate is clearly documented before the first review.

- [ ] Guardian has been formally appointed and accepted by the project team.
- [ ] Mandate includes veto rights at all Gate Reviews.
- [ ] Guardian has no direct interest in the project outcome (independence).
- [ ] For **High Risk**: Two-Man Rule active (Privacy Officer + AI Quality Ethicist both appointed).
- [ ] Contact persons and escalation paths are documented.

______________________________________________________________________

## 2. Gate 1 Review — Discovery & Strategy

**Moment:** Before go-ahead to Validation (PoV).

### Risk & Scope

- [ ] Risk Pre-Scan has been completed and risk classification determined.
- [ ] Risk classification is realistic (not underestimated to avoid compliance).
- [ ] For High Risk: EU AI Act Article 9 (risk management system) applies — confirmed.

### Hard Boundaries & Objective Card

- [ ] Objective Card has been drawn up with explicit Hard Boundaries (what is the system absolutely not allowed to do?).
- [ ] Hard Boundaries are concrete and verifiable (no vague formulations).
- [ ] Green AI considerations have been completed (Section E of the Objective Card).
- [ ] Guardian has approved and signed the Hard Boundaries.

**Gate 1 outcome:**

- [ ] Approved — proceed to Validation (PoV)
- [ ] Approved with conditions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- [ ] Rejected — reason: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Guardian signature: \_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 3. Gate 2 Review — PoV Investment

**Moment:** Before go-ahead to Development.

### Dataset & Fairness

- [ ] Training dataset is documented (source, size, date range).
- [ ] Dataset has been checked for representational bias (age, gender, geography, etc.).
- [ ] Privacy-sensitive data has been identified and anonymised or masked.
- [ ] Data sourcing complies with GDPR (lawful basis, data minimisation).

### Business Case & Proportionality

- [ ] Business Case is ethically justified: benefits outweigh risks.
- [ ] Is AI proportionate? Can a simpler system (rule-based, smaller model) perform the same task?
- [ ] Planned AI contribution is realistic (no AI Productivity Paradox pitfall; expected organisation-wide gain 5–15%).

### Hard Boundaries in Objective Card

- [ ] Hard Boundaries are recorded in the Objective Card (Section D).
- [ ] Hard Boundaries cannot be changed without Guardian approval.

**Gate 2 outcome:**

- [ ] Approved — proceed to Development
- [ ] Approved with conditions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- [ ] Rejected — reason: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Guardian signature: \_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 4. Gate 3 Review — Go-Live (Production)

**Moment:** Before going live in production.

### Red Team & Safety

- [ ] Red Team session has been conducted (mandatory for High Risk).
- [ ] No open **Critical** or **High** findings in the Red Team report.
- [ ] OWASP Top 10 LLM 2025 has been completed as minimum scope.
- [ ] Deceptive Delight and HashJack attack patterns have been tested.
- [ ] AI Safety Checklist has been completed and approved.

### Compliance

- [ ] GDPR: privacy impact has been assessed; DPIA conducted where required.
- [ ] EU AI Act: technical dossier is up to date (for High Risk systems).
- [ ] Traceability report is present (from data to output).
- [ ] Prompts are versioned and documented (per Prompt Versioning template).

### Operational Readiness

- [ ] Incident response plan is active and tested.
- [ ] Monitoring and alerting are configured (drift, hallucination rate, MTTD \< 15 min).
- [ ] Decommissioning triggers are documented in the monitoring configuration.
- [ ] Handover to management organisation is complete (Handover Checklist signed off).

**Gate 3 outcome:**

- [ ] Approved for go-live
- [ ] Approved with conditions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- [ ] Not approved — open findings: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Guardian signature (Privacy Officer): \_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_

Guardian signature (AI Quality Ethicist): \_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 5. Ongoing Oversight (Post-Live)

Periodic Guardian checks after go-live.

### Quarterly check

- [ ] Benefits Realisation Report received and reviewed.
- [ ] No unresolved incidents with Guardian escalation.
- [ ] Drift reports reviewed: no structural bias escalation.
- [ ] Kaizen Log updated with Guardian notes.

### Annual re-review (mandatory for High Risk)

- [ ] Renewed Red Team session conducted.
- [ ] Legal framework re-assessed (EU AI Act updates, new regulations).
- [ ] Objective Card and Hard Boundaries reviewed for continued relevance.

______________________________________________________________________

## 6. Decommissioning Review

**Moment:** Upon shutdown of the AI system.

- [ ] Shutdown decision has been formally made by CAIO or steering committee.
- [ ] Users have been informed in good time (minimum 30 days in advance).
- [ ] Personal data has been deleted in accordance with GDPR (right to erasure).
- [ ] Models and configurations have been archived or destroyed (per policy).
- [ ] Knowledge transfer to management organisation is complete.
- [ ] Guardian final judgement documented in Kaizen Log.

Guardian signature: \_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

**Related modules:**

- [Roles & Responsibilities](../../08-rollen-en-verantwoordelijkheden/index.md)
- [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md)
- [Objective Card template](../06-ai-native-artefacten/doelkaart.md)
- [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md)
- [Incident Response](../../07-compliance-hub/05-incidentrespons.md)
