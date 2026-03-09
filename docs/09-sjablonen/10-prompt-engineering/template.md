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
