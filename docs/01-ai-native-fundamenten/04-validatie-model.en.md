---
versie: '1.1'
type: foundation
layer: 1
roles: [Data Scientist]
tags: [governance, validation]
---

# 1. Validation Model

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

## 2. Related Modules

- [Risk Classification](05-risicoclassificatie.md)
- [Evidence Standards](07-bewijsstandaarden.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
- [SDD Pattern](../04-fase-ontwikkeling/05-sdd-patroon.md)

______________________________________________________________________
