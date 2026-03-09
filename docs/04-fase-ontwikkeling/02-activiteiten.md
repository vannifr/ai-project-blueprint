---
versie: '1.0'
---

# 1. Kernactiviteiten & Rollen (Realisatie)

## 1. Kernactiviteiten

### Datastromen Automatiseren

Het opzetten van pijplijnen die data automatisch opschonen en aanleveren (geen handwerk meer).

- **Data Pipelines:** Geautomatiseerde ETL-processen (Extract, Transform, Load)
- **Kwaliteitscontroles:** Automatische validatie van inkomende data
- **Versiebeheer:** Tracking van data-wijzigingen en lineage

### RAG & Fine-tunen

Het verbinden van de AI aan interne documenten en het **Fine-tunen** voor optimale prestaties.

- **RAG:** Verbinden van de AI aan interne documenten, FAQ's, procedures.
- **Prompt Engineering:** Optimaliseren van de **Prompts**.
- **Model-Afstelling:** Aanpassen van parameters voor specifieke gebruikscasus.

### Specificatie-eerst Methode

We schrijven eerst de verwachte uitkomst (de test), dan pas de implementatie. Zo borgen we kwaliteit.

- **Test-Driven Development voor AI:** Definieer eerst wat het systeem moet doen.
- **Acceptatiecriteria:** Heldere, meetbare eisen per functionaliteit.
- **Geautomatiseerde Tests:** Continue validatie bij elke wijziging.

### Variant: SaaS & Inkoop (Buy vs. Build)

Niet alle AI-oplossingen worden zelf gebouwd. Bij aanschaf van standaard AI-software (SaaS) verandert de focus van de Realisatie-fase:

- **Van Bouwen naar Configureren:** Focus op het instellen van de juiste systeem-prompts, RAG-kennisbronnen en veiligheidsfilters binnen de leveranciersomgeving.
- **Validatie blijft Identiek:** Ook een gekochte tool moet slagen voor de **Proof of Value (PoV)** en de **Golden Set** test voordat deze live gaat. Vertrouw niet blind op de "demo" van de leverancier.
- **Modelkaart wordt Configuratiekaart:** Documenteer welke instellingen, plugins en data-connecties actief zijn.
- **Vendor Lock-in Check:** Controleer of data en logs exporteerbaar zijn voor compliance (EU AI Act).

______________________________________________________________________

### Validatie op Drie Niveaus

Elke wijziging wordt getoetst op drie dimensies:

#### Syntactisch

- **Vraag:** Werkt de code? Geen crashes of errors?
- **Check:** Unit tests, integration tests

#### Technische Realisatie & Pijplijnen

- **Data Pijplijnen:** Inrichten van robuuste stromen voor training en inferentie.
- **Automated Gates (Governance-as-Code):** Integreer de **Rode Lijnen** en succes-metrics direct in de CI/CD-pipeline.
- *Voorbeeld:* De build faalt automatisch als de bias-score te hoog is of de accuraatheid onder de drempelwaarde zakt.
- **Continuous Testing (CT):** Geautomatiseerde evaluatie van model-outputs bij elke wijziging in de **Prompts**.

______________________________________________________________________

#### Gedrag

- **Vraag:** Doet het wat we verwachten?
- **Check:** Functionele tests, regressie tests

#### Doelgericht

- **Vraag:** Helpt het de gebruiker? Levert het waarde?
- **Check:** User acceptance testing, A/B testing

## 2. Team & Rollen

| Rol                    | Verantwoordelijkheid in Realisatie                                  |
| ---------------------- | ------------------------------------------------------------------- |
| **Data Scientist**     | **R**esponsible: Ontwikkeling van AI-modellen en **RAG**.           |
| **ML Engineer**        | **R**esponsible: Bouwen van data pipelines en infrastructuur.       |
| **AI Product Manager** | **A**ccountable: Eigenaar van de product backlog en prioritering.   |
| **QA Engineer**        | **R**esponsible: Uitvoeren van geautomatiseerde tests en validatie. |
| **DevOps**             | **C**onsulted: Adviseert over **Ingebruikname** en infrastructuur.  |

______________________________________________________________________

## 5. Gerelateerde Modules

**Sjablonen:**

- [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)

**Verdieping:**

- [Spec-Driven Development](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)
- [SDD Patroon](05-sdd-patroon.md)

**Zie ook:** [Overzicht Fase 3](01-doelstellingen.md) · [Afleveringen](03-afleveringen.md)
