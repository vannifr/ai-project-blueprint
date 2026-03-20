---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [Data Scientist]
tags: [quick-reference]
answers: [What is the quick reference for Cheatsheet — Golden Set?]
---

# Cheatsheet — Golden Set

**Source:** [Validation Report](../07-validatie-bewijs/validatierapport.md)

______________________________________________________________________

## What is a Golden Set?

A **Golden Set** is a fixed collection of input-output pairs with known, correct answers. It is the benchmark for measuring the quality of your AI system.

______________________________________________________________________

## Minimum Composition

| Criterion          | Minimum value   | Recommended       |
| :----------------- | :-------------- | :---------------- |
| Number of examples | 50              | 200+              |
| Use case coverage  | 80%             | 100%              |
| Edge cases         | 10% of set      | 20%               |
| Raters per item    | 1               | 2–3 (inter-rater) |
| Update frequency   | On model change | Quarterly         |

______________________________________________________________________

## Build in 4 Steps

```
1. Collect real user queries (or synthetic if no data available)
2. Have domain experts establish correct outputs
3. Categorise by use case + difficulty level
4. Lock the set — modify only via formal process
```

______________________________________________________________________

## Quality Thresholds

| Metric                                                                         | Threshold (Go)  | Action on failure           |
| :----------------------------------------------------------------------------- | :-------------- | :-------------------------- |
| Accuracy (classification)                                                      | ≥ 85%           | Retrain or optimise prompts |
| F1-score                                                                       | ≥ 0.80          | Check class imbalance       |
| Human rating                                                                   | ≥ 4.0/5.0       | Review prompt design        |
| Hallucination rate                                                             | ≤ 5%            | Improve RAG quality         |
| Latency p95 (95th percentile — 95% of all requests are faster than this value) | ≤ \[budget\] ms | Consider model tiering      |

______________________________________________________________________

## Pitfalls

!!! warning "Avoid these mistakes"
    - Using the Golden Set as **training data** (contamination)
    - Not updating the set after **domain changes** (concept drift)
    - Including only happy-path cases (no edge cases)
    - Single rater per item (no inter-rater agreement)

**Source for full approach:** [Validation report template](../07-validatie-bewijs/validatierapport.md)
