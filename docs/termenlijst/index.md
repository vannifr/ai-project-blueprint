---
versie: '1.0'
---

# 1. Termenlijst (Glossary)

Dit document bevat de definities van de belangrijkste termen en afkortingen die in de AI Project Blauwdruk worden gebruikt. Wij slaan de brug tussen techniek en business door consequent heldere Nederlandse termen te gebruiken.

______________________________________________________________________

## 1. A

- **Fine-tunen:** Het fine-tunen van parameters en configuraties om de prestaties van een AI-model te optimaliseren voor een specifieke taak (*Hyperparameter Tuning*).
- **AI-Samenwerkingsmodi:** Een model met vijf niveaus dat de relatie en taakverdeling tussen mens en AI definieert (Instrumenteel t/m Autonoom). → [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)

## 2. B

- **Beheer & Optimalisatie:** De fase na ingebruikname gericht op het monitoren van prestaties, kosten en compliance.
- **Bewijsstandaarden:** De minimale criteria waaraan testresultaten en documentatie moeten voldoen om door een Gate te komen. Definieert normen per risiconiveau voor feitelijkheid, relevantie, veiligheid en eerlijkheid. → [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- **Bias:** Vooroordelen in data of modellen die leiden tot onrechtvaardige resultaten. Zie ook **Fairness audit (bias audit)**.
- **Business Case:** Het financiële onderbouwingsdocument dat de investering, verwachte opbrengsten (ROI) en kosten-batenanalyse beschrijft. Wordt aangevuld met de **Doelkaart (goal card)** voor AI-specifieke doeldefinities en Rode Lijnen.

## 3. C

- **CI/CD (Continuous Integration / Continuous Delivery):** Een automatische pijplijn die codewijzigingen bouwt, test en beschikbaar stelt. In AI-projecten bewaakt de CI/CD-pijplijn ook modelkwaliteit via geautomatiseerde gates (bijv. nauwkeurigheid > 85% voor ingebruikname).
- **Circuit Breaker:** Een automatisch stopmechanisme in agentic AI-systemen dat acties blokkeert of menselijke goedkeuring vereist wanneer het systeem afwijkend gedrag vertoont of geconfigureerde drempelwaarden overschrijdt.
- **Constitutional AI:** Een techniek waarbij AI-systemen worden getraind met expliciete ethische principes als verankerd stelsel van regels, zodat het systeem consistent veilig en eerlijk gedrag vertoont.

## 4. D

- **Data-Evaluatie:** Het proces van het beoordelen of data geschikt is voor een AI-oplossing op basis van Toegang, Kwaliteit en Relevantie.
- **Doeldefinitie:** Een formeel document dat het beoogde resultaat en de waarde-hypothese van een AI-systeem vastlegt (*Intent Record*).
- **Doelkaart (goal card):** Het AI-specifieke sturingsdocument dat de **Doeldefinitie** (wat willen we bereiken), **Rode Lijnen** (wat mag nooit gebeuren) en **Prompts** (hoe sturen we het gedrag) combineert. Kernafact voor elke AI-oplossing (*Intent Map*). → [Doelkaart (goal card) sjabloon](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)
- **DPIA (Data Protection Impact Assessment):** Verplichte risicoanalyse onder de AVG voor AI-systemen die persoonsgegevens verwerken en een hoog risico vormen voor de betrokkenen. → [Data & Privacyblad](../09-sjablonen/11-privacy-data/privacyblad.md)

## 5. E

- **Fairness audit (bias audit):** Een controle of audit om ongewenste vooroordelen of discriminatie in de output van een AI-systeem op te sporen. Meet verschillen in prestaties tussen groepen (*Bias Audit*).
- **EU AI Act:** De Europese verordening die regels stelt voor de veiligheid en ethiek van AI-systemen. → [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md)

## 6. F

- **Fast Lane:** Een versnelde projectroute voor AI-toepassingen met Minimaal risico en Samenwerkingsmodus 1-2. Vereist minder documentatie maar behoudt kerngovernance. → [Fast Lane](../02-fase-ontdekking/06-fast-lane.md)

## 7. G

- **Gate:**
- **GPU (Graphics Processing Unit):** Gespecialiseerde processor die veelvuldig wordt ingezet voor het trainen en uitvoeren van AI-modellen, vanwege de hoge parallelisatiecapaciteit. Een formeel beslismoment in de AI-levenscyclus waarbij op basis van bewijs een Go/No-Go beslissing wordt genomen. De blauwdruk definieert 4 gates (Gate 1 t/m Gate 4). → [Gate Reviews](../09-sjablonen/04-gate-reviews/checklist.md)
- **Gebruikskosten:** De variabele kosten voor het draaien van een AI-systeem, zoals API-tokens of cloud-rekentijd (*Inference costs*).
- **Golden Set:** Een representatieve verzameling testcases die wordt gebruikt om AI-prestaties te meten. Bevat standaardcases, randgevallen en adversarial scenarios. Grootte varieert per risiconiveau (20-150 cases).
- **Guardian:** De onafhankelijke rol binnen het projectteam die waakt over ethische en wettelijke kaders. Heeft veto-recht bij overschrijding van Rode Lijnen. → [Rollen & Verantwoordelijkheden](../08-rollen-en-verantwoordelijkheden/index.md)

## 8. H

- **Het Kostenoverzicht:** Een integrale berekening van alle kosten (investering + exploitatie) en de verwachte opbrengsten (ROI) (*Total Cost of Ownership*).
- **Human-in-the-loop:** Een werkwijze waarbij een mens toezicht houdt of een beslissende rol speelt in een AI-gestuurd proces.

## 9. I

- **Ingebruikname:** Het proces van het live zetten van een AI-systeem in de productieomgeving en de overdracht aan de organisatie (*Deployment / Livegang*).

## 10. K

- **RAG:** Het verbinden van een AI-model aan specifieke bedrijfsinformatie of documenten om de antwoorden relevanter en accurater te maken (*Retrieval-Augmented Generation / RAG*).
- **Kernprincipes:** De fundamentele uitgangspunten van deze blauwdruk, gericht op gedragssturing, impact, traceerbaarheid en continue toetsing.

## 11. M

- **LLM (Large Language Model):** Een grootschalig taalmodel getraind op omvangrijke tekstcorpora, in staat tot het genereren, samenvatten en redeneren over tekst. Voorbeelden zijn modellen in de GPT-, Claude- en Gemini-familie.
- **MLOps (Machine Learning Operations):** De combinatie van praktijken, processen en tools voor het betrouwbaar bouwen, testen, uitrollen en bewaken van ML-modellen in productie. Het is de ML-tegenhanger van DevOps.
- **Modelkaart:** Verkorte naam voor **Technische Modelkaart**. Het technische verantwoordingsdocument voor ontwikkelaars en auditors. → [Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md)
- **Modus 1–5 (AI-Samenwerkingsmodi):** De vijf samenwerkingsniveaus tussen mens en AI: Modus 1 (Instrumenteel), Modus 2 (Adviserend), Modus 3 (Collaboratief), Modus 4 (Delegerend), Modus 5 (Autonoom). → [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)

## 12. P

- **Proof of Value (PoV):** Een kleinschalig, gecontroleerd experiment om te bewijzen dat een AI-oplossing werkt in de beoogde context (*Proof of Value / PoV*). → [Fase 2: Validatie](../03-fase-validatie/01-doelstellingen.md)
- **Drift:** Het fenomeen waarbij de nauwkeurigheid of relevantie van een model over tijd afneemt door veranderingen in data of de wereld (*Model Drift / Data Drift*). → [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)

## 13. R

- **RACI:** Een matrix voor het toewijzen van rollen: **R**esponsible (uitvoerder), **A**ccountable (eindverantwoordelijke), **C**onsulted (geraadpleegd), **I**nformed (geïnformeerd). Elke activiteit heeft precies één A.
- **ROI (Return on Investment):** De verhouding tussen de opbrengst en de investering van een project of systeem, uitgedrukt als percentage of absolute waarde.
- **Realisatie:** De fase waarin de AI-oplossing technisch wordt gebouwd en uitvoerig wordt getest.
- **Rode Lijnen:** De harde grenzen en veiligheidskaders waar een AI-systeem nooit buiten mag treden (*Constraints / Guardrails*).

## 14. S

- **SLO (Service Level Objective):** Een meetbaar streefdoel voor de kwaliteit of beschikbaarheid van een dienst, zoals "latentie P95 \< 2 seconden" of "uptime > 99,5%". Lager dan een SLA maar intern bindend voor het team.
- **Specificatie-gedreven Ontwikkeling (SDD):** Een methode waarbij tests en specificaties worden opgesteld vóór de implementatie. Eerst definiëren wat het systeem moet doen en wat het nooit mag doen, daarna pas bouwen (*Spec-First / Test-Driven Development*). → [Spec-Driven Development](../01-ai-native-fundamenten/06-specificatie-gedreven-ontwikkeling.md)
- **Prompts:** De verzameling van informatie, aanwijzingen en configuraties die bepalen hoe de AI zich gedraagt (*Prompts / Context Artifacts*). → [Prompt Engineering sjabloon](../09-sjablonen/10-prompt-engineering/template.md)

## 15. T

- **Technische Modelkaart:** Het technische verantwoordingsdocument voor ontwikkelaars en auditors. Beschrijft modelversie, architectuur, databronnen en configuratie. → [Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md)

## 16. V

- **Validatierapport:** Het bewijsdocument dat met objectieve testdata aantoont dat een AI-systeem voldoet aan de gestelde doelen en de normen uit de Bewijsstandaarden. Bevat testresultaten, metrics en conclusies (*Evidence Report*). Let op: dit is een ander document dan het Data & Privacyblad (AVG-gerelateerd). → [Validatierapport sjabloon](../09-sjablonen/07-validatie-bewijs/validatierapport.md)
- **Verkenning & Strategie:** De eerste fase van een project gericht op het begrijpen van het probleem en de haalbaarheid.

## 17. W

- **Wildgroei:** Het ongecontroleerd of onbeheerd gebruik van AI-tools binnen een organisatie (*Shadow AI*).

______________________________________________________________________
