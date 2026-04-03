---
versie: '1.1'
type: compliance
layer: 3
roles: [Guardian]
tags: [eu-ai-act, security]
summary: Ernst-matrix, rollen en directe acties voor snel en gecoördineerd reageren op AI-incidenten.
answers: [Wat zijn de compliance-eisen voor Incident Respons?, Welke rollen heb ik nodig?]
sources:
  - id: eu-ai-act
    ref: Verordening (EU) 2024/1689 — EU AI Act (Art. 73, 74, 75)
    url: https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32024R1689
    date_verified: '2025-03-20'
    next_review: '2026-01-01'
    notes: Meldplicht voor ernstige incidenten via AI-autoriteitsmeldportaal (van kracht per aug 2025).
---

# Incident Respons

!!! abstract "Doel"
    Ernst-matrix, rollen en directe acties voor snel en gecoördineerd reageren op AI-incidenten.

Snel en gecoördineerd reageren op AI-incidenten. Deze pagina definieert de ernst-matrix, rollen en directe acties. Gedetailleerde procedures staan in de [Incident Playbooks](06-incidentrespons-playbooks.md).

______________________________________________________________________

## 1. Ernst-Matrix

| Niveau        | Criteria                                                                              | Reactietijd | Escalatie                  | Communicatie                    |
| :------------ | :------------------------------------------------------------------------------------ | :---------- | :------------------------- | :------------------------------ |
| 🔴 **Rood**   | Kritieke veiligheids- of compliance-schending; mogelijke wettelijke aansprakelijkheid | 15 min      | CAIO, Legal, Guardian      | Directe stakeholder-notificatie |
| 🟠 **Oranje** | Significante functionele storing; betrokkenen beïnvloed; reputatierisico              | 1 uur       | Tech Lead, AI PM, Guardian | Binnen 4 uur                    |
| 🟡 **Geel**   | Beperkte degradatie; geen directe schade; gebruikerservaring verminderd               | 4 uur       | Tech Lead, AI PM           | Binnen 24 uur                   |
| 🟢 **Groen**  | Minimale afwijking; geen directe impact; monitoring vereist                           | 24 uur      | Tech Lead                  | Volgende statusupdate           |

______________________________________________________________________

## 2. Incidenttypes & Playbooks

Vier incidenttypes hebben elk een eigen stappenplan in de [Incident Playbooks](06-incidentrespons-playbooks.md):

| Type                     | Signalen                                                                 | Typisch niveau |
| :----------------------- | :----------------------------------------------------------------------- | :------------- |
| **Prestatieverloop**     | Dalende kwaliteitsscores, gebruikersklachten, anomalieën in monitoring   | 🟡–🟠          |
| **Beveiligingsincident** | Ongeautoriseerde toegang, datalekkage, abnormaal gebruik                 | 🟠–🔴          |
| **Bias-detectie**        | Klachten over ongelijke behandeling, fairness-metrics buiten bandbreedte | 🟠–🔴          |
| **Systeemuitval**        | Onbeschikbaarheid, time-outs, foutmeldingen op schaal                    | 🟡–🔴          |

______________________________________________________________________

## 3. Circuit Breaker

De Circuit Breaker is de noodstop voor AI-systemen in Samenwerkingsmodus 4 en 5.

**Activeer de Circuit Breaker wanneer:**

- [ ] Het systeem handelt buiten gedefinieerde Harde Grenzen
- [ ] Een beveiligingsincident actief is of vermoed wordt
- [ ] Bias of discriminerende output is vastgesteld
- [ ] Het systeem onherstelbare acties dreigt uit te voeren

**Circuit Breaker procedure:**

1. **Isoleer** — schakel het systeem naar read-only of schakel inferentie uit
1. **Notificeer** — stuur onmiddellijk alert naar Guardian + Tech Lead
1. **Documenteer** — noteer tijdstip, trigger, systeem-state en betrokken outputs
1. **Herbeoordeel** — geen herstart zonder expliciete goedkeuring Guardian

______________________________________________________________________

## 4. Rollen bij Incidenten

| Rol           | Verantwoordelijkheid                                          |
| :------------ | :------------------------------------------------------------ |
| **Tech Lead** | Technische diagnose, containment, herstel                     |
| **AI PM**     | Coördinatie, stakeholder-communicatie, tijdlijn               |
| **Guardian**  | Ethische beoordeling, besluit over herstart, compliance-check |
| **CAIO / MT** | Escalatie bij Rood-niveau, externe communicatie               |
| **Legal**     | Meldingsplicht toetsen (GDPR, EU AI Act Art. 73)              |

______________________________________________________________________

## 5. Meldingsplicht

Bij incidenten die mensen benadelen of waarbij persoonsgegevens betrokken zijn:

- **GDPR-datalek:** melding bij Autoriteit Persoonsgegevens binnen **72 uur**
- **EU AI Act (Hoog Risico):** melding bij markttoezichthouder zodra incident vastgesteld
- **Intern:** melding aan Compliance/Legal binnen **24 uur** na detectie

______________________________________________________________________

## 6. Post-Incident

Na elk 🟠 Oranje of 🔴 Rood incident:

- [ ] Root cause analysis uitgevoerd
- [ ] Lessons Learned gedocumenteerd (zie [Lessons Learned sjabloon](../11-project-afsluiting/01-lessons-learned.md))
- [ ] Risico-inventarisatie bijgewerkt
- [ ] Blueprint/monitoring aangepast om herhaling te voorkomen
- [ ] Incident geregistreerd in het projectlogboek

______________________________________________________________________

## 7. Gerelateerde Modules

- [Incident Playbooks (4 gedetailleerde procedures)](06-incidentrespons-playbooks.md)
- [Red Teaming Playbook](07-red-teaming.md)
- [AI Safety Checklist](08-ai-safety-checklist.md)
- [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)
- [Risicobeheer](02-risicobeheer/index.md)
