---
versie: '1.0'
pdf: false
type: cheatsheet
layer: 3
phase: [1, 2, 3, 4, 5]
tags: [quick-reference]
---

# Cheatsheet — AI-Samenwerkingsmodi

**Bron:** [Samenwerkingsmodi](../../00-strategisch-kader/06-has-h-niveaus.md)

______________________________________________________________________

## De 5 Modi

| Modus | Naam                      | Wie beslist         | Typische toepassing                       |
| :---- | :------------------------ | :------------------ | :---------------------------------------- |
| **1** | Mens volledig             | Mens                | Creatieve of ethische oordelen            |
| **2** | AI adviseert              | Mens (na AI-input)  | Analyses, samenvattingen, opties          |
| **3** | AI stelt voor, mens keurt | Mens (finale klik)  | Documentgeneratie, e-mails, rapporten     |
| **4** | AI handelt, mens monitort | AI (mens grijpt in) | Geautomatiseerde verwerking, routinetaken |
| **5** | AI volledig autonoom      | AI                  | Volledig geautomatiseerde pipelines       |

______________________________________________________________________

## Wanneer Welk Niveau?

```
Vraag 1: Wat zijn de gevolgen als de AI fout zit?
  → Groot / onomkeerbaar?  → Modus 1 of 2
  → Klein / herstelbaar?   → Modus 3, 4 of 5

Vraag 2: Is de taak gestandaardiseerd en repetitief?
  → Nee  → Modus 1 of 2
  → Ja   → Overweeg Modus 3 of 4

Vraag 3: Is het Hoog Risico systeem (EU AI Act)?
  → Ja   → Modus 1, 2 of 3 (menselijk toezicht verplicht)
  → Nee  → Modus 4 of 5 mogelijk
```

______________________________________________________________________

## Escalatieregels

| Situatie                      | Actie                                         |
| :---------------------------- | :-------------------------------------------- |
| Onverwachte output            | Schakel terug naar lagere modus               |
| Kwaliteitsdaling gedetecteerd | Review modus; overweeg menselijke tussenkomst |
| Nieuw gebruik buiten scope    | Herbeoordeel modus; leg vast in charter       |
| Klacht of incident            | Minstens naar Modus 3 tot oorzaak bekend      |

______________________________________________________________________

## Governance Vereisten per Modus

| Modus | Logging                 | Menselijke review       | Guardian sign-off           |
| :---- | :---------------------- | :---------------------- | :-------------------------- |
| 1–2   | Aanbevolen              | Bij elk besluit         | Niet vereist                |
| 3     | Verplicht               | Steekproef (10%)        | Bij implementatie           |
| 4     | Verplicht               | Alert-based             | Verplicht                   |
| 5     | Verplicht + audit trail | Periodiek (maandelijks) | Verplicht + hercertificatie |

**Bron:** [Samenwerkingsmodi](../../00-strategisch-kader/06-has-h-niveaus.md) | [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md)
