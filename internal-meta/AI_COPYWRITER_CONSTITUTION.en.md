# AI Copywriter Constitution — AI Project Blueprint

**Version:** 1.0
**Date:** 10 March 2026

This document defines the content principles for everyone — human or AI — writing content for the Blueprint. It is not a style guide (see STYLE_GUIDE.en.md) and not an architecture guide (see INFORMATION_ARCHITECTURE.en.md). It answers the question: *why do we write what we write, and what do we never write?*

Read this document before you type a single word.

______________________________________________________________________

## The Reader

The reader is an **AI Project Manager** in the middle of a project. They have little time, are under pressure from stakeholders who want results, and are dealing with a technology that evolves faster than any methodology. They have no need for theory for theory's sake. They need a clear answer to a concrete question.

Always write for that person.

Not for the regulator. Not for the academic. Not for the AI that may be reading this.

______________________________________________________________________

## The Five Content Principles

### 1. Concrete action over abstract description

Every page must end with something the reader can do tomorrow. If you explain a concept without it leading to action, the page is incomplete.

- ❌ "Drift is a phenomenon in which model performance degrades due to changes in the input distribution."
- ✅ "If your model scores lower two weeks after go-live than it did at Gate 3: run a Golden Set test, compare to the baseline and document the difference. Only then decide whether to retrain."

### 2. Governance as protection, not bureaucracy

The Blueprint asks teams to produce documentation, approvals and gate reviews. Write these as protection for the team — not as compliance theatre for the organisation. The difference is in tone.

- ❌ "The Guardian must sign the form before the gate."
- ✅ "The Guardian signs before the gate so that no one is later personally liable for a decision the whole team made together."

### 3. Honesty about uncertainty

AI projects are inherently uncertain. The Blueprint does not offer false certainty. If something depends on context, say so. If a recommendation applies in most cases but not all, say so. Absolute statements are only justified for hard boundaries (Red Lines, legal requirements).

- ❌ "A chunk size of 512 tokens is optimal."
- ✅ "512 tokens is a good starting point for continuous text. Test with your specific data before deciding."

### 4. Ownership over process description

The Blueprint does not describe how processes work in the abstract. It describes who is responsible for what and what that person concretely does. Every piece of content has an owner — a role from the RACI.

Do not write: "Validation takes place." Write: "The Data Scientist validates the Golden Set before Gate 2."

### 5. Simplicity as the final test

After writing a section: re-read it as a busy PM seeing it for the first time. If they still don't know what to do after reading it twice, it is too complex. Rewrite — simplify, shorter sentences, fewer levels.

A good page does not need to be exhaustive. A good page needs to be usable.

______________________________________________________________________

## What We Do Not Write

**No hype.** The Blueprint makes no promises AI cannot keep. "AI will double your productivity" never appears here. Statistics we use are cited and nuanced.

**No fear.** Compliance and risk are serious, but the tone is never alarming for dramatic effect. Danger admonitions are for real boundaries, not theatrical emphasis.

**No vendor lock-in.** We do not name specific tools as the only choice. We name examples with explicit alternatives. Tools change; principles do not.

**No completeness for its own sake.** Missing an edge case is not a failure. A page that covers 90% of cases well is better than a page that covers all cases but is unreadable.

**No duplicate content.** If it already exists somewhere, link to it. Repetition creates inconsistency at update time.

______________________________________________________________________

## When Principles Conflict

Sometimes principles conflict. Here is the priority order:

1. **Legal correctness** always wins. When in doubt about EU AI Act or GDPR: formulate conservatively and cite the source.
1. **Reader safety** wins over readability. An extra warning may disrupt the flow if it prevents harm.
1. **Usability** wins over completeness. A workable guideline for 80% of cases beats an exhaustive decision tree that nobody uses.
1. **Consistency** wins over personal style preference. Follow the Style Guide even if you disagree — open a discussion afterwards.

______________________________________________________________________

## The Final Test

Ask yourself this one question before publishing:

> **"Would an AI Project Manager reading this at 5pm on a busy Friday know what to do first thing tomorrow morning?"**

If the answer is no, the page is not ready.

______________________________________________________________________

## For AI-Generated Content Specifically

When using an AI tool (including Claude) to write or improve content:

1. **Always provide context**: which phase, which role is the reader, which specific gap is being filled.
1. **Do not generate new terminology**. Use only terms from the Lexicon in STYLE_GUIDE.en.md.
1. **Do not generate statistics** unless you can provide a `[so-XX]` source that exists in `docs/16-bronnen/index.en.md`.
1. **Always check for duplicate content**: search first whether the concept already exists before adding new text.
1. **Have a human perform the final test.** AI-generated text is a starting point, not a finished product.

______________________________________________________________________

**Related documents:**

- [STYLE_GUIDE.en.md](STYLE_GUIDE.en.md) — tone, terminology, formatting
- [INFORMATION_ARCHITECTURE.en.md](INFORMATION_ARCHITECTURE.en.md) — structure and placement rules
