# Module 02.F: Snelle Route (Fast Lane)
## Documentbeheer
- **Document-ID:** MOD-02-FL
- **Titel:** Module 02.F â€” Snelle Route (Fast Lane)
- **Versie:** 1.0
- **Status:** Definitief
- **Eigenaar:** AI Competence Center
- **Laatst herzien:** 2026-02-01
- **Wijziging t.o.v. vorige versie:** Nieuw; definieert criteria en minimumpakket voor laag risico experimenten.

---

## 1. Doel
De Fast Lane is bedoeld om **veilig en snel** waarde te testen voor **laagâ€‘risico** AIâ€‘toepassingen, zonder onnodige bureaucratieâ€”maar **met minimale governance**.

## 2. Toelatingscriteria (allemaal verplicht)
Een use case mag alleen Fast Lane als aan **alle** punten is voldaan:

1. **EU AI Act risiconiveau = Minimaal** (zie MODâ€‘07)  
2. **Samenwerkingsmodus = 1 of 2** (Instrumenteel of Adviserend; zie MODâ€‘00â€‘06)  
3. De AI **neemt geen beslissingen over mensen** (geen selectie/toekenning/afwijzing)  
4. Geen verwerking van **bijzondere persoonsgegevens** (gezondheid, religie, biometrie, etc.)  
5. Output wordt **altijd** door een mens bekeken vÃ³Ã³r gebruik (geen autonoom versturen/uitvoeren)  
6. Alleen intern gebruik Ã³f (indien extern) **100% transparantie** (â€œJe spreekt met AIâ€)

**Als Ã©Ã©n criterium niet gehaald wordt:**
â†’ *geen Fast Lane*, volg de standaard lifecycle (MODâ€‘02 t/m MODâ€‘06).

## 3. Minimumpakket deliverables (Fast Lane)
- **TMPâ€‘09â€‘01 Project Charter** (Fast Lane variant: kort)  
- **TMPâ€‘09â€‘03 Risico Preâ€‘Scan** (moet â€œMinimaalâ€ bevestigen)  
- **TMPâ€‘09â€‘02 Doelkaart** (incl. Rode Lijnen)  
- **TMPâ€‘09â€‘05 Test & Acceptatie Protocol** (light: minimaal 20 cases)  
- **TMPâ€‘09â€‘06 Validatierapport** (bewijs van testresultaten)

**Wat mag je overslaan in Fast Lane:**
- Uitgebreide business case (ROI) *mag later*, maar je noteert wÃ©l een â€œwaardeâ€‘hypotheseâ€ in het Charter.
- Uitgebreid technisch dossier (alleen relevant bij hoog risico).

## 4. Fast Lane Gates (simpel en toetsbaar)
### Gate FLâ€‘1 â€” Start experiment (max. 2 weken)
**Go** als:
- Risico Preâ€‘Scan = Minimaal
- Doelkaart bevat Rode Lijnen
- Minimaal testplan staat klaar (Gouden Set â‰¥ 20)

### Gate FLâ€‘2 â€” Interne live pilot (max. 4 weken)
**Go** als:
- Validatierapport (TMPâ€‘09â€‘06) voldoet aan **MODâ€‘01â€‘07** normen voor Minimaal risico
- Logging/traceerbaarheid is ingericht op basismetaâ€‘niveau
- Incidentprocedure bekend bij team

## 5. Wanneer Fast Lane stopt (escalatie)
Fast Lane stopt direct en je stapt over op standaard lifecycle als:
- Samenwerkingsmodus opschuift naar **3+**
- De tool extern gebruikt gaat worden met impact op klanten
- Het datagebruik uitbreidt naar (bijzondere) persoonsgegevens
- Er 1 Kritieke fout optreedt (Rode Lijnen geraakt)

---
Â© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
