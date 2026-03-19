---
versie: '1.1'
type: playbook
layer: 1
tags: [playbook, stakeholder]
---

# Stakeholder Communication Playbook

!!! abstract "Purpose"
    Practical guide for communicating with stakeholders about the unique challenges of AI projects, such as probabilistic outcomes and iterative validation.

Practical guide for AI Project Managers on communicating with stakeholders in AI projects. AI projects present unique communication challenges: probabilistic outcomes, iterative validation and technical complexity that must be translated into business impact.

!!! info "Audience"
    This playbook is primarily intended for the **AI PM**. The communication techniques are, however, also valuable for **Tech Leads** and **Data Scientists** who regularly communicate with non-technical stakeholders.

______________________________________________________________________

## 1. Communication Cadence

Structure your communication around fixed moments. Each stakeholder group receives information at the right level and with the right frequency.

| Stakeholder group | What                                             | Frequency | Format                      | Responsible       |
| :---------------- | :----------------------------------------------- | :-------- | :-------------------------- | :---------------- |
| Sponsor           | Strategic progress, budget, Gate decisions       | Bi-weekly | 1-on-1 briefing (30 min)    | AI PM             |
| Guardian          | Compliance status, hard boundaries, risk updates | Monthly   | Written report              | AI PM + Tech Lead |
| Tech Lead         | Technical progress, blockers, architecture       | Weekly    | Standup or Slack update     | AI PM             |
| Stakeholders      | Business impact, adoption, model health          | Monthly   | Model Health Review meeting | AI PM             |
| CAIO              | Portfolio overview, escalations                  | Quarterly | Dashboard + briefing        | AI PM             |

______________________________________________________________________

## 2. The Maybe Problem

AI systems deliver probabilistic outcomes. Where traditional software is deterministic ("it works or it doesn't"), an AI system provides answers with a certain degree of confidence. This is fundamentally different and requires a different way of communicating.

### Why this is challenging

- Stakeholders expect yes/no answers; AI delivers probabilities.
- An accuracy of 95% sounds high, but means that 1 in 20 predictions is wrong.
- "The model doesn't know" is a valid and valuable outcome, but is often perceived as failure.

### How to frame this

1. **Start with the baseline.** Always compare with the current situation: "Manual assessment has an error rate of 12%; the model reduces this to 5%."
1. **Make errors concrete.** Translate percentages into numbers: "With 10,000 transactions per month, 95% accuracy means that 500 cases require manual review."
1. **Show confidence intervals.** Present not just the average, but also the range: "The model predicts with 87-93% certainty, depending on data quality."
1. **Normalise uncertainty.** Explain that uncertainty is a feature, not a bug: "The model indicates when it is uncertain, so that a human expert can step in."

______________________________________________________________________

## 3. Building Trust

Trust in AI systems is not won with numbers alone. It requires active involvement of stakeholders in the validation process.

### Practical techniques

- **Involve stakeholders in edge case review.** Invite stakeholders to examine borderline cases and assess the model on cases they know from practice. This gives them ownership of quality.
- **Show confidence intervals.** Make visible when the model is confident and when it is not. Stakeholders trust a system more that is honest about its limitations.
- **Organise regular health reviews.** Use the [Monthly Model Health Review](../09-sjablonen/18-modelgezondheid/template.md) template to provide structural transparency.
- **Let stakeholders "break" the model.** Organise informal sessions where stakeholders can submit difficult cases. This lowers the threshold and increases understanding.
- **Share near misses proactively.** Do not wait until a stakeholder discovers an error. Report proactively on cases where the system nearly failed and what you did about it.

!!! warning "Avoid the numbers-as-proof argument"
    Never say: "The numbers prove it works." This undermines trust. Instead say: "Let us look at some specific cases together so you can judge for yourself."

______________________________________________________________________

## 4. Escalation Procedure

The escalation procedure is aligned with the existing governance model, including the 48-hour cooling-off period for disagreements.

### Escalation levels

| Level | Trigger                                     | Action                                    | Communication to             |
| :---- | :------------------------------------------ | :---------------------------------------- | :--------------------------- |
| 1     | Metric below threshold (yellow)             | Increased monitoring; AI PM informs       | Tech Lead, Data Scientist    |
| 2     | Structural performance degradation (orange) | Schedule retraining; inform Sponsor       | Sponsor, Guardian, Tech Lead |
| 3     | Hard Boundaries exceeded (red)              | Pause system; activate incident process   | CAIO, Sponsor, Guardian, all |
| 4     | Disagreement on decision                    | 48-hour cooling-off; then CAIO escalation | All involved parties         |

### Communication templates for escalation

**Level 2 — Message to Sponsor:**

> "Dear \[Name\], the performance of \[system\] shows a declining trend over the past \[period\]. The current \[metric\] stands at \[value\], below our threshold of \[threshold\]. The team is scheduling retraining on \[date\]. We will keep you informed of progress in the next briefing on \[date\]."

**Level 3 — Message to all stakeholders:**

> "The AI system \[name\] has been temporarily paused due to a hard boundary breach on \[date\]. The incident response team is investigating the cause. Expected resolution time: \[estimate\]. We will communicate updates every \[frequency\] via \[channel\]."

______________________________________________________________________

## 5. Trade-off Communication

AI projects require continuous trade-offs between accuracy, speed and cost. Help stakeholders understand these trade-offs.

### The 95% to 99% cost curve

Improving from 90% to 95% accuracy typically costs X. Improving from 95% to 99% often costs 5-10x as much. Make this explicit:

| Accuracy | Relative cost | Errors per 10,000 | Considerations                              |
| :------- | :------------ | :---------------- | :------------------------------------------ |
| 90%      | 1x            | 1,000             | Suitable for low-risk applications          |
| 95%      | 2-3x          | 500               | Standard for most applications              |
| 99%      | 10-20x        | 100               | Only for high-risk / critical flows         |
| 99.9%    | 50-100x       | 10                | Rarely achievable; consider hybrid approach |

### The triangle model

Present trade-offs as a triangle with three axes:

- **Accuracy:** How correct are the predictions?
- **Latency:** How quickly does the answer arrive?
- **Cost:** What does each prediction cost?

Improve one axis, and at least one of the others deteriorates. Help stakeholders determine which axis has priority for their use case.

______________________________________________________________________

**Next step:** Use the [Monthly Model Health Review](../09-sjablonen/18-modelgezondheid/template.md) template for structured stakeholder communication and consult the [Decision Authority Matrix](besluitvormingsmatrix.md) for decision authority per role.
