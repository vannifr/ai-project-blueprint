---
versie: '1.1'
type: foundation
layer: 1
roles: [Data Scientist]
tags: [governance, validation]
summary: Description of the three validation dimensions (syntactic, behavioural, goal-oriented) that every change to prompts or RAG must pass through.
answers: [What does Validation Model entail?, How much validation is sufficient?]
---

# 1. Validation Model

!!! abstract "Purpose"
    Description of the three validation dimensions (syntactic, behavioural, goal-oriented) that every change to prompts or RAG must pass through.

## 1. Three Dimensions of Validation

Every change to **Steering Instructions** or knowledge coupling must pass through three validation categories:

### Syntactic Validity

- **Question:** Does the code work? No crashes or errors?
- **Method:** Automated checks on structure, structured schemas (such as JSON, YAML) and linting.

### Behavioural Conformance

- **Question:** Does the system do what we expect under controlled conditions?
- **Method:** Automated evaluation suites that are reproducible (test sets).

### Goal Alignment (Intent-Alignment)

- **Question:** Does the system genuinely help the user in practice?
- **Method:** Scenario-based evaluation by experts or advanced simulation.

______________________________________________________________________

## 2. Validation Depth per Risk Level

Not every change requires the same validation effort. The required depth is linked to the [risk level](05-risicoclassificatie.md) of the change. The table below describes what each validation level looks like in practice.

### Level 1 — Minimal Validation (Low Risk)

**When:** Cosmetic changes, minor prompt adjustments that do not affect Hard Boundaries, textual corrections.

| Dimension      | What to do                                   | Example                                                                        |
| :------------- | :------------------------------------------- | :----------------------------------------------------------------------------- |
| Syntactic      | Run automated linting and schema validation  | CI pipeline verifies that JSON output schema remains valid after prompt change |
| Behavioural    | Run existing regression test set (automated) | 20 standard test cases are automatically validated; all must pass              |
| Goal Alignment | Not required                                 | —                                                                              |

**Lead time:** minutes (fully automated).

**Evidence:** CI/CD pipeline report with green status.

### Level 2 — Standard Validation (Medium Risk)

**When:** Changes to system prompts, adding new knowledge sources to RAG, adjusting retrieval logic, new use case within an existing system.

| Dimension      | What to do                                                       | Example                                                                                   |
| :------------- | :--------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| Syntactic      | Automated linting + schema validation + output format check      | Validate that the API response structure remains intact after RAG change                  |
| Behavioural    | Golden Set evaluation (minimum 50 cases) + regression test       | Compare scores before and after change; maximum 5% regression on existing metrics allowed |
| Goal Alignment | Spot check by domain expert (minimum 10 cases manually reviewed) | Expert assesses whether answers in the business context are still correct and usable      |

**Lead time:** 1-2 days.

**Evidence:** Golden Set report + expert sign-off.

### Level 3 — Deep Validation (High Risk)

**When:** Changes that affect Hard Boundaries, new model or model version, system that makes external decisions, personal data in scope, high-risk classification under EU AI Act.

| Dimension      | What to do                                                                        | Example                                                                                     |
| :------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Syntactic      | Full automated suite + contract testing between components                        | Validate that all upstream/downstream systems communicate correctly after model switch      |
| Behavioural    | Full Golden Set (100+ cases) + adversarial test set + bias analysis + Red Teaming | Red Team attempts to manipulate the system via prompt injection, jailbreaks, and edge cases |
| Goal Alignment | Scenario evaluation by multiple domain experts + end-user test + Guardian review  | Minimum 3 experts assess independently; end users evaluate in realistic scenarios           |

**Lead time:** 1-2 weeks.

**Evidence:** Full [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md) + Red Teaming report + Guardian sign-off + expert assessments.

______________________________________________________________________

## 3. Validation in Practice

### Rules of Thumb

1. **Always start with Level 1.** Every change goes through at minimum the automated checks. If those fail, do not proceed.
1. **The Guardian determines the level.** When in doubt about the required level, the Guardian decides. Better one level too high than too low.
1. **No validation, no deployment.** No change goes to production without the corresponding validation level being completed and documented.
1. **Never combine levels downward.** If a change affects multiple components, one of which is High Risk, then Level 3 applies to the entire change.

### Example: validation flow for a RAG update

```
1. Add new knowledge source to vector store
2. CI pipeline runs automatically (Level 1: schema + linting)       ✅
3. Golden Set evaluation runs (Level 2: 50 cases)                   ✅
4. Domain expert reviews 10 sample cases                            ✅
5. No Hard Boundaries affected → Level 2 suffices
6. Result: deployment approved with Golden Set report + expert sign-off
```

______________________________________________________________________

## 4. Related Modules

- [Risk Classification](05-risicoclassificatie.md)
- [Evidence Standards](07-bewijsstandaarden.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
- [SDD Pattern](../04-fase-ontwikkeling/05-sdd-patroon.md)
- [Validation Report template](../09-sjablonen/07-validatie-bewijs/validatierapport.md)

______________________________________________________________________
