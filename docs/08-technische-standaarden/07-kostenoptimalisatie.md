---
versie: '1.0'
type: technical
layer: 3
roles: [Tech Lead]
tags: [cost]
summary: Concrete technieken en een kostenraming-tool om AI-systeemkosten beheersbaar te houden in de Realisatie- en Beheerfase.
answers: [Wat zijn de technische standaarden voor Kostenoptimalisatie?, Wat kost dit?]
---

# Kostenoptimalisatie

!!! abstract "Doel"
    Concrete technieken en een kostenraming-tool om AI-systeemkosten beheersbaar te houden in de Realisatie- en Beheerfase.

Concrete technieken en een kostenraming-tool voor AI-systemen. Gebruik dit document in de **Realisatie**- en **Beheer & Optimalisatie**-fase om kosten beheersbaar te houden.

______________________________________________________________________

## 1. Kostenraming (Calculator)

Vul de onderstaande tabel in voor een snelle maandelijkse raming.

### LLM API-kosten

| Parameter                            | Uw waarde | Voorbeeld |
| :----------------------------------- | :-------- | :-------- |
| Verzoeken per dag                    |           | 500       |
| Gemiddelde input-tokens per verzoek  |           | 800       |
| Gemiddelde output-tokens per verzoek |           | 300       |
| Prijs per 1M input-tokens (€)        |           | €2,50     |
| Prijs per 1M output-tokens (€)       |           | €10,00    |

```
Maandelijkse input-kosten  = (verzoeken/dag × 30 × input-tokens) / 1.000.000 × prijs
Maandelijkse output-kosten = (verzoeken/dag × 30 × output-tokens) / 1.000.000 × prijs
Totaal API-kosten/maand    = input-kosten + output-kosten
```

**Voorbeeld:** 500 verzoeken/dag → 500 × 30 × 800 / 1.000.000 × €2,50 = **€30/maand** input + 500 × 30 × 300 / 1.000.000 × €10 = **€45/maand** output = **€75/maand totaal**

### Totale Maandelijkse Kostenraming

| Kostenpost                             | Maandelijks (€) |
| :------------------------------------- | :-------------- |
| LLM API (inferentie)                   |                 |
| Compute (servers/GPU)                  |                 |
| Opslag (vectorstore, logs, artefacten) |                 |
| Monitoring & observability tools       |                 |
| Development/onderhoud (intern)         |                 |
| **Totaal**                             |                 |

**Scenario's:**

| Scenario                   | Volume           | Geschatte kosten |
| :------------------------- | :--------------- | :--------------- |
| Best case (laag volume)    | 20% van verwacht |                  |
| Verwacht                   | 100%             |                  |
| Worst case (hoog volume)   | 300%             |                  |
| Schaalscenario (10× groei) | 1000%            |                  |

______________________________________________________________________

## 2. Optimalisatietechnieken

### Techniek 1 — Promptoptimalisatie

**Verwachte besparing:** 20–40% op input-tokens

Onnodige tokens in systeemprompts en gebruikersinstructies verhogen kosten zonder kwaliteitswinst.

| Actie                            | Aanpak                                                                               |
| :------------------------------- | :----------------------------------------------------------------------------------- |
| Verwijder redundante instructies | Controleer overlap tussen systeemprompt en gebruikersinstructies                     |
| Gebruik kortere voorbeelden      | Few-shot voorbeelden comprimeren zonder kwaliteitsverlies                            |
| Systeem-caching                  | Hergebruik identieke systeemprompts via provider-caching (Anthropic: prompt caching) |
| Verwijder overbodige context     | Stuur alleen relevante documentsecties, niet het volledige document                  |

______________________________________________________________________

### Techniek 2 — Response Caching

**Verwachte besparing:** 30–60% voor repetitieve queries

Identificeerbare, herhaalde vragen (FAQ, standaardrapporten) worden gecached in plaats van opnieuw naar de API gestuurd.

| Cachetype             | Geschikt voor                                        | TTL-aanbeveling |
| :-------------------- | :--------------------------------------------------- | :-------------- |
| **Exacte match**      | Identieke queries                                    | 24–72 uur       |
| **Semantische match** | Gelijksoortige vragen (cosine similarity > 0,95)     | 6–24 uur        |
| **Template-output**   | Gegenereerde documenten op basis van vaste structuur | Tot 7 dagen     |

**Meet cache-efficiëntie:** target cache-hitpercentage ≥ 40% voor systemen met repetitieve queries.

______________________________________________________________________

### Techniek 3 — Model Tiering

**Verwachte besparing:** 40–60% bij gemengde workloads

Niet elke vraag vereist het zwaarste (duurste) model. Routeer op basis van complexiteit.

| Tier          | Model (voorbeeld)         | Geschikt voor                               | Relatieve kosten |
| :------------ | :------------------------ | :------------------------------------------ | :--------------- |
| **Licht**     | Claude Haiku, GPT-4o mini | Classificatie, extractie, eenvoudige vragen | 1×               |
| **Gemiddeld** | Claude Sonnet             | Analyse, samenvatting, Q&A                  | 5–10×            |
| **Zwaar**     | Claude Opus               | Complexe redenering, juridisch, medisch     | 15–30×           |

**Routeringslogica (eenvoudig):**

```python
def kies_model(vraag: str) -> str:
    if len(vraag) < 100 and is_classificatie(vraag):
        return "claude-haiku-4-5-20251001"
    elif is_complexe_analyse(vraag):
        return "claude-opus-4-6"
    else:
        return "claude-sonnet-4-6"
```

______________________________________________________________________

### Techniek 4 — Chunking & RAG-optimalisatie

**Verwachte besparing:** 20–40% op context-lengte bij documentverwerking

Bij RAG-systemen worden vaak te grote documentfragmenten meegestuurd.

| Parameter                | Suboptimaal | Geoptimaliseerd               |
| :----------------------- | :---------- | :---------------------------- |
| Chunk-grootte            | 2000 tokens | 400–600 tokens                |
| Aantal chunks per query  | 10          | 3–5 (reranking)               |
| Drempelwaarde similarity | 0,70        | 0,82+                         |
| Compressie van chunks    | Nee         | Ja (extractieve samenvatting) |

______________________________________________________________________

### Techniek 5 — Batchverwerking

**Verwachte besparing:** 30–50% bij niet-realtime workloads

Asynchrone verwerking in bulk is goedkoper dan individuele real-time verzoeken.

- Gebruik Batch API-endpoints (Anthropic, OpenAI bieden kortingen van 50%)
- Plan zware verwerking buiten piekuren (lagere compute-kosten bij cloud)
- Combineer meerdere documenten in één API-verzoek waar mogelijk

______________________________________________________________________

## 3. Monitoring & Kostenbeheer

### KPI's voor kostenbeheer

| Metric                      | Drempel (waarschuwing) | Actie                       |
| :-------------------------- | :--------------------- | :-------------------------- |
| Kosten per succesvolle taak | > 2× baseline          | Onderzoek model-tiering     |
| Token-gebruik per verzoek   | > 130% van gemiddeld   | Promptoptimalisatie         |
| Cache-hitpercentage         | \< 20%                 | Vergroot TTL of cache-scope |
| Kosten/maand vs. budget     | > 80% van budget       | Review en bijsturen         |

### Budget-alerts instellen

Stel in uw cloud-provider of LLM-provider altijd budgetalerts in op:

- **70%** van maandbudget → waarschuwingsnotificatie
- **90%** van maandbudget → escalatie naar AI PM + CAIO
- **100%** van maandbudget → automatisch rate-limiten of stoppen

### Kostentoewijzing

Wijs kosten toe per systeem, team of use case via tags/labels in uw cloud-omgeving. Dit maakt ROI-berekening per project mogelijk (zie [Waarderealisatie](../10-doorlopende-verbetering/04-batenrealisatie.md)).

______________________________________________________________________

## 4. Kostenoptimalisatie per Fase

| Fase           | Prioriteit | Actie                                                                |
| :------------- | :--------- | :------------------------------------------------------------------- |
| **Verkenning** | Basis      | Gebruik licht model voor prototyping; stel budget-cap in             |
| **Validatie**  | Basis      | Meet kosten per test-case; bereken kosten/maand bij productie-volume |
| **Realisatie** | Hoog       | Implementeer caching en model-tiering; stel monitoring in            |
| **Levering**   | Hoog       | Valideer kosten vs. Business Case; automatiseer budget-alerts        |
| **Beheer**     | Continu    | Review maandelijks; optimaliseer bij > 10% afwijking van baseline    |

______________________________________________________________________

## Gerelateerde Modules

- [Cloud vs. On-Premise](06-cloud-vs-onpremise.md)
- [MLOps Standaarden](01-mloops-standaarden.md)
- [Waarderealisatie](../10-doorlopende-verbetering/04-batenrealisatie.md)
- [Business Case Sjabloon](../09-sjablonen/02-business-case/template.md)
- [Agentic AI Engineering — Kostenbeheersing](09-agentic-ai-engineering.md)
- [Engineering Patterns](../04-fase-ontwikkeling/06-engineering-patterns.md)
