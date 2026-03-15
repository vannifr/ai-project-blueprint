---
versie: '1.0'
type: guide
layer: 2
phase: [3]
roles: [Tech Lead]
tags: [mlops, security, validation]
---

# 1. Engineering Patterns for AI-Driven Development

## 1. Purpose

This module describes proven engineering patterns and common anti-patterns for teams using AI tools during the development phase. The goal is to ensure the quality of AI-generated output and prevent productivity loss through rework.

______________________________________________________________________

## 2. Patterns

### Pattern 1: Safe Refactor

**Problem:** AI-generated refactoring can introduce subtle regressions.

**Solution:**

1. Write or validate tests that capture current behaviour.
1. Let AI perform the refactoring.
1. Run existing tests to detect regressions.
1. Review the diff manually for intent and readability.

```
[Write tests] → [AI refactors] → [Run tests] → [Human review]
```

**Why:** Tests act as a safety net. If tests pass but the code is unreadable, reject the change.

### Pattern 2: AI as First Reviewer

**Problem:** Human code review is time-consuming and inconsistent for style and convention checks.

**Solution:**

1. Configure AI to review code for conventions, formatting and common mistakes.
1. Human reviewer handles only what remains: architecture decisions, business logic, security.

**When to use:** For teams with many pull requests and limited review capacity. The AI review is a filter, not a replacement.

### Pattern 3: Bounded Contexts for Agents

**Problem:** Agents with access to a large codebase produce inconsistent or conflicting changes.

**Solution:**

- Limit context per agent to a scoped domain (module, service, bounded context).
- Use machine-readable context files that describe the domain, interfaces and constraints.
- Do not allow agents to make changes outside their domain boundary without explicit approval.

**Why:** Domain isolation prevents "emergent complexity" — unforeseen interactions between parallel changes.

### Pattern 4: Machine-Readable Context Files

**Problem:** AI tools produce generic output because they lack project context.

**Solution:** Maintain structured context files that AI tools can consume as input:

- **Objective Card:** What the system should achieve and which boundaries apply ([Objective Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)).
- **Architecture decisions:** Technical choices recorded as Architecture Decision Records (ADRs).
- **API contracts:** Interface definitions that describe domain boundaries.
- **Hard Boundaries:** Explicit constraints that the AI must never violate.

**Why:** The more specific the context, the more relevant the AI output. Generic prompts produce generic code.

______________________________________________________________________

## 3. Anti-patterns

### Anti-pattern 1: Blind Copy-Paste

**Description:** AI-generated code is accepted without understanding what it does.

**Risk:**

- Hidden bugs and security vulnerabilities
- Technical debt that only becomes visible later
- Loss of team expertise about their own codebase

**Mitigation:** Every AI-generated change goes through the same review and test criteria as manually written code. Use the [Definition of Done](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) as a benchmark.

### Anti-pattern 2: Prompt Perfectionism

**Description:** The engineer spends more time refining the prompt than building the solution.

**Risk:**

- Delayed delivery without quality improvement
- False sense of control (the "perfect prompt" does not exist)

**Mitigation:** Set a time limit on prompt iteration. If the output is not usable after three attempts, build it manually and use the prompt as documentation for next time.

### Anti-pattern 3: Context Pollution

**Description:** Too much or irrelevant context is provided to the AI.

**Risk:**

- Lower output quality (the model gets "lost" in noise)
- Higher costs due to unnecessary token consumption
- Slower response times

**Mitigation:** Apply the principle of "minimum effective context". Only include information directly relevant to the current task. Use the [Context Builder](../08-rollen-en-verantwoordelijkheden/index.md) approach.

### Anti-pattern 4: Unvalidated Chain

**Description:** Multiple AI steps in sequence without intermediate validation.

**Risk:** Errors in step 1 are amplified in steps 2, 3, 4 (hallucination escalation).

**Mitigation:** Build validation checkpoints after every significant AI step. Use the [3-layer validation model](../01-ai-native-fundamenten/04-validatie-model.md): syntactic (automated), behavioural (tests), intent (human).

______________________________________________________________________

## 4. Limiting Rework

Research shows that a significant proportion of time savings from AI tools is lost to rework — correcting and rewriting AI-generated output.

**Strategies to limit rework:**

1. **Specification-first:** Define the expected result before deploying AI ([SDD Pattern](05-sdd-patroon.md)).
1. **Work incrementally:** Have AI produce small, verifiable pieces rather than large blocks.
1. **Direct feedback:** Correct AI output immediately and specifically. Vague feedback leads to vague improvements.
1. **Measure acceptance rate:** Monitor what percentage of AI suggestions is actually adopted. A declining rate signals that context needs improvement.

______________________________________________________________________

## 5. Related Modules

- [SDD Pattern (Specification-Driven Development)](05-sdd-patroon.md)
- [Validation Model](../01-ai-native-fundamenten/04-validatie-model.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Objective Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)

______________________________________________________________________
