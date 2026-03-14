---
versie: '1.0'
description: 'Snelle referentiekaart van de 5-fasen AI-levenscyclus: doel per fase, gate-criteria, kernactiviteit en primair sjabloon — alles op één pagina.'
type: strategic
layer: 1
---

# AI-Levenscyclus — Snelle Referentie

> Dit is een navigatiekaart, geen uitleg. Voor de volledige methodologie: zie [AI-Levenscyclus](01-ai-levenscyclus.md).

______________________________________________________________________

| Fase                           | Doel                                                  | Gate                           | Kernactiviteit                                    | Primair Sjabloon                                                            |
| :----------------------------- | :---------------------------------------------------- | :----------------------------- | :------------------------------------------------ | :-------------------------------------------------------------------------- |
| **1 — Verkenning & Strategie** | Probleem valideren, data evalueren, risico inschatten | Gate 1: Go/No-Go probleemdef.  | Doelkaart invullen + Moduskeuze Beoordeling       | [Project Charter](../09-sjablonen/01-project-charter/template.md)           |
| **2 — Validatie (PoV)**        | Hypothese testen op kleine schaal, ROI onderbouwen    | Gate 2: Investeringsbeslissing | Validatiepilot uitvoeren + Business Case          | [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) |
| **3 — Realisatie**             | Systeem bouwen conform spec, Golden Set valideren     | Gate 3: Productie-readiness    | SDD-patroon: spec → golden set → build → validate | [Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md)     |
| **4 — Levering**               | Uitrollen naar productie, overdracht aan beheer       | Gate 3 (vervolg): Livegang     | Overdrachtschecklist + gebruikerstraining         | [Overdracht Checklist](../09-sjablonen/index.md)                            |
| **5 — Beheer & Optimalisatie** | Drift bewaken, kosten beheersen, feedback verwerken   | Gate 4: Kwartaalreview         | Driftmeting + kostenefficiëntie review            | [Beheerplan](../09-sjablonen/index.md)                                      |

______________________________________________________________________

## Tijdlijn per risicoklasse

| Risicoklasse    | Typische doorlooptijd | Fast Lane? |
| :-------------- | :-------------------- | :--------- |
| Minimaal Risico | 6–8 weken             | ✅ Ja      |
| Beperkt Risico  | 13 weken              | Optioneel  |
| Hoog Risico     | 18–24 weken           | ❌ Nee     |

______________________________________________________________________

## Vier Kernartefacten (altijd verplicht)

| Artefact             | Wat het vastlegt                               | Aangemaakt in |
| :------------------- | :--------------------------------------------- | :------------ |
| **Doeldefinitie**    | De menselijke intentie achter het systeem      | Fase 1        |
| **Rode Lijnen**      | Wat het systeem nooit mag doen                 | Fase 1        |
| **Prompts**          | De stuurinstructies voor het AI-systeem        | Fase 1–3      |
| **Validatierapport** | Het bewijs dat het systeem werkt zoals bedoeld | Fase 2–3      |

> Voor de volledige uitleg van deze artefacten: zie [AI-Native Fundamenten](../01-ai-native-fundamenten/01-definitie.md).

______________________________________________________________________

**Gerelateerde modules:**

- [Volledige AI-Levenscyclus](01-ai-levenscyclus.md)
- [Samenwerkingsmodi](06-has-h-niveaus.md)
- [90-Dagen Roadmap](../12-90-dagen-roadmap/index.md)
- [Alle Sjablonen](../09-sjablonen/index.md)

______________________________________________________________________

**Versie:** 1.0
**Datum:** 13 maart 2026
**Status:** Definitief
