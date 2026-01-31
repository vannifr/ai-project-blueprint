# 🎨 Huisstijl & Schrijfwijzer (Styleguide v2.0)

Deze gids borgt dat alle modules in het Playbook consistent, begrijpelijk en uniform blijven, ongeacht wie ze schrijft.

---

## 1. Toon & Stem (Tone of Voice)
Wij schrijven voor professionals die actie willen ondernemen. Onze taal is direct, activerend en zelfverzekerd, maar nooit arrogant.

*   **Actief boven Passief:**
    *   ❌ Fout: "Door het team zal worden beoordeeld of de data geschikt is."
    *   ✅ Goed: "Het team evalueert de data."
*   **De "Wij"-vorm:** We schrijven vanuit het perspectief van het projectteam. "Wij bouwen", "Wij toetsen".
*   **Geen Academisch Jargon:** Vermijd wollig taalgebruik. We schrijven geen scriptie, maar een handleiding.

---

## 2. Terminologie & Lexicon (De Vertaallijst)
Wij slaan de brug tussen techniek en business. Gebruik daarom consequent de Nederlandse, zakelijke termen in plaats van Engels technisch jargon.

| ❌ Vermijd Jargon (Engels/Tech) | ✅ Gebruik (Playbook Standaard) | Toelichting |
| :--- | :--- | :--- |
| Intent / Intent Record | **Doeldefinitie** | Het 'Waarom' |
| Context Artifacts | **Sturingsinstructies** | Prompts/Configs |
| Constraints / Guardrails | **Rode Lijnen** | De harde grenzen |
| Data Readiness Check | **Data-Evaluatie** | Framework: Toegang, Kwaliteit, Relevantie |
| Proof of Value (PoV) | **Praktijkproef** | Mag PoV blijven als afkorting |
| Model Drift | **Prestatieverloop** | Verslechtering over tijd |
| RAG (Retrieval Augmented Gen) | **Kenniskoppeling** | Verbinden aan eigen docs |
| Hyperparameter Tuning | **Afstellen van het model** | Fijn-afstelling |
| Shadow AI | **Wildgroei** | Ongecontroleerd gebruik |
| Deploy / Deployment | **Ingebruikname / Livegang** | |
| Total Cost of Ownership (TCO) | **Het Kostenplaatje** | |

---

## 3. Plagiaat & Originaliteit
*   **Strikte Regel:** Kopieer nooit letterlijke zinnen uit bronbestanden (zoals PMI-documenten, ISO-normen of externe whitepapers).
*   **Herformuleren:** Lees de bron, begrijp de kern, en schrijf het op alsof je het uitlegt aan een collega.
*   **Context:** Vertaal algemene theorie altijd naar de specifieke context van onze modulaire aanpak.

---

## 4. Opmaakstandaarden (Markdown)
Consistentie zorgt voor leesbaarheid.

*   **Titels:**
    *   `#` voor Modulenamen.
    *   `##` voor Hoofdstukken.
    *   `###` voor Activiteiten.
*   **Navigatie-Icoontjes:** Gebruik emoji's spaarzaam maar functioneel:
    *   📂 = Module / Hoofdstuk
    *   🎯 = Doelstelling
    *   ⚙️ = Activiteiten / Proces
    *   👥 = Rollen (RACI)
    *   ✅ = Checklists / Gates
*   **Lijsten:** Gebruik bullets voor opsommingen en genummerde lijsten voor stappenplannen.

---

## 📝 Instructies voor Auteurs
Volg dit proces wanneer je een nieuwe module toevoegt of een bestaande bewerkt.

### Stap 1: Bepaal de Plaats in de Levenscyclus
Kijk naar **Module 00 (Het Strategisch Kader)**. Waar past jouw document?
- Is het strategie? -> Module 00 - 02.
- Is het uitvoering? -> Module 03 - 05.
- Is het beheer? -> Module 06.
- Is het een template? -> Module 09+.

### Stap 2: Gebruik de Vaste Structuur
Elke Proces-Module moet de volgende anatomie hebben:
1.  **Doelstelling (Het Waarom):** Eén krachtige zin.
2.  **Intrede Criteria (Definition of Ready):** Wat moet er af zijn voordat we mogen beginnen?
3.  **Kernactiviteiten (Het Wat):** 3 tot 5 duidelijke stappen. Gebruik de termen uit het Lexicon.
4.  **RACI (Het Wie):** Wie is Responsible (R) en wie is Accountable (A)?
5.  **Exit Criteria (De Gate):** De checklist om de fase af te sluiten.
6.  **Deliverables:** De concrete bestanden die worden opgeleverd.

### Stap 3: De 'Jip en Janneke' Check (Begrijpelijkheid)
Lees je concepttekst door met de bril van een niet-technische manager (bijv. een Financieel Directeur).
- Snapt hij/zij wat "Inference costs" zijn? -> Nee? Verander in **"Gebruikskosten"**.
- Snapt hij/zij wat "Bias audit" is? -> Nee? Verander in **"Eerlijkheidstoets"**.

### Stap 4: Versiebeheer
Eindig elk document altijd met een footer voor traceerbaarheid:

---
**Versie:** [X.X]
**Datum:** [DD maand JJJJ]
**Status:** [Concept / Definitief]

---

## Checklist voor Publicatie
- [ ] Heb ik alle Engelse jargon-termen vertaald naar de Playbook-standaard?
- [ ] Heb ik gecontroleerd op plagiaat (geen copy-paste)?
- [ ] Is de toon actief ("Wij doen") en niet passief ("Er wordt gedaan")?
- [ ] Staan de icoontjes bij de juiste secties?

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
