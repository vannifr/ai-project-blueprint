---
versie: '1.0'
description: 'AI-governancemodel: beslissingsbevoegdheden, toezichtstructuren en verantwoordingskaders voor verantwoorde AI-inzet — afgestemd op EU AI Act en PMI-CPMAI vereisten.'
type: strategic
layer: 1
roles: [Data Scientist]
tags: [governance]
summary: Definitie van de besluitvormingsstructuren, rollen en toezichtlagen die AI-projecten veilig en effectief sturen.
answers: [Wat houdt Governance Model in?, Welke rollen heb ik nodig?]
---

# 1. Governance Model

!!! abstract "Doel"
    Definitie van de besluitvormingsstructuren, rollen en toezichtlagen die AI-projecten veilig en effectief sturen.

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

| Rol                          | Niveau        | Kernverantwoordelijkheden                                                    |
| :--------------------------- | :------------ | :--------------------------------------------------------------------------- |
| **CAIO** (Chief AI Officer)  | Strategisch   | Strategie, ROI oversight, Governance eindverantwoordelijkheid.               |
| **Executive Committee**      | Strategisch   | Budgetgoedkeuring, strategische alignment.                                   |
| **AI Product Manager**       | Operationeel  | Gebruikscasus prioriteit, Stakeholder management, Backlog eigenaar.          |
| **AI Transformation Office** | Operationeel  | Procesbewaking, standaardisatie, training.                                   |
| **Data Scientist**           | Technisch     | Model development, validatie, experimentatie.                                |
| **ML Engineering**           | Technisch     | **Ingebruikname** pipelines, monitoring, infrastructuur.                     |
| **Guardian**                 | Ondersteunend | Bewaakt alle grenzen: Fairness Audits, Compliance checks, ethische toetsing. |
| **Security Officer**         | Ondersteunend | Security maatregelen, Privacy waarborging.                                   |

______________________________________________________________________

## 4. Besluitvormingsproces (Gate Model)

```mermaid
flowchart TD
 A["🟢 Initiatief\nIdee of business case"] --> B{"Gate 1\nProbleem helder?\nData beschikbaar?"}
 B -->|"✅ Go"| C["Fase 2: Validatie\nValidatiepilot uitvoeren"]
 B -->|"❌ No Go"| X["⏹ Stop"]
 C --> D{"Gate 2\nInvesteringsbeslissing\nBusiness case goedgekeurd?"}
 D -->|"✅ Go"| E["Fase 3: Realisatie\nProductie-klaar bouwen"]
 D -->|"❌ No Go"| X
 E --> F{"Gate 3\nProductie-gereed?\nAlle tests geslaagd?"}
 F -->|"✅ Go"| G["Fase 4: Beheer\n& Optimalisatie"]
 F -->|"❌ No Go"| X
 G --> H{"Gate 4\nKwartaalreview\nDoorgaan?"}
 H -->|"✅ Ja"| A
 H -->|"❌ Nee"| I["Afsluiting"]
```

## 5. Gate Reviews

Elke gate fungeert als een harde stop/go beslissing. Zie de [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md) voor specifieke criteria per fase.

______________________________________________________________________
