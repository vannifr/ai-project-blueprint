---
versie: '1.0'
---

# 1. Rollen & Verantwoordelijkheden

## 1. Wie doet wat in een AI-project?

In AI-projecten vervagen de grenzen tussen business en IT. Daarom definiëren we rollen op basis van verantwoordelijkheid, niet op basis van functietitel.

______________________________________________________________________

## 2. Het Kernteam (The Squad)

Deze mensen werken dagelijks aan het project en vormen de motor van de innovatie.

### De AI Product Manager (Business Lead)

Niet zomaar een Product Owner. De AI PM begrijpt niet alleen de klantvraag, maar snapt ook wat technisch haalbaar is met AI (en wat niet).

- **Verantwoordelijkheid:** De **Doelkaart (goal card)**.
- **Taak:** Vertaalt vage business-wensen naar scherpe AI-instructies. Beheert de backlog en prioriteert op waarde.
- **Focus:** "Lossen we het juiste probleem op?"

### De Tech Lead (Technical Lead)

De architect van de oplossing. Zorgt dat de losse componenten (data, model, interface) naadloos samenwerken.

- **Verantwoordelijkheid:** De **Technische Modelkaart**.
- **Taak:** Selecteert het juiste model, bouwt de pijplijnen en borgt de technische stabiliteit.
- **Focus:** "Is het robuust en schaalbaar?"

### De Guardian (Rol & Invulling)

De 'Guardian' is geen enkele functietitel, maar een rol met veto-recht die waakt over de ethische en wettelijke kaders. Gezien de complexiteit wordt deze rol in de praktijk vaak ingevuld door een duo ("Two-man rule"):

- **Privacy & Legal Officer:** Toetst op AVG, EU AI Act en juridische risico's. Focus: *Mag dit wettelijk?*
- **AI Quality Ethicist (of QA Lead):** Toetst op bias in de dataset, kwaliteit van de Golden Set en output-veiligheid. Focus: *Is dit eerlijk en veilig?*

Voor projecten met een **Hoog Risico** is expliciete goedkeuring van beiden vereist bij Gate Reviews. Bij kleine projecten kan één persoon de rol dragen, mits voldoende mandaat.

- **Verantwoordelijkheid:** De **Risico Pre-scan**.
- **Focus:** "Is het veilig en eerlijk?"

______________________________________________________________________

## 3. De Ondersteunende Rollen

Deze specialisten worden ingevlogen wanneer de specifieke fase daarom vraagt.

| Rol                     | Focus           | Taak                                                                                       |
| :---------------------- | :-------------- | :----------------------------------------------------------------------------------------- |
| **Data Engineer**       | Datakwaliteit   | De ruggengraat van de data. Zorgt dat data schoon aankomt bij het model.                   |
| **AI Tester (QA)**      | Betrouwbaarheid | Specialist in het 'kapot maken' van AI via *Adversarial Testing*.                          |
| **Adoptie Manager**     | Verandering     | Zorgt dat mensen de tool echt gebruiken (ADKAR-model).                                     |
| **Context Builder**     | Kennisbeheer    | Beheert wat het model op elk moment ziet — zie uitbreiding hieronder.                      |
| **AI Security Officer** | Beveiliging     | Focust op LLM-kwetsbaarheden, data poisoning en AI-governance — zie uitbreiding hieronder. |

______________________________________________________________________

### Context Builder

De industrie verschuift van *prompt engineering* (instructies schrijven) naar **context engineering** (beheren wat het model op elk moment ziet). De Context Builder fungeert als digitale bibliothecaris: hij verzamelt relevante informatie uit honderden bestanden en realtime datastromen, samenvat deze, en archiveert ze in een hiërarchische kennisbank die de contextlimieten van het LLM overstijgt.

**Kernverantwoordelijkheden:**

- Ontwerpen en onderhouden van de RAG-architectuur (Retrieval-Augmented Generation)
- Voorkomen van *contextvervuiling* — meer context is niet altijd beter; irrelevante informatie schaadt de modelprestaties
- Verlagen van inferentiekosten via gerichte informatieophaling (tot 50× goedkoper dan volledige context)
- Bewaken van de Context Development Lifecycle: welke informatie is actueel, welke verouderd?

**Wanneer inzetten:** verplicht bij RAG-systemen of wanneer het model toegang heeft tot meer dan één kennisbron. Kan een menselijke rol zijn of een geautomatiseerde agentic component.

Bron: \[so-44\]

______________________________________________________________________

### AI Security Officer

Naarmate AI-systemen kritischer worden, volstaan traditionele beveiligingsrollen niet langer. De AI Security Officer richt zich specifiek op dreigingen die uniek zijn voor ML-systemen.

**Kernverantwoordelijkheden:**

- Dreigingsmodellering op basis van de [OWASP Top 10 voor LLMs](../07-compliance-hub/07-red-teaming.md)
- Uitvoeren of coördineren van Red Teaming sessies
- Beheer van AI-governance raamwerken (EU AI Act Art. 9, NIST AI RMF)
- Respons op AI-specifieke incidenten: model poisoning, prompt injection, bias-escalaties

**Certificering:** ISACA introduceerde in augustus 2025 de **AAISM** (Advanced in AI Security Management) — 's werelds eerste AI-gecentreerde beveiligingsmanagementkwalificatie, specifiek gericht op LLM-kwetsbaarheden en AI-governance.

Bron: \[so-45\]

______________________________________________________________________

## 4. Strategisch Niveau (Steering Com)

### Chief AI Officer (CAIO)

Sponsor van het programma. Bepaalt de overkoepelende strategie en wijst budget toe.

- **Taak:** Beslist bij de **Gates** of een project doorgaat of stopt.
- **Eigenaarschap:** Bewaakt het gehele portfolio en de AI-volwassenheid van de organisatie.
