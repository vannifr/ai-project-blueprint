---
versie: '1.0'
description: 'Compliance Hub: alle wettelijke en ethische vereisten voor AI-projecten op één plek — EU AI Act, risicobeheer, ethische richtlijnen, incidentrespons, red teaming en veiligheidschecklists.'
---

# 1. Risicobeheersing & Compliance

## 1. Doel van deze Module

Compliance is geen rem, maar de remmen op een auto zorgen ervoor dat je veilig hard kunt rijden. Deze module definieert de **Rode Lijnen**: de ethische en wettelijke grenzen waarbinnen we innoveren. Het centraliseert de vereisten vanuit de EU AI Act en interne waarden.

______________________________________________________________________

## 2. Risico-Classificatie (De Piramide)

Voordat een project start (in **Verkenning & Strategie**), moet het worden ingedeeld in een risicocategorie. Dit bepaalt de zwaarte van het toezicht.

| Risico Niveau       | Omschrijving                                              | Voorbeeld                                                | Vereiste Actie                                                                                                                                  |
| :------------------ | :-------------------------------------------------------- | :------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Onacceptabel**    | Systemen die mensen manipuleren of social scoring doen.   | Real-time gezichtsherkenning in openbare ruimte.         | **VERBODEN**. Project wordt direct gestopt.                                                                                                     |
| **Hoog Risico**     | AI met impact op kritieke infrastructuur of grondrechten. | CV-scanner voor sollicitanten, kredietwaardigheidstoets. | Volledige EU AI Act Compliance ([Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md), Menselijk toezicht, CE-markering). |
| **Beperkt Risico**  | Systemen met interactie of die content genereren.         | Klantenservice Chatbot, Marketing tekstgenerator.        | Transparantieplicht. De gebruiker moet weten dat hij met AI praat.                                                                              |
| **Minimaal Risico** | Interne optimalisaties zonder persoonsgegevens.           | Spamfilter, voorraadvoorspelling, code-assistent.        | Geen specifieke eisen (Gedragscode aanbevolen).                                                                                                 |

______________________________________________________________________

## 3. De Rol van de 'Guardian' (Ethicus)

De Guardian is de "Beschermheer" van de waarden van de organisatie. Deze rol is onafhankelijk van het ontwikkelteam.

- **Mandaat:** De Guardian heeft veto-recht (via een 'Stop-knop') in elke fase van het project als de **Rode Lijnen** worden overschreden.
- **Taken:**
- Fase 1: Toetst de **Doeldefinitie** op ethische wenselijkheid.
- Fase 2 & 3: Voert **Fairness audit (bias audit)en** (Bias audits) uit.
- Fase 5: Voert periodieke 'Vibe Checks' uit op productie-systemen.

______________________________________________________________________

## 4. De Fairness audit (bias audit) (Bias Audit)

AI leert van data uit het verleden en kan daardoor vooroordelen overnemen. We toetsen elk Hoog en Beperkt risico systeem op drie niveaus:

1. **Representativiteit:** Is de data een goede afspiegeling van de werkelijkheid?
1. **Stereotypering:** Bevestigt de AI schadelijke clichés?
1. **Gelijke Behandeling:** Krijgt elke gebruikersgroep dezelfde kwaliteit van antwoorden?

______________________________________________________________________

## 5. Beheer van Incidenten

Wat als het misgaat?

- **De Noodstop (Circuit Breaker):** Voor autonome systemen (**Samenwerkingsmodus** 4 & 5) moet er een technische of procedurele manier zijn om de AI direct 'offline' te halen.
- **Meldingsplicht:** Incidenten waarbij mensen zijn benadeeld moeten binnen 24 uur worden gemeld aan het interne Compliance/Legal team.

______________________________________________________________________

## 6. Documentatievereisten (Het Dossier)

Voor Hoog Risico systemen is een 'Technisch Dossier' verplicht. Dit bevat:

- **Systeembeschrijving:** Wat doet het en voor wie?
- **Dataset Specificaties:** Waar komt de data vandaan en hoe is deze geëvalueerd (**Data-Evaluatie**)?
- **Risicobeheerplan:** Welke risico's zijn er en hoe zijn ze gemitigeerd?
- **Instructies voor Gebruik:** Handleiding voor de menselijke toezichthouder.
- **Logboeken:** Bewijs van de werking en beslissingen ([Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)).

______________________________________________________________________

## 7. Privacy-by-Design (AVG/GDPR) — Praktische richtlijnen

**Doel:** privacy is geen bijlage, maar een ontwerpkeuze.

### Minimale regels (altijd)

- **Dataminimalisatie:** verzamel/verwerk alleen wat noodzakelijk is.
- **Doelbinding:** hergebruik data niet automatisch voor andere doelen.
- **Transparantie:** gebruiker/betrokkene weet wanneer AI wordt ingezet (waar relevant).
- **Beveiliging:** toegang, logging en retentie zijn ingericht vóór livegang.

### Privacy acties per fase

**Fase 1 (Verkenning & Strategie):**

- Vul [Data & Privacyblad](../09-sjablonen/11-privacy-data/privacyblad.md) op hoofdlijnen in.
- Bepaal of een DPIA nodig is (zie [Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) triggers).

**Fase 2 (Validatie):**

- Test met zo min mogelijk persoonsgegevens (pseudonimiseer waar mogelijk).
- Leg vast welke logs je nodig hebt en hoe je privacy borgt.

**Fase 3 (Realisatie):**

- Implementeer redactie/pseudonimisering in pipelines waar mogelijk.
- Zorg dat toegang tot prompts/config beperkt is (change control).

**Fase 4 (Levering):**

- Transparantie en gebruiksinstructies publiceren (indien extern/klantgericht).
- Verwerkersafspraken en datalocatie bevestigd.

**Fase 5 (Beheer & Optimalisatie):**

- Monitor op datalekken/ongewenste data in logs.
- Periodieke review van retentie en toegangsrechten.

### Livegang-voorwaarde

Geen livegang zonder:

- [Data & Privacyblad](../09-sjablonen/11-privacy-data/privacyblad.md) ingevuld en akkoord (Privacy/DPO indien nodig)
- Logging- en retentieafspraken vastgelegd (zie [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md))

______________________________________________________________________

______________________________________________________________________

## 8. Agentic AI & Constitutional AI

Wanneer AI-systemen autonoom acties uitvoeren (Modus 4 & 5), verschuift de focus naar **Constitutional AI**:

- **Actieradius:** Technische inperking van wat een agent mag doen (bijv. maximale budgetlimieten).
- **Rode-Lijnen-bewaking:** Real-time monitoring die acties blokkeert als deze de **Rode Lijnen** dreigen te overschrijden.

Wanneer een AI‑systeem handelingen kan uitvoeren in andere systemen, wordt expliciet vastgelegd welke systemen en functies toegankelijk zijn, onder welke voorwaarden dit mag plaatsvinden en hoe toegang direct kan worden beperkt of ingetrokken bij afwijkingen of incidenten.

______________________________________________________________________

**Volgende stap:** Bepaal de risicoklasse van uw systeem en kies het bijbehorende compliance-pad.
→ Gebruik de [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) als startpunt.
→ Zie ook: [Risicoclassificatie](../01-ai-native-fundamenten/05-risicoclassificatie.md) | [Besluitvormingsmatrix](../08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md)
