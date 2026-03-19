---
versie: '1.1'
type: technical
layer: 3
roles: [Tech Lead]
tags: [governance, security, mlops]
---

# 1. Agentic AI Engineering

## 1. Purpose

This module describes the engineering practices for building, testing and managing agentic AI systems (Collaboration Mode 4-5). Where [AI Architecture](05-ai-architectuur.md) defines the strategic pattern, this document provides the operational guide: orchestration, protocols, tool design, failure modes, observability and cost management.

!!! warning "Prerequisite"
    First read [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md) and the [acceptance criteria for Mode 4-5](../00-strategisch-kader/06-has-h-niveaus.md#4b-acceptance-criteria-for-mode-4-5-agentic). Every technical choice in this document is determined by the mode and risk profile.

______________________________________________________________________

## 2. Orchestration Patterns

An agent system selects an orchestration pattern based on task complexity and risk. Always start with the simplest pattern that works.

### Single Agent

```
[User/Trigger] → [Agent + Tools] → [Result]
```

One LLM with direct access to a set of tools. Suitable for well-scoped tasks with limited action radius.

**When to use:** Tasks with a clear goal, limited tool set, low to moderate complexity.

### Multi-Agent (Supervisor)

```
[Trigger] → [Supervisor Agent] → [Specialist Agent A] → [Result A]
                                → [Specialist Agent B] → [Result B]
                                → [Merge] → [Final Result]
```

A supervisor agent distributes work across specialised sub-agents. Each sub-agent has a scoped mandate and its own tool set.

**When to use:** Complex tasks requiring multiple areas of expertise, or tasks that can be parallelised.

### Handoff Pattern

```
[Agent A] → [Handoff Point] → [Agent B] → [Handoff Point] → [Agent C]
```

Responsibility transfers between agents as the context evolves. Each agent processes a specific phase.

**When to use:** Sequential workflows with clear phase boundaries (e.g. analysis → plan → execution → review).

### Selection Matrix

| Pattern      | Complexity | Risk          | Cost     | Recommended for              |
| :----------- | :--------- | :------------ | :------- | :--------------------------- |
| Single Agent | Low        | Low-Moderate  | Lowest   | Well-scoped tasks, Mode 4    |
| Supervisor   | High       | Moderate-High | Higher   | Parallel expertise, Mode 4-5 |
| Handoff      | Moderate   | Moderate      | Moderate | Sequential workflows, Mode 4 |

______________________________________________________________________

## 3. Protocols and Standards

### Model Context Protocol (MCP)

MCP is an open standard (Anthropic, 2024) that defines how agents connect to external tools, data sources and APIs. MCP provides:

- **Standardised tool descriptions:** Tools are described in a uniform schema so that any MCP-compatible agent can invoke them.
- **Transport layers:** Stdio (local) and Streamable HTTP (network).
- **Security model:** Server identity, capability registration and permission management.

**Recommendation:** Design new internal APIs with MCP compatibility. This prevents vendor lock-in and makes tools reusable across agent frameworks.

### Agent-to-Agent (A2A) Protocol

A2A (Google, 2025; Linux Foundation) is an open standard for communication between agents from different frameworks or vendors. Agents publish their capabilities and negotiate interaction modalities.

**When relevant:** In multi-agent systems that combine agents from different teams or vendors.

______________________________________________________________________

## 4. Tool Design for Agents

### Design Principles

1. **Allowlist-first:** Only explicitly permitted tools are available. Deny-by-default.
1. **Progressive disclosure:** Give the agent a short tool index; load extended descriptions only when needed. This limits token consumption.
1. **Atomic actions:** Each tool does exactly one thing. Do not combine "read and write" in a single tool.
1. **Idempotent where possible:** Repeated invocation of the same tool with the same input should have no side effects.
1. **Sandbox execution:** Tools run in an isolated environment without direct access to production data (see [Technical Controls](05-ai-architectuur.md#technically-enforceable-controls-mandatory-for-collaboration-mode-4-5)).

### Code Execution Pattern

Instead of direct tool invocations, an agent can write code that calls tools. This offers:

- On-demand tool loading (lower baseline token costs)
- Complex logic in a single step (filtering, transformation)
- Better traceability (code is inspectable)

**Risk:** Requires strict sandboxing. Use only with Mode 5 governance.

______________________________________________________________________

## 5. Agent Memory

Agents that perform long-running tasks or work across multiple sessions require memory. We distinguish four types:

| Type             | Description                                                                 | Storage Medium        | Example                                             |
| :--------------- | :-------------------------------------------------------------------------- | :-------------------- | :-------------------------------------------------- |
| **Token memory** | Context window contents (system prompt, conversation history, tool results) | In-context            | Running conversation                                |
| **Episodic**     | Specific events: what happened, when, with what result                      | Database/file         | "Previous deployment failed due to schema mismatch" |
| **Semantic**     | General knowledge, facts, relationships                                     | Knowledge base/RAG    | Company policy, product documentation               |
| **Procedural**   | Learned skills and operational knowledge                                    | Configuration/prompts | Optimal sequence of deployment steps                |

**Recommendation:** Start with token memory + RAG (semantic). Only add episodic memory when the agent performs recurring tasks and needs to learn from previous results.

______________________________________________________________________

## 6. Failure Modes and Mitigation

Agentic systems fail qualitatively differently from traditional software. The patterns below require specific mitigation.

| Failure Mode                 | Description                                                          | Impact                                 | Mitigation                                                                       |
| :--------------------------- | :------------------------------------------------------------------- | :------------------------------------- | :------------------------------------------------------------------------------- |
| **Infinite loop**            | Agent continuously generates subtasks or repeats the same action     | Cost explosion, system load            | Hard iteration limit per task; Circuit Breaker on token budget                   |
| **Hallucination escalation** | Hallucinated output becomes input for the next step, errors compound | Unreliable results that appear correct | Multi-step validation; intermediate fact-checks; cross-validation between models |
| **Scope creep**              | Agent interprets mandate more broadly than intended                  | Unauthorised actions                   | Explicit scope boundaries in system prompt + tool allowlist                      |
| **Tool misuse**              | Agent invokes tools in unintended combinations or sequences          | Data corruption, unwanted side effects | Log and validate tool invocations against permitted sequences                    |
| **Cascade failure**          | Error in sub-agent propagates through the entire system              | System-wide disruption                 | Isolation per agent; error boundaries; graceful degradation                      |
| **Silent degradation**       | Quality gradually declines without visible error messages            | Unnoticed poor output                  | Periodic Golden Set validation; acceptance rate monitoring                       |

!!! tip "Rule of thumb"
    Every failure mode must have a corresponding alert in the [monitoring dashboard](../10-doorlopende-verbetering/03-metrics-dashboards.md). No mitigation without a measurable signal.

______________________________________________________________________

## 7. Observability

### Why Agent Observability Is Different

Traditional monitoring measures **what** happens (latency, errors, throughput). Agent observability must also measure **why** something happens: what decisions did the agent make, which tools did it invoke, and what was the reasoning?

### Minimum Telemetry

| Data Point            | Description                                                 | Purpose                        |
| :-------------------- | :---------------------------------------------------------- | :----------------------------- |
| **Decision trail**    | Per step: input, reasoning, chosen action, confidence score | Audit, debugging               |
| **Tool invocations**  | Which tool, with which parameters, result, duration         | Cost analysis, fault detection |
| **Escalation events** | When and why the agent escalated to a human                 | Scope validation               |
| **Token consumption** | Per step and per session                                    | Cost management                |
| **Session outcome**   | Success/fail, elapsed time, number of steps                 | Quality monitoring             |

### OpenTelemetry

OpenTelemetry has established standardised semantic conventions for AI agent observability. Use these conventions to implement vendor-independent tracing. This makes it possible to analyse agent behaviour regardless of the underlying framework.

______________________________________________________________________

## 8. Cost Management

Agentic systems have a fundamentally different cost model from traditional AI applications. Usage costs account for only approximately 20% of total cost of ownership.

### TCO Structure

| Cost Category                    | Share | Control Measure                        |
| :------------------------------- | :---- | :------------------------------------- |
| Inference (API tokens)           | ~20%  | Prompt caching, model tiering          |
| Data preparation and integration | ~25%  | Standardised pipelines                 |
| Governance and compliance        | ~20%  | Proportional governance per risk level |
| Monitoring and tuning            | ~15%  | Automated alerts, SLO monitoring       |
| Training and onboarding          | ~20%  | Reusable patterns and documentation    |

### Optimisation Techniques

- **Prompt caching:** If an agent always uses the same system prompt, the provider can cache those tokens. Reduces input costs by ~90% and latency by ~75%.
- **Model tiering:** Route simple tasks to a cheaper model; complex tasks to a more capable model.
- **Dynamic iteration limits:** Set the maximum number of steps based on task complexity, not as a fixed number.
- **Hard budget cap:** Technical limit per task/session/day (see [Technical Controls](05-ai-architectuur.md#technically-enforceable-controls-mandatory-for-collaboration-mode-4-5)).

______________________________________________________________________

## 9. Agent Testing

### Test Strategy

Agent testing goes beyond functional tests. We test across four dimensions:

| Dimension       | What to Test                                               | Method                         |
| :-------------- | :--------------------------------------------------------- | :----------------------------- |
| **Quality**     | Task completion, correct tool selection, reasoning quality | Golden Set scenarios           |
| **Performance** | Latency, throughput, resource usage                        | Load tests                     |
| **Safety**      | Prompt injection, scope violation, tool misuse             | Adversarial tests, red teaming |
| **Cost**        | Token consumption per task, cost per successful result     | Cost benchmarks                |

### Adversarial Scenarios (mandatory for Mode 4-5)

- **Scope test:** Give the agent an assignment outside its mandate. Expected: refusal or escalation.
- **Loop test:** Create a situation that could lead to infinite repetition. Expected: stop after iteration limit.
- **Conflicting instructions:** Provide contradictory context. Expected: escalation, not guessing.
- **Tool misuse:** Offer tools the agent should not use. Expected: no invocation.

______________________________________________________________________

## 10. Agentic AI Engineering Checklist

!!! check "10. Agentic AI Engineering Checklist"
    - [ ] Orchestration pattern is selected and documented
    - [ ] Tool allowlist is defined and enforced
    - [ ] Sandbox environment is set up for tool execution
    - [ ] Iteration limits and budget caps are configured
    - [ ] Failure modes are identified with corresponding alerts
    - [ ] Decision trail (audit trail) is active per agent step
    - [ ] Escalation path to human is defined and tested
    - [ ] Adversarial tests are completed and documented
    - [ ] Cost model is established (TCO, not just inference)
    - [ ] OpenTelemetry or equivalent tracing is implemented

______________________________________________________________________

## 11. Related Modules

- [AI Architecture — Pattern C: Agentic AI](05-ai-architectuur.md)
- [AI Collaboration Modes (Mode 4-5)](../00-strategisch-kader/06-has-h-niveaus.md)
- [AI Safety Checklist](../07-compliance-hub/08-ai-safety-checklist.md)
- [Red Teaming](../07-compliance-hub/07-red-teaming.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
- [Cost Optimisation](07-kostenoptimalisatie.md)

______________________________________________________________________
