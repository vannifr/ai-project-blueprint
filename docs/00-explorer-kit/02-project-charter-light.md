---
versie: '1.0'
type: guide
layer: 2
roles: [AI Product Manager]
tags: [onboarding]
---

# Project Charter Light

## Instructies

Dit is een **vereenvoudigd 1-pagina projectkader** voor uw eerste AI-initiatief. Vul dit in met uw team tijdens de kick-off sessie op dag 1–2. De volledige versie vindt u in het [Project Charter](../09-sjablonen/01-project-charter/template.md).

!!! tip "Doe het in 60 minuten"
    Plan een gestructureerde sessie van 60 minuten. Behandel elke sectie in 10 minuten. Beslispunten die langer dan 10 minuten duren: noteer ze als open punt en ga door.

______________________________________________________________________

**Project:** \[Naam van het project\]
**Datum:** \[Datum\]
**AI PM:** \[Naam\]
**Sponsor:** \[Naam Opdrachtgever\]
**Versie:** 1.0

______________________________________________________________________

## Sectie 1 — Het Probleem (Het Waarom)

*Beschrijf het knelpunt dat u wilt oplossen. Focus op het probleem, niet op de technologie.*

**Wat is het knelpunt?**

\[Bijv. Klantenservice beantwoordt e-mails handmatig en doet hier gemiddeld 3 dagen over, wat leidt tot klachten.\]

**Wat is de impact van dit probleem?**

\[Bijv. 40 klachten per maand, 2 FTE besteden 30% van hun tijd aan repetitieve antwoorden.\]

**Wat is de huidige werkwijze?**

\[Bijv. Medewerkers lezen e-mails in Outlook en typen handmatig antwoorden op basis van een FAQ-document.\]

______________________________________________________________________

## Sectie 2 — De Oplossing (Het Wat)

*Beschrijf op één zin wat u gaat bouwen.*

**Oplossingsconcept (1 zin):**

\[Bijv. Een AI-assistent die inkomende e-mails samenvat en een concept-antwoord klaarzet, dat een medewerker goedkeurt vóór verzending.\]

**Samenwerkingsmodus** (kies één):

- [ ] **Modus 1 — Instrumenteel:** AI als tool (bijv. automatisch sorteren), geen interactie met eindgebruikers
- [x] **Modus 2 — Adviserend:** AI doet een suggestie, mens beslist en keurt goed *(aanbevolen voor Verkenners)*
- [ ] **Modus 3 — Collaboratief:** Mens en AI werken samen als gelijkwaardige partners
- [ ] **Modus 4 — Gedelegeerd:** AI voert zelfstandig uit, mens controleert uitzonderingen

!!! warning "Begin laag"
    Bij twijfel: kies één niveau lager. Modus 2 is de veiligste start voor een eerste prototype.

______________________________________________________________________

## Sectie 3 — Team & Rollen

| Rol                       | Naam                 | Tijdsbesteding   |
| :------------------------ | :------------------- | :--------------- |
| AI Projectmanager (AI PM) | \[Naam\]             | \[bijv. 50%\]    |
| Developer / Tech Lead     | \[Naam\]             | \[bijv. 80%\]    |
| Domeinexpert              | \[Naam\]             | \[bijv. 20%\]    |
| AI Guardian (optioneel)   | \[Naam of "n.v.t."\] | \[bijv. 10%\]    |
| Sponsor                   | \[Naam\]             | Review op dag 21 |

______________________________________________________________________

## Sectie 4 — Scope

**In scope (wat we wél doen):**

- \[Bijv. Prototype verwerkt inkomende e-mails uit de mailbox "klantenservice@org.nl"\]
- \[Bijv. Prototype genereert concept-antwoorden in het Nederlands\]
- \[Bijv. Prototype wordt getest op 20 historische e-mails\]

**Buiten scope (wat we NIET doen in deze 30 dagen):**

- Automatische verzending van e-mails (mens keurt altijd goed)
- Integratie met CRM-systeem
- Multi-taal ondersteuning
- GDPR-compliance auditrapportage (volgt in Bouwer-fase)

______________________________________________________________________

## Sectie 5 — Risico & Compliance (Samenvatting)

*Gebaseerd op de [Risk Pre-Scan Quick](03-risk-prescan-quick.md). Vul dit in na dag 3–4.*

**Risicoscore Pre-Scan:** \[ \] Groen    \[ \] Oranje    \[ \] Rood

**EU AI Act categorie:** \[ \] Geen/Minimaal    \[ \] Transparantieverplichting    \[ \] Hoog Risico

**Bevat persoonsgegevens:** \[ \] Ja — privacy-maatregelen: \[beschrijf\]    \[ \] Nee

**Rode Lijnen (wat doet het systeem NOOIT):**

- \[Bijv. Het systeem verstuurt nooit automatisch e-mails zonder menselijke goedkeuring.\]
- \[Bijv. Het systeem geeft nooit financieel of juridisch advies.\]

______________________________________________________________________

## Sectie 6 — Succes & Planning

**Definitie van succes op dag 21:**

\[Bijv. Prototype verwerkt 20 historische e-mails met ≥ 80% kwaliteitsscore op door domeinexpert beoordeelde conceptantwoorden.\]

**Gate 1 Review datum:** \[Datum, circa dag 21 vanaf start\]

**Go/No-Go criteria:**

| Criterium                  | Drempelwaarde         | Gemeten op dag |
| :------------------------- | :-------------------- | :------------- |
| Kwaliteitsscore Golden Set | ≥ 80%                 | Dag 16–17      |
| Prototype draait stabiel   | 0 crashes op 20 cases | Dag 16–17      |
| Sponsor is overtuigd       | Subjectief oordeel    | Dag 21         |

______________________________________________________________________

## Goedkeuring

| Rol     | Naam     | Datum     | Handtekening / E-mail bevestiging |
| :------ | :------- | :-------- | :-------------------------------- |
| AI PM   | \[Naam\] | \[Datum\] |                                   |
| Sponsor | \[Naam\] | \[Datum\] |                                   |

______________________________________________________________________

## Vervolgstappen

- [30-Dagen Plan](01-30-dagen-plan.md) — dag-tot-dag uitvoering
- [Risk Pre-Scan Quick](03-risk-prescan-quick.md) — voor sectie 5 van dit charter
- [Volledige Project Charter](../09-sjablonen/01-project-charter/template.md) — voor de Bouwer-fase
