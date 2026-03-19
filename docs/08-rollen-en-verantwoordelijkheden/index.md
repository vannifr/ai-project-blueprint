---
versie: '1.1'
description: 'Rollen en verantwoordelijkheden in AI-projecten: AI-projectmanager, data scientist, domeinexpert, Guardian en meer — met RACI-matrix en verantwoording per levenscyclusfase.'
type: index
layer: 1
---

# 1. Rollen & Verantwoordelijkheden

!!! abstract "Doel"
    Overzicht van alle rollen in een AI-project en hun verantwoordelijkheden per levenscyclusfase.

In AI-projecten vervagen de grenzen tussen business en IT. Daarom definiëren we rollen op basis van verantwoordelijkheid, niet op basis van functietitel.

______________________________________________________________________

## 2. Het Kernteam (The Squad)

| Rol                    | Eigenaarschap                                                           | Focus                                                                                                                 |
| :--------------------- | :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| **AI Product Manager** | [Doelkaart](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)       | "Lossen we het juiste probleem op?" — vertaalt business-wensen naar AI-instructies                                    |
| **Tech Lead**          | [Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md) | "Is het robuust en schaalbaar?" — selecteert model, bouwt pipelines, borgt stabiliteit                                |
| **Guardian** (duo)     | [Risico Pre-scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)         | "Is het veilig en eerlijk?" — vetorecht op harde grenzen. Ingevuld door Privacy & Legal Officer + AI Quality Ethicist |

Voor Hoog Risico projecten is expliciete goedkeuring van beide Guardian-leden vereist bij Gate Reviews.

______________________________________________________________________

## 3. Ondersteunende Rollen

| Rol                                                                              | Focus           | Wanneer inzetten                                                                     |
| :------------------------------------------------------------------------------- | :-------------- | :----------------------------------------------------------------------------------- |
| **Data Engineer**                                                                | Datakwaliteit   | Altijd — zorgt dat data schoon bij het model aankomt                                 |
| **AI Tester (QA)**                                                               | Betrouwbaarheid | Vanaf Fase 2 — adversarial testing en Golden Set beheer                              |
| **Adoptie Manager**                                                              | Verandering     | Vanaf Fase 4 — zorgt dat mensen de tool gebruiken (ADKAR)                            |
| **[Context Builder](../08-technische-standaarden/09-agentic-ai-engineering.md)** | Kennisbeheer    | Bij RAG-systemen of meerdere kennisbronnen — beheert wat het model ziet \[so-44\]    |
| **[AI Security Officer](../07-compliance-hub/07-red-teaming.md)**                | Beveiliging     | Bij Hoog/Beperkt Risico — OWASP LLM Top 10, red teaming, incident response \[so-45\] |

______________________________________________________________________

## 4. Strategisch Niveau

**Chief AI Officer (CAIO)** — Sponsor van het programma. Bepaalt de strategie, wijst budget toe en beslist bij de Gates of een project doorgaat of stopt.

______________________________________________________________________

## 5. Verdieping

- [RACI Matrix](02-raci-matrix.md) — wie is verantwoordelijk per activiteit per fase
- [Stakeholder Communicatie](03-stakeholder-communicatie.md) — communicatieplan per doelgroep
- [AI PM Onboarding](04-ai-pm-onboarding.md) — startgids voor nieuwe AI Project Managers
- [Besluitvormingsmatrix](besluitvormingsmatrix.md) — escalatie en vetorecht per rol
