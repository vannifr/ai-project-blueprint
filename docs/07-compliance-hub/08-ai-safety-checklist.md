---
versie: '1.0'
---

# AI Safety Checklist

Gestructureerde veiligheidschecks over vier dimensies: training, deployment, monitoring en governance. Gebruik deze checklist bij elke Gate Review voor Hoog Risico en Beperkt Risico systemen.

!!! tip "Risico-proportioneel gebruik"
    Minimaal Risico systemen: voer sectie 4 (Governance) uit. Beperkt Risico: sectie 2 + 4. Hoog Risico: alle vier secties verplicht.

______________________________________________________________________

## Sectie 1 — Trainings- & Dataveiligheid

*Relevant bij zelf-getrainde modellen of fine-tuning. Sla over bij pure API-gebruik van foundation models.*

| Check                                                                  | Status | Notitie |
| :--------------------------------------------------------------------- | :----- | :------ |
| Trainingsdata geëvalueerd op schadelijke content                       | ☐      |         |
| Bias gedetecteerd en gedocumenteerd in trainingsdata                   | ☐      |         |
| Persoonsgegevens in trainingsdata geminimaliseerd of gepseudonimiseerd | ☐      |         |
| Datasources gedocumenteerd (herkomst, licentie, datums)                | ☐      |         |
| Adversarial voorbeelden opgenomen in trainingsset                      | ☐      |         |
| Modelgewichten veilig opgeslagen (toegangscontrole, versiebeheer)      | ☐      |         |

______________________________________________________________________

## Sectie 2 — Deployment Safety

| Check                                                                              | Status | Notitie |
| :--------------------------------------------------------------------------------- | :----- | :------ |
| **Input-filtering** geconfigureerd (blokkeer verboden inputs)                      | ☐      |         |
| **Output-filtering** geconfigureerd (blokkeer verboden outputs)                    | ☐      |         |
| **Rode Lijnen** gedocumenteerd en technisch afgedwongen                            | ☐      |         |
| Rate limiting ingesteld (misbruikpreventie)                                        | ☐      |         |
| **Circuit Breaker** geconfigureerd (zie [Incident Respons](05-incidentrespons.md)) | ☐      |         |
| Least-privilege toegang: systeem heeft minimale benodigde rechten                  | ☐      |         |
| Systeemprompt beschermd tegen extractie                                            | ☐      |         |
| Gebruikers zijn geïnformeerd dat ze met AI interageren (transparantieplicht)       | ☐      |         |
| Human-in-the-loop mechanisme operationeel voor beslissingen met impact             | ☐      |         |
| Exit-procedure voor gebruikers gedocumenteerd (escalatie naar mens)                | ☐      |         |

______________________________________________________________________

## Sectie 3 — Monitoring Safety

| Check                                                                                                | Status | Notitie |
| :--------------------------------------------------------------------------------------------------- | :----- | :------ |
| Logging van inputs en outputs actief (met retentiebeleid)                                            | ☐      |         |
| Kwaliteitsmonitoring actief (drempelwaarden ingesteld)                                               | ☐      |         |
| **Drift-detectie** geconfigureerd (zie [Drift Detectie](../06-fase-monitoring/05-drift-detectie.md)) | ☐      |         |
| Fairness-metrics gemonitord (indien meerdere gebruikersgroepen)                                      | ☐      |         |
| Anomalie-detectie op gebruik (ongebruikelijke patronen, misbruik)                                    | ☐      |         |
| Alerting naar verantwoordelijke bij drempeloverschrijding                                            | ☐      |         |
| Procedure voor schadelijke output-meldingen door gebruikers                                          | ☐      |         |
| Periodieke steekproef-review van outputs ingepland                                                   | ☐      |         |

______________________________________________________________________

## Sectie 4 — Governance Safety

| Check                                                                  | Status | Notitie |
| :--------------------------------------------------------------------- | :----- | :------ |
| **Guardian** aangesteld en actief betrokken                            | ☐      |         |
| Safety review uitgevoerd bij elke Gate                                 | ☐      |         |
| [Red Teaming](07-red-teaming.md) uitgevoerd (Hoog/Beperkt Risico)      | ☐      |         |
| Incidentrespons-procedure gedocumenteerd en getest                     | ☐      |         |
| Verantwoordelijke voor het systeem benoemd (accountable owner)         | ☐      |         |
| Model Card up-to-date met bekende limieten en risico's                 | ☐      |         |
| Periodieke hercertificatie ingepland (min. jaarlijks voor Hoog Risico) | ☐      |         |
| EU AI Act compliance-status gedocumenteerd                             | ☐      |         |

______________________________________________________________________

## Constitutional AI — Richtlijnen voor Autonome Systemen

Bij Samenwerkingsmodus 4 en 5 (systeem handelt autonoom) gelden aanvullende Constitutional AI-principes:

### De drie kernprincipes

**1. Harmlessness — Geen schade**
Het systeem vermijdt acties die schade kunnen toebrengen aan gebruikers, derden of de organisatie. Definieer expliciet welke acties verboden zijn, ongeacht instructie.

**2. Honesty — Geen misleiding**
Het systeem communiceert transparant over zijn capaciteiten, onzekerheden en beperkingen. Het verzint geen feiten, geeft aan wanneer het iets niet weet.

**3. Helpfulness — Relevante assistentie**
Het systeem probeert oprecht behulpzaam te zijn binnen de gedefinieerde scope. Weigering is altijd verantwoord met een alternatief.

### Implementatie-checklist voor autonome systemen

| Vereiste                                                                  | Status |
| :------------------------------------------------------------------------ | :----- |
| Actieradius technisch begrensd (welke systemen/acties zijn toegankelijk)  | ☐      |
| Verboden acties expliciet gedocumenteerd (niet alleen impliciet verwacht) | ☐      |
| Maximale impact per actie begrensd (bijv. maximale transactiewaarde)      | ☐      |
| Self-critique mechanisme: systeem toetst eigen output vóór uitvoering     | ☐      |
| Menselijke goedkeuring vereist boven gedefinieerde impactdrempel          | ☐      |
| Audit trail van alle autonome acties (onveranderbaar)                     | ☐      |
| Explainability: systeem kan zijn beslissing toelichten op verzoek         | ☐      |

______________________________________________________________________

## Safety Score

Tel het aantal afgevinkte items per sectie en bereken de veiligheidsscore:

| Sectie                          | Afgevinkt | Totaal | %   |
| :------------------------------ | :-------- | :----- | :-- |
| 1 — Trainings- & Dataveiligheid |           | 6      |     |
| 2 — Deployment Safety           |           | 10     |     |
| 3 — Monitoring Safety           |           | 8      |     |
| 4 — Governance Safety           |           | 8      |     |
| **Totaal**                      |           | **32** |     |

**Minimale drempel voor livegang:**

- Hoog Risico: ≥ 90% (≥ 29/32)
- Beperkt Risico: ≥ 75% (≥ 24/32, sectie 1 optioneel)
- Minimaal Risico: sectie 4 volledig

______________________________________________________________________

## Gerelateerde Modules

- [Red Teaming Playbook](07-red-teaming.md)
- [Incident Respons](05-incidentrespons.md)
- [EU AI Act](01-eu-ai-act/index.md)
- [Ethische Richtlijnen](03-ethische-richtlijnen.md)
- [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
