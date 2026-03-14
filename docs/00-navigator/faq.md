---
versie: '1.0'
description: Veelgestelde vragen over AI-projectmanagement met de Blueprint.
---

# Veelgestelde Vragen (FAQ)

## 1. Welke metrics moet ik bijhouden om succes te meten?

De Blueprint werkt met fase-specifieke metrics. Gebruik onderstaande tabel als startpunt en pas aan op basis van uw projectcontext.

| Fase                    | Kernmetrics                                                               | Bron                                                                                                                                   |
| :---------------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
| Verkenning & Strategie  | Datakwaliteitsscore, haalbaarheidsuitkomst                                | [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)                                                               |
| Validatie (PoV)         | Nauwkeurigheid vs. baseline, latentie (p95), kosten per voorspelling      | [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md), [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)    |
| Realisatie              | Testdekking, integratiescore, naleving Rode Lijnen                        | [SDD Patroon](../04-fase-ontwikkeling/05-sdd-patroon.md)                                                                               |
| Levering                | Adoptiegraad, gebruikerstevredenheid (CSAT/NPS), ingebruikname-gereedheid | [Overdracht Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)                                                       |
| Beheer & Optimalisatie  | Prestatieverloop-indicatoren, business impact, hallucinatiepercentage     | [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md), [Modelgezondheid Review](../09-sjablonen/18-modelgezondheid/template.md) |
| Doorlopende Verbetering | Kaizen-snelheid, batenrealisatie vs. business case                        | [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)                                                           |

!!! tip "Begin met drie"
    Kies maximaal drie kernmetrics per fase. Te veel metrics leiden tot rapportagelast zonder inzicht. Voeg metrics pas toe wanneer bestaande vragen niet beantwoord worden.

______________________________________________________________________

## 2. Hebben we nog story points nodig bij AI-projecten?

**Kort antwoord:** Story points blijven bruikbaar voor coördinatie, maar verliezen hun voorspellende waarde voor AI-specifiek experimenteerwerk.

**Waarom?** AI-experimenten hebben een niet-deterministisch karakter: de uitkomst hangt af van datakwaliteit, modelgedrag en onverwachte edge cases. Traditionele schatting gaat uit van bekende complexiteit — bij AI is de complexiteit vaak pas achteraf duidelijk.

**Aanbeveling:**

- **Time-boxing in plaats van schatting** voor AI-experimentwerk. Gebruik het [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md) om spikes af te bakenen met een vaste einddatum en beslispunt (Doorgaan / Pivoteren / Stoppen).
- **Story points behouden** voor infrastructuur-, integratie- en UI-werk binnen dezelfde sprint — daar blijft relatieve schatting zinvol.
- **Vermijd de valkuil** van het achteraf toekennen van hogere punten aan mislukte experimenten. Een mislukt experiment met waardevolle inzichten is geen "groter ticket" — het is een geleerd resultaat.

Zie ook: [Agile Antipatronen](../00-strategisch-kader/04-agile-antipatronen-niet-toegestaan.md) voor veelvoorkomende valkuilen bij AI-projecten.

______________________________________________________________________

**Volgende stap:** Bepaal uw fase-specifieke metrics en leg deze vast in het [Project Charter](../09-sjablonen/01-project-charter/template.md).
→ Zie ook: [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md) | [Metrics Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
