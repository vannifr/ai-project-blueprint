---
versie: '1.1'
type: playbook
layer: 3
roles: [Guardian]
tags: [eu-ai-act, playbook, security]
summary: 'Vier gedetailleerde stappenplannen voor de meest voorkomende AI-incidenten: prestatieverloop, bias, beveiligingsincidenten en datakwaliteit.'
answers: [Hoe voer ik Incident Playbooks uit?]
---

# Incident Playbooks

!!! abstract "Doel"
    Vier gedetailleerde stappenplannen voor de meest voorkomende AI-incidenten: prestatieverloop, bias, beveiligingsincidenten en datakwaliteit.

Vier gedetailleerde stappenplannen voor de meest voorkomende AI-incidenten. Gebruik deze naast de [Incident Respons overzichtspagina](05-incidentrespons.md) voor de ernst-matrix en rollen.

______________________________________________________________________

## Playbook 1 — Prestatieverloop

**Wanneer activeren:** kwaliteitsscores dalen structureel, gebruikersklachten nemen toe, monitoring-alerts op outputkwaliteit.

### Stap 1 — Detectie & Validatie (0–30 min)

- [ ] Controleer monitoring-dashboard op trend (niet eenmalige piek)
- [ ] Vergelijk huidige scores met baseline (Golden Set of productie-sample)
- [ ] Classificeer ernst: 🟡 Geel (score ≥ 80% baseline) / 🟠 Oranje (60–80%) / 🔴 Rood (\< 60%)
- [ ] Noteer tijdstip eerste afwijking

### Stap 2 — Containment (indamming) (30–60 min)

- [ ] Notificeer Tech Lead + AI PM
- [ ] Notificeer Guardian bij 🟠 Oranje of hoger
- [ ] Overweeg rollback naar vorige modelversie indien beschikbaar
- [ ] Verhoog monitoringfrequentie tijdelijk

### Stap 3 — Onderzoek (1–24 uur)

- [ ] Bepaal type drift: **data-drift** (input veranderd) of **concept-drift** (wereld veranderd)
- [ ] Identificeer wanneer drift begon (git log, model registry, data pipeline logs)
- [ ] Kwantificeer impact: hoeveel outputs zijn mogelijk incorrect?
- [ ] Inventariseer compliance-implicaties (Hoog Risico systemen: meldingsplicht nagaan)

### Stap 4 — Herstel (24–72 uur)

- [ ] Kies herstelstrategie: hertraining / promptaanpassing / kennisbank-update
- [ ] Test herstelstrategie op Golden Set (minimale drempel: baseline + 5%)
- [ ] Laat Guardian valideren bij systemen met menselijke impact
- [ ] Deploy fix met verhoogde monitoring (eerste 48 uur)

### Stap 5 — Post-Incident

- [ ] Root cause gedocumenteerd
- [ ] Monitoringdrempels bijgesteld
- [ ] Baseline geüpdatet indien concept-drift structureel is
- [ ] Lessons Learned ingevuld

______________________________________________________________________

## Playbook 2 — Beveiligingsincident

**Wanneer activeren:** ongeautoriseerde toegang, datalekkage, abnormaal gebruik, verdachte API-patronen.

### Stap 1 — Detectie & Eerste Actie (0–15 min)

- [ ] Classificeer type: **toegangsschending** / **datalekkage** / **misbruik van systeem**
- [ ] Activeer [Circuit Breaker](05-incidentrespons.md) indien actieve dreiging
- [ ] Notificeer onmiddellijk: Security/CISO, Guardian, Legal
- [ ] Preserveer bewijs: exporteer logs, maak screenshots, noteer tijdlijn

!!! danger "Vernietig geen logs"
    Logs zijn bewijsmateriaal. Verwijder of overschrijf niets totdat Legal akkoord geeft.

### Stap 2 — Containment (indamming) (15 min–1 uur)

- [ ] Revoceer gecompromitteerde credentials/tokens
- [ ] Blokkeer verdachte IP-adressen of accounts
- [ ] Isoleer getroffen systemen van productieomgeving indien mogelijk
- [ ] Stel vast of aanvaller nog actief is

### Stap 3 — Impact-assessment (1–24 uur)

- [ ] Welke data is accessed of geëxfiltreerd?
- [ ] Hoeveel gebruikers/betrokkenen zijn geraakt?
- [ ] Zijn er persoonsgegevens betrokken? → GDPR-meldingsplicht binnen 72 uur
- [ ] Zijn er EU AI Act-implicaties (Hoog Risico systeem)? → Markttoezichthouder

### Stap 4 — Herstel (24–168 uur)

- [ ] Patch kwetsbaarheid of pas toegangscontroles aan
- [ ] Roep penetratietest in voor getroffen component
- [ ] Herstel dienstverlening gradueel met verhoogde monitoring
- [ ] Notificeer betrokkenen indien wettelijk vereist (GDPR Art. 34)

### Stap 5 — Post-Incident

- [ ] Forensische analyse afgerond
- [ ] Security-maatregelen bijgewerkt
- [ ] Team getraind op nieuwe procedure
- [ ] Responsible Disclosure overwogen indien externe onderzoeker

______________________________________________________________________

## Playbook 3 — Bias-detectie

**Wanneer activeren:** klachten over ongelijke behandeling, fairness-metrics buiten bandbreedte, audit-bevinding, mediarapportage.

### Stap 1 — Validatie (0–4 uur)

- [ ] Analyseer gemelde outputs op het betrokken kenmerk (geslacht, leeftijd, etniciteit, etc.)
- [ ] Vergelijk outputkwaliteit/beslissingen over relevante groepen
- [ ] Kwantificeer dispariteit (bijv. verschil in acceptatiegraad, kwaliteitsscore per groep)
- [ ] Classificeer ernst en notificeer Guardian (verplicht bij bias-incidenten)

### Stap 2 — Impact-assessment (4–24 uur)

- [ ] Hoelang bestaat de bias vermoedelijk al?
- [ ] Hoeveel beslissingen/outputs zijn potentieel beïnvloed?
- [ ] Welke groepen zijn benadeeld?
- [ ] Zijn er juridische consequenties (discriminatiewetgeving, EU AI Act)?

### Stap 3 — Root Cause (24–48 uur)

Bepaal de bron:

| Bron                   | Indicatie                                    | Aanpak                              |
| :--------------------- | :------------------------------------------- | :---------------------------------- |
| **Data-bias**          | Trainingsdata oververtegenwoordigt een groep | Herbalanceren dataset + hertraining |
| **Model-bias**         | Model versterkt bias onafhankelijk van data  | Fine-tuning of modelwissel          |
| **Prompt-bias**        | Instructies leiden tot ongelijke behandeling | Promptherziening + testen           |
| **Ingebruikname-bias** | Systeem anders ingezet dan gevalideerd       | Scope aanpassen                     |

### Stap 4 — Mitigatie & Herstel (48–168 uur)

- [ ] Implementeer mitigatiestrategie op basis van root cause
- [ ] Valideer met fairness-metrics (gelijkheid van kansen, demografische pariteit)
- [ ] Hervalidatie vereist Guardian-goedkeuring vóór herstart
- [ ] Overweeg herziening van eerdere betrokken beslissingen

### Stap 5 — Post-Incident

- [ ] Model Card bijgewerkt met bias-bevindingen
- [ ] Fairness-monitoring uitgebreid
- [ ] Fairness Audit protocol herzien
- [ ] Communicatie naar betrokkenen indien van toepassing

______________________________________________________________________

## Playbook 4 — Systeemuitval

**Wanneer activeren:** systeem onbereikbaar, time-outs op schaal, hoge foutpercentages, productiepijplijn geblokkeerd.

### Stap 1 — Detectie & Eerste Actie (0–15 min)

- [ ] Bepaal scope: **partieel** (component down) of **volledig** (systeem onbeschikbaar)
- [ ] Activeer fallback-modus indien geconfigureerd (menselijke overdracht of tijdelijk offline)
- [ ] Notificeer Tech Lead (incident commander) + AI PM (communicatie)
- [ ] Communiceer naar gebruikers: status-update binnen 15 minuten

### Stap 2 — Diagnose (15 min–2 uur)

Doorloop in volgorde:

1. **Infrastructuur** — cloud provider status, servers, netwerk
1. **Afhankelijkheden** — externe API's (LLM provider, databases)
1. **Applicatie** — logs, memory/CPU, foutcodes
1. **Recent gewijzigd** — laatste livegang, config-wijziging, data-update

### Stap 3 — Herstel (2–8 uur)

- [ ] Ontwikkel fix op basis van diagnose
- [ ] Test in staging-omgeving vóór productie
- [ ] Documenteer rollback-plan vóór livegang
- [ ] Deploy fix met graduele uitrol (canary of blue-green indien mogelijk)

### Stap 4 — Validatie & Herstart

- [ ] Verificeer alle functies operationeel
- [ ] Verwijder fallback-modus
- [ ] Monitor nauwlettend eerste 2 uur na herstart
- [ ] Update statuspage / communiceer oplossing

### Stap 5 — Post-Incident

- [ ] Tijdlijn gedocumenteerd (detectie → herstel)
- [ ] Root cause vastgesteld
- [ ] Monitoring verbeterd om sneller te detecteren
- [ ] Runbook bijgewerkt

______________________________________________________________________

## Communicatietemplates

### Eerste Alert (intern)

```
INCIDENT ALERT — [Niveau: Rood/Oranje/Geel]
Systeem: [naam]
Type: [Drift / Security / Bias / Uitval]
Tijdstip detectie: [datum + tijd]
Initiële impact: [beschrijving]
Incident commander: [naam]
Volgende update: [tijdstip]
```

### Gebruikerscommunicatie (bij uitval)

```
We zijn op de hoogte van een verstoring in [systeem].
Ons team onderzoekt de oorzaak. Verwachte hersteltijd: [tijdstip].
Tijdelijke oplossing: [beschrijving fallback indien van toepassing].
Updates volgen elk uur via [kanaal].
```

______________________________________________________________________

## Gerelateerde Modules

- [Incident Respons Overzicht](05-incidentrespons.md)
- [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)
- [AI Safety Checklist](08-ai-safety-checklist.md)
- [Risicobeheer](02-risicobeheer/index.md)
- [Agentic AI Engineering — Faalpatronen](../08-technische-standaarden/09-agentic-ai-engineering.md)
- [Valkuilencatalogus](../17-bijlagen/valkuilen-catalogus.md)
