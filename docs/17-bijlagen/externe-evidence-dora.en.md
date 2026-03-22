---
versie: '1.1'
type: reference
layer: 3
tags: [validation]
answers: ['What is External Evidence: DORA (DevOps Research & Assessment)?']
---

# 1. External Evidence: DORA (DevOps Research & Assessment)

## 1. Purpose

This document summarises the key findings from the DORA research programme (DevOps Research and Assessment) regarding AI-assisted software development, including the DORA AI Capabilities Model (2025).

## 2. Key Findings

### Mixed effects on delivery performance

AI-assisted development does not automatically lead to better delivery outcomes. The effects are strongly dependent on context, the type of work and the degree of guidance. Teams should maintain realistic expectations and not rely on AI as a silver bullet for productivity.

### Local process gains do not always translate to delivery

Individual productivity gains (writing code faster, generating documentation faster) do not automatically lead to improved team deliveries. The bottleneck often shifts to other parts of the process, such as code review, integration or validation.

### Small batches and frequent tests remain essential

The fundamental DevOps principles remain fully applicable in AI-assisted development. Small batches, frequent integration and automated tests are even more important when AI-generated code is introduced, because the provenance and quality of that code requires additional validation.

### Trust is built through feedback loops and policies

Teams build trust in AI tools through transparent feedback loops and clear policy guidelines. Without explicit agreements about when and how AI may be used, ambiguity arises that undermines team confidence.

### Adoption requires transparency, learning time and policies

Successful adoption of AI tools requires openness about their use, sufficient time to learn to work with the tools, and clear policy guidelines indicating what is and is not permitted within the team context.

______________________________________________________________________

## 3. DORA AI Capabilities Model (2025)

!!! quote "Key Insight"
    "AI is an amplifier — it magnifies the strengths of high-performing organisations and the dysfunctions of struggling ones."

Based on research with nearly 5,000 technology professionals, DORA identifies seven foundational capabilities that amplify the positive impact of AI adoption on performance. Without these capabilities, AI adoption delivers limited or even negative results.

### Capability 1: Clear and communicated AI stance

A clear organisational policy on AI tools and usage provides psychological safety for experimentation. Without policy, teams either do not dare to experiment or do so in an uncontrolled manner.

**Amplifies:** individual effectiveness, organisational performance, throughput. Reduces friction.

### Capability 2: Healthy data ecosystems

High-quality, accessible and unified internal data. Organisations with fragmented or poor data quality derive less value from AI tools.

**Amplifies:** organisational performance.

### Capability 3: AI-accessible internal data

Connect AI tools to internal codebases, documentation and wikis via *context engineering* (not just prompt engineering). The better AI understands the organisational context, the more relevant the output.

**Amplifies:** individual effectiveness, code quality.

### Capability 4: Strong version control practices

AI increases the velocity of change; version control is the safety net. Frequent rollbacks amplify team performance. Teams that excel at version control benefit more from AI.

**Amplifies:** individual effectiveness, team performance.

### Capability 5: Working in small batches

Counteracts the risk of AI generating large, unstable changes. Small batches keep changes verifiable and manageable.

**Amplifies:** product performance. Reduces friction.

### Capability 6: User-centric focus

Ensures AI-accelerated teams move quickly in the *right* direction. Without user-centricity, AI can actually harm team performance.

**Amplifies:** team performance, product performance, organisational performance.

### Capability 7: Quality internal platforms

Automated, secure pathways that allow AI benefits to scale. Internal platforms act as the "highway" through which AI-generated output flows safely to production.

**Amplifies:** organisational performance.

### Mapping to the Blueprint

| DORA Capability             | Blueprint Module                                                                                                     |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| Clear AI stance             | [Governance Model](../00-strategisch-kader/03-governance-model.md)                                                   |
| Healthy data ecosystems     | [Data Governance](../08-technische-standaarden/10-data-governance.md)                                                |
| AI-accessible internal data | [Context Files Pattern](../04-fase-ontwikkeling/06-engineering-patterns.md#pattern-4-machine-readable-context-files) |
| Strong version control      | [Technical Standards](../08-technische-standaarden/01-mloops-standaarden.md)                                         |
| Working in small batches    | [Engineering Patterns — Limiting Rework](../04-fase-ontwikkeling/06-engineering-patterns.md#4-limiting-rework)       |
| User-centric focus          | [Discovery Phase — Objectives](../02-fase-ontdekking/01-doelstellingen.md)                                           |
| Quality internal platforms  | [MLOps Standards](../08-technische-standaarden/01-mloops-standaarden.md)                                             |

______________________________________________________________________

Source: \[so-28\] — <https://dora.dev/ai/>
