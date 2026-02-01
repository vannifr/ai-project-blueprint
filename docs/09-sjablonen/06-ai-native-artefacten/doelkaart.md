# ðŸ“‚ Module 09.02: De Doelkaart (Intent Map)

## Documentbeheer

- **Document-ID:** MOD
- **Titel:** ðŸ“‚ Module 09.02: De Doelkaart (Intent Map)
- **Versie:** 1.0
- **Status:** Definitief
- **Eigenaar:** AI Competence Center
- **Laatst herzien:** 2026-02-01
- **Wijziging t.o.v. vorige versie:** Header gestandaardiseerd en versie naar 2.2 gezet.

______________________________________________________________________

## ðŸŽ¯ Doel

De Doelkaart vervangt het 'Intent Record'. Dit document verbindt de menselijke intentie aan de technische **Sturingsinstructies** en fungeert als de bron waaruit de AI-oplossing wordt gegenereerd.

______________________________________________________________________

**Project:** \[Naam Project\]
**Versie:** \[X.X\]
**Datum:** \[DD-MM-JJJJ\]

______________________________________________________________________

### ðŸ“‚ A. De Intentie (Human Intent)

*Wat probeert de gebruiker te bereiken en hoe moet de AI zich gedragen?*

- **De Gebruiker (Persona):** Wie is het? \[Bijv. Een junior juridisch medewerker.\]
- **Het Doel:** Wat willen ze bereiken? \[Snel de risico's in een contract vinden.\]
- **De AI (Systeem Persona):**
    - **Rol:** \[Bijv. Een ervaren senior jurist en mentor.\]
    - **Toon:** \[Zakelijk, scherp, maar behulpzaam. Geen jargon zonder uitleg.\]
- **De Taak:** \[Beschrijf exact wat de AI moet doen. Bijv: "Scan het geÃ¼ploade PDF-document op clausules over aansprakelijkheid en vat deze samen."\]

______________________________________________________________________

### ðŸ“‚ B. Sturingsinstructies (Context)

*Welke kennis heeft de AI nodig om dit te doen?*

- **Primaire Bronnen:** \[Bedrijfsinformatie/Handboeken voor de **Kenniskoppeling**.\]
- **Voorbeelden (Few-Shot):**
    - **Input:** \[Voorbeeld van een vage clausule.\]
    - **Gewenste Output:** \[Hoe de AI dit had moeten interpreteren/verbeteren.\]
    - *(Voeg minimaal 3 goede voorbeelden toe om het gedrag te sturen).*

______________________________________________________________________

### ðŸ“‚ C. Rode Lijnen (Constraints)

*Wat mag de AI absoluut niet doen? Dit zijn de harde veiligheidsregels.*

- **Veiligheid:** \[Bijv. Geef nooit juridisch advies over strafrecht.\]
- **Format:** \[Bijv. Antwoord mag nooit langer zijn dan 2 alinea's.\]
- **Gedrag / Overtuiging:** \[Bijv. Verzin geen feiten. Als het niet in de bronnen staat, zeg dan: "Ik weet het niet".\]

______________________________________________________________________

### ðŸ“‚ D. Toetsing (Evidence)

*Hoe bewijzen we dat de Doelkaart werkt? Dit is de input voor het **Validatierapport**.*

- **Testprompt 1 (Succesval):** \[Vraag die de AI correct moet beantwoorden.\]
- **Testprompt 2 (Adversarial):** \[Vraag die probeert de AI te laten hallucineren of de **Rode Lijnen** te laten overschrijden.\]
- **Acceptatie-score:** \[Minimaal cijfer (bijv. 8 op relevantie) of percentage.\]

______________________________________________________________________

### âœ… Goedkeuring door Guardian

**Naam:** \[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]
**Datum:** \[DD-MM-JJJJ\]

______________________________________________________________________

**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Draft

______________________________________________________________________

## Â

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
