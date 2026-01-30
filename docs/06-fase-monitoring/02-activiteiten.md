# Kernactiviteiten (Monitoring)

## Activiteit 7.1: Technische Monitoring & MLOps
Het operationeel houden van de machinekamer.
*   **Infrastructure Monitoring:** Bewaken van *uptime*, *latency* en kosten.
*   **Model Performance Tracking:** Continu meten van metrieken (bijv. nauwkeurigheid) tegen de *baseline*.
*   **Drift Detectie:** Identificeren wanneer de inputdata teveel afwijkt van de trainingsdata (*Data Drift*) of wanneer de relaties in de data veranderen (*Concept Drift*).

## Activiteit 7.2: Business & Ethiek Monitoring
Rapportage over de werkelijke impact.
*   **KPI Rapportage:** Dashboards die de ROI en andere business doelen tonen.
*   **Ethische Audits:** Periodieke controle op bias en ongewenst gedrag in productie.
*   **Hallucinatie Monitoring:** Systematisch in kaart brengen van foutieve of onvoorspelbare outputs.

## Activiteit 7.3: Retraining & Optimalisatie
Het verbeteren van het systeem op basis van feiten.
*   **Feedback Analyse:** Verwerken van gebruikersbeoordelingen (duimpjes omhoog/omlaag).
*   **Model Verversing:** Het model opnieuw trainen of de prompts aanpassen op basis van nieuwe data.
*   **Release Management:** Versiebeheer van verbeteringen via de gevestigde CI/CD pijplijnen.

## Activiteit 7.4: Incident Respons
Snel handelen bij afwijkingen.
*   **Alerting:** Meldingen bij kritieke fouten of grote dalingen in kwaliteit.
*   **Kill Switch:** Indien nodig de AI-functie tijdelijk uitschakelen bij onvoorspelbaar gedrag.
*   **Root Cause Analyse:** Onderzoeken en oplossen van incidenten.

## Team & Rollen (RACI)

| Rol | Verantwoordelijkheid in Monitoring |
| :--- | :--- |
| **MLOps Engineer** | **R**esponsible: Beheert de technische monitoring en infrastructuur. |
| **Data Scientist** | **R**esponsible: Analyseert model-drift en adviseert over retraining. |
| **AI Product Manager** | **A**ccountable: Rapporteert over batenrealisatie en business KPI's. |
| **IT Support / Ops** | **R**esponsible: Eerste lijn bij incidenten en beschikbaarheid. |
| **Chief AI Officer** | **C**onsulted: Ontvangt periodieke rapportages over risico's en waarde. |

---

© 2026 AI Project Playbook. Door **Frederik Vannieuwenhuyse** & **Hadrien-Joseph van Durme**. Gelicenseerd onder CC BY-NC-SA 4.0.

