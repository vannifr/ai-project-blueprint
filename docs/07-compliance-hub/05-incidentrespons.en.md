---
versie: '1.1'
pdf: false
---

# Incident Response

Respond quickly and in a coordinated manner to AI incidents. This page defines the severity matrix, roles and immediate actions. Detailed procedures are in the [Incident Playbooks](06-incidentrespons-playbooks.md).

______________________________________________________________________

## 1. Severity Matrix

| Level         | Criteria                                                                        | Response time | Escalation                 | Communication                      |
| :------------ | :------------------------------------------------------------------------------ | :------------ | :------------------------- | :--------------------------------- |
| 🔴 **Red**    | Critical safety or compliance violation; potential legal liability              | 15 min        | CAIO, Legal, Guardian      | Immediate stakeholder notification |
| 🟠 **Orange** | Significant functional disruption; affected parties impacted; reputational risk | 1 hour        | Tech Lead, AI PM, Guardian | Within 4 hours                     |
| 🟡 **Yellow** | Limited degradation; no direct harm; user experience impaired                   | 4 hours       | Tech Lead, AI PM           | Within 24 hours                    |
| 🟢 **Green**  | Minimal deviation; no direct impact; monitoring required                        | 24 hours      | Tech Lead                  | Next status update                 |

______________________________________________________________________

## 2. Incident Types & Playbooks

Four incident types each have their own step-by-step procedure in the [Incident Playbooks](06-incidentrespons-playbooks.md):

| Type                  | Signals                                                           | Typical level |
| :-------------------- | :---------------------------------------------------------------- | :------------ |
| **Model Drift**       | Declining quality scores, user complaints, monitoring anomalies   | 🟡–🟠         |
| **Security Incident** | Unauthorised access, data leakage, abnormal usage                 | 🟠–🔴         |
| **Bias Detection**    | Complaints about unequal treatment, fairness metrics out of range | 🟠–🔴         |
| **System Outage**     | Unavailability, time-outs, errors at scale                        | 🟡–🔴         |

______________________________________________________________________

## 3. Circuit Breaker

The Circuit Breaker is the emergency stop for AI systems in Collaboration Mode 4 and 5.

**Activate the Circuit Breaker when:**

- [ ] The system acts outside defined Hard Boundaries
- [ ] A security incident is active or suspected
- [ ] Bias or discriminatory output has been established
- [ ] The system is at risk of executing irreversible actions

**Circuit Breaker procedure:**

1. **Isolate** — switch to read-only mode or disable inference
1. **Notify** — immediately alert Guardian + Tech Lead
1. **Document** — record timestamp, trigger, system state and affected outputs
1. **Reassess** — no restart without explicit Guardian approval

______________________________________________________________________

## 4. Incident Roles

| Role          | Responsibility                                            |
| :------------ | :-------------------------------------------------------- |
| **Tech Lead** | Technical diagnosis, containment, recovery                |
| **AI PM**     | Coordination, stakeholder communication, timeline         |
| **Guardian**  | Ethical assessment, restart decision, compliance check    |
| **CAIO / MT** | Escalation at Red level, external communication           |
| **Legal**     | Assess notification obligations (GDPR, EU AI Act Art. 73) |

______________________________________________________________________

## 5. Notification Obligations

For incidents that harm people or involve personal data:

- **GDPR data breach:** notification to supervisory authority within **72 hours**
- **EU AI Act (High Risk):** notify market supervisory authority upon confirmation
- **Internal:** notify Compliance/Legal within **24 hours** of detection

______________________________________________________________________

## 6. Post-Incident

After every 🟠 Orange or 🔴 Red incident:

- [ ] Root cause analysis completed
- [ ] Lessons Learned documented
- [ ] Risk inventory updated
- [ ] Blueprint/monitoring adjusted to prevent recurrence
- [ ] Incident recorded in the project log

______________________________________________________________________

## 7. Related Modules

- [Incident Playbooks (4 detailed procedures)](06-incidentrespons-playbooks.md)
- [Red Teaming Playbook](07-red-teaming.md)
- [AI Safety Checklist](08-ai-safety-checklist.md)
- [Drift Detection](../06-fase-monitoring/05-drift-detectie.md)
- [Risk Management](02-risicobeheer/index.md)
