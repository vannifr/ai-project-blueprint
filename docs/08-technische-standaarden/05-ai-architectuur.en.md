---
versie: '1.0'
type: technical
layer: 3
roles: [Tech Lead]
---

# 1. AI Architecture

## 1. Purpose

This module describes the most common architecture patterns for AI systems and the considerations when choosing the right approach. Good architecture balances functionality, scalability, cost and security.

______________________________________________________________________

## 2. Basic Architecture: The AI Stack

Every AI solution consists of a number of layers that work together:

```
┌─────────────────────────────────────────┐
│ User Interface    │ Web, App, API, Chat
├─────────────────────────────────────────┤
│ Orchestration Layer │ Routing, workflow, caching
├─────────────────────────────────────────┤
│ AI Core (Model)   │ LLM, classifier, etc.
├─────────────────────────────────────────┤
│ Knowledge Coupling (RAG) │ Vectorstore, documents
├─────────────────────────────────────────┤
│ Data Layer        │ Databases, logging, storage
└─────────────────────────────────────────┘
```

______________________________________________________________________

## 3. Reference Architectures

### Pattern A: Direct LLM Integration

**Description:** User communicates directly with an LLM via a simple interface.

```
[User] → [API Gateway] → [LLM Provider] → [Response]
```

**Characteristics:**

| Aspect         | Value                                    |
| -------------- | ---------------------------------------- |
| Complexity     | Low                                      |
| Cost           | Variable (per API call)                  |
| Latency        | Dependent on provider                    |
| Data isolation | Data goes to external provider           |
| Suitable for   | Prototypes, internal tools, Minimal risk |

**Considerations:**

- Ensure rate limiting and cost monitoring
- Log all interactions according to [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- Implement Hard Boundaries via system prompts

### Pattern B: Knowledge Coupling (RAG)

**Description:** LLM is enriched with company-specific information from a knowledge base.

```
[User] → [Orchestration] → [Vectorstore Query] → [Context + Prompt] → [LLM] → [Response]
```

**Characteristics:**

| Aspect         | Value                                      |
| -------------- | ------------------------------------------ |
| Complexity     | Medium                                     |
| Cost           | Vectorstore + LLM API                      |
| Latency        | Higher (extra query step)                  |
| Data isolation | Knowledge base can remain internal         |
| Suitable for   | Customer service, documentation assistants |

**Components:**

- **Document Processor:** Splits documents into chunks
- **Embedding Model:** Converts text to vectors
- **Vectorstore:** Stores and searches vectors (Pinecone, Weaviate, pgvector)
- **Retriever:** Retrieves relevant context based on query
- **LLM:** Generates response with context

**Considerations:**

- Chunk size affects quality and cost
- Embedding model must fit language and domain
- Log source references for traceability

### Pattern C: Agentic AI (Autonomous Systems)

**Description:** AI system that independently executes tasks, calls tools and makes decisions.

```
[User/Trigger] → [Agent Orchestrator] → [Decide] → [Call Tool] → [Evaluate] → [Next Step or Response]
```

**Characteristics:**

| Aspect         | Value                                   |
| -------------- | --------------------------------------- |
| Complexity     | High                                    |
| Cost           | Variable, can escalate quickly          |
| Latency        | Variable (multiple steps)               |
| Data isolation | Dependent on tools                      |
| Suitable for   | Automation, research, complex workflows |

**Requirements (Collaboration Mode 4-5):**

- **Action radius restriction:** Define which tools are available
- **Budget limits:** Maximum cost per task
- **Circuit Breaker:** Automatic stop on deviant behaviour
- **Human escalation:** Define when a human must intervene
- **Extended logging:** Record every decision and action

**Considerations:**

- Start with limited action radius, expand gradually
- Test extensively with adversarial scenarios
- Guardian review mandatory for High Risk

#### Technically Enforceable Controls (Mandatory for Collaboration Mode 4–5)

For agentic AI systems that perform actions autonomously, the following technical controls are mandatory.

| Control                                | Description                                                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Tool allowlist                         | Explicit list of permitted tools; unauthorised tools are blocked.                                                            |
| Capability-based access control (CBAC) | Access rights are granted based on capabilities (what is permitted), optionally on top of RBAC (who is it).                  |
| Sandboxed tool execution               | Tools are executed in an isolated environment without direct access to production systems.                                   |
| Just-in-time permissions               | Rights are granted only at the moment of execution and for the minimum required scope.                                       |
| Per-task budget/spend limit            | Maximum cost or resources per individual task or session.                                                                    |
| Deny-by-default network egress         | Outgoing network traffic is blocked by default; only explicit destinations are permitted.                                    |
| Hard Budget Cap (Cost Hard Boundary)   | Technical limit on API costs per day/month (via API gateway or provider). Prevents "bill shock" from infinite loops or DDoS. |
| Rate Limiting                          | Maximum number of requests per user per minute. Protects against misuse and cost explosion.                                  |

Source: \[so-1\]

______________________________________________________________________

## 4. Architecture Decisions

### Cloud vs On-Premise

| Factor            | Cloud (API)                  | On-Premise / Private Cloud  |
| ----------------- | ---------------------------- | --------------------------- |
| Start-up costs    | Low                          | High                        |
| Operational costs | Variable per use             | Fixed (infra + maintenance) |
| Scalability       | Automatic                    | Manual                      |
| Data sovereignty  | Data goes to provider        | Data stays internal         |
| Latency           | Dependent on network         | Potentially lower           |
| Suitable for      | Prototypes, variable volumes | Strict privacy, high volume |

### Model Choice

| Consideration  | Foundation Model (GPT, Claude) | Fine-tuned / Custom Model     |
| -------------- | ------------------------------ | ----------------------------- |
| Time to live   | Fast (days)                    | Slow (weeks-months)           |
| Flexibility    | High, broadly applicable       | Optimised for specific task   |
| Cost per query | Higher                         | Potentially lower             |
| Maintenance    | Provider responsible           | Team responsible              |
| Suitable for   | Generic tasks, prototypes      | High volume, specialist tasks |

______________________________________________________________________

## 5. Security Architecture

### Minimum Security Layers

| Layer            | Measure                              |
| ---------------- | ------------------------------------ |
| Network          | HTTPS, API gateway, firewall         |
| Authentication   | API keys, OAuth, service accounts    |
| Authorisation    | Role-based access (who may do what?) |
| Input validation | Sanitisation, length limits          |
| Output filtering | PII detection, content filtering     |
| Logging          | Audit trail per Evidence Standards   |

### Specific to AI

- **Prompt injection protection:** Separation of system/user prompts
- **Rate limiting:** Per user and total
- **Cost monitoring:** Alerts on unexpectedly high usage
- **Model access:** Restricted access to production models

______________________________________________________________________

## 6. Scalability

### Typical Bottlenecks

| Component     | Bottleneck                        | Solution                   |
| ------------- | --------------------------------- | -------------------------- |
| LLM API       | Rate limits, cost                 | Caching, batching, queuing |
| Vectorstore   | Query latency with many documents | Indexing, sharding         |
| Orchestration | Complex workflows                 | Async processing, workers  |

### Scaling Strategies

| Strategy         | When to Apply                        |
| ---------------- | ------------------------------------ |
| Response caching | Repetitive questions, static content |
| Semantic caching | Similar questions                    |
| Batching         | Many concurrent requests             |
| Model tiering    | Simple questions to cheaper model    |

______________________________________________________________________

## 7. Architecture Checklist

!!! check "7. Architecture Checklist"
    - [ ] Architecture pattern is chosen and documented
    - [ ] Security layers are implemented
    - [ ] Scalability is considered
    - [ ] Cost estimate is made
    - [ ] Logging and monitoring are set up
    - [ ] Hard Boundaries are implemented in the architecture
    - [ ] Rollback strategy is defined

______________________________________________________________________

## 8. Related Modules

- [Technical Standards & Delivery Criteria](01-mloops-standaarden.md)
- [Model Governance](03-model-governance.md)
- [Risk Management & Compliance](../07-compliance-hub/index.md)
- [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
