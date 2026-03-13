---
versie: '1.0'
description: "AI risico-inventarisatie sjabloon: systematisch technische, ethische en compliancerisico's identificeren, classificeren en mitigeren — gebaseerd op EU AI Act risicocategorieën."
---

# 1. Sjabloon: Risico-Inventarisatie

## 1. Doel

Het identificeren en beoordelen van risico's op het gebied van techniek, organisatie en compliance (EU AI Act).

______________________________________________________________________

### Risicoclassificatie

*Kies de categorie conform de EU AI Act:*

- [ ] **Onacceptabel:** (VERBODEN)
- [ ] **Hoog Risico:** (Vereist technisch dossier & menselijk toezicht)
- [ ] **Beperkt Risico:** (Transparantieplicht)
- [ ] **Minimaal Risico:** (Geen specifieke eisen)

______________________________________________________________________

### Toetsing op Rode Lijnen

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
