---
versie: '1.0'
type: template
layer: 3
phase: [1, 2]
roles: [Guardian]
tags: [risk, template]
answers: [Hoe gebruik ik het Risico Pre-Scan (Gate 1 Checklist) sjabloon?]
---

# 1. Risico Pre-Scan (Gate 1 Checklist)

## 1. Doel

Dit sjabloon dient voor de initiële risico-inventarisatie in **Verkenning & Strategie** (Fase 1). Het helpt bij het vroegtijdig identificeren van blokkades op het gebied van wetgeving (EU AI Act), privacy en ethiek.

______________________________________________________________________

**Project:** \[Naam Project\]
**Ingevuld door:** \[Naam\]

______________________________________________________________________

### Deel A: EU AI Act Classificatie

*Kruis aan wat van toepassing is. Als één van deze 'Ja' is, bepaalt dat de risicocategorie.*

!!! check "Verboden Praktijken (ONACCEPTABEL)"

- [ ] Gebruikt het systeem subliminale technieken om gedrag te manipuleren?
- [ ] Wordt er gebruik gemaakt van biometrische categorisering (ras, politiek, religie)?
- [ ] Wordt er in openbare ruimtes real-time biometrische identificatie toegepast?

**Indien JA op één van bovenstaande: STOP PROJECT DIRECT.**

!!! check "Hoog Risico Systemen (HOOG RISICO)"

- [ ] Wordt het gebruikt in kritieke infrastructuur (water, energie, verkeer)?
- [ ] Beslist het over toegang tot onderwijs of beoordeling van studenten?
- [ ] Beslist het over werving, selectie of promotie van werknemers?
- [ ] Beslist het over toegang tot diensten (krediet, uitkeringen, verzekeringen)?

**Indien JA: Volledige compliance verplicht (Technisch Dossier, CE-markering).**

!!! check "Transparantieverplichtingen (Art. 50)"

- [ ] Is er directe interactie met mensen (chatbot, virtuele assistent)?
- [ ] Genereert het systeem synthetische of gemanipuleerde content (tekst, beeld, geluid)?

**Indien JA: Transparantieplicht (Gebruiker moet weten dat het AI is, content moet gelabeld worden waar vereist).**

______________________________________________________________________

### Deel A.2: GPAI & Rolbepaling

!!! check "Rolbepaling & Verplichtingen"

- [ ] Gebruiken wij een GPAI/foundation model van een derde partij?
- [ ] Zijn wij deployer of (deels) provider (bijvoorbeeld door fine-tuning of eigen distributie)?
- [ ] Valt dit systeem onder Art. 50 transparantieverplichtingen (chatbot, synthetische content, of content met manipulatief potentieel)?
- [ ] Is er een AI-geletterdheidsplan voor betrokken rollen (verplicht vanaf 2 februari 2025)?

**Indien één of meer vragen met "Ja" worden beantwoord:**
Raadpleeg de uitgebreide guidance in [EU AI Act Compliance](../../07-compliance-hub/01-eu-ai-act/index.md).

______________________________________________________________________

### Deel B: Privacy & Data (AVG)

- **Worden er persoonsgegevens verwerkt?** \[Ja/Nee\]
- **Is er een wettelijke grondslag voor dit gebruik?** \[Ja/Nee\]
- **Wordt data gedeeld met externe partijen (bijv. OpenAI, Azure)?** \[Ja/Nee\]

#### B.4 DPIA-triggers (indien één "Ja": DPIA starten of DPO raadplegen)

!!! check "DPIA Triggers"

- [ ] Grootschalige verwerking van persoonsgegevens
- [ ] Systematische monitoring van gedrag (bijv. profiling)
- [ ] Gebruik van bijzondere persoonsgegevens
- [ ] Geautomatiseerde beoordeling met significante impact op personen
- [ ] Nieuwe technologie + hoge risico context (twijfel = DPO betrekken)

______________________________________________________________________

### Deel C: Ethische Quickscan

- **Kan het systeem groepen discrimineren of uitsluiten (Bias)?** \[Ja/Nee\]
- **Is de werking uitlegbaar aan een leek?** \[Ja/Nee\]
- **Is er een menselijke 'noodstop' of override mogelijk?** \[Ja/Nee\]

______________________________________________________________________

### Conclusie & Advies Guardian

- **Definitief Risiconiveau:** \[Laag / Beperkt / Hoog / Verboden\]
- **Actievereisten:** \[Bijv. "DPIA uitvoeren", "Validatierapport opstellen", "Disclaimer toevoegen"\]
