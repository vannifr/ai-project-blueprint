# Kernactiviteiten & RACI (Realisatie)

## 3. Kernactiviteiten

### Activiteit 3.1: Datastromen Automatiseren
Het opzetten van pijplijnen die data automatisch opschonen en aanleveren (geen handwerk meer).

*   **Data Pipelines:** Geautomatiseerde ETL-processen (Extract, Transform, Load)
*   **Kwaliteitscontroles:** Automatische validatie van inkomende data
*   **Versiebeheer:** Tracking van data-wijzigingen en lineage

### Activiteit 3.2: Kenniskoppeling & Afstellen
Het verbinden van de AI aan interne documenten en het fijn-afstellen van de parameters voor optimale prestaties.

*   **Knowledge Base Integratie:** Koppelen van interne documentatie, FAQ's, procedures
*   **Retrieval-Augmented Generation (RAG):** Combineren van AI met bedrijfsspecifieke kennis
*   **Fine-tuning:** Aanpassen van model-parameters voor specifieke use case
*   **Prompt Engineering:** Optimaliseren van de Stuurinformatie

### Activiteit 3.3: Specificatie-eerst Methode
We schrijven eerst de verwachte uitkomst (de test), dan pas de implementatie. Zo borgen we kwaliteit.

*   **Test-Driven Development:** Definieer eerst wat het systeem moet doen
*   **Acceptatiecriteria:** Heldere, meetbare eisen per functionaliteit
*   **Geautomatiseerde Tests:** Continue validatie bij elke wijziging

### Activiteit 3.4: Validatie op Drie Niveaus
Elke wijziging wordt getoetst op drie dimensies:

#### 1. Syntactisch
*   **Vraag:** Werkt de code? Geen crashes of errors?
*   **Check:** Unit tests, integration tests

#### 2. Gedrag
*   **Vraag:** Doet het wat we verwachten?
*   **Check:** Functionele tests, regressie tests

#### 3. Doelgericht
*   **Vraag:** Helpt het de gebruiker? Levert het waarde?
*   **Check:** User acceptance testing, A/B testing

## 4. Team & Rollen (RACI)

| Rol | Verantwoordelijkheid in Realisatie |
| :--- | :--- |
| **Data Scientist** | **R**esponsible: Ontwikkeling van AI-modellen en kenniskoppeling. |
| **ML Engineer** | **R**esponsible: Bouwen van data pipelines en infrastructuur. |
| **AI Product Manager** | **A**ccountable: Eigenaar van de product backlog en prioritering. |
| **QA Engineer** | **R**esponsible: Uitvoeren van geautomatiseerde tests en validatie. |
| **DevOps** | **C**onsulted: Adviseert over deployment en infrastructuur. |

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
