---
versie: '1.0'
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
