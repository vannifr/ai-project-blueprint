---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 1. Blueprint & Methodologie Index

Deze pagina fungeert als de "Rosetta-steen" van de AI Project Gids. Hier vindt u de koppeling tussen de technische codes (gebruikt voor auditing en automatisering) en de inhoudelijke documenten.

## 1. De Codestructuur

| Code     | Betekenis        | Gebruik                                              |
| :------- | :--------------- | :--------------------------------------------------- |
| **MOD**  | **Module**       | Een procesfase of kennisgebied in de gids.           |
| **TMP**  | **Sjabloon**     | Een invulbaar document of sjabloon (sjabloon).       |
| **SDD**  | **Spec-Driven**  | Richtlijnen voor specificatie-gedreven ontwikkeling. |
| **GATE** | **Beslismoment** | Een formeel reviewmoment tussen fasen.               |

______________________________________________________________________

## 2. Overzicht van Modules (MOD)

De modules vormen de navigatiestructuur van de AI-levenscyclus.

| Code       | Fase / Domein                                                                    | Beschrijving                                     |
| :--------- | :------------------------------------------------------------------------------- | :----------------------------------------------- |
| **MOD-00** | [Strategisch Kader](../index.md)                                                 | Fundering, leeswijzer en samenvatting.           |
| **MOD-01** | [AI-Native Fundamenten](../01-ai-native-fundamenten/01-definitie.md)             | De 7 normatieve criteria voor AI-projecten.      |
| **MOD-02** | [Fase 1: Verkenning](../02-fase-ontdekking/01-doelstellingen.md)                 | Probleemdefinitie en data-evaluatie.             |
| **MOD-03** | [Fase 2: Validatie](../03-fase-validatie/01-doelstellingen.md)                   | Praktijkproef (PoV) en Business Case.            |
| **MOD-04** | [Fase 3: Realisatie](../04-fase-ontwikkeling/01-doelstellingen.md)               | Ontwikkeling via de SDD-methode.                 |
| **MOD-05** | [Fase 4: Levering](../05-fase-levering/01-doelstellingen.md)                     | Ingebruikname en menselijk toezicht.             |
| **MOD-06** | [Fase 5: Monitoring](../06-fase-monitoring/01-doelstellingen.md)                 | Beheer, drift-detectie en optimalisatie.         |
| **MOD-07** | [Compliance Hub](../07-compliance-hub/index.md)                                  | EU AI Act, Risicobeheer en Ethiek.               |
| **MOD-08** | [Rollen & Verantwoordelijkheden](../08-rollen-en-verantwoordelijkheden/index.md) | Wie doet wat in AI-projecten.                    |
| **MOD-09** | [Toolkit & Sjablonen](../09-sjablonen/index.md)                                  | Centrale opslag van alle herbruikbare sjablonen. |

______________________________________________________________________

## 3. Overzicht van Sjablonen (TMP)

Dit zijn de artefacten die gedurende een project worden geproduceerd. Deze vormen samen het **Wettelijk Dossier**.

| Code          | Naam Document                                                                   | Fase       | Verplicht? |
| :------------ | :------------------------------------------------------------------------------ | :--------- | :--------- |
| **TMP-09-01** | [Project Charter](../09-sjablonen/01-project-charter/template.md)               | Initiatie  | ✅         |
| **TMP-09-02** | [Business Case](../09-sjablonen/02-business-case/template.md)                   | Validatie  | ✅\*       |
| **TMP-09-03** | [Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)                 | Initiatie  | ✅         |
| **TMP-09-04** | [Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md)         | Realisatie | ✅         |
| **TMP-09-05** | [Gate Review Checklist](../09-sjablonen/04-gate-reviews/checklist.md)           | Alle       | ✅         |
| **TMP-09-06** | [Doelkaart (AI Artefact)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) | Realisatie | ✅         |
| **TMP-09-07** | [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)     | Validatie  | ✅         |
| **TMP-09-08** | [Traceerbaarheid Matrix](../09-sjablonen/08-traceerbaarheid-links/template.md)  | Levering   | ⚠️         |
| **TMP-09-09** | [Risicoanalyse (Volledig)](../09-sjablonen/03-risicoanalyse/template.md)        | Validatie  | ⚠️         |
| **TMP-09-10** | [Prompt Sjabloon](../09-sjablonen/10-prompt-engineering/template.md)            | Realisatie | 💡         |
| **TMP-09-11** | [Privacy & Data Blad](../09-sjablonen/11-privacy-data/privacyblad.md)           | Verkenning | ✅         |

*\*Optioneel bij Fast Lane projecten.*

______________________________________________________________________

## 4. Beslismomenten (GATES)

| Gate       | Naam                | Voorwaarde voor doorgang                          |
| :--------- | :------------------ | :------------------------------------------------ |
| **GATE 1** | Go/No-Go Ontdekking | Risico Pre-Scan (TMP-03) voltooid.                |
| **GATE 2** | Investering PoV     | Business Case (TMP-02) goedgekeurd.               |
| **GATE 3** | Productie-klaar     | Validatierapport (TMP-07) getekend door Guardian. |
| **GATE 4** | Livegang            | Ingebruikname-audit voltooid.                     |
