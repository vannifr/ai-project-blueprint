---
versie: '1.1'
type: playbook
layer: 3
roles: [Guardian]
tags: [eu-ai-act, playbook, security]
summary: 'Four detailed step-by-step procedures for the most common AI incidents: performance degradation, bias, security incidents and data quality.'
answers: [How do I execute Incident Playbooks?]
---

# Incident Playbooks

!!! abstract "Purpose"
    Four detailed step-by-step procedures for the most common AI incidents: performance degradation, bias, security incidents and data quality.

!!! tip "When to use this?"
    An AI incident has been detected (performance degradation, bias, security breach or data quality issue) and you need an immediate step-by-step response procedure.

Four detailed step-by-step procedures for the most common AI incidents. Use these alongside the [Incident Response overview](05-incidentrespons.md) for the severity matrix and roles.

______________________________________________________________________

## Playbook 1 — Performance Degradation

**When to activate:** quality scores decline structurally, user complaints increase, monitoring alerts on output quality.

### Step 1 — Detection & Validation (0–30 min)

- [ ] Check monitoring dashboard for trend (not a one-off spike)
- [ ] Compare current scores to baseline (Golden Set or production sample)
- [ ] Classify severity: 🟡 Yellow (score ≥ 80% baseline) / 🟠 Orange (60–80%) / 🔴 Red (\< 60%)
- [ ] Record timestamp of first deviation

### Step 2 — Containment (30–60 min)

- [ ] Notify Tech Lead + AI PM
- [ ] Notify Guardian at 🟠 Orange or higher
- [ ] Consider rollback to previous model version if available
- [ ] Temporarily increase monitoring frequency

### Step 3 — Investigation (1–24 hours)

- [ ] Determine drift type: **data drift** (input changed) or **concept drift** (world changed)
- [ ] Identify when drift started (git log, model registry, data pipeline logs)
- [ ] Quantify impact: how many outputs may be incorrect?
- [ ] Assess compliance implications (High Risk systems: check notification obligations)

### Step 4 — Recovery (24–72 hours)

- [ ] Select recovery strategy: retraining / prompt adjustment / knowledge base update
- [ ] Test strategy against Golden Set (minimum threshold: baseline + 5%)
- [ ] Have Guardian validate for systems with human impact
- [ ] Deploy fix with enhanced monitoring (first 48 hours)

### Step 5 — Post-Incident

- [ ] Root cause documented
- [ ] Monitoring thresholds adjusted
- [ ] Baseline updated if concept drift is structural
- [ ] Lessons Learned completed

______________________________________________________________________

## Playbook 2 — Security Incident

**When to activate:** unauthorised access, data leakage, abnormal usage, suspicious API patterns.

### Step 1 — Detection & First Action (0–15 min)

- [ ] Classify type: **access violation** / **data leakage** / **system misuse**
- [ ] Activate [Circuit Breaker](05-incidentrespons.md) if active threat
- [ ] Immediately notify: Security/CISO, Guardian, Legal
- [ ] Preserve evidence: export logs, take screenshots, record timeline

!!! danger "Do not destroy logs"
    Logs are evidence. Do not delete or overwrite anything until Legal approves.

### Step 2 — Containment (15 min–1 hour)

- [ ] Revoke compromised credentials/tokens
- [ ] Block suspicious IP addresses or accounts
- [ ] Isolate affected systems from production if possible
- [ ] Determine whether attacker is still active

### Step 3 — Impact Assessment (1–24 hours)

- [ ] Which data was accessed or exfiltrated?
- [ ] How many users/data subjects are affected?
- [ ] Are personal data involved? → GDPR notification within 72 hours
- [ ] Are there EU AI Act implications (High Risk system)? → Market supervisory authority

### Step 4 — Recovery (24–168 hours)

- [ ] Patch vulnerability or update access controls
- [ ] Commission penetration test for affected component
- [ ] Restore services gradually with enhanced monitoring
- [ ] Notify affected parties if legally required (GDPR Art. 34)

### Step 5 — Post-Incident

- [ ] Forensic analysis completed
- [ ] Security measures updated
- [ ] Team trained on new procedure
- [ ] Responsible Disclosure considered if external researcher involved

______________________________________________________________________

## Playbook 3 — Bias Detection

**When to activate:** complaints about unequal treatment, fairness metrics out of range, audit finding, media report.

### Step 1 — Validation (0–4 hours)

- [ ] Analyse reported outputs on the relevant characteristic (gender, age, ethnicity, etc.)
- [ ] Compare output quality/decisions across relevant groups
- [ ] Quantify disparity (e.g. difference in acceptance rate, quality score per group)
- [ ] Classify severity and notify Guardian (mandatory for bias incidents)

### Step 2 — Impact Assessment (4–24 hours)

- [ ] How long has the bias likely existed?
- [ ] How many decisions/outputs are potentially affected?
- [ ] Which groups have been disadvantaged?
- [ ] Are there legal consequences (discrimination law, EU AI Act)?

### Step 3 — Root Cause (24–48 hours)

Identify the source:

| Source              | Indication                                 | Approach                         |
| :------------------ | :----------------------------------------- | :------------------------------- |
| **Data bias**       | Training data over-represents a group      | Rebalance dataset + retraining   |
| **Model bias**      | Model amplifies bias independently of data | Fine-tuning or model replacement |
| **Prompt bias**     | Instructions lead to unequal treatment     | Prompt revision + testing        |
| **Deployment bias** | System used differently than validated     | Adjust scope                     |

### Step 4 — Mitigation & Recovery (48–168 hours)

- [ ] Implement mitigation strategy based on root cause
- [ ] Validate with fairness metrics (equality of opportunity, demographic parity)
- [ ] Revalidation requires Guardian approval before restart
- [ ] Consider reviewing previously affected decisions

### Step 5 — Post-Incident

- [ ] Model Card updated with bias findings
- [ ] Fairness monitoring extended
- [ ] Fairness Check (Bias Audit) protocol revised
- [ ] Communication to affected parties if applicable

______________________________________________________________________

## Playbook 4 — System Outage

**When to activate:** system unreachable, time-outs at scale, high error rates, production pipeline blocked.

### Step 1 — Detection & First Action (0–15 min)

- [ ] Determine scope: **partial** (component down) or **full** (system unavailable)
- [ ] Activate fallback mode if configured (human handover or temporarily offline)
- [ ] Notify Tech Lead (incident commander) + AI PM (communications)
- [ ] Communicate to users: status update within 15 minutes

### Step 2 — Diagnosis (15 min–2 hours)

Work through in order:

1. **Infrastructure** — cloud provider status, servers, network
1. **Dependencies** — external APIs (LLM provider, databases)
1. **Application** — logs, memory/CPU, error codes
1. **Recent changes** — last deployment, config change, data update

### Step 3 — Recovery (2–8 hours)

- [ ] Develop fix based on diagnosis
- [ ] Test in staging environment before production
- [ ] Document rollback plan before deployment
- [ ] Deploy fix with gradual rollout (canary or blue-green if possible)

### Step 4 — Validation & Restart

- [ ] Verify all functions operational
- [ ] Remove fallback mode
- [ ] Monitor closely for first 2 hours after restart
- [ ] Update status page / communicate resolution

### Step 5 — Post-Incident

- [ ] Timeline documented (detection → recovery)
- [ ] Root cause established
- [ ] Monitoring improved for faster detection
- [ ] Runbook updated

______________________________________________________________________

## Communication Templates

### Initial Alert (internal)

```
INCIDENT ALERT — [Level: Red/Orange/Yellow]
System: [name]
Type: [Drift / Security / Bias / Outage]
Detection time: [date + time]
Initial impact: [description]
Incident commander: [name]
Next update: [time]
```

### User Communication (outage)

```
We are aware of a disruption to [system].
Our team is investigating the cause. Expected recovery time: [time].
Temporary workaround: [description of fallback if applicable].
Updates will follow every hour via [channel].
```

______________________________________________________________________

## Related Modules

- [Incident Response Overview](05-incidentrespons.md)
- [Drift Detection](../06-fase-monitoring/05-drift-detectie.md)
- [AI Safety Checklist](08-ai-safety-checklist.md)
- [Risk Management](02-risicobeheer/index.md)
- [Agentic AI Engineering — Failure Modes](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Pitfalls Catalogue](../17-bijlagen/valkuilen-catalogus.md)
