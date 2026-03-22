---
versie: '1.0'
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [AI Product Manager]
tags: [gate-review, quick-reference]
answers: [Wat is de snelle referentie voor Cheatsheet — Gate Reviews?]
---

# Cheatsheet — Gate Reviews

**Bron:** [Gate Reviews Checklist](../04-gate-reviews/checklist.md)

______________________________________________________________________

## Overzicht 5 Gates

| Gate       | Na fase         | Kernvraag                                   | Minimale opleveringen                              |
| :--------- | :-------------- | :------------------------------------------ | :------------------------------------------------- |
| **Gate 1** | Verkenning      | Is de use case haalbaar en de kans waardig? | Project Charter, Risk Pre-Scan, Samenwerkingsmodus |
| **Gate 2** | Validatie (PoV) | Werkt het bewezen op echte data?            | Golden Set resultaten, PoV-rapport, Go/No-Go       |
| **Gate 3** | Realisatie      | Is het systeem productiewaardig?            | AI Safety Checklist, Red Teaming, Model Card       |
| **Gate 4** | Levering        | Is de overdracht volledig?                  | Overdracht checklist, SLA, monitoringplan          |
| **Gate 5** | Afsluiting      | Zijn de baten gerealiseerd?                 | Lessons Learned, batenrapport                      |

______________________________________________________________________

## Beslissingsopties

| Beslissing            | Betekenis                            | Vereiste actie                                 |
| :-------------------- | :----------------------------------- | :--------------------------------------------- |
| **Go**                | Fase geslaagd, volgende fase starten | Documenteer, start volgende sprint             |
| **Voorwaardelijk Go** | Ga verder met openstaande punten     | Lijst + eigenaar + deadline vastleggen         |
| **No-Go**             | Fase niet geslaagd                   | Root cause, herstelplan, nieuwe gate inplannen |
| **Stop**              | Project beëindigen                   | Afsluitingsrapport + lessons learned           |

______________________________________________________________________

## Vereiste Aanwezigen

| Rol           | Gate 1 | Gate 2 | Gate 3      | Gate 4 | Gate 5 |
| :------------ | :----- | :----- | :---------- | :----- | :----- |
| AI PM         | ✓      | ✓      | ✓           | ✓      | ✓      |
| Guardian      | ✓      | ✓      | ✓           | ✓      | ✓      |
| Tech Lead     | ✓      | ✓      | ✓           | ✓      | —      |
| Opdrachtgever | ✓      | —      | —           | ✓      | ✓      |
| CAIO          | —      | —      | Hoog Risico | —      | —      |

______________________________________________________________________

## Rode Vlaggen per Gate

- **Gate 1:** Geen meetbare succescriteria → No-Go
- **Gate 2:** Golden Set score onder drempel → No-Go
- **Gate 3:** Kritieke bevinding open in Red Teaming → blokkeer livegang
- **Gate 4:** Monitoringplan ontbreekt → Voorwaardelijk Go maximaal
- **Gate 5:** Baten niet gemeten → Lessons Learned verplicht

**Bron volledige aanpak:** [Gate Reviews Checklist](../04-gate-reviews/checklist.md)
