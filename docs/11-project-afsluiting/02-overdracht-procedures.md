---
versie: '1.0'
type: guide
layer: 2
phase: [5]
---

# 2. Overdracht Procedures

!!! abstract "Doel"
    Gestructureerde overdracht van het AI-systeem aan de beheerorganisatie zodat continuïteit, compliance en kwaliteit gegarandeerd zijn.

## 1. Doelstelling

Wij dragen het AI-systeem formeel en gestructureerd over aan de beheerorganisatie zodat continuïteit, compliance en kwaliteit na projectafsluiting zijn gegarandeerd.

______________________________________________________________________

## 2. Intrede Criteria

- Gate 3 (Productie-klaar) is goedgekeurd.
- Het beheerteam is aangewezen en beschikbaar voor training.
- De Overdracht Checklist is voorbereid. → [Overdracht Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)

______________________________________________________________________

## 3. Kernactiviteiten

### Overdrachtsplan opstellen

Minimaal twee weken vóór Gate 4 stelt de AI PM een overdrachtsplan op met:

- **Scope:** Welke systemen, databronnen en processen worden overgedragen?
- **Tijdlijn:** Wanneer worden welke onderdelen overgedragen?
- **Acceptatiecriteria:** Wanneer beschouwt de beheerorganisatie de overdracht als geslaagd?
- **Contactpersonen:** Wie is de eerste aanspreekpunt na overdracht?

### Technische overdracht

De Tech Lead organiseert de technische overdracht in drie stappen:

1. **Documentatiereview:** Technische Modelkaart, runbook en infrastructuurdocumentatie worden samen met de beheerder doorgenomen.
1. **Hands-on sessie:** De beheerder voert zelf de belangrijkste beheertaken uit (herstart, schaling, monitoring bekijken) onder begeleiding van de Tech Lead.
1. **Schaduwperiode:** De beheerder runt het systeem zelfstandig gedurende minimaal 5 werkdagen terwijl het projectteam nog beschikbaar is voor vragen.

### Guardian-overdracht

De overdracht van de Guardian-rol vereist een aparte procedure:

1. Nieuwe Guardian wordt aangewezen door de beheerorganisatie.
1. Gezamenlijke sessie: huidige Guardian + nieuwe Guardian lopen de Harde Grenzen door.
1. Schriftelijke overdracht van het compliance-dossier.
1. Nieuwe Guardian tekent de acceptatie van de Guardian-verantwoordelijkheden.

### Formele acceptatie

De overdracht is pas voltooid wanneer:

- De Overdracht Checklist volledig is afgevinkt.
- Zowel projectteam als beheerorganisatie het overdrachtsformulier hebben ondertekend.
- Gate 4 (Livegang) is goedgekeurd door de Guardian.

______________________________________________________________________

## 4. Team & Rollen

| Rol                        | Verantwoordelijkheid                                | R/A/C/I |
| :------------------------- | :-------------------------------------------------- | :------ |
| AI Product Manager         | Coördineert het volledige overdrachtsproces         | A       |
| Tech Lead                  | Voert technische overdracht en hands-on sessies uit | R       |
| Guardian (project)         | Draagt compliance-dossier en Harde Grenzen over     | R       |
| Guardian (beheer)          | Accepteert Guardian-rol en compliance-dossier       | R       |
| Beheerorganisatie eigenaar | Tekent formele acceptatie                           | A       |

______________________________________________________________________

## 5. Exit Criteria

- [ ] Overdracht Checklist is volledig afgevinkt en ondertekend.
- [ ] Schaduwperiode van minimaal 5 werkdagen is afgerond.
- [ ] Guardian-overdracht is formeel bevestigd.
- [ ] Gate 4 is goedgekeurd.
- [ ] Projectteam heeft officieel geen operationele verantwoordelijkheid meer.

______________________________________________________________________

## 6. Deliverables

| Deliverable                     | Beschrijving                                       | Eigenaar  |
| :------------------------------ | :------------------------------------------------- | :-------- |
| Overdrachtsplan                 | Tijdlijn, scope en acceptatiecriteria              | AI PM     |
| Overdracht Checklist (ingevuld) | Volledig afgevinkte checklist met handtekeningen   | AI PM     |
| Overdrachtsformulier            | Formeel document met handtekeningen beide partijen | AI PM     |
| Runbook                         | Stap-voor-stap handleiding voor de beheerder       | Tech Lead |

______________________________________________________________________

**Gerelateerde modules:**

- [Project Afsluiting — Overzicht](index.md)
- [Overdracht Checklist Sjabloon](../05-fase-levering/04-sjablonen/overdracht-checklist.md)
- [Gate Reviews Checklist](../09-sjablonen/04-gate-reviews/checklist.md)
- [Lessons Learned](01-lessons-learned.md)
- [Waarderealisatie](03-batenrealisatie.md)

______________________________________________________________________

**Volgende stap:** [Meet de definitieve baten via Waarderealisatie](03-batenrealisatie.md)
→ Zie ook: [Overdracht Checklist](../05-fase-levering/04-sjablonen/overdracht-checklist.md)
