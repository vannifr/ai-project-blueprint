---
versie: '1.0'
type: guide
layer: 2
phase: [3]
roles: [AI Product Manager]
summary: Proven engineering patterns and common anti-patterns for teams using AI tools, focused on quality assurance and preventing rework.
answers: [How does Engineering Patterns for AI-Driven Development work?, What roles do I need?, How do I use AI as a development tool when the end product itself does not contain AI (Type A)?]
---

# 1. Engineering Patterns for AI-Driven Development

!!! abstract "Purpose"
    Proven engineering patterns and common anti-patterns for teams using AI tools, focused on quality assurance and preventing rework.

!!! tip "When to use this?"
    Your team is using AI tools (such as code assistants) during development and you want to know which working patterns ensure quality and which pitfalls to avoid.

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

## 5. AI-Assisted Development Practices (Type A)

!!! info "Type A versus Type B"
    The patterns above target **Type B** projects: systems that contain AI themselves. This section covers **Type A** projects — teams that use AI as a development tool (pair programming, code review, code generation) while the end product itself does not contain AI. Think of a web application, an API or a mobile app built with the help of AI assistants.

### 5.1 AI Pair Programming

AI pair programming means a developer collaborates with an AI assistant (such as Copilot, Cursor or Claude Code) while writing code. The ground rules:

- **Treat AI suggestions as draft code.** Read every suggestion, understand what it does and adapt it before accepting. "Accept all" is not a workflow.
- **Steer quality through context files.** Add ADRs, coding conventions and examples of good code to the context. The better the input, the more usable the output.
- **Time-box your AI sessions.** Set a limit (e.g. 20 minutes) per problem. If the AI does not produce usable output after three iterations, switch to manual work. You are the programmer, not the prompter.
- **Pair, don't delegate.** Use AI to reach a first draft faster, but always take the wheel for edge cases, error handling and domain-specific logic.

!!! warning "Anti-pattern: Blind Copy-Paste"
    Accepting AI-generated code without understanding what it does is the most common and most dangerous anti-pattern. It leads to hidden bugs, security vulnerabilities and loss of knowledge about your own codebase. See also [Anti-pattern 1](#anti-pattern-1-blind-copy-paste).

### 5.2 AI-Assisted Code Review

A layered review approach combines speed (AI) with depth (human):

| Step                | Who         | Focus                                                                    |
| ------------------- | ----------- | ------------------------------------------------------------------------ |
| 1. Automated review | AI          | Conventions, formatting, common mistakes, missing tests, inconsistencies |
| 2. Human review     | Developer   | Business logic, security implications, architectural fit, readability    |
| 3. Approval         | Team member | Final assessment and merge decision                                      |

**What AI is good at:**

- Flagging inconsistencies between code and existing conventions
- Spotting missing tests or test scenarios
- Detecting style violations and formatting issues
- Finding simple bugs (null checks, off-by-one errors, unused variables)

**What AI is bad at:**

- Understanding business intent ("does this code do what the customer expects?")
- Assessing security implications (authentication logic, authorisation boundaries)
- Evaluating architectural trade-offs (scalability vs. complexity)
- Recognising when code is technically correct but functionally wrong

!!! danger "Rule"
    AI must never be the sole reviewer. Every pull request must be approved by at least one human reviewer.

### 5.3 Quality Assurance for AI-Generated Code

AI-generated code is code. The same quality requirements apply as for manually written code — no exceptions.

1. **Test coverage.** The same coverage requirements apply. AI-generated code does not need fewer tests, if anything more — because the developer is less intimately familiar with the implementation details.
1. **Security scanning is mandatory.** AI can introduce subtle vulnerabilities: hard-coded credentials, SQL injection via string concatenation, insecure deserialisation. Run SAST/DAST tools on all code, regardless of origin.
1. **Licence compliance.** AI models are trained on open-source code and may reproduce fragments that fall under a specific licence. Use licence detection tools if you work in a regulated environment.
1. **Quality metrics.** Measure cyclomatic complexity, duplication and dependency degree for AI-generated code separately. This reveals whether AI output improves or degrades code quality.

### 5.4 Responsibility and Accountability

- **The developer who commits the code is responsible.** It does not matter whether the code was written by a human, an AI or a combination. Whoever clicks "merge" carries the responsibility.
- **AI-generated code goes through the same gates.** Code review, tests, security scans, Definition of Done — no exceptions.
- **Document AI assistance when relevant.** For audit trails, compliance or knowledge sharing it can be valuable to record which parts were AI-assisted. This is not shame but transparency.
- **Record team agreements.** Define in your team conventions how you work with AI tools: which tools are approved, which quality checks apply, and how usage is documented.

### 5.5 Practical Checklist

Use this checklist when your team starts adopting AI development tools:

- [ ] **Tool selection:** Approved AI tools are defined and communicated to the team
- [ ] **Context files:** ADRs, coding conventions and example code are available as AI context
- [ ] **Review process:** The review process explicitly describes the division of roles between AI and human review
- [ ] **Test policy:** Coverage requirements apply equally to AI-generated and manually written code
- [ ] **Security scanning:** SAST/DAST tooling runs automatically on all pull requests
- [ ] **Licence compliance:** Licence detection is enabled if the project requires it
- [ ] **Time-boxing:** Team agreements on maximum time investment in prompt iteration are recorded
- [ ] **Ownership rule:** The team understands and accepts that whoever commits code owns it
- [ ] **Audit trail:** There is an agreement on whether and how AI assistance is documented
- [ ] **Onboarding:** New team members are trained on the AI working agreements

______________________________________________________________________

## 6. Related Modules

- [SDD Pattern (Specification-Driven Development)](05-sdd-patroon.md)
- [Validation Model](../01-ai-native-fundamenten/04-validatie-model.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Objective Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)

______________________________________________________________________
