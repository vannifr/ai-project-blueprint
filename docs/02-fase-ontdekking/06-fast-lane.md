---
versie: '1.0'
type: guide
layer: 2
phase: [1]
roles: [AI Product Manager]
---

# 1. Snelle Route (Fast Lane)

## 1. Doel

De Fast Lane is bedoeld om **veilig en snel** waarde te testen voor **laag‑risico** AI‑toepassingen, zonder onnodige bureaucratie—maar **met minimale governance**.

## 2. Toelatingscriteria (allemaal verplicht)

Een gebruikscasus mag alleen Fast Lane als aan **alle** punten is voldaan:

1. **EU AI Act risiconiveau = Minimaal** (zie Compliance Hub)
1. **Samenwerkingsmodus = 1 of 2** (Instrumenteel of Adviserend; zie AI-Samenwerkingsmodi)
1. De AI **neemt geen beslissingen over mensen** (geen selectie/toekenning/afwijzing)
1. Geen verwerking van **bijzondere persoonsgegevens** (gezondheid, religie, biometrie, etc.)
1. Output wordt **altijd** door een mens bekeken vóór gebruik (geen autonoom versturen/uitvoeren)
1. Alleen intern gebruik óf (indien extern) **100% transparantie** ("Je spreekt met AI")

**Als één criterium niet gehaald wordt:**
→ *geen Fast Lane*, volg de standaard lifecycle (Verkenning & Strategie t/m Beheer & Optimalisatie).

### Harde uitsluitingen

Fast Lane is **niet toegestaan** voor de volgende categorieën:

1. **Externe customer-facing chatbots of publieke contentgeneratie** zonder aantoonbare Art. 50 disclosure/labeling implementatie.
1. **Tool-using agents met write-access** naar bedrijfssystemen (bijv. ERP, CRM, HRM) — ook niet in "pilot"-vorm.
1. **Systemen met autonome beslissingen** die personen raken (screening, scoring, toekenning).

!!! check "Bewijsvoering voor Art. 50 implementatie (indien van toepassing)"

- [ ] Screenshot of UX-copy van disclosure/labeling in de gebruikersinterface
- [ ] Testcases in Golden Set die disclosure/labeling-gedrag valideren
- [ ] Vermelding in Validatierapport met verwijzing naar bewijsstukken

## 3. Minimumpakket opleveringen (Fast Lane)

- **[Project Charter](../09-sjablonen/01-project-charter/template.md)** (Fast Lane variant: kort)
- **[Risico Pre‑Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)** (moet "Minimaal" bevestigen)
- **[Doelkaart (goal card)](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)** (incl. Rode Lijnen)
- **[Golden Set Test & Acceptatie Protocol](../09-sjablonen/07-validatie-bewijs/template.md)** (light: minimaal 20 cases)
- **[Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)** (bewijs van testresultaten)

**Wat mag je overslaan in Fast Lane:**

- Uitgebreide business case (ROI) *mag later*, maar je noteert wél een "waarde‑hypothese" in het Charter.
- Uitgebreid technisch dossier (alleen relevant bij hoog risico).

## 4. Fast Lane Gates (simpel en toetsbaar)

### Gate FL‑1 — Start experiment (max. 2 weken)

**Go** als:

- Risico Pre‑Scan = Minimaal
- Doelkaart (goal card) bevat Rode Lijnen
- Minimaal testplan staat klaar (Golden Set ≥ 20)

### Gate FL‑2 — Interne live pilot (max. 4 weken)

**Go** als:

- [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) normen voor Minimaal risico
- Logging/traceerbaarheid is ingericht op basismeta‑niveau
- Incidentprocedure bekend bij team

## 5. Wanneer Fast Lane stopt (escalatie)

Fast Lane stopt direct en je stapt over op standaard lifecycle als:

- Samenwerkingsmodus opschuift naar **3+**
- De tool extern gebruikt gaat worden met impact op klanten
- Het datagebruik uitbreidt naar (bijzondere) persoonsgegevens
- Er 1 Kritieke fout optreedt (Rode Lijnen geraakt)

______________________________________________________________________

**Volgende stap:** Als u in de Fast Lane past, start direct met [Fase 2 — Validatie](../03-fase-validatie/01-doelstellingen.md)
→ Zie ook: [Explorer Kit](../00-explorer-kit/index.md)
