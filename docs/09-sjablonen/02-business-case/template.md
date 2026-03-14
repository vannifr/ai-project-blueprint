---
versie: '1.0'
type: template
layer: 3
phase: [2]
roles: [AI Product Manager, Business Sponsor]
tags: [template]
---

# 1. Sjabloon: Business Case & Het Kostenoverzicht

## 1. Doel

Dit sjabloon helpt bij het kwantificeren van de businesswaarde en het in kaart brengen van de totale exploitatiekosten van een AI-oplossing.

______________________________________________________________________

### Waarde-Hypothese

*Wat is de verwachte winst?*

- **Efficiëntiewinst:** \[Bijv. Aantal uur besparing per maand.\]
- **Kwaliteitsverbetering:** \[Bijv. Reductie in foutpercentage.\]
- **Omzetgroei:** \[Bijv. Hogere conversie door personalisatie.\]

______________________________________________________________________

### Het Kostenoverzicht (TCO)

*Wat zijn de totale kosten voor ontwikkeling en beheer?*

- **Investering (Capex):**
- Uren team (Project Management, Data Science, Engineering).
- Initiële data-acquisitie of tooling.
- **Gebruikskosten (Opex):**
- API / Token kosten per maand.
- Compute / Hosting (Cloud).
- Onderhoud & Monitoring door team.

______________________________________________________________________

### ROI & Terugverdientijd

- **Netto opbrengst:** \[Waarde - Kosten\].
- **Terugverdientijd:** \[Maanden tot break-even\].

______________________________________________________________________

## Ecologische Voetafdruk

> **Verplicht veld** voor alle systemen met continue inferentie of schaalbare uitrol.

| Aspect                        | Schatting / Toelichting                                  |
| :---------------------------- | :------------------------------------------------------- |
| Inferentie-intensiteit        | \[Laag / Middel / Hoog — aantal calls/dag + model-type\] |
| CO₂-schatting inferentie      | \[kg CO₂eq/maand — gebruik provider dashboard of tool\]  |
| Trainingskosten (indien nvt.) | \[Niet van toepassing / kg CO₂eq eenmalig\]              |
| Vergelijking met baseline     | \[Huidig proces vs. AI-systeem — netto impact\]          |
| Optimalisatiemaatregelen      | \[Bijv. model-quantisatie, batch-inferentie, caching\]   |

!!! info "Richtlijn Green AI"
    Raadpleeg de [Green AI-standaard](../../08-technische-standaarden/index.md) voor rekentools en drempelwaarden. Bij systemen met >1.000 calls/dag is een gedetailleerde berekening verplicht.

______________________________________________________________________
