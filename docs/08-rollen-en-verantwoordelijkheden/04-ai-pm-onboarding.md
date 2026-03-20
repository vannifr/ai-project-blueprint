---
versie: '1.0'
type: playbook
layer: 1
roles: [AI Product Manager]
tags: [onboarding, playbook]
summary: Stap-voor-stap inwerkgids waarmee nieuwe AI Project Managers in zes weken van observatie naar volwaardig eigenaarschap groeien.
answers: [Hoe voer ik AI PM Onboarding Playbook uit?]
---

# AI PM Onboarding Playbook

!!! abstract "Doel"
    Stap-voor-stap inwerkgids waarmee nieuwe AI Project Managers in zes weken van observatie naar volwaardig eigenaarschap groeien.

Stap-voor-stap inwerkgids voor nieuwe AI Project Managers die instromen in een lopend of nieuw AI-project. Dit playbook helpt u om in zes weken van observatie naar volwaardig eigenaarschap te groeien, met concrete deliverables per fase.

!!! info "Verschil met klassieke PM-onboarding"
    AI-projecten kennen unieke uitdagingen: probabilistische uitkomsten, iteratieve modelvalidatie en nauwe samenwerking met Data Scientists. Deze gids richt zich specifiek op de vaardigheden en het begrip die u als AI PM nodig heeft bovenop uw bestaande PM-ervaring.

______________________________________________________________________

## Week 1 — Leren & Observeren (Dag 1-5)

Het doel van week 1 is om het systeem, de data en de succesdefinitie te doorgronden. Stel vragen, luister en documenteer.

### Dag 1-2: Deep Dive in Systeem, Data & Doelstelling

- [ ] Lees het Project Charter en de Doelkaart van het project door.
- [ ] Bestudeer de huidige modelarchitectuur met de Tech Lead (1-op-1 sessie, 60 min).
- [ ] Loop de data pipeline door met de Data Scientist (1-op-1 sessie, 60 min): databronnen, kwaliteitsniveaus, bekende beperkingen.
- [ ] Spreek de Sponsor (30 min): wat is de zakelijke verwachting? Hoe definieert de Sponsor succes?
- [ ] Maak een eerste inventarisatie van de huidige metrics en drempelwaarden.

**Deliverable:** Persoonlijke samenvatting (1 pagina) van systeem, data en succeskriterium.

### Dag 3-4: Faalmodi & Stakeholderverwachtingen

- [ ] Bekijk de laatste 3 Model Health Reviews (indien beschikbaar).
- [ ] Identificeer de top-3 faalscenario's met de Tech Lead en Data Scientist.
- [ ] Voer stakeholder-interviews uit (minimaal 3): wat is hun verwachting, welke zorgen hebben zij, wat is hun ervaring met het systeem tot nu toe?
- [ ] Bestudeer het Incident Response plan en de escalatieprocedure.

**Deliverable:** Stakeholder-verwachtingenmatrix (wie verwacht wat, met welke prioriteit).

### Dag 5: Documentatie-setup

- [ ] Richt uw persoonlijk Decision Log in (gebruik het [Projectdagboek-sjabloon](../09-sjablonen/13-project-dagboek/template.md)).
- [ ] Start een Question List: alle openstaande vragen die u nog moet beantwoorden.
- [ ] Stel een eerste communicatieschema op voor de komende twee weken.
- [ ] Plan uw eerste 1-op-1 meetings met alle kernrollen.

**Deliverable:** Ingevuld Decision Log (initieel), Question List, communicatieschema.

______________________________________________________________________

## Week 2 — Eerste Echte Beslissingen (Dag 6-10)

In week 2 neemt u uw eerste beslissingen. Dit is bewust vroeg: het dwingt u om uw begrip te toetsen.

### Experimentschatting

- [ ] Bestudeer een lopend of recent afgerond Experiment Ticket.
- [ ] Maak een eigen schatting voor het volgende experiment: scope, time-box, teamallocatie.
- [ ] Bespreek uw schatting met de Tech Lead en Data Scientist; vergelijk met hun inzicht.
- [ ] Pas uw schatting aan op basis van feedback.

**Deliverable:** Eerste conceptversie van een [Experiment Ticket](../09-sjablonen/17-experiment-ticket/template.md).

### Eerste Model Health Review

- [ ] Bereid een Model Health Review voor met het [sjabloon](../09-sjablonen/18-modelgezondheid/template.md).
- [ ] Faciliteer de review (of observeer en geef feedback achteraf).
- [ ] Documenteer actiepunten en eigenaren.

**Deliverable:** Ingevulde Model Health Review met actiepuntenlijst.

### Reflectie: AI PM vs. Software PM

- [ ] Schrijf op welke aspecten van AI-projectmanagement fundamenteel anders zijn dan software PM.
- [ ] Identificeer minimaal 3 situaties waarin uw PM-intuïtie u misleidde of zou kunnen misleiden.
- [ ] Bespreek uw reflectie met een ervaren AI PM of de Sponsor.

**Deliverable:** Reflectieverslag (half pagina).

______________________________________________________________________

## Maand 2-3 — Eigenaarschap Opnemen

Na de inwerkperiode neemt u stapsgewijs volledig eigenaarschap over de AI PM-verantwoordelijkheden.

### RACI Verduidelijken

- [ ] Bestudeer de [RACI Matrix](02-raci-matrix.md) en bespreek met de Tech Lead waar de grenzen van uw verantwoordelijkheid liggen.
- [ ] Identificeer grijze gebieden (waar is de verantwoordelijkheid onduidelijk?) en los deze op.
- [ ] Maak concrete afspraken over wie wat beslist in de dagelijkse operatie.

### Eerste Moeilijke Gesprek

- [ ] Bereid een moeilijk stakeholdergesprek voor met behulp van de communicatiescripts uit het [Stakeholder Communicatie Playbook](03-stakeholder-communicatie.md).
- [ ] Voer het gesprek en documenteer het verloop in uw Decision Log.
- [ ] Vraag feedback aan een collega of mentor over uw aanpak.

### Monitoring Eigenaarschap

- [ ] Neem het eigenaarschap over de monitoring-dashboards over.
- [ ] Configureer persoonlijke alerts voor kritieke drempelwaarden.
- [ ] Voer uw eerste zelfstandige prestatierapportage uit richting de Sponsor.

**Deliverables maand 2-3:**

- [ ] Verduidelijkte RACI-afspraken met Tech Lead (gedocumenteerd).
- [ ] Minimaal 1 zelfstandig gevoerd moeilijk stakeholdergesprek (gedocumenteerd in Decision Log).
- [ ] Zelfstandig uitgevoerde Model Health Review.
- [ ] Eerste zelfstandige prestatierapportage aan Sponsor.
- [ ] Bijgewerkt communicatieschema voor het komende kwartaal.

______________________________________________________________________

## Onboarding Checklist — Totaaloverzicht

| Week / Periode | Deliverable                                     | Status |
| :------------- | :---------------------------------------------- | :----- |
| Dag 1-2        | Persoonlijke samenvatting systeem & data        | \[ \]  |
| Dag 3-4        | Stakeholder-verwachtingenmatrix                 | \[ \]  |
| Dag 5          | Decision Log, Question List, communicatieschema | \[ \]  |
| Week 2         | Concept Experiment Ticket                       | \[ \]  |
| Week 2         | Eerste Model Health Review                      | \[ \]  |
| Week 2         | Reflectieverslag AI PM vs. Software PM          | \[ \]  |
| Maand 2        | Verduidelijkte RACI-afspraken                   | \[ \]  |
| Maand 2        | Eerste moeilijk stakeholdergesprek              | \[ \]  |
| Maand 3        | Zelfstandige Model Health Review                | \[ \]  |
| Maand 3        | Zelfstandige prestatierapportage aan Sponsor    | \[ \]  |
| Maand 3        | Bijgewerkt communicatieschema kwartaal          | \[ \]  |

______________________________________________________________________

## Gerelateerde Modules

- [Rollen & Verantwoordelijkheden — Overzicht](index.md)
- [RACI Matrix](02-raci-matrix.md)
- [Stakeholder Communicatie Playbook](03-stakeholder-communicatie.md)
- [Experiment Ticket sjabloon](../09-sjablonen/17-experiment-ticket/template.md)
- [Model Healthsreview sjabloon](../09-sjablonen/18-modelgezondheid/template.md)
- [Projectdagboek sjabloon](../09-sjablonen/13-project-dagboek/template.md)

______________________________________________________________________

**Volgende stap:** Raadpleeg het [Rollen & Verantwoordelijkheden overzicht](index.md) voor de volledige rolbeschrijvingen en de [RACI Matrix](02-raci-matrix.md) voor de taakverdeling per projectfase.
