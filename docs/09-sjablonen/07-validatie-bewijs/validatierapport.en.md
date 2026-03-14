---
versie: '1.0'
type: template
layer: 3
phase: [2, 3]
roles: [Data Scientist]
tags: [template, validation]
---

# 1. Template 09.06: Validation Report (Evidence Package)

## 1. Summary (1 page)

**Project:** \[Name\]
**Risk Level:** \[Minimal / Limited / High\]
**Collaboration Mode:** \[1–5\]
**Release/Build:** \[e.g. RC-1\]
**Test period:** \[YYYY-MM-DD to YYYY-MM-DD\]

### Conclusion (choose one)

!!! check "Conclusion (choose one)"
    - [ ] **Go** — meets Evidence Standards norms for this risk level
    - [ ] **Go with actions** — only after completing actions under §7
    - [ ] **No-Go** — does not meet; redesign/retrain/reformulate required

**Top 3 findings:**

1. ...
1. ...
1. ...

______________________________________________________________________

## 2. Scope & references (traceability)

**Objective Card version:** \[link/ID\]
**Hard Boundaries version:** \[link/ID\]
**System Prompts version:** \[link/ID\]
**Model Card version:** \[link/ID\]
**Test protocol version (Golden Set Test):** \[link/ID\]
**Risk Pre-Scan:** \[link/ID\]

______________________________________________________________________

## 3. Test Setup

- **Environment:** \[Dev/Test/Prod-simulation\]
- **Model settings:** \[e.g. temperature, max tokens\]
- **Knowledge Coupling:** \[Yes/No\] — if yes: which source set + update frequency
- **Preconditions:** \[e.g. rate limits, timeouts, tooling\]

______________________________________________________________________

## 4. Test Sets (Golden Set + supplements)

### Golden Set

- **Number of cases:** \[minimum according to Evidence Standards\]
- **Origin:** \[tickets, emails, calls, forms...\]
- **Coverage:** \[80/15/5 or 70/20/10 depending on risk level\]

### Adversarial set (required for Limited/High)

- **Number of adversarial prompts:** \[#\]
- **Types:** jailbreak / prompt injection / data leak / source fabrication

### Fairness set (required for High)

- **Approach:** \[quantitative / qualitative + motivation\]
- **Groups/segments:** \[describe without sensitive details\]

______________________________________________________________________

## 5. Results vs Evidence Standards

| Criterion                    |         Norm | Measured | Pass/Fail             | Note |
| ---------------------------- | -----------: | -------: | --------------------- | ---- |
| Critical errors              |            0 |    \[#\] | \[ \] Pass \[ \] Fail |      |
| Major errors (max)           |        \[#\] |    \[#\] | \[ \] Pass \[ \] Fail |      |
| Factuality                   |     \[≥..%\] |  \[..%\] | \[ \] Pass \[ \] Fail |      |
| Relevance (1–5)              |      \[≥..\] |   \[..\] | \[ \] Pass \[ \] Fail |      |
| Safety (refusal)             |         100% |  \[..%\] | \[ \] Pass \[ \] Fail |      |
| Transparency (if applicable) |         100% |  \[..%\] | \[ \] Pass \[ \] Fail |      |
| Fairness (bias)              |     \[≤..%\] |  \[..%\] | \[ \] Pass \[ \] Fail |      |
| Audit trail                  | per standard |   \[..\] | \[ \] Pass \[ \] Fail |      |

______________________________________________________________________

## 6. Error Overview (mandatory)

### Critical errors (0 permitted)

| Case-ID | Description | Impact | Cause | Fix | Status |
| ------- | ----------- | ------ | ----- | --- | ------ |

### Major errors

| Case-ID | Description | Impact | Cause | Fix | Status |
| ------- | ----------- | ------ | ----- | --- | ------ |

### Recurring patterns (failure modes)

- \[e.g. source attribution incorrect for document type X\]
- \[e.g. overly creative tone on short prompts\]

______________________________________________________________________

## 7. Logging & Audit Trail (evidence that we can trace back)

- **What we log:** \[according to Evidence Standards §7\]
- **Where it is stored:** \[tool + location\]
- **Retention:** \[90 days / 12 months / other\]
- **Privacy measures:** \[hashing/pseudonymisation/redaction\]

______________________________________________________________________

## 8. Action Plan (complete only if "Go with actions" or "No-Go")

| Action | Owner | Deadline | Expected effect | Verification (test) |
| ------ | ----- | -------- | --------------- | ------------------- |
|        |       |          |                 |                     |

______________________________________________________________________

## 9. Go/No-Go Sign-off

**Tech Lead:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **AI Product Manager:** \_\_\_\_\_\_\_\_\_ **Guardian:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
