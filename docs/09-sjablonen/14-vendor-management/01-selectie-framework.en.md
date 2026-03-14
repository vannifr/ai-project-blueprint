---
versie: '1.0'
pdf: false
type: template
layer: 3
phase: [2, 3]
tags: [template, vendor]
---

# Vendor Selection Framework

Structured approach for evaluating and selecting AI vendors. Follow the steps in order.

______________________________________________________________________

## Step 1 — Define Requirements

First define your minimum requirements (knock-out criteria) and desired properties (wishes).

### Knock-out Criteria

| Requirement           | Notes                                                            |
| :-------------------- | :--------------------------------------------------------------- |
| GDPR compliance       | Processing within EU or adequacy decision                        |
| Uptime SLA            | Minimum \[x\]% (e.g. 99.5%)                                      |
| Data retention policy | No permanent storage of prompts/outputs unless explicitly agreed |
| Supported languages   | \[languages\]                                                    |
| Pricing model         | \[token-based / subscription / pay-per-use\]                     |

Vendors that do **not** meet knock-out criteria are immediately excluded.

### Desired Properties (Weighted)

| Property                           | Weight (1–5) | Notes |
| :--------------------------------- | :----------- | :---- |
| Output quality                     |              |       |
| Latency (response time)            |              |       |
| Documentation & support            |              |       |
| Ecosystem & integrations           |              |       |
| Pricing flexibility / discounts    |              |       |
| Transparency about model behaviour |              |       |
| Innovation velocity                |              |       |

______________________________________________________________________

## Step 2 — Compile Longlist

| Vendor          | Type           | Primary product               | In scope? |
| :-------------- | :------------- | :---------------------------- | :-------- |
| Anthropic       | API            | Claude (Haiku/Sonnet/Opus)    | ☐         |
| OpenAI          | API            | GPT-4o / o1                   | ☐         |
| Google          | API / Platform | Gemini / Vertex AI            | ☐         |
| Microsoft Azure | Platform       | OpenAI-as-a-service, Azure ML | ☐         |
| AWS             | Platform       | Bedrock, SageMaker            | ☐         |
| Mistral AI      | API            | Mistral models                | ☐         |
| Cohere          | API            | Command / Embed               | ☐         |
| \[Other\]       |                |                               | ☐         |

______________________________________________________________________

## Step 3 — Shortlist Scorecard

Give each vendor on the shortlist a score (1–5) per property and multiply by the weight.

### Scorecard

| Property        | Weight | \[Vendor A\] | \[Vendor B\] | \[Vendor C\] |
| :-------------- | :----- | :----------- | :----------- | :----------- |
| Output quality  |        |              |              |              |
| Latency         |        |              |              |              |
| Documentation   |        |              |              |              |
| Ecosystem       |        |              |              |              |
| Price           |        |              |              |              |
| Transparency    |        |              |              |              |
| Innovation      |        |              |              |              |
| **Total score** |        |              |              |              |

### PoC Results (optional)

| Test                 | \[Vendor A\] | \[Vendor B\] | \[Vendor C\] |
| :------------------- | :----------- | :----------- | :----------- |
| Task type 1          |              |              |              |
| Task type 2          |              |              |              |
| Latency p95          |              |              |              |
| Cost per 1K requests |              |              |              |

______________________________________________________________________

## Step 4 — Recommendation

**Selected vendor:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Reason for choice:**

> _Brief rationale (3–5 sentences)._

**Risks of this choice:**

| Risk           | Mitigation                                      |
| :------------- | :---------------------------------------------- |
| Vendor lock-in | Build abstraction layer / multi-vendor strategy |
| Price increase | Contractual price cap or prepare alternative    |
| Availability   | Define fallback to second vendor                |

**Approval:**

| Role           | Name | Date | Signature |
| :------------- | :--- | :--- | :-------- |
| AI PM          |      |      |           |
| Tech Lead      |      |      |           |
| CAIO / Sponsor |      |      |           |

______________________________________________________________________

## Related Modules

- [RFP Template](02-rfp-template.md)
- [Contract Checklist](03-contract-checklist.md)
- [Cloud vs. On-Premise](../../08-technische-standaarden/06-cloud-vs-onpremise.md)
- [Business Case](../02-business-case/template.md)
