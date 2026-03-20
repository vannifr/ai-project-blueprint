---
versie: '1.0'
type: template
layer: 3
phase: [1, 2]
tags: [template]
answers: [How do I use the Experiment Ticket template?]
---

# Experiment Ticket

This template guides your team through setting up, executing and evaluating a time-boxed AI experiment sprint. Each experiment follows a structured path from hypothesis to decision, aligned with the AI Project Blueprint Gate structure.

!!! info "When to use this template"
    Use this template when you want to validate a new AI hypothesis within a bounded time period. The experiment produces objective evidence for the Gate Review decision: **Continue**, **Pivot** or **Stop**.

______________________________________________________________________

## 1. Hypothesis & Assumptions

- **Hypothesis name:** \[Short, recognisable name\]
- **Description:** \[What do you expect the model/system will achieve? Formulate as: "We expect that \[intervention\] will lead to \[measurable outcome\] for \[target group\]."\]
- **Rationale:** \[Why do you expect this outcome? Reference prior data, literature or stakeholder insights.\]

### Riskiest Assumption Test (RAT)

*Which assumption underlying this hypothesis carries the most risk? Test this one first — not the easiest, but the one that makes the experiment pointless if it turns out to be wrong.*

- **Riskiest assumption:** \[Describe the assumption that carries the most risk\]
- **Validation method:** \[How will we test this assumption as cheaply and quickly as possible? E.g. data analysis, interviews, concierge test, technical spike\]
- **Pass/fail criterion:** \[When is the assumption validated? When invalidated?\]
- **Owner:** \[Who will execute the test?\]

______________________________________________________________________

## 2. Time-box

- **Start date:** \[DD-MM-YYYY\]
- **End date:** \[DD-MM-YYYY\]
- **Duration:** \[Recommended: 1-2 sprints (2-4 weeks)\]
- **Mid-point checkpoint:** \[Date halfway through for go/no-go assessment\]

!!! warning "Do not exceed the time-box"
    If the experiment does not yield conclusive results by the agreed end date, activate the decision point (section 6). Extension without a formal decision is not permitted.

______________________________________________________________________

## 3. Team Allocation

| Role           | Name           | Availability (%) | Responsibility                                   |
| :------------- | :------------- | :--------------: | :----------------------------------------------- |
| AI PM          | \[Enter name\] |   \[e.g. 30%\]   | Scope management, stakeholder updates, decision  |
| Data Scientist | \[Enter name\] |   \[e.g. 60%\]   | Model development, measurements, analysis        |
| Tech Lead      | \[Enter name\] |   \[e.g. 40%\]   | Architecture, integration, technical feasibility |

______________________________________________________________________

## 4. Success Criteria

Define measurable criteria aligned with the AI Project Blueprint Evidence Standards \[so-1\].

| Criterion           | Metric                                                                                        | Minimum threshold | Target value      |
| :------------------ | :-------------------------------------------------------------------------------------------- | :---------------- | :---------------- |
| Accuracy            | \[e.g. F1 score\]                                                                             | \[e.g. >= 0.80\]  | \[e.g. >= 0.90\]  |
| Latency             | \[e.g. p95 response time\] (95th percentile — 95% of all requests are faster than this value) | \[e.g. \< 2s\]    | \[e.g. \< 500ms\] |
| Cost per prediction | \[e.g. EUR/1000 calls\]                                                                       | \[e.g. \< EUR 5\] | \[e.g. \< EUR 2\] |
| User acceptance     | \[e.g. NPS or CSAT\]                                                                          | \[e.g. >= 7/10\]  | \[e.g. >= 8/10\]  |

- **Evidence level:** \[Reference to the required Evidence Level for this Gate\]
- **Golden Set available:** \[Yes/No — if No, include as deliverable in sprint 1\]

______________________________________________________________________

## 5. Fail Criteria

Define the boundaries at which the experiment is considered failed and the pivot/stop trigger is activated.

| Fail criterion                        | Threshold                   | Consequence    |
| :------------------------------------ | :-------------------------- | :------------- |
| Accuracy below minimum threshold      | \[e.g. F1 \< 0.70\]         | Stop or Pivot  |
| Hard Boundaries violated              | Any violation               | Immediate Stop |
| Costs exceed budget                   | \[e.g. > 150% of estimate\] | Pivot or Stop  |
| No measurable improvement vs baseline | After sprint 1              | Pivot          |

______________________________________________________________________

## 6. Decision Point

At the end of the time-box the team makes a formal decision based on collected data. This decision point is linked to the Gate structure.

| Decision     | Conditions                                                      | Follow-up action                                 |
| :----------- | :-------------------------------------------------------------- | :----------------------------------------------- |
| **Continue** | All success criteria met; no fail criteria triggered            | Proceed to next Gate; plan development sprint    |
| **Pivot**    | Partially successful; adjusting hypothesis offers better chance | New Experiment Ticket with adjusted hypothesis   |
| **Stop**     | Fail criteria triggered; no realistic path to success           | Document in Validation Report; archive learnings |

- **Decision:** \[Continue / Pivot / Stop\]
- **Justification:** \[Brief summary of the data supporting the decision\]
- **Decision maker:** \[AI PM name\]
- **Date:** \[DD-MM-YYYY\]

______________________________________________________________________

## 7. Budget

| Cost item             | Continue (est.) | Pivot (est.)  | Stop (est.)             |
| :-------------------- | :-------------- | :------------ | :---------------------- |
| Compute & API costs   | \[EUR\]         | \[EUR\]       | \[EUR wind-down\]       |
| Team hours (internal) | \[FTE hours\]   | \[FTE hours\] | \[FTE hours wind-down\] |
| Data acquisition      | \[EUR\]         | \[EUR\]       | N/A                     |
| Tooling & licences    | \[EUR\]         | \[EUR\]       | \[EUR wind-down\]       |
| **Total estimated**   | \[EUR\]         | \[EUR\]       | \[EUR\]                 |

______________________________________________________________________

## 8. Sprint Capacity Guideline

The allocation below provides a guideline for capacity planning during experiment sprints.

| Category                | Share |
| :---------------------- | :---- |
| Feature development     | 30%   |
| Experimentation         | 40%   |
| Maintenance / tech debt | 15%   |
| Buffer                  | 15%   |

*This allocation is indicative. Adjust based on project phase and team size.*

______________________________________________________________________

## 9. Results Documentation

- **Validation Report:** \[Link to completed Validation Report\]
- **Measurement results:** \[Link to dashboard or data export\]
- **Lessons learned:** \[Brief summary of key insights\]

______________________________________________________________________

**Next step:** Document the experiment results in the [Validation Report](../07-validatie-bewijs/validatierapport.md) and complete the [Gate Review Checklist](../15-guardian-review/template.md) for the formal decision moment.
