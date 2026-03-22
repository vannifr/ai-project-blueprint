---
versie: '1.0'
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference]
answers: [What is the quick reference for Cheatsheet — AI Collaboration Modes?]
---

# Cheatsheet — AI Collaboration Modes

**Source:** [Collaboration Modes](../../00-strategisch-kader/06-has-h-niveaus.md)

______________________________________________________________________

## The 5 Modes

| Mode  | Name                        | Who decides            | Typical application                  |
| :---- | :-------------------------- | :--------------------- | :----------------------------------- |
| **1** | Human only                  | Human                  | Creative or ethical judgements       |
| **2** | AI advises                  | Human (after AI input) | Analyses, summaries, options         |
| **3** | AI proposes, human approves | Human (final click)    | Document generation, emails, reports |
| **4** | AI acts, human monitors     | AI (human intervenes)  | Automated processing, routine tasks  |
| **5** | AI fully autonomous         | AI                     | Fully automated pipelines            |

______________________________________________________________________

## When to Use Which Level?

```
Question 1: What are the consequences if the AI is wrong?
  → Large / irreversible?  → Mode 1 or 2
  → Small / recoverable?   → Mode 3, 4 or 5

Question 2: Is the task standardised and repetitive?
  → No   → Mode 1 or 2
  → Yes  → Consider Mode 3 or 4

Question 3: Is it a High Risk system (EU AI Act)?
  → Yes  → Mode 1, 2 or 3 (human oversight mandatory)
  → No   → Mode 4 or 5 possible
```

______________________________________________________________________

## Escalation Rules

| Situation                    | Action                                   |
| :--------------------------- | :--------------------------------------- |
| Unexpected output            | Switch back to lower mode                |
| Quality degradation detected | Review mode; consider human intervention |
| New use outside scope        | Reassess mode; document in charter       |
| Complaint or incident        | At least Mode 3 until cause identified   |

______________________________________________________________________

## Governance Requirements per Mode

| Mode | Logging                 | Human review       | Guardian sign-off          |
| :--- | :---------------------- | :----------------- | :------------------------- |
| 1–2  | Recommended             | Per decision       | Not required               |
| 3    | Mandatory               | Sample (10%)       | At implementation          |
| 4    | Mandatory               | Alert-based        | Required                   |
| 5    | Mandatory + audit trail | Periodic (monthly) | Required + recertification |

**Source:** [Collaboration Modes](../../00-strategisch-kader/06-has-h-niveaus.md) | [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md)
