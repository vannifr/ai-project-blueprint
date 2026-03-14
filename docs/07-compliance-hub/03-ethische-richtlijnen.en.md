---
versie: '1.0'
type: compliance
layer: 3
roles: [Guardian]
tags: [ethics, eu-ai-act]
---

# 1. Ethical Guidelines

## 1. Purpose

Ensure that AI systems are developed and used in a way that respects human values and causes no unintended harm.

______________________________________________________________________

## 2. Ethical Principles

### Human Oversight and Control

AI must not undermine human autonomy. Users must be able to understand how the system works and, where necessary, intervene (**Human Oversight**).

### Justice & Fairness

AI systems must not lead to unjust discrimination. We apply the **Fairness Check** to eliminate bias at three levels (Representativeness, Stereotyping, Equal Treatment).

### Transparency & Explainability

It must be clear to a user when they are communicating with an AI. Decisions made by the system must be explainable in an understandable way.

### Privacy & Data Protection

Strict compliance with GDPR. Data is only used for the intended purpose and in accordance with the established **Hard Boundaries**.
Source: \[so-49\]

### Societal & Environmental Wellbeing

We strive for a positive impact on society and minimise the ecological footprint of our AI systems (energy efficiency).

______________________________________________________________________

## 3. The Fairness Check (Bias Audit) — Extended

### Audit Levels

We assess every High and Limited risk system at three levels:

| Level                  | Question                                                     | Example                                                              |
| ---------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------- |
| **Representativeness** | Is the data a good reflection of reality?                    | Are all customer segments represented in training data?              |
| **Stereotyping**       | Does the AI reinforce harmful clichés?                       | Does the system associate certain professions with specific genders? |
| **Equal Treatment**    | Does every user group receive the same quality of responses? | Is the error margin equal for different age groups?                  |

### Measurable Fairness Criteria

We use the following measurable criteria for fairness:

| Criterion               | Definition                                                     | Formula                           | When to Apply                                                 |
| ----------------------- | -------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------- |
| **Demographic Parity**  | Probability of positive outcome is equal for all groups        | P(Y=1\|A=0) ≈ P(Y=1\|A=1)         | Selection/assignment without legitimising difference          |
| **Equalized Odds**      | True Positive Rate and False Positive Rate are equal per group | TPR and FPR equal for A=0 and A=1 | Decisions where both positive and negative errors have impact |
| **Predictive Parity**   | Precision (positive predictive value) is equal per group       | Precision equal for A=0 and A=1   | When confidence in positive predictions is crucial            |
| **Individual Fairness** | Similar individuals receive similar treatment                  | d(f(x), f(x')) ≤ d(x, x')         | Personalised service delivery                                 |

### Thresholds per Risk Level

| Risk Level  | Maximum Difference Between Groups    | Additional Requirements                            |
| ----------- | ------------------------------------ | -------------------------------------------------- |
| **Minimal** | Qualitative assessment by Guardian   | No quantitative requirement                        |
| **Limited** | ≤ 10% difference in Major error rate | Documentation of group comparison                  |
| **High**    | ≤ 5% difference in Major error rate  | Quantitative analysis + documented mitigation plan |

### Performing the Fairness Check

**Step 1: Identify Relevant Groups**

- Which protected characteristics are relevant? (gender, age, ethnicity, etc.)
- Note: some characteristics are proxies for protected characteristics (postcode, name)
- Document choices in Risk Pre-Scan

**Step 2: Collect or Annotate Data**

- Option A: Group labels available in test data
- Option B: Manual annotation of Golden Set subset
- Option C: Proxy variables with justification
- Note privacy: pseudonymise where possible

**Step 3: Measure Performance per Group**

| Metric       | Group A     | Group B     | Difference | Status     |
| ------------ | ----------- | ----------- | ---------- | ---------- |
| Factuality   | 98.5%       | 97.2%       | 1.3%       | OK         |
| Major errors | 2/75 (2.7%) | 4/75 (5.3%) | 2.6%       | OK (\< 5%) |
| Relevance    | 4.3         | 4.1         | 0.2        | OK         |

**Step 4: Analyse and Mitigate**

When thresholds are exceeded:

| Cause               | Possible Mitigation                       |
| ------------------- | ----------------------------------------- |
| Data imbalance      | Rebalancing, oversampling, synthetic data |
| Bias in source data | Expand data sources, debiasing            |
| Prompt bias         | Neutral phrasing, explicit instructions   |
| Model bias          | Threshold calibration, post-processing    |

**Step 5: Document and Report**

Record in [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md):

- Which groups were compared
- Which metrics were measured
- Results per group
- Conclusion relative to thresholds
- Mitigation measures (if applicable)

### Tooling for Fairness Check

| Tool                      | Type           | Strength                                   | Link                             |
| ------------------------- | -------------- | ------------------------------------------ | -------------------------------- |
| **Fairlearn** (Microsoft) | Python library | Integration with sklearn, multiple metrics | fairlearn.org                    |
| **AI Fairness 360** (IBM) | Python toolkit | Extensive algorithms, good documentation   | aif360.mybluemix.net             |
| **Aequitas**              | Python library | Focus on auditing, visual reports          | github.com/dssg/aequitas         |
| **What-If Tool** (Google) | Visualisation  | Interactive exploration                    | pair-code.github.io/what-if-tool |

### Limitations and Considerations

**Fairness-accuracy trade-off:**
Optimising for fairness can lead to lower overall accuracy. Document the trade-off.

**Incompatibility of criteria:**
Some fairness criteria are mathematically incompatible. Choose criteria that fit the use case.

**Proxy discrimination:**
Even without direct protected characteristics a model can discriminate via proxies. Test for this.

**Intersectionality:**
Fairness for individual groups does not guarantee fairness for combinations (e.g. young women). Consider subgroup analysis for High Risk.

______________________________________________________________________

## 4. The Role of the Guardian

The Guardian acts as the moral compass of the project:

- Guards the **Hard Boundaries**
- Performs independent ethical reviews
- Has veto mandate for ethical violations
- Approves Fairness Check results
- Escalates for unresolvable fairness issues

### Guardian Tasks per Phase

| Phase       | Guardian Activity                                   |
| ----------- | --------------------------------------------------- |
| Discovery   | Assess ethical desirability, define Hard Boundaries |
| Validation  | Perform/review Fairness Check                       |
| Development | Validate mitigation measures                        |
| Delivery    | Final ethical approval                              |
| Management  | Periodic ethics reviews, bias monitoring            |

______________________________________________________________________

## 5. Ethical Guidelines Checklist

!!! check "5. Ethical Guidelines Checklist"
    - [ ] Ethical principles have been discussed with the team
    - [ ] Hard Boundaries are defined in the Objective Card
    - [ ] Relevant groups for Fairness Check have been identified
    - [ ] Fairness Check has been performed according to risk level
    - [ ] Results meet thresholds or mitigation is documented
    - [ ] Guardian has given ethical approval
    - [ ] Transparency obligation is implemented (Limited/High Risk)

______________________________________________________________________

## 6. Related Modules

- [Risk Management & Compliance](index.md)
- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [EU AI Act](01-eu-ai-act/index.md)
