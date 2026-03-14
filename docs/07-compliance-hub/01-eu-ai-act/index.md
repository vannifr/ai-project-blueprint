---
versie: '1.0'
description: 'EU AI Act compliance gids: risicoklassificatie, verplichtingen per AI-systeemcategorie en praktische stappen om jouw AI-project in lijn te brengen met de Europese AI-verordening.'
type: index
layer: 3
roles: [Guardian]
tags: [eu-ai-act]
---

# 1. EU AI Act

## 1. Doel

Dit document beschrijft de specifieke vereisten van de Europese AI Verordening (EU AI Act) en hoe deze worden toegepast binnen het project. De EU AI Act is de eerste uitgebreide AI-regelgeving ter wereld en is van toepassing op alle organisaties die AI-systemen aanbieden of gebruiken binnen de EU.

______________________________________________________________________

## 2. Risicoclassificatie conform EU AI Act

De EU AI Act deelt systemen in op basis van het risico dat ze vormen voor veiligheid en grondrechten.

### Onacceptabel Risico (Art. 5)

- **Definitie:** Systemen die een duidelijke bedreiging vormen voor fundamentele rechten.
- **Actie:** Absoluut verboden.

**Verboden toepassingen (Art. 5):**

| Categorie                     | Omschrijving                                                           |
| ----------------------------- | ---------------------------------------------------------------------- |
| Manipulatie                   | Subliminale technieken die gedrag beïnvloeden                          |
| Exploitatie kwetsbare groepen | Misbruik van leeftijd, handicap of sociale situatie                    |
| Social scoring                | Beoordeling van burgers door overheid op basis van gedrag              |
| Real-time biometrie           | Gezichtsherkenning in openbare ruimten (uitzonderingen voor opsporing) |
| Emotieherkenning              | Op werkplek of in onderwijs (beperkte uitzonderingen)                  |
| Biometrische categorisatie    | Op basis van gevoelige kenmerken (ras, religie, etc.)                  |

### Hoog Risico (Art. 6, Bijlage III)

- **Definitie:** Systemen in kritieke domeinen met significante impact op grondrechten.
- **Vereisten:** Strenge regels voor data-governance, documentatie, transparantie en menselijk toezicht.
- **Documentatie:** Verplicht technisch dossier en CE-markering.

### Transparantieverplichtingen (EU AI Act Art. 50)

- **Toepassing:** Transparantieverplichtingen gelden voor bepaalde AI-systemen, waaronder systemen die met personen interageren (bijvoorbeeld chatbots) en systemen die synthetische of gemanipuleerde content genereren of publiceren in contexten waar labeling/disclosure vereist is.
- **Vereisten:** Disclosure/labeling waar wettelijk vereist, inclusief (a) melden dat men met AI interageert (tenzij evident uit de context), en (b) markeren/labelen van kunstmatig gegenereerde of gemanipuleerde content waar van toepassing.

> **Verduidelijking:** "Beperkt risico" is een interne werkcategorie binnen deze blauwdruk. De EU AI Act werkt niet met een expliciet "beperkt risico"-niveau, maar met concrete verplichtingen per systeemtype (Art. 50).

Bronnen: \[so-27\], \[so-36\]

### Minimaal Risico

- **Definitie:** De meeste AI-systemen (spamfilters, AI in games).
- **Vereisten:** Geen wettelijke verplichtingen, maar vrijwillige gedragscodes aanbevolen.

______________________________________________________________________

## 3. Bijlage III: Hoog-Risico Gebieden

AI-systemen vallen onder Hoog Risico als ze worden ingezet in de volgende domeinen:

| Domein                          | Voorbeelden                                            | Playbook Mapping           |
| ------------------------------- | ------------------------------------------------------ | -------------------------- |
| **Biometrie (1)**               | Gezichtsherkenning, vingerafdrukanalyse                | Risicoclassificatie > Hoog |
| **Kritieke infrastructuur (2)** | Verkeer, water, gas, elektriciteit                     | Risicoclassificatie > Hoog |
| **Onderwijs (3)**               | Toelating, beoordeling, surveillantie                  | Risicoclassificatie > Hoog |
| **Werkgelegenheid (4)**         | Werving, CV-screening, prestatiebeoordeling            | Risicoclassificatie > Hoog |
| **Essentiële diensten (5)**     | Kredietwaardigheid, verzekering, sociale voorzieningen | Risicoclassificatie > Hoog |
| **Rechtshandhaving (6)**        | Risicobeoordeling, bewijsanalyse                       | Risicoclassificatie > Hoog |
| **Migratie & asiel (7)**        | Visumaanvragen, grensbewaking                          | Risicoclassificatie > Hoog |
| **Rechtspraak (8)**             | Onderzoek van feiten en recht                          | Risicoclassificatie > Hoog |

______________________________________________________________________

## 4. Artikelverwijzingen: Kernverplichtingen

### Art. 9: Risicobeheersysteem

**Vereiste:** Een continu risicobeheersysteem gedurende de volledige levenscyclus.

**Playbook Implementatie:**

- [Risico Pre-Scan](../../09-sjablonen/03-risicoanalyse/pre-scan.md) bij project start
- Periodieke risico-updates bij elke Gate
- Guardian review op Rode Lijnen
- Incidentproces voor nieuwe risico's

**Checklist:**

- [ ] Risico's zijn geïdentificeerd en gedocumenteerd
- [ ] Mitigatiemaatregelen zijn geïmplementeerd
- [ ] Residuele risico's zijn geaccepteerd door Guardian
- [ ] Risicoregister wordt periodiek herzien

### Art. 10: Data Governance

**Vereiste:** Gebruik van hoogwaardige datasets met passende maatregelen tegen bias.

**Playbook Implementatie:**

- [Data-Evaluatie](../../02-fase-ontdekking/02-activiteiten.md) in Fase 1
- [Data Pipelines](../../08-technische-standaarden/02-data-pipelines.md) standaarden
- [Fairness audit (bias audit)](../../07-compliance-hub/03-ethische-richtlijnen.md) voor bias-detectie

**Checklist:**

- [ ] Databronnen zijn gedocumenteerd
- [ ] Datakwaliteit is geëvalueerd
- [ ] Bias-analyse is uitgevoerd
- [ ] Representativiteit is gevalideerd

### Art. 11-12: Technische Documentatie

**Vereiste:** Uitgebreide technische documentatie die compliance aantoont.

**Playbook Implementatie:**

- [Technische Modelkaart](../../09-sjablonen/02-business-case/modelkaart.md)
- [Doelkaart (goal card)](../../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- [Validatierapport](../../09-sjablonen/07-validatie-bewijs/validatierapport.md)

**Vereiste Inhoud Technisch Dossier:**

| Element                 | Playbook Document                   |
| ----------------------- | ----------------------------------- |
| Systeembeschrijving     | Technische Modelkaart               |
| Ontwerp en ontwikkeling | Specificatie (SDD Patroon)          |
| Werking en beperkingen  | Doelkaart (goal card) + Rode Lijnen |
| Risicobeheersysteem     | Risico Pre-Scan + updates           |
| Wijzigingslogboek       | Git history + release notes         |
| Testresultaten          | Validatierapport + Golden Set       |

### Art. 13: Transparantie

**Vereiste:** Voldoende transparantie zodat gebruikers de output kunnen interpreteren.

**Playbook Implementatie:**

- Transparantieplicht in [Rode Lijnen](../../07-compliance-hub/index.md)
- AI-disclaimer in gebruikersinterface (Beperkt/Hoog Risico)
- Bronvermelding bij RAG (RAG)

**Checklist:**

- [ ] Gebruikers weten dat ze met AI communiceren
- [ ] Beperkingen zijn gecommuniceerd
- [ ] Bronnen worden getoond waar relevant

### Art. 14: Menselijk Toezicht

**Vereiste:** Maatregelen om effectief menselijk toezicht mogelijk te maken.

**Playbook Implementatie:**

- [AI-Samenwerkingsmodi](../../00-strategisch-kader/06-has-h-niveaus.md) bepalen toezichtsniveau
- Guardian rol met veto-recht
- Human-in-the-loop voor Modus 1-3
- Circuit Breaker voor Modus 4-5

**Toezicht per Samenwerkingsmodus:**

| Modus | Toezichtsvorm        | Implementatie                                |
| ----- | -------------------- | -------------------------------------------- |
| 1-2   | Human-in-the-loop    | Mens beslist altijd                          |
| 3     | Human-on-the-loop    | Mens monitort, grijpt in bij afwijking       |
| 4     | Human-over-the-loop  | Mens stelt kaders, AI voert uit              |
| 5     | Human-above-the-loop | Mens stelt beleid, AI autonoom binnen kaders |

### Art. 15: Nauwkeurigheid, Robuustheid & Cybersecurity

**Vereiste:** Passende niveaus van nauwkeurigheid, robuustheid en cybersecurity.

**Playbook Implementatie:**

- [Bewijsstandaarden](../../01-ai-native-fundamenten/07-bewijsstandaarden.md) voor nauwkeurigheidsnormen
- [Test Frameworks](../../08-technische-standaarden/04-test-frameworks.md) incl. adversarial testing
- [AI Architectuur](../../08-technische-standaarden/05-ai-architectuur.md) beveiligingslagen

**Checklist:**

- [ ] Nauwkeurigheid voldoet aan normen per risiconiveau
- [ ] Adversarial testing is uitgevoerd
- [ ] Beveiligingsmaatregelen zijn geïmplementeerd
- [ ] Robuustheid is getest (variatie, edge cases)

### GPAI (vanaf 2 augustus 2025) — implicaties voor vendorselectie

Wanneer uw organisatie een general-purpose AI (GPAI) of foundation model van een derde partij inzet, gelden specifieke overwegingen.

**Rolbepaling:**

- Bepaal of uw organisatie optreedt als **deployer** (toepassen van een bestaand model) of als **(deels) provider** (fine-tuning, eigen distributie, of substantiële aanpassing).
- Bij substantiële aanpassing of (her)distributie van een model kan de rol verschuiven richting provider; leg dit expliciet vast in het dossier.

**Contractuele eisen aan leveranciers:**

- [ ] Modeldocumentatie beschikbaar en actueel
- [ ] Update-notificaties bij modelwijzigingen
- [ ] Incident support en meldingsprocedures
- [ ] Contractuele waarborgen voor data-governance en beveiliging
- [ ] Capability om Art. 50 downstream te implementeren (disclosure/labeling) waar relevant

Bronnen: \[so-27\], \[so-36\]

______________________________________________________________________

## 5. Compliance Mapping: Playbook naar EU AI Act

| EU AI Act Artikel    | Vereiste                  | Playbook Module                              | Sjabloon              |
| -------------------- | ------------------------- | -------------------------------------------- | --------------------- |
| Art. 5               | Verboden praktijken       | Risico Pre-Scan                              | Deel A                |
| Art. 6 + Bijlage III | Hoog-risico classificatie | Compliance Hub                               | Risicoclassificatie   |
| Art. 9               | Risicobeheersysteem       | Risico Pre-Scan + Gates                      | Risicoanalyse         |
| Art. 10              | Data governance           | Data Pipelines + Fairness audit (bias audit) | Data & Privacyblad    |
| Art. 11-12           | Technische documentatie   | Technische standaarden                       | Modelkaart            |
| Art. 13              | Transparantie             | Rode Lijnen                                  | Doelkaart (goal card) |
| Art. 14              | Menselijk toezicht        | AI-Samenwerkingsmodi                         | Project Charter       |
| Art. 15              | Nauwkeurigheid & security | Bewijsstandaarden                            | Validatierapport      |
| Art. 50              | Transparantieplicht       | Rode Lijnen                                  | Doelkaart (goal card) |

______________________________________________________________________

## 6. Tijdlijn EU AI Act

De EU AI Act kent een gefaseerde inwerkingtreding. Onderstaande data zijn bindend.

- **1 augustus 2024** — Inwerkingtreding van de verordening.
- **2 februari 2025** — Verboden praktijken van kracht (Art. 5) + verplichting tot AI-geletterdheid voor betrokken personeel.
- **2 augustus 2025** — GPAI-regels van kracht (general-purpose AI / foundation models).
- **2 augustus 2026** — Meeste verplichtingen van kracht, inclusief Annex III hoog-risico systemen.
- **2 augustus 2027** — Verlengde overgangsperiode voor specifieke categorieën: hoog-risico AI in gereguleerde producten + reeds op de markt geplaatste GPAI-modellen (legacy).

Bronnen: \[so-27\], \[so-36\]

______________________________________________________________________

## 7. Checklist EU AI Act Compliance (Hoog Risico)

**Voorafgaand aan ontwikkeling:**

- [ ] Risicoclassificatie bepaald (niet Onacceptabel)
- [ ] Bijlage III categorisering gedocumenteerd
- [ ] Risicobeheersysteem ingericht

**Tijdens ontwikkeling:**

- [ ] Data governance maatregelen geïmplementeerd
- [ ] Technische documentatie bijgehouden
- [ ] Menselijk toezicht ingebouwd

**Voor livegang:**

- [ ] Validatierapport voldoet aan Art. 15 eisen
- [ ] Transparantie-eisen geïmplementeerd
- [ ] Conformiteitsbeoordeling afgerond (indien vereist)
- [ ] CE-markering (indien van toepassing)

**Na livegang:**

- [ ] Monitoring en logging actief
- [ ] Incidentmeldingsprocedure gereed
- [ ] Periodieke compliance review gepland

______________________________________________________________________

## 8. Aanvullende Wetgeving & Belgische Context

### Intrekking AI Liability Directive (AILD)

In februari 2025 kondigde de Europese Commissie de intrekking aan van het voorstel voor de AI Liability Directive, officieel gepubliceerd in oktober 2025. De AILD was bedoeld om via een "weerlegbaar vermoeden van causaliteit" de bewijslast voor slachtoffers van AI-schade te verlichten.

**Gevolg voor Belgische organisaties:** er is momenteel geen geharmoniseerde EU-richtlijn voor AI-aansprakelijkheid. Aansprakelijkheid valt terug op:

- Het **algemeen Belgisch aansprakelijkheidsrecht** (art. 1382 BW)
- De herziene **Product Liability Directive (PLD)** — zie hieronder

Bron: \[so-40\]

______________________________________________________________________

### Herziene Product Liability Directive (PLD)

De herziene PLD (Richtlijn (EU) 2024/2853) trad in werking op **8 december 2024** en omvat nu expliciet software en AI-systemen als producten. België moet deze omzetten in nationaal recht uiterlijk **9 december 2026**.

**Kernpunten voor AI-projecten:**

- AI-software valt onder de definitie van "product" → productaansprakelijkheid geldt
- Schade door defecte AI-systemen kan worden verhaald op de fabrikant/aanbieder
- Documentatieplichten uit de EU AI Act ondersteunen de PLD-verdediging

Bron: \[so-41\]

______________________________________________________________________

### Toepassingsbereik per regelgeving (België)

| Regelgeving            | Van toepassing?                              | Deadline               |
| :--------------------- | :------------------------------------------- | :--------------------- |
| EU AI Act              | ✅ Ja — direct van kracht als EU-verordening | Gefaseerd t/m aug 2027 |
| GDPR / AVG             | ✅ Ja — aanvullend van kracht                | Doorlopend             |
| PLD (herzien)          | ✅ Ja — na omzetting in Belgisch recht       | Dec 2026               |
| AI Liability Directive | ❌ Ingetrokken — niet van kracht             | N.v.t.                 |
| Colorado AI Act (VS)   | ❌ Niet van toepassing op Belgische markt    | N.v.t.                 |

!!! warning "Juridische fragmentatie"
    Door het wegvallen van de AILD navigeren organisaties nu door een lappendeken van nationale wetgevingen. Documenteer uw AI-systemen grondig via de EU AI Act-verplichtingen: dit vormt ook uw PLD-verdediging.

Bronnen: \[so-40\], \[so-41\]

______________________________________________________________________

## 9. Gerelateerde Modules

- [Risicobeheersing & Compliance](../index.md)
- [Risico Pre-Scan](../../09-sjablonen/03-risicoanalyse/pre-scan.md)
- [Bewijsstandaarden](../../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Ethische Richtlijnen](../03-ethische-richtlijnen.md)
