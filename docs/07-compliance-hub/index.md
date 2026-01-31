# 📂 Module 07: Risicobeheersing & Compliance

## 🎯 1. Doel van deze Module
Compliance is geen rem, maar de remmen op een auto zorgen ervoor dat je veilig hard kunt rijden. Deze module definieert de **Rode Lijnen**: de ethische en wettelijke grenzen waarbinnen we innoveren. Het centraliseert de vereisten vanuit de EU AI Act en interne waarden.

---

## 📂 2. Risico-Classificatie (De Piramide)
Voordat een project start (in **Verkenning & Strategie**), moet het worden ingedeeld in een risicocategorie. Dit bepaalt de zwaarte van het toezicht.

| Risico Niveau | Omschrijving | Voorbeeld | ✅ Vereiste Actie |
| :--- | :--- | :--- | :--- |
| 🔴 **Onacceptabel** | Systemen die mensen manipuleren of social scoring doen. | Real-time gezichtsherkenning in openbare ruimte. | **VERBODEN**. Project wordt direct gestopt. |
| 🟠 **Hoog Risico** | AI met impact op kritieke infrastructuur of grondrechten. | CV-scanner voor sollicitanten, kredietwaardigheidstoets. | Volledige EU AI Act Compliance (**Validatierapport**, Menselijk toezicht, CE-markering). |
| 🟡 **Beperkt Risico** | Systemen met interactie of die content genereren. | Klantenservice Chatbot, Marketing tekstgenerator. | Transparantieplicht. De gebruiker moet weten dat hij met AI praat. |
| 🟢 **Minimaal Risico** | Interne optimalisaties zonder persoonsgegevens. | Spamfilter, voorraadvoorspelling, code-assistent. | Geen specifieke eisen (Gedragscode aanbevolen). |

---

## 👥 3. De Rol van de 'Guardian' (Ethicus)
De Guardian is de "Beschermheer" van de waarden van de organisatie. Deze rol is onafhankelijk van het ontwikkelteam.

*   **Mandaat:** De Guardian heeft veto-recht (via een 'Stop-knop') in elke fase van het project als de **Rode Lijnen** worden overschreden.
*   **Taken:**
    *   Fase 1: Toetst de **Doeldefinitie** op ethische wenselijkheid.
    *   Fase 2 & 3: Voert **Eerlijkheidstoetsen** (Bias audits) uit.
    *   Fase 5: Voert periodieke 'Vibe Checks' uit op productie-systemen.

---

## ⚙️ 4. De Eerlijkheidstoets (Bias Audit)
AI leert van data uit het verleden en kan daardoor vooroordelen overnemen. We toetsen elk Hoog en Beperkt risico systeem op drie niveaus:

1.  **Representativiteit:** Is de data een goede afspiegeling van de werkelijkheid?
2.  **Stereotypering:** Bevestigt de AI schadelijke clichés?
3.  **Gelijke Behandeling:** Krijgt elke gebruikersgroep dezelfde kwaliteit van antwoorden?

---

## ⚙️ 5. Beheer van Incidenten
Wat als het misgaat?

*   **De Noodstop (Circuit Breaker):** Voor autonome systemen (**Samenwerkingsmodus** 4 & 5) moet er een technische of procedurele manier zijn om de AI direct 'offline' te halen.
*   **Meldingsplicht:** Incidenten waarbij mensen zijn benadeeld moeten binnen 24 uur worden gemeld aan het interne Compliance/Legal team.

---

## 📂 6. Documentatievereisten (Het Dossier)
Voor Hoog Risico systemen is een 'Technisch Dossier' verplicht. Dit bevat:

*   **Systeembeschrijving:** Wat doet het en voor wie?
*   **Dataset Specificaties:** Waar komt de data vandaan en hoe is deze geëvalueerd (**Data-Evaluatie**)?
*   **Risicobeheerplan:** Welke risico's zijn er en hoe zijn ze gemitigeerd?
*   **Instructies voor Gebruik:** Handleiding voor de menselijke toezichthouder.
*   **Logboeken:** Bewijs van de werking en beslissingen (**Validatierapport**).

## 🤖 Toekomst: Agentic AI & Constitutional AI
Wanneer AI-systemen autonoom acties gaan uitvoeren (Modus 4 & 5), verschuift de focus naar **Constitutional AI**:
*   **Actieradius:** Technische inperking van wat een agent mag doen (bijv. maximale budgetlimieten).
*   **Guardrails:** Real-time monitoring die acties blokkeert als deze de **Rode Lijnen** dreigen te overschrijden.

---
**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Definitief
**Bron:** Gebaseerd op EU AI Act & Interne Beleidskaders

---
�
---
**Versie:** 2.1
**Datum:** 31 januari 2026
**Status:** Definitief

---
� 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
