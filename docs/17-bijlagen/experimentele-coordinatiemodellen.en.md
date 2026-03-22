---
versie: '1.0'
type: reference
layer: 3
roles: [Data Scientist]
tags: [governance]
answers: [What is Experimental Coordination Models?]
---

# 1. Experimental Coordination Models

!!! warning "Experimental"
    The models in this document are academically supported but not broadly validated in commercial software teams. They are intended as inspiration for highly mature organisations ([Visionary profile](../13-organisatieprofielen/03-ai-expert.md)) that wish to reconsider traditional coordination mechanisms.

## 1. Purpose

Traditional Agile coordination (standups, sprint planning, retrospectives) was designed for human teams. As AI agents take over a larger share of execution work, the question arises whether coordination forms exist that better suit human-machine teams. This document describes four experimental models from academic literature.

______________________________________________________________________

## 2. Stigmergic Coordination

### Concept

Stigmergy is coordination through the environment rather than through direct communication. The term comes from biology (termites coordinate construction by leaving pheromone trails, not by holding meetings).

In software teams this means: agents and people coordinate through the work product itself — code commits, documentation changes, issue statuses and test results form the "pheromone trails" that steer the next action.

### How It Works

1. Agent A completes a task and commits code.
1. The commit automatically triggers tests and quality checks.
1. Agent B detects the change, analyses the impact on its domain and adapts.
1. No explicit handoff or meeting required.

### Academic Basis

- Kevin Crowston (Syracuse University) published extensively on stigmergic coordination in FLOSS development (Free/Libre Open Source Software).
- The MIDST tool (ACM CSCW) implemented stigmergic coordination for data science teams with positive results.

### When to Consider

- Teams with a high proportion of agent-driven tasks (Mode 4-5)
- Asynchronous, geographically distributed teams
- Open-source projects with changing contributors

### Risks

- Requires excellent observability (who did what, why)
- Can lead to conflicting changes without a good branching strategy
- Less suitable for tasks requiring complex human alignment

______________________________________________________________________

## 3. Prediction Market Model

### Concept

Team members "trade" in success contracts for project components. The market price reflects the collective estimate of the probability of success and reveals hidden risks that remain invisible in traditional estimation methods.

### How It Works

1. For each milestone or deliverable a "contract" is created.
1. Team members buy or sell contracts based on their assessment of the probability of success.
1. A falling price signals hidden problems that the team does not explicitly name.
1. A rising price confirms confidence in the approach.

### Academic Basis

- Microsoft has run multiple internal prediction markets, including for software project estimation (Microsoft Research).
- Google, GE, HP and Best Buy have deployed corporate prediction markets.

### When to Consider

- Large teams (>10 people) where implicit knowledge is distributed
- Projects with high uncertainty about feasibility
- As a supplement to, not replacement for, standard estimation techniques

### Risks

- Optimism bias: employees do not trade against their own project
- Requires psychological safety (honest "selling" without repercussions)
- Small teams have insufficient "liquidity" for meaningful market prices

______________________________________________________________________

## 4. Immune System Model

### Concept

Autonomous agents continuously monitor for "pathogens" (bugs, technical debt, security vulnerabilities, drift) and neutralise them without a central command structure. Comparable to how the biological immune system works: distributed, adaptive and self-regulating.

### How It Works

1. **Detection agents** continuously scan codebases, logs and metrics.
1. Upon detecting an anomaly, a **response agent** is triggered.
1. The response agent classifies the problem and applies mitigation (or escalates to a human).
1. The system "remembers" previous patterns (episodic memory) and responds faster to known threats.

### Academic Basis

- Artificial Immune Systems (AIS) is a recognised computational paradigm with decades of research.
- Applications in intrusion detection, software fault detection and anomaly detection are documented in ACM, IEEE and ScienceDirect.

### When to Consider

- Large production environments with many AI systems (Visionary profile)
- Supplement to existing [performance degradation detection](../06-fase-monitoring/05-drift-detectie.md)
- Environments where response time is critical

### Risks

- Requires highly mature observability and agent governance
- Autonomous correction can have unintended side effects
- Must always operate within [Circuit Breaker](../00-strategisch-kader/06-has-h-niveaus.md) frameworks

______________________________________________________________________

## 5. Narrative-Driven System

### Concept

Instead of steering on fragmented user stories and features, the team steers on coherent narratives about the system. A "system narrative" describes how a user experiences the system from start to finish, including edge cases and failure scenarios.

### How It Works

1. The team writes and maintains a readable system narrative.
1. AI agents receive the narrative as context and generate code that fits within the larger story.
1. Changes are assessed against the narrative: "does this feature fit the story?"
1. The narrative evolves along with the system.

### When to Consider

- Products with complex user journeys
- Teams struggling to maintain the "big picture" during AI-driven development
- As a complement to the [Objective Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)

### Risks

- Requires strong writing skills and discipline to keep the narrative current
- Can conflict with traditional backlog-driven approaches
- Less suitable for purely technical systems without user interaction

______________________________________________________________________

## 6. Related Modules

- [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [The Visionary (Organisation Profile)](../13-organisatieprofielen/03-ai-expert.md)
- [Performance Degradation Detection](../06-fase-monitoring/05-drift-detectie.md)
- [Objective Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)

______________________________________________________________________
