---
versie: '1.0'
type: template
layer: 3
phase: [1, 2]
tags: [template]
---

# Experiment Ticket

Dit sjabloon begeleidt uw team bij het opzetten, uitvoeren en evalueren van een time-boxed AI-experimentsprint. Elk experiment volgt een gestructureerd pad van hypothese naar beslissing, afgestemd op de Gate-structuur van de AI Project Blueprint.

!!! info "Wanneer dit sjabloon gebruiken"
    Gebruik dit sjabloon wanneer u een nieuwe AI-hypothese wilt valideren binnen een afgebakende tijdsperiode. Het experiment levert objectief bewijs op voor de Gate Review-beslissing: **Doorgaan**, **Pivoteren** of **Stoppen**.

______________________________________________________________________

## 1. Hypothese & Aannames

- **Hypothesenaam:** \[Korte, herkenbare naam\]
- **Beschrijving:** \[Wat verwacht u dat het model/systeem zal bereiken? Formuleer als: "Wij verwachten dat \[interventie\] leidt tot \[meetbaar resultaat\] voor \[doelgroep\]."\]
- **Rationale:** \[Waarom verwacht u dit resultaat? Verwijs naar eerdere data, literatuur of stakeholder-inzichten.\]

### Riskantste Aanname Test (RAT)

*Welke aanname onder deze hypothese is het riskantst? Test deze eerst — niet de makkelijkste, maar de aanname die het experiment zinloos maakt als ze niet klopt.*

- **Riskantste aanname:** \[Beschrijf de aanname die het meeste risico draagt\]
- **Validatiemethode:** \[Hoe testen we deze aanname zo goedkoop en snel mogelijk? Bijv. data-analyse, interviews, concierge-test, technische spike\]
- **Slaag/faalcriterium:** \[Wanneer is de aanname gevalideerd? Wanneer ontkracht?\]
- **Eigenaar:** \[Wie voert de test uit?\]

______________________________________________________________________

## 2. Time-box

- **Startdatum:** \[DD-MM-JJJJ\]
- **Einddatum:** \[DD-MM-JJJJ\]
- **Duur:** \[Aanbevolen: 1-2 sprints (2-4 weken)\]
- **Tussentijds checkpoint:** \[Datum halverwege voor go/no-go beoordeling\]

!!! warning "Overschrijd de time-box niet"
    Indien het experiment na de afgesproken einddatum geen eenduidige resultaten oplevert, activeer dan het beslispunt (sectie 6). Uitstel zonder formele beslissing is niet toegestaan.

______________________________________________________________________

## 3. Teamallocatie

| Rol            | Naam              | Beschikbaarheid (%) | Verantwoordelijkheid                              |
| :------------- | :---------------- | :-----------------: | :------------------------------------------------ |
| AI PM          | \[Naam invullen\] |    \[Bijv. 30%\]    | Scope bewaken, stakeholders informeren, besluit   |
| Data Scientist | \[Naam invullen\] |    \[Bijv. 60%\]    | Modelontwikkeling, metingen, analyse              |
| Tech Lead      | \[Naam invullen\] |    \[Bijv. 40%\]    | Architectuur, integratie, technische haalbaarheid |

______________________________________________________________________

## 4. Succescriteria

Definieer meetbare criteria die aansluiten bij de Evidence Standards van de AI Project Blueprint \[so-1\].

| Criterium               | Metric                    | Minimumdrempel     | Streefwaarde       |
| :---------------------- | :------------------------ | :----------------- | :----------------- |
| Nauwkeurigheid          | \[Bijv. F1-score\]        | \[Bijv. >= 0.80\]  | \[Bijv. >= 0.90\]  |
| Latentie                | \[Bijv. p95 responstijd\] | \[Bijv. \< 2s\]    | \[Bijv. \< 500ms\] |
| Kosten per voorspelling | \[Bijv. EUR/1000 calls\]  | \[Bijv. \< EUR 5\] | \[Bijv. \< EUR 2\] |
| Gebruikersacceptatie    | \[Bijv. NPS of CSAT\]     | \[Bijv. >= 7/10\]  | \[Bijv. >= 8/10\]  |

- **Bewijsniveau:** \[Verwijzing naar het vereiste Evidence Level voor deze Gate\]
- **Golden Set beschikbaar:** \[Ja/Nee — indien Nee, opnemen als deliverable in sprint 1\]

______________________________________________________________________

## 5. Faalcriteria

Definieer de grenzen waarbij het experiment als mislukt wordt beschouwd en de pivot/stop-trigger wordt geactiveerd.

| Faalcriterium                             | Drempel                        | Gevolg            |
| :---------------------------------------- | :----------------------------- | :---------------- |
| Nauwkeurigheid onder minimumgrens         | \[Bijv. F1 \< 0.70\]           | Stop of Pivot     |
| Rode Lijnen geschonden                    | Elke schending                 | Onmiddellijk Stop |
| Kosten overschrijden budget               | \[Bijv. > 150% van schatting\] | Pivot of Stop     |
| Geen meetbare verbetering t.o.v. baseline | Na sprint 1                    | Pivot             |

______________________________________________________________________

## 6. Beslispunt

Na afloop van de time-box neemt het team een formele beslissing op basis van de verzamelde data. Dit beslispunt is gekoppeld aan de Gate-structuur.

| Beslissing    | Voorwaarden                                                | Vervolgactie                                         |
| :------------ | :--------------------------------------------------------- | :--------------------------------------------------- |
| **Doorgaan**  | Alle succescriteria behaald; geen faalcriteria geactiveerd | Voort naar volgende Gate; plan realisatiesprint      |
| **Pivoteren** | Deels succesvol; hypothese aanpassen levert betere kans op | Nieuw Experiment Ticket met aangepaste hypothese     |
| **Stoppen**   | Faalcriteria geactiveerd; geen realistisch pad naar succes | Documenteer in Validatierapport; archiveer learnings |

- **Besluit:** \[Doorgaan / Pivoteren / Stoppen\]
- **Onderbouwing:** \[Korte samenvatting van de data die het besluit ondersteunt\]
- **Beslisser:** \[Naam AI PM\]
- **Datum:** \[DD-MM-JJJJ\]

______________________________________________________________________

## 7. Budget

| Kostenpost           | Doorgaan     | Pivoteren    | Stoppen             |
| :------------------- | :----------- | :----------- | :------------------ |
| Compute & API-kosten | \[EUR\]      | \[EUR\]      | \[EUR afbouw\]      |
| Teamuren (intern)    | \[FTE-uren\] | \[FTE-uren\] | \[FTE-uren afbouw\] |
| Data-acquisitie      | \[EUR\]      | \[EUR\]      | N.v.t.              |
| Tooling & licenties  | \[EUR\]      | \[EUR\]      | \[EUR afbouw\]      |
| **Totaal geschat**   | \[EUR\]      | \[EUR\]      | \[EUR\]             |

______________________________________________________________________

## 8. Sprint Capaciteitsrichtlijn

De onderstaande verdeling biedt een richtlijn voor de capaciteitsplanning tijdens experimentssprints.

| Categorie             | Aandeel |
| :-------------------- | :------ |
| Feature-ontwikkeling  | 30%     |
| Experimentatie        | 40%     |
| Onderhoud / tech debt | 15%     |
| Buffer                | 15%     |

*Deze verdeling is indicatief. Pas aan op basis van de projectfase en teamgrootte.*

______________________________________________________________________

## 9. Resultaatdocumentatie

- **Validatierapport:** \[Link naar ingevuld Validatierapport\]
- **Meetresultaten:** \[Link naar dashboard of dataexport\]
- **Lessons learned:** \[Korte opsomming van de belangrijkste inzichten\]

______________________________________________________________________

**Volgende stap:** Documenteer de experimentresultaten in het [Validatierapport](../07-validatie-bewijs/validatierapport.md) en doorloop de [Gate Review Checklist](../15-guardian-review/template.md) voor het formele beslismoment.
