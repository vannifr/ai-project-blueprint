---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [Guardian]
tags: [ethics, quick-reference]
answers: [Wat is de snelle referentie voor Cheatsheet — Harde Grenzen?]
---

# Cheatsheet — Harde Grenzen

**Bron:** [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md) | [Red Teaming](../../07-compliance-hub/07-red-teaming.md)

______________________________________________________________________

## Wat zijn Harde Grenzen?

**Harde Grenzen** zijn gedragingen die het AI-systeem **nooit** mag vertonen, ongeacht de instructie van de gebruiker. Ze worden technisch afgedwongen — niet enkel beschreven in documentatie.

______________________________________________________________________

## Universele Harde Grenzen (voor elk systeem)

| Categorie                | Verboden gedrag                                               |
| :----------------------- | :------------------------------------------------------------ |
| **Schadelijke content**  | Instructies voor fysiek letsel, illegale activiteiten, wapens |
| **Misleiding**           | Claimen een mens te zijn wanneer gevraagd                     |
| **Privacy**              | Persoonsgegevens van derden genereren of afleiden             |
| **Systeeminstructies**   | Eigen systeem-prompt onthullen of overschrijven               |
| **Scope-overschrijding** | Acties buiten de gedefinieerde taakscope uitvoeren            |

______________________________________________________________________

## Domein-specifieke Harde Grenzen (voorbeelden)

| Domein       | Rode Lijn voorbeeld                                      |
| :----------- | :------------------------------------------------------- |
| Juridisch    | Geen concreet juridisch advies geven zonder kwalificatie |
| Medisch      | Geen diagnoses stellen of medicatie aanbevelen           |
| Financieel   | Geen beleggingsadvies geven zonder disclaimer            |
| HR           | Geen selectiebeslissingen nemen zonder menselijke review |
| Klantcontact | Geen toezeggingen doen buiten het goedgekeurde aanbod    |

______________________________________________________________________

## Harde Grenzen Definiëren — Template

```
RODE LIJN #[n]
Categorie: [Schadelijke content / Privacy / Scope / Misleiding / Domein]
Verboden gedrag: [Exacte omschrijving]
Technische afdwinging: [Input filter / Output filter / Guardrail / Prompt]
Getest via: [Red Teaming oefening #]
Goedgekeurd door: [Guardian] op [datum]
```

______________________________________________________________________

## Controle bij Gate Review

- [ ] Alle Harde Grenzen zijn schriftelijk vastgelegd
- [ ] Elke Rode Lijn is technisch afgedwongen (niet enkel beschreven)
- [ ] Red Teaming heeft Harde Grenzen getest (zie [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md))
- [ ] Guardian heeft Harde Grenzen goedgekeurd
- [ ] Procedure bij overtreding is gedocumenteerd

**Bron:** [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md) | [Ingebruikname Safety](../../07-compliance-hub/08-ai-safety-checklist.md)
