---
versie: '1.0'
description: 'Het AI-levenscyclusmodel: zeven opeenvolgende fasen van Verkenning tot Afsluiting. Leer hoe elke fase doelstellingen, opleveringen en governance gates verbindt in een AI-project.'
type: strategic
layer: 1
---

# 1. AI-Projectcyclus

!!! abstract "Doel"
    Beschrijving van de volledige vijf-fasen AI-levenscyclus die als centrale routekaart dient voor elk AI-project.

## 1. Doel

Dit document definieert de volledige methodologie voor AI-projecten en vormt de fundering van de AI-projectcyclus. Het beschrijft de 5 fasen van AI-projecten en fungeert als centrale routekaart voor het team.

!!! info "Toepasbaarheid"
    Deze projectcyclus is van toepassing op **beide projecttypen**: zowel projecten die AI inzetten als onderdeel van het ontwikkelproces (Type A — bouwen met AI) als projecten waarbij AI-functionaliteit onderdeel is van het eindproduct (Type B — AI in het product). De fasering, gates en bewijsstandaarden zijn identiek; het verschil zit in de aard van de opleveringen per fase. Zie [Projecttype Classificatie](../02-fase-ontdekking/02-activiteiten.md) voor details.

______________________________________________________________________

## 2. Overzicht van de AI Levenscyclus

Een succesvol AI-project is geen lineair proces, maar een iteratieve cyclus waarbij techniek, business en compliance constant op elkaar worden afgestemd. De AI levenscyclus bestaat uit 5 fasen die elkaar overlappen en versterken:

```mermaid
graph TD
 A[Verkenning & Strategie] --> B[Validatie]
 B --> C[Realisatie]
 C --> D[Levering]
 D --> E[Beheer & Optimalisatie]
 E --> A
```

### Belangrijkste Kenmerken

- **Iteratief:** Elke fase leert van de vorige en voedt de volgende.
- **Hybride:** Combineert voorspelbare planning met agile uitvoering (zie [Hybride Methodologie](02-hybride-methodologie.md)).
- **Compliance-First:** EU AI Act compliance is geïntegreerd in elke fase.
- **Traceerbaarheid:** Elke beslissing wordt ondersteund door bewijs.
- **Mensgerichte Regie:** Mensen blijven verantwoordelijk voor AI-beslissingen.

______________________________________________________________________

## 3. De Vijf Fasen van de Levenscyclus

> \[!TIP\]
> **De Fast Lane (De Innovatie-route)**
> Voor projecten met een **Minimaal/Beperkt Risico** en een **Instrumentele/Adviserende modus** (Modus 1 & 2) bieden we een versnelde route. Hierbij kan na een positieve **Risico Pre-Scan** (Gate 1) direct worden gestart met een beperkte **Validatiepilot (PoV)**, zonder uitgebreide business case.

### Verkenning & Strategie

**📍 Doel:** Het identificeren van het juiste probleem en toetsen of we klaar zijn om te starten.

#### Kernactiviteiten

- **Probleemverkenning:** Het probleem definiëren vanuit de gebruiker, niet vanuit de techniek.
- **Data-Evaluatie:** Beoordelen van Toegang, Kwaliteit en Relevantie van de data.
- **Risico-Inventarisatie:** Bepalen of de toepassing valt onder de EU AI Act (hoog risico).

______________________________________________________________________

### Validatie

**📍 Doel:** Bewijzen dat het idee werkt en financieel levensvatbaar is voordat we groot investeren.

#### Kernactiviteiten

- **Validatiepilot (PoV):** Kleinschalig experiment om de hypothese te testen.
- **Het Kostenoverzicht:** Schatten van investering versus ROI.
- **Fairness audit (bias audit) (Bias Detectie):** Eerste scan op ongewenste vooroordelen in het model.

______________________________________________________________________

### Realisatie

**📍 Doel:** Het bouwen van een robuuste, productiewaardige oplossing.

#### Kernactiviteiten

- **Specificatie-eerst Methode:** Eerst tests schrijven, dan pas de implementatie.
- **RAG:** De AI verbinden aan interne bedrijfsinformatie.
- **Fine-tunen:** Optimaliseren van de parameters en **Prompts**.

______________________________________________________________________

### Levering

**📍 Doel:** Een veilige **Ingebruikname** en acceptatie door de organisatie.

#### Kernactiviteiten

- **Ingebruikname Plan:** Stapsgewijze uitrol naar productie.
- **Menselijke Regie:** Implementeren van toezichtsprotocollen.
- **Adoptie & Training:** Gebruikers opleiden in de nieuwe werkwijze.

______________________________________________________________________

### Beheer & Optimalisatie

**📍 Doel:** Waarde behouden en de oplossing actueel houden.

#### Kernactiviteiten

- **Drift Meten:** Continu monitoren van accuraatheid en drift.
- **Kostenbeheersing:** Het verbruik en de middelen optimaliseren.
- **Feedbacklus:** Gebruikerservaringen terugkoppelen naar Fase 1.

______________________________________________________________________

## 4. Gerelateerde Modules

- [Hybride Methodologie](02-hybride-methodologie.md)
- [Governance Model](03-governance-model.md)
- [Agile Antipatronen](04-agile-antipatronen-niet-toegestaan.md)
- [Project Initiatie](05-project-initiatie.md)

______________________________________________________________________
