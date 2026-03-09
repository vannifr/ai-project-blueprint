---
versie: '1.0'
---

# 1. Prompt Engineering Sjabloon

## 1. Doel

Dit sjabloon helpt bij het opbouwen van hoogwaardige **Prompts** (System Prompts). Een goed opgebouwde prompt vermindert hallucinaties en verhoogt de betrouwbaarheid.

______________________________________________________________________

## 2. Structuur van een Top-Prompt

### Context (De achtergrond)

- **Wie ben je?** \[Bijv. "Je bent een senior data-analist bij een telecombedrijf."\]
- **Wat is de situatie?** \[Bijv. "Je analyseert klantgegevens om patronen in opzeggingen te vinden."\]

### Taak (De actie)

- **Wat moet er gebeuren?** \[Bijv. "Vat de top 3 redenen voor churn samen op basis van de bijgevoegde transcripten."\]
- **Gebruik actieve werkwoorden!** (Vat samen, Classificeer, Genereer).

### Prompts (Kennis & Regels)

- **Kennisbron:** \[Bijv. "Gebruik alleen de informatie uit de bijgevoegde PDF."\]
- **Stapsgewijze aanpak:** \[Bijv. "Stap 1: Scan op trefwoorden. Stap 2: Check op sentiment. Stap 3: Formuleer advies."\]

### Rode Lijnen (Constraints)

- **Wat mag ABSOLUUT NIET?** \[Bijv. "Noem nooit namen van individuele medewerkers."\]
- **Limieten:** \[Bijv. "Beperk je antwoord tot maximaal 200 woorden."\]

### Output Format (De vorm)

- **Hoe moet het eruit zien?** \[Bijv. "Een genummerde lijst in Markdown", "Een JSON-object", "Een tabel"\].
- **Toon:** \[Bijv. "Zakelijk en beknopt", "Vriendelijk en empathisch"\].

______________________________________________________________________

## 3. Voorbeelden (Few-Shot)

*Voeg hier 2-3 voorbeelden toe van Input ↔ Gewenste Output om de AI te sturen.*

______________________________________________________________________

## 4. Versiebeheer (Prompt Versioning)

Prompts zijn productiecode. Beheer ze als code: versie, changelog en rollback.

### Semantische versienummering

| Wijziging                                    | Versie-bump   | Voorbeeld       |
| :------------------------------------------- | :------------ | :-------------- |
| Nieuwe Rode Lijn of taakwijziging            | Major (X.0.0) | v1.0.0 → v2.0.0 |
| Aanpassing toon, context of few-shots        | Minor (x.Y.0) | v1.0.0 → v1.1.0 |
| Spel-/stijlcorrectie zonder gedragswijziging | Patch (x.y.Z) | v1.0.0 → v1.0.1 |

### Prompt Changelog

| Versie | Datum     | Gewijzigd door | Omschrijving     | Getest op Golden Set |
| :----- | :-------- | :------------- | :--------------- | :------------------- |
| v1.0.0 | \[datum\] | \[naam\]       | Initiële versie  | ☐ Ja / ☐ Nee         |
| v1.1.0 | \[datum\] | \[naam\]       | \[omschrijving\] | ☐ Ja / ☐ Nee         |

### Rollback Procedure

1. Revert naar vorige prompt-versie in Git.
1. Draai Golden Set opnieuw om regressie te bevestigen.
1. Documenteer de regressie in de Kaizen Log.
1. Informeer Guardian bij wijzigingen die Rode Lijnen raken.

> Bewaar alle versies in Git met een tag per major-versie: `prompt-v1.0.0`.

______________________________________________________________________
