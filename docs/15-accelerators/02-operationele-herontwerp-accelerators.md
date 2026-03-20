---
versie: '1.0'
type: strategic
layer: 2
answers: [Wat houdt Operationele Herontwerp Accelerators in?]
---

# 2. Operationele Herontwerp Accelerators

## 1. Doelstelling

Deze accelerators versnellen de uitvoering van de [Operationele Herontwerp](../14-drie-tracks/02-operationele-herontwerp.md) track. Ze bieden kant-en-klare kaders voor procesanalyse, prioritering en implementatieplanning.

______________________________________________________________________

## 2. Accelerator: Processcorekaart

Gebruik dit format om processen te evalueren op AI-geschiktheid. Score elk criterium van 1 (laag) tot 3 (hoog).

| Criterium            | Score (1–3) | Toelichting                                            |
| :------------------- | :---------- | :----------------------------------------------------- |
| **Herhaalbaarheid**  |             | Hoe vaak wordt dit proces uitgevoerd?                  |
| **Datarijkheid**     |             | Is er voldoende historische data beschikbaar?          |
| **Regelgebaseerd**   |             | Zijn de beslissingen gebaseerd op duidelijke regels?   |
| **Foutgevoeligheid** |             | Hoe vaak treden fouten op in het huidige proces?       |
| **Tijdsintensiteit** |             | Hoeveel uren per week kost dit proces?                 |
| **Lage foutimpact**  |             | Zijn fouten van de AI herstelbaar zonder grote schade? |

**Totaalscore:** Som van alle scores (max. 18). Processen met score ≥ 12 zijn sterke kandidaten.

______________________________________________________________________

## 3. Accelerator: AI Process Redesign Template

Gebruik dit format voor elk geselecteerd proces vóór de implementatie:

### Huidige situatie ('As-Is')

- **Procesnaam:** \[naam\]
- **Proceseigenaar:** \[naam + rol\]
- **Frequentie:** \[dagelijks / wekelijks / per aanvraag\]
- **Stappen:** \[geef de stappen op als genummerde lijst\]
- **KPI huidige situatie:** \[bijv. 45 min/document, 8% foutpercentage\]
- **Knelpunten:** \[wat kost de meeste tijd of veroorzaakt de meeste fouten?\]

### Gewenste situatie ('To-Be')

- **Rol van AI:** \[welke stappen neemt AI over of ondersteunt AI?\]
- **Rol van mens:** \[wat doet de medewerker nog?\]
- **Samenwerkingsmodus:** \[Modus 2 / 3 / 4 — zie [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)\]
- **KPI doelwaarde:** \[bijv. 10 min/document, \<2% foutpercentage\]
- **Harde Grenzen:** \[welke beslissingen mag AI nooit zelfstandig nemen?\]

### Nulmeting

| KPI       | Huidige waarde | Doelwaarde | Meetmethode |
| :-------- | :------------- | :--------- | :---------- |
| \[KPI 1\] |                |            |             |
| \[KPI 2\] |                |            |             |

______________________________________________________________________

## 4. Accelerator: Implementatie-Sprint Plan

Verdeel de implementatie in vier sprints van twee weken:

| Sprint   | Week | Doel                           | Opleveringen                                             |
| :------- | :--- | :----------------------------- | :------------------------------------------------------- |
| Sprint 1 | 1–2  | Bouwen & intern testen         | Werkende basisversie + interne testrapportage            |
| Sprint 2 | 3–4  | Gebruikerspilot (kleine groep) | Pilotfeedback + eerste metingen                          |
| Sprint 3 | 5–6  | Bijsturen & uitbreiden         | Verbeterde versie + uitgebreidere pilotgroep             |
| Sprint 4 | 7–8  | Opschalen & borgen             | Productieversie + procesbeschrijving + monitoring actief |

**Go/No-Go na Sprint 2:** Als de pilotresultaten niet in de richting van de doelwaarden bewegen, stop dan en analyseer de oorzaak vóór Sprint 3.

______________________________________________________________________

## 5. Accelerator: Adoptieplan

Technologie alleen is niet genoeg — adoptie bepaalt het succes.

| Fase          | Activiteit                                                   | Eigenaar           |
| :------------ | :----------------------------------------------------------- | :----------------- |
| Bewustwording | Communicatie over het 'waarom' van de verandering            | AI PM + Management |
| Training      | Hands-on sessie in de nieuwe werkwijze (niet alleen de tool) | Tech Lead + HR     |
| Begeleiding   | Buddysysteem: ervaren gebruikers helpen nieuwe gebruikers    | Proceseigenaar     |
| Meting        | Wekelijkse check-in: hoe gaat het gebruik?                   | AI PM              |
| Verankering   | KPI's opnemen in reguliere performance-gesprekken            | Management         |

______________________________________________________________________

## 6. Gerelateerde Modules

- [Accelerators — Overzicht](index.md)
- [Operationele Herontwerp](../14-drie-tracks/02-operationele-herontwerp.md)
- [Snelstart: AI-Project in 90 Dagen](../12-90-dagen-roadmap/index.md)
- [Metrics & Dashboards](../10-doorlopende-verbetering/03-metrics-dashboards.md)
- [Waarderealisatie — Operationeel](../10-doorlopende-verbetering/04-batenrealisatie.md)
