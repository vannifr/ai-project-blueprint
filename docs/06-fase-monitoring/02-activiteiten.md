---
versie: '1.0'
---

# 1. Kernactiviteiten & Rollen (Beheer & Optimalisatie)

## 1. Kernactiviteiten

### Operationele Monitoring & MLOps

We houden de 'hartslag' van het systeem in de gaten.

- **Real-time Performance Tracking:** Dashboarding van kritieke metrics: Latency (snelheid), Foutpercentages, Uptime, Throughput.
- **Prestatieverloop Meten:** Statistisch monitoren of de invoerdata in productie afwijkt van de trainingsdata (*Data Drift*) of als de relatie tussen data en uitkomst verandert (*Concept Drift*).
- **Data Loop Integratie:** Terugkoppelen van productie-data en uitkomsten naar de ontwikkelomgeving voor analyse (Feedback Loop).
- **Geautomatiseerde Triggers:** Alerts instellen voor dalingen onder drempelwaarden (bv. accuracy \< 85%).

### Continue Verbetering & Retraining

Stilstand is achteruitgang.

- **Retraining Strategie:** Wanneer trainen we opnieuw? (Periodiek? Bij drift-alert? Bij nieuwe data?).
- **Experiment Loops:** Gebruik productie-inzichten om nieuwe hypotheses te testen in korte sprints (A/B testing, Canary releases).
- **Backlog Management:** Beheer een levende lijst van bugs, verbeterpunten en feature requests vanuit gebruikers.

### Kostenbeheersing & Energie-efficiëntie

Duurzaamheid in euro's en CO2.

- **Cloud & API Optimalisatie (Het Kostenoverzicht):** Maandelijkse review van compute (GPU/CPU) en token-kosten. Optimaliseren door model-compressie (*quantization*) of caching.
- **Duurzaamheidsmeting (ESG):** Monitoren van energieverbruik (*inference footprint*) en rapporteren voor ESG-doelen.
- **Resource Allocatie:** Autoscaling instellen om infrastructuur aan te passen aan de werkelijke vraag.

### Ethisch Toezicht & Compliance Monitoring

Blijvende wettelijke conformiteit.

- **Post-Market Surveillance:** (EU AI Act eis) Continu scannen op onvoorziene bias, discriminatie of veiligheidsrisico's.
- **Audit-ready Logging:** Bewaren van logs van beslissingen en menselijke interventies voor auditeurs.
- **Transparantie Rapporten:** Periodieke rapportage aan stakeholders en CAIO over veiligheid en performance.
- **Eerlijkheidstoets (Bias Audit):** Regelmatige steekproeven door de Ethicist op de 'toon' en kwaliteit van outputs.

## 2. Team & Rollen

| Rol                         | Verantwoordelijkheid in Beheer & Optimalisatie                                                |
| :-------------------------- | :-------------------------------------------------------------------------------------------- |
| **MLOps Engineer**          | **R**esponsible: Eigenaar monitoring-pipelines, infrastructuur en stabiliteit.                |
| **AI Product Manager**      | **A**ccountable: Bewaakt Business KPI's, beheert backlog en user feedback.                    |
| **Chief AI Officer (CAIO)** | **C**onsulted: Evalueert lange termijn ROI en strategische impact.                            |
| **Data Scientist**          | **R**esponsible: Analyseert **Prestatieverloop**, voert retraining uit en verbetert modellen. |
| **Guardian (Ethicist)**     | **C**onsulted: Voert ethische reviews en post-market surveillance uit.                        |

______________________________________________________________________

## 5. Gerelateerde Modules

**Verdieping:**

- [Drift Detectie](05-drift-detectie.md)
- [MLOps Standaarden](../08-technische-standaarden/01-mloops-standaarden.md)
- [EU AI Act compliance](../07-compliance-hub/01-eu-ai-act/index.md)

**Zie ook:** [Overzicht Fase 5](01-doelstellingen.md) · [Afleveringen](03-afleveringen.md)
