---
versie: '1.1'
description: 'AI Collaboration Modes: five levels of human-AI autonomy — from Instrumental to Autonomous — with decision criteria for selecting the right mode per task and risk profile.'
type: strategic
layer: 1
summary: Classification of five human-AI collaboration modes (Instrumental to Autonomous) to determine the right governance and risk controls per application.
answers: [What does AI Collaboration Modes entail?, How do I classify the risk of my AI project?]
---

# 1. AI Collaboration Modes

!!! abstract "Purpose"
    Classification of five human-AI collaboration modes (Instrumental to Autonomous) to determine the right governance and risk controls per application.

## 1. Purpose of the Modes

To determine which processes, governance and risk controls are needed, we classify the relationship between human and machine into five **Collaboration Modes**.

This model describes the shift from AI as a tool to AI as an independent actor. It is crucial to define upfront in which mode a system operates, because a 'Mode 4' system (Delegated) requires far stricter safety rules than a 'Mode 2' system (Advisory).

______________________________________________________________________

## 2. The Five Modes

### Mode 1: Instrumental (The Tool)

**The human works, AI waits.**

This is the classic situation. The AI is passive and does nothing unless the human presses a button. The human is fully responsible for the initiation, execution and result.

- **Dynamic:** Human Action → AI Result.
- **Example:** Translating a text with Google Translate or generating a formula in Excel.
- **Risk:** Low (errors are seen directly by the user).
- **Governance:** Standard IT management.

### Mode 2: Advisory (The Advisor)

**AI proposes, the human decides.**

The AI analyses the situation and offers options or recommendations. The human acts as 'Gatekeeper'; nothing happens without explicit approval. This is often the entry level for professional applications.

- **Dynamic:** AI Suggestion → Human Approval/Action.
- **Example:** A copilot making code suggestions, or a system flagging fraud for inspection by an analyst.
- **Risk:** "Rubber stamping" (the human approves blindly out of convenience).
- **Governance:** Focus on training the human reviewer.

### Mode 3: Collaborative (The Partner)

**Dialogue is central.**

Human and AI work iteratively together on a complex problem. It is a ping-pong game of ideas where the end result is a mix of both intelligences. This is also called 'Co-Intelligence' or the 'Centaur model'.

- **Dynamic:** Human ↔ AI (Continuous loop of input and feedback).
- **Example:** Brainstorming and refining a strategic plan together with an AI assistant.
- **Risk:** Blurring of ownership (who thought of what?) and loss of independent critical thinking.
- **Governance:** Guidelines for attribution and fact-checking.

### Mode 4: Delegated (The Agent)

**AI executes, the human manages exceptions.**

Here we reverse the process: we design the workflow so that AI does the 'heavy lifting'. The human steps out of the daily loop and only intervenes when the AI indicates it does not know (low confidence score) or when there is an error. This is often called *Human-on-the-loop*.

- **Dynamic:** AI Execution → (Only on Error) → Human.
- **Example:** A chatbot handling customer queries independently and only escalating with upset customers.
- **Risk:** 'Silent failures' (errors not recognised as errors) and degradation of human expertise because they never do the work themselves. Output becomes sterile and generic as not enough variation between existing AI models.
- **Governance:** Strict automated monitoring and sampling (Audits).

Human oversight in this context does not mean continuous manual checking, but clear agreements about when, how and by whom to intervene in the event of deviating behaviour or exceeding established hard boundaries. Need for sufficient creative thinking to prevent generic output.

### Mode 5: Autonomous (The Entity)

**AI sets goals and acts independently.**

The system receives a broad mandate (e.g. "Optimise the purchasing inventory") and determines the sub-tasks, timing and method itself. The human role is limited to setting the frameworks (the policy) and the 'Kill Switch'.

- **Dynamic:** Human (Policy) → AI (Autonomous Execution).
- **Example:** High-frequency trading algorithms or fully autonomous supply chain planners.
- **Risk:** Unpredictable emergent behaviour and chain reactions (Flash Crashes).
- **Governance:** 'Circuit Breakers' (emergency stops) and policy constraints (what the AI is absolutely not allowed to do).

Human oversight in this context does not mean continuous manual checking, but clear agreements about when, how and by whom to intervene in the event of deviating behaviour or exceeding established hard boundaries.

______________________________________________________________________

## 3. Risk & Validation Matrix

The higher the mode, the heavier the validation requirements.

| Mode                 | Primary Validation                                  | Human Role                  | Ownership Focus  |
| :------------------- | :-------------------------------------------------- | :-------------------------- | :--------------- |
| **1. Instrumental**  | User Acceptance Testing (UAT)                       | Executor                    | Task-oriented    |
| **2. Advisory**      | Precision measurement                               | Decision-maker (Gatekeeper) | Decision-making  |
| **3. Collaborative** | Experience & Usability                              | Partner                     | Result-oriented  |
| **4. Delegated**     | Continuous Monitoring & **Performance Degradation** | Supervisor (Auditor)        | Process-oriented |
| **5. Autonomous**    | Simulation & Stress-testing                         | Policy-setter               | System-oriented  |

______________________________________________________________________

## 4. Application in Projects

When starting a project (Discovery phase), the intended mode must be recorded in the **Project Charter**.

!!! tip "Start low, scale up"

Start a use case in **Mode 2 (Advisor)** to collect data and build trust. Only when quality is proven (>90%) can you transition to **Mode 4 (Delegated)**.

!!! warning "Warning"

Do not try to jump directly to Mode 4 or 5 without the intermediate learning phases.

______________________________________________________________________

## 4b. Acceptance Criteria for Mode 4-5 (Agentic)

When a system operates in Mode 4 (Delegated) or Mode 5 (Autonomous), additional acceptance criteria apply on top of the standard Gate requirements:

**Functional Criteria:**

- [ ] Agent correctly classifies tasks in ≥ \[X%\] of cases
- [ ] Agent calls the correct tools/APIs for \[specific tasks\]
- [ ] Agent generates output in the correct format and tone

**Safety & Escalation:**

- [ ] Agent escalates ambiguous cases to a human at \[confidence threshold\]
- [ ] Escalation path is defined: agent → \[human role\] → resolution
- [ ] Humans can override agent decisions via \[mechanism\]
- [ ] Time to human review is ≤ \[X minutes\] for critical escalations

**Auditability:**

- [ ] Every agent decision is logged with: input, tools called, decision, confidence score, any human override
- [ ] Audit trail is queryable by: AI PM, compliance, support team

**Scope Boundaries (Critical):**

- [ ] Agent handles: \[specific task list\]
- [ ] Agent does NOT handle: \[excluded tasks\]
- [ ] Scope is documented in: system prompts, Hard Boundaries, tool access

**Governance:**

- [ ] Cross-functional approval: Business ☑ | Compliance ☑ | Tech ☑
- [ ] Monitoring dashboard shows: decision volume, escalation rate, override rate

______________________________________________________________________

## 5. Operating Model for Mode 4-5

When a system operates in Mode 4 or 5, the team's role shifts from execution to orchestration. The Human-Machine-Human (H-M-H) pattern describes this cycle:

```
[Human defines goal & boundaries] → [Machine executes] → [Human validates & adjusts]
```

### Team Composition for Mode 4-5

In addition to the standard [roles](../08-rollen-en-verantwoordelijkheden/index.md), the following responsibilities are critical for agentic systems:

| Responsibility          | Description                                                                  | Carried by              |
| :---------------------- | :--------------------------------------------------------------------------- | :---------------------- |
| **Goal direction**      | Defines the "why" and "what" — translates business goals into agent mandates | AI PM                   |
| **System direction**    | Optimises the human-machine system, monitors flow and learning process       | Tech Lead               |
| **Agent orchestration** | Configures orchestration patterns, tool sets and iteration limits            | Tech Lead / AI Engineer |
| **Quality assurance**   | Validates output, monitors scope boundaries and runs adversarial tests       | Guardian / AI Tester    |

### Handover Protocol: Agent to Human

Define in advance when and how an agent hands over work to a human:

- **Confidence threshold:** Agent escalates at confidence score below \[X%\].
- **Domain boundary:** Agent escalates for tasks outside the defined scope.
- **Error boundary:** Agent stops after \[N\] consecutive errors.
- **Budget boundary:** Agent stops when reaching the token or cost limit.

Every escalation is logged in the [decision trail](../08-technische-standaarden/09-agentic-ai-engineering.md).

______________________________________________________________________

## 6. Related Modules

- [Core Principles](../01-ai-native-fundamenten/01-definitie.md)
- [Validation Model](../01-ai-native-fundamenten/04-validatie-model.md)
- [Risk Management](../07-compliance-hub/02-risicobeheer/index.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Pitfalls Catalogue](../17-bijlagen/valkuilen-catalogus.md)

______________________________________________________________________
