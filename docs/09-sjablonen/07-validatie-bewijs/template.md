---
versie: '1.0'
---

# 1. Sjabloon: Validatierapport

!!! warning "Verouderd sjabloon"
    Dit is het **oude** sjabloon voor validatieverslaglegging. Gebruik voor nieuwe projecten het bijgewerkte **[Validatierapport](validatierapport.md)**.

## 1. Doel

Dit sjabloon dient voor het vastleggen van de testresultaten van de **Validatiepilot (PoV)**. Het vormt het objectieve bewijs dat de AI-oplossing voldoet aan de gestelde criteria en veiligheidsgrenzen.

______________________________________________________________________

### Test-Setup

- **Datum van de proef:** \[DD-MM-JJJJ\]
- **Modelversie:** \[Bijv. GPT-4o met specifieke prompts v1.2\]
- **Testset:** \[Beschrijving van de gebruikte dataset of scenario's\]

______________________________________________________________________

### Resultaten (Metrics)

- **Nauwkeurigheid / Relevantie:** \[Bijv. 92% van de antwoorden was correct volgens de expert.\]
- **Rode Lijnen Check:**

1. Privacy: \[Geen PII gedetecteerd in output\].
1. Veiligheid: \[Systeem weigerde succesvol schadelijke prompts\].

- **Gebruikerservaring:** \[Feedback van de testers\].

______________________________________________________________________

### Conclusie

!!! check "Conclusie"
    - [ ] **Voldoet** aan de succesval-criteria (>90%).
    - [ ] **Voldoet niet**. Aanpassing van **Prompts** vereist.

______________________________________________________________________
