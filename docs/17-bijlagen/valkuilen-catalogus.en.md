---
versie: '1.0'
type: reference
layer: 3
answers: [What is Pitfalls Catalogue for AI Projects?]
---

# 1. Pitfalls Catalogue for AI Projects

## 1. Purpose

This catalogue consolidates the most common pitfalls in AI projects, grouped by theme. Each pitfall includes a description, the risk and a reference to the Blueprint module that describes the mitigation.

______________________________________________________________________

## 2. Governance & Organisation

| #    | Pitfall                                                                                        | Risk                                              | Mitigation (Blueprint reference)                                            |
| :--- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------ | :-------------------------------------------------------------------------- |
| G-01 | **No governance framework** — AI projects start without clear roles, gates or responsibilities | Uncontrollable outcomes, compliance risk          | [Governance Model](../00-strategisch-kader/03-governance-model.md)          |
| G-02 | **Rubber stamping** — Human reviewer approves AI output blindly                                | Errors pass unnoticed                             | [Collaboration Modes — Mode 2](../00-strategisch-kader/06-has-h-niveaus.md) |
| G-03 | **AI tool sprawl** — Teams use unapproved AI services (AI sprawl)                              | Data leaks, vendor lock-in, compliance violations | [Approved Tools](../07-compliance-hub/08-ai-safety-checklist.md)            |
| G-04 | **Missing escalation paths** — No clear procedure when AI fails                                | Delayed incident response                         | [Incident Playbooks](../07-compliance-hub/06-incidentrespons-playbooks.md)  |
| G-05 | **Governance as blocker** — Excessive governance for low-risk applications                     | Delayed time-to-value, team frustration           | [Fast Lane](../02-fase-ontdekking/06-fast-lane.md)                          |

______________________________________________________________________

## 3. Technical & Engineering

| #    | Pitfall                                                                               | Risk                                                  | Mitigation (Blueprint reference)                                                           |
| :--- | :------------------------------------------------------------------------------------ | :---------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| T-01 | **Blind copy-paste** — Accepting AI code without understanding it                     | Hidden bugs, security vulnerabilities, technical debt | [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)                 |
| T-02 | **Prompt perfectionism** — More time on the prompt than on the solution               | Delayed delivery                                      | [Engineering Patterns — Anti-patterns](../04-fase-ontwikkeling/06-engineering-patterns.md) |
| T-03 | **Unvalidated chain** — Multiple AI steps without intermediate checks                 | Hallucination escalation                              | [Validation Model](../01-ai-native-fundamenten/04-validatie-model.md)                      |
| T-04 | **AI-accelerated technical debt** — AI generates code faster than the team can review | Debt accumulates exponentially                        | [SDD Pattern](../04-fase-ontwikkeling/05-sdd-patroon.md)                                   |
| T-05 | **Context pollution** — Too much or irrelevant context provided to AI                 | Lower quality, higher costs                           | [Context Builder](../08-rollen-en-verantwoordelijkheden/index.md)                          |
| T-06 | **Infinite agent loop** — Agent repeats steps without progress                        | Cost explosion                                        | [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)        |
| T-07 | **Agent scope creep** — Agent interprets mandate more broadly than intended           | Unauthorised actions                                  | [Acceptance Criteria Mode 4-5](../00-strategisch-kader/06-has-h-niveaus.md)                |

______________________________________________________________________

## 4. Data & Quality

| #    | Pitfall                                                                         | Risk                                            | Mitigation (Blueprint reference)                                                |
| :--- | :------------------------------------------------------------------------------ | :---------------------------------------------- | :------------------------------------------------------------------------------ |
| D-01 | **Undetected data bias** — Training or RAG data contains systematic distortions | Discriminatory output                           | [Ethical Guidelines](../07-compliance-hub/03-ethische-richtlijnen.md)           |
| D-02 | **No baseline** — No measurement of current performance before AI deployment    | Impossible to demonstrate improvement           | [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)  |
| D-03 | **Silent degradation** — Model quality gradually declines without alarm         | Users receive progressively worse output        | [Performance Degradation Detection](../06-fase-monitoring/05-drift-detectie.md) |
| D-04 | **Unmitigated hallucinations** — AI generates plausible but incorrect facts     | Legal risk, reputational damage                 | [Red Teaming](../07-compliance-hub/07-red-teaming.md)                           |
| D-05 | **Stale knowledge base** — RAG sources are not updated                          | Incorrect answers based on outdated information | [Management & Optimisation](../06-fase-monitoring/02-activiteiten.md)           |

______________________________________________________________________

## 5. Organisation & People

| #    | Pitfall                                                                  | Risk                                       | Mitigation (Blueprint reference)                                                 |
| :--- | :----------------------------------------------------------------------- | :----------------------------------------- | :------------------------------------------------------------------------------- |
| O-01 | **Skill atrophy** — Team loses domain expertise as AI takes over work    | Nobody can assess AI output any more       | [Collaboration Modes — Mode 4 risk](../00-strategisch-kader/06-has-h-niveaus.md) |
| O-02 | **AI theatre** — Pilots without measurable business value                | Wasted budget, stakeholder fatigue         | [Benefits Realisation](../10-doorlopende-verbetering/04-batenrealisatie.md)      |
| O-03 | **No adoption strategy** — AI tools available but not used               | Licence costs without value                | [Adoption Manager](../08-rollen-en-verantwoordelijkheden/index.md)               |
| O-04 | **Autonomy leap** — Jumping directly to Mode 4-5 without learning phases | Unmanageable systems                       | [Start low, scale up](../00-strategisch-kader/06-has-h-niveaus.md)               |
| O-05 | **Missing owner** — No clear owner for AI system in production           | Drift goes unnoticed, incidents unresolved | [Roles & Responsibilities](../08-rollen-en-verantwoordelijkheden/index.md)       |

______________________________________________________________________

## 6. Cost & ROI

| #    | Pitfall                                                                          | Risk                                         | Mitigation (Blueprint reference)                                                                      |
| :--- | :------------------------------------------------------------------------------- | :------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| K-01 | **Only usage costs calculated** — TCO misses governance, monitoring, integration | Budget overrun                               | [Cost Optimisation](../08-technische-standaarden/07-kostenoptimalisatie.md)                           |
| K-02 | **No cost limit per agent task** — Agent runs without limits                     | Bill shock from infinite loops               | [Agentic AI Engineering — Cost Management](../08-technische-standaarden/09-agentic-ai-engineering.md) |
| K-03 | **ROI measured too early** — Drawing conclusions about value after 4-6 weeks     | Premature cancellation of promising projects | [Benefits Realisation](../10-doorlopende-verbetering/04-batenrealisatie.md)                           |
| K-04 | **Rework not measured** — Time savings from AI are negated by correction work    | False productivity picture                   | [Engineering Patterns — Rework](../04-fase-ontwikkeling/06-engineering-patterns.md)                   |

______________________________________________________________________

## 7. Using this Catalogue

- **At project start:** Walk through the categories relevant to the risk profile.
- **At gate reviews:** Verify that identified pitfalls have been mitigated.
- **At retrospectives:** Use the catalogue as a checklist for lessons learned.

______________________________________________________________________

## 8. Related Modules

- [Governance Model](../00-strategisch-kader/03-governance-model.md)
- [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
- [Risk Management](../07-compliance-hub/02-risicobeheer/index.md)

______________________________________________________________________
