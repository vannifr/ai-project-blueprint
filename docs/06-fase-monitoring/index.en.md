---
versie: '1.0'
type: index
layer: 2
phase: [5]
summary: Safeguard performance, ethical integrity, and cost-efficiency throughout the operational lifespan.
answers: [What does Phase 5 — Monitoring & Optimisation contain?, How do I monitor an AI system after go-live?]
---

# 5. Monitoring & Optimisation

!!! abstract "Purpose"
    Safeguard performance, ethical integrity, and cost-efficiency throughout the operational lifespan.

## 1. Purpose

After go-live, the real work begins: the system must continue to perform while data changes, user behaviour shifts, and costs accumulate. This phase focuses on drift detection, performance monitoring, cost management, and periodic reassessment. No automatic corrections — first investigate the cause, then adjust purposefully.

**Entry criteria:** System live, monitoring dashboards active, operations team ready, incident plan tested.

______________________________________________________________________

## 2. Components

- [Overview & Objectives](01-doelstellingen.md) — What this phase aims to achieve
- [Activities](02-activiteiten.md) — Continuous monitoring, cost management, feedback loop
- [Deliverables](03-afleveringen.md) — Monitoring dashboards, incident logs
- [Drift Detection](05-drift-detectie.md) — Data drift, concept drift, performance degradation, and assumption drift

______________________________________________________________________

## 3. Common pitfalls

- **No baseline recorded** — without a baseline you cannot detect drift
- **Auto-correcting without investigation** — first understand why performance is declining
- **Not monitoring costs** — API costs and compute can explode unnoticed
- **Ignoring user feedback** — the system may be technically correct but not useful

______________________________________________________________________

**Next step:** Set up [Continuous Improvement](../10-doorlopende-verbetering/index.md) for structural feedback loops.
→ See also: [Gate 4 (Quarterly Review)](../09-sjablonen/04-gate-reviews/checklist.md) for periodic reassessment.
