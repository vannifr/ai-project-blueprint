---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 1. Governance Model

## 1. Doel

Het definiëren van de besluitvormingsstructuren, rollen en verantwoordelijkheden om AI-projecten veilig en effectief te sturen.

______________________________________________________________________

## 2. Structuur

Het governance model bestaat uit drie lagen die samenwerken om strategie, operatie en techniek te verbinden:

1. **Strategisch Niveau:** Focus op visie en **Het Kostenoverzicht**.
1. **Operationeel Niveau:** Focus op uitvoering en prioriteit.
1. **Technisch Niveau:** Focus op kwaliteit en **Ingebruikname**.

______________________________________________________________________

## 3. Verantwoordelijkheden

| Rol                          | Niveau        | Kernverantwoordelijkheden                                           |
| :--------------------------- | :------------ | :------------------------------------------------------------------ |
| **CAIO** (Chief AI Officer)  | Strategisch   | Strategie, ROI oversight, Governance eindverantwoordelijkheid.      |
| **Executive Committee**      | Strategisch   | Budgetgoedkeuring, strategische alignment.                          |
| **AI Product Manager**       | Operationeel  | Gebruikscasus prioriteit, Stakeholder management, Backlog eigenaar. |
| **AI Transformation Office** | Operationeel  | Procesbewaking, standaardisatie, training.                          |
| **Data Scientist**           | Technisch     | Model development, validatie, experimentatie.                       |
| **ML Engineering**           | Technisch     | **Ingebruikname** pipelines, monitoring, infrastructuur.            |
| **Guardian (Ethicist)**      | Ondersteunend | Eerlijkheidstoetsen, Bias audits, Compliance checks.                |
| **Security Officer**         | Ondersteunend | Security maatregelen, Privacy waarborging.                          |

______________________________________________________________________

## 4. Besluitvormingsproces (Gate Model)

```mermaid
flowchart TD
    A[Initiatief] --> B{Gate 1 (Go/No-Go Ontdekking): Verkenning}
    B -->|Go| C[Validatie]
    B -->|No Go| X[Stop]
    C --> D{Gate 2 (Investering PoV): Kostenplaatje}
    D -->|Go| E[Realisatie]
    D -->|No Go| X
    E --> F{Gate 3 (Productie-klaar): Ingebruikname}
    F -->|Go| G[Beheer & Optimalisatie]
    F -->|No Go| X
    G --> H{Gate 4 (Livegang): Continue?}
    H -->|Ja| A
    H -->|Nee| I[Afsluiting]
```

## 5. Gate Reviews

Elke gate fungeert als een harde stop/go beslissing. Zie de [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) voor specifieke criteria per fase.

______________________________________________________________________
