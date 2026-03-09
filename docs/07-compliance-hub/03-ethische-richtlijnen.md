---
versie: '1.0'
---

# 1. Ethische Richtlijnen

## 1. Doel

Waarborgen dat AI-systemen worden ontwikkeld en gebruikt op een manier die de menselijke waarden respecteert en geen onbedoelde schade toebrengt.

______________________________________________________________________

## 2. Ethische Grondbeginselen

### Menselijke Regie en Toezicht

AI mag de menselijke autonomie niet ondermijnen. Gebruikers moeten in staat zijn om de werking van het systeem te begrijpen en, indien nodig, in te grijpen (**Menselijke Regie**).

### Rechtvaardigheid & Eerlijkheid

AI-systemen mogen niet leiden tot onrechtvaardige discriminatie. We passen de **Fairness audit (bias audit)** toe om bias op drie niveaus (Representativiteit, Stereotypering, Gelijke Behandeling) te elimineren.

### Transparantie & Uitlegbaarheid

Het moet voor een gebruiker duidelijk zijn wanneer hij met een AI communiceert. Beslissingen van het systeem moeten op een begrijpelijke manier kunnen worden uitgelegd.

### Privacy & Gegevensbescherming

Strikte naleving van de AVG/GDPR. Gegevens worden alleen gebruikt voor het beoogde doel en conform de gestelde **Rode Lijnen**.

Bron: \[so-49\]

### Maatschappelijk & Ecologisch Welzijn

We streven naar een positieve impact op de samenleving en minimaliseren de ecologische voetafdruk van onze AI-systemen (energie-efficiëntie).

______________________________________________________________________

## 3. De Fairness audit (bias audit) (Bias Audit) - Uitgebreid

### Toetsniveaus

We toetsen elk Hoog en Beperkt risico systeem op drie niveaus:

| Niveau                  | Vraag                                                          | Voorbeeld                                                           |
| ----------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Representativiteit**  | Is de data een goede afspiegeling van de werkelijkheid?        | Zijn alle klantsegmenten vertegenwoordigd in trainingsdata?         |
| **Stereotypering**      | Bevestigt de AI schadelijke clichés?                           | Associeert het systeem bepaalde beroepen met specifieke geslachten? |
| **Gelijke Behandeling** | Krijgt elke gebruikersgroep dezelfde kwaliteit van antwoorden? | Is de foutmarge gelijk voor verschillende leeftijdsgroepen?         |

### Meetbare Fairness Criteria

Wij hanteren de volgende meetbare criteria voor eerlijkheid:

| Criterium               | Definitie                                                       | Formule                           | Wanneer Toepassen                                                    |
| ----------------------- | --------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------- |
| **Demographic Parity**  | Kans op positieve uitkomst is gelijk voor alle groepen          | P(Y=1\|A=0) ≈ P(Y=1\|A=1)         | Selectie/toewijzing zonder legitimerend verschil                     |
| **Equalized Odds**      | True Positive Rate en False Positive Rate zijn gelijk per groep | TPR en FPR gelijk voor A=0 en A=1 | Beslissingen waar zowel positieve als negatieve fouten impact hebben |
| **Predictive Parity**   | Precision (positief voorspellende waarde) is gelijk per groep   | Precision gelijk voor A=0 en A=1  | Wanneer vertrouwen in positieve voorspellingen cruciaal is           |
| **Individual Fairness** | Vergelijkbare individuen krijgen vergelijkbare behandeling      | d(f(x), f(x')) ≤ d(x, x')         | Gepersonaliseerde dienstverlening                                    |

### Drempelwaarden per Risiconiveau

| Risiconiveau | Maximaal Verschil Tussen Groepen       | Aanvullende Eisen                                    |
| ------------ | -------------------------------------- | ---------------------------------------------------- |
| **Minimaal** | Kwalitatieve beoordeling door Guardian | Geen kwantitatieve eis                               |
| **Beperkt**  | ≤ 10% verschil in Major-foutpercentage | Documentatie van groepsvergelijking                  |
| **Hoog**     | ≤ 5% verschil in Major-foutpercentage  | Kwantitatieve analyse + gedocumenteerd mitigatieplan |

### Uitvoering van de Fairness audit (bias audit)

**Stap 1: Identificeer Relevante Groepen**

- Welke beschermde kenmerken zijn relevant? (geslacht, leeftijd, etniciteit, etc.)
- Let op: sommige kenmerken zijn proxy's voor beschermde kenmerken (postcode, naam)
- Documenteer keuzes in Risico Pre-Scan

**Stap 2: Verzamel of Annoteer Data**

- Optie A: Groepslabels beschikbaar in testdata
- Optie B: Handmatige annotatie van Golden Set subset
- Optie C: Proxy-variabelen met onderbouwing
- Let op privacy: pseudonimiseer waar mogelijk

**Stap 3: Meet Prestaties per Groep**

| Metric        | Groep A     | Groep B     | Verschil | Status     |
| ------------- | ----------- | ----------- | -------- | ---------- |
| Feitelijkheid | 98.5%       | 97.2%       | 1.3%     | OK         |
| Major fouten  | 2/75 (2.7%) | 4/75 (5.3%) | 2.6%     | OK (\< 5%) |
| Relevantie    | 4.3         | 4.1         | 0.2      | OK         |

**Stap 4: Analyseer en Mitigeer**

Bij overschrijding van drempels:

| Oorzaak                | Mogelijke Mitigatie                          |
| ---------------------- | -------------------------------------------- |
| Data-onevenwichtigheid | Herbalancering, oversampling, synthetic data |
| Bias in brondata       | Databronnen uitbreiden, debiasing            |
| Prompt bias            | Neutrale formulering, expliciete instructies |
| Model bias             | Threshold calibratie, post-processing        |

**Stap 5: Documenteer en Rapporteer**

Leg vast in [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md):

- Welke groepen zijn vergeleken
- Welke metrics zijn gemeten
- Resultaten per groep
- Conclusie t.a.v. drempels
- Mitigatiemaatregelen (indien van toepassing)

### Tooling voor Fairness audit (bias audit)

| Tool                      | Type           | Sterkte                                    | Link                             |
| ------------------------- | -------------- | ------------------------------------------ | -------------------------------- |
| **Fairlearn** (Microsoft) | Python library | Integratie met sklearn, meerdere metrics   | fairlearn.org                    |
| **AI Fairness 360** (IBM) | Python toolkit | Uitgebreide algoritmes, goede documentatie | aif360.mybluemix.net             |
| **Aequitas**              | Python library | Focus op auditing, visuele reports         | github.com/dssg/aequitas         |
| **What-If Tool** (Google) | Visualisatie   | Interactieve exploratie                    | pair-code.github.io/what-if-tool |

### Beperkingen en Overwegingen

**Fairness-accuracy trade-off:**
Het optimaliseren voor fairness kan leiden tot lagere overall accuracy. Documenteer de afweging.

**Incompatibiliteit van criteria:**
Sommige fairness criteria zijn mathematisch onverenigbaar. Kies criteria die passen bij de use case.

**Proxy discriminatie:**
Zelfs zonder directe beschermde kenmerken kan een model discrimineren via proxy's. Test hierop.

**Intersectionaliteit:**
Fairness voor individuele groepen garandeert geen fairness voor combinaties (bijv. jonge vrouwen). Overweeg subgroep-analyse bij Hoog Risico.

______________________________________________________________________

## 4. De Rol van de Guardian

De Guardian fungeert als het morele kompas van het project:

- Bewaakt de **Rode Lijnen**
- Voert onafhankelijke ethische reviews uit
- Heeft veto-mandaat bij ethische overschrijdingen
- Keurt Fairness audit (bias audit) resultaten goed
- Escaleert bij onoplosbare fairness issues

### Guardian Taken per Fase

| Fase       | Guardian Activiteit                                       |
| ---------- | --------------------------------------------------------- |
| Verkenning | Ethische wenselijkheid beoordelen, Rode Lijnen definiëren |
| Validatie  | Fairness audit (bias audit) uitvoeren/reviewen            |
| Realisatie | Mitigatiemaatregelen valideren                            |
| Levering   | Finale ethische goedkeuring                               |
| Beheer     | Periodieke ethics reviews, bias monitoring                |

______________________________________________________________________

## 5. Checklist Ethische Richtlijnen

!!! check "5. Checklist Ethische Richtlijnen"
    - [ ] Ethische grondbeginselen zijn besproken met team
    - [ ] Rode Lijnen zijn gedefinieerd in Doelkaart (goal card)
    - [ ] Relevante groepen voor Fairness audit (bias audit) zijn geïdentificeerd
    - [ ] Fairness audit (bias audit) is uitgevoerd conform risiconiveau
    - [ ] Resultaten voldoen aan drempels óf mitigatie is gedocumenteerd
    - [ ] Guardian heeft ethische goedkeuring gegeven
    - [ ] Transparantieplicht is geïmplementeerd (Beperkt/Hoog Risico)

______________________________________________________________________

## 6. Gerelateerde Modules

- [Risicobeheersing & Compliance](index.md)
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- [EU AI Act](01-eu-ai-act/index.md)
