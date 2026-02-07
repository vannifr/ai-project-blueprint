---
versie: '1.0'
---

# 1. Model Governance

## 1. Doel

Deze module definieert hoe wij AI-modellen beheren gedurende hun levenscyclus: van ontwikkeling tot productie en uiteindelijke uitfasering. Goede model governance zorgt voor traceerbaarheid, controleerbaarheid en veilige releases.

______________________________________________________________________

## 2. Kernprincipes

### Elk Model Heeft Een Eigenaar

- Elke AI-oplossing heeft één aangewezen **Tech Lead** die verantwoordelijk is voor de technische kwaliteit.
- De eigenaar is aanspreekpunt voor incidenten, updates en decommissioning.

### Alles Is Versiebeheerd

- Modelgewichten, configuraties en Sturingsinstructies staan in versiebeheer.
- Wijzigingen zijn traceerbaar: wie heeft wat wanneer aangepast?

### Geen Wijziging Zonder Review

- Wijzigingen aan productiemodellen vereisen review door ten minste één andere teamlid.
- Bij Hoog Risico: Guardian review verplicht.

______________________________________________________________________

## 3. Model Registry

Een centrale plek waar alle modellen zijn geregistreerd met hun metadata.

### Minimale Metadata per Model

| Veld                | Beschrijving                                    | Voorbeeld                   |
| ------------------- | ----------------------------------------------- | --------------------------- |
| Model ID            | Unieke identificatie                            | `invoice-classifier-v2.1`   |
| Versie              | Semantische versie of hash                      | `2.1.0` of `abc123`         |
| Status              | Development / Staging / Production / Deprecated | Production                  |
| Eigenaar            | Verantwoordelijke persoon/team                  | Team Finance AI             |
| Aanmaakdatum        | Wanneer getraind/gedeployed                     | 2026-01-15                  |
| Databron versie     | Welke data gebruikt voor training               | `invoices-2025-q4`          |
| Sturingsinstructies | Link naar prompt/config versie                  | `prompts/invoice-v2.1.yaml` |
| Validatierapport    | Link naar bijbehorend bewijs                    | `reports/invoice-v2.1.md`   |
| Risiconiveau        | Classificatie conform EU AI Act                 | Beperkt                     |

### Implementatie-opties

| Optie                     | Geschikt voor                    | Complexiteit |
| ------------------------- | -------------------------------- | ------------ |
| Spreadsheet/Wiki          | Startende teams, weinig modellen | Laag         |
| Git repository met YAML   | Engineering teams                | Midden       |
| MLflow / Weights & Biases | Mature MLOps, veel modellen      | Hoog         |

______________________________________________________________________

## 4. Goedkeuringsworkflow

### Standaard Flow (Beperkt Risico)

```
[Development] → [Code Review] → [Staging Test] → [Gate Review] → [Production]
```

- **Code Review:** Ten minste één peer review
- **Staging Test:** Gouden Set test op staging-omgeving
- **Gate Review:** Validatierapport voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)

### Uitgebreide Flow (Hoog Risico)

```
[Development] → [Code Review] → [Guardian Review] → [Staging Test] → [Eerlijkheidstoets] → [Gate Review] → [Gefaseerde Uitrol] → [Production]
```

- **Guardian Review:** Onafhankelijke toetsing op Rode Lijnen
- **Eerlijkheidstoets:** Kwantitatieve bias-analyse
- **Gefaseerde Uitrol:** Start met beperkte gebruikersgroep, monitor, dan volledige uitrol

______________________________________________________________________

## 5. Modellevenscyclus

| Fase        | Kenmerken                   | Acties                                      |
| ----------- | --------------------------- | ------------------------------------------- |
| Development | Experimenten, prototypes    | Geen productiedata, geen externe gebruikers |
| Staging     | Kandidaat voor productie    | Volledige Gouden Set test, review           |
| Production  | Live, wordt actief gebruikt | Monitoring, incidentprocedure actief        |
| Deprecated  | Wordt uitgefaseerd          | Geen nieuwe gebruikers, migratieplan actief |
| Retired     | Niet meer beschikbaar       | Archivering, documentatie bewaard           |

______________________________________________________________________

## 6. Wijzigingsbeheer

### Typen Wijzigingen

| Type                    | Voorbeeld                              | Vereiste Goedkeuring          |
| ----------------------- | -------------------------------------- | ----------------------------- |
| Configuratie-aanpassing | Temperatuur van 0.7 naar 0.5           | Peer review                   |
| Prompt-wijziging        | Instructie herschrijven                | Peer review + regressietest   |
| Modelversie-update      | Nieuw basismodel (bijv. GPT-4 → GPT-5) | Volledige Gate Review         |
| Databron-wijziging      | Nieuwe kennisbank koppelen             | Guardian review (Hoog Risico) |

### Rollback Procedure

- Elke productierelease heeft een gedocumenteerd rollback plan.
- Rollback moet binnen 30 minuten uitvoerbaar zijn.
- Na rollback: incident-analyse en documentatie.

______________________________________________________________________

## 7. Checklist Model Governance

!!! check "Model Governance Checklist"
    - [ ] Model registry is ingericht en up-to-date
    - [ ] Alle productiemodellen hebben een eigenaar
    - [ ] Goedkeuringsworkflow is gedocumenteerd en wordt gevolgd
    - [ ] Wijzigingsbeheer is ingericht met rollback-procedure
    - [ ] Modellen zijn gekoppeld aan Validatierapporten

______________________________________________________________________

## 8. Gerelateerde Modules

- [Technische Standaarden & Leveringscriteria](01-mloops-standaarden.md)
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Risicobeheersing & Compliance](../07-compliance-hub/index.md)
