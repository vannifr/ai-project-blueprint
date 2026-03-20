---
versie: '1.0'
type: guide
layer: 2
tags: [onboarding]
summary: This plan guides teams step by step through their **first AI project in 30 days**. It is a concrete, daily checklist that takes you from problem definition to a working prototype and Gate Review…
answers: [How does 30-Day Day-by-Day Plan work?, What roles do I need?]
---

# 30-Day Day-by-Day Plan

!!! abstract "Purpose"
    This plan guides teams step by step through their **first AI project in 30 days**. It is a concrete, daily checklist that takes you from problem definition to a working prototype and Gate Review. Designed for teams without prior AI experience who need structure to start quickly but responsibly.

## 1. Instructions

Use this plan as your daily guide. Tick off each activity when completed. The time estimates are indicative for a team of 2–3 people.

!!! warning "This is a guideline, not a rigid schedule"
    Adapt the planning to your own pace. If you need more time for a step, take it. The goal on day 21 (Gate Review) is sacred — the daily schedule leading up to it is flexible.

______________________________________________________________________

## 2. Week 1 — Foundation (Day 1–5)

### Day 1–2: Project Charter Light

**Goal:** Shared understanding of the problem and the scope.

- [ ] Read the [Explorer Kit Overview](index.md) in full (AI PM, 30 min)
- [ ] Schedule a kick-off session with the team (1–2 hours)
- [ ] Complete sections 1–3 of the [Project Charter Light](02-project-charter-light.md): Problem Statement, Solution Concept, Team Composition
- [ ] Complete section 4: Scope & Exclusions (what we do NOT do)
- [ ] Have the Sponsor approve the charter (signature or e-mail confirmation)
- [ ] Save the charter as `project-charter-v1.md` in your project folder

**Done when:** Charter is completed and approved by the Sponsor.

______________________________________________________________________

### Day 3–4: Quick Risk Pre-Scan

**Goal:** Early identification of blocking risks (legal, ethical, data).

- [ ] Read the [Quick Risk Pre-Scan](03-risk-prescan-quick.md) (AI PM + Guardian if available, 20 min)
- [ ] Work through the 15 questions — record each answer
- [ ] Calculate your risk score (green / amber / red)
- [ ] If **green**: proceed to day 5
- [ ] If **amber**: schedule a 1-hour risk session with a senior stakeholder
- [ ] If **red**: consult the [full Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) and [EU AI Act module](../07-compliance-hub/01-eu-ai-act/index.md) before proceeding — this project requires additional compliance measures
- [ ] Document the risk score and mitigations in the project charter (section 5)

**Done when:** Risk score is determined and documented. No unresolved red flags.

______________________________________________________________________

### Day 5: Team & Roles

**Goal:** Clear mandate for every role for the next 25 days.

- [ ] Confirm who the **AI PM** is (project steering, daily check-in)
- [ ] Appoint a **Guardian** if possible (mini-role: monitor ethics & risk)
- [ ] Schedule a daily stand-up (15 min, asynchronous via Slack/Teams is OK)
- [ ] Create a shared project folder (SharePoint, Notion, GitHub — whatever you already use)
- [ ] Store all artefacts in the project folder: charter, risk scan

**Done when:** Roles are confirmed. Project folder is created and shared.

______________________________________________________________________

## 3. Week 2 — Discovery (Day 6–10)

### Day 6–8: Data Evaluation

**Goal:** Assess whether your data is suitable for the chosen use case.

- [ ] Identify all potential data sources (internal, external, synthetic)
- [ ] Run the Data Evaluation checklist per source:
    - [ ] **Access:** Can we reach the data? (Yes / No / Partially)
    - [ ] **Volume:** Sufficient examples? (\< 100 = red, 100–500 = amber, > 500 = green)
    - [ ] **Quality:** Is the data clean and representative? (Sample of 20 records)
    - [ ] **Privacy:** Does the data contain personal data? (Yes → complete the [Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md))
    - [ ] **Licence:** Are we allowed to use this data for AI training/inference?
- [ ] Assign a data quality score per source (green/amber/red)
- [ ] Select the best data source(s) for your prototype

**Done when:** At least one green data source identified. Privacy risks documented.

______________________________________________________________________

### Day 9–10: Use Case Selection

**Goal:** Choose the optimal use case for a 30-day prototype.

Use the scorecard below. Score each candidate use case from 1 (low) to 3 (high):

| Criterion          | Description                              | Weighting |
| :----------------- | :--------------------------------------- | :-------- |
| **Impact**         | How significant is the problem we solve? | × 2       |
| **Feasibility**    | Can we build this in 2 weeks?            | × 3       |
| **Data available** | Is there a green data source?            | × 2       |
| **Risk**           | Low risk (green pre-scan)?               | × 2       |
| **Visibility**     | Will the Sponsor see results?            | × 1       |

**Calculate:** (Impact × 2) + (Feasibility × 3) + (Data × 2) + (Risk × 2) + (Visibility × 1) = max 30.

- [ ] Score at least 2 candidate use cases with the scorecard
- [ ] Select the use case with the highest score (minimum 18/30 recommended)
- [ ] Document the choice and the rejected alternatives in the project charter
    - 📄 **Document Q&A**: questions about internal documents, manuals, policies
    - 📧 **Email classification**: sorting and prioritising incoming messages
    - ✍️ **Content generation**: structured text or reports

______________________________________________________________________

## 4. Week 3 — Build & Test Prototype (Day 11–17)

### Day 11–15: Build Prototype

**Goal:** A working prototype that can process 20 test cases.

- [ ] Configure the API key and data source
- [ ] Run the first test with 5 sample inputs
- [ ] Refine the prompt or configuration based on initial results
- [ ] Build a minimal interface or script for the Sponsor demo (day 21)
- [ ] Commit all code to your project repository (GitHub or internal)

!!! tip "Keep it simple"
    The prototype does not need to be perfect. A working notebook that processes 20 cases and produces reproducible results is sufficient for Gate 1.

**Done when:** Prototype runs stably and processes input data reproducibly.

______________________________________________________________________

### Day 16–17: Golden Set Test (20 Test Cases)

**Goal:** Objective quality measurement with a reference set.

- [ ] Assemble a Golden Set of **20 representative test cases**:
    - Choose cases that cover the breadth of the problem
    - Include at least 3 edge cases
    - Have a domain expert (not the developer) define the expected outcomes
- [ ] Run the Golden Set through the prototype
- [ ] Score each result: Correct / Partially correct / Wrong
- [ ] Calculate the quality score: (Correct + 0.5 × Partially correct) / 20 × 100%
- [ ] Document deviations and their causes

| Score  | Interpretation                              | Action                              |
| :----- | :------------------------------------------ | :---------------------------------- |
| ≥ 80%  | Good — ready for Gate Review                | Proceed to day 18                   |
| 60–79% | Acceptable — improvement areas identifiable | Adjust prompt, retest once, proceed |
| \< 60% | Insufficient — fundamental issue            | Reconsider the use case or data     |

**Done when:** Quality score documented. Decision made on go/no-go for Gate Review.

______________________________________________________________________

## 5. Week 4 — Reporting & Decision (Day 18–30)

### Day 18–20: Minimal Validation Report

**Goal:** Document the findings for the Gate 1 Review.

- [ ] Open the [Minimal Validation Report](04-validatierapport-minimal.md)
- [ ] Complete section 1: What did we build?
- [ ] Complete section 2: Does it work? (paste the Golden Set results)
- [ ] Complete section 3: What did we learn? (3–5 lessons learned)
- [ ] Complete section 4: Recommendation (Go / No-Go / Pivot)
- [ ] Have the report reviewed by the Guardian (if available)
- [ ] Prepare a 10-minute demo for the Sponsor

**Done when:** Report is complete. Demo is prepared.

______________________________________________________________________

### Day 21: Gate 1 Review

**Goal:** Go/No-Go decision from the Sponsor.

- [ ] Present the demo (10 minutes)
- [ ] Present the quality score and the validation report (5 minutes)
- [ ] Discuss the recommendation (5 minutes)
- [ ] Obtain an explicit decision: **Go / No-Go / Pivot**
- [ ] Document the decision and the rationale in the validation report
- [ ] If **Go**: proceed to the [Builder phase](../13-organisatieprofielen/02-ai-piloot.md) and the [Development phase](../04-fase-ontwikkeling/01-doelstellingen.md)
- [ ] If **No-Go**: document the lessons and archive the project neatly

______________________________________________________________________

### Day 22–30: Iteration or Wrap-up

**Upon Go decision:**

- [ ] Start [Phase 1: Discovery & Strategy](../02-fase-ontdekking/01-doelstellingen.md) in full with the complete Project Charter
- [ ] Appoint a formal Guardian (if you have not already)
- [ ] Schedule the next Gate Review based on the roadmap

**Upon No-Go or Pivot:**

- [ ] Conduct a brief [Lessons Learned](../11-project-afsluiting/01-lessons-learned.md) session (1 hour)
- [ ] Document the 3 most important insights
- [ ] If Pivot: which other use case scored highest?
- [ ] Archive all artefacts in the project folder

______________________________________________________________________

## 6. Related Modules

- [Explorer Kit Overview](index.md)
- [Project Charter Light](02-project-charter-light.md)
- [Quick Risk Pre-Scan](03-risk-prescan-quick.md)
- [Minimal Validation Report](04-validatierapport-minimal.md)
