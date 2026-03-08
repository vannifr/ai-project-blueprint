---
versie: '1.0'
pdf: false
---

# AI Safety Checklist

Structured safety checks across four dimensions: training, deployment, monitoring and governance. Use this checklist at every Gate Review for High Risk and Limited Risk systems.

!!! tip "Risk-proportional use"
    Minimal Risk systems: complete section 4 (Governance). Limited Risk: sections 2 + 4. High Risk: all four sections mandatory.

______________________________________________________________________

## Section 1 — Training & Data Safety

*Relevant for self-trained models or fine-tuning. Skip for pure API usage of foundation models.*

| Check                                                              | Status | Note |
| :----------------------------------------------------------------- | :----- | :--- |
| Training data evaluated for harmful content                        | ☐      |      |
| Bias detected and documented in training data                      | ☐      |      |
| Personal data in training data minimised or pseudonymised          | ☐      |      |
| Data sources documented (origin, licence, dates)                   | ☐      |      |
| Adversarial examples included in training set                      | ☐      |      |
| Model weights securely stored (access control, version management) | ☐      |      |

______________________________________________________________________

## Section 2 — Deployment Safety

| Check                                                                           | Status | Note |
| :------------------------------------------------------------------------------ | :----- | :--- |
| **Input filtering** configured (block prohibited inputs)                        | ☐      |      |
| **Output filtering** configured (block prohibited outputs)                      | ☐      |      |
| **Hard Boundaries** documented and technically enforced                         | ☐      |      |
| Rate limiting configured (abuse prevention)                                     | ☐      |      |
| **Circuit Breaker** configured (see [Incident Response](05-incidentrespons.md)) | ☐      |      |
| Least-privilege access: system has minimum required permissions                 | ☐      |      |
| System prompt protected against extraction                                      | ☐      |      |
| Users informed they are interacting with AI (transparency obligation)           | ☐      |      |
| Human-in-the-loop mechanism operational for impactful decisions                 | ☐      |      |
| Exit procedure for users documented (escalation to human)                       | ☐      |      |

______________________________________________________________________

## Section 3 — Monitoring Safety

| Check                                                                                              | Status | Note |
| :------------------------------------------------------------------------------------------------- | :----- | :--- |
| Logging of inputs and outputs active (with retention policy)                                       | ☐      |      |
| Quality monitoring active (thresholds configured)                                                  | ☐      |      |
| **Drift detection** configured (see [Drift Detection](../06-fase-monitoring/05-drift-detectie.md)) | ☐      |      |
| Fairness metrics monitored (if multiple user groups)                                               | ☐      |      |
| Anomaly detection on usage (unusual patterns, abuse)                                               | ☐      |      |
| Alerting to responsible party on threshold breach                                                  | ☐      |      |
| Procedure for harmful output reports by users                                                      | ☐      |      |
| Periodic sample review of outputs scheduled                                                        | ☐      |      |

______________________________________________________________________

## Section 4 — Governance Safety

| Check                                                            | Status | Note |
| :--------------------------------------------------------------- | :----- | :--- |
| **Guardian** appointed and actively involved                     | ☐      |      |
| Safety review performed at every Gate                            | ☐      |      |
| [Red Teaming](07-red-teaming.md) performed (High/Limited Risk)   | ☐      |      |
| Incident response procedure documented and tested                | ☐      |      |
| Accountable owner for the system named                           | ☐      |      |
| Model Card up-to-date with known limitations and risks           | ☐      |      |
| Periodic recertification scheduled (min. annually for High Risk) | ☐      |      |
| EU AI Act compliance status documented                           | ☐      |      |

______________________________________________________________________

## Constitutional AI — Guidelines for Autonomous Systems

For Collaboration Mode 4 and 5 (system acts autonomously), additional Constitutional AI principles apply:

### The Three Core Principles

**1. Harmlessness — No harm**
The system avoids actions that may cause harm to users, third parties or the organisation. Explicitly define which actions are prohibited, regardless of instruction.

**2. Honesty — No deception**
The system communicates transparently about its capabilities, uncertainties and limitations. It does not fabricate facts and indicates when it does not know something.

**3. Helpfulness — Relevant assistance**
The system genuinely attempts to be helpful within the defined scope. Refusal is always justified with an alternative.

### Implementation Checklist for Autonomous Systems

| Requirement                                                             | Status |
| :---------------------------------------------------------------------- | :----- |
| Action scope technically bounded (which systems/actions are accessible) | ☐      |
| Prohibited actions explicitly documented (not only implicitly expected) | ☐      |
| Maximum impact per action bounded (e.g. maximum transaction value)      | ☐      |
| Self-critique mechanism: system checks own output before execution      | ☐      |
| Human approval required above defined impact threshold                  | ☐      |
| Audit trail of all autonomous actions (immutable)                       | ☐      |
| Explainability: system can explain its decision on request              | ☐      |

______________________________________________________________________

## Safety Score

Count the number of checked items per section and calculate the safety score:

| Section                    | Checked | Total  | %   |
| :------------------------- | :------ | :----- | :-- |
| 1 — Training & Data Safety |         | 6      |     |
| 2 — Deployment Safety      |         | 10     |     |
| 3 — Monitoring Safety      |         | 8      |     |
| 4 — Governance Safety      |         | 8      |     |
| **Total**                  |         | **32** |     |

**Minimum threshold for go-live:**

- High Risk: ≥ 90% (≥ 29/32)
- Limited Risk: ≥ 75% (≥ 24/32, section 1 optional)
- Minimal Risk: section 4 complete

______________________________________________________________________

## Related Modules

- [Red Teaming Playbook](07-red-teaming.md)
- [Incident Response](05-incidentrespons.md)
- [EU AI Act](01-eu-ai-act/index.md)
- [Ethical Guidelines](03-ethische-richtlijnen.md)
- [AI Collaboration Modes (HAS-H)](../00-strategisch-kader/06-has-h-niveaus.md)
