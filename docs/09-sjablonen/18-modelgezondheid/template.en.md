---
versie: '1.0'
---

# Monthly Model Health Review

This template provides a structured agenda for the monthly model health review with stakeholders. The goal is to provide regular transparency on the performance, risks and maintenance of AI systems in production.

!!! info "Participants"
    Invite at minimum the following roles: **AI PM** (facilitator), **Tech Lead**, **Data Scientist**, **Sponsor** and **Guardian**. Consider adding the **Adoption Manager** when user adoption is a point of attention.

______________________________________________________________________

## 1. Executive Summary (5 min)

| Field              | Value                                 |
| :----------------- | :------------------------------------ |
| **Model version**  | \[e.g. v2.3.1\]                       |
| **Review date**    | \[DD-MM-YYYY\]                        |
| **Primary metric** | \[e.g. F1 score: 0.91\]               |
| **Baseline**       | \[e.g. F1 score: 0.88 at deployment\] |
| **Trend**          | \[Rising / Stable / Declining\]       |
| **Status**         | \[Green / Yellow / Orange / Red\]     |

**Status definitions** (aligned with Drift Detection alert levels):

- **Green:** All metrics within thresholds; no action required.
- **Yellow:** Minor deviation detected; increased monitoring active.
- **Orange:** Significant performance degradation; retraining being scheduled.
- **Red:** Hard Boundaries exceeded; immediate intervention required.

______________________________________________________________________

## 2. Key Metrics Dashboard (10 min)

| Metric               | Previous month | Current month | Trend   | Threshold   |
| :------------------- | :------------- | :------------ | :------ | :---------- |
| Accuracy (primary)   | \[Value\]      | \[Value\]     | \[+/-\] | \[Minimum\] |
| Volume (predictions) | \[Count\]      | \[Count\]     | \[+/-\] | N/A         |
| Cost per prediction  | \[EUR\]        | \[EUR\]       | \[+/-\] | \[Maximum\] |
| Latency (p95)        | \[ms\]         | \[ms\]        | \[+/-\] | \[Maximum\] |
| Hallucination rate   | \[%\]          | \[%\]         | \[+/-\] | \[Maximum\] |

**Explanation of deviations:** \[Summarise deviations here and reference root cause analysis if available.\]

______________________________________________________________________

## 3. Business Impact (5 min)

| Indicator                | Previous month | Current month | Trend   |
| :----------------------- | :------------- | :------------ | :------ |
| Transactions processed   | \[Count\]      | \[Count\]     | \[+/-\] |
| Estimated revenue impact | \[EUR\]        | \[EUR\]       | \[+/-\] |
| User satisfaction        | \[Score\]      | \[Score\]     | \[+/-\] |
| Adoption rate            | \[%\]          | \[%\]         | \[+/-\] |

______________________________________________________________________

## 4. Upcoming Maintenance (5 min)

| Maintenance activity  | Planned date | Responsible | Status                       |
| :-------------------- | :----------- | :---------- | :--------------------------- |
| Model retraining      | \[Date\]     | \[Name\]    | \[Planned/In progress/Done\] |
| Data quality check    | \[Date\]     | \[Name\]    | \[Planned/In progress/Done\] |
| Infrastructure update | \[Date\]     | \[Name\]    | \[Planned/In progress/Done\] |
| Golden Set refresh    | \[Date\]     | \[Name\]    | \[Planned/In progress/Done\] |

**Data quality trends:** \[Describe trends in data integrity, volume changes, new data sources.\]

______________________________________________________________________

## 5. Q&A & Decisions (30 min)

Use this time for open discussion with stakeholders.

**Agenda items:**

1. \[Item 1\]
1. \[Item 2\]
1. \[Item 3\]

**Decisions taken:**

| Decision        | Owner    | Deadline |
| :-------------- | :------- | :------- |
| \[Description\] | \[Name\] | \[Date\] |

______________________________________________________________________

## 6. Action Items & Next Review

| Action item  | Owner    | Deadline | Status   |
| :----------- | :------- | :------- | :------- |
| \[Action 1\] | \[Name\] | \[Date\] | \[Open\] |
| \[Action 2\] | \[Name\] | \[Date\] | \[Open\] |

- **Next review scheduled for:** \[DD-MM-YYYY\]
- **Facilitator next session:** \[AI PM name\]

______________________________________________________________________

## 7. Communication Scripts

Use the scripts below as guidance when communicating sensitive topics to stakeholders. Avoid jargon and emphasise concrete actions.

| Scenario                                       | Don't say                                               | Do say                                                                                                                                                           |
| :--------------------------------------------- | :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model needs retraining                         | "The model is outdated and no longer works properly."   | "Performance shows a declining trend. We are scheduling retraining on \[date\] to restore accuracy."                                                             |
| Accuracy lower than expected                   | "The model is making too many mistakes."                | "Accuracy is currently at \[X%\], below our threshold of \[Y%\]. We are investigating the cause and will present an action plan at the next review."             |
| Model accurate but stakeholders don't trust it | "The numbers prove it works well, you should trust it." | "We understand your concern. Let us review some edge cases together so you can see how the model reaches its decisions."                                         |
| Experiment failed                              | "The experiment has failed."                            | "The validation pilot has shown that this approach does not meet the success criteria. We have gained valuable insights that we will carry into the next phase." |

!!! info "Terminology"
    Within the AI Project Blueprint, use the following terms: **performance degradation** (not "model drift"), **validation pilot** (not "proof of value"), **hard boundaries** (not "guardrails"), **deployment** (not "go-live" in technical documentation).

______________________________________________________________________

**Next step:** Consult the [Drift Detection module](../../05-beheer-optimalisatie/05-drift-detectie.md) for detailed monitoring guidelines and the [Metrics & Dashboards overview](../../05-beheer-optimalisatie/03-afleveringen.md) for KPI configuration.
