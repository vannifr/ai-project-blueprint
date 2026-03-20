---
versie: '1.0'
type: index
layer: 2
phase: [3]
summary: Build a robust, production-ready AI solution that meets quality and safety requirements.
answers: [What does Phase 3 — Development contain?]
---

# 3. Development

!!! abstract "Purpose"
    Build a robust, production-ready AI solution that meets quality and safety requirements.

## 1. Purpose

After the validation pilot, it is proven that AI delivers value. Now you build the system production-ready: automated data pipelines, the specification-first pattern, and validation at three levels (syntactic, behavioural, goal-aligned). Behaviour changes are implemented in a controlled manner with pre-defined intent, boundaries, and verification method.

**Entry criteria:** Gate 2 approved, validation pilot >90%, cost overview approved, team complete.

______________________________________________________________________

## 2. Components

- [Overview & Objectives](01-doelstellingen.md) — What this phase aims to achieve
- [Activities](02-activiteiten.md) — Data pipelines, RAG/fine-tuning, specification-first method
- [Deliverables & Gate 3](03-afleveringen.md) — Production-ready system, validation report, test suite
- [Specification-first Pattern](05-sdd-patroon.md) — Define expected behaviour before you build
- [Engineering Patterns](06-engineering-patterns.md) — Proven patterns and anti-patterns for AI development

______________________________________________________________________

## 3. Common pitfalls

- **Building without specification** — the specification-first pattern prevents expensive rework
- **Not maintaining a golden set** — test cases age; keep them current with each iteration
- **Changing too much at once** — small, bounded behaviour changes are easier to validate
- **Not considering buy vs. build** — SaaS may be faster; validation requirements remain identical

______________________________________________________________________

**Next step:** After Gate 3 (Production-ready), proceed to [Phase 4 — Delivery](../05-fase-levering/01-doelstellingen.md).
