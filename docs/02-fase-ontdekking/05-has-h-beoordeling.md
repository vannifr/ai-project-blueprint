---
versie: '1.0'
type: assessment
layer: 2
phase: [1]
roles: [AI Product Manager]
---

# 5. Moduskeuze Beoordeling

## 1. Doelstelling

Tijdens de Verkenningsfase bepalen wij welke [Samenwerkingsmodus](../00-strategisch-kader/06-has-h-niveaus.md) (Modus 1 t/m 5) passend is voor de te ontwikkelen gebruikscasus. Deze keuze legt de basis voor de governance-eisen, de technische vereisten en de menselijke toezichtsstructuur van het project.

De beoogde modus wordt vastgelegd in het [Project Charter](../09-sjablonen/01-project-charter/template.md).

______________________________________________________________________

## 2. Beoordelingsproces

De moduskeuze beoordeling bestaat uit drie stappen:

1. **Risicoanalyse** — Wat zijn de gevolgen als het systeem een fout maakt?
1. **Beslisanalyse** — Wie neemt de uiteindelijke beslissing?
1. **Moduskeuze** — Welke modus past het beste bij het risico en de beslisstructuur?

______________________________________________________________________

## 3. Stap 1: Risicoanalyse

Score de volgende vragen. Elke vraag levert 0, 1 of 2 punten.

| Vraag                                                      | 0 punten            | 1 punt            | 2 punten                           | Score |
| :--------------------------------------------------------- | :------------------ | :---------------- | :--------------------------------- | :---: |
| Wat is de impact van een fout van het AI-systeem?          | Geen of herstelbaar | Beperkt, intern   | Groot of extern (klant, juridisch) |       |
| Hoe snel moet een fout gecorrigeerd worden?                | Geen tijdsdruk      | Binnen dagen      | Direct (real-time)                 |       |
| Worden persoonsgegevens verwerkt?                          | Nee                 | Geanonimiseerd    | Ja, direct identificeerbaar        |       |
| Valt dit systeem onder de EU AI Act hoog-risico categorie? | Nee                 | Onbekend          | Ja                                 |       |
| Kunnen besluiten van het systeem iemand benadelen?         | Nee                 | Indirect mogelijk | Ja, direct                         |       |

**Totale risicoscore:** \_\_\_\_\_ (max. 10)

______________________________________________________________________

## 4. Stap 2: Beslisanalyse

Beantwoord de volgende vragen:

**a. Wie keurt de output van het AI-systeem goed vóór gebruik?**

- [ ] Niemand — het systeem handelt direct (→ hoge modus)
- [ ] Een medewerker keurt elk voorstel goed (→ lage/middelste modus)
- [ ] Steekproef: een medewerker controleert periodiek (→ middelste/hoge modus)

**b. Hoe snel moet het systeem reageren?**

- [ ] Real-time (\< 1 seconde) → menselijke goedkeuring per beslissing is niet haalbaar
- [ ] Bijna real-time (seconden tot minuten) → beperkte menselijke tussenkomst mogelijk
- [ ] Asynchroon (uren tot dagen) → volledige menselijke goedkeuring haalbaar

**c. Wat is de omvang van de beslissingen?**

- [ ] Minder dan 100 per dag → individuele beoordeling haalbaar
- [ ] 100–10.000 per dag → steekproef haalbaar
- [ ] Meer dan 10.000 per dag → geautomatiseerde bewaking noodzakelijk

______________________________________________________________________

## 5. Stap 3: Moduskeuze

Combineer de risicoscore met de beslisanalyse om de aanbevolen modus te bepalen:

| Risicoscore | Beslissing per geval door mens | Aanbevolen startmodus                               |
| :---------- | :----------------------------- | :-------------------------------------------------- |
| 0 – 3       | Ja                             | **Modus 2 (Adviserend)**                            |
| 0 – 3       | Nee, te groot volume           | **Modus 3 (Collaboratief)**                         |
| 4 – 6       | Ja, elke beslissing            | **Modus 2 (Adviserend)**                            |
| 4 – 6       | Steekproef / monitoring        | **Modus 3 (Collaboratief)**                         |
| 7 – 10      | Elke beslissing verplicht      | **Modus 2 (Adviserend)**                            |
| 7 – 10      | Niet haalbaar door volume      | **Modus 4 (Gedelegeerd)** — met strenge Rode Lijnen |

!!! tip "Begin laag, schaal op"
    Start in de laagst haalbare modus om vertrouwen en data op te bouwen. Verhoog de modus pas na bewijs van betrouwbaarheid (≥ 90% nauwkeurigheid over minimaal 4 weken productie).

!!! warning "Modus 5 (Autonoom)"
    Modus 5 vereist altijd een expliciete beslissing van de stuurgroep én goedkeuring van de Guardian. Het is geen automatische vervolgstap op Modus 4.

______________________________________________________________________

## 5b. Architectuurspecifieke Overwegingen

De moduskeuze hangt mede af van het type AI-architectuur. Elk type heeft specifieke aandachtspunten bij de beoordeling:

| Architectuur                             | Primair Aandachtspunt              | Sleutelvragen                                                                                     |
| :--------------------------------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------ |
| **RAG (Retrieval-Augmented Generation)** | Documentdekking & ophaalrelevantie | Beschikt u over ≥100 kwalitatieve brondocumenten? Kunt u ophaalrelevantie meten?                  |
| **Fine-tuning**                          | Labelbudget & datakwaliteit        | Beschikt u over 5k–50k gelabelde voorbeelden? Is de data representatief voor de productiecontext? |
| **Agentisch (Modus 4-5)**                | Toolbetrouwbaarheid & rode lijnen  | Zijn de aangeroepen tools betrouwbaar? Wat is de ergst denkbare actie die de agent kan uitvoeren? |

!!! tip "Architectuurkeuze beïnvloedt moduskeuze"
    Een RAG-systeem met beperkte brondocumenten start doorgaans in Modus 2. Een agentisch systeem met financiële tools vereist minimaal Modus 4 governance — ongeacht de risicoscore.

______________________________________________________________________

## 6. Vastlegging

De uitkomst van de moduskeuze beoordeling wordt vastgelegd in:

1. **Project Charter** — Sectie 'Samenwerkingsmodus': noteer de gekozen modus en de motivatie.
1. **Rode Lijnen** — Definieer de grenzen die passen bij de gekozen modus.
1. **Validatieplan** — Koppel de modus aan de vereiste validatie-intensiteit (zie [Validatie Model](../01-ai-native-fundamenten/04-validatie-model.md)).

| Te documenteren                    | Waar                 | Eigenaar       |
| :--------------------------------- | :------------------- | :------------- |
| Gekozen modus (1–5)                | Project Charter      | AI PM          |
| Risicoscore en motivatie           | Project Charter      | Guardian       |
| Rode Lijnen gekoppeld aan modus    | Rode Lijnen document | Guardian       |
| Validatie-eisen op basis van modus | Validatieplan        | Tech Lead + QA |

______________________________________________________________________

## 7. Gerelateerde Modules

- [Verkenning & Strategie — Kernactiviteiten](02-activiteiten.md)
- [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
- [Project Charter Sjabloon](../09-sjablonen/01-project-charter/template.md)
- [Validatie Model](../01-ai-native-fundamenten/04-validatie-model.md)
- [Risicobeheer](../07-compliance-hub/02-risicobeheer/index.md)

______________________________________________________________________

**Volgende stap:** Bepaal de samenwerkingsmodus en leg deze vast in het [Project Charter](../09-sjablonen/01-project-charter/template.md)
→ Zie ook: [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
