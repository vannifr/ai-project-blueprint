---
versie: '1.1'
description: Praktijkvoorbeelden van AI-projecten — gedocumenteerde publieke cases en conceptuele scenario's op verschillende risiconiveaus.
type: reference
layer: 3
answers: [Wat is Praktijkvoorbeelden?]
---

# Praktijkvoorbeelden

!!! warning "Disclaimer"
    Deze pagina bevat twee soorten voorbeelden: **gedocumenteerde publieke cases** (met bronvermelding) en **conceptuele scenario's** (geanonimiseerd, ter illustratie van Blueprint-toepassing). Elk voorbeeld is duidelijk gelabeld. Bronnen zijn vermeld waar beschikbaar.

______________________________________________________________________

## Deel A — Gedocumenteerde Publieke Cases

### Case 1 — Amazon Geautomatiseerd Wervingssysteem (2014–2018) { #case-amazon-hiring }

!!! example "Bias in geautomatiseerde werving — Hoog Risico"

**Context:** Amazon ontwikkelde vanaf 2014 een intern AI-systeem om cv's te screenen en kandidaten te rangschikken voor technische functies. Het model werd getraind op historische wervingsdata van de afgelopen 10 jaar.

**Wat er gebeurde:** Het systeem leerde patronen uit de historische data, waarin mannen oververtegenwoordigd waren in technische functies. Het model strafte cv's af die het woord "women's" bevatten (bijvoorbeeld "women's chess club captain") en gaf de voorkeur aan mannelijk geassocieerde taalpatronen. Amazon ontdekte het probleem intern, probeerde het model te corrigeren, maar kon niet garanderen dat het systeem geen andere vormen van discriminatie zou ontwikkelen. Het project werd in 2018 stopgezet.

**Blueprint-les:**

- **Fairness audit** (Validatiefase): systematische bias-toetsing vóór productie had het probleem eerder blootgelegd.
- **Rode Lijnen** (Harde Grenzen): proxy-discriminatie is een onacceptabel risico dat automatisch een stop-beslissing triggert.
- **Guardian Review**: classificatie als Hoog Risico (EU AI Act Bijlage III, punt 4a — werving) zou het volledige compliance-traject hebben geactiveerd.

**Bron:** Reuters, "Amazon scraps secret AI recruiting tool that showed bias against women", 10 oktober 2018.

______________________________________________________________________

### Case 2 — Microsoft Tay Chatbot (2016) { #case-microsoft-tay }

!!! example "Onbeschermde AI in publieke omgeving — Reputatierisico"

**Context:** Microsoft lanceerde in maart 2016 "Tay", een experimentele Twitter-chatbot ontworpen om te leren van interacties met gebruikers. Het doel was conversatie-AI te testen in een publieke omgeving.

**Wat er gebeurde:** Binnen 16 uur na lancering begon Tay racistische, seksistische en beledigende berichten te genereren. Gebruikers ontdekten dat ze de bot konden manipuleren door offensieve content te herhalen. Microsoft haalde Tay binnen 24 uur offline.

**Blueprint-les:**

- **Harde Grenzen** (Doelkaart): het definiëren van expliciete outputgrenzen en verboden onderwerpen had de schade beperkt.
- **Red Teaming** (Compliance Hub): adversarial testing vóór lancering had de manipuleerbaarheid blootgelegd.
- **Modus 2/3 in plaats van Modus 4**: een collaboratief model met menselijke review had onacceptabele output gefilterd.

**Bron:** Microsoft Official Blog, "Learning from Tay's introduction", 25 maart 2016.

______________________________________________________________________

### Case 3 — Air Canada Chatbot Juridische Zaak (2024) { #case-air-canada-chatbot }

!!! example "Juridische aansprakelijkheid voor AI-output — Beperkt Risico"

**Context:** Een passagier van Air Canada gebruikte de chatbot op de website om te vragen naar het rouwbeleid voor vliegtickets. De chatbot gaf onjuiste informatie: het beloofde dat de passagier retroactief een korting kon aanvragen na het boeken van een volledig tarief.

**Wat er gebeurde:** Toen de passagier de korting aanvroeg, weigerde Air Canada met het argument dat de chatbot foutieve informatie had gegeven. De passagier stapte naar het Canadian Civil Resolution Tribunal. In februari 2024 oordeelde het tribunaal dat Air Canada verantwoordelijk is voor alle informatie op haar website, inclusief output van haar chatbot. Air Canada werd veroordeeld tot het betalen van de korting plus rente.

**Blueprint-les:**

- **Validatierapport** (Validatiefase): de Golden Set had representatieve klantvragen moeten bevatten over het rouwbeleid.
- **Transparantieverplichting** (EU AI Act Art. 50): gebruikers moeten weten dat ze met een AI communiceren en de beperkingen begrijpen.
- **Incident Response** (Compliance Hub): een duidelijk escalatiepad had het probleem kunnen opvangen voordat het juridisch werd.
- **Modus 3** (Collaboratief): complexe klantvragen doorsturen naar een menselijke medewerker in plaats van autonoom beantwoorden.

**Bron:** Moffatt v Air Canada, 2024 BCCRT 149, Canadian Civil Resolution Tribunal, 14 februari 2024.

______________________________________________________________________

### Case 4 — Italiaanse Toezichthouder Blokkeert ChatGPT (2023) { #case-italy-chatgpt }

!!! example "Privacyhandhaving bij AI-systemen — Regulatoir risico"

**Context:** In maart 2023 blokkeerde de Italiaanse privacytoezichthouder (Garante per la protezione dei dati personali) tijdelijk ChatGPT in Italië wegens vermeende overtredingen van de AVG/GDPR.

**Wat er gebeurde:** De Garante identificeerde vier bezwaren: (1) geen rechtsgrondslag voor massale verwerking van persoonsgegevens voor modeltraining, (2) onnauwkeurige informatie over personen (hallucinaties), (3) geen leeftijdsverificatie voor minderjarigen, en (4) onvoldoende transparantie naar gebruikers. OpenAI voerde binnen een maand verbeteringen door — waaronder een opt-out voor training, leeftijdsverificatie en een verbeterd privacybeleid — waarna de blokkade werd opgeheven. In december 2024 legde de Garante een boete van €15 miljoen op aan OpenAI.

**Blueprint-les:**

- **Privacy-by-Design** (DPIA in Verkenningsfase): privacyrisico's moeten vanaf dag 1 worden geadresseerd.
- **Guardian Review**: classificatie en compliance-check voordat een systeem aan gebruikers wordt aangeboden.
- **Harde Grenzen**: outputfilters voor persoonsgegevens en leeftijdsbeperkingen als standaardonderdeel.

**Bron:** Garante per la protezione dei dati personali, Provvedimento del 30 marzo 2023 \[9870832\]; Garante, Provvedimento del 20 december 2024.

______________________________________________________________________

### Case 5 — DORA State of AI: Productiedrempel (2025) { #case-dora-production }

!!! example "AI-projecten halen productie niet — Strategisch risico"

**Context:** Het DORA (DevOps Research and Assessment) rapport over GenAI \[so-28\] documenteert een terugkerend patroon in de industrie: organisaties starten AI-projecten maar slagen er niet in om ze naar productie te brengen. Gartner, VentureBeat en S&P Global \[so-51\] rapporteren faal- en abandonpercentages van 30–85% voor AI-projecten.

**Wat er gebeurde:** De onderzoeken identificeren gemeenschappelijke oorzaken: ontbrekende governance, onduidelijke succescriteria, technische schuld, gebrek aan menselijk toezicht, en het ontbreken van een gestructureerd validatieproces. Projecten die wel slagen, hebben significant vaker duidelijke gates, gedefinieerde rollen en een iteratief validatieproces.

**Blueprint-les:**

- **Gate Reviews** (Governance Model): gefaseerde go/no-go beslissingen voorkomen dat projecten zonder validatie doorlopen.
- **Project Charter** (Verkenningsfase): duidelijke succescriteria en scope-afbakening vanaf het begin.
- **90-Dagen Roadmap**: gestructureerde aanpak voor organisaties die hun AI-volwassenheid willen verhogen.

**Bron:** DORA GenAI Report v2025.2 \[so-28\]; Gartner, VentureBeat, S&P Global — AI Production Surveys (2019–2024) \[so-51\].

______________________________________________________________________

## Deel B — Conceptuele Scenario's

!!! info "Over deze scenario's"
    De volgende voorbeelden zijn **conceptuele scenario's** — geanonimiseerde illustraties van hoe de Blauwdruk wordt toegepast op verschillende risiconiveaus. Ze zijn gebaseerd op veelvoorkomende patronen in de praktijk maar verwijzen niet naar specifieke organisaties.

### Scenario 1 — Minimaal Risico: Interne Kennisbot (Overheid) { #scenario-kennisbot }

!!! example "Conceptueel voorbeeld — Fast Lane toepassing"

**Sector:** Overheid — gemeentelijke dienstverlening
**Risicoklasse:** Minimaal Risico (Modus 2 — Adviserend)
**Toegepaste Blauwdruk-onderdelen:** Explorer Kit, Project Charter, Doelkaart, Validatierapport

**Situatie:** Een middelgrote gemeente wilde medewerkers helpen snel antwoorden te vinden in interne beleidsdocumenten en procesbeschrijvingen. Het callcenter had gemiddeld 40 minuten per complexe vraag nodig; veel tijd ging verloren aan het opzoeken van informatie in een verouderd intranet.

**Aanpak:** Het projectteam gebruikte de **Fast Lane** (6 weken) omdat de risicoklasse Minimaal was: geen persoonsgegevens, geen externe beslissingen, volledig intern gebruik. De Doelkaart definieerde de intentie als "medewerker vindt het juiste beleidsdocument binnen 2 minuten". Harde Grenzen beperkten het systeem tot interne documenten en verboden antwoorden op juridische of medische vragen.

De PoV duurde 2 weken en testte 50 representatieve vragen (de Golden Set). Na validatie (89% correcte verwijzingen) werd het systeem uitgerold naar 3 pilootafdelingen.

**Resultaat:** Gemiddelde zoektijd daalde van 40 naar 6 minuten. Adoptie na 8 weken: 74% van medewerkers gebruikt het systeem dagelijks. Geen incidenten gerapporteerd. Het systeem opereert in **Modus 2**: elke medewerker beoordeelt zelf het antwoord voordat hij het gebruikt.

*Conceptueel voorbeeld — namen en cijfers zijn illustratief.*

______________________________________________________________________

### Scenario 2 — Beperkt Risico: Klantenservice-automatisering (Financiële dienstverlening) { #scenario-klantenservice }

!!! example "Conceptueel voorbeeld — Volledig lifecycle met Fairness audit"

**Sector:** Financiële dienstverlening — verzekeraar
**Risicoklasse:** Beperkt Risico (Modus 3 — Collaboratief)
**Toegepaste Blauwdruk-onderdelen:** Volledig lifecycle (13 weken), Business Case, Fairness audit, Guardian Review, Validatierapport

**Situatie:** Een middelgrote verzekeraar ontving maandelijks 12.000 klantvragen via e-mail, waarvan 60% routinematig (polisstatus, betalingsbevestigingen, adreswijzigingen). Het verwerkingsteam van 8 medewerkers werkte structureel met achterstand.

**Aanpak:** De Guardian classificeerde het systeem als Beperkt Risico: klanten communiceren met een AI maar nemen zelf de actie (geen automatische beslissingen). Transparantieverplichting: klanten worden geïnformeerd dat ze met een AI-assistent communiceren.

De **Fairness audit** testte of klantvragen in eenvoudiger taalgebruik (lager taalniveau, niet-moedertaalsprekers) gelijkwaardige antwoordkwaliteit ontvingen. Een initieel probleem met formeel taalgebruik werd gecorrigeerd in de prompt-herziening van week 8.

De Business Case toonde een ROI van 340% op 18 maanden. Gate 2 (investeringsbeslissing) werd genomen op basis van het Validatierapport na de PoV: 91% correcte routering, 0 privacyincidenten.

**Resultaat:** Verwerkingstijd routinevragen daalde van 4 uur naar 12 minuten per batch. Het team van 8 werd herbestemd naar complexe klachtenbehandeling. Klanttevredenheid (NPS) steeg met 12 punten. Het systeem opereert in **Modus 3**: de AI stelt een conceptantwoord op, een medewerker keurt goed voor verzending.

*Conceptueel voorbeeld — namen en cijfers zijn illustratief.*

______________________________________________________________________

### Scenario 3 — Hoog Risico: Kredietrisicobeoordeling (Financiën) { #scenario-kredietrisico }

!!! example "Conceptueel voorbeeld — Hoog Risico compliance-traject"

**Sector:** Financiële dienstverlening — kredietverstrekker
**Risicoklasse:** Hoog Risico (EU AI Act Bijlage III — Modus 4 Gedelegeerd)
**Toegepaste Blauwdruk-onderdelen:** Volledig lifecycle (22 weken), DPIA, Fairness audit (uitgebreid), Guardian Review, Bewijsstandaarden Hoog Risico, CE-marking voorbereiding

**Situatie:** Een kredietverstrekker wilde het acceptatieproces voor kleine bedrijfsleningen (\< €50.000) deels automatiseren. Het handmatige proces duurde gemiddeld 5 werkdagen; de commerciële druk was hoog om dit terug te brengen naar 24 uur.

**Aanpak:** De Guardian classificeerde het systeem onmiddellijk als **Hoog Risico** (EU AI Act Bijlage III, punt 5b: AI-systemen voor kredietwaardigheidsbeoordelingen). Dit activeerde het volledige compliance-traject: DPIA, uitgebreide Fairness audit, menselijk toezicht bij elke beslissing, logging voor 5 jaar, en voorbereiding voor de EU AI Act conformiteitsverklaring.

De **Fairness audit** onthulde dat het initiële model aanvragen van eenmanszaken in bepaalde postcodegebieden 23% vaker afwees dan vergelijkbare aanvragen. Na analyse bleek dit een proxy voor demografische kenmerken — een onacceptabele Rode Lijn. Het model werd herzien met gecorrigeerde trainingsdata.

Gate 3 (productie-go) werd uitgesteld met 3 weken voor aanvullende validatie door een externe auditor. Het systeem werd uitgerold in **Modus 4**: AI doet een aanbeveling met confidence score; een kredietanalist neemt de finale beslissing en documenteert de motivatie.

**Resultaat:** Doorlooptijd daalde van 5 naar 1,5 werkdag. De Fairness-correctie verbeterde de representativiteit van het portfolio. Eerste externe audit na 6 maanden productie: geen overtredingen. Het incident met de proxy-variabele is gedocumenteerd als leerpunt in de Lessons Learned.

*Conceptueel voorbeeld — namen en cijfers zijn illustratief.*

______________________________________________________________________

**Gerelateerde modules:**

- [Risicoclassificatie](../01-ai-native-fundamenten/05-risicoclassificatie.md)
- [Compliance Hub](../07-compliance-hub/index.md)
- [90-Dagen Roadmap](../12-90-dagen-roadmap/index.md)
- [Red Teaming](../07-compliance-hub/07-red-teaming.md)
- [Incident Response Playbooks](../07-compliance-hub/06-incidentrespons-playbooks.md)
- [Bronnen & Inspiratie](../16-bronnen/index.md)

______________________________________________________________________

**Versie:** 1.1
**Datum:** 20 maart 2026
**Status:** Definitief
