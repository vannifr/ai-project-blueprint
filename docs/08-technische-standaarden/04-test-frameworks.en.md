---
versie: '1.1'
type: technical
layer: 3
roles: [Tech Lead]
summary: Testing approach for AI systems that combines deterministic tests with evaluation of probabilistic behaviour.
answers: [What are the technical standards for Test Frameworks?]
---

# 1. Test Frameworks

!!! abstract "Purpose"
    Testing approach for AI systems that combines deterministic tests with evaluation of probabilistic behaviour.

## 1. Purpose

This module defines how we test AI systems. Unlike traditional software, AI requires a combination of deterministic tests and evaluation of probabilistic behaviour.

______________________________________________________________________

## 2. Test Levels

### Component Tests (Unit Tests)

Testing individual components in isolation.

**What we test:**

- Data transformation functions (input → expected output)
- Prompt parsing and formatting
- API integration code (with mocks)
- Error handling (edge cases)

**Characteristics:**

- Fast to execute (seconds)
- Deterministic (same input = same result)
- Automatic at every code change

### Integration Tests

Testing the cooperation between components.

**What we test:**

- End-to-end flow from input to output
- Integration with external systems (databases, APIs)
- Data validation in the full pipeline

**Characteristics:**

- Slower than unit tests (minutes)
- May require external dependencies
- Periodic or at important changes

### AI Behaviour Tests (Golden Set)

Testing AI behaviour on representative scenarios.

**What we test:**

- Factuality and relevance of answers
- Compliance with Hard Boundaries
- Consistency over multiple runs
- Performance per user group (fairness)

**Characteristics:**

- Requires human assessment or automated evaluation
- Variation possible due to probabilistic nature
- Mandatory for every Gate Review

______________________________________________________________________

## 3. The Golden Set

The Golden Set is the central test set for AI behaviour. See [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md) for minimum requirements per risk level.

### Composition

| Category          | Description                                    | Minimum % |
| ----------------- | ---------------------------------------------- | --------: |
| Standard cases    | Typical, realistic scenarios                   |    70-80% |
| Complex cases     | Edge cases, multi-step questions               |    15-20% |
| Adversarial cases | Jailbreaks, prompt injection, policy bypassing |     5-10% |
| Fairness cases    | Scenarios per relevant user group              | As needed |

### Format per Test Case

| Field             | Description                                 |
| ----------------- | ------------------------------------------- |
| ID                | Unique identification (e.g. GS-001)         |
| Category          | Standard / Complex / Adversarial / Fairness |
| Input             | The exact prompt or question                |
| Expected outcome  | Correct answer or assessment criteria       |
| Assessment method | Exact match / Keywords / Human assessment   |
| Critical?         | Yes/No (Critical error if incorrect?)       |

### Maintenance

- Golden Set is periodically reviewed (minimum per release)
- New scenarios are added at incidents or new functionality
- Outdated cases are removed or updated

______________________________________________________________________

## 4. Adversarial Testing

Specific tests to validate safety and robustness.

### Required Adversarial Scenarios

| Scenario                          | Description                                                               | Expected Behaviour                                  |
| --------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------- |
| Jailbreak                         | Attempt to ignore instructions                                            | Refusal                                             |
| Prompt injection                  | Hidden instructions in user input                                         | Ignore instruction                                  |
| Policy bypass                     | Cleverly circumventing Hard Boundaries                                    | Refusal                                             |
| Source fabrication                | "Make up a source" or "pretend"                                           | Refusal                                             |
| PII extraction                    | Attempt to retrieve training data                                         | Refusal                                             |
| Tool abuse / privilege escalation | Attempt to obtain higher rights or perform unauthorised actions via tools | Refusal + logging                                   |
| Data exfiltration via tool output | Attempt to extract sensitive data via tool responses or artefacts         | Blocking + alert                                    |
| Retrieval poisoning               | Injection of malicious sources into knowledge base to manipulate output   | Detection (monitoring) + blocking/refusal + logging |
| Action injection                  | Manipulation of tool schemas to trigger unintended actions                | Schema validation + refusal                         |

Sources: \[so-1\], \[so-10\]

### Execution

- **Minimal Risk:** Qualitative sampling by Guardian
- **Limited Risk:** Structured adversarial set (minimum 5% of Golden Set)
- **High Risk:** Extended adversarial testing + external red team where relevant

______________________________________________________________________

## 5. Regression Testing

Automatically repeating tests at changes to detect degradation.

### What Triggers Regression Tests?

| Change               | Regression test level                 |
| -------------------- | ------------------------------------- |
| Code change          | Component tests + Integration tests   |
| Prompt change        | Integration tests + Golden Set sample |
| Model version update | Full Golden Set                       |
| Data source change   | Full Golden Set + Fairness            |

### Automation

| Level | Approach                              | Tooling examples          |
| ----- | ------------------------------------- | ------------------------- |
| L0    | Manual execution at release           | Spreadsheet tracking      |
| L1    | Scheduled periodic tests              | Cron jobs, CI scheduled   |
| L2    | Automatic at every commit             | GitHub Actions, GitLab CI |
| L3    | Continuous testing with quality gates | MLflow, custom pipelines  |

______________________________________________________________________

## 6. Evaluation Metrics

| Metric       | Application               | Calculation                    |
| ------------ | ------------------------- | ------------------------------ |
| Factuality   | Factual correctness       | % correct / total              |
| Relevance    | Answer fits question      | Average score (1-5 scale)      |
| Consistency  | Stability over runs       | Standard deviation over N runs |
| Refusal rate | Adversarial scenarios     | % correctly refused            |
| Fairness     | Difference between groups | Max difference in error rate   |

______________________________________________________________________

## 7. Test Framework Checklist

!!! check "7. Test Framework Checklist"
    - [ ] Component tests cover critical functions
    - [ ] Integration tests validate end-to-end flow
    - [ ] Golden Set is composed according to [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
    - [ ] Adversarial scenarios are defined and tested
    - [ ] Regression test strategy is documented
    - [ ] Evaluation metrics are defined
    - [ ] Test results are recorded in [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)

______________________________________________________________________

## 8. Related Modules

- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Golden Set Test Template](../09-sjablonen/07-validatie-bewijs/template.md)
