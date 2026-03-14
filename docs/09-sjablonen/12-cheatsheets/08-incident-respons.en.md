---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference, security]
---

# Cheatsheet — Incident Response

**Source:** [Incident Response](../../07-compliance-hub/05-incidentrespons.md) | [Incident Playbooks](../../07-compliance-hub/06-incidentrespons-playbooks.md)

______________________________________________________________________

## First 15 Minutes

```
1. DETECT    — Is this a real incident or a false alarm?
2. CLASSIFY  — What type? (Drift / Security / Bias / Outage)
3. SEVERITY  — Red / Orange / Yellow / Green?
4. NOTIFY    — Inform the right people immediately
5. PRESERVE  — Secure logs, delete nothing
```

______________________________________________________________________

## Severity & Action

| Severity      | Threshold                           | Action                                            | Who                   |
| :------------ | :---------------------------------- | :------------------------------------------------ | :-------------------- |
| 🔴 **Red**    | Direct harm or legal obligation     | Activate Circuit Breaker; CISO + Guardian + Legal | Tech Lead (commander) |
| 🟠 **Orange** | Significant risk, no direct harm    | Increased monitoring; inform Guardian             | AI PM + Tech Lead     |
| 🟡 **Yellow** | Quality degradation, limited impact | Monitor; recovery plan within 24h                 | AI PM                 |
| 🟢 **Green**  | Deviation within bandwidth          | Document; no action needed                        | Automated             |

______________________________________________________________________

## Circuit Breaker — Activate When

- Unauthorised access or active data leakage
- Outputs that could cause direct harm
- System outside all normal parameters
- Legal obligation to act immediately

**Activate Circuit Breaker:** → [Incident Response Overview](../../07-compliance-hub/05-incidentrespons.md)

______________________________________________________________________

## Playbook per Type

| Incident type               | Playbook                                                                                        |
| :-------------------------- | :---------------------------------------------------------------------------------------------- |
| Quality degradation / drift | [Playbook 1 — Performance Degradation](../../07-compliance-hub/06-incidentrespons-playbooks.md) |
| Security incident           | [Playbook 2 — Security](../../07-compliance-hub/06-incidentrespons-playbooks.md)                |
| Unequal treatment           | [Playbook 3 — Bias](../../07-compliance-hub/06-incidentrespons-playbooks.md)                    |
| System unavailable          | [Playbook 4 — Outage](../../07-compliance-hub/06-incidentrespons-playbooks.md)                  |

______________________________________________________________________

## Reporting Obligations (Timeline)

| Obligation                   | Deadline            | Trigger                    |
| :--------------------------- | :------------------ | :------------------------- |
| GDPR data breach             | 72 hours            | Personal data involved     |
| EU AI Act (High Risk)        | Per national policy | Incident with human impact |
| Internal escalation Guardian | Immediately         | Red or Orange incident     |
| User communication           | 15 min (outage)     | System unavailable         |

**Source for full approach:** [Incident Playbooks](../../07-compliance-hub/06-incidentrespons-playbooks.md)
