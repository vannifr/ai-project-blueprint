---
versie: '1.1'
type: reference
layer: 3
tags: [validation]
answers: ['Wat is Externe Evidence: DORA (DevOps Research & Assessment)?']
---

# 1. Externe Evidence: DORA (DevOps Research & Assessment)

## 1. Doel

Dit document vat de belangrijkste bevindingen samen uit het DORA-onderzoeksprogramma (DevOps Research and Assessment) met betrekking tot AI-ondersteunde softwareontwikkeling, inclusief het DORA AI Capabilities Model (2025).

## 2. Kernbevindingen

### Gemengde effecten op delivery performance

AI-ondersteunde ontwikkeling leidt niet automatisch tot betere delivery outcomes. De effecten zijn sterk afhankelijk van de context, het type werk en de mate van begeleiding. Teams dienen realistische verwachtingen te hanteren en niet te vertrouwen op AI als wondermiddel voor productiviteit.

### Lokale proceswinst vertaalt zich niet altijd naar delivery

Individuele productiviteitswinst (sneller code schrijven, sneller documentatie genereren) leidt niet vanzelfsprekend tot verbeterde teamleveringen. De bottleneck verschuift vaak naar andere delen van het proces, zoals code review, integratie of validatie.

### Small batches en frequente tests blijven essentieel

De fundamentele DevOps-principes blijven onverminderd van kracht bij AI-ondersteunde ontwikkeling. Kleine batches, frequente integratie en geautomatiseerde tests zijn nog belangrijker wanneer AI-gegenereerde code wordt geïntroduceerd, omdat de herkomst en kwaliteit van die code extra validatie vereist.

### Vertrouwen ontstaat via feedback loops en policies

Teams bouwen vertrouwen in AI-tools op door transparante feedback loops en duidelijke beleidsrichtlijnen. Zonder expliciete afspraken over wanneer en hoe AI mag worden ingezet, ontstaat onduidelijkheid die het teamvertrouwen ondermijnt.

### Adoptie vereist transparantie, leertijd en policies

Succesvolle adoptie van AI-tools vraagt om openheid over het gebruik ervan, voldoende tijd om te leren werken met de tools, en heldere beleidsrichtlijnen die aangeven wat wel en niet is toegestaan binnen de teamcontext.

______________________________________________________________________

## 3. DORA AI Capabilities Model (2025)

!!! quote "Kerninzicht"
    "AI is een versterker — het vergroot de sterktes van goed presterende organisaties en de disfuncties van worstelde organisaties."

Uit onderzoek onder bijna 5.000 technologieprofessionals identificeert DORA zeven fundamentele capabilities die het positieve effect van AI-adoptie op prestaties versterken. Zonder deze capabilities levert AI-adoptie beperkte of zelfs negatieve resultaten.

### Capability 1: Helder en gecommuniceerd AI-beleid

Een duidelijk organisatiebeleid over AI-tools en -gebruik biedt psychologische veiligheid voor experimentatie. Zonder beleid durven teams niet te experimenteren of doen ze het ongecontroleerd.

**Versterkt:** individuele effectiviteit, organisatieprestaties, doorvoersnelheid. Vermindert wrijving.

### Capability 2: Gezond data-ecosysteem

Hoogwaardige, toegankelijke en geïntegreerde interne data. Organisaties met gefragmenteerde of slechte datakwaliteit halen minder uit AI-tools.

**Versterkt:** organisatieprestaties.

### Capability 3: AI-toegankelijke interne data

Verbind AI-tools met interne codebases, documentatie en wiki's via *context engineering* (niet alleen prompt engineering). Hoe beter de AI de organisatiecontext begrijpt, hoe relevanter de output.

**Versterkt:** individuele effectiviteit, codekwaliteit.

### Capability 4: Sterke versiebeheer-praktijken

AI verhoogt de snelheid van verandering; versiebeheer is het vangnet. Frequente rollbacks versterken teamprestaties. Teams die goed zijn in versiebeheer profiteren meer van AI.

**Versterkt:** individuele effectiviteit, teamprestaties.

### Capability 5: Werken in kleine batches

Compenseert het risico dat AI grote, instabiele wijzigingen genereert. Kleine batches houden wijzigingen verifieerbaar en beheersbaar.

**Versterkt:** productprestaties. Vermindert wrijving.

### Capability 6: Gebruikersgerichte focus

Zorgt ervoor dat AI-versnelde teams snel de *juiste* richting bewegen. Zonder gebruikersgerichtheid kan AI de teamprestaties juist schaden.

**Versterkt:** teamprestaties, productprestaties, organisatieprestaties.

### Capability 7: Kwalitatieve interne platformen

Geautomatiseerde, veilige paden die AI-voordelen schaalbaar maken. Interne platformen fungeren als de "snelweg" waarover AI-gegenereerde output veilig naar productie stroomt.

**Versterkt:** organisatieprestaties.

### Mapping naar het Blueprint

| DORA Capability                 | Blueprint Module                                                                                                        |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| Helder AI-beleid                | [Governance Model](../00-strategisch-kader/03-governance-model.md)                                                      |
| Gezond data-ecosysteem          | [Data Governance](../08-technische-standaarden/10-data-governance.md)                                                   |
| AI-toegankelijke interne data   | [Context Files Pattern](../04-fase-ontwikkeling/06-engineering-patterns.md#pattern-4-machine-leesbare-contextbestanden) |
| Sterke versiebeheer-praktijken  | [Technische Standaarden](../08-technische-standaarden/01-mloops-standaarden.md)                                         |
| Werken in kleine batches        | [Engineering Patterns — Rework Beperken](../04-fase-ontwikkeling/06-engineering-patterns.md#4-rework-beperken)          |
| Gebruikersgerichte focus        | [Fase Ontdekking — Doelstellingen](../02-fase-ontdekking/01-doelstellingen.md)                                          |
| Kwalitatieve interne platformen | [MLOps Standaarden](../08-technische-standaarden/01-mloops-standaarden.md)                                              |

______________________________________________________________________

Bron: \[so-28\] — <https://dora.dev/ai/>
