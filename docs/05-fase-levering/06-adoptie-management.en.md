---
versie: '1.0'
type: guide
layer: 2
roles: [AI Product Manager, Business Sponsor]
tags: [stakeholder, onboarding]
summary: 'Concrete adoption framework for AI systems: from resistance analysis to measurable user acceptance using the ADKAR model.'
answers: [How do I ensure people actually start using an AI system?, What is the ADKAR model for AI adoption?]
---

# Adoption Management

!!! abstract "Purpose"
    Concrete adoption framework for AI systems: from resistance analysis to measurable user acceptance using the ADKAR model.

!!! tip "When to use this?"
    Use this guide as soon as an AI system moves towards production (Phase 4 — Delivery). Begin the resistance analysis at least **4 weeks before go-live** so that communication and training can start in time. The Adoption Manager is responsible for execution; the AI Product Manager and Business Sponsor own the mandate.

______________________________________________________________________

## 1. Why Adoption Is Different for AI

AI systems are not traditional IT tools. They require a fundamentally different trust relationship with the user:

| Factor             | Traditional IT                                      | AI system                                      |
| :----------------- | :-------------------------------------------------- | :--------------------------------------------- |
| **Output**         | Deterministic — same input always gives same output | Probabilistic — output can vary per invocation |
| **Trust**          | Based on correctness of rules                       | Based on statistical evidence and experience   |
| **Fear**           | "Does it work?"                                     | "Will it replace me?" / "Can I trust it?"      |
| **Explainability** | Traceable via business rules                        | Often a black box without additional measures  |
| **Errors**         | Bug — reproducible and fixable                      | Hallucination — difficult to predict           |

**Consequence:** AI adoption requires not only training in *using* the tool, but also in *evaluating* its output. Users must learn when they can trust the AI and when they cannot.

______________________________________________________________________

## 2. ADKAR Model for AI Adoption

The ADKAR model (Prosci) provides a structured approach to change management. Below we translate each step to the specific context of AI projects.

### Awareness

> *"Why is something changing and why now?"*

| Aspect              | AI-specific application                                                                                                        |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| Core message        | The AI system solves a concrete problem that we currently handle manually or suboptimally                                      |
| What to communicate | Purpose of the system, what it can and cannot do, how it fits into daily work                                                  |
| Pitfall             | Focusing too much on technology instead of the problem being solved                                                            |
| Action              | Kick-off session with demo; share the [Goal Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) in accessible language |

### Desire

> *"What's in it for me?"*

| Aspect              | AI-specific application                                                   |
| :------------------ | :------------------------------------------------------------------------ |
| Core message        | The AI makes your work better, not redundant — you remain the expert      |
| What to communicate | Concrete benefits per role (time savings, fewer errors, better decisions) |
| Pitfall             | Making promises the system cannot keep                                    |
| Action              | Appoint champions per team; make early successes visible                  |

### Knowledge

> *"How do I use it?"*

| Aspect        | AI-specific application                                                         |
| :------------ | :------------------------------------------------------------------------------ |
| Core message  | You don't need to be an AI expert, but you must know how to evaluate the output |
| What to train | Basic usage, output evaluation, when to escalate, hard boundaries of the system |
| Pitfall       | Only explaining buttons without the *why* of critical evaluation                |
| Action        | Hands-on workshops with realistic scenarios; quick reference card               |

### Ability

> *"Can I apply it in practice?"*

| Aspect             | AI-specific application                                                   |
| :----------------- | :------------------------------------------------------------------------ |
| Core message       | Practice and support until it becomes daily routine                       |
| What to facilitate | Buddy system, helpdesk, feedback channel, time for adjustment             |
| Pitfall            | Expecting everyone to use the system perfectly immediately after training |
| Action             | 2-4 week guided pilot period; weekly Q&A sessions                         |

### Reinforcement

> *"How do we make it stick?"*

| Aspect       | AI-specific application                                                  |
| :----------- | :----------------------------------------------------------------------- |
| Core message | Celebrate successes, process feedback, improve the system based on usage |
| What to do   | Monitor adoption metrics, communicate improvements, share successes      |
| Pitfall      | Losing attention after go-live and not noticing regression               |
| Action       | Monthly adoption review; feedback loop to the development team           |

______________________________________________________________________

## 3. Resistance Analysis

Resistance during AI introduction is normal and predictable. Recognise the patterns and address them systematically.

| Form of resistance         | Signals                                          | Approach                                                                                                 |
| :------------------------- | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Fear of replacement**    | "Will my job become redundant?"                  | Clearly communicate which tasks the AI takes over and which become more important                        |
| **Distrust of output**     | "I don't trust it" / "I double-check everything" | Share Golden Set results; be transparent about error rates; involve users in validation                  |
| **Comfort zone behaviour** | "I prefer the old way"                           | Demonstrate time savings; buddy system with enthusiasts                                                  |
| **Perfectionism**          | "It makes mistakes, so it's unusable"            | Provide context: human error rates vs. AI error rates; explain that the human+AI combination is stronger |
| **Political resistance**   | Managers losing control over information flows   | Involve sponsors; demonstrate that AI provides more insight, not less                                    |
| **Passive resistance**     | The system is available but nobody uses it       | Activate workaround detection; discuss in team meetings; remove barriers                                 |

!!! warning "Red line"
    If resistance stems from legitimate concerns about safety, privacy or ethics, treat these as serious findings via the [risk management process](../07-compliance-hub/02-risicobeheer/index.md) — not as resistance to be overcome.

______________________________________________________________________

## 4. Communication Strategy per Audience

| Audience                            | Core message                                              | Channel                                        | Frequency                |
| :---------------------------------- | :-------------------------------------------------------- | :--------------------------------------------- | :----------------------- |
| **Management / Steering committee** | ROI, risk mitigation, compliance status                   | Steering committee update, dashboard           | Monthly                  |
| **End users**                       | What changes in my work, how to use it, where to get help | Workshop, quick reference, Teams/Slack channel | Weekly (pre/post-launch) |
| **IT / Operations**                 | Technical integration, monitoring, escalation paths       | Technical briefing, runbook                    | At go-live + monthly     |
| **Legal / Compliance**              | EU AI Act status, privacy protection, audit trail         | Compliance report                              | Per gate review          |
| **Works council**                   | Impact on employment, privacy, transparency               | Formal consultation                            | As per advisory rights   |

!!! tip "Communication rule"
    Always communicate **what the system cannot do** before telling people what it can do. This builds trust and prevents disappointment.

______________________________________________________________________

## 5. Adoption Metrics

Measure adoption objectively. Gut feeling matters, but numbers make problems visible before they escalate.

| Metric                    | Description                                        | Target                       | Measurement method               |
| :------------------------ | :------------------------------------------------- | :--------------------------- | :------------------------------- |
| **Usage Rate**            | % active users vs. intended users                  | >80% after 8 weeks           | Application logging              |
| **Task Completion Rate**  | % tasks successfully completed via the AI system   | >70% after 4 weeks           | Application logging              |
| **Satisfaction Score**    | User satisfaction (1-5)                            | ≥3.5                         | Periodic survey                  |
| **Error Escalation Rate** | Number of times users escalate or report AI output | Declining trend              | Ticket system / feedback channel |
| **Workaround Detection**  | Signals that users are bypassing the system        | \<10%                        | Process monitoring, spot checks  |
| **Time-to-Competence**    | Time until a user can work independently           | \<2 weeks                    | Training evaluation              |
| **Support Ticket Volume** | Number of support queries about the AI system      | Declining trend after week 4 | Helpdesk data                    |

!!! info "Dashboard"
    Combine these metrics in an adoption dashboard and discuss them in the monthly [retrospective](../10-doorlopende-verbetering/01-retrospectives.md). Feed findings back to the development team.

______________________________________________________________________

## 6. Practical Checklist

### Pre-launch (4-6 weeks before go-live)

!!! check "Pre-launch Checklist"
    - [ ] Resistance analysis completed per audience
    - [ ] ADKAR plan drafted with concrete actions per step
    - [ ] Champions identified and briefed
    - [ ] Communication plan ready with messages per audience
    - [ ] Training materials developed (workshop, quick reference card)
    - [ ] Feedback channel set up (Teams/Slack channel, form)
    - [ ] Adoption metrics defined and measurable
    - [ ] Works council informed (if applicable)

### Launch (week 1-2)

!!! check "Launch Checklist"
    - [ ] Kick-off session held with demo and Q&A
    - [ ] Hands-on training delivered per team
    - [ ] Quick reference cards distributed
    - [ ] Helpdesk / support available
    - [ ] Daily check-in with champions (first week)
    - [ ] Initial adoption metrics collected

### Post-launch (week 3-8)

!!! check "Post-launch Checklist"
    - [ ] Weekly adoption metrics reviewed
    - [ ] Workaround detection actively monitored
    - [ ] Feedback collected and fed back to development team
    - [ ] Corrective actions taken where needed
    - [ ] Successes shared with management and teams
    - [ ] Advanced training offered for power users
    - [ ] Evaluation report completed after 8 weeks

______________________________________________________________________

## 7. Related Modules

- [Roles & Responsibilities](../08-rollen-en-verantwoordelijkheden/index.md) — Adoption Manager role
- [Stakeholder Communication](../08-rollen-en-verantwoordelijkheden/03-stakeholder-communicatie.md) — Communication plan per audience
- [Goal Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) — Translate AI goals into accessible language
- [Retrospectives](../10-doorlopende-verbetering/01-retrospectives.md) — Discuss adoption findings structurally
- [Risk Management](../07-compliance-hub/02-risicobeheer/index.md) — Process resistance from legitimate concerns
- [Handover Checklist](04-sjablonen/overdracht-checklist.md) — Formal handover to the operations team

______________________________________________________________________

**Next step:** Conduct the resistance analysis and draft the ADKAR plan at least 4 weeks before go-live.
→ See also: [Stakeholder Communication](../08-rollen-en-verantwoordelijkheden/03-stakeholder-communicatie.md)
