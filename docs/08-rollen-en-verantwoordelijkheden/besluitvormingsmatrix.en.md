---
versie: '1.1'
description: 'Decision matrix: who decides what at each gate, who has veto rights, and who is informed — clear authority structure for AI projects.'
type: template
layer: 1
tags: [governance, template]
---

# Decision Matrix

## Purpose

This document makes explicit who takes which decision at each gate and who can block a decision. Ambiguity about decision authority is one of the most common causes of delayed AI projects.

**Core rule:**

- **Sponsor** bears final responsibility for all go/no-go decisions.
- **Guardian** has stop right over any decision that crosses a Red Line.
- **Tech Lead** signs off on technical feasibility — no go without their approval.
- **AI PM** coordinates and informs, but does not decide unilaterally.

______________________________________________________________________

## Decision matrix per gate

| Decision                                          | Accountable         | Responsible       | Veto right             | Consult                   | Inform                                             |
| :------------------------------------------------ | :------------------ | :---------------- | :--------------------- | :------------------------ | :------------------------------------------------- |
| **Go/No-Go Gate 1** (problem def. & feasibility)  | Sponsor             | AI PM             | Guardian (Red Lines)   | Tech Lead, Guardian       | Steering committee, Finance                        |
| **Go/No-Go Gate 2** (investment decision PoV)     | Sponsor             | AI PM + Finance   | Guardian (Red Lines)   | Tech Lead, Guardian       | Steering committee, Legal                          |
| **Go/No-Go Gate 3** (production go/no-go)         | Sponsor + Tech Lead | Tech Lead + AI PM | Guardian (Red Lines)   | Legal, Privacy Officer    | Steering committee, Ops                            |
| **Go/No-Go Gate 4** (quarterly operations review) | Sponsor             | AI PM + Ops       | Guardian (Red Lines)   | Tech Lead                 | Finance, Steering committee                        |
| **Stop decision** (circuit breaker activation)    | Guardian            | Tech Lead         | —                      | AI PM, Sponsor            | Steering committee, Legal                          |
| **Mode change** (raising Collaboration Mode)      | Sponsor             | AI PM + Tech Lead | Guardian (Red Lines)   | Guardian, Legal           | Steering committee                                 |
| **Technical feasibility**                         | Tech Lead           | Tech Lead         | —                      | AI PM                     | Sponsor, Guardian                                  |
| **Adjusting Red Lines**                           | Guardian + Sponsor  | Guardian          | Sponsor (scope), Legal | AI PM, Tech Lead, Legal   | Steering committee                                 |
| **Replace or fine-tune model**                    | Tech Lead           | Tech Lead + AI PM | Guardian (quality)     | Guardian, Privacy Officer | Sponsor, Ops                                       |
| **Incident escalation** (High Risk systems)       | Guardian            | AI PM             | —                      | Legal, Tech Lead          | Sponsor, Steering committee, Supervisory authority |

______________________________________________________________________

## Role description

### Sponsor

Bears final responsibility for all strategic go/no-go decisions. Has the mandate to authorise investments and stop projects. Is the only party who can sign off Gate 1, 2 or 3.

### Guardian

Has **stop right** over any decision that crosses a Red Line or where the ethical or compliance assessment is negative. This stop right supersedes the Sponsor on compliance matters. The Guardian also initiates the circuit breaker for Mode 4 and 5 systems.

### Tech Lead

Signs off on the technical feasibility of each gate. No production go without explicit technical approval. Responsible for architectural decisions and the quality of the Validation report.

### AI PM

Coordinates the decision-making process, prepares gate documentation and informs all stakeholders. Is Responsible for execution but not Accountable for the outcome of strategic decisions.

______________________________________________________________________

## Escalation procedure in case of conflict

If the Sponsor and the Guardian disagree:

1. Guardian documents the objection in writing in the Gate Review Checklist.
1. A cooling-off period of 48 hours — no decision in the interim.
1. External mediation by an independent AI ethics adviser (mandatory for High Risk systems).
1. In case of persistent conflict: the Sponsor may overrule the Guardian but personally takes over compliance responsibility, documented in the project file.

!!! danger "Never bypass"
    The Guardian may not be bypassed due to time pressure or commercial urgency. An overrule by the Sponsor on a High Risk system is reported to the steering committee and, where applicable, to the relevant supervisory authority.

______________________________________________________________________

**Related modules:**

- [Roles & Responsibilities](index.md)
- [Gate Reviews Checklist](../09-sjablonen/08-traceerbaarheid-links/template.md)
- [Compliance Hub](../07-compliance-hub/index.md)

______________________________________________________________________

**Version:** 1.0
**Date:** 13 March 2026
**Status:** Final
