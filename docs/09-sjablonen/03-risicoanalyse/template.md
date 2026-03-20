---
versie: '1.0'
description: "AI risico-inventarisatie sjabloon: systematisch technische, ethische en compliancerisico's identificeren, classificeren en mitigeren — gebaseerd op EU AI Act risicocategorieën."
type: template
layer: 3
phase: [1, 2]
roles: [Guardian]
tags: [risk, template]
answers: ['Hoe gebruik ik het Sjabloon: Risico-Inventarisatie sjabloon?']
---

# 1. Sjabloon: Risico-Inventarisatie

## 1. Doel

Het identificeren en beoordelen van risico's op het gebied van techniek, organisatie en compliance (EU AI Act).

______________________________________________________________________

!!! note "Download dit sjabloon"
    [Download als Markdown](https://github.com/vannifr/ai-project-blueprint/raw/main/docs/09-sjablonen/03-risicoanalyse/template.md){ .md-button } — Open in je editor of AI-assistent en vul de velden in.

### Risicoclassificatie

*Kies de categorie conform de EU AI Act:*

- [ ] **Onacceptabel:** (VERBODEN)
- [ ] **Hoog Risico:** (Vereist technisch dossier & menselijk toezicht)
- [ ] **Beperkt Risico:** (Transparantieplicht)
- [ ] **Minimaal Risico:** (Geen specifieke eisen)

______________________________________________________________________

### Toetsing op Harde Grenzen

*Welke harde grenzen mogen niet worden overschreden?*

1. **Privacy:** \[Risico op lekken van PII\].
1. **Veiligheid:** \[Risico op schadelijke outputs\].
1. **Bias:** \[Risico op ongelijke behandeling\].

______________________________________________________________________

### Mitigatieplan

*Hoe verlagen we de risico's naar een acceptabel niveau?*

- **Technisch:** \[Bijv. Filters op output, anonimiseren van input\].
- **Procedureel:** \[Bijv. De Guardian voert steekproeven uit\].

______________________________________________________________________

### Duurzaamheidstrigger

- [ ] **Schaaltrigger:** Vereist het systeem continue inferentie op grote schaal (>1.000 calls/dag)?
    - Ja → verwijs naar [Green AI-standaard](../../08-technische-standaarden/index.md) en vul het Ecologische Voetafdruk-veld in de Business Case verplicht in.
    - Nee → geen aanvullende actie vereist.

______________________________________________________________________
