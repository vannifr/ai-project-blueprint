# Ethische Richtlijnen voor AI-Projecten

## Doel
Het doel van deze richtlijnen is het waarborgen van verantwoorde en mensgerichte AI-ontwikkeling. We gaan verder dan juridische compliance; we streven naar systemen die eerlijk, transparant en uitlegbaar zijn.

## Kernprincipes

### 1. Rechtvaardigheid & Bias-Preventie (*Fairness*)
AI mag geen discriminatie versterken of introduceren.
*   **Actie:** Test datasets en modeloutputs op ongewenste vooroordelen ten aanzien van geslacht, leeftijd, etniciteit of andere beschermde kenmerken.
*   **Check:** Is de data representatief voor de eindgebruiker?

### 2. Transparantie & Uitlegbaarheid (*Explainability*)
Gebruikers hebben het recht om te begrijpen hoe een AI-besluit tot stand is gekomen.
*   **Actie:** Gebruik technieken (zoals SHAP of LIME) of kies voor interpreteerbare modellen waar mogelijk.
*   **Check:** Kan een domeinexpert de reden achter een output verklaren?

### 3. Menselijk Toezicht (*Human Agency & Oversight*)
De mens moet de uiteindelijke controle behouden (zie [HAS H Niveaus](../../00-strategisch-kader/06-has-h-niveaus.md)).
*   **Actie:** Implementeer 'Human-in-the-Loop' (HITL) voor kritieke beslissingen en voorzie een 'kill switch'.
*   **Check:** Kan de gebruiker een AI-besluit overrulen?

### 4. Privacy & Data Souvereiniteit
Respecteer de privacy van individuen en voldoe aan de GDPR.
*   **Actie:** Gebruik technieken als anonimisering en *Privacy-Enhancing Technologies* (PETs).
*   **Check:** Is alleen de noodzakelijke data gebruikt (*data minimization*)?

### 5. Veiligheid & Robuustheid
Het systeem moet bestand zijn tegen invloeden van buitenaf en onverwachte situaties.
*   **Actie:** Voer *adversarial testing* uit en test op randgevallen (*boundary cases*).
*   **Check:** Wat gebeurt er als de input opzettelijk misleidend is?

## Implementatie in het Project
Ethische checks zijn geen eenmalige gebeurtenis, maar een integraal onderdeel van elke fase:
*   **Discovery:** Bias-check op ruwe data.
*   **Validatie:** Toetsing van het prototype door een Ethicus.
*   **Ontwikkeling:** Continue geautomatiseerde bias-testing.
*   **Monitoring:** Rapportage over ongewenst gedrag in productie.

---

© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.

