---
versie: '1.1'
type: playbook
layer: 1
tags: [playbook, stakeholder]
summary: Praktische handleiding voor het communiceren met stakeholders over de unieke uitdagingen van AI-projecten, zoals probabilistische uitkomsten en iteratieve validatie.
answers: [Hoe voer ik Stakeholder Communicatie Playbook uit?, Hoeveel validatie is voldoende?]
---

# Stakeholder Communicatie Playbook

!!! abstract "Doel"
    Praktische handleiding voor het communiceren met stakeholders over de unieke uitdagingen van AI-projecten, zoals probabilistische uitkomsten en iteratieve validatie.

Praktische handleiding voor AI Project Managers over het communiceren met stakeholders in AI-projecten. AI-projecten kennen unieke communicatie-uitdagingen: probabilistische uitkomsten, iteratieve validatie en technische complexiteit die vertaald moet worden naar zakelijke impact.

!!! info "Voor wie"
    Dit playbook is primair bedoeld voor de **AI PM**. De communicatietechnieken zijn echter ook waardevol voor **Tech Leads** en **Data Scientists** die regelmatig met niet-technische stakeholders communiceren.

______________________________________________________________________

## 1. Communicatiecadans

Structureer uw communicatie rond vaste momenten. Elke stakeholdergroep ontvangt informatie op het juiste niveau en met de juiste frequentie.

| Stakeholdergroep | Wat                                              | Frequentie    | Formaat                     | Verantwoordelijke |
| :--------------- | :----------------------------------------------- | :------------ | :-------------------------- | :---------------- |
| Sponsor          | Strategische voortgang, budget, Gate-besluiten   | Tweewekelijks | 1-op-1 briefing (30 min)    | AI PM             |
| Guardian         | Compliance-status, harde grenzen, risico-updates | Maandelijks   | Schriftelijk rapport        | AI PM + Tech Lead |
| Tech Lead        | Technische voortgang, blokkades, architectuur    | Wekelijks     | Standup of Slack-update     | AI PM             |
| Stakeholders     | Business impact, adoptie, modelgezondheid        | Maandelijks   | Model Health Review meeting | AI PM             |
| CAIO             | Portfolio-overzicht, escalaties                  | Kwartaal      | Dashboard + toelichting     | AI PM             |

______________________________________________________________________

## 2. Het Misschien-probleem

AI-systemen leveren probabilistische uitkomsten. Waar traditionele software deterministisch is ("het werkt of het werkt niet"), geeft een AI-systeem antwoorden met een bepaalde mate van zekerheid. Dit is fundamenteel anders en vereist een andere manier van communiceren.

### Waarom dit lastig is

- Stakeholders verwachten ja/nee-antwoorden; AI levert waarschijnlijkheden.
- Een nauwkeurigheid van 95% klinkt hoog, maar betekent dat 1 op 20 voorspellingen fout is.
- "Het model weet het niet" is een valide en waardevolle uitkomst, maar wordt vaak als falen ervaren.

### Hoe u dit framet

1. **Begin met de baseline.** Vergelijk altijd met de huidige situatie: "Handmatige beoordeling heeft een foutmarge van 12%; het model brengt dit terug naar 5%."
1. **Maak fouten concreet.** Vertaal percentages naar aantallen: "Bij 10.000 transacties per maand betekent 95% nauwkeurigheid dat 500 gevallen handmatige controle vereisen."
1. **Toon betrouwbaarheidsintervallen.** Presenteer niet alleen het gemiddelde, maar ook de range: "Het model voorspelt met 87-93% zekerheid, afhankelijk van de datakwaliteit."
1. **Normaliseer onzekerheid.** Leg uit dat onzekerheid een feature is, geen bug: "Het model geeft aan wanneer het onzeker is, zodat een menselijke expert kan bijspringen."

______________________________________________________________________

## 3. Vertrouwen Opbouwen

Vertrouwen in AI-systemen wordt niet gewonnen met cijfers alleen. Het vereist actieve betrokkenheid van stakeholders bij het validatieproces.

### Praktische technieken

- **Betrek stakeholders bij edge case review.** Nodig stakeholders uit om grensgevallen te bekijken en het model te beoordelen op cases die zij uit de praktijk kennen. Dit geeft hen eigenaarschap over de kwaliteit.
- **Toon betrouwbaarheidsintervallen.** Maak inzichtelijk wanneer het model zeker is en wanneer niet. Stakeholders vertrouwen een systeem meer dat eerlijk is over zijn beperkingen.
- **Organiseer regelmatige health reviews.** Gebruik het [Maandelijkse Model Healthsreview](../09-sjablonen/18-modelgezondheid/template.md) sjabloon om structureel transparantie te bieden.
- **Laat stakeholders het model "breken".** Organiseer informele sessies waar stakeholders moeilijke cases mogen invoeren. Dit verlaagt de drempel en vergroot het begrip.
- **Deel "near misses" proactief.** Wacht niet tot een stakeholder een fout ontdekt. Rapporteer proactief over gevallen waar het systeem bijna faalde en wat u eraan heeft gedaan.

!!! warning "Vermijd het cijfer-als-bewijs-argument"
    Zeg nooit: "De cijfers bewijzen dat het werkt." Dit ondermijnt het vertrouwen. Zeg in plaats daarvan: "Laten wij samen naar een aantal specifieke gevallen kijken zodat u zelf kunt beoordelen."

______________________________________________________________________

## 4. Escalatieprocedure

De escalatieprocedure is afgestemd op het bestaande governance-model, inclusief de 48-uur cooling-off periode bij meningsverschillen.

### Escalatieniveaus

| Niveau | Trigger                               | Actie                                      | Communicatie naar             |
| :----- | :------------------------------------ | :----------------------------------------- | :---------------------------- |
| 1      | Metric onder drempel (geel)           | Verhoogde monitoring; AI PM informeert     | Tech Lead, Data Scientist     |
| 2      | Structureel prestatieverloop (oranje) | Hertraining plannen; Sponsor informeren    | Sponsor, Guardian, Tech Lead  |
| 3      | Rode lijnen overschreden (rood)       | Systeem pauzeren; incidentproces activeren | CAIO, Sponsor, Guardian, alle |
| 4      | Meningsverschil over besluit          | 48-uur cooling-off; daarna CAIO-escalatie  | Alle betrokken partijen       |

### Communicatiesjablonen bij escalatie

**Niveau 2 — Bericht aan Sponsor:**

> "Geachte \[Naam\], de prestaties van \[systeem\] vertonen een dalende trend over de afgelopen \[periode\]. De huidige \[metric\] staat op \[waarde\], onder onze drempel van \[drempel\]. Het team plant een hertraining op \[datum\]. Wij houden u op de hoogte van de voortgang in de volgende briefing op \[datum\]."

**Niveau 3 — Bericht aan alle stakeholders:**

> "Het AI-systeem \[naam\] is tijdelijk gepauzeerd vanwege een overschrijding van de harde grenzen op \[datum\]. Het incidentresponsteam onderzoekt de oorzaak. Verwachte doorlooptijd: \[schatting\]. Wij communiceren updates elke \[frequentie\] via \[kanaal\]."

______________________________________________________________________

## 5. Trade-off Communicatie

AI-projecten vereisen voortdurend afwegingen tussen nauwkeurigheid, snelheid en kosten. Help stakeholders deze afwegingen te begrijpen.

### De 95% naar 99% kostencurve

De verbetering van 90% naar 95% nauwkeurigheid kost doorgaans X. De verbetering van 95% naar 99% kost vaak 5-10x zoveel. Maak dit expliciet:

| Nauwkeurigheid | Relatieve kosten | Fouten per 10.000 | Overwegingen                             |
| :------------- | :--------------- | :---------------- | :--------------------------------------- |
| 90%            | 1x               | 1.000             | Geschikt voor laag-risico toepassingen   |
| 95%            | 2-3x             | 500               | Standaard voor de meeste toepassingen    |
| 99%            | 10-20x           | 100               | Alleen bij hoog-risico / kritieke flows  |
| 99.9%          | 50-100x          | 10                | Zelden haalbaar; overweeg hybride aanpak |

### Het driehoeksmodel

Presenteer trade-offs als een driehoek met drie assen:

- **Nauwkeurigheid:** Hoe correct zijn de voorspellingen?
- **Latentie:** Hoe snel komt het antwoord?
- **Kosten:** Wat kost elke voorspelling?

Verbeter u de ene as, dan verslechtert minstens een van de andere. Help stakeholders te bepalen welke as prioriteit heeft voor hun use case.

______________________________________________________________________

**Volgende stap:** Gebruik het [Maandelijkse Model Healthsreview](../09-sjablonen/18-modelgezondheid/template.md) sjabloon voor gestructureerde stakeholdercommunicatie en raadpleeg de [Besluitvormingsmatrix](besluitvormingsmatrix.md) voor beslissingsbevoegdheden per rol.
