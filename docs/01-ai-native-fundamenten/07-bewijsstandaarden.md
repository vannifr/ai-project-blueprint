---
versie: '1.0'
laatst_herzien: '2026-02-01'
---

# 1. Bewijsstandaarden

## 1. Doel

Deze module definieert **minimale bewijsstandaarden** voor AI-oplossingen, zodat Gate Reviews niet op gevoel maar op **toetsbare criteria** plaatsvinden.

**Kernprincipe:**
Een AI-oplossing mag pas door naar de volgende fase als het bewijs voldoet aan de normen voor het gekozen **risiconiveau** (zie Risicobeheersing & Compliance) en **Samenwerkingsmodus** (zie AI-Samenwerkingsmodi).

______________________________________________________________________

## 2. Scope (waar geldt dit voor?)

Deze standaarden gelden voor:

- Generatieve AI (tekst/beeld/advies)
- AI die classificatie/extractie doet
- AI die beslissingen ondersteunt (advies) of uitvoert (agent/actie)

Niet bedoeld voor:

- Zuivere BI-rapportage zonder AI-besluitvorming
- Simpele regels/automatisering zonder model

______________________________________________________________________

## 3. Definities (zodat termen toetsbaar zijn)

### Foutclassificatie

- **Kritiek:** overtreding Rode Lijnen (privacy-lek, verboden advies, discriminatoire output, gevaarlijke instructies, misleidende transparantie).
    **Norm:** 0 toegestaan.
- **Major:** inhoudelijk fout met reële kans op schade of verkeerde beslissing.
    **Norm:** zeer beperkt (zie tabel).
- **Minor:** stijl/format/kleine onvolledigheid zonder besluit-impact.

### "Significant prestatieverloop"

Prestatieverloop is **significant** als één van onderstaande optreedt t.o.v. de nulmeting:

- **Feitelijkheid daalt ≥ 2 procentpunten** (bijv. van 99% naar 97%)
- **Relevantie-score daalt ≥ 0,3** op een 1–5 schaal
- **Aantal Major fouten stijgt ≥ 50%** over twee opeenvolgende meetperioden

*(Let op: precieze drempels mogen per use-case strenger, maar niet soepeler zonder expliciet akkoord van Guardian.)*

______________________________________________________________________

## 4. Vereiste bewijsstukken (evidence pack)

Elke Gate Review baseert zich minimaal op deze documenten:

1. **[Gouden Set Test & Acceptatie Protocol](../09-sjablonen/07-validatie-bewijs/template.md)** (de aanpak)
1. **[Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md)** (de resultaten + conclusie)
1. **[Technische Modelkaart](../09-sjablonen/02-business-case/modelkaart.md)** (wat draait er precies)
1. **[Doelkaart](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)** (wat moest het doen + Rode Lijnen)
1. **[Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)** (risicoklasse)

______________________________________________________________________

## 5. Minimale eisen aan testsets ("Gouden Set")

| Risiconiveau | Minimale grootte Gouden Set | Verplichte onderdelen                                        |
| ------------ | --------------------------: | ------------------------------------------------------------ |
| **Minimaal** |                    20 cases | 80% standaardcases + 20% randgevallen                        |
| **Beperkt**  |                    50 cases | 80% standaard + 15% complex + 5% adversarial                 |
| **Hoog**     |                   150 cases | 70% standaard + 20% complex + 10% adversarial + fairness set |

**Extra regels (alle niveaus):**

- Testcases zijn **realistische praktijkvoorbeelden** (geen synthetische "happy flow only").
- Elke testcase heeft: **verwachte uitkomst** of **beoordelingscriteria**.
- Adversarial set bevat expliciet: jailbreaks, prompt-injectie, policy-omzeiling, "verzin bron"-trucs.
- **Synthetische Data Generatie:** Om de workload van 150+ testcases te verlichten, mag gebruik worden gemaakt van een "red-teaming AI" om concept-testcases te genereren. **Eis:** Een menselijk expert moet elke gegenereerde testcase en het "verwachte antwoord" (Ground Truth) valideren en goedkeuren voor opname in de Gouden Set.

______________________________________________________________________

## 6. Meetcriteria en minimale normen (per risiconiveau)

> *Als jouw gebruikscasus geen "accuracy" heeft (bijv. generatieve tekst), gebruik je "Feitelijkheid", "Compleetheid" en "Relevantie" als primaire maatstaven.*

### Normtabel

| Criterium                                          |           Minimaal risico |                  Beperkt risico |                                     Hoog risico |
| -------------------------------------------------- | ------------------------: | ------------------------------: | ----------------------------------------------: |
| **Kritieke fouten**                                |                         0 |                               0 |                                               0 |
| **Major fouten (max)**                             |            ≤ 2 in testset |                  ≤ 1 in testset |           ≤ 0–1 in testset *(Guardian beslist)* |
| **Feitelijkheid** *(geen feitelijke onjuistheden)* |                     ≥ 98% |                           ≥ 99% |                                         ≥ 99,5% |
| **Relevantie (1–5)**                               |                     ≥ 4,0 |                           ≥ 4,2 |                                           ≥ 4,5 |
| **Veiligheid: "moet weigeren" prompts**            |            100% weigering |                  100% weigering |                                  100% weigering |
| **Transparantie (AI-disclaimer waar vereist)**     | n.v.t./100% indien extern |      100% indien van toepassing |                      100% indien van toepassing |
| **Eerlijkheidstoets** *(bias)*                     |    kwalitatief (Guardian) |     kwali + kwant waar mogelijk |                 verplicht kwant + mitigatieplan |
| **Audit trail (logging compleetheid)**             |         minimaal metadata | 100% metadata + sampling output |         100% input/output + herleidbare context |
| **Stabiliteit** *(variatie over runs)*             |                 monitoren |    beperkte variatie toegestaan | strikt: variatie moet verklaard/acceptabel zijn |

### Eerlijkheid (bias) — minimale norm (kort en toetsbaar)

- **Beperkt:** als er relevante groepen te onderscheiden zijn, dan geldt: verschil in **Major-foutpercentage** tussen groepen ≤ **10%**.
- **Hoog:** verschil in **Major-foutpercentage** tussen groepen ≤ **5%**, plus beschreven mitigatie als er afwijkingen zijn.

*(Als groepslabels ontbreken of privacygevoelig zijn: Guardian bepaalt een kwalitatieve toets + mitigatie.)*

______________________________________________________________________

## 7. Logging-eisen (audit trail)

### Wat loggen we minimaal?

- **Datum/tijd**, gebruiker/rol (gehashte ID waar nodig)
- **Gebruikscasus / endpoint**
- **Modelnaam + versie**
- **Prompt-/Sturingsinstructies versie**
- **Bronnen gebruikt** (bij Kenniskoppeling: document-ID's/URLs)
- **Output**
- **Human override** (ja/nee + reden)

### Retentie (basis)

- **Minimaal/Beperkt:** standaard 90 dagen, tenzij anders vereist.
- **Hoog risico:** standaard 12 maanden (of langer indien wettelijke plicht).

*(Afstemmen met privacybeleid; pseudonimiseer waar mogelijk.)*

______________________________________________________________________

## 8. Bewijs per Gate (praktisch)

- **Gate 1 (Go/No-Go Ontdekking) (naar Bewijsvoering):** 09.01 + 09.02 (draft) + 09.03 + Data-Evaluatie afgerond.
- **Gate 2 (Investering PoV) (naar Realisatie):** 09.06 (pilotresultaten) + 09.04 (concept) + akkoord Guardian op Rode Lijnen.
- **Gate 3 (Productie-klaar) (naar Livegang/Levering):** 09.06 (release candidate) voldoet aan normen uit §6 + logging-plan + incidentprocedure.
- **Gate 4 (Livegang) (naar Beheer):** nulmeting vastgelegd + monitoring/feedback-loop ingericht.
