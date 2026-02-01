# 🚀 Module 09.03: Risico Pre-Scan (Gate 1 Checklist)
## Documentbeheer
- **Document-ID:** TMP-09-03
- **Titel:** 📍 Module 09.03: Risico Pre-Scan (Gate 1 Checklist)
- **Versie:** 1.0
- **Status:** Definitief
- **Eigenaar:** AI Competence Center
- **Laatst herzien:** 2026-02-01
- **Wijziging t.o.v. vorige versie:** DPIA-triggers toegevoegd aan sectie Privacy & Data.

---

## 📖 Doel
Dit sjabloon dient voor de initiële risico-inventarisatie in **Verkenning & Strategie** (Fase 1). Het helpt bij het vroegtijdig identificeren van blokkades op het gebied van wetgeving (EU AI Act), privacy en ethiek.

---

**Project:** [Naam Project]  
**Datum:** [DD-MM-JJJJ]  
**Ingevuld door:** [Naam]

---

### 🎯 Deel A: EU AI Act Classificatie
*Kruis aan wat van toepassing is. Als één van deze 'Ja' is, bepaalt dat de risicocategorie.*

#### 1. Verboden Praktijken (📍 ONACCEPTABEL)
*   [ ] Gebruikt het systeem subliminale technieken om gedrag te manipuleren?
*   [ ] Wordt er gebruik gemaakt van biometrische categorisering (ras, politiek, religie)?
*   [ ] Wordt er in openbare ruimtes real-time biometrische identificatie toegepast?  
    > **Indien JA op één van bovenstaande: STOP PROJECT DIRECT.**

#### 2. Hoog Risico Systemen (📍 HOOG RISICO)
*   [ ] Wordt het gebruikt in kritieke infrastructuur (water, energie, verkeer)?
*   [ ] Beslist het over toegang tot onderwijs of beoordeling van studenten?
*   [ ] Beslist het over werving, selectie of promotie van werknemers?
*   [ ] Beslist het over toegang tot diensten (krediet, uitkeringen, verzekeringen)?  
    > **Indien JA: Volledige compliance verplicht (Technisch Dossier, CE-markering).**

#### 3. Beperkt Risico (📍 BEPERKT RISICO)
*   [ ] Is er directe interactie met mensen (chatbot, emotie-herkenning)?
*   [ ] Genereert het systeem inhoud (tekst, beeld, geluid)?  
    > **Indien JA: Transparantieplicht (Gebruiker moet weten dat het AI is).**

---

### 🎯 Deel B: Privacy & Data (AVG)
*   **Worden er persoonsgegevens verwerkt?** [Ja/Nee]
*   **Is er een wettelijke grondslag voor dit gebruik?** [Ja/Nee]
*   **Wordt data gedeeld met externe partijen (bijv. OpenAI, Azure)?** [Ja/Nee]

#### B.4 DPIA-triggers (indien één “Ja”: DPIA starten of DPO raadplegen)
- [ ] Grootschalige verwerking van persoonsgegevens
- [ ] Systematische monitoring van gedrag (bijv. profiling)
- [ ] Gebruik van bijzondere persoonsgegevens
- [ ] Geautomatiseerde beoordeling met significante impact op personen
- [ ] Nieuwe technologie + hoge risico context (twijfel = DPO betrekken)

---

### 🎯 Deel C: Ethische Quickscan
*   **Kan het systeem groepen discrimineren of uitsluiten (Bias)?** [Ja/Nee]
*   **Is de werking uitlegbaar aan een leek?** [Ja/Nee]
*   **Is er een menselijke 'noodstop' of override mogelijk?** [Ja/Nee]

---

### 🎯 Conclusie & Advies Guardian
*   **Definitief Risiconiveau:** [Laag / Beperkt / Hoog / Verboden]
*   **Actievereisten:** [Bijv. "DPIA uitvoeren", "Validatierapport opstellen", "Disclaimer toevoegen"]

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
