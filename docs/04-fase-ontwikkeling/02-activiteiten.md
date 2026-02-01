# ?? Kernactiviteiten & RACI (Realisatie)
## Documentbeheer
- **Document-ID:** MOD-02
- **Titel:** ?? Kernactiviteiten & RACI (Realisatie)
- **Versie:** 1.0
- **Status:** Definitief
- **Eigenaar:** AI Competence Center
- **Laatst herzien:** 2026-02-01
- **Wijziging t.o.v. vorige versie:** Header gestandaardiseerd en versie naar 2.2 gezet.

---

## 3. Kernactiviteiten

### Activiteit 3.1: Datastromen Automatiseren
Het opzetten van pijplijnen die data automatisch opschonen en aanleveren (geen handwerk meer).

*   **Data Pipelines:** Geautomatiseerde ETL-processen (Extract, Transform, Load)
*   **Kwaliteitscontroles:** Automatische validatie van inkomende data
*   **Versiebeheer:** Tracking van data-wijzigingen en lineage

### Activiteit 3.2: Kenniskoppeling & Afstellen
Het verbinden van de AI aan interne documenten en het **Afstellen van het model** voor optimale prestaties.

*   **Kenniskoppeling (RAG):** Verbinden van de AI aan interne documenten, FAQ's, procedures.
*   **Prompt Engineering:** Optimaliseren van de **Sturingsinstructies**.
*   **Model-Afstelling:** Aanpassen van parameters voor specifieke use case.

### Activiteit 3.3: Specificatie-eerst Methode
We schrijven eerst de verwachte uitkomst (de test), dan pas de implementatie. Zo borgen we kwaliteit.

*   **Test-Driven Development voor AI:** Definieer eerst wat het systeem moet doen.
*   **Acceptatiecriteria:** Heldere, meetbare eisen per functionaliteit.
*   **Geautomatiseerde Tests:** Continue validatie bij elke wijziging.

### Activiteit 3.4: Validatie op Drie Niveaus
Elke wijziging wordt getoetst op drie dimensies:

#### 1. Syntactisch
*   **Vraag:** Werkt de code? Geen crashes of errors?
*   **Check:** Unit tests, integration tests

#### 2. Technische Realisatie & Pijplijnen
*   **Data Pijplijnen:** Inrichten van robuuste stromen voor training en inferentie.
*   **Automated Gates (Governance-as-Code):** Integreer de **Rode Lijnen** en succes-metrics direct in de CI/CD-pipeline.
    *   *Voorbeeld:* De build faalt automatisch als de bias-score te hoog is of de accuraatheid onder de drempelwaarde zakt.
*   **Continuous Testing (CT):** Geautomatiseerde evaluatie van model-outputs bij elke wijziging in de **Sturingsinstructies**.

---
#### 3. Gedrag
*   **Vraag:** Doet het wat we verwachten?
*   **Check:** Functionele tests, regressie tests

#### 4. Doelgericht
*   **Vraag:** Helpt het de gebruiker? Levert het waarde?
*   **Check:** User acceptance testing, A/B testing

## ?? 4. Team & Rollen (RACI)

| Rol | Verantwoordelijkheid in Realisatie |
| :--- | :--- |
| **Data Scientist** | **R**esponsible: Ontwikkeling van AI-modellen en **Kenniskoppeling**. |
| **ML Engineer** | **R**esponsible: Bouwen van data pipelines en infrastructuur. |
| **AI Product Manager** | **A**ccountable: Eigenaar van de product backlog en prioritering. |
| **QA Engineer** | **R**esponsible: Uitvoeren van geautomatiseerde tests en validatie. |
| **DevOps** | **C**onsulted: Adviseert over **Ingebruikname** en infrastructuur. |

---
**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Definitief

---
---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.



