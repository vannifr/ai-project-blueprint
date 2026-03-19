---
versie: '1.1'
type: technical
layer: 3
roles: [Data Scientist, Tech Lead]
tags: [data, mlops]
---

# 1. Data Pipelines

## 1. Purpose

This module defines the standards for setting up and managing data pipelines that feed AI systems. A robust data pipeline is the backbone of every reliable AI solution.

______________________________________________________________________

## 2. Core Activities

### Data Ingestion

Collecting data from source files into a central processing environment.

**Minimum requirements:**

- [ ] Sources are documented (where does the data come from?)
- [ ] Access rights are arranged and minimal (least privilege)
- [ ] Ingestion is repeatable and automated where possible
- [ ] Error handling is implemented (what happens on failed ingestion?)

### Data Validation & Quality Controls

Checking whether incoming data meets expected schemas and quality standards.

**Minimum requirements:**

- [ ] Schema validation: data meets expected format
- [ ] Completeness check: critical fields are present
- [ ] Range check: values fall within expected bounds
- [ ] Anomaly detection: unexpected patterns are flagged

**Recommended approach:**

| Control Type  | Example                             | Action on Failure       |
| ------------- | ----------------------------------- | ----------------------- |
| Critical      | Required field missing              | Pipeline stops, alert   |
| Warning       | Value outside expected range        | Log, pipeline continues |
| Informational | Statistical deviation vs historical | Log for review          |

### Data Transformation

Converting raw data into a usable format for the AI model.

**Minimum requirements:**

- [ ] Transformation logic is documented and version-controlled
- [ ] Personally identifiable information (PII) is pseudonymised where necessary
- [ ] Transformations are reproducible (same input = same output)

### Versioning & Reproducibility

Tracking data versions so that results are traceable.

**Minimum requirements:**

- [ ] Datasets are tagged with version numbers or timestamps
- [ ] Relationship between data version and model version is recorded
- [ ] Historical data is queryable for debugging/auditing

______________________________________________________________________

## 3. Basic vs Advanced

| Aspect         | Basic (L0-L1)             | Advanced (L2-L3)                        |
| -------------- | ------------------------- | --------------------------------------- |
| Ingestion      | Manual or scheduled batch | Event-driven, real-time where needed    |
| Validation     | Manual sampling           | Automated controls in pipeline          |
| Transformation | Scripts in repository     | Documented, tested transformations      |
| Versioning     | File names with date      | Data versioning tools (DVC, Delta Lake) |
| Monitoring     | Periodic manual check     | Dashboards with alerts                  |

______________________________________________________________________

## 4. Integration with Governance

- **Traceability:** Every model output must be traceable to the data version used.
- **Privacy:** Apply the rules from [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md) to the pipeline.
- **Logging:** Log data ingestion and transformations according to [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md).

______________________________________________________________________

## 5. Go-Live Checklist

!!! check "5. Go-Live Checklist"
    - [ ] Data ingestion runs stably in production environment
    - [ ] Quality controls are implemented and tested
    - [ ] Transformation logic has been reviewed and documented
    - [ ] Data versioning is set up
    - [ ] Monitoring and alerting are active
    - [ ] Privacy measures are implemented and validated

______________________________________________________________________

## 6. Related Modules

- [Technical Standards & Delivery Criteria](01-mloops-standaarden.md)
- [Data & Privacy Sheet](../09-sjablonen/11-privacy-data/privacyblad.md)
- [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md)
