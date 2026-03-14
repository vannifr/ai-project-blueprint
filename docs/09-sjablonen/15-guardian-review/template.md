---
versie: '1.0'
type: template
layer: 3
phase: [1, 2, 3, 4, 5]
roles: [Guardian]
tags: [ethics, gate-review, template]
---

# Guardian Review Checklist

De Guardian bewaakt de ethische en juridische kaders van een AI-systeem. Deze checklist begeleidt de Guardian door alle formele reviewmomenten in de lifecycle — van Gate 1 t/m decommissioning.

!!! info "Two-Man Rule bij High Risk"
    Bij AI-systemen met risicoklasse **Hoog** is expliciete goedkeuring vereist van twee personen: de **Privacy & Legal Officer** (toetst AVG + EU AI Act) én de **AI Quality Ethicist / QA Lead** (toetst bias, Golden Set-kwaliteit, outputveiligheid).

______________________________________________________________________

## 1. Mandaat & Onafhankelijkheid

Zorg vóór de eerste review dat het mandaat helder is vastgelegd.

- [ ] Guardian is formeel benoemd en geaccepteerd door het projectteam.
- [ ] Mandaat omvat veto-recht bij alle Gate Reviews.
- [ ] Guardian heeft geen directe belangen in het projectresultaat (onafhankelijkheid).
- [ ] Bij **Hoog Risico**: Two-Man Rule actief (Privacy Officer + AI Quality Ethicist beiden benoemd).
- [ ] Contactpersonen en escalatiepaden zijn gedocumenteerd.

______________________________________________________________________

## 2. Gate 1 Review — Verkenning & Strategie

**Moment:** Vóór go-ahead naar Validatie (PoV).

### Risico & Scope

- [ ] Risk Pre-Scan is ingevuld en risicoklasse is bepaald.
- [ ] Risicoklasse is realistisch (niet onderschat om compliance te vermijden).
- [ ] Bij Hoog Risico: EU AI Act Artikel 9 (risicobeheerssysteem) is van toepassing — bevestigd.

### Rode Lijnen & Doelkaart

- [ ] Doelkaart is opgesteld met expliciete Rode Lijnen (wat mag het systeem absoluut niet?).
- [ ] Rode Lijnen zijn concreet en toetsbaar (geen vage formuleringen).
- [ ] Green AI-overwegingen zijn ingevuld (sectie E van de Doelkaart).
- [ ] Guardian heeft Rode Lijnen goedgekeurd en ondertekend.

**Uitkomst Gate 1:**

- [ ] Goedgekeurd — voort naar Validatie (PoV)
- [ ] Goedgekeurd met voorwaarden: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- [ ] Afgewezen — reden: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Handtekening Guardian: \_\_\_\_\_\_\_\_\_\_ Datum: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 3. Gate 2 Review — PoV-investering

**Moment:** Vóór go-ahead naar Realisatie.

### Dataset & Fairness

- [ ] Trainingsdataset is gedocumenteerd (bron, omvang, datumrange).
- [ ] Dataset is gecontroleerd op representativiteitsbias (leeftijd, geslacht, geografie, etc.).
- [ ] Privacygevoelige data is geïdentificeerd en geanonimiseerd of gemaskeerd.
- [ ] Datasourcing voldoet aan AVG (rechtmatige grondslag, dataminimalisatie).

### Business Case & Proportionaliteit

- [ ] Business Case is ethisch verantwoord: voordelen wegen op tegen risico's.
- [ ] Is AI proportioneel? Kan een eenvoudiger systeem (rule-based, kleinere model) dezelfde taak uitvoeren?
- [ ] Geplande AI-bijdrage is realistisch (geen AI Productivity Paradox-valkuil; verwachte organisatiebrede winst 5–15%).

### Hard Boundaries in Doelkaart

- [ ] Hard Boundaries zijn vastgelegd in de Doelkaart (sectie D).
- [ ] Hard Boundaries zijn onwijzigbaar zonder Guardian-goedkeuring.

**Uitkomst Gate 2:**

- [ ] Goedgekeurd — voort naar Realisatie
- [ ] Goedgekeurd met voorwaarden: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- [ ] Afgewezen — reden: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Handtekening Guardian: \_\_\_\_\_\_\_\_\_\_ Datum: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 4. Gate 3 Review — Go-Live (Productie)

**Moment:** Vóór livegang in productie.

### Red Team & Veiligheid

- [ ] Red Team sessie is uitgevoerd (verplicht voor Hoog Risico).
- [ ] Geen open **Critical** of **High** bevindingen in het Red Team rapport.
- [ ] OWASP Top 10 LLM 2025 is afgewerkt als minimale scope.
- [ ] Deceptive Delight en HashJack aanvalspatronen zijn getest.
- [ ] AI Safety Checklist is ingevuld en goedgekeurd.

### Compliance

- [ ] AVG/GDPR: privacy-impact is beoordeeld; DPIA uitgevoerd indien vereist.
- [ ] EU AI Act: technisch dossier is up-to-date (voor Hoog Risico systemen).
- [ ] Traceerbaarheidsrapport is aanwezig (van data tot output).
- [ ] Prompts zijn geversioneerd en gedocumenteerd (conform Prompt Versioning template).

### Operationele Gereedheid

- [ ] Incident response plan is actief en getest.
- [ ] Monitoring en alerting zijn geconfigureerd (drift, hallucination rate, MTTD \< 15 min).
- [ ] Decommissioning-triggers zijn gedocumenteerd in de monitoring-configuratie.
- [ ] Overdracht aan beheerorganisatie is voltooid (Overdracht Checklist afgevinkt).

**Uitkomst Gate 3:**

- [ ] Goedgekeurd voor go-live
- [ ] Goedgekeurd met voorwaarden: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- [ ] Niet goedgekeurd — open bevindingen: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Handtekening Guardian (Privacy Officer): \_\_\_\_\_\_\_\_\_\_ Datum: \_\_\_\_\_\_\_\_\_\_

Handtekening Guardian (AI Quality Ethicist): \_\_\_\_\_\_\_\_\_\_ Datum: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 5. Doorlopend Toezicht (Post-Live)

Periodieke Guardian-checks na livegang.

### Kwartaalcheck

- [ ] Batenrealisatierapport ontvangen en beoordeeld.
- [ ] Geen onopgeloste incidents met Guardian-escalatie.
- [ ] Drift-rapporten beoordeeld: geen structurele bias-escalatie.
- [ ] Kaizen Log bijgewerkt met Guardian-aantekeningen.

### Jaarlijkse re-review (verplicht voor Hoog Risico)

- [ ] Hernieuwde Red Team sessie uitgevoerd.
- [ ] Juridisch kader opnieuw getoetst (EU AI Act updates, nieuwe regelgeving).
- [ ] Doelkaart en Rode Lijnen herzien op relevantie.

______________________________________________________________________

## 6. Decommissioning Review

**Moment:** Bij stopzetting van het AI-systeem.

- [ ] Stopzettingsbesluit is formeel genomen door CAIO of stuurgroep.
- [ ] Gebruikers zijn tijdig geïnformeerd (minimaal 30 dagen vooraf).
- [ ] Persoonsgegevens zijn verwijderd conform AVG (recht op vergetelheid).
- [ ] Modellen en configuraties zijn gearchiveerd of vernietigd (conform beleid).
- [ ] Kennisoverdracht aan beheerorganisatie is voltooid.
- [ ] Guardian-eindoordeel gedocumenteerd in Kaizen Log.

Handtekening Guardian: \_\_\_\_\_\_\_\_\_\_ Datum: \_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

**Gerelateerde modules:**

- [Rollen & Verantwoordelijkheden](../../08-rollen-en-verantwoordelijkheden/index.md)
- [Red Teaming Playbook](../../07-compliance-hub/07-red-teaming.md)
- [Doelkaart template](../06-ai-native-artefacten/doelkaart.md)
- [AI Safety Checklist](../../07-compliance-hub/08-ai-safety-checklist.md)
- [Incident Respons](../../07-compliance-hub/05-incidentrespons.md)
