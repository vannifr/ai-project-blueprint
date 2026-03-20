---
versie: '1.0'
type: index
layer: 2
phase: [5]
summary: Bewaak prestaties, ethische integriteit en kostenefficiëntie gedurende de operationele levensduur.
answers: [Wat bevat Fase 5 — Beheer & Optimalisatie?, Hoe monitor ik een AI-systeem na livegang?]
---

# 5. Beheer & Optimalisatie

!!! abstract "Doel"
    Bewaak prestaties, ethische integriteit en kostenefficiëntie gedurende de operationele levensduur.

## 1. Doel

Na livegang begint het echte werk: het systeem moet blijven presteren terwijl data verandert, gebruikersgedrag verschuift en kosten oplopen. Deze fase richt zich op drift-detectie, prestatiemonitoring, kostenbeheersing en periodieke herbeoordeling. Geen automatische correcties — eerst oorzaak onderzoeken, dan gericht bijsturen.

**Instapvereisten:** Systeem live, monitoring dashboards actief, operationeel team gereed, incidentplan getest.

______________________________________________________________________

## 2. Onderdelen

- [Overzicht & Doelstellingen](01-doelstellingen.md) — Wat deze fase beoogt
- [Activiteiten](02-activiteiten.md) — Continue monitoring, kostenbeheersing, feedbacklus
- [Opleveringen](03-afleveringen.md) — Monitoring dashboards, incidentlogs
- [Drift Detectie](05-drift-detectie.md) — Data drift, concept drift, prestatieverval en assumption drift

______________________________________________________________________

## 3. Veelvoorkomende valkuilen

- **Geen nulmeting vastgelegd** — zonder baseline kunt u drift niet detecteren
- **Automatisch corrigeren zonder onderzoek** — begrijp eerst waarom de prestatie daalt
- **Kosten niet monitoren** — API-kosten en compute kunnen ongemerkt exploderen
- **Feedback van gebruikers negeren** — het systeem kan technisch correct zijn maar niet nuttig

______________________________________________________________________

**Volgende stap:** Richt [Doorlopende Verbetering](../10-doorlopende-verbetering/index.md) in voor structurele feedbackloops.
→ Zie ook: [Gate 4 (Kwartaalreview)](../09-sjablonen/04-gate-reviews/checklist.md) voor periodieke herbeoordeling.
