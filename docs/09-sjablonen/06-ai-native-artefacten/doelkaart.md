---
versie: '1.0'
type: template
layer: 3
phase: [1, 2, 3]
tags: [template]
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

### C. Harde Grenzen (Constraints)

*Wat mag de AI absoluut niet doen? Dit zijn de harde veiligheidsregels.*

- **Veiligheid:** \[Bijv. Geef nooit juridisch advies over strafrecht.\]
- **Format:** \[Bijv. Antwoord mag nooit langer zijn dan 2 alinea's.\]
- **Gedrag / Overtuiging:** \[Bijv. Verzin geen feiten. Als het niet in de bronnen staat, zeg dan: "Ik weet het niet".\]

______________________________________________________________________

### D. Toetsing (Evidence)

*Hoe bewijzen we dat de Doelkaart (goal card) werkt? Dit is de input voor het **Validatierapport**.*

- **Testprompt 1 (Succesval):** \[Vraag die de AI correct moet beantwoorden.\]
- **Testprompt 2 (Adversarial):** \[Vraag die probeert de AI te laten hallucineren of de **Harde Grenzen** te laten overschrijden.\]
- **Acceptatie-score:** \[Minimaal cijfer (bijv. 8 op relevantie) of percentage.\]

______________________________________________________________________

### E. Aannames

*Welke aannames liggen onder dit project? Documenteer de belangrijkste aannames en hun validatiestatus. Test de riskantste aanname eerst.*

| Categorie      | Aanname                                                 | Impact als onjuist      | Bewijs                 | Status                             |
| :------------- | :------------------------------------------------------ | :---------------------- | :--------------------- | :--------------------------------- |
| **Data**       | \[Bijv. Voldoende representatieve data is beschikbaar\] | \[Hoog/Gemiddeld/Laag\] | \[Welk bewijs is er?\] | \[Open / Gevalideerd / Ontkracht\] |
| **Model**      | \[Bijv. Model generaliseert naar productiedata\]        | \[Hoog/Gemiddeld/Laag\] | \[Welk bewijs is er?\] | \[Open / Gevalideerd / Ontkracht\] |
| **Adoptie**    | \[Bijv. Gebruikers vertrouwen de output\]               | \[Hoog/Gemiddeld/Laag\] | \[Welk bewijs is er?\] | \[Open / Gevalideerd / Ontkracht\] |
| **Kosten**     | \[Bijv. Gebruikskosten blijven beheersbaar bij schaal\] | \[Hoog/Gemiddeld/Laag\] | \[Welk bewijs is er?\] | \[Open / Gevalideerd / Ontkracht\] |
| **Ethiek**     | \[Bijv. Trainingsdata bevat geen systematische bias\]   | \[Hoog/Gemiddeld/Laag\] | \[Welk bewijs is er?\] | \[Open / Gevalideerd / Ontkracht\] |
| **Regulering** | \[Bijv. Aanpak blijft compliant met EU AI Act\]         | \[Hoog/Gemiddeld/Laag\] | \[Welk bewijs is er?\] | \[Open / Gevalideerd / Ontkracht\] |

- **Riskantste aanname:** \[Welke aanname doodt het project als deze niet klopt?\]
- **Validatieaanpak:** \[Hoe gaan we deze testen? Verwijs naar een Experiment Ticket indien nodig.\]
- **Eigenaar:** \[Wie is verantwoordelijk voor het valideren van de kritieke aannames?\]
- **Herbeoordelingsdatum:** \[Wanneer worden de aannames opnieuw getoetst?\]

______________________________________________________________________

### F. Green AI & Duurzaamheid

*Hoe beperken we de ecologische voetafdruk van dit systeem?*

- **Is AI proportioneel?** Weegt de waardecreatie op tegen de energiekost? \[Ja / Nee / Toelichting\]
- **Kleiner model mogelijk?** Kan een kleiner, gespecialiseerd model de taak uitvoeren? \[Ja / Nee / Motivatie\]
- **Groene infrastructuur?** Draait het systeem op een cloudprovider met hernieuwbare energie? \[Provider + certificering\]
- **E-waste plan?** Is er een plan voor hardware-lifecycle en vervanging? \[Ja / Nee / Verwijzing\]

Zie: [Green AI & Duurzaamheid](../../08-technische-standaarden/08-green-ai.md)

______________________________________________________________________

### Goedkeuring door Guardian

**Naam:** \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]

______________________________________________________________________
