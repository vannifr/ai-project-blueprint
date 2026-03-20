---
versie: '1.1'
type: assessment
layer: 2
phase: [1]
roles: [AI Product Manager]
summary: Determine which AI Collaboration Mode (1 through 5) is appropriate for your use case, as the basis for governance and oversight requirements.
answers: [What is Collaboration Mode Assessment?, Who decides what in an AI project?]
---

# 5. Collaboration Mode Assessment

!!! abstract "Purpose"
    Determine which AI Collaboration Mode (1 through 5) is appropriate for your use case, as the basis for governance and oversight requirements.

## 1. Objective

During the Discovery phase, we determine which [Collaboration Mode](../00-strategisch-kader/06-has-h-niveaus.md) (Mode 1 through 5) is appropriate for the use case being developed. This choice forms the basis for the governance requirements, technical specifications and human oversight structure of the project.

The intended mode is recorded in the [Project Charter](../09-sjablonen/01-project-charter/template.md).

______________________________________________________________________

## 2. Assessment Process

The collaboration mode assessment consists of three steps:

1. **Risk Analysis** — What are the consequences if the system makes an error?
1. **Decision Analysis** — Who makes the final decision?
1. **Mode Selection** — Which mode best fits the risk and decision structure?

______________________________________________________________________

## 3. Step 1: Risk Analysis

Score the following questions. Each question yields 0, 1 or 2 points.

| Question                                                      | 0 points            | 1 point             | 2 points                          | Score |
| :------------------------------------------------------------ | :------------------ | :------------------ | :-------------------------------- | :---: |
| What is the impact of an error by the AI system?              | None or recoverable | Limited, internal   | Major or external (client, legal) |       |
| How quickly must an error be corrected?                       | No time pressure    | Within days         | Immediately (real-time)           |       |
| Is personal data being processed?                             | No                  | Anonymised          | Yes, directly identifiable        |       |
| Does this system fall under the EU AI Act high-risk category? | No                  | Unknown             | Yes                               |       |
| Can decisions by the system harm an individual?               | No                  | Indirectly possible | Yes, directly                     |       |

**Total risk score:** \_\_\_\_\_ (max. 10)

______________________________________________________________________

## 4. Step 2: Decision Analysis

Answer the following questions:

**a. Who approves the output of the AI system before use?**

- [ ] Nobody — the system acts directly (→ high mode)
- [ ] An employee approves each proposal (→ low/middle mode)
- [ ] Sample: an employee checks periodically (→ middle/high mode)

**b. How quickly must the system respond?**

- [ ] Real-time (\< 1 second) → human approval per decision is not feasible
- [ ] Near real-time (seconds to minutes) → limited human intervention possible
- [ ] Asynchronous (hours to days) → full human approval feasible

**c. What is the volume of decisions?**

- [ ] Fewer than 100 per day → individual review feasible
- [ ] 100–10,000 per day → sampling feasible
- [ ] More than 10,000 per day → automated monitoring required

______________________________________________________________________

## 5. Step 3: Mode Selection

Combine the risk score with the decision analysis to determine the recommended mode:

| Risk score | Human decision per case | Recommended starting mode                            |
| :--------- | :---------------------- | :--------------------------------------------------- |
| 0 – 3      | Yes                     | **Mode 2 (Advisory)**                                |
| 0 – 3      | No, too high volume     | **Mode 3 (Collaborative)**                           |
| 4 – 6      | Yes, every decision     | **Mode 2 (Advisory)**                                |
| 4 – 6      | Sample / monitoring     | **Mode 3 (Collaborative)**                           |
| 7 – 10     | Every decision required | **Mode 2 (Advisory)**                                |
| 7 – 10     | Not feasible by volume  | **Mode 4 (Delegated)** — with strict Hard Boundaries |

!!! tip "Start low, scale up"
    Start in the lowest feasible mode to build trust and data. Only raise the mode after evidence of reliability (≥ 90% accuracy over at least 4 weeks of production).

!!! warning "Mode 5 (Autonomous)"
    Mode 5 always requires an explicit decision by the steering committee and approval from the Guardian. It is not an automatic next step after Mode 4.

______________________________________________________________________

## 5b. Architecture-Specific Considerations

The mode selection also depends on the type of AI architecture. Each type has specific considerations during the assessment:

| Architecture                             | Primary Concern                         | Key Questions                                                                               |
| :--------------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------ |
| **RAG (Retrieval-Augmented Generation)** | Document coverage & retrieval relevance | Do you have ≥100 quality source documents? Can you measure retrieval relevance?             |
| **Fine-tuning**                          | Labelling budget & data quality         | Do you have 5k–50k labelled examples? Is the data representative of the production context? |
| **Agentic (Mode 4-5)**                   | Tool reliability & Hard Boundaries      | Are the called tools reliable? What is the worst action the agent could take?               |

!!! tip "Architecture choice influences mode selection"
    A RAG system with limited source documents typically starts in Mode 2. An agentic system with financial tools requires at least Mode 4 governance — regardless of the risk score.

______________________________________________________________________

## 6. Recording

The outcome of the collaboration mode assessment is recorded in:

1. **Project Charter** — Section 'Collaboration Mode': record the chosen mode and the rationale.
1. **Hard Boundaries** — Define the boundaries appropriate to the chosen mode.
1. **Validation Plan** — Link the mode to the required validation intensity (see [Validation Model](../01-ai-native-fundamenten/04-validatie-model.md)).

| To document                           | Where               | Owner          |
| :------------------------------------ | :------------------ | :------------- |
| Chosen mode (1–5)                     | Project Charter     | AI PM          |
| Risk score and rationale              | Project Charter     | Guardian       |
| Hard Boundaries linked to mode        | Hard Boundaries doc | Guardian       |
| Validation requirements based on mode | Validation Plan     | Tech Lead + QA |

______________________________________________________________________

## 7. Related Modules

- [Discovery & Strategy — Core Activities](02-activiteiten.md)
- [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- [Project Charter Template](../09-sjablonen/01-project-charter/template.md)
- [Validation Model](../01-ai-native-fundamenten/04-validatie-model.md)
- [Risk Management](../07-compliance-hub/02-risicobeheer/index.md)

______________________________________________________________________

**Next step:** Determine the collaboration mode and record it in the [Project Charter](../09-sjablonen/01-project-charter/template.md)
→ See also: [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
