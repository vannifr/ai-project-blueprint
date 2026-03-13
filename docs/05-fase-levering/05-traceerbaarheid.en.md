---
versie: '1.1'
---

# 1. Traceability

## 1. Objective

Traceability ensures that we can always explain why an AI system produced a particular output. This is essential for auditing, debugging, incident analysis and compliance with the EU AI Act.

______________________________________________________________________

## 2. The Traceability Pyramid

```
 ┌───────────────┐
 │ Goal          │  Why are we building this?
 │ Definition    │
 └───────┬───────┘
         │
 ┌───────v───────┐
 │ Specification │  How must it behave?
 │ (Contract)    │
 └───────┬───────┘
         │
 ┌───────v───────┐
 │ Steering      │  Which prompts/configs steer it?
 │ Instructions  │
 └───────┬───────┘
         │
 ┌───────v───────┐
 │ Golden Set    │  How have we tested?
 │ (Tests)       │
 └───────┬───────┘
         │
 ┌───────v───────┐
 │ Validation    │  What were the results?
 │ Report        │
 └───────────────┘
```

**Each layer must be traceable back to the layer above it.**

______________________________________________________________________

## 3. Traceability Matrix

The traceability matrix links requirements to implementation to tests.

### Structure

| Goal-ID | Goal Description       | Spec-ID | Specification                | Prompt version | Test-ID | Test Result |
| ------- | ---------------------- | ------- | ---------------------------- | -------------- | ------- | ----------- |
| D-001   | Answer product queries | S-001   | Answer with price and source | v2.3           | GS-001  | Pass        |
| D-002   | No medical advice      | S-002   | Refusal for medical queries  | v2.3           | GS-003  | Pass        |
| D-003   | Transparency           | S-003   | Show AI disclaimer           | v2.3           | GS-010  | Pass        |

### Minimum Fields

| Field             | Description                                  |
| ----------------- | -------------------------------------------- |
| Goal-ID           | Reference to Goal Definition item            |
| Goal Description  | Brief description of the objective           |
| Spec-ID           | Reference to specification item              |
| Specification     | How is the objective technically translated? |
| Prompt version    | Which version of Steering Instructions?      |
| Test-ID           | Reference to Golden Set test case            |
| Test Result       | Pass/Fail/N/A                                |
| Validation Report | Link to evidence                             |

______________________________________________________________________

## 4. Runtime Traceability (Logging)

In addition to documentation traceability, runtime logging is essential.

### What Do We Log?

Per interaction, at minimum (see [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)):

| Field                         | Example                                |
| ----------------------------- | -------------------------------------- |
| Timestamp                     | 2026-02-01T14:32:15Z                   |
| Request-ID                    | req-abc123                             |
| User/Session                  | user-456 (hashed if required)          |
| Model + version               | gpt-4-turbo / v2024-01                 |
| Steering Instructions version | prompts/v2.3                           |
| Input (query)                 | "What does product X cost?"            |
| Sources used                  | doc-789, doc-012                       |
| Output                        | "Product X costs €49.99 (source: ...)" |
| Latency                       | 1.2s                                   |
| Human override                | No                                     |

For systems that execute tasks autonomously, we additionally record which actions were taken, within which pre-established boundaries, and whether human intervention or approval took place.

### Logging per Risk Level

| Level   | Logging requirement                             |
| ------- | ----------------------------------------------- |
| Minimal | Metadata (timestamp, model, version, status)    |
| Limited | Metadata + sampling of input/output (e.g. 10%)  |
| High    | 100% input/output + source references + context |

### Retention

- **Minimal/Limited:** 90 days standard
- **High Risk:** 12 months or longer (depending on regulations)

______________________________________________________________________

## 5. Incident Analysis with Traceability

When an incident occurs, we follow the traceability chain back:

### Analysis Procedure

1. **Identify the output:** Which response caused the problem?
1. **Retrieve logging:** Request-ID, input, model, sources
1. **Check Steering Instructions:** Was the correct version active?
1. **Compare with specification:** Did the output comply with the spec?
1. **Check Golden Set:** Had we tested this scenario?
1. **Back to Goal Definition:** Was this behaviour intended or a gap?

### Root Cause Categories

| Category             | Description                           | Action                     |
| -------------------- | ------------------------------------- | -------------------------- |
| Spec Gap             | Scenario not specified                | Extend specification       |
| Implementation Bug   | Spec correct, implementation deviates | Fix code/prompt            |
| Test Gap             | Scenario not in Golden Set            | Add test case              |
| Unforeseen Behaviour | Probabilistic nature of AI            | Strengthen Hard Boundaries |

______________________________________________________________________

## 6. Traceability for Audit

### EU AI Act Requirements (High Risk)

- All decisions must be traceable
- Documentation must be available to supervisory authorities
- Changes to the system must be documented

### Audit-Ready Package

For each production release:

| Document              | Content                              |
| --------------------- | ------------------------------------ |
| Goal Definition       | Intent and Hard Boundaries           |
| Specification         | Behaviour contract                   |
| Steering Instructions | Prompts/configs (version-controlled) |
| Golden Set            | Test cases and expected results      |
| Validation Report     | Test results and conclusion          |
| Traceability Matrix   | Links between the above              |
| Change Log            | All changes since previous release   |

______________________________________________________________________

## 7. Tooling Suggestions

| Purpose               | Options                                   |
| --------------------- | ----------------------------------------- |
| Document traceability | Git (everything as code), your wiki or KB |
| Runtime logging       | CloudWatch, Datadog, ELK Stack, custom    |
| Traceability matrix   | Spreadsheet, Jira, dedicated tools        |
| Audit trail           | Immutable logging (append-only)           |

______________________________________________________________________

## 8. Traceability Checklist

!!! check "8. Traceability Checklist"
    - [ ] Traceability matrix is established
    - [ ] All Goal Definition items are linked to specifications
    - [ ] All specifications are linked to test cases
    - [ ] Runtime logging is set up in line with the risk level
    - [ ] Logging meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
    - [ ] Retention is aligned with privacy policy
    - [ ] Audit-ready package is complete

______________________________________________________________________

## 9. Related Modules

- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Traceability Template](../09-sjablonen/08-traceerbaarheid-links/template.md)
- [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Incident Response](../07-compliance-hub/05-incidentrespons.md)
