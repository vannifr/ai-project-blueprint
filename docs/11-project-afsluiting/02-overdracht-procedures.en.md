---
versie: '1.0'
type: guide
layer: 2
phase: [5]
---

# 2. Handover Procedures

## 1. Objective

We formally and structurally hand over the AI system to the management organisation so that continuity, compliance and quality are guaranteed after project closure.

______________________________________________________________________

## 2. Entry Criteria

- Gate 3 (Production-Ready) has been approved.
- The management team has been designated and is available for training.
- The Handover Checklist has been prepared. → [Handover Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)

______________________________________________________________________

## 3. Core Activities

### Drawing Up the Handover Plan

At least two weeks before Gate 4, the AI PM draws up a handover plan with:

- **Scope:** Which systems, data sources and processes are being handed over?
- **Timeline:** When are which components handed over?
- **Acceptance criteria:** When does the management organisation consider the handover successful?
- **Points of contact:** Who is the first point of contact after handover?

### Technical Handover

The Tech Lead organises the technical handover in three steps:

1. **Documentation review:** Technical Model Card, runbook and infrastructure documentation are reviewed together with the administrator.
1. **Hands-on session:** The administrator independently performs the most important management tasks (restart, scaling, viewing monitoring) under the guidance of the Tech Lead.
1. **Shadow period:** The administrator runs the system independently for at least 5 working days while the project team is still available for questions.

### Guardian Handover

The handover of the Guardian role requires a separate procedure:

1. New Guardian is designated by the management organisation.
1. Joint session: current Guardian + new Guardian review the Hard Boundaries.
1. Written transfer of the compliance dossier.
1. New Guardian signs acceptance of the Guardian responsibilities.

### Formal Acceptance

The handover is only complete when:

- The Handover Checklist is fully ticked off.
- Both project team and management organisation have signed the handover form.
- Gate 4 (Go-Live) has been approved by the Guardian.

______________________________________________________________________

## 4. Team & Roles

| Role                          | Responsibility                                    | R/A/C/I |
| :---------------------------- | :------------------------------------------------ | :------ |
| AI Product Manager            | Coordinates the full handover process             | A       |
| Tech Lead                     | Performs technical handover and hands-on sessions | R       |
| Guardian (project)            | Hands over compliance dossier and Hard Boundaries | R       |
| Guardian (management)         | Accepts Guardian role and compliance dossier      | R       |
| Management organisation owner | Signs formal acceptance                           | A       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Handover Checklist is fully ticked off and signed.
- [ ] Shadow period of at least 5 working days is completed.
- [ ] Guardian handover has been formally confirmed.
- [ ] Gate 4 has been approved.
- [ ] Project team officially has no more operational responsibility.

______________________________________________________________________

## 6. Deliverables

| Deliverable                    | Description                                       | Owner     |
| :----------------------------- | :------------------------------------------------ | :-------- |
| Handover Plan                  | Timeline, scope and acceptance criteria           | AI PM     |
| Handover Checklist (completed) | Fully ticked checklist with signatures            | AI PM     |
| Handover Form                  | Formal document with signatures from both parties | AI PM     |
| Runbook                        | Step-by-step guide for the administrator          | Tech Lead |

______________________________________________________________________

**Related modules:**

- [Project Closure — Overview](index.md)
- [Handover Checklist Template](../05-fase-levering/04-sjablonen/overdracht-checklist.md)
- [Gate Reviews Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
- [Lessons Learned](01-lessons-learned.md)
- [Benefits Realisation](03-batenrealisatie.md)

______________________________________________________________________

**Next step:** [Measure definitive benefits via Benefits Realisation](03-batenrealisatie.md)
→ See also: [Handover Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)
