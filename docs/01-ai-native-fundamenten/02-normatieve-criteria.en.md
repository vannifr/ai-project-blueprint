---
versie: '1.3'
type: foundation
layer: 1
summary: This page describes the five core principles that distinguish an AI-native approach from traditional software development, and the assessment criteria to determine whether a project falls under these…
answers: [What does Assessment Criteria & AI-Native Principles entail?]
---

# Assessment Criteria & AI-Native Principles

!!! abstract "Purpose"
    This page describes the five core principles that distinguish an AI-native approach from traditional software development, and the assessment criteria to determine whether a project falls under these principles.

______________________________________________________________________

## 1. When Does This Apply?

A project falls under the AI-native approach when it meets at least two of these three conditions:

| Condition                    | Description                                                                                              |
| :--------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Material Impact**          | The system influences production outputs, decisions or customer interactions.                            |
| **Context-Driven Behaviour** | Inputs that steer behaviour (prompts, RAG sources, fine-tuning data) are actively managed and versioned. |
| **Non-Deterministic**        | The output is probabilistic — the same input can produce different results.                              |

> Once qualified, the five principles below serve as guidance for governance, development and monitoring.

______________________________________________________________________

## 2. The Five AI-Native Principles

### Principle 1 — Behaviour Steering Over Model Choice

The behaviour of an AI system is primarily determined by **specifications, prompts and hard boundaries** — not by which model runs underneath. Invest in clearly defined expected behaviour before investing in model optimisation.

**In practice:**

- Write a [Goal Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) before choosing a model.
- Define [Hard Boundaries](../09-sjablonen/12-cheatsheets/07-rode-lijnen.md) as non-negotiable constraints.
- Treat prompts as versioned artefacts, not throwaway experiments.

______________________________________________________________________

### Principle 2 — Proportional Governance

The weight of controls, validation and documentation should be proportional to the **risk** of the system. An internal summarisation tool requires a lighter approach than a customer-facing decision system.

**In practice:**

- Use the [Risk Classification](05-risicoclassificatie.md) to determine the level (Critical → Low).
- [Fast Lane](../02-fase-ontdekking/06-fast-lane.md) for minimal risk; full lifecycle for high risk.
- Adjust the burden of proof per Gate Review — not every gate requires the same depth.

______________________________________________________________________

### Principle 3 — Evidence Over Assumptions

Every claim about performance, safety or value must be supported by **measurable results**. Intuition and demos are not evidence; structured tests and validation reports are.

**In practice:**

- Compile a [Golden Set](../09-sjablonen/07-validatie-bewijs/template.md) before development.
- Validate at three levels: syntactic (does it work?), behavioural (does it do what's expected?), goal-oriented (does it help the user?).
- Document results in a [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md).

______________________________________________________________________

### Principle 4 — Human in Control

AI systems operate within frameworks determined by humans. At higher [Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md) (delegated, autonomous), the frameworks become stricter, not looser.

**In practice:**

- Every mode has explicit escalation criteria and an emergency stop.
- The [Guardian](../07-compliance-hub/index.md) has veto rights when hard boundaries are breached.
- Human-in-the-loop is the default; human-on-the-loop only after explicit approval.

______________________________________________________________________

### Principle 5 — Continuous Validation

AI behaviour changes over time due to data drift, model updates and changing context. Validation is therefore not a one-off activity but an **ongoing process**.

**In practice:**

- Set up [Monitoring & Drift Detection](../06-fase-monitoring/05-drift-detectie.md) from day one.
- Repeat Golden Set tests with every significant change.
- Use [Retrospectives](../10-doorlopende-verbetering/01-retrospectives.md) and [Kaizen Logs](../10-doorlopende-verbetering/02-kaizen-logs.md) to continuously improve the approach.

______________________________________________________________________

## 3. Related Modules

- [AI-Native Definition](01-definitie.md) — what makes a system AI-native?
- [Artefact Model](03-artefact-model.md) — the five managed artefacts
- [Validation Model](04-validatie-model.md) — the three validation dimensions
- [Evidence Standards](07-bewijsstandaarden.md) — what must you prove per gate?
