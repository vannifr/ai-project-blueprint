---
versie: '1.0'
---

# 1. De Doelkaart (goal card) (Intent Map)

## 1. Doel

De Doelkaart (goal card) formaliseert de **Doeldefinitie** van het AI-project. Dit document verbindt de menselijke intentie aan de technische **Prompts** en fungeert als de bron waaruit de AI-oplossing wordt gegenereerd.

______________________________________________________________________

**Project:** \[Naam Project\]

______________________________________________________________________

### A. De Intentie (Human Intent)

*Wat probeert de gebruiker te bereiken en hoe moet de AI zich gedragen?*

- **De Gebruiker (Persona):** Wie is het? \[Bijv. Een junior juridisch medewerker.\]
- **Het Doel:** Wat willen ze bereiken? \[Snel de risico's in een contract vinden.\]
- **De AI (Systeem Persona):**
- **Rol:** \[Bijv. Een ervaren senior jurist en mentor.\]
- **Toon:** \[Zakelijk, scherp, maar behulpzaam. Geen jargon zonder uitleg.\]
- **De Taak:** \[Beschrijf exact wat de AI moet doen. Bijv: "Scan het geüploade PDF-document op clausules over aansprakelijkheid en vat deze samen."\]

______________________________________________________________________

### B. Prompts (Context)

*Welke kennis heeft de AI nodig om dit te doen?*

- **Primaire Bronnen:** \[Bedrijfsinformatie/Handboeken voor de **RAG**.\]
- **Voorbeelden (Few-Shot):**
- **Input:** \[Voorbeeld van een vage clausule.\]
- **Gewenste Output:** \[Hoe de AI dit had moeten interpreteren/verbeteren.\]
- *(Voeg minimaal 3 goede voorbeelden toe om het gedrag te sturen).*

______________________________________________________________________

### C. Rode Lijnen (Constraints)

*Wat mag de AI absoluut niet doen? Dit zijn de harde veiligheidsregels.*

- **Veiligheid:** \[Bijv. Geef nooit juridisch advies over strafrecht.\]
- **Format:** \[Bijv. Antwoord mag nooit langer zijn dan 2 alinea's.\]
- **Gedrag / Overtuiging:** \[Bijv. Verzin geen feiten. Als het niet in de bronnen staat, zeg dan: "Ik weet het niet".\]

______________________________________________________________________

### D. Toetsing (Evidence)

*Hoe bewijzen we dat de Doelkaart (goal card) werkt? Dit is de input voor het **Validatierapport**.*

- **Testprompt 1 (Succesval):** \[Vraag die de AI correct moet beantwoorden.\]
- **Testprompt 2 (Adversarial):** \[Vraag die probeert de AI te laten hallucineren of de **Rode Lijnen** te laten overschrijden.\]
- **Acceptatie-score:** \[Minimaal cijfer (bijv. 8 op relevantie) of percentage.\]

______________________________________________________________________

### Goedkeuring door Guardian

**Naam:** \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]

______________________________________________________________________
