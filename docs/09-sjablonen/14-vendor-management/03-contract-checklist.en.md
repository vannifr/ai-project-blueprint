---
versie: '1.0'
pdf: false
type: template
layer: 3
phase: [2, 3]
tags: [gate-review, template, vendor]
answers: [How do I use the Contract Checklist — AI Vendors template?]
---

# Contract Checklist — AI Vendors

Verification list for AI-specific contract requirements. Use during contract negotiation with external AI vendors.

!!! warning "Legal advice"
    This checklist is a tool, not legal advice. Consult your legal department or external counsel for high-value contracts or complex AI risks.

______________________________________________________________________

## Section 1 — Data Processing Agreement (DPA)

| Requirement                                      | Status | Note |
| :----------------------------------------------- | :----- | :--- |
| DPA present and signed                           | ☐      |      |
| Processing purposes explicitly defined           | ☐      |      |
| Data location recorded (EU / country)            | ☐      |      |
| Sub-processors documented and approved           | ☐      |      |
| Data retention period specified                  | ☐      |      |
| Data breach procedure (notify within 72h)        | ☐      |      |
| Audit rights of controller established           | ☐      |      |
| Data subject rights (access, deletion) addressed | ☐      |      |

______________________________________________________________________

## Section 2 — AI-specific Provisions

| Requirement                                                                | Status | Note |
| :------------------------------------------------------------------------- | :----- | :--- |
| Prohibition on using prompts/outputs for model training (unless permitted) | ☐      |      |
| Model update policy: advance notice of changes                             | ☐      |      |
| Deprecation policy: minimum notice period \[e.g. 6 months\]                | ☐      |      |
| Version pinning: ability to pin to specific model version                  | ☐      |      |
| Transparency about model behaviour and known limitations                   | ☐      |      |
| Liability for harmful outputs clarified                                    | ☐      |      |
| Intellectual property of outputs addressed                                 | ☐      |      |

______________________________________________________________________

## Section 3 — Service Level Agreement (SLA)

| Requirement                                                                                                      | Status | Note |
| :--------------------------------------------------------------------------------------------------------------- | :----- | :--- |
| Uptime SLA established (e.g. 99.5%)                                                                              | ☐      |      |
| Uptime measurement method defined                                                                                | ☐      |      |
| Penalty clause for SLA breach                                                                                    | ☐      |      |
| Latency guarantees (p95, p99) specified (p95 = 95th percentile — 95% of all requests are faster than this value) | ☐      |      |
| Capacity guarantees (rate limits) established                                                                    | ☐      |      |
| Incident procedure and communication channels described                                                          | ☐      |      |
| Status page and incident notifications arranged                                                                  | ☐      |      |

______________________________________________________________________

## Section 4 — Security & Compliance

| Requirement                                             | Status | Note |
| :------------------------------------------------------ | :----- | :--- |
| ISO 27001 / SOC 2 certification present                 | ☐      |      |
| Penetration test report recent (\< 1 year) available    | ☐      |      |
| Encryption in transit (TLS 1.2+) guaranteed             | ☐      |      |
| Encryption at rest guaranteed                           | ☐      |      |
| Access control and least-privilege described            | ☐      |      |
| EU AI Act compliance position described (if applicable) | ☐      |      |
| Vendor Responsible Disclosure policy present            | ☐      |      |

______________________________________________________________________

## Section 5 — Commercial Terms

| Requirement                                            | Status | Note |
| :----------------------------------------------------- | :----- | :--- |
| Pricing model and units clearly defined                | ☐      |      |
| Price change clause: notice period ≥ \[e.g. 90 days\]  | ☐      |      |
| Maximum annual price increase established              | ☐      |      |
| Termination notice period and exit procedure described | ☐      |      |
| Data portability upon termination arranged             | ☐      |      |
| Liability cap established                              | ☐      |      |
| Applicable law and jurisdiction determined             | ☐      |      |

______________________________________________________________________

## Summary

| Section         | Items  | Checked | %   |
| :-------------- | :----- | :------ | :-- |
| 1 — DPA         | 8      |         |     |
| 2 — AI-specific | 7      |         |     |
| 3 — SLA         | 7      |         |     |
| 4 — Security    | 7      |         |     |
| 5 — Commercial  | 7      |         |     |
| **Total**       | **36** |         |     |

**Recommendation:** Only sign the contract at ≥ 90% score (≥ 33/36). Document outstanding items as risks in the risk register.

**Reviewed by:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## Related Modules

- [Selection Framework](01-selectie-framework.md)
- [RFP Template](02-rfp-template.md)
- [Risk Analysis](../03-risicoanalyse/template.md)
- [EU AI Act](../../07-compliance-hub/01-eu-ai-act/index.md)
