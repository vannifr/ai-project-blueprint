---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# Module 02.F: Snelle Route (Fast Lane)

## 1. Doel

De Fast Lane is bedoeld om **veilig en snel** waarde te testen voor **laag‑risico** AI‑toepassingen, zonder onnodige bureaucratie—maar **met minimale governance**.

## 2. Toelatingscriteria (allemaal verplicht)

Een use case mag alleen Fast Lane als aan **alle** punten is voldaan:

1. **EU AI Act risiconiveau = Minimaal** (zie MOD‑07)
1. **Samenwerkingsmodus = 1 of 2** (Instrumenteel of Adviserend; zie MOD‑00‑06)
1. De AI **neemt geen beslissingen over mensen** (geen selectie/toekenning/afwijzing)
1. Geen verwerking van **bijzondere persoonsgegevens** (gezondheid, religie, biometrie, etc.)
1. Output wordt **altijd** door een mens bekeken vóór gebruik (geen autonoom versturen/uitvoeren)
1. Alleen intern gebruik óf (indien extern) **100% transparantie** (“Je spreekt met AI”)

**Als één criterium niet gehaald wordt:**
→ *geen Fast Lane*, volg de standaard lifecycle (MOD‑02 t/m MOD‑06).

## 3. Minimumpakket deliverables (Fast Lane)

- **TMP‑09‑01 Project Charter** (Fast Lane variant: kort)
- **TMP‑09‑03 Risico Pre‑Scan** (moet “Minimaal” bevestigen)
- **TMP‑09‑02 Doelkaart** (incl. Rode Lijnen)
- **TMP‑09‑05 Test & Acceptatie Protocol** (light: minimaal 20 cases)
- **TMP‑09‑06 Validatierapport** (bewijs van testresultaten)

**Wat mag je overslaan in Fast Lane:**

- Uitgebreide business case (ROI) *mag later*, maar je noteert wél een “waarde‑hypothese” in het Charter.
- Uitgebreid technisch dossier (alleen relevant bij hoog risico).

## 4. Fast Lane Gates (simpel en toetsbaar)

### Gate FL‑1 — Start experiment (max. 2 weken)

**Go** als:

- Risico Pre‑Scan = Minimaal
- Doelkaart bevat Rode Lijnen
- Minimaal testplan staat klaar (Gouden Set ≥ 20)

### Gate FL‑2 — Interne live pilot (max. 4 weken)

**Go** als:

- Validatierapport (TMP‑09‑06) voldoet aan **MOD‑01‑07** normen voor Minimaal risico
- Logging/traceerbaarheid is ingericht op basismeta‑niveau
- Incidentprocedure bekend bij team

## 5. Wanneer Fast Lane stopt (escalatie)

Fast Lane stopt direct en je stapt over op standaard lifecycle als:

- Samenwerkingsmodus opschuift naar **3+**
- De tool extern gebruikt gaat worden met impact op klanten
- Het datagebruik uitbreidt naar (bijzondere) persoonsgegevens
- Er 1 Kritieke fout optreedt (Rode Lijnen geraakt)
