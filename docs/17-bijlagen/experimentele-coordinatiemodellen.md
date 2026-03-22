---
versie: '1.0'
type: reference
layer: 3
roles: [Data Scientist]
tags: [governance]
answers: [Wat is Experimentele Coordinatiemodellen?]
---

# 1. Experimentele Coordinatiemodellen

!!! warning "Experimenteel"
    De modellen in dit document zijn academisch onderbouwd maar niet breed gevalideerd in commerciele softwareteams. Ze zijn bedoeld als inspiratie voor hoog-mature organisaties ([Visionair-profiel](../13-organisatieprofielen/03-ai-expert.md)) die traditionele coordinatiemechanismen willen heroverwegen.

## 1. Doel

Traditionele Agile-coordinatie (standups, sprint planning, retrospectives) is ontworpen voor menselijke teams. Naarmate AI-agents een groter deel van het uitvoerende werk overnemen, ontstaat de vraag of er coordinatievormen bestaan die beter passen bij mens-machine teams. Dit document beschrijft vier experimentele modellen uit de academische literatuur.

______________________________________________________________________

## 2. Stigmergische Coordinatie

### Concept

Stigmergie is coordinatie via de omgeving in plaats van via directe communicatie. De term komt uit de biologie (termieten coordineren bouwwerk door feromonsporen achter te laten, niet door vergaderingen te houden).

In softwareteams betekent dit: agents en mensen coordineren via het werkproduct zelf — code commits, documentatiewijzigingen, issue-statussen en test-resultaten vormen de "feromonsporen" die de volgende actie sturen.

### Hoe het werkt

1. Agent A voltooit een taak en commit code.
1. De commit triggert automatisch tests en quality checks.
1. Agent B detecteert de verandering, analyseert de impact op zijn domein en past aan.
1. Geen expliciete overdracht of vergadering nodig.

### Academische basis

- Kevin Crowston (Syracuse University) publiceerde uitgebreid over stigmergische coordinatie in FLOSS-ontwikkeling (Free/Libre Open Source Software).
- De MIDST-tool (ACM CSCW) implementeerde stigmergische coordinatie voor data-science teams met positieve resultaten.

### Wanneer overwegen

- Teams met hoog aandeel agent-gedreven taken (Modus 4-5)
- Asynchrone, geografisch verspreide teams
- Open-source projecten met wisselende bijdragers

### Risico's

- Vereist uitstekende observeerbaarheid (wie deed wat, waarom)
- Kan leiden tot conflicterende wijzigingen zonder goede branch-strategie
- Minder geschikt voor taken die complexe menselijke afstemming vereisen

______________________________________________________________________

## 3. Prediction Market Model

### Concept

Teamleden "handelen" in succes-contracten voor projectonderdelen. De marktprijs weerspiegelt de collectieve inschatting van de slagingskans en onthult verborgen risico's die in traditionele schattingsmethoden onzichtbaar blijven.

### Hoe het werkt

1. Voor elk milestone of deliverable wordt een "contract" aangemaakt.
1. Teamleden kopen of verkopen contracten op basis van hun inschatting van de slagingskans.
1. Een dalende prijs signaleert verborgen problemen die het team niet expliciet benoemt.
1. Een stijgende prijs bevestigt vertrouwen in de aanpak.

### Academische basis

- Microsoft heeft intern meerdere prediction markets gedraaid, waaronder voor software-projectschattingen (Microsoft Research).
- Google, GE, HP en Best Buy hebben corporate prediction markets toegepast.

### Wanneer overwegen

- Grote teams (>10 personen) waar impliciete kennis verspreid zit
- Projecten met hoge onzekerheid over haalbaarheid
- Als aanvulling op, niet vervanging van, standaard schattingstechnieken

### Risico's

- Optimisme-bias: medewerkers handelen niet tegen eigen project
- Vereist psychologische veiligheid (eerlijk "verkopen" zonder repercussies)
- Kleine teams hebben onvoldoende "liquiditeit" voor zinvolle marktprijzen

______________________________________________________________________

## 4. Immuunsysteem-Model

### Concept

Autonome agents monitoren continu op "pathogenen" (bugs, technische schuld, security-kwetsbaarheden, drift) en neutraliseren deze zonder centrale commando-structuur. Vergelijkbaar met hoe het biologische immuunsysteem werkt: gedistribueerd, adaptief en zelfregulerend.

### Hoe het werkt

1. **Detectie-agents** scannen continu codebases, logs en metrics.
1. Bij detectie van een anomalie wordt een **respons-agent** getriggerd.
1. De respons-agent classificeert het probleem en past een mitigatie toe (of escaleert naar een mens).
1. Het systeem "onthoudt" eerdere patronen (episodisch geheugen) en reageert sneller op bekende dreigingen.

### Academische basis

- Artificial Immune Systems (AIS) is een erkend computationeel paradigma met tientallen jaren onderzoek.
- Toepassingen in intrusion detection, software fault detection en anomaly detection zijn gedocumenteerd in ACM, IEEE en ScienceDirect.

### Wanneer overwegen

- Grote productie-omgevingen met vele AI-systemen (Visionair-profiel)
- Aanvulling op bestaande [drift detectie](../06-fase-monitoring/05-drift-detectie.md)
- Omgevingen waar reactietijd kritiek is

### Risico's

- Vereist zeer mature observeerbaarheid en agent-governance
- Autonome correctie kan onbedoelde bijwerkingen hebben
- Moet altijd binnen [Circuit Breaker](../00-strategisch-kader/06-has-h-niveaus.md)-kaders opereren

______________________________________________________________________

## 5. Narratief-Gedreven Systeem

### Concept

In plaats van te sturen op gefragmenteerde user stories en features, stuurt het team op coherente verhalen over het systeem. Een "systeemnarratief" beschrijft hoe een gebruiker het systeem ervaart van begin tot eind, inclusief randgevallen en faalscenario's.

### Hoe het werkt

1. Het team schrijft en onderhoudt een leesbaar systeemnarratief.
1. AI-agents ontvangen het narratief als context en genereren code die past binnen het grotere verhaal.
1. Wijzigingen worden getoetst aan het narratief: "past deze feature in het verhaal?"
1. Het narratief evolueert mee met het systeem.

### Wanneer overwegen

- Producten met complexe gebruikersreizen
- Teams die moeite hebben om het "grote plaatje" te bewaken bij AI-gedreven ontwikkeling
- Als complement op de [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)

### Risico's

- Vereist sterke schrijfvaardigheid en discipline om het narratief actueel te houden
- Kan conflicteren met traditionele backlog-gestuurde aanpakken
- Minder geschikt voor puur technische systemen zonder gebruikersinteractie

______________________________________________________________________

## 6. Gerelateerde Modules

- [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
- [Agentic AI Engineering](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [De Visionair (Organisatieprofiel)](../13-organisatieprofielen/03-ai-expert.md)
- [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)
- [Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)

______________________________________________________________________
