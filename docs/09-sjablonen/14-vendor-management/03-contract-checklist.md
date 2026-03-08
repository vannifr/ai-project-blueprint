---
versie: '1.0'
pdf: false
---

# Contract Checklist — AI-leveranciers

Verificatielijst voor AI-specifieke contractvereisten. Gebruik bij contractonderhandeling met externe AI-leveranciers.

!!! warning "Juridisch advies"
    Deze checklist is een hulpmiddel, geen juridisch advies. Raadpleeg uw juridische afdeling of externe advocaat bij contracten met hoge waarde of complexe AI-risico's.

______________________________________________________________________

## Sectie 1 — Dataverwerkingsovereenkomst (DPA)

| Vereiste                                            | Status | Notitie |
| :-------------------------------------------------- | :----- | :------ |
| DPA aanwezig en ondertekend                         | ☐      |         |
| Verwerkingsdoeleinden expliciet gedefinieerd        | ☐      |         |
| Gegevenslocatie vastgelegd (EU / land)              | ☐      |         |
| Sub-verwerkers gedocumenteerd en goedgekeurd        | ☐      |         |
| Retentieperiode gegevens gespecificeerd             | ☐      |         |
| Procedure bij datalekken (binnen 72u melden)        | ☐      |         |
| Auditrechten opdrachtgever vastgelegd               | ☐      |         |
| Rechten betrokkenen (inzage, verwijdering) geregeld | ☐      |         |

______________________________________________________________________

## Sectie 2 — AI-specifieke Bepalingen

| Vereiste                                                                     | Status | Notitie |
| :--------------------------------------------------------------------------- | :----- | :------ |
| Verbod op gebruik van prompts/outputs voor modeltraining (tenzij toegestaan) | ☐      |         |
| Beleid bij modelupdates: vooraankondiging van wijzigingen                    | ☐      |         |
| Deprecatiebeleid: minimale aankondigingstermijn \[bijv. 6 maanden\]          | ☐      |         |
| Versievastheid: mogelijkheid tot pinnen op specifieke modelversie            | ☐      |         |
| Transparantie over modelgedrag en bekende beperkingen                        | ☐      |         |
| Aansprakelijkheid bij schadelijke outputs verduidelijkt                      | ☐      |         |
| Intellectueel eigendom van outputs geregeld                                  | ☐      |         |

______________________________________________________________________

## Sectie 3 — Service Level Agreement (SLA)

| Vereiste                                            | Status | Notitie |
| :-------------------------------------------------- | :----- | :------ |
| Uptime SLA vastgelegd (bijv. 99.5%)                 | ☐      |         |
| Meetmethode uptime gedefinieerd                     | ☐      |         |
| Boeteclausule bij SLA-schending                     | ☐      |         |
| Latency-garanties (p95, p99) gespecificeerd         | ☐      |         |
| Capaciteitsgaranties (rate limits) vastgelegd       | ☐      |         |
| Incidentprocedure en communicatiekanalen beschreven | ☐      |         |
| Statuspagina en incidentmeldingen geregeld          | ☐      |         |

______________________________________________________________________

## Sectie 4 — Beveiliging & Compliance

| Vereiste                                                  | Status | Notitie |
| :-------------------------------------------------------- | :----- | :------ |
| ISO 27001 / SOC 2 certificering aanwezig                  | ☐      |         |
| Penetratietestrapport recent (\< 1 jaar) beschikbaar      | ☐      |         |
| Encryptie in transit (TLS 1.2+) gegarandeerd              | ☐      |         |
| Encryptie at rest gegarandeerd                            | ☐      |         |
| Toegangscontrole en least-privilege beschreven            | ☐      |         |
| EU AI Act compliance-positie beschreven (indien relevant) | ☐      |         |
| Responsible Disclosure beleid leverancier aanwezig        | ☐      |         |

______________________________________________________________________

## Sectie 5 — Commerciële Voorwaarden

| Vereiste                                                           | Status | Notitie |
| :----------------------------------------------------------------- | :----- | :------ |
| Prijsmodel en eenheden helder gedefinieerd                         | ☐      |         |
| Prijswijzigingsclausule: aankondigingstermijn ≥ \[bijv. 90 dagen\] | ☐      |         |
| Maximale jaarlijkse prijsstijging vastgelegd                       | ☐      |         |
| Opzegtermijn en exit-procedure beschreven                          | ☐      |         |
| Dataportering bij beëindiging geregeld                             | ☐      |         |
| Aansprakelijkheidsplafond vastgelegd                               | ☐      |         |
| Toepasselijk recht en jurisdictie bepaald                          | ☐      |         |

______________________________________________________________________

## Samenvatting

| Sectie           | Items  | Afgevinkt | %   |
| :--------------- | :----- | :-------- | :-- |
| 1 — DPA          | 8      |           |     |
| 2 — AI-specifiek | 7      |           |     |
| 3 — SLA          | 7      |           |     |
| 4 — Beveiliging  | 7      |           |     |
| 5 — Commercieel  | 7      |           |     |
| **Totaal**       | **36** |           |     |

**Aanbeveling:** Teken contract pas bij ≥ 90% score (≥ 33/36). Openstaande punten documenteren als risico in het risicoregister.

**Beoordeeld door:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Datum:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## Gerelateerde Modules

- [Selectie Framework](01-selectie-framework.md)
- [RFP Template](02-rfp-template.md)
- [Risicoanalyse](../03-risicoanalyse/template.md)
- [EU AI Act](../../07-compliance-hub/01-eu-ai-act/index.md)
