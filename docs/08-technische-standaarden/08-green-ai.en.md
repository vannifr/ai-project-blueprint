---
versie: '1.1'
type: technical
layer: 3
roles: [Tech Lead]
tags: [cost]
summary: Guidelines for reducing the ecological footprint of AI systems and embedding sustainability as a strategic design choice.
answers: [What are the technical standards for Green AI & Sustainability?]
---

# Green AI & Sustainability

!!! abstract "Purpose"
    Guidelines for reducing the ecological footprint of AI systems and embedding sustainability as a strategic design choice.

AI systems have a substantial ecological footprint. The electricity demand for AI computing power is growing rapidly: it is expected to be **11 times higher** in 2030 than in 2023. For project managers, sustainability is therefore not an afterthought but a strategic decision that must be made as early as the Business Understanding phase.

!!! info "Why now?"
    Rising energy prices make sustainable choices financially attractive too. Energy-efficient models and smart scheduling are not only good for the climate — they directly reduce operational costs.

Sources: \[so-47\], \[so-48\]

______________________________________________________________________

## 1. The Ecological Footprint of AI

### Energy

- A single AI query consumes an estimated **0.3–0.8 Wh** of electricity — up to 10 times more than a standard search query. The exact value depends on model size and modality.
- Training a large language model can emit **hundreds to thousands of tonnes of CO₂**, depending on model size and infrastructure — equivalent to hundreds or thousands of transatlantic flights.
- Data centres are responsible for approximately **2% of global greenhouse gas emissions**.

### Water

- For every kilowatt-hour a data centre consumes, approximately **2 litres of water** are required for cooling.
- By 2030, water consumption by data centres is expected to triple to **664 billion litres per year**.

### Hardware

- Rapid hardware refresh cycles lead to large quantities of e-waste containing specialised metals that are difficult to recycle.

Sources: \[so-47\], \[so-48\]

______________________________________________________________________

## 2. Reduction Potential

Research from Cornell University (2025) shows that the ecological impact of AI can be drastically reduced by combining two measures:

| Measure                                                                       | CO₂ reduction     | Water reduction   |
| :---------------------------------------------------------------------------- | :---------------- | :---------------- |
| Smart siting (data centres in regions with low water stress and green energy) | up to 73%         | up to 86%         |
| Grid decarbonisation (transition to renewable energy sources)                 | additional effect | additional effect |

Source: \[so-47\]

______________________________________________________________________

## 3. Practical Measures per Project Phase

### Phase 1 — Discovery & Strategy

**Model selection as a sustainability consideration:**

- Choose "lean" models or *knowledge distillation* (transferring knowledge from a large to a small model) when the task allows. According to compression research (Polino et al.), this can reduce operational emissions by **up to 80%**, though actual savings are task-dependent.
- Document the choice of a specific model including the motivation for the model size in the [Technical Model Card](../09-sjablonen/02-business-case/modelkaart.md).

**Questions at model selection:**

- [ ] Is a smaller specialised model sufficient for this task?
- [ ] Does the vendor provide transparency on energy consumption and data centre location?
- [ ] Are there alternatives with comparable performance on green infrastructure?

______________________________________________________________________

### Phase 3 — Development

**Temporal Workload Shifting:**

- Schedule non-urgent training tasks at times when there is a surplus of solar or wind energy available on the grid. This leads to an average of **40% fewer emissions** for the same computation.
- Consider carbon-aware schedulers (e.g. via the Carbon Aware SDK from the Green Software Foundation).

**Green Coding Guidelines:**

- [ ] Avoid unnecessary API calls: use caching for repeated queries (see also [Cost Optimisation](07-kostenoptimalisatie.md))
- [ ] Minimise prompt length without quality loss
- [ ] Limit model response length where possible (`max_tokens`)
- [ ] Use batch processing for non-real-time tasks

______________________________________________________________________

### Phase 5 — Monitoring & Optimisation

**Continuous monitoring of ecological KPIs:**

| KPI                         | Measurement                              | Threshold                                                                           |
| :-------------------------- | :--------------------------------------- | :---------------------------------------------------------------------------------- |
| Energy per query (Wh)       | Monitoring via cloud provider dashboards | Define at project start                                                             |
| CO₂ per month (kg)          | Via provider reporting or external tool  | Declining trend                                                                     |
| Cost per Productive Outcome | See GAINS™ framework                     | Link to [Benefits Realisation](../10-doorlopende-verbetering/04-batenrealisatie.md) |

______________________________________________________________________

## 4. Decision Framework: When is AI Sustainably Justified?

Ask yourself the following questions at every AI initiative:

1. **Is the problem large enough?** Does the value creation outweigh the energy cost?
1. **Is there a leaner alternative?** A simple rule-based system or a small specialised model may be better than a large foundation model.
1. **Is the energy being decarbonised?** Does your cloud provider choose renewable energy?
1. **Is hardware being managed responsibly?** Is there a plan for hardware lifecycle and e-waste?

!!! tip "Governance anchor point"
    Record the answers to the above questions in the [Goal Card (Doelkaart)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) as part of the Hard Boundaries. An AI system whose environmental costs do not outweigh the social benefits does not meet the responsible deployment criteria of this blueprint.

______________________________________________________________________

## 5. Related Modules

- [Cost Optimisation](07-kostenoptimalisatie.md)
- [AI Architecture](05-ai-architectuur.md)
- [Goal Card (Doelkaart)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Benefits Realisation](../10-doorlopende-verbetering/04-batenrealisatie.md)
- [Sources & Inspiration](../16-bronnen/index.md)
