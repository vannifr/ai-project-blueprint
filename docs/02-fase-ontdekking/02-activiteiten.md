---
versie: '1.0'
type: activities
layer: 2
phase: [1]
roles: [AI Product Manager]
---

# 1. Kernactiviteiten & Rollen (Verkenning & Strategie)

!!! abstract "Doel"
    Overzicht van de kernactiviteiten en rolverdelingen tijdens de Verkenningsfase, van probleemverkenning tot dataevaluatie en risicobeoordeling.

## 1. Kernactiviteiten

### Probleemverkenning

We definiëren de uitdaging vanuit de eindgebruiker, niet vanuit de technologie.

- **Vraagarticulatie:** Wat is het echte probleem? Wat zijn de pijnpunten?
- **AI-Geschiktheid:** Is AI hier echt de oplossing? Of kan het eenvoudiger?
- **Succesindicatoren:** Hoe meten we of we het probleem hebben opgelost?

### Data-Evaluatie

Een analyse van de benodigde informatie op drie dimensies:

#### Toegang

- **Vraag:** Mogen en kunnen we er technisch bij?
- **Check:** Juridische rechten, API's, databases, beveiliging

#### Kwaliteit

- **Vraag:** Is de data compleet en consistent?
- **Check:** Volledigheid, nauwkeurigheid, actualiteit, duplicaten

#### Relevantie

- **Vraag:** Bevat de data het answer op de vraag?
- **Check:** Correlatie met het doel, representativiteit

### Risico-Inventarisatie

Een eerste scan op juridische en ethische obstakels.

- **EU AI Act Classificatie:** Valt het systeem onder hoog-risico?
- **Privacy & AVG:** Welke persoonsgegevens worden verwerkt?
- **Ethische Vraagstukken:** Kan het systeem discrimineren of schade veroorzaken?
- **Organisatorische Risico's:** Hebben we de juiste mensen en middelen?

______________________________________________________________________

## 1b. Projecttype Classificatie

!!! info "Twee projecttypen in het kort"
    - **Type A — Bouwen met AI**: Het ontwikkelteam gebruikt AI-tools en agentische AI als onderdeel van het ontwikkelproces. Het eindproduct zelf hoeft geen AI te bevatten.
    - **Type B — AI in het Product**: Het eindproduct integreert AI-functionaliteit voor eindgebruikers.

Voordat u verdergaat met de kernactiviteiten, bepaal het type AI-project. De Blueprint onderscheidt twee fundamenteel verschillende projecttypen:

| Kenmerk                | Type A — Bouwen *met* AI                                                                                                                                                      | Type B — AI *in* het product                                                                                                 |
| :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **Omschrijving**       | AI/agents worden ingezet als ontwikkeltools (code-assistenten, testgeneratie, documentatieautomatisering)                                                                     | Het eindproduct bevat AI-functionaliteit voor eindgebruikers (aanbevelingen, classificatie, generatie, agentische workflows) |
| **Risicoprofiel**      | Standaard softwarerisico's; AI-fouten raken het ontwikkelproces, niet de eindgebruiker                                                                                        | AI-specifieke risico's; fouten raken eindgebruikers, klanten of bedrijfsprocessen direct                                     |
| **Samenwerkingsmodus** | Doorgaans Modus 1–2 (de ontwikkelaar beoordeelt AI-output)                                                                                                                    | Modus 2–5 afhankelijk van risico en volume (volledige lifecycle vereist)                                                     |
| **Blueprint scope**    | Selectief: gebruik [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md), [Governance Model](../00-strategisch-kader/03-governance-model.md) en relevante cheatsheets | Volledig: alle fasen, Gate Reviews, Samenwerkingsmodi en monitoring zijn van toepassing                                      |

!!! warning "Deze Blueprint is primair ontworpen voor Type B-projecten"
    Type A-projecten (bouwen *met* AI) kunnen geselecteerde modules gebruiken, maar vereisen niet de volledige levenscyclus. Classificeer uw project bewust — een verkeerde classificatie leidt tot ofwel onnodig zware governance, ofwel onvoldoende waarborgen.

**Twijfelt u?** Als het AI-systeem output genereert die direct door eindgebruikers wordt gezien of gebruikt zonder menselijke tussenkomst, is het een Type B-project.

## 2. Team & Rollen

| Rol                     | Verantwoordelijkheid in Verkenning                                     |
| :---------------------- | :--------------------------------------------------------------------- |
| **AI Product Manager**  | **A**ccountable: Eigenaar van de business case en probleemarticulatie. |
| **Data Scientist**      | **R**esponsible: Uitvoeren van de Data-Evaluatie.                      |
| **Business Sponsor**    | **C**onsulted: Valideert het probleem en de waarde-hypothese.          |
| **Guardian (Ethicist)** | **C**onsulted: Voert de eerste ethische en juridische scan uit.        |
| **Stakeholders**        | **I**nformed: Worden op de hoogte gehouden van bevindingen.            |

______________________________________________________________________

## 5. Gerelateerde Modules

**Sjablonen:**

- [Project Charter](../09-sjablonen/01-project-charter/template.md)
- [Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)
- [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)

**Zie ook:** [Overzicht Fase 1](01-doelstellingen.md) · [Opleveringen](03-afleveringen.md)

______________________________________________________________________

**Volgende stap:** Vul de Doelkaart in en voer de Moduskeuze Beoordeling uit.
→ Gebruik het [Project Charter](../09-sjablonen/01-project-charter/template.md) als startpunt.
→ Zie ook: [Moduskeuze Beoordeling](05-has-h-beoordeling.md) | [Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)
