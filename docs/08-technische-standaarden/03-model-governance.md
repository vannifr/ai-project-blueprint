---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 3.2.3 Model Governance

## 3.2.3.1 Doel

Deze module definieert hoe wij AI-modellen beheren gedurende hun levenscyclus: van ontwikkeling tot productie en uiteindelijke uitfasering. Goede model governance zorgt voor traceerbaarheid, controleerbaarheid en veilige releases.

______________________________________________________________________

## 3.2.3.2 Kernprincipes

### 3.2.3.2.1 Elk Model Heeft Een Eigenaar

- Elke AI-oplossing heeft één aangewezen **Tech Lead** die verantwoordelijk is voor de technische kwaliteit.
- De eigenaar is aanspreekpunt voor incidenten, updates en decommissioning.

### 3.2.3.2.2 Alles Is Versiebeheerd

- Modelgewichten, configuraties en Sturingsinstructies staan in versiebeheer.
- Wijzigingen zijn traceerbaar: wie heeft wat wanneer aangepast?

### 3.2.3.2.3 Geen Wijziging Zonder Review

- Wijzigingen aan productiemodellen vereisen review door ten minste één andere teamlid.
- Bij Hoog Risico: Guardian review verplicht.

______________________________________________________________________

## 3.2.3.3 Model Registry

Een centrale plek waar alle modellen zijn geregistreerd met hun metadata.

### 3.2.3.3.1 Minimale Metadata per Model

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

### 3.2.3.3.2 Implementatie-opties

| Optie                     | Geschikt voor                    | Complexiteit |
| ------------------------- | -------------------------------- | ------------ |
| Spreadsheet/Wiki          | Startende teams, weinig modellen | Laag         |
| Git repository met YAML   | Engineering teams                | Midden       |
| MLflow / Weights & Biases | Mature MLOps, veel modellen      | Hoog         |

______________________________________________________________________

## 3.2.3.4 Goedkeuringsworkflow

### 3.2.3.4.1 Standaard Flow (Beperkt Risico)

```
[Development] → [Code Review] → [Staging Test] → [Gate Review] → [Production]
```

- **Code Review:** Ten minste één peer review
- **Staging Test:** Gouden Set test op staging-omgeving
- **Gate Review:** Validatierapport voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)

### 3.2.3.4.2 Uitgebreide Flow (Hoog Risico)

```
[Development] → [Code Review] → [Guardian Review] → [Staging Test] → [Eerlijkheidstoets] → [Gate Review] → [Gefaseerde Uitrol] → [Production]
```

- **Guardian Review:** Onafhankelijke toetsing op Rode Lijnen
- **Eerlijkheidstoets:** Kwantitatieve bias-analyse
- **Gefaseerde Uitrol:** Start met beperkte gebruikersgroep, monitor, dan volledige uitrol

______________________________________________________________________

## 3.2.3.5 Modellevenscyclus

| Fase        | Kenmerken                   | Acties                                      |
| ----------- | --------------------------- | ------------------------------------------- |
| Development | Experimenten, prototypes    | Geen productiedata, geen externe gebruikers |
| Staging     | Kandidaat voor productie    | Volledige Gouden Set test, review           |
| Production  | Live, wordt actief gebruikt | Monitoring, incidentprocedure actief        |
| Deprecated  | Wordt uitgefaseerd          | Geen nieuwe gebruikers, migratieplan actief |
| Retired     | Niet meer beschikbaar       | Archivering, documentatie bewaard           |

______________________________________________________________________

## 3.2.3.6 Wijzigingsbeheer

### 3.2.3.6.1 Typen Wijzigingen

| Type                    | Voorbeeld                              | Vereiste Goedkeuring          |
| ----------------------- | -------------------------------------- | ----------------------------- |
| Configuratie-aanpassing | Temperatuur van 0.7 naar 0.5           | Peer review                   |
| Prompt-wijziging        | Instructie herschrijven                | Peer review + regressietest   |
| Modelversie-update      | Nieuw basismodel (bijv. GPT-4 → GPT-5) | Volledige Gate Review         |
| Databron-wijziging      | Nieuwe kennisbank koppelen             | Guardian review (Hoog Risico) |

### 3.2.3.6.2 Rollback Procedure

- Elke productierelease heeft een gedocumenteerd rollback plan.
- Rollback moet binnen 30 minuten uitvoerbaar zijn.
- Na rollback: incident-analyse en documentatie.

______________________________________________________________________

## 3.2.3.7 Checklist Model Governance

- [ ] Model registry is ingericht en up-to-date
- [ ] Alle productiemodellen hebben een eigenaar
- [ ] Goedkeuringsworkflow is gedocumenteerd en wordt gevolgd
- [ ] Wijzigingsbeheer is ingericht met rollback-procedure
- [ ] Modellen zijn gekoppeld aan Validatierapporten

______________________________________________________________________

## 3.2.3.8 Gerelateerde Modules

- [Technische Standaarden & Leveringscriteria](01-mloops-standaarden.md)
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
- [Risicobeheersing & Compliance](../07-compliance-hub/index.md)
