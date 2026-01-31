# ?? Kernactiviteiten & RACI (Beheer & Optimalisatie)

## 3. Kernactiviteiten

### Activiteit 3.1: Operationele Monitoring & MLOps
We houden de 'hartslag' van het systeem in de gaten.
*   **Real-time Performance Tracking:** Dashboarding van kritieke metrics: Latency (snelheid), Foutpercentages, Uptime, Throughput.
*   **Prestatieverloop Meten:** Statistisch monitoren of de invoerdata in productie afwijkt van de trainingsdata (*Data Drift*) of als de relatie tussen data en uitkomst verandert (*Concept Drift*).
*   **Data Loop Integratie:** Terugkoppelen van productie-data en uitkomsten naar de ontwikkelomgeving voor analyse (Feedback Loop).
*   **Geautomatiseerde Triggers:** Alerts instellen voor dalingen onder drempelwaarden (bv. accuracy < 85%).

### Activiteit 3.2: Continue Verbetering & Retraining
Stilstand is achteruitgang.
*   **Retraining Strategie:** Wanneer trainen we opnieuw? (Periodiek? Bij drift-alert? Bij nieuwe data?).
*   **Experiment Loops:** Gebruik productie-inzichten om nieuwe hypotheses te testen in korte sprints (A/B testing, Canary releases).
*   **Backlog Management:** Beheer een levende lijst van bugs, verbeterpunten en feature requests vanuit gebruikers.

### Activiteit 3.3: Kostenbeheersing & Energie-efficiëntie
Duurzaamheid in euro's en CO2.
*   **Cloud & API Optimalisatie (Het Kostenoverzicht):** Maandelijkse review van compute (GPU/CPU) en token-kosten. Optimaliseren door model-compressie (*quantization*) of caching.
*   **Duurzaamheidsmeting (ESG):** Monitoren van energieverbruik (*inference footprint*) en rapporteren voor ESG-doelen.
*   **Resource Allocatie:** Autoscaling instellen om infrastructuur aan te passen aan de werkelijke vraag.

### Activiteit 3.4: Ethisch Toezicht & Compliance Monitoring
Blijvende wettelijke conformiteit.
*   **Post-Market Surveillance:** (EU AI Act eis) Continu scannen op onvoorziene bias, discriminatie of veiligheidsrisico's.
*   **Audit-ready Logging:** Bewaren van logs van beslissingen en menselijke interventies voor auditeurs.
*   **Transparantie Rapporten:** Periodieke rapportage aan stakeholders en CAIO over veiligheid en performance.
*   **Eerlijkheidstoets (Bias Audit):** Regelmatige steekproeven door de Ethicist op de 'toon' en kwaliteit van outputs.

## ?? 4. Team & Rollen (RACI)

| Rol | Verantwoordelijkheid in Beheer & Optimalisatie |
| :--- | :--- |
| **MLOps Engineer** | **R**esponsible: Eigenaar monitoring-pipelines, infrastructuur en stabiliteit. |
| **AI Product Manager** | **A**ccountable: Bewaakt Business KPI's, beheert backlog en user feedback. |
| **Chief AI Officer (CAIO)** | **C**onsulted: Evalueert lange termijn ROI en strategische impact. |
| **Data Scientist** | **R**esponsible: Analyseert **Prestatieverloop**, voert retraining uit en verbetert modellen. |
| **Guardian (Ethicist)** | **C**onsulted: Voert ethische reviews en post-market surveillance uit. |

---
**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Definitief

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
