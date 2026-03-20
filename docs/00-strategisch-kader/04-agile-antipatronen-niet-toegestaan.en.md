---
versie: '1.1'
type: strategic
layer: 1
tags: [agile]
summary: Overview of the "NOT DONE" anti-patterns that must be avoided in AI projects to prevent failure and compliance issues.
answers: [What does Anti-patterns in AI Projects entail?]
---

# 1. Anti-patterns in AI Projects

!!! abstract "Purpose"
    Overview of the "NOT DONE" anti-patterns that must be avoided in AI projects to prevent failure and compliance issues.

## 1. Objective

This list defines the "NOT DONE" criteria for AI projects: anti-patterns that must be absolutely avoided to prevent failure, unethical behaviour or compliance issues.

______________________________________________________________________

## 2. The "NOT DONE" List

### No Fairness Check (Bias Audit)

- **Rule:** AI systems must be regularly checked for bias.
- **Impact:** Discrimination and reputational damage.

### No Human Oversight

- **Rule:** AI decisions (especially at high risk) must have human approval or 'in-the-loop' supervision in line with the chosen **Collaboration Mode**.
- **Impact:** Uncontrolled errors.

### No Continuous Monitoring

- **Rule:** Models degrade over time (**Performance Degradation**). Continuous monitoring is required.
- **Impact:** Performance loss and unreliable output.

### No Governance Checkpoints

- **Rule:** Every phase must have formal checkpoints (**Gates**).
- **Impact:** Unmanageable risks and budget overruns.

### No Stakeholder Engagement

- **Rule:** Stakeholders and end users must be involved from day one.
- **Impact:** Solutions that are not used.

### No Explainability

- **Rule:** AI decisions must be explainable to the user.
- **Impact:** "Black box" distrust and non-compliance with regulations.

### No Data Evaluation

- **Rule:** Input data must be valid, clean and representative.
- **Impact:** "Garbage in, garbage out".

### No Risk Management

- **Rule:** Risks must be proactively identified and mitigated.
- **Impact:** Unexpected incidents.

### No Traceability

- **Rule:** For every model version it must be traceable on which data and with which **Steering Instructions** it was trained.
- **Impact:** Inability to audit errors.

______________________________________________________________________

## 3. Implementation

Use this list as:

1. **Checklist** during project initiation.
1. **Review criteria** during Gate Reviews.
1. **Training material** for teams to create awareness.
1. **Audit tool** for compliance verification.

______________________________________________________________________
