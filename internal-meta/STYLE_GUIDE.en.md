# House Style & Writing Guide (Style Guide v2.3 — English)

This guide ensures that all modules in the Playbook remain consistent, readable, and uniform. Version 2.3 incorporates lessons from the March 2026 editorial audit: stricter rules on redundancy, mandatory Collaboration Mode linkage at gates, CTA structure per module, and extended terminology.

**Languages:** The Blueprint is available in **Dutch (default)** and **English** only.

______________________________________________________________________

## Tone & Voice

We write for professionals who want to take action. Our language is direct, activating, and confident.

- **Professional register:** Address the reader as "you" consistently. Use a formal but accessible register — avoid overly academic language.
- **Active over Passive:**
    - ❌ Avoid: "It will be assessed by the team whether the data is suitable."
    - ✅ Use: "The team evaluates the data."
- **The "We" form:** We write from the perspective of the project team. "We build", "We validate".
- **No Academic Jargon:** Avoid obscure or overly theoretical language. This is a practical handbook.
- **Register per layer:**
    - Layer 1 (Strategy): persuasive, concise, executive level — no step-by-step lists
    - Layer 2 (Phases): step-by-step, instructive, team-oriented — use imperative ("Determine", "Assess")
    - Layer 3 (Toolkit): functional, scannable, without prose — tables and checklists over running text

______________________________________________________________________

## Single Source of Truth — the anti-redundancy rule

> **Core rule: one concept, one home. All other references link to it.**

The AI lifecycle, the five collaboration modes, the four core artefacts, and the risk classification are explained **once in full** — in their canonical home document. All other modules reference them; they do **not** repeat the explanation.

| Concept                                                          | Canonical home document                                      |
| :--------------------------------------------------------------- | :----------------------------------------------------------- |
| AI lifecycle (5 phases)                                          | `docs/00-strategisch-kader/01-ai-levenscyclus.en.md`         |
| Collaboration modes (Mode 1–5)                                   | `docs/00-strategisch-kader/06-has-h-niveaus.en.md`           |
| Core artefacts (goal definition, red lines, prompts, validation) | `docs/01-ai-native-fundamenten/01-definitie.en.md`           |
| Risk classification (pyramid)                                    | `docs/01-ai-native-fundamenten/05-risicoclassificatie.en.md` |
| Evidence standards per risk class                                | `docs/01-ai-native-fundamenten/07-bewijsstandaarden.en.md`   |
| Gate criteria (4 gates)                                          | `docs/09-sjablonen/08-gate-reviews/template.en.md`           |

**Practical test:** Does the same explanation appear in more than one document? Keep the version in the canonical home. Replace all other instances with a reference: `→ See [Collaboration Modes](../../00-strategisch-kader/06-has-h-niveaus.en.md) for the full explanation.`

______________________________________________________________________

## Collaboration Modes — mandatory linkage at gates

Every phase gate and every template containing a go/no-go decision **explicitly states the relevant collaboration mode (Mode 1–5)** as a design constraint.

**Standard phrasing at gates:**

```markdown
**Collaboration mode:** [Mode X — Name]
Required validation for this mode: [reference to 01.07 Evidence Standards]
```

**Guidance per phase:**

| Phase            | Typical modes | What to state                                                     |
| :--------------- | :------------ | :---------------------------------------------------------------- |
| Discovery (02)   | 1–3           | State the intended mode as a design choice in the Project Charter |
| Validation (03)  | 1–3           | Verify mode at Gate 2 (does the mode match the risk level?)       |
| Realisation (04) | 1–4           | SDD specification states the mode as a constraint                 |
| Delivery (05)    | 1–4           | Handover protocol specifies human oversight requirements per mode |
| Operations (06)  | all           | Drift thresholds and human checkpoints depend on the mode         |

______________________________________________________________________

## Terminology & Lexicon (The Translation Table)

We bridge the gap between technology and business. Use the table below for consistent terminology that is both technically accurate and accessible to a broad professional audience.

> **Note v2.3:** The table reflects the **current documentation standard**. Terms have been deliberately aligned with internationally recognised professional vocabulary.

| ❌ Avoid (Jargon / NL import)                | ✅ Use (Current Playbook Standard)              | Notes                                                                 |
| :------------------------------------------- | :---------------------------------------------- | :-------------------------------------------------------------------- |
| Cost footprint                               | **Cost overview**                               | More formal and businesslike                                          |
| Shadow AI                                    | **Uncontrolled AI use**                         | Ungoverned usage                                                      |
| Intent Record                                | **Goal definition**                             | The 'Why'                                                             |
| Context Artifacts / Steering instructions    | **Prompts**                                     | Use "Prompts" — internationally standard                              |
| Guardrails                                   | **Hard boundaries / Red Lines**                 | Non-negotiable constraints                                            |
| Proof of Value (PoV) / Validation pilot      | **Proof of Value (PoV)**                        | PoV is the standard abbreviation; spell out on first use              |
| Model Drift / Performance degradation        | **Drift**                                       | Write as "Drift"; on first use add: "Drift (performance degradation)" |
| Retrieval Augmented Gen / Knowledge coupling | **RAG**                                         | Write as "RAG" — no English paraphrase required                       |
| Hyperparameter Tuning / Model fine-tuning    | **Fine-tuning**                                 | Standardised term in this playbook                                    |
| Deployment                                   | **Go-live / Release**                           |                                                                       |
| Inference costs                              | **Usage costs**                                 | Cost per model call                                                   |
| Bias audit / Fairness check                  | **Fairness audit (bias audit)**                 | Use both terms on first mention                                       |
| Benefits realisation                         | **Benefits realisation (benefits realization)** | Use full term on first mention per document                           |
| Goal card                                    | **Goal card (Doelkaart)**                       | Include NL equivalent on first mention                                |

______________________________________________________________________

## Agentic AI — terminology

| ❌ Avoid                       | ✅ Use (Blueprint standard) | Notes                                                                                                         |
| ------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| AI agent / bot                 | **Agent**                   | Write without qualifier; "the agent" is correct                                                               |
| Multi-agent system             | **Multi-agent system**      | On first mention add: "multi-agent system (multiple collaborating agents)"                                    |
| Orchestrator / conductor       | **Orchestrator**            | Internationally standard; no paraphrase needed                                                                |
| Tool calls / function calls    | **Tool calls**              | Use consistently; singular: "tool call"                                                                       |
| Memory                         | **Agent memory**            | Always specify type on first mention: short-term memory (context window) or long-term memory (vector storage) |
| ReAct / Reason + Act           | **ReAct pattern**           | On first use add: "ReAct pattern (alternating reasoning and action steps)"                                    |
| Human-in-the-loop              | **Human in the loop**       | Alternative: "human checkpoint" in non-technical text                                                         |
| Human-on-the-loop              | **Human on the loop**       | Use only in Mode 4 (Delegated) context                                                                        |
| Agentic workflow               | **Agentic workflow**        | Standard; "agentic" as adjective throughout                                                                   |
| Tool allowlist / whitelist     | **Tool allowlist**          | Avoid "whitelist" — use "tool allowlist"                                                                      |
| Circuit breaker                | **Circuit breaker**         | On first use add: "circuit breaker (automatic stop triggered by anomalous behaviour)"                         |
| Excessive Agency (OWASP LLM06) | **Excessive agency**        | Always include full OWASP reference on first mention                                                          |
| Sandboxed execution            | **Sandboxed execution**     | Alternative: "isolated execution" in non-technical text                                                       |
| Task decomposition             | **Task decomposition**      | Specific to agentic planning; do not confuse with work packages                                               |

______________________________________________________________________

## AI Project Management as a Discipline — terminology

| ❌ Avoid               | ✅ Use (Blueprint standard)              | Notes                                                                                            |
| ---------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Managing uncertainty   | **Productive uncertainty**               | The core of AI-PM: knowing when to continue and when to stop                                     |
| Failed experiment      | **Experiment without converging result** | More neutral; avoids blame culture around iterations                                             |
| Model doesn't work     | **Model does not meet success criteria** | Always links back to the Golden Set; avoid vague negatives                                       |
| Sprint velocity        | **Iteration velocity**                   | In AI context; always link to experiment budget, not only story points                           |
| Stakeholder management | **Expectation management**               | More specific in AI-PM context than generic stakeholder management                               |
| Model accuracy         | **Model accuracy**                       | Write in full; add the metric used on first mention (e.g. F1, Precision@K)                       |
| Retraining             | **Retraining**                           | On first use add: "retraining (re-training the model on new or corrected data)"                  |
| Concept drift          | **Concept drift**                        | Distinguish explicitly from data drift and model drift                                           |
| Cone of uncertainty    | **Cone of uncertainty**                  | On first use add: "cone of uncertainty (increasing uncertainty as the planning horizon extends)" |
| Build vs. buy          | **Build or buy**                         | Write out in full in running text                                                                |
| Foundation model       | **Foundation model**                     | Use "LLM" only when referring specifically to language models                                    |

______________________________________________________________________

## Source Citations `[so-XX]`

External claims, statistics, legislation, and research findings **always require** a source reference in the format `[so-XX]`.

**When required:**

- Statistics and quantitative claims ("40% of AI time savings are lost to rework")
- References to legislation (EU AI Act, GDPR, PLD)
- External frameworks (NIST, OWASP, ISACA)
- Research findings (universities, consultancies, standards bodies)

**When not required:**

- Internal blueprint concepts (Red Lines, Golden Set, Goal Card)
- Process descriptions that describe the blueprint's own methodology
- Universally accepted definitions without a specific source

**Format:** Place `Source: \[so-XX\]` or `Sources: \[so-XX\], \[so-YY\]` on a separate line after the relevant paragraph or table. See `docs/16-bronnen/index.en.md` for the full sources list.

______________________________________________________________________

## Admonitions (Information Boxes)

Use MkDocs Material admonitions sparingly and consistently. Each type has a specific purpose:

| Admonition    | Use for                                                             |
| :------------ | :------------------------------------------------------------------ |
| `!!! tip`     | Practical advice that helps the reader — not mandatory but valuable |
| `!!! info`    | Contextual background information that deepens understanding        |
| `!!! warning` | A risk or pitfall that requires active attention                    |
| `!!! danger`  | A critical boundary or prohibition — do not ignore                  |
| `!!! check`   | Checklists requiring action (preferred in gates and templates)      |

**Guidelines:**

- Maximum **2 admonitions per section** — more disrupts the reading flow
- Admonition text is **concise** (max. 4 lines); longer explanation belongs in the running text
- Use the **title syntax** for specific context: `!!! warning "Title of the warning"`

______________________________________________________________________

## Module Anatomy — fixed structure

Every Process Module (Layer 2) must follow this anatomy:

1. **Objective (The Why):** One powerful sentence.
1. **Entry Criteria (Definition of Ready):** What must be complete before we may begin?
1. **Core Activities (The What):** 3 to 5 clear steps. Use terms from the Lexicon.
1. **RACI (The Who):** Who is Responsible (R) and who is Accountable (A)?
1. **Exit Criteria (The Gate):** The checklist to close the phase. Always state the intended Collaboration Mode.
1. **Deliverables:** The concrete artefacts to be produced.
1. **CTA block (Next step):** See "Module CTA" below.

______________________________________________________________________

## Module CTA (Call to Action)

Every module in Layer 2 ends with a **"Next step" block**. This is not optional.

**Format:**

```markdown
______________________________________________________________________

**Next step:** [One concrete action the reader can take now]
→ Use the [Template name](relative/path/to/template.en.md) as your starting point.
→ See also: [Related module](relative/path.en.md)
```

**CTA guidelines:**

- The action is specific ("Complete the Goal Card") — not vague ("Continue")
- Always reference the relevant template if one exists
- Maximum 3 "See also" links — more dilutes the focus

______________________________________________________________________

## Case Studies (Worked Examples)

Anonymised real-world examples strengthen credibility and make abstract concepts concrete. Use the following format:

```markdown
!!! info "Case study — [Sector] / [Risk class]"
    **Situation:** [2–3 sentences: what was the AI project, what was the challenge]
    **Approach:** [2–3 sentences: which part of the Blueprint was applied]
    **Outcome:** [1–2 sentences: measurable or qualitative result]
    *Sector: [e.g. Financial services] — Names anonymised.*
```

**Placement rule:** Maximum **1 case study per module**. Preferred position: after core activities, before exit criteria. Longer cases belong in `docs/17-bijlagen/`.

**Priority for the first series (see IMPLEMENTATION_PLAN.md):**

- 1 example per risk class: Minimal, Limited, High Risk
- Sectors: healthcare, finance, government, HR (aligned with EU AI Act Annex III)

______________________________________________________________________

## Green AI — sustainability integration

Sustainability is not a standalone chapter — it is a **cross-cutting concern** that appears at three fixed points:

1. **Business Case (Phase 2):** Mandatory field "Environmental footprint" — estimate inference and training costs in CO₂ equivalents.
1. **Risk Pre-Scan (Phase 1):** Trigger: "Does the system require continuous large-scale inference?" → refer to the Green AI standard.
1. **Operations & Optimisation (Phase 5):** Drift monitoring includes cost efficiency; refer to Green AI benchmarks.

Always refer to `docs/08-technische-standaarden/` for the full Green AI guidelines. Do not re-explain Green AI in phase modules.

______________________________________________________________________

## Plagiarism & Originality

- **Strict rule:** Never copy verbatim sentences from source materials (PMI documents, ISO standards, external whitepapers).
- **Paraphrase:** Read the source, understand the core, and write it as if explaining it to a colleague.
- **Context:** Always translate general theory into the specific context of our modular approach.

______________________________________________________________________

## Formatting Standards (Markdown)

Consistency ensures readability.

- **Headings:**
    - `#` for Module names.
    - `##` for Chapters.
    - `###` for Activities.
- **Navigation icons:** Use emojis sparingly but functionally:
    - 📂 = Module / Chapter
    - 🎯 = Objective
    - ⚙️ = Activities / Process
    - 👥 = Roles (RACI)
    - ✅ = Checklists / Gates
- **Lists:** Use bullet points for enumerations and numbered lists for step-by-step procedures.
- **Separator lines:** Use `______________________________________________________________________` as a section separator between H2 sections. Not between H3 subsections.

______________________________________________________________________

## Author Instructions

### Determine the Position in the Lifecycle

Refer to **Module 00 (The Strategic Framework)**. Where does your document belong?

- Is it strategy? → Module 00–02.
- Is it execution? → Module 03–05.
- Is it management? → Module 06.
- Is it a template? → Module 09+.

### The Plain Language Check (Readability)

Read your draft through the eyes of a non-technical manager (e.g. a CFO).

- Do they understand "Inference costs"? → No? Change to **"Usage costs"**.
- Do they understand "Bias audit"? → Use **"Fairness audit (bias audit)"**.

### Version Control

End every document with a footer for traceability:

______________________________________________________________________

**Version:** \[X.X\]
**Date:** \[DD Month YYYY\]
**Status:** \[Draft / Final\]

______________________________________________________________________

## Placement Rules for New Content

Before creating a new document, always consult:

1. **[INFORMATION_ARCHITECTURE.en.md](INFORMATION_ARCHITECTURE.en.md)** — decision tree for where new content belongs
1. **[AI_COPYWRITER_CONSTITUTION.en.md](AI_COPYWRITER_CONSTITUTION.en.md)** — content principles and final test
1. **[BACKLOG.md](BACKLOG.md)** — check whether the topic is already planned

**Rule of thumb:** One new concept = extend one existing document. Only when a genuinely new theme fits nowhere: create a new file.

______________________________________________________________________

## Publication Checklist

- [ ] Have I replaced all jargon terms with the Playbook standard equivalents?
- [ ] Have I checked for plagiarism (no copy-paste from sources)?
- [ ] Is the tone active ("We do") and not passive ("It is done")?
- [ ] Are the icons placed at the correct sections?
- [ ] Are external claims supported by a source reference `[so-XX]`?
- [ ] Have I applied the Single Source of Truth rule — no repeated explanation of core concepts?
- [ ] Does the module include a CTA block ("Next step")?
- [ ] Does the gate state the relevant Collaboration Mode (Mode 1–5)?
- [ ] Is the corresponding NL source document synchronised?
- [ ] Has the new source been added to `docs/16-bronnen/index.en.md`?

______________________________________________________________________

© 2026 AI Project Playbook. Licensed under CC BY-NC-SA 4.0.

______________________________________________________________________

**Version:** 2.3
**Date:** 13 March 2026
**Status:** Final
