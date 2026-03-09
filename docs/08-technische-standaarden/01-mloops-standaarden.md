---
versie: '1.0'
---

# 1. Technische Standaarden & Leveringscriteria

## 1. Doel

Deze module definieert wat "productiewaardig" betekent voor AI-oplossingen, inclusief een realistische route:

- **Basis** (handmatige governance, minimale automatisering)
- **Gevorderd** (meer automatisering, CI/CD/kwaliteitspoorten)

## 2. Automation Ladder (realistisch groeipad)

| Niveau                        | Omschrijving                            | Voor wie          | Voorbeeld controles                  |
| ----------------------------- | --------------------------------------- | ----------------- | ------------------------------------ |
| **L0 Handmatig**              | Checklists + handmatige gates           | startende teams   | sjablonen ingevuld, handtekeningen   |
| **L1 Semi**                   | vaste testset + vaste rapportage        | meeste teams      | Doelkaart (goal card) elke release   |
| **L2 Geautomatiseerd testen** | tests draaien automatisch bij wijziging | engineering teams | regressietest op Golden Set          |
| **L3 Governance-as-Code**     | policy checks blokkeren release         | mature MLOps      | release faalt zonder bewijs/metadata |

## 3. Minimum Technical Baseline (moet elk team halen)

!!! check "Reproduceerbaarheid & wijzigingsbeheer"
    - [ ] Code/instructies staan in versiebeheer (repo)
    - [ ] Config (modelversie, instellingen) is traceerbaar
    - [ ] Release is tagbaar (RC-1, v1.0) + rollback plan bestaat

!!! check "Security & toegang"
    - [ ] Secrets niet hardcoded; toegang via veilige opslag
    - [ ] Role-based access (wie mag prompts/config wijzigen?)
    - [ ] Least privilege op data-bronnen

!!! check "Observability (minimaal)"
    - [ ] Logging aanwezig (modelversie, promptversie, bron-IDs, output-status)
    - [ ] Basis metrics: foutpercentage, latency, volume
    - [ ] Incidentproces is bekend (wie belt wie)

!!! check "Kwaliteit & bewijs"
    - [ ] Golden Set bestaat en wordt gebruikt
    - [ ] [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md) beschikbaar voor pilot/RC
    - [ ] Voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md) normen voor risiconiveau

## 4. Basisroute (zonder zware MLOps)

**Doel:** veilig live met minimale tooling.

- Gebruik sjablonen als "single source of truth"
- Plan vaste evaluatiemomenten (bijv. wekelijks in pilot, maandelijks in beheer)
- Logging minimaal: metadata + sampling output (waar privacy toelaat)

## 5. Gevorderde route (met meer automatisering)

**Doel:** schaalbaar beheer bij meerdere use cases.

- Automatische regressietests op Golden Set bij elke wijziging
- Automatisch genereren van Validatierapport uit testruns (waar mogelijk)
- Integratie van policy checks: "geen Validatierapport = geen release"

## 6. Definition of Done voor Livegang

!!! check "Livegang Checklist"
    - [ ] Gate 3 (Productie-klaar) akkoord (Validatierapport RC voldoet aan [Bewijsstandaarden](../01-ai-native-fundamenten/07-bewijsstandaarden.md))
    - [ ] Logging/retentie ingericht (incl. privacymaatregelen)
    - [ ] Incident & rollback procedure getest (tabletop oefening of simulatie)
    - [ ] Owner voor beheer benoemd + monitoring actief
    - [ ] Gebruikersinstructies + transparantie (indien relevant) gepubliceerd
