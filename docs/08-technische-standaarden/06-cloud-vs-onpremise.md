---
versie: '1.0'
---

# Cloud vs. On-Premise

Beslissingsraamwerk voor de keuze tussen cloud-ingebruikname, on-premise infrastructuur of een hybride aanpak. Gebruik dit in de **Verkenning & Strategie**-fase voordat architectuurkeuzes worden vastgelegd.

______________________________________________________________________

## 1. Beslissingsmatrix

Scoor elk criterium op basis van uw situatie: **C** = voordeel voor Cloud, **O** = voordeel voor On-Premise, **=** = neutraal.

| Criterium                                                                | Gewicht   | Uw situatie | Richting |
| :----------------------------------------------------------------------- | :-------- | :---------- | :------- |
| **Datasouvereiniteit** — data moet binnen NL/EU blijven                  | Hoog      |             | C / O    |
| **Schaalbaarheid** — volumes variëren sterk of zijn onbekend             | Hoog      |             | C / O    |
| **Time-to-market** — snel prototype of pilot nodig                       | Hoog      |             | C / O    |
| **Kostenzekerheid** — voorspelbare maandelijkse kosten vereist           | Hoog      |             | C / O    |
| **Compliance** — sector-regulering vereist volledige controle            | Hoog      |             | C / O    |
| **Latentie** — real-time verwerking met \< 100 ms vereist                | Gemiddeld |             | C / O    |
| **Bestaande infrastructuur** — significante on-prem investering aanwezig | Gemiddeld |             | C / O    |
| **Onderhoudscapaciteit** — intern team voor infra-beheer beschikbaar     | Gemiddeld |             | C / O    |

### Interpretatie

- **Overwegend C:** cloud-first aanpak aanbevolen
- **Overwegend O:** on-premise of private cloud aanbevolen
- **Gemengd:** hybride architectuur overwegen

______________________________________________________________________

## 2. Beslissingsboom (5 vragen)

```
1. Verwerkt het systeem bijzondere categorieën persoonsgegevens (gezondheid, biometrie)?
   JA  → On-premise of private cloud sterk aanbevolen
   NEE → ga naar 2

2. Is de verwachte belasting onvoorspelbaar of seizoensgebonden (factor 10+ variatie)?
   JA  → Cloud aanbevolen (elastische schaalbaarheid)
   NEE → ga naar 3

3. Heeft de organisatie < 2 FTE beschikbaar voor infrastructuurbeheer?
   JA  → Cloud aanbevolen (managed services)
   NEE → ga naar 4

4. Vereist de sector volledige audit-controle over hardware en data-locatie?
   JA  → On-premise of private cloud vereist
   NEE → ga naar 5

5. Is time-to-market < 3 maanden voor een werkend systeem?
   JA  → Cloud aanbevolen
   NEE → beide opties vergelijkbaar; baseer op TCO
```

______________________________________________________________________

## 3. Cloud Ingebruikname

### Aanbieders — Vergelijking

| Aspect                | AWS                        | Azure                      | GCP                  |
| :-------------------- | :------------------------- | :------------------------- | :------------------- |
| **LLM/AI services**   | Bedrock (Claude, Llama)    | Azure OpenAI, Copilot      | Vertex AI (Gemini)   |
| **EU data residency** | Frankfurt, Ireland         | West/North Europe          | Belgium, Netherlands |
| **Compliance**        | ISO 27001, SOC 2, NEN 7510 | ISO 27001, SOC 2, NEN 7510 | ISO 27001, SOC 2     |
| **Min. kosten (dev)** | Pay-per-use                | Pay-per-use                | Pay-per-use          |
| **MLOps platform**    | SageMaker                  | Azure ML                   | Vertex AI            |

### Kostenbeheersing in Cloud

**Primaire kostenrijvers:**

1. **Inferentie-API's** — aantal tokens × prijs per token (LLM)
1. **Compute** — GPU/CPU uren voor training of zware inferentie
1. **Opslag** — vector stores, model artefacten, logs
1. **Netwerk** — data transfer (vooral egress) en API-gateways

**Kostenoptimalisatie:** zie [Kostenoptimalisatie](07-kostenoptimalisatie.md) voor concrete technieken.

### Beveiligings-checklist Cloud

- [ ] Data-residency geconfigureerd op EU-regio
- [ ] Encryption at rest en in transit ingesteld
- [ ] IAM met least-privilege geconfigureerd
- [ ] VPC/private endpoint voor gevoelige services
- [ ] Secrets management (geen credentials in code)
- [ ] Logging en audit trail actief (CloudTrail / Azure Monitor / Cloud Audit)
- [ ] Budget alerts ingesteld

______________________________________________________________________

## 4. On-Premise Ingebruikname

### Infrastructuurvereisten

| Component   | Minimaal (pilot)           | Productie                              |
| :---------- | :------------------------- | :------------------------------------- |
| **CPU**     | 16 cores                   | 32+ cores                              |
| **RAM**     | 64 GB                      | 256 GB+                                |
| **GPU**     | Optioneel (CPU-inferentie) | NVIDIA A100 / H100 voor grote modellen |
| **Opslag**  | 2 TB NVMe                  | 20+ TB RAID                            |
| **Netwerk** | 1 Gbps                     | 10 Gbps                                |
| **OS**      | Ubuntu 22.04 LTS           | Ubuntu 22.04 LTS / RHEL                |

### Software Stack (open source opties)

| Laag              | Optie                       | Licentie         |
| :---------------- | :-------------------------- | :--------------- |
| **Model serving** | Ollama, vLLM, TGI           | MIT / Apache 2.0 |
| **Orchestratie**  | Kubernetes (k3s voor klein) | Apache 2.0       |
| **MLOps**         | MLflow, DVC                 | Apache 2.0       |
| **Monitoring**    | Prometheus + Grafana        | Apache 2.0       |
| **Vector store**  | Qdrant, Weaviate, pgvector  | Apache 2.0 / BSD |

### TCO-berekening (vereenvoudigd)

```
CapEx (eenmalig):
  Hardware:            €_______
  Installatie/setup:   €_______

OpEx (jaarlijks):
  Energie:             €_______ /jaar
  Onderhoud/beheer:    €_______ /jaar  (1–2 FTE × tarief)
  Licenties:           €_______ /jaar

Vergelijk met Cloud:
  Verwachte cloud-kosten: €_______ /jaar
  Break-even punt:         _______ jaar
```

______________________________________________________________________

## 5. Hybride Architectuur

De meest voorkomende hybride patronen:

| Patroon                             | Beschrijving                                                          | Wanneer                                        |
| :---------------------------------- | :-------------------------------------------------------------------- | :--------------------------------------------- |
| **Dev cloud / Prod on-prem**        | Ontwikkelen in cloud (flexibel), produceren on-prem (controle)        | Strenge productie-eisen, flexibele R&D         |
| **Data on-prem / Inferentie cloud** | Ruwe data blijft on-prem; anoniem/verwerkt naar cloud voor inferentie | Data-souvereiniteit + schaalbaarheid           |
| **Multi-cloud**                     | Kritieke workloads op twee providers                                  | Vendor lock-in vermijden, hoge beschikbaarheid |
| **Edge + cloud**                    | Real-time inferentie on-device; zware verwerking in cloud             | IoT, lage latentie, beperkte connectiviteit    |

______________________________________________________________________

## 6. Aanbevelingen per Organisatieprofiel

| Profiel                        | Aanbeveling                                                                   |
| :----------------------------- | :---------------------------------------------------------------------------- |
| **Verkenner** (eerste pilot)   | Cloud-first: managed LLM API + SaaS tooling. Minimale infra-investering.      |
| **Bouwer** (productiesystemen) | Hybride: cloud voor dev/test, on-prem of private cloud voor productie-data.   |
| **Visionair** (portfolio)      | Multi-cloud + on-prem voor kritieke systemen. Eigen Platform Enablement team. |

______________________________________________________________________

## Gerelateerde Modules

- [Kostenoptimalisatie](07-kostenoptimalisatie.md)
- [AI Architectuur](05-ai-architectuur.md)
- [MLOps Standaarden](01-mloops-standaarden.md)
- [Data Pipelines](02-data-pipelines.md)
