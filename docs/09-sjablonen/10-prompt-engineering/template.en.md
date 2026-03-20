---
versie: '1.0'
type: template
layer: 3
phase: [3, 5]
roles: [Data Scientist]
tags: [prompt-engineering, template]
answers: [How do I use the Prompt Engineering Template template?]
---

# 1. Prompt Engineering Template

## 1. Purpose

This template helps build high-quality **System Prompts**. A well-structured prompt reduces hallucinations and increases reliability.

______________________________________________________________________

## 2. Structure of a Top Prompt

### Context (The Background)

- **Who are you?** \[E.g. "You are a senior data analyst at a telecoms company."\]
- **What is the situation?** \[E.g. "You are analysing customer data to find patterns in cancellations."\]

### Task (The Action)

- **What needs to happen?** \[E.g. "Summarise the top 3 reasons for churn based on the attached transcripts."\]
- **Use active verbs!** (Summarise, Classify, Generate).

### System Prompts (Knowledge & Rules)

- **Knowledge source:** \[E.g. "Use only the information from the attached PDF."\]
- **Step-by-step approach:** \[E.g. "Step 1: Scan for keywords. Step 2: Check sentiment. Step 3: Formulate advice."\]

### Hard Boundaries (Constraints)

- **What is ABSOLUTELY NOT ALLOWED?** \[E.g. "Never mention individual employee names."\]
- **Limits:** \[E.g. "Limit your response to a maximum of 200 words."\]

### Output Format (The Form)

- **What should it look like?** \[E.g. "A numbered list in Markdown", "A JSON object", "A table"\].
- **Tone:** \[E.g. "Professional and concise", "Friendly and empathetic"\].

______________________________________________________________________

## 3. Examples (Few-Shot)

*Add 2-3 examples of Input ↔ Desired Output here to guide the AI.*

______________________________________________________________________

## 4. Version Control (Prompt Versioning)

Prompts are production code. Manage them like code: version, changelog and rollback.

### Semantic versioning

| Change                                             | Version bump  | Example         |
| :------------------------------------------------- | :------------ | :-------------- |
| New Hard Boundary or task change                   | Major (X.0.0) | v1.0.0 → v2.0.0 |
| Tone, context or few-shot adjustment               | Minor (x.Y.0) | v1.0.0 → v1.1.0 |
| Spelling/style correction without behaviour change | Patch (x.y.Z) | v1.0.0 → v1.0.1 |

### Prompt Changelog

| Version | Date     | Changed by | Description     | Tested on Golden Set |
| :------ | :------- | :--------- | :-------------- | :------------------- |
| v1.0.0  | \[date\] | \[name\]   | Initial version | ☐ Yes / ☐ No         |
| v1.1.0  | \[date\] | \[name\]   | \[description\] | ☐ Yes / ☐ No         |

### Rollback Procedure

1. Revert to the previous prompt version in Git.
1. Re-run the Golden Set to confirm regression.
1. Document the regression in the Kaizen Log.
1. Inform the Guardian when changes affect Hard Boundaries.

> Store all versions in Git with a tag per major version: `prompt-v1.0.0`.

______________________________________________________________________
