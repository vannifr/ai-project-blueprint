---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# ðŸ“‚ Module 09.04: Technische Modelkaart (Model Card)

## ðŸŽ¯ Doel

Dit sjabloon is bedoeld voor ontwikkelaars en auditors. Het documenteert de technische specificaties, trainingsdata en prestaties van het model en reist mee van **Realisatie** naar **Beheer & Optimalisatie**.

______________________________________________________________________

**Model Naam:** \[Bijv. Klantenservice-Bot-v2\]
**Versie:** \[X.X.X\]
**Type:** \[Bijv. LLM (GPT-4o) met RAG\]
**Datum:** \[DD-MM-JJJJ\]

______________________________________________________________________

### ðŸ“‚ 1. Doel & Beperkingen

- **Primair Gebruik:** \[Waar is dit model voor bedoeld?\]
- **Buiten Scope:** \[Waar mag dit model NIET voor gebruikt worden?\]
- **Samenwerkingsmodus:** \[Bijv. Modus 3: Collaboratief\]

______________________________________________________________________

### ðŸ“‚ 2. Technische Specificaties

- **Basismodel (Foundation):** \[Bijv. Azure OpenAI GPT-4\]
- **Parameters:** \[Bijv. Temperature: 0.7, TopP: 0.9\]
- **Kenniskoppeling (RAG):**
    - **Bron:** \[Bijv. SharePoint Map 'Kennisbeheer'\]
    - **Update frequentie:** \[Wekelijks / Real-time\]

______________________________________________________________________

### ðŸ“‚ 3. Training & Data

- *Alleen invullen indien er sprake is van fine-tuning of eigen training.*
- **Trainingsdata:** \[Beschrijving dataset\]
- **Periode:** \[Data van JJJJ tot JJJJ\]
- **Data-Evaluatie:** \[Verwijzing naar kwaliteitsrapport / Module 02\]

______________________________________________________________________

### ðŸ“‚ 4. Prestaties & Validatie

*Resultaten geëxtraheerd uit het **Validatierapport** (Fase 3).*

- **Metrieken:**
    - **Nauwkeurigheid (Accuracy):** \[X%\]
    - **Hallucinatie-rate:** \[\< X%\]
- **Testset:** \[Beschrijving van de gebruikte vragen of scenario's\]

______________________________________________________________________

### ðŸ“‚ 5. Ethische Overwegingen

- **Bekende Beperkingen:** \[Bijv. "Model heeft moeite met jargon in taal X".\]
- **Bias Mitigatie:** \[Welke stappen zijn genomen om vooroordelen te verminderen?\]

______________________________________________________________________

### ðŸ‘¥ 6. Beheer & Onderhoud

- **Eigenaar (Tech):** \[Naam Tech Lead\]
- **Eigenaar (Business):** \[Naam Product Owner\]
- **Drift Monitoring:** \[Welke tool meet het **Prestatieverloop**?\]

______________________________________________________________________

### ⚙️ Versiebeheer

- **v1.0:** Initial Release (Naam Developer)
- **v1.1:** Prompt update na feedback (Naam Developer)

______________________________________________________________________

**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Draft

______________________________________________________________________

## Â

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
