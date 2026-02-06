---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 1. Kernactiviteiten & Rollen (Realisatie)

## 1. Kernactiviteiten

### Datastromen Automatiseren

Het opzetten van pijplijnen die data automatisch opschonen en aanleveren (geen handwerk meer).

- **Data Pipelines:** Geautomatiseerde ETL-processen (Extract, Transform, Load)
- **Kwaliteitscontroles:** Automatische validatie van inkomende data
- **Versiebeheer:** Tracking van data-wijzigingen en lineage

### Kenniskoppeling & Afstellen

Het verbinden van de AI aan interne documenten en het **Afstellen van het model** voor optimale prestaties.

- **Kenniskoppeling (RAG):** Verbinden van de AI aan interne documenten, FAQ's, procedures.
- **Prompt Engineering:** Optimaliseren van de **Sturingsinstructies**.
- **Model-Afstelling:** Aanpassen van parameters voor specifieke gebruikscasus.

### Specificatie-eerst Methode

We schrijven eerst de verwachte uitkomst (de test), dan pas de implementatie. Zo borgen we kwaliteit.

- **Test-Driven Development voor AI:** Definieer eerst wat het systeem moet doen.
- **Acceptatiecriteria:** Heldere, meetbare eisen per functionaliteit.
- **Geautomatiseerde Tests:** Continue validatie bij elke wijziging.

### Validatie op Drie Niveaus

Elke wijziging wordt getoetst op drie dimensies:

#### Syntactisch

- **Vraag:** Werkt de code? Geen crashes of errors?
- **Check:** Unit tests, integration tests

#### Technische Realisatie & Pijplijnen

- **Data Pijplijnen:** Inrichten van robuuste stromen voor training en inferentie.
- **Automated Gates (Governance-as-Code):** Integreer de **Rode Lijnen** en succes-metrics direct in de CI/CD-pipeline.
- *Voorbeeld:* De build faalt automatisch als de bias-score te hoog is of de accuraatheid onder de drempelwaarde zakt.
- **Continuous Testing (CT):** Geautomatiseerde evaluatie van model-outputs bij elke wijziging in de **Sturingsinstructies**.

______________________________________________________________________

#### Gedrag

- **Vraag:** Doet het wat we verwachten?
- **Check:** Functionele tests, regressie tests

#### Doelgericht

- **Vraag:** Helpt het de gebruiker? Levert het waarde?
- **Check:** User acceptance testing, A/B testing

## 2. Team & Rollen

| Rol                    | Verantwoordelijkheid in Realisatie                                    |
| :--------------------- | :-------------------------------------------------------------------- |
| **Data Scientist**     | **R**esponsible: Ontwikkeling van AI-modellen en **Kenniskoppeling**. |
| **ML Engineer**        | **R**esponsible: Bouwen van data pipelines en infrastructuur.         |
| **AI Product Manager** | **A**ccountable: Eigenaar van de product backlog en prioritering.     |
| **QA Engineer**        | **R**esponsible: Uitvoeren van geautomatiseerde tests en validatie.   |
| **DevOps**             | **C**onsulted: Adviseert over **Ingebruikname** en infrastructuur.    |

______________________________________________________________________
