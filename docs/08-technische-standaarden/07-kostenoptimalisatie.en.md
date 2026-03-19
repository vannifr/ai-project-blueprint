---
versie: '1.1'
pdf: false
type: technical
layer: 3
roles: [Tech Lead]
tags: [cost]
---

# Cost Optimisation

!!! abstract "Purpose"
    Concrete techniques and a cost estimation tool to keep AI system costs manageable during the Development and Operations phases.

Concrete techniques and a cost estimation tool for AI systems. Use this document in the **Development** and **Monitoring & Optimisation** phases to keep costs manageable.

______________________________________________________________________

## 1. Cost Estimation (Calculator)

Complete the table below for a quick monthly estimate.

### LLM API Costs

| Parameter                         | Your value | Example |
| :-------------------------------- | :--------- | :------ |
| Requests per day                  |            | 500     |
| Average input tokens per request  |            | 800     |
| Average output tokens per request |            | 300     |
| Price per 1M input tokens (€)     |            | €2.50   |
| Price per 1M output tokens (€)    |            | €10.00  |

```
Monthly input costs  = (requests/day × 30 × input tokens) / 1,000,000 × price
Monthly output costs = (requests/day × 30 × output tokens) / 1,000,000 × price
Total API costs/month = input costs + output costs
```

**Example:** 500 requests/day → 500 × 30 × 800 / 1,000,000 × €2.50 = **€30/month** input + 500 × 30 × 300 / 1,000,000 × €10 = **€45/month** output = **€75/month total**

### Total Monthly Cost Estimate

| Cost item                               | Monthly (€) |
| :-------------------------------------- | :---------- |
| LLM API (inference)                     |             |
| Compute (servers/GPU)                   |             |
| Storage (vector store, logs, artefacts) |             |
| Monitoring & observability tools        |             |
| Development/maintenance (internal)      |             |
| **Total**                               |             |

**Scenarios:**

| Scenario                    | Volume          | Estimated costs |
| :-------------------------- | :-------------- | :-------------- |
| Best case (low volume)      | 20% of expected |                 |
| Expected                    | 100%            |                 |
| Worst case (high volume)    | 300%            |                 |
| Scale scenario (10× growth) | 1000%           |                 |

______________________________________________________________________

## 2. Optimisation Techniques

### Technique 1 — Prompt Optimisation

**Expected saving:** 20–40% on input tokens

Unnecessary tokens in system prompts and user instructions increase costs without quality gains.

| Action                        | Approach                                                      |
| :---------------------------- | :------------------------------------------------------------ |
| Remove redundant instructions | Check for overlap between system prompt and user instructions |
| Use shorter examples          | Compress few-shot examples without quality loss               |
| System caching                | Reuse identical system prompts via provider caching           |
| Remove unnecessary context    | Send only relevant document sections, not the full document   |

______________________________________________________________________

### Technique 2 — Response Caching

**Expected saving:** 30–60% for repetitive queries

Identifiable, repeated questions (FAQ, standard reports) are cached rather than re-sent to the API.

| Cache type          | Suitable for                                 | TTL recommendation |
| :------------------ | :------------------------------------------- | :----------------- |
| **Exact match**     | Identical queries                            | 24–72 hours        |
| **Semantic match**  | Similar questions (cosine similarity > 0.95) | 6–24 hours         |
| **Template output** | Generated documents based on fixed structure | Up to 7 days       |

______________________________________________________________________

### Technique 3 — Model Tiering

**Expected saving:** 40–60% for mixed workloads

Not every question requires the heaviest (most expensive) model. Route based on complexity.

| Tier       | Model (example)           | Suitable for                                 | Relative cost |
| :--------- | :------------------------ | :------------------------------------------- | :------------ |
| **Light**  | Claude Haiku, GPT-4o mini | Classification, extraction, simple questions | 1×            |
| **Medium** | Claude Sonnet             | Analysis, summarisation, Q&A                 | 5–10×         |
| **Heavy**  | Claude Opus               | Complex reasoning, legal, medical            | 15–30×        |

**Example routing logic (Python):**

```python
def select_model(query: str, complexity_score: float) -> str:
    if complexity_score < 0.3:
        return "claude-haiku-4-5-20251001"   # Light — fast & cheap
    elif complexity_score < 0.7:
        return "claude-sonnet-4-6"           # Medium — balanced
    else:
        return "claude-opus-4-6"             # Heavy — complex reasoning
```

______________________________________________________________________

### Technique 4 — Chunking & RAG Optimisation

**Expected saving:** 20–40% on context length for document processing

| Parameter            | Suboptimal  | Optimised                      |
| :------------------- | :---------- | :----------------------------- |
| Chunk size           | 2000 tokens | 400–600 tokens                 |
| Chunks per query     | 10          | 3–5 (with reranking)           |
| Similarity threshold | 0.70        | 0.82+                          |
| Chunk compression    | No          | Yes (extractive summarisation) |

______________________________________________________________________

### Technique 5 — Batch Processing

**Expected saving:** 30–50% for non-real-time workloads

- Use Batch API endpoints (Anthropic, OpenAI offer 50% discounts)
- Schedule heavy processing outside peak hours
- Combine multiple documents in one API request where possible

______________________________________________________________________

## 3. Monitoring & Cost Management

### KPIs for Cost Management

| Metric                   | Threshold (warning) | Action                      |
| :----------------------- | :------------------ | :-------------------------- |
| Cost per successful task | > 2× baseline       | Investigate model tiering   |
| Token usage per request  | > 130% of average   | Prompt optimisation         |
| Cache hit rate           | \< 20%              | Increase TTL or cache scope |
| Cost/month vs. budget    | > 80% of budget     | Review and adjust           |

### Budget Alert Configuration

Always configure budget alerts at:

- **70%** of monthly budget → warning notification
- **90%** of monthly budget → escalation to AI PM + CAIO
- **100%** of monthly budget → automatic rate limiting or stop

### Cost Allocation

Allocate costs per system, team or use case via tags/labels in your cloud environment. This enables ROI calculation per project (see [Benefits Realisation](../10-doorlopende-verbetering/04-batenrealisatie.md)).

______________________________________________________________________

## 4. Cost Optimisation per Phase

| Phase           | Priority | Action                                                                  |
| :-------------- | :------- | :---------------------------------------------------------------------- |
| **Discovery**   | Basic    | Use light model for prototyping; set budget cap                         |
| **Validation**  | Basic    | Measure cost per test case; calculate monthly cost at production volume |
| **Development** | High     | Implement caching and model tiering; set up monitoring                  |
| **Delivery**    | High     | Validate costs vs. Business Case; automate budget alerts                |
| **Monitoring**  | Ongoing  | Review monthly; optimise when > 10% deviation from baseline             |

______________________________________________________________________

## Related Modules

- [Cloud vs. On-Premise](06-cloud-vs-onpremise.md)
- [MLOps Standards](01-mloops-standaarden.md)
- [Benefits Realisation](../10-doorlopende-verbetering/04-batenrealisatie.md)
- [Business Case Template](../09-sjablonen/02-business-case/template.md)
- [Agentic AI Engineering — Cost Management](09-agentic-ai-engineering.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
