---
versie: '1.0'
pdf: false
---

# Vendor Selectie Framework

Gestructureerde aanpak voor het evalueren en kiezen van AI-leveranciers. Doorloop de stappen in volgorde.

______________________________________________________________________

## Stap 1 — Vereisten Vaststellen

Definieer eerst uw minimale vereisten (knock-out criteria) en gewenste eigenschappen (wensen).

### Knock-out Criteria

| Vereiste            | Toelichting                                                                |
| :------------------ | :------------------------------------------------------------------------- |
| GDPR-compliance     | Verwerking binnen EU of adequaatheidsbesluit                               |
| Uptime SLA          | Minimaal \[x\]% (bijv. 99.5%)                                              |
| Dataretentie beleid | Geen permanente opslag van prompts/outputs tenzij expliciet overeengekomen |
| Ondersteunde talen  | \[talen\]                                                                  |
| Prijsmodel          | \[token-based / abonnement / pay-per-use\]                                 |

Leveranciers die **niet** voldoen aan knock-out criteria worden direct uitgesloten.

### Wensen (Gewogen)

| Eigenschap                     | Gewicht (1–5) | Toelichting |
| :----------------------------- | :------------ | :---------- |
| Kwaliteit van outputs          |               |             |
| Latency (response tijd)        |               |             |
| Documentatie & support         |               |             |
| Ecosysteem & integraties       |               |             |
| Prijsflexibiliteit / kortingen |               |             |
| Transparantie over modelgedrag |               |             |
| Innovatiesnelheid              |               |             |

______________________________________________________________________

## Stap 2 — Longlist Samenstellen

| Leverancier     | Type           | Primair product               | In scope? |
| :-------------- | :------------- | :---------------------------- | :-------- |
| Anthropic       | API            | Claude (Haiku/Sonnet/Opus)    | ☐         |
| OpenAI          | API            | GPT-4o / o1                   | ☐         |
| Google          | API / Platform | Gemini / Vertex AI            | ☐         |
| Microsoft Azure | Platform       | OpenAI-as-a-service, Azure ML | ☐         |
| AWS             | Platform       | Bedrock, SageMaker            | ☐         |
| Mistral AI      | API            | Mistral modellen              | ☐         |
| Cohere          | API            | Command / Embed               | ☐         |
| \[Andere\]      |                |                               | ☐         |

______________________________________________________________________

## Stap 3 — Shortlist Scorecard

Geef elke leverancier op de shortlist een score (1–5) per eigenschap en vermenigvuldig met het gewicht.

### Scorecard

| Eigenschap      | Gewicht | \[Leverancier A\] | \[Leverancier B\] | \[Leverancier C\] |
| :-------------- | :------ | :---------------- | :---------------- | :---------------- |
| Outputkwaliteit |         |                   |                   |                   |
| Latency         |         |                   |                   |                   |
| Documentatie    |         |                   |                   |                   |
| Ecosysteem      |         |                   |                   |                   |
| Prijs           |         |                   |                   |                   |
| Transparantie   |         |                   |                   |                   |
| Innovatie       |         |                   |                   |                   |
| **Totaalscore** |         |                   |                   |                   |

### PoC-resultaten (optioneel)

| Test                   | \[Leverancier A\] | \[Leverancier B\] | \[Leverancier C\] |
| :--------------------- | :---------------- | :---------------- | :---------------- |
| Taaktype 1             |                   |                   |                   |
| Taaktype 2             |                   |                   |                   |
| Latency p95            |                   |                   |                   |
| Kosten per 1K requests |                   |                   |                   |

______________________________________________________________________

## Stap 4 — Aanbeveling

**Geselecteerde leverancier:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Reden voor keuze:**

> _Korte onderbouwing (3–5 zinnen)._

**Risico's bij deze keuze:**

| Risico          | Mitigatie                                             |
| :-------------- | :---------------------------------------------------- |
| Vendor lock-in  | Abstractielaag bouwen / multi-vendor strategie        |
| Prijsstijging   | Contractueel prijsplafond of alternatief voorbereiden |
| Beschikbaarheid | Fallback naar tweede leverancier definiëren           |

**Goedkeuring:**

| Rol                  | Naam | Datum | Handtekening |
| :------------------- | :--- | :---- | :----------- |
| AI PM                |      |       |              |
| Tech Lead            |      |       |              |
| CAIO / Opdrachtgever |      |       |              |

______________________________________________________________________

## Gerelateerde Modules

- [RFP Template](02-rfp-template.md)
- [Contract Checklist](03-contract-checklist.md)
- [Cloud vs. On-Premise](../../08-technische-standaarden/06-cloud-vs-onpremise.md)
- [Business Case](../02-business-case/template.md)
