---
pdf: false
versie: '1.1'
description: Case studies of AI projects — documented public cases and conceptual scenarios at different risk levels.
type: reference
layer: 3
answers: [What is Case Studies?]
---

# Case Studies

!!! warning "Disclaimer"
    This page contains two types of examples: **documented public cases** (with source citations) and **conceptual scenarios** (anonymised, illustrating Blueprint application). Each example is clearly labelled. Sources are cited where available.

______________________________________________________________________

## Part A — Documented Public Cases

### Case 1 — Amazon Automated Hiring System (2014–2018) { #case-amazon-hiring }

!!! example "Bias in automated recruitment — High Risk"

**Context:** Starting in 2014, Amazon developed an internal AI system to screen CVs and rank candidates for technical positions. The model was trained on historical hiring data from the previous 10 years.

**What happened:** The system learned patterns from historical data in which men were overrepresented in technical roles. The model penalised CVs containing the word "women's" (e.g. "women's chess club captain") and favoured male-associated language patterns. Amazon discovered the problem internally, attempted to correct the model, but could not guarantee the system would not develop other forms of discrimination. The project was discontinued in 2018.

**Blueprint lesson:**

- **Fairness audit** (Validation phase): systematic bias testing before production would have exposed the problem earlier.
- **Red Lines** (Hard Boundaries): proxy discrimination is an unacceptable risk that automatically triggers a stop decision.
- **Guardian Review**: classification as High Risk (EU AI Act Annex III, point 4a — recruitment) would have activated the full compliance trajectory.

**Source:** Reuters, "Amazon scraps secret AI recruiting tool that showed bias against women", 10 October 2018.

______________________________________________________________________

### Case 2 — Microsoft Tay Chatbot (2016) { #case-microsoft-tay }

!!! example "Unprotected AI in a public environment — Reputational risk"

**Context:** In March 2016, Microsoft launched "Tay", an experimental Twitter chatbot designed to learn from interactions with users. The goal was to test conversational AI in a public setting.

**What happened:** Within 16 hours of launch, Tay began generating racist, sexist and offensive messages. Users discovered they could manipulate the bot by repeating offensive content. Microsoft took Tay offline within 24 hours.

**Blueprint lesson:**

- **Hard Boundaries** (Goal card): defining explicit output boundaries and prohibited topics would have limited the damage.
- **Red Teaming** (Compliance Hub): adversarial testing before launch would have exposed the manipulability.
- **Mode 2/3 instead of Mode 4**: a collaborative model with human review would have filtered unacceptable output.

**Source:** Microsoft Official Blog, "Learning from Tay's introduction", 25 March 2016.

______________________________________________________________________

### Case 3 — Air Canada Chatbot Legal Case (2024) { #case-air-canada-chatbot }

!!! example "Legal liability for AI output — Limited Risk"

**Context:** A passenger of Air Canada used the website chatbot to ask about the bereavement policy for flight tickets. The chatbot provided incorrect information: it promised the passenger could retroactively apply for a discount after booking a full-fare ticket.

**What happened:** When the passenger applied for the discount, Air Canada refused, arguing that the chatbot had provided incorrect information. The passenger took the case to the Canadian Civil Resolution Tribunal. In February 2024, the tribunal ruled that Air Canada is responsible for all information on its website, including output from its chatbot. Air Canada was ordered to pay the discount plus interest.

**Blueprint lesson:**

- **Validation report** (Validation phase): the Golden Set should have included representative customer queries about the bereavement policy.
- **Transparency obligation** (EU AI Act Art. 50): users must know they are communicating with an AI and understand its limitations.
- **Incident Response** (Compliance Hub): a clear escalation path could have caught the problem before it became a legal matter.
- **Mode 3** (Collaborative): route complex customer queries to a human agent rather than answering autonomously.

**Source:** Moffatt v Air Canada, 2024 BCCRT 149, Canadian Civil Resolution Tribunal, 14 February 2024.

______________________________________________________________________

### Case 4 — Italian Regulator Blocks ChatGPT (2023) { #case-italy-chatgpt }

!!! example "Privacy enforcement for AI systems — Regulatory risk"

**Context:** In March 2023, the Italian data protection authority (Garante per la protezione dei dati personali) temporarily blocked ChatGPT in Italy for alleged violations of the GDPR.

**What happened:** The Garante identified four concerns: (1) no legal basis for mass processing of personal data for model training, (2) inaccurate information about individuals (hallucinations), (3) no age verification for minors, and (4) insufficient transparency towards users. OpenAI implemented improvements within a month — including a training opt-out, age verification, and an improved privacy policy — after which the block was lifted. In December 2024, the Garante imposed a fine of EUR 15 million on OpenAI.

**Blueprint lesson:**

- **Privacy-by-Design** (DPIA in Discovery phase): privacy risks must be addressed from day 1.
- **Guardian Review**: classification and compliance check before a system is offered to users.
- **Hard Boundaries**: output filters for personal data and age restrictions as standard components.

**Source:** Garante per la protezione dei dati personali, Provvedimento del 30 marzo 2023 \[9870832\]; Garante, Provvedimento del 20 December 2024.

______________________________________________________________________

### Case 5 — DORA State of AI: Production Threshold (2025) { #case-dora-production }

!!! example "AI projects fail to reach production — Strategic risk"

**Context:** The DORA (DevOps Research and Assessment) report on GenAI \[so-28\] documents a recurring pattern in the industry: organisations start AI projects but fail to bring them to production. Gartner, VentureBeat, and S&P Global \[so-51\] report failure and abandonment rates of 30–85% for AI projects.

**What happened:** The research identifies common causes: missing governance, unclear success criteria, technical debt, lack of human oversight, and the absence of a structured validation process. Projects that succeed significantly more often have clear gates, defined roles, and an iterative validation process.

**Blueprint lesson:**

- **Gate Reviews** (Governance Model): phased go/no-go decisions prevent projects from proceeding without validation.
- **Project Charter** (Discovery phase): clear success criteria and scope definition from the start.
- **90-Day Roadmap**: structured approach for organisations seeking to increase their AI maturity.

**Source:** DORA GenAI Report v2025.2 \[so-28\]; Gartner, VentureBeat, S&P Global — AI Production Surveys (2019–2024) \[so-51\].

______________________________________________________________________

## Part B — Conceptual Scenarios

!!! info "About these scenarios"
    The following examples are **conceptual scenarios** — anonymised illustrations of how the Blueprint is applied at different risk levels. They are based on common patterns in practice but do not refer to specific organisations.

### Scenario 1 — Minimal Risk: Internal Knowledge Bot (Government) { #scenario-knowledge-bot }

!!! example "Conceptual example — Fast Lane application"

**Sector:** Government — municipal services
**Risk class:** Minimal Risk (Mode 2 — Advisory)
**Blueprint components used:** Explorer Kit, Project Charter, Goal card, Validation report

**Situation:** A mid-sized municipality wanted to help employees quickly find answers in internal policy documents and process descriptions. The call centre needed an average of 40 minutes per complex query; much time was lost searching for information in an outdated intranet.

**Approach:** The project team used the **Fast Lane** (6 weeks) because the risk class was Minimal: no personal data, no external decisions, fully internal use. The Goal card defined the intent as "employee finds the correct policy document within 2 minutes". Hard Boundaries restricted the system to internal documents and prohibited answers to legal or medical questions.

The PoV lasted 2 weeks and tested 50 representative questions (the Golden Set). After validation (89% correct references) the system was rolled out to 3 pilot departments.

**Result:** Average search time fell from 40 to 6 minutes. Adoption after 8 weeks: 74% of employees use the system daily. No incidents reported. The system operates in **Mode 2**: each employee evaluates the answer themselves before using it.

*Conceptual example — names and figures are illustrative.*

______________________________________________________________________

### Scenario 2 — Limited Risk: Customer Service Automation (Financial Services) { #scenario-customer-service }

!!! example "Conceptual example — Full lifecycle with Fairness audit"

**Sector:** Financial services — insurer
**Risk class:** Limited Risk (Mode 3 — Collaborative)
**Blueprint components used:** Full lifecycle (13 weeks), Business Case, Fairness audit (bias audit), Guardian Review, Validation report

**Situation:** A mid-sized insurer received 12,000 customer queries per month by email, of which 60% were routine (policy status, payment confirmations, address changes). The processing team of 8 employees consistently worked with a backlog.

**Approach:** The Guardian classified the system as Limited Risk: customers communicate with an AI but take the action themselves (no automatic decisions). Transparency obligation: customers are informed that they are communicating with an AI assistant.

The **Fairness audit (bias audit)** tested whether customer queries in simpler language (lower literacy level, non-native speakers) received equivalent response quality. An initial problem with formal language use was corrected in the prompt revision of week 8.

The Business Case demonstrated an ROI of 340% over 18 months. Gate 2 (investment decision) was made based on the Validation report after the PoV: 91% correct routing, 0 privacy incidents.

**Result:** Processing time for routine queries fell from 4 hours to 12 minutes per batch. The team of 8 was redeployed to handle complex complaints. Customer satisfaction (NPS) rose by 12 points. The system operates in **Mode 3**: the AI drafts a response, an employee approves before sending.

*Conceptual example — names and figures are illustrative.*

______________________________________________________________________

### Scenario 3 — High Risk: Credit Risk Assessment (Finance) { #scenario-credit-risk }

!!! example "Conceptual example — High Risk compliance trajectory"

**Sector:** Financial services — credit provider
**Risk class:** High Risk (EU AI Act Annex III — Mode 4 Delegated)
**Blueprint components used:** Full lifecycle (22 weeks), DPIA, Fairness audit (bias audit, extended), Guardian Review, Evidence Standards High Risk, CE-marking preparation

**Situation:** A credit provider wanted to partially automate the acceptance process for small business loans (\< EUR 50,000). The manual process took an average of 5 working days; commercial pressure was high to reduce this to 24 hours.

**Approach:** The Guardian immediately classified the system as **High Risk** (EU AI Act Annex III, point 5b: AI systems for creditworthiness assessments). This activated the full compliance trajectory: DPIA, extended Fairness audit (bias audit), human oversight at every decision, logging for 5 years, and preparation for the EU AI Act declaration of conformity.

The **Fairness audit (bias audit)** revealed that the initial model rejected applications from sole traders in certain postal code areas 23% more often than comparable applications. Analysis showed this was a proxy for demographic characteristics — an unacceptable Red Line. The model was revised with corrected training data.

Gate 3 (production go) was delayed by 3 weeks for additional validation by an external auditor. The system was deployed in **Mode 4**: the AI makes a recommendation with a confidence score; a credit analyst makes the final decision and documents the rationale.

**Result:** Turnaround time fell from 5 to 1.5 working days. The Fairness correction improved the representativeness of the portfolio. First external audit after 6 months of production: no violations. The incident involving the proxy variable is documented as a learning point in the Lessons Learned.

*Conceptual example — names and figures are illustrative.*

______________________________________________________________________

**Related modules:**

- [Risk Classification](../01-ai-native-fundamenten/05-risicoclassificatie.md)
- [Compliance Hub](../07-compliance-hub/index.md)
- [90-Day Roadmap](../12-90-dagen-roadmap/index.md)
- [Red Teaming](../07-compliance-hub/07-red-teaming.md)
- [Incident Response Playbooks](../07-compliance-hub/06-incidentrespons-playbooks.md)
- [Sources & Inspiration](../16-bronnen/index.md)

______________________________________________________________________

**Version:** 1.1
**Date:** 20 March 2026
**Status:** Final
