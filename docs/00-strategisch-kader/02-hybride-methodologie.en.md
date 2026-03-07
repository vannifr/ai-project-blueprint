---
versie: '1.0'
---

# 1. Hybrid Methodology

## 1. Objective

This document describes the hybrid approach of the AI Project Blueprint, combining predictable planning (Waterfall) with iterative execution (Agile) for an optimal balance between structure and flexibility.

______________________________________________________________________

## 2. Concept

The hybrid methodology recognises that AI projects require strict milestones for budgeting and compliance on the one hand, and extreme flexibility during model development on the other.

### Predictable Elements (Waterfall)

- Strategic planning and **Cost Overview**.
- Compliance and governance checkpoints.
- Risk inventory.
- Milestone planning (**Gates**).

### Iterative Elements (Agile)

- **Model Fine-Tuning**.
- User feedback loops.
- *Experiment-driven development*.
- Continuous improvement (*Kaizen*).

______________________________________________________________________

## 3. Practical Implementation

```mermaid
gantt
 title Hybrid Methodology
 dateFormat YYYY-MM-DD
 section Predictable
 Discovery & Strategy :p1, 2024-01-01, 2w
 Cost Overview :p2, after p1, 1w
 section Iterative
 Development Sprints 1-4 :s1, after p2, 4w
 section Predictable
 Gate 3 (Production-Ready) Review :m1, after s1, 1w
 section Iterative
 Development Sprints 5-8 :s2, after m1, 4w
```

______________________________________________________________________

## 4. Benefits

- **Structure:** Clear planning and governance for management.
- **Flexibility:** Rapid adaptation to new data insights for the team.
- **Risk Management:** Proactive risk identification and mitigation.
- **Compliance:** Integrated EU AI Act compliance reviews.

______________________________________________________________________
