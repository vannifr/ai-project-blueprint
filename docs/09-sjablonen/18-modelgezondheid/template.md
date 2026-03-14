---
versie: '1.0'
type: template
layer: 3
phase: [5]
roles: [Data Scientist]
tags: [governance, monitoring, template]
---

# Maandelijkse Modelgezondheidsreview

Dit sjabloon biedt een gestructureerde agenda voor de maandelijkse modelgezondheidsreview met stakeholders. Het doel is om op regelmatige basis transparantie te bieden over de prestaties, risico's en het onderhoud van AI-systemen in productie.

!!! info "Deelnemers"
    Nodig minimaal de volgende rollen uit: **AI PM** (facilitator), **Tech Lead**, **Data Scientist**, **Sponsor** en **Guardian**. Overweeg de **Adoption Manager** toe te voegen wanneer gebruikersadoptie een aandachtspunt is.

______________________________________________________________________

## 1. Executive Summary (5 min)

| Veld                | Waarde                                     |
| :------------------ | :----------------------------------------- |
| **Modelversie**     | \[Bijv. v2.3.1\]                           |
| **Reviewdatum**     | \[DD-MM-JJJJ\]                             |
| **Primaire metric** | \[Bijv. F1-score: 0.91\]                   |
| **Baseline**        | \[Bijv. F1-score: 0.88 bij ingebruikname\] |
| **Trend**           | \[Stijgend / Stabiel / Dalend\]            |
| **Status**          | \[Groen / Geel / Oranje / Rood\]           |

**Statusdefinities** (afgestemd op het Drift Detection alertniveau):

- **Groen:** Alle metrics binnen drempelwaarden; geen actie vereist.
- **Geel:** Lichte afwijking gedetecteerd; verhoogde monitoring actief.
- **Oranje:** Significante prestatieverloop; hertraining wordt gepland.
- **Rood:** Rode lijnen overschreden; onmiddellijke interventie vereist.

______________________________________________________________________

## 2. Key Metrics Dashboard (10 min)

| Metric                   | Vorige maand | Huidige maand | Trend   | Drempel     |
| :----------------------- | :----------- | :------------ | :------ | :---------- |
| Nauwkeurigheid (primair) | \[Waarde\]   | \[Waarde\]    | \[+/-\] | \[Minimum\] |
| Volume (voorspellingen)  | \[Aantal\]   | \[Aantal\]    | \[+/-\] | N.v.t.      |
| Kosten per voorspelling  | \[EUR\]      | \[EUR\]       | \[+/-\] | \[Maximum\] |
| Latentie (p95)           | \[ms\]       | \[ms\]        | \[+/-\] | \[Maximum\] |
| Hallucination rate       | \[%\]        | \[%\]         | \[+/-\] | \[Maximum\] |

**Toelichting bij afwijkingen:** \[Vat hier afwijkingen samen en verwijs naar de root cause analyse indien beschikbaar.\]

______________________________________________________________________

## 3. Business Impact (5 min)

| Indicator              | Vorige maand | Huidige maand | Trend   |
| :--------------------- | :----------- | :------------ | :------ |
| Transacties verwerkt   | \[Aantal\]   | \[Aantal\]    | \[+/-\] |
| Geschatte omzetimpact  | \[EUR\]      | \[EUR\]       | \[+/-\] |
| Gebruikerstevredenheid | \[Score\]    | \[Score\]     | \[+/-\] |
| Adoptiegraad           | \[%\]        | \[%\]         | \[+/-\] |

______________________________________________________________________

## 4. Gepland Onderhoud (5 min)

| Onderhoudsactiviteit  | Geplande datum | Verantwoordelijke | Status                  |
| :-------------------- | :------------- | :---------------- | :---------------------- |
| Hertraining model     | \[Datum\]      | \[Naam\]          | \[Gepland/Bezig/Klaar\] |
| Datakwaliteitscheck   | \[Datum\]      | \[Naam\]          | \[Gepland/Bezig/Klaar\] |
| Infrastructuurupdate  | \[Datum\]      | \[Naam\]          | \[Gepland/Bezig/Klaar\] |
| Golden Set verversing | \[Datum\]      | \[Naam\]          | \[Gepland/Bezig/Klaar\] |

**Datakwaliteitstrends:** \[Beschrijf trends in data-integriteit, volumeveranderingen, nieuwe databronnen.\]

______________________________________________________________________

## 5. Vragen & Beslissingen (30 min)

Gebruik deze tijd voor open discussie met stakeholders.

**Agendapunten:**

1. \[Punt 1\]
1. \[Punt 2\]
1. \[Punt 3\]

**Genomen beslissingen:**

| Beslissing       | Eigenaar | Deadline  |
| :--------------- | :------- | :-------- |
| \[Beschrijving\] | \[Naam\] | \[Datum\] |

______________________________________________________________________

## 6. Actiepunten & Volgende Review

| Actiepunt   | Eigenaar | Deadline  | Status   |
| :---------- | :------- | :-------- | :------- |
| \[Actie 1\] | \[Naam\] | \[Datum\] | \[Open\] |
| \[Actie 2\] | \[Naam\] | \[Datum\] | \[Open\] |

- **Volgende review gepland op:** \[DD-MM-JJJJ\]
- **Facilitator volgende sessie:** \[Naam AI PM\]

______________________________________________________________________

## 7. Communicatiescripts

Gebruik de onderstaande scripts als leidraad bij het communiceren van gevoelige onderwerpen aan stakeholders. Vermijd jargon en leg de nadruk op concrete acties.

| Scenario                                               | Zeg niet                                                         | Zeg wel                                                                                                                                                                    |
| :----------------------------------------------------- | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model heeft hertraining nodig                          | "Het model is verouderd en werkt niet meer goed."                | "De prestaties vertonen een dalende trend. Wij plannen een hertraining op \[datum\] om de nauwkeurigheid te herstellen."                                                   |
| Nauwkeurigheid lager dan verwacht                      | "Het model maakt te veel fouten."                                | "De nauwkeurigheid ligt momenteel op \[X%\], onder onze drempel van \[Y%\]. Wij onderzoeken de oorzaak en presenteren een actieplan in de volgende review."                |
| Model nauwkeurig maar stakeholders vertrouwen het niet | "De cijfers bewijzen dat het goed werkt, u moet het vertrouwen." | "Wij begrijpen uw bezorgdheid. Laten wij samen een aantal randgevallen bekijken zodat u kunt zien hoe het model tot zijn beslissingen komt."                               |
| Experiment mislukt                                     | "Het experiment is gefaald."                                     | "De validatiepilot heeft aangetoond dat deze aanpak niet aan de succescriteria voldoet. Wij hebben waardevolle inzichten opgedaan die wij meenemen in het vervolgtraject." |

!!! info "Terminologie"
    Gebruik binnen de AI Project Blueprint de volgende termen: **prestatieverloop**, **validatiepilot (PoV)**, **rode lijnen**, **ingebruikname/livegang**. Zie de [Termenlijst](../../termenlijst/index.md) voor de volledige lijst.

______________________________________________________________________

**Volgende stap:** Raadpleeg de [Drift Detectie module](../../06-fase-monitoring/05-drift-detectie.md) voor gedetailleerde monitoring-richtlijnen en het [Metrics & Dashboards overzicht](../../06-fase-monitoring/03-afleveringen.md) voor KPI-configuratie.
