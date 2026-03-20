---
versie: '1.0'
type: technical
layer: 3
roles: [AI Product Manager, Data Scientist, Guardian]
tags: [data, governance]
summary: Raamwerk voor datakwaliteit, data lineage, data contracts en metadata management in AI-projecten.
answers: [Hoe borg ik datakwaliteit in een AI-project?, Wat zijn data contracts?, Hoe track ik data lineage?]
---

# Data Governance

!!! abstract "Doel"
    Slechte data is de belangrijkste oorzaak van falende AI-projecten. Deze module biedt een concreet raamwerk voor datakwaliteit, data lineage, data contracts en metadata management — zodat je AI-systeem op een betrouwbare datafundament rust.

!!! tip "Wanneer gebruik je dit?"
    Vanaf de Verkenningsfase (Fase 1) bij de Data-Evaluatie. Data governance is geen eenmalige activiteit: het loopt door alle fasen heen. Start vroeg, bouw incrementeel op.

______________________________________________________________________

## 1. Datakwaliteit Raamwerk

Datakwaliteit wordt gemeten langs zes dimensies. Definieer per dimensie concrete drempelwaarden die passen bij het risiconiveau van het project.

| Dimensie           | Definitie                                                     | Meetmethode                                                   | Voorbeeld drempelwaarde                                   |
| :----------------- | :------------------------------------------------------------ | :------------------------------------------------------------ | :-------------------------------------------------------- |
| **Volledigheid**   | Alle verwachte records en velden zijn aanwezig                | `(records met waarde / totaal verwachte records) × 100%`      | ≥ 95% voor kritieke velden                                |
| **Nauwkeurigheid** | Waarden komen overeen met de werkelijkheid                    | Vergelijking met betrouwbare bronnen of handmatige steekproef | ≥ 98% bij steekproef van 200 records                      |
| **Consistentie**   | Dezelfde feiten zijn gelijk gerepresenteerd in alle systemen  | Cross-system vergelijkingen, business rule checks             | 0 conflicten in primaire sleutels                         |
| **Tijdigheid**     | Data is beschikbaar binnen de vereiste doorlooptijd           | Meting van ingestie-latency                                   | ≤ 4 uur voor dagelijkse batch; ≤ 5 min voor near-realtime |
| **Uniciteit**      | Geen ongewenste duplicaten                                    | Deduplicatie-analyse op unieke sleutels                       | ≤ 0,1% duplicaten                                         |
| **Geldigheid**     | Waarden voldoen aan het gedefinieerde formaat en domeinregels | Schema-validatie, regex, domeinlijsten                        | 100% van records past het schema                          |

!!! warning "Drempelwaarden zijn projectspecifiek"
    De voorbeelddrempels hierboven zijn startpunten. Pas ze aan op basis van het risiconiveau: een hoog-risico systeem (EU AI Act) vereist strengere drempels dan een intern dashboard.

______________________________________________________________________

## 2. Data Lineage & Provenance

### Wat is data lineage?

Data lineage is de volledige beschrijving van de herkomst, transformaties en bewegingen van data — van bron tot model-input en uiteindelijk model-output.

### Waarom is het belangrijk?

- **Traceerbaarheid:** Bij onverwachte modelresultaten kun je snel achterhalen welke data de oorzaak is.
- **Debugging:** Identificeer exact waar in de pipeline een datafout is geintroduceerd.
- **Compliance:** De EU AI Act vereist voor hoog-risico systemen dat de herkomst van trainingsdata aantoonbaar is.
- **Reproduceerbaarheid:** Zonder lineage kun je experimenten niet betrouwbaar herhalen.

### Hoe implementeren?

**Minimale vereisten:**

- [ ] Elke dataset heeft een unieke identifier en versienummer
- [ ] Transformatiestappen zijn vastgelegd met input-versie, output-versie en timestamp
- [ ] Metadata tags bevatten: bron, eigenaar, verwerkingsdatum, kwaliteitsscore

**Tooling opties:**

| Categorie    | Voorbeelden                                | Geschikt voor                 |
| :----------- | :----------------------------------------- | :---------------------------- |
| Lichtgewicht | dbt lineage graph, handmatige documentatie | Kleine teams, L0-L1           |
| Middenklasse | Apache Atlas, DataHub, OpenLineage         | Groeiende organisaties, L1-L2 |
| Enterprise   | Collibra, Alation, Purview                 | Grote organisaties, L2-L3     |

**Minimale vereisten per risiconiveau:**

| Risiconiveau   | Lineage vereiste                                                  |
| :------------- | :---------------------------------------------------------------- |
| Laag risico    | Documentatie van bronnen en hoofdtransformaties                   |
| Beperkt risico | Geautomatiseerde lineage tracking, traceerbaarheid tot bronniveau |
| Hoog risico    | Volledige end-to-end lineage met audit trail, onwijzigbare logs   |

______________________________________________________________________

## 3. Data Contracts

### Wat zijn data contracts?

Een data contract is een formele afspraak tussen een data producer (het team dat data levert) en een data consumer (het team dat data gebruikt). Het voorkomt dat wijzigingen in upstream data onverwacht je AI-pipeline breken.

### Componenten van een data contract

| Component              | Beschrijving                                                | Voorbeeld                                                     |
| :--------------------- | :---------------------------------------------------------- | :------------------------------------------------------------ |
| **Schema**             | Verwachte velden, datatypes, nullable regels                | `klant_id: INT NOT NULL, naam: VARCHAR(255)`                  |
| **SLA**                | Beschikbaarheid, verversingsfrequentie, maximale latency    | Dagelijks vóór 06:00 UTC, 99,5% uptime                        |
| **Eigenaarschap**      | Wie is verantwoordelijk voor de data?                       | Team Klantenservice (producer), Team ML (consumer)            |
| **Kwaliteitsregels**   | Minimale kwaliteitseisen waar de producer garant voor staat | Volledigheid ≥ 98%, geen duplicaten op `klant_id`             |
| **Wijzigingsbeleid**   | Hoe worden schemawijzigingen gecommuniceerd?                | Minimaal 2 sprints vooraankondiging, breaking changes via RFC |
| **Escalatieprocedure** | Wat gebeurt er als het contract wordt geschonden?           | Alert naar consumer, incident binnen 4 uur opgepakt           |

### Voorbeeld contract template

```yaml
# Data Contract — [Dataset Naam]
contract_versie: "1.0"
producer:
  team: "Team Klantenservice"
  contactpersoon: "naam@organisatie.nl"
consumer:
  team: "Team ML Platform"
  contactpersoon: "naam@organisatie.nl"
dataset:
  naam: "klant_interacties"
  formaat: "parquet"
  locatie: "s3://data-lake/klant_interacties/"
schema:
  - veld: "klant_id"
    type: "INT"
    nullable: false
  - veld: "interactie_datum"
    type: "DATE"
    nullable: false
  - veld: "kanaal"
    type: "VARCHAR(50)"
    nullable: false
    toegestane_waarden: ["email", "telefoon", "chat", "portal"]
sla:
  verversing: "dagelijks vóór 06:00 UTC"
  beschikbaarheid: "99.5%"
kwaliteitsregels:
  volledigheid: "≥ 98%"
  uniciteit_op: "klant_id + interactie_datum"
wijzigingsbeleid: "Breaking changes: minimaal 2 sprints vooraankondiging via RFC"
```

______________________________________________________________________

## 4. Data Versioning

### Waarom?

Zonder dataversioning kun je niet garanderen dat een modeltraining reproduceerbaar is. Als de trainingsdata verandert zonder versieregistratie, is debugging en auditing onmogelijk.

### Aanpak

| Methode                             | Beschrijving                                                                          | Wanneer gebruiken                                           |
| :---------------------------------- | :------------------------------------------------------------------------------------ | :---------------------------------------------------------- |
| **DVC (Data Version Control)**      | Git-achtige versioning voor datasets, slaat metadata in git en data in remote storage | Kleine tot middelgrote datasets, teams die al git gebruiken |
| **Lakehouse (Delta Lake, Iceberg)** | Time-travel via tabelversionering, ACID-transacties op datalake                       | Grote datasets, analytische workloads                       |
| **Snapshots**                       | Periodieke kopieën van datasets met timestamp                                         | Eenvoudigste aanpak, geschikt voor L0-L1                    |

**Minimale vereisten:**

- [ ] Elke trainingsdataset heeft een uniek versienummer of hash
- [ ] De relatie model-versie ↔ data-versie is vastgelegd in het model registry
- [ ] Vorige versies zijn opvraagbaar voor debugging en auditing
- [ ] Wijzigingen in datasets worden gelogd (wat veranderde, wanneer, door wie)

______________________________________________________________________

## 5. Metadata Management

Goede metadata maakt data vindbaar, begrijpelijk en herbruikbaar.

### Minimale metadata per dataset

| Metadata-veld                     | Beschrijving                                                          |
| :-------------------------------- | :-------------------------------------------------------------------- |
| **Naam**                          | Unieke, beschrijvende naam                                            |
| **Beschrijving**                  | Wat bevat deze dataset? Waarvoor wordt ze gebruikt?                   |
| **Eigenaar**                      | Team of persoon die verantwoordelijk is                               |
| **Classificatie**                 | Publiek / intern / vertrouwelijk / geheim                             |
| **Schema**                        | Velddefinities, datatypes, beperkingen                                |
| **Kwaliteitsscore**               | Actuele score op de zes kwaliteitsdimensies                           |
| **Herkomst**                      | Bronnen en transformaties (link naar lineage)                         |
| **Aanmaakdatum / Laatste update** | Timestamps                                                            |
| **Tags**                          | Vrije tags voor zoekbaarheid (bijv. `klantdata`, `financieel`, `PII`) |

### Data catalogus

!!! tip "Start simpel"
    Een gedeeld spreadsheet of wiki-pagina met bovenstaande velden is een prima startpunt. Schaal op naar tooling als het aantal datasets groeit.

**Tooling opties:** DataHub, Amundsen, Apache Atlas, Collibra, of een eenvoudige interne wiki.

______________________________________________________________________

## 6. Praktische Checklist per Fase

### Fase 1 — Verkenning

- [ ] Data bronnen geïnventariseerd en gedocumenteerd
- [ ] Eerste kwaliteitsmeting uitgevoerd (steekproef op de zes dimensies)
- [ ] Data-eigenaarschap vastgesteld per bron
- [ ] Privacy-classificatie toegekend (bevat de data PII?)
- [ ] Eerste data lineage geschetst (bron → verwerking → gebruik)

### Fase 2 — Validatie

- [ ] Data contracts opgesteld met alle relevante producers
- [ ] Geautomatiseerde kwaliteitscontroles ingericht in de pipeline
- [ ] Data versioning opgezet voor trainingssets
- [ ] Metadata ingevuld in de data catalogus
- [ ] Kwaliteitsdrempels gedefinieerd en afgestemd met het team

### Fase 3 — Realisatie

- [ ] Data contracts actief gehandhaafd (monitoring op schendingen)
- [ ] Volledige lineage tracking operationeel
- [ ] Kwaliteitsrapporten geautomatiseerd en zichtbaar in dashboards
- [ ] Data versioning geïntegreerd met model registry
- [ ] Metadata up-to-date en doorzoekbaar

### Fase 4+ — Monitoring & Doorlopend

- [ ] Continue datakwaliteitsmonitoring actief
- [ ] Drift detectie op inputdata (niet alleen modeloutput)
- [ ] Periodieke review van data contracts (minimaal per kwartaal)
- [ ] Data catalogus bijgewerkt bij nieuwe of gewijzigde datasets
- [ ] Audit trail beschikbaar voor compliance-reviews

______________________________________________________________________

## 7. Gerelateerde Modules

- [Data Pipelines](02-data-pipelines.md) — technische standaarden voor data-ingestie, transformatie en validatie
- [Data-Evaluatie (Fase 1)](../02-fase-ontdekking/02-activiteiten.md) — eerste datakwaliteitsbeoordeling in de Verkenningsfase
- [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md) — detectie van verschuivingen in data en modelgedrag
- [Data & Privacyblad](../09-sjablonen/11-privacy-data/privacyblad.md) — privacy-aspecten van dataverwerking
- [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) — logging en auditability
