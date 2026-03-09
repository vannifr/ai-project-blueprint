# House Style & Writing Guide (Style Guide v2.2 — English)

This guide ensures that all modules in the Playbook remain consistent, readable, and uniform. Version 2.2 is adapted for English-speaking professionals working alongside the Flemish/Dutch source material, and synchronises the terminology table with the current documentation standard.

______________________________________________________________________

## Tone & Voice

We write for professionals who want to take action. Our language is direct, activating, and confident.

- **Professional register:** Address the reader as "you" consistently. Use a formal but accessible register — avoid overly academic language.
- **Active over Passive:**
    - ❌ Avoid: "It will be assessed by the team whether the data is suitable."
    - ✅ Use: "The team evaluates the data."
- **The "We" form:** We write from the perspective of the project team. "We build", "We validate".
- **No Academic Jargon:** Avoid obscure or overly theoretical language. This is a practical handbook.

______________________________________________________________________

## Terminology & Lexicon (The Translation Table)

We bridge the gap between technology and business. Use the table below for consistent terminology that is both technically accurate and accessible to a broad professional audience.

> **Note v2.2:** The table below reflects the **current documentation standard**. Several terms have been deliberately updated from v2.1 to align with internationally recognised professional vocabulary.

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

Follow this process when adding a new module or editing an existing one.

### Determine the Position in the Lifecycle

Refer to **Module 00 (The Strategic Framework)**. Where does your document belong?

- Is it strategy? → Module 00–02.
- Is it execution? → Module 03–05.
- Is it management? → Module 06.
- Is it a template? → Module 09+.

### Use the Fixed Structure

Every Process Module must follow this anatomy:

1. **Objective (The Why):** One powerful sentence.
1. **Entry Criteria (Definition of Ready):** What must be complete before we may begin?
1. **Core Activities (The What):** 3 to 5 clear steps. Use terms from the Lexicon.
1. **RACI (The Who):** Who is Responsible (R) and who is Accountable (A)?
1. **Exit Criteria (The Gate):** The checklist to close the phase.
1. **Deliverables:** The concrete artefacts to be produced.

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

## Publication Checklist

- [ ] Have I replaced all jargon terms with the Playbook standard equivalents?
- [ ] Have I checked for plagiarism (no copy-paste from sources)?
- [ ] Is the tone active ("We do") and not passive ("It is done")?
- [ ] Are the icons placed at the correct sections?
- [ ] Are external claims supported by a source reference `[so-XX]`?
- [ ] Is the corresponding NL source document synchronised?
- [ ] Has the new source been added to `docs/16-bronnen/index.en.md`?

______________________________________________________________________

© 2026 AI Project Playbook. Licensed under CC BY-NC-SA 4.0.
