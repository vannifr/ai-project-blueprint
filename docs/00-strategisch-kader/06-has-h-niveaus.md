---
versie: '1.1'
description: 'AI-Samenwerkingsmodi: vijf niveaus van mens-AI autonomie — van Instrumenteel tot Autonoom — met besliscriteria voor de juiste modus per taak en risicoprofiel.'
type: strategic
layer: 1
summary: Classificatie van vijf mens-AI samenwerkingsmodi (Instrumenteel tot Autonoom) om de juiste governance en risicobeheersing per toepassing te bepalen.
answers: [Wat houdt AI-Samenwerkingsmodi in?, Hoe classificeer ik het risico van mijn AI-project?]
---

# 1. AI-Samenwerkingsmodi

!!! abstract "Doel"
    Classificatie van vijf mens-AI samenwerkingsmodi (Instrumenteel tot Autonoom) om de juiste governance en risicobeheersing per toepassing te bepalen.

!!! tip "Wanneer gebruik je dit?"
    Je ontwerpt een AI-toepassing en moet bepalen hoeveel autonomie de AI krijgt en welke governance daarbij hoort.

## 1. Doel van de Modi

Om te bepalen welke processen, governance en risicobeheersing nodig zijn, classificeren we de relatie tussen mens en machine in vijf **Samenwerkingsmodi**.

Dit model beschrijft de verschuiving van AI als gereedschap naar AI als zelfstandige actor. Het is cruciaal om vooraf te definiëren in welke modus een systeem opereert, omdat een 'Modus 4'-systeem (Gedelegeerd) veel strengere veiligheidsregels vereist dan een 'Modus 2'-systeem (Adviserend).

______________________________________________________________________

## 2. De Vijf Modi

### Modus 1: Instrumenteel (The Tool)

**De mens werkt, AI wacht.**

Dit is de klassieke situatie. De AI is passief en doet niets tenzij de mens op een knop drukt. De mens is volledig verantwoordelijk voor de start, de uitvoering en het resultaat.

- **Dynamiek:** Mens Actie AI Resultaat.
- **Voorbeeld:** Een tekst vertalen met Google Translate of een formule genereren in Excel.
- **Risico:** Laag (fouten worden direct door de gebruiker gezien).
- **Governance:** Standaard IT-beheer.

### Modus 2: Adviserend (The Advisor)

**De AI stelt voor, de mens beslist.**

De AI analyseert de situatie en biedt opties of aanbevelingen. De mens fungeert als 'Gatekeeper'; er gebeurt niets zonder expliciete goedkeuring. Dit is vaak de instapfase voor professionele toepassingen.

- **Dynamiek:** AI Suggestie Mens Goedkeuring/Actie.
- **Voorbeeld:** Een copiloot die code-suggesties doet, of een systeem dat fraude markeert voor inspectie door een analist.
- **Risico:** "Rubber stamping" (de mens keurt blind goed uit gemakzucht).
- **Governance:** Focus op het trainen van de menselijke beoordelaar.

### Modus 3: Collaboratief (The Partner)

**De dialoog staat centraal.**

Mens en AI werken iteratief samen aan een complex probleem. Het is een ping-pong spel van ideeën waarbij het eindresultaat een mix is van beide intelligenties. Dit wordt ook wel 'Co-Intelligentie' of het 'Centaur-model' genoemd.

- **Dynamiek:** Mens AI (Continue lus van input en feedback).
- **Voorbeeld:** Samen met ChatGPT een strategisch plan brainstormen en verfijnen.
- **Risico:** Vertroebeling van eigenaarschap (wie bedacht wat?) en verlies van eigen kritisch denkvermogen.
- **Governance:** Richtlijnen voor bronvermelding en fact-checking.

### Modus 4: Gedelegeerd (The Agent)

**AI voert uit, de mens beheert uitzonderingen.**

Hier draaien we het proces om: we ontwerpen de workflow zo dat AI het 'zware werk' doet. De mens stapt uit de dagelijkse loop en grijpt alleen in als de AI aangeeft het niet te weten (laag betrouwbaarheidsscore) of als er een foutmelding is. Dit heet vaak *Human-on-the-loop*.

- **Dynamiek:** AI Uitvoering (Alleen bij Fout) Mens.
- **Voorbeeld:** Een chatbot die zelfstandig klantvragen afhandelt en alleen doorverbindt bij boze klanten.
- **Risico:** 'Silent failures' (fouten die niet als fout worden herkend) en degradatie van menselijke expertise omdat ze het werk nooit meer zelf doen.
- **Governance:** Strenge geautomatiseerde monitoring en steekproeven (Audits).

Menselijke regie betekent in deze context niet voortdurende handmatige controle, maar duidelijke afspraken over wanneer, hoe en door wie wordt ingegrepen bij afwijkend gedrag of overschrijding van vastgestelde grenzen.

### Modus 5: Autonoom (The Entity)

**AI stelt doelen en handelt zelfstandig.**

Het systeem krijgt een breed mandaat (bijv. "Optimaliseer de inkoopvoorraad") en bepaalt zelf de sub-taken, timing en methode. De menselijke rol beperkt zich tot het stellen van de kaders (het beleid) en de 'Kill Switch'.

- **Dynamiek:** Mens (Beleid) AI (Autonome Uitvoering).
- **Voorbeeld:** High-frequency trading algoritmes of volledig autonome supply chain planners.
- **Risico:** Onvoorspelbaar emergent gedrag en kettingreacties (Flash Crashes).
- **Governance:** 'Circuit Breakers' (noodstoppen) en beleidsmatige constraints (wat mag de AI absoluut niet).

Menselijke regie betekent in deze context niet voortdurende handmatige controle, maar duidelijke afspraken over wanneer, hoe en door wie wordt ingegrepen bij afwijkend gedrag of overschrijding van vastgestelde grenzen.

______________________________________________________________________

## 3. Risico & Validatie Matrix

Hoe hoger de modus, hoe zwaarder de validatie-eisen.

| Modus                | Primaire Validatie              | Rol van de Mens          | Focus van Eigenaarschap |
| :------------------- | :------------------------------ | :----------------------- | :---------------------- |
| **1. Instrumenteel** | Gebruikerstest (UAT)            | Uitvoerder               | Taakgericht             |
| **2. Adviserend**    | Precisie-meting                 | Beslisser (Gatekeeper)   | Besluitvorming          |
| **3. Collaboratief** | Ervaring & Bruikbaarheid        | Partner                  | Resultaatgericht        |
| **4. Gedelegeerd**   | Continue Monitoring & **Drift** | Toezichthouder (Auditor) | Procesgericht           |
| **5. Autonoom**      | Simulatie & Stress-testing      | Beleidsbepaler           | Systeemgericht          |

______________________________________________________________________

## 4. Toepassing in Projecten

Bij het starten van een project (Fase Discovery) moet de beoogde modus worden vastgelegd in het **Project Charter**.

!!! tip "Begin laag, schaal op"

Start een gebruikscasus in **Modus 2 (Adviseur)** om data te verzamelen en vertrouwen te bouwen. Pas als de kwaliteit bewezen is (>90%), kan worden overgestapt naar **Modus 4 (Gedelegeerd)**.

!!! warning "Waarschuwing"

Probeer niet direct naar Modus 4 of 5 te springen zonder de tussenliggende leerfases.

______________________________________________________________________

## 4b. Acceptatiecriteria voor Modus 4-5 (Agentisch)

Wanneer een systeem in Modus 4 (Gedelegeerd) of Modus 5 (Autonoom) opereert, gelden aanvullende acceptatiecriteria bovenop de standaard Gate-eisen:

**Functionele Criteria:**

- [ ] Agent classificeert taken correct in ≥ \[X%\] van de gevallen
- [ ] Agent roept de juiste tools/API's aan voor \[specifieke taken\]
- [ ] Agent genereert output in het juiste formaat en de juiste toon

**Veiligheid & Escalatie:**

- [ ] Agent escaleert ambigue gevallen naar een mens bij \[drempelwaarde vertrouwen\]
- [ ] Escalatiepad is gedefinieerd: agent → \[menselijke rol\] → oplossing
- [ ] Mens kan agentbeslissingen overschrijven via \[mechanisme\]
- [ ] Tijd tot menselijke review is ≤ \[X minuten\] voor kritieke escalaties

**Controleerbaarheid:**

- [ ] Elke agentbeslissing wordt gelogd met: invoer, aangeroepen tools, beslissing, vertrouwensscore, eventuele menselijke override
- [ ] Audittrail is doorzoekbaar door: AI PM, compliance, supportteam

**Scopegrenzen (Kritiek):**

- [ ] Agent handelt: \[specifieke takenlijst\]
- [ ] Agent handelt NIET: \[uitgesloten taken\]
- [ ] Scope is gedocumenteerd in: systeemprompts, harde grenzen, tool-toegang

**Governance:**

- [ ] Cross-functionele goedkeuring: Business ☑ | Compliance ☑ | Techniek ☑
- [ ] Monitoring-dashboard toont: beslissingsvolume, escalatiepercentage, override-percentage

______________________________________________________________________

## 5. Operationeel Model voor Modus 4-5

Wanneer een systeem in Modus 4 of 5 opereert, verschuift de rol van het team van uitvoering naar orkestratie. Het Mens-Machine-Mens (M-M-M) patroon beschrijft deze cyclus:

```
[Mens definieert doel & grenzen] → [Machine voert uit] → [Mens valideert & stuurt bij]
```

### Teamsamenstelling bij Modus 4-5

Naast de standaard [rollen](../08-rollen-en-verantwoordelijkheden/index.md) zijn bij agentische systemen de volgende verantwoordelijkheden kritiek:

| Verantwoordelijkheid   | Beschrijving                                                                    | Draagt bij aan          |
| :--------------------- | :------------------------------------------------------------------------------ | :---------------------- |
| **Doelregie**          | Definieert het "waarom" en "wat" — vertaalt business-doelen naar agent-mandaten | AI PM                   |
| **Systeemregie**       | Optimaliseert het mens-machine systeem, bewaakt flow en leerproces              | Tech Lead               |
| **Agent-orchestratie** | Configureert orkestratiepatronen, tool-sets en iteratielimieten                 | Tech Lead / AI Engineer |
| **Kwaliteitsborging**  | Valideert output, bewaakt scopegrenzen en voert adversarial tests uit           | Guardian / AI Tester    |

### Handover-protocol: Agent naar Mens

Definieer vooraf wanneer en hoe een agent werk overdraagt aan een mens:

- **Vertrouwensdrempel:** Agent escaleert bij confidence score onder \[X%\].
- **Domeingrens:** Agent escaleert bij taken buiten gedefinieerde scope.
- **Foutgrens:** Agent stopt na \[N\] opeenvolgende fouten.
- **Budgetgrens:** Agent stopt bij bereiken van token- of kostenlimiet.

Elke escalatie wordt gelogd in het [beslissingsspoor](../08-technische-standaarden/09-agentic-ai-engineering.md).

______________________________________________________________________

## 6. Gerelateerde Modules

- [Kernprincipes](../01-ai-native-fundamenten/01-definitie.md)
- [Validatie Model](../01-ai-native-fundamenten/04-validatie-model.md)
- [Risicobeheer](../07-compliance-hub/02-risicobeheer/index.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Valkuilencatalogus](../17-bijlagen/valkuilen-catalogus.md)

______________________________________________________________________
