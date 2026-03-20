---
versie: '1.0'
type: technical
layer: 3
roles: [AI Product Manager, Data Scientist, Guardian]
tags: [data, governance]
summary: Framework for data quality, data lineage, data contracts and metadata management in AI projects.
answers: [How do I ensure data quality in an AI project?, What are data contracts?, How do I track data lineage?]
---

# Data Governance

!!! abstract "Purpose"
    Bad data is the number one reason AI projects fail. This module provides a concrete framework for data quality, data lineage, data contracts and metadata management — so your AI system rests on a reliable data foundation.

!!! tip "When to use this?"
    From the Discovery phase (Phase 1) during Data Evaluation. Data governance is not a one-time activity: it runs through all phases. Start early, build incrementally.

______________________________________________________________________

## 1. Data Quality Framework

Data quality is measured along six dimensions. Define concrete thresholds per dimension that match the risk level of the project.

| Dimension        | Definition                                                    | Measurement Method                                     | Example Threshold                                    |
| :--------------- | :------------------------------------------------------------ | :----------------------------------------------------- | :--------------------------------------------------- |
| **Completeness** | All expected records and fields are present                   | `(records with value / total expected records) × 100%` | ≥ 95% for critical fields                            |
| **Accuracy**     | Values correspond to reality                                  | Comparison with trusted sources or manual sample       | ≥ 98% on sample of 200 records                       |
| **Consistency**  | The same facts are represented identically across all systems | Cross-system comparisons, business rule checks         | 0 conflicts in primary keys                          |
| **Timeliness**   | Data is available within the required lead time               | Measurement of ingestion latency                       | ≤ 4 hours for daily batch; ≤ 5 min for near-realtime |
| **Uniqueness**   | No unwanted duplicates                                        | Deduplication analysis on unique keys                  | ≤ 0.1% duplicates                                    |
| **Validity**     | Values comply with the defined format and domain rules        | Schema validation, regex, domain lists                 | 100% of records match the schema                     |

!!! warning "Thresholds are project-specific"
    The example thresholds above are starting points. Adjust them based on risk level: a high-risk system (EU AI Act) requires stricter thresholds than an internal dashboard.

______________________________________________________________________

## 2. Data Lineage & Provenance

### What is data lineage?

Data lineage is the complete description of the origin, transformations and movements of data — from source to model input and ultimately model output.

### Why does it matter?

- **Traceability:** When unexpected model results occur, you can quickly identify which data is the cause.
- **Debugging:** Identify exactly where in the pipeline a data error was introduced.
- **Compliance:** The EU AI Act requires that the provenance of training data is demonstrable for high-risk systems.
- **Reproducibility:** Without lineage you cannot reliably repeat experiments.

### How to implement?

**Minimum requirements:**

- [ ] Every dataset has a unique identifier and version number
- [ ] Transformation steps are recorded with input version, output version and timestamp
- [ ] Metadata tags include: source, owner, processing date, quality score

**Tooling options:**

| Category    | Examples                                | Suitable for                 |
| :---------- | :-------------------------------------- | :--------------------------- |
| Lightweight | dbt lineage graph, manual documentation | Small teams, L0-L1           |
| Mid-range   | Apache Atlas, DataHub, OpenLineage      | Growing organisations, L1-L2 |
| Enterprise  | Collibra, Alation, Purview              | Large organisations, L2-L3   |

**Minimum requirements per risk level:**

| Risk Level   | Lineage Requirement                                      |
| :----------- | :------------------------------------------------------- |
| Low risk     | Documentation of sources and main transformations        |
| Limited risk | Automated lineage tracking, traceability to source level |
| High risk    | Full end-to-end lineage with audit trail, immutable logs |

______________________________________________________________________

## 3. Data Contracts

### What are data contracts?

A data contract is a formal agreement between a data producer (the team that delivers data) and a data consumer (the team that uses data). It prevents changes in upstream data from unexpectedly breaking your AI pipeline.

### Components of a data contract

| Component                | Description                                          | Example                                                    |
| :----------------------- | :--------------------------------------------------- | :--------------------------------------------------------- |
| **Schema**               | Expected fields, data types, nullable rules          | `customer_id: INT NOT NULL, name: VARCHAR(255)`            |
| **SLA**                  | Availability, refresh frequency, maximum latency     | Daily before 06:00 UTC, 99.5% uptime                       |
| **Ownership**            | Who is responsible for the data?                     | Customer Service Team (producer), ML Team (consumer)       |
| **Quality rules**        | Minimum quality requirements the producer guarantees | Completeness ≥ 98%, no duplicates on `customer_id`         |
| **Change policy**        | How are schema changes communicated?                 | Minimum 2 sprints advance notice, breaking changes via RFC |
| **Escalation procedure** | What happens when the contract is violated?          | Alert to consumer, incident addressed within 4 hours       |

### Example contract template

```yaml
# Data Contract — [Dataset Name]
contract_version: "1.0"
producer:
  team: "Customer Service Team"
  contact: "name@organisation.com"
consumer:
  team: "ML Platform Team"
  contact: "name@organisation.com"
dataset:
  name: "customer_interactions"
  format: "parquet"
  location: "s3://data-lake/customer_interactions/"
schema:
  - field: "customer_id"
    type: "INT"
    nullable: false
  - field: "interaction_date"
    type: "DATE"
    nullable: false
  - field: "channel"
    type: "VARCHAR(50)"
    nullable: false
    allowed_values: ["email", "phone", "chat", "portal"]
sla:
  refresh: "daily before 06:00 UTC"
  availability: "99.5%"
quality_rules:
  completeness: "≥ 98%"
  uniqueness_on: "customer_id + interaction_date"
change_policy: "Breaking changes: minimum 2 sprints advance notice via RFC"
```

______________________________________________________________________

## 4. Data Versioning

### Why?

Without data versioning you cannot guarantee that a model training run is reproducible. If training data changes without version tracking, debugging and auditing become impossible.

### Approach

| Method                              | Description                                                                         | When to use                                       |
| :---------------------------------- | :---------------------------------------------------------------------------------- | :------------------------------------------------ |
| **DVC (Data Version Control)**      | Git-like versioning for datasets, stores metadata in git and data in remote storage | Small to medium datasets, teams already using git |
| **Lakehouse (Delta Lake, Iceberg)** | Time-travel via table versioning, ACID transactions on data lake                    | Large datasets, analytical workloads              |
| **Snapshots**                       | Periodic copies of datasets with timestamp                                          | Simplest approach, suitable for L0-L1             |

**Minimum requirements:**

- [ ] Every training dataset has a unique version number or hash
- [ ] The relationship model version ↔ data version is recorded in the model registry
- [ ] Previous versions are queryable for debugging and auditing
- [ ] Changes to datasets are logged (what changed, when, by whom)

______________________________________________________________________

## 5. Metadata Management

Good metadata makes data findable, understandable and reusable.

### Minimum metadata per dataset

| Metadata Field             | Description                                                                   |
| :------------------------- | :---------------------------------------------------------------------------- |
| **Name**                   | Unique, descriptive name                                                      |
| **Description**            | What does this dataset contain? What is it used for?                          |
| **Owner**                  | Team or person responsible                                                    |
| **Classification**         | Public / internal / confidential / secret                                     |
| **Schema**                 | Field definitions, data types, constraints                                    |
| **Quality score**          | Current score on the six quality dimensions                                   |
| **Provenance**             | Sources and transformations (link to lineage)                                 |
| **Created / Last updated** | Timestamps                                                                    |
| **Tags**                   | Free-form tags for discoverability (e.g. `customer_data`, `financial`, `PII`) |

### Data catalogue

!!! tip "Start simple"
    A shared spreadsheet or wiki page with the fields above is a perfectly fine starting point. Scale up to dedicated tooling as the number of datasets grows.

**Tooling options:** DataHub, Amundsen, Apache Atlas, Collibra, or a simple internal wiki.

______________________________________________________________________

## 6. Practical Checklist per Phase

### Phase 1 — Discovery

- [ ] Data sources inventoried and documented
- [ ] Initial quality measurement performed (sample across the six dimensions)
- [ ] Data ownership established per source
- [ ] Privacy classification assigned (does the data contain PII?)
- [ ] Initial data lineage sketched (source → processing → usage)

### Phase 2 — Validation

- [ ] Data contracts established with all relevant producers
- [ ] Automated quality controls set up in the pipeline
- [ ] Data versioning configured for training sets
- [ ] Metadata populated in the data catalogue
- [ ] Quality thresholds defined and agreed with the team

### Phase 3 — Development

- [ ] Data contracts actively enforced (monitoring for violations)
- [ ] Full lineage tracking operational
- [ ] Quality reports automated and visible in dashboards
- [ ] Data versioning integrated with model registry
- [ ] Metadata up-to-date and searchable

### Phase 4+ — Monitoring & Ongoing

- [ ] Continuous data quality monitoring active
- [ ] Drift detection on input data (not just model output)
- [ ] Periodic review of data contracts (at least quarterly)
- [ ] Data catalogue updated for new or modified datasets
- [ ] Audit trail available for compliance reviews

______________________________________________________________________

## 7. Related Modules

- [Data Pipelines](02-data-pipelines.md) — technical standards for data ingestion, transformation and validation
- [Data Evaluation (Phase 1)](../02-fase-ontdekking/02-activiteiten.md) — initial data quality assessment in the Discovery phase
- [Drift Detection](../06-fase-monitoring/05-drift-detectie.md) — detection of shifts in data and model behaviour
- [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md) — privacy aspects of data processing
- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md) — logging and auditability
