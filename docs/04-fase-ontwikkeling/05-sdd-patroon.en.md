---
versie: '1.1'
---

# 1. Specification-First Pattern (SDD)

## 1. Objective

The Specification-First Pattern (Specification-Driven Development) is a working method in which we formally record what the AI system must do before we start building. This prevents costly corrections afterwards and ensures demonstrable compliance.

______________________________________________________________________

## 2. Core Principle: Specification Before Implementation

```
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Goal Definition │ --> │ Specification   │ --> │ Implementation  │
│ (Intent)        │     │ (Contract)      │     │ (Code/Prompts)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                       │                       │
         v                       v                       v
 What do we want?    How does it behave    How do we build it?
                          exactly?
```

**The difference from traditional development:**

| Traditional                  | Specification-First                           |
| ---------------------------- | --------------------------------------------- |
| Build first, test later      | Specify first, build to spec                  |
| "It works!" = done           | "It meets the spec" = done                    |
| Specification often implicit | Specification explicit and version-controlled |
| Validation after the fact    | Validation upfront (shift-left)               |

______________________________________________________________________

## 3. The SDD Cycle

### Draft the Goal Definition

The **AI Product Manager** records the business intent in the [Goal Definition](../09-sjablonen/06-ai-native-artefacten/doelkaart.md).

**Minimum to record:**

- What is the objective? (Goal Definition)
- What must never happen? (Hard Boundaries)
- Who are the users?
- What is success? (Measurable criteria)

### Elaborate the Specification

The **Tech Lead** and **ML Engineer** translate the Goal Definition into a technical specification.

**Components of the specification:**

| Component               | Description                               | Example                          |
| ----------------------- | ----------------------------------------- | -------------------------------- |
| Input format            | What does the system receive?             | JSON with fields X, Y, Z         |
| Output format           | What does the system produce?             | Structured answer with sources   |
| Behaviour rules         | How does the system respond in scenarios? | For question about X, refer to Y |
| Constraints             | Technical limitations                     | Max 500 tokens, latency \< 2s    |
| Hard Boundaries (tech.) | Concrete implementation of constraints    | Filter on PII patterns           |

### Specification Review

The specification is reviewed before implementation starts.

**Review checklist:**

- [ ] Does the specification cover all scenarios from the Goal Definition?
- [ ] Are the Hard Boundaries concrete and implementable?
- [ ] Is the specification testable (can we derive a Golden Set from it)?
- [ ] Are edge cases described?
- [ ] Guardian approval on Hard Boundaries implementation?

### Derive the Golden Set

We derive the test cases from the specification.

**Per behaviour rule:**

- At least 1 positive test case (happy flow)
- At least 1 negative test case (what is not allowed?)
- Edge cases where relevant

### Implement Against the Specification

Only now do we start building:

- Draft Steering Instructions (prompts/configs)
- Integration with data sources
- Implementation of filters and hard boundaries

### Validate Against the Specification

We validate whether the implementation meets the specification:

- Execute the Golden Set
- Compare results with expectations
- Analyse and resolve deviations

______________________________________________________________________

## 4. Benefits of SDD

| Benefit                 | Explanation                                         |
| ----------------------- | --------------------------------------------------- |
| Early error detection   | Intent errors discovered before building            |
| Demonstrable compliance | Specification = evidence of intent                  |
| Efficient development   | Fewer iterations thanks to a clear contract         |
| Better collaboration    | Business and Tech speak the same language           |
| Testability             | Golden Set follows logically from the specification |

______________________________________________________________________

## 5. Practical Tips

### Start Small

Begin with the most important scenarios. Extend the specification iteratively.

### Specification Is a Living Document

Update the specification when requirements change. Old versions are retained for audit.

### Specification ≠ Documentation

The specification is not a user manual, but a contract for developers and testers.

### Integration with Gates

- **Gate 2:** Specification approved, Golden Set derived
- **Gate 3:** Implementation meets the specification

______________________________________________________________________

## 6. Example: Customer Service Chatbot

**Goal Definition (excerpt):**

> "Answer customer queries about products using information from our knowledge base."

**Specification (excerpt):**

| Scenario                   | Input                            | Expected Behaviour                     |
| -------------------------- | -------------------------------- | -------------------------------------- |
| Product information        | "What does product X cost?"      | Price from knowledge base, with source |
| Unknown product            | "What does product Y cost?"      | "I have no information about Y"        |
| Hard Boundary: medical     | "Should I take this?"            | Refusal + referral                     |
| Hard Boundary: competition | "Is your product better than Z?" | Neutral answer, no comparison          |

**Golden Set (derived):**

- GS-001: Query about price of product X → price + source
- GS-002: Query about unknown product → "no information"
- GS-003: Medical advice query → refusal
- GS-004: Competition comparison → neutral

______________________________________________________________________

## 7. Fallback & Failure Experience

Define how the system fails (*Graceful Degradation*). A "white screen" or a technical error is unacceptable.

| Scenario                                | Expected Behaviour                                                                                                      |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| No answer possible / Hallucination risk | "I do not have enough information about this in my knowledge base." + Referral to a human expert.                       |
| Service Down / API Error                | Message "The AI assistant is temporarily unavailable" + Showing an alternative route (e.g. phone number or search bar). |
| Hard Boundary triggered                 | Neutral refusal ("I cannot answer this question due to safety guidelines").                                             |

______________________________________________________________________

## 8. SDD Checklist

!!! check "8. SDD Checklist"
    - [ ] Goal Definition is drafted and approved
    - [ ] Specification is elaborated with input/output/behaviour rules
    - [ ] Specification is reviewed by Tech Lead and Guardian
    - [ ] Golden Set is derived from the specification
    - [ ] Implementation is validated against the specification
    - [ ] Deviations are documented and resolved

______________________________________________________________________

## 9. Related Modules

- [Goal Definition Template](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Test Frameworks](../08-technische-standaarden/04-test-frameworks.md)
- [Specification-First Method](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)

______________________________________________________________________

**Next step:** Apply the SDD pattern in your next sprint and document specifications in the [Project Journal](../09-sjablonen/13-project-dagboek/template.md)
→ See also: [Gate 3 Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
