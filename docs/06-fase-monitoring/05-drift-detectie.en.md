---
versie: '1.1'
type: guide
layer: 2
phase: [5]
roles: [AI Product Manager, Data Scientist]
tags: [monitoring]
---

# 1. Performance Degradation Detection (Drift Detection)

## 1. Objective

Performance degradation (drift) is the phenomenon where the quality of an AI system deteriorates over time. This module describes how we detect, measure and respond to drift.

______________________________________________________________________

## 2. Types of Performance Degradation

### Data Drift

**What:** The input the system receives changes relative to the data on which it was trained/tested.

**Examples:**

- New product categories not present in the knowledge base
- Changed language use by customers
- Seasonal demand patterns

**Signals:**

- Increase in "I don't know" answers
- Queries about unknown topics
- Changing query distribution

### Concept Drift

**What:** The relationship between input and desired output changes, even if the input remains similar.

**Examples:**

- Price changes not updated in the knowledge base
- New policy requiring different answers
- Changing customer expectations

**Signals:**

- Correct answers are assessed as incorrect
- Increase in complaints despite unchanged test results
- Gap between validation and production feedback

### Performance Degradation

**What:** The model itself changes (through provider updates) or degrades.

**Examples:**

- Provider update to a new model
- Changes in API behaviour
- Fine-tuned model loses quality

**Signals:**

- Sudden change in output style
- Changed latency or token usage
- Regression on previously working scenarios

### Assumption Drift

**What:** The assumptions on which the AI system was built no longer hold due to changes in the environment, usage patterns or regulations.

**Examples:**

- User volume grows beyond assumed capacity
- Data distribution shifts compared to the original assumption
- New regulations (e.g. EU AI Act enforcement) make the current approach non-compliant
- Costs scale differently than assumed

**Signals:**

- Discrepancy between assumed and actual user profile
- Cost overruns without changes in functionality
- Compliance findings during audits

**Action:** Re-assess the assumptions in the [Objective Card (section E)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) at every quarterly review or after significant changes in the operational landscape.

______________________________________________________________________

## 3. Detection Methods

### Periodic Golden Set Testing

**Approach:** Run the Golden Set regularly in production.

| Risk Level | Frequency        | Scope                 |
| ---------- | ---------------- | --------------------- |
| Minimal    | Monthly          | Sample (25%)          |
| Limited    | Weekly           | Full set              |
| High       | Daily/Continuous | Full set + additional |

**What we measure:**

- Factual accuracy (% correct)
- Relevance (average score)
- Refusal rate (adversarial)
- Comparison with baseline

### Real-time Monitoring

**Approach:** Monitor production interactions for signals of drift.

**Metrics to monitor:**

| Metric               | Threshold for alert              |
| -------------------- | -------------------------------- |
| Error rate           | > 1.5x baseline                  |
| "Don't know" answers | > 2x baseline                    |
| Latency              | > 2x baseline                    |
| Token usage          | > 1.5x baseline (cost indicator) |
| Negative feedback    | > 2x baseline                    |

### User Feedback Analysis

**Approach:** Collect and analyse feedback systematically.

**Feedback channels:**

- Thumbs up/down in interface
- Escalations to human staff
- Complaints via other channels
- Corrections by users

______________________________________________________________________

## 4. Thresholds

Based on [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md) section 3.2:

**Significant performance degradation occurs when:**

| Criterion        | Threshold                                  |
| ---------------- | ------------------------------------------ |
| Factual accuracy | Drops ≥ 2 percentage points vs baseline    |
| Relevance (1–5)  | Drops ≥ 0.3 vs baseline                    |
| Major errors     | Increases ≥ 50% over 2 measurement periods |
| Critical errors  | > 0 = immediate action                     |

**Alert levels:**

| Level  | Condition                            | Action                          |
| ------ | ------------------------------------ | ------------------------------- |
| Green  | Within baseline                      | Normal management               |
| Yellow | Between baseline and threshold       | Increased monitoring            |
| Orange | Threshold exceeded                   | Investigation + mitigation plan |
| Red    | Critical error or severe degradation | Escalation + possible rollback  |

______________________________________________________________________

## 5. Response Protocol

### On Yellow (Increased Monitoring)

- [ ] Increase measurement frequency
- [ ] Analyse trend (is it stable or worsening?)
- [ ] Identify possible causes
- [ ] Document findings

### On Orange (Investigation)

- [ ] Perform root cause analysis
- [ ] Determine type of drift (data/concept/model)
- [ ] Draft mitigation plan
- [ ] Inform stakeholders
- [ ] Plan corrective action

### On Red (Escalation)

- [ ] Escalate to Tech Lead and Guardian
- [ ] Consider rollback or temporary shutdown
- [ ] Activate incident process
- [ ] Communicate to users if relevant
- [ ] Document for lessons learned

______________________________________________________________________

## 6. Mitigation Strategies

### Data Drift

| Cause                   | Mitigation                      |
| ----------------------- | ------------------------------- |
| Knowledge base outdated | Update knowledge base, reindex  |
| New topics              | Extend knowledge base           |
| Changed language use    | Adjust prompts, update examples |

### Concept Drift

| Cause                | Mitigation                          |
| -------------------- | ----------------------------------- |
| Policy changed       | Update Steering Instructions        |
| Expectations changed | Revise Goal Definition, update spec |
| External changes     | Revise Hard Boundaries              |

### Performance Degradation

| Cause                   | Mitigation                           |
| ----------------------- | ------------------------------------ |
| Provider update         | Regression test, adjust prompts      |
| API changes             | Update integration, provide fallback |
| Unexplained degradation | Contact provider, consider rollback  |

______________________________________________________________________

## 7. Baseline Measurement

### Recording the Baseline

At go-live, record the baseline:

| Metric        | Value at go-live | Alert threshold |
| ------------- | ---------------- | --------------- |
| Factual acc.  | 99.2%            | \< 97.2%        |
| Relevance     | 4.4              | \< 4.1          |
| Major errors  | 2/150            | > 3/150         |
| Latency (p95) | 1.8s             | > 3.6s          |

### Updating the Baseline

- After significant system changes
- After knowledge base expansion
- Minimum annual review

______________________________________________________________________

## 8. Monitoring Dashboard

Recommended visualisations:

| Visualisation            | Purpose                               |
| ------------------------ | ------------------------------------- |
| Trend line metrics       | Factual accuracy, relevance over time |
| Heatmap query categories | Identify problematic areas            |
| Alert timeline           | Overview of threshold breaches        |
| Comparison with baseline | Current vs baseline                   |

______________________________________________________________________

## 9. Performance Degradation Monitoring Checklist

!!! check "9. Performance Degradation Monitoring Checklist"
    - [ ] Baseline is recorded at go-live
    - [ ] Periodic Golden Set testing is scheduled
    - [ ] Real-time monitoring is active
    - [ ] Thresholds are configured
    - [ ] Alerting is linked to responsible parties
    - [ ] Response protocol is documented and known
    - [ ] Feedback channels are set up

______________________________________________________________________

## 10. Related Modules

- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Monitoring & Optimisation](01-doelstellingen.md)
- [Incident Response](../07-compliance-hub/05-incidentrespons.md)
- [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
- [Agentic AI Engineering — Silent Degradation](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Pitfalls Catalogue](../17-bijlagen/valkuilen-catalogus.md)

______________________________________________________________________

**Next step:** Set up the monitoring dashboard and define thresholds for your production environment
→ See also: [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
