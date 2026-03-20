---
versie: '1.0'
type: guide
layer: 2
roles: [Data Scientist]
tags: [onboarding, validation]
answers: [How does Minimal Validation Report work?]
---

# Minimal Validation Report

## Instructions

Complete this report on days 18–20 in preparation for the Gate 1 Review (day 21). The report is intentionally brief: **2 pages, 60–90 minutes to complete**.

The full version of the validation report is available at [Validation Report (full)](../09-sjablonen/07-validatie-bewijs/validatierapport.md).

______________________________________________________________________

**Project:** \[Name\]
**Period:** \[Start date\] – \[End date prototype\]
**AI PM:** \[Name\]
**Developer:** \[Name\]
**Sponsor:** \[Name\]
**Gate 1 Review date:** \[Date\]

______________________________________________________________________

## Section 1 — What did we build?

### 1.1 Solution Description (3–5 sentences)

\[Describe the prototype. What does the system do? How does it work? Which technology was used? Which collaboration mode (1–4)?

E.g.: We built a document Q&A system that answers questions about our internal policy manuals. The system uses RAG (Retrieval-Augmented Generation) to retrieve relevant passages and formulate an answer. The end user asks a question via a Jupyter notebook interface; the system returns an answer plus the source passages. A staff member reviews the answer before use (Mode 2 — Advisory).\]

### 1.2 Technical Configuration

| Parameter          | Value                                                       |
| :----------------- | :---------------------------------------------------------- |
| AI model / API     | \[e.g. Claude claude-haiku-4-5 via Anthropic API\]          |
| Data source        | \[e.g. 45 internal PDF policy documents, total 320 pages\]  |
| Interface          | \[e.g. Jupyter notebook / Python script / Simple web page\] |
| Collaboration Mode | \[e.g. Mode 2 — Advisory\]                                  |
| Repository         | \[e.g. GitHub repo link or internal location\]              |

______________________________________________________________________

## Section 2 — Does it work? (Golden Set Results)

### 2.1 Test Setup

| Parameter                         | Value                                             |
| :-------------------------------- | :------------------------------------------------ |
| Number of test cases (Golden Set) | \[e.g. 20\]                                       |
| Created by                        | \[e.g. Name of domain expert, not the developer\] |
| Test date                         | \[Date\]                                          |
| Edge cases                        | \[e.g. 4 of the 20 cases\]                        |

### 2.2 Results

| Category             | Count | Percentage                                  |
| :------------------- | :---- | :------------------------------------------ |
| ✅ Correct           |       |                                             |
| ⚠️ Partially correct |       |                                             |
| ❌ Wrong             |       |                                             |
| **Quality score**    |       | **(Correct + 0.5 × Partially) / 20 × 100%** |

**Quality score:** \_\_\_%

### 2.3 Notable Findings

*Describe up to 3 notable successes or shortcomings.*

| #   | Finding                                                                        | Cause                         | Impact              |
| :-- | :----------------------------------------------------------------------------- | :---------------------------- | :------------------ |
| 1   | \[E.g. System performs poorly on questions about legislation older than 2020\] | \[E.g. Old PDFs not indexed\] | \[Low/Medium/High\] |
| 2   |                                                                                |                               |                     |
| 3   |                                                                                |                               |                     |

______________________________________________________________________

## Section 3 — What did we learn?

*Note 3–5 concrete lessons. Focus on insights that are valuable for the next phase, not on technical details.*

| #   | Lesson                                                                               | Recommendation for next phase                                     |
| :-- | :----------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| 1   | \[E.g. Data quality of old PDFs is a bigger bottleneck than expected.\]              | \[E.g. Invest in document hygiene before Phase 2.\]               |
| 2   | \[E.g. Domain experts ask many questions about context not found in the documents.\] | \[E.g. Consider a FAQ supplement or explicit scope delineation.\] |
| 3   |                                                                                      |                                                                   |
| 4   |                                                                                      |                                                                   |
| 5   |                                                                                      |                                                                   |

______________________________________________________________________

## Section 4 — Recommendation

### 4.1 Final Assessment

*Choose one option and justify in no more than 3 sentences.*

- [ ] ✅ **Go** — The prototype demonstrates the value of the use case. We proceed to the Builder phase with a full project charter.
- [ ] 🔄 **Pivot** — The use case is feasible, but we adjust the scope/approach. \[Describe the pivot.\]
- [ ] ⛔ **No-Go** — The prototype has not demonstrated the value. We stop the project and document the lessons.

**Justification (max. 3 sentences):**

\[E.g. The prototype achieves a quality score of 85% on the Golden Set and saves an average of 8 minutes processing time per e-mail. The technical approach is feasible and data quality is sufficient. We recommend Go provided the scope is explicitly limited to English-language e-mails.\]

### 4.2 Preconditions for Go (only for Go decisions)

*What needs to be in place before the Builder phase starts?*

- [ ] \[E.g. Formal Guardian appointed (name: \_\_\_)\]
- [ ] \[E.g. Privacy Impact Assessment completed for personal data in e-mails\]
- [ ] \[E.g. Budget approved for production infrastructure (€ \_\_\_)\]
- [ ] \[E.g. Full Project Charter completed before \[date\]\]

______________________________________________________________________

## Gate 1 Review Decision

|                                       |     |
| :------------------------------------ | :-- |
| **Decision (Go / No-Go / Pivot):**    |     |
| **Date:**                             |     |
| **Sponsor name:**                     |     |
| **Signature / E-mail confirmation:**  |     |
| **Sponsor justification (optional):** |     |

______________________________________________________________________

## Related Modules

- [30-Day Plan](01-30-dagen-plan.md)
- [Full Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
- [Phase 3: Development (next step after Go)](../04-fase-ontwikkeling/01-doelstellingen.md)
- [Lessons Learned Template](../11-project-afsluiting/01-lessons-learned.md)
