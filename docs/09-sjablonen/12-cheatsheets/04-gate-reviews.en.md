---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [AI Product Manager]
tags: [gate-review, quick-reference]
---

# Cheatsheet — Gate Reviews

**Source:** [Gate Reviews Checklist](../04-gate-reviews/checklist.md)

______________________________________________________________________

## Overview 5 Gates

| Gate       | After phase      | Core question                                | Minimum deliverables                               |
| :--------- | :--------------- | :------------------------------------------- | :------------------------------------------------- |
| **Gate 1** | Discovery        | Is the use case feasible and worth pursuing? | Project Charter, Risk Pre-Scan, Collaboration mode |
| **Gate 2** | Validation (PoV) | Has it been proven to work on real data?     | Golden Set results, PoV report, Go/No-Go           |
| **Gate 3** | Development      | Is the system production-ready?              | AI Safety Checklist, Red Teaming, Model Card       |
| **Gate 4** | Delivery         | Is the handover complete?                    | Handover checklist, SLA, monitoring plan           |
| **Gate 5** | Closure          | Have the benefits been realised?             | Lessons Learned, benefits report                   |

______________________________________________________________________

## Decision Options

| Decision           | Meaning                           | Required action                            |
| :----------------- | :-------------------------------- | :----------------------------------------- |
| **Go**             | Phase succeeded, start next phase | Document, start next sprint                |
| **Conditional Go** | Proceed with open items           | List + owner + deadline established        |
| **No-Go**          | Phase failed                      | Root cause, recovery plan, reschedule gate |
| **Stop**           | Terminate project                 | Closure report + lessons learned           |

______________________________________________________________________

## Required Attendees

| Role      | Gate 1 | Gate 2 | Gate 3    | Gate 4 | Gate 5 |
| :-------- | :----- | :----- | :-------- | :----- | :----- |
| AI PM     | ✓      | ✓      | ✓         | ✓      | ✓      |
| Guardian  | ✓      | ✓      | ✓         | ✓      | ✓      |
| Tech Lead | ✓      | ✓      | ✓         | ✓      | —      |
| Sponsor   | ✓      | —      | —         | ✓      | ✓      |
| CAIO      | —      | —      | High Risk | —      | —      |

______________________________________________________________________

## Red Flags per Gate

- **Gate 1:** No measurable success criteria → No-Go
- **Gate 2:** Golden Set score below threshold → No-Go
- **Gate 3:** Critical Red Teaming finding still open → block go-live
- **Gate 4:** Monitoring plan missing → Conditional Go at most
- **Gate 5:** Benefits not measured → Lessons Learned mandatory

**Source for full approach:** [Gate Reviews Checklist](../04-gate-reviews/checklist.md)
