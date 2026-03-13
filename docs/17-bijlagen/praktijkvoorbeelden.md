---
versie: '1.0'
description: Drie geanonimiseerde praktijkvoorbeelden van AI-projecten op verschillende risiconiveaus — van interne kennisbot tot hoog-risico kredietbeoordeling.
---

# Praktijkvoorbeelden

Onderstaande voorbeelden illustreren hoe de Blauwdruk in de praktijk wordt toegepast. Alle organisatienamen en personen zijn geanonimiseerd.

______________________________________________________________________

## Voorbeeld 1 — Minimaal Risico: Interne Kennisbot (Overheid)

**Sector:** Overheid — gemeentelijke dienstverlening
**Risicoklasse:** Minimaal Risico (Modus 2 — Adviserend)
**Toegepaste Blauwdruk-onderdelen:** Explorer Kit, Project Charter, Doelkaart, Validatierapport

### Situatie

Een middelgrote gemeente wilde medewerkers helpen snel antwoorden te vinden in interne beleidsdocumenten en procesbeschrijvingen. Het callcenter had gemiddeld 40 minuten per complexe vraag nodig; veel tijd ging verloren aan het opzoeken van informatie in een verouderd intranet.

### Aanpak

Het projectteam gebruikte de **Fast Lane** (6 weken) omdat de risicoklasse Minimaal was: geen persoonsgegevens, geen externe beslissingen, volledig intern gebruik. De Doelkaart definieerde de intentie als "medewerker vindt het juiste beleidsdocument binnen 2 minuten". Rode Lijnen beperkten het systeem tot interne documenten en verboden antwoorden op juridische of medische vragen.

De PoV duurde 2 weken en testte 50 representatieve vragen (de Golden Set). Na validatie (89% correcte verwijzingen) werd het systeem uitgerold naar 3 pilootafdelingen.

### Resultaat

Gemiddelde zoektijd daalde van 40 naar 6 minuten. Adoptie na 8 weken: 74% van medewerkers gebruikt het systeem dagelijks. Geen incidenten gerapporteerd. Het systeem opereert in **Modus 2**: elke medewerker beoordeelt zelf het antwoord voordat hij het gebruikt.

*Sector: Overheid — Namen geanonimiseerd.*

______________________________________________________________________

## Voorbeeld 2 — Beperkt Risico: Klantenservice-automatisering (Financiële dienstverlening)

**Sector:** Financiële dienstverlening — verzekeraar
**Risicoklasse:** Beperkt Risico (Modus 3 — Collaboratief)
**Toegepaste Blauwdruk-onderdelen:** Volledig lifecycle (13 weken), Business Case, Fairness audit, Guardian Review, Validatierapport

### Situatie

Een middelgrote verzekeraar ontving maandelijks 12.000 klantvragen via e-mail, waarvan 60% routinematig (polisstatus, betalingsbevestigingen, adreswijzigingen). Het verwerkingsteam van 8 medewerkers werkte structureel met achterstand.

### Aanpak

De Guardian classificeerde het systeem als Beperkt Risico: klanten communiceren met een AI maar nemen zelf de actie (geen automatische beslissingen). Transparantieverplichting: klanten worden geïnformeerd dat ze met een AI-assistent communiceren.

De **Fairness audit** testte of klantvragen in eenvoudiger taalgebruik (lager taalniveau, niet-moedertaalsprekers) gelijkwaardige antwoordkwaliteit ontvingen. Een initieel probleem met formeel taalgebruik werd gecorrigeerd in de prompt-herziening van week 8.

De Business Case toonde een ROI van 340% op 18 maanden. Gate 2 (investeringsbeslissing) werd genomen op basis van het Validatierapport na de PoV: 91% correcte routering, 0 privacyincidenten.

### Resultaat

Verwerkingstijd routinevragen daalde van 4 uur naar 12 minuten per batch. Het team van 8 werd herbestemd naar complexe klachtenbehandeling. Klanttevredenheid (NPS) steeg met 12 punten. Het systeem opereert in **Modus 3**: de AI stelt een conceptantwoord op, een medewerker keurt goed voor verzending.

*Sector: Financiële dienstverlening — Namen geanonimiseerd.*

______________________________________________________________________

## Voorbeeld 3 — Hoog Risico: Kredietrisicobeoordeling (Financiën)

**Sector:** Financiële dienstverlening — kredietverstrekker
**Risicoklasse:** Hoog Risico (EU AI Act Bijlage III — Modus 4 Gedelegeerd)
**Toegepaste Blauwdruk-onderdelen:** Volledig lifecycle (22 weken), DPIA, Fairness audit (uitgebreid), Guardian Review, Bewijsstandaarden Hoog Risico, CE-marking voorbereiding

### Situatie

Een kredietverstrekker wilde het acceptatieproces voor kleine bedrijfsleningen (\< €50.000) deels automatiseren. Het handmatige proces duurde gemiddeld 5 werkdagen; de commerciële druk was hoog om dit terug te brengen naar 24 uur.

### Aanpak

De Guardian classificeerde het systeem onmiddellijk als **Hoog Risico** (EU AI Act Bijlage III, punt 5b: AI-systemen voor kredietwaardigheidsbeoordelingen). Dit activeerde het volledige compliance-traject: DPIA, uitgebreide Fairness audit, menselijk toezicht bij elke beslissing, logging voor 5 jaar, en voorbereiding voor de EU AI Act conformiteitsverklaring.

De **Fairness audit** onthulde dat het initiële model aanvragen van eenmanszaken in bepaalde postcodegebieden 23% vaker afwees dan vergelijkbare aanvragen. Na analyse bleek dit een proxy voor demografische kenmerken — een onacceptabele Rode Lijn. Het model werd herzien met gecorrigeerde trainingsdata.

Gate 3 (productie-go) werd uitgesteld met 3 weken voor aanvullende validatie door een externe auditor. Het systeem werd uitgerold in **Modus 4**: AI doet een aanbeveling met confidence score; een kredietanalist neemt de finale beslissing en documenteert de motivatie.

### Resultaat

Doorlooptijd daalde van 5 naar 1,5 werkdag. De Fairness-correctie verbeterde de representativiteit van het portfolio. Eerste externe audit na 6 maanden productie: geen overtredingen. Het incident met de proxy-variabele is gedocumenteerd als leerpunt in de Lessons Learned en heeft geleid tot een aanscherping van de Fairness audit-procedure in de Blauwdruk.

*Sector: Financiële dienstverlening — Namen geanonimiseerd.*

______________________________________________________________________

**Gerelateerde modules:**

- [Risicoclassificatie](../01-ai-native-fundamenten/05-risicoclassificatie.md)
- [Compliance Hub](../07-compliance-hub/index.md)
- [90-Dagen Roadmap](../12-90-dagen-roadmap/index.md)

______________________________________________________________________

**Versie:** 1.0
**Datum:** 13 maart 2026
**Status:** Definitief
