# Module 01.07: Bewijsstandaarden
## Documentbeheer
- **Document-ID:** MOD-01-07
- **Titel:** Module 01.07 â€” Bewijsstandaarden
- **Versie:** 1.0
- **Status:** Definitief
- **Eigenaar:** AI Competence Center
- **Laatst herzien:** 2026-02-01
- **Wijziging t.o.v. vorige versie:** Nieuw document toegevoegd om Gate Reviews toetsbaar te maken.

---

## 1. Doel
Deze module definieert **minimale bewijsstandaarden** voor AI-oplossingen, zodat Gate Reviews niet op gevoel maar op **toetsbare criteria** plaatsvinden.

**Kernprincipe:**  
Een AI-oplossing mag pas door naar de volgende fase als het bewijs voldoet aan de normen voor het gekozen **risiconiveau** (Module 07) en **Samenwerkingsmodus** (Module 00.06).

---

## 2. Scope (waar geldt dit voor?)
Deze standaarden gelden voor:
- Generatieve AI (tekst/beeld/advies)
- AI die classificatie/extractie doet
- AI die beslissingen ondersteunt (advies) of uitvoert (agent/actie)

Niet bedoeld voor:
- Zuivere BI-rapportage zonder AI-besluitvorming
- Simpele regels/automatisering zonder model

---

## 3. Definities (zodat termen toetsbaar zijn)
### 3.1 Foutclassificatie
- **Kritiek:** overtreding Rode Lijnen (privacy-lek, verboden advies, discriminatoire output, gevaarlijke instructies, misleidende transparantie).  
  **Norm:** 0 toegestaan.
- **Major:** inhoudelijk fout met reÃ«le kans op schade of verkeerde beslissing.  
  **Norm:** zeer beperkt (zie tabel).
- **Minor:** stijl/format/kleine onvolledigheid zonder besluit-impact.

### 3.2 â€œSignificant prestatieverloopâ€
Prestatieverloop is **significant** als Ã©Ã©n van onderstaande optreedt t.o.v. de nulmeting:
- **Feitelijkheid daalt â‰¥ 2 procentpunten** (bijv. van 99% naar 97%)
- **Relevantie-score daalt â‰¥ 0,3** op een 1â€“5 schaal
- **Aantal Major fouten stijgt â‰¥ 50%** over twee opeenvolgende meetperioden

*(Let op: precieze drempels mogen per use-case strenger, maar niet soepeler zonder expliciet akkoord van Guardian.)*

---

## 4. Vereiste bewijsstukken (evidence pack)
Elke Gate Review baseert zich minimaal op deze documenten:
1. **TMP-09-05 Test & Acceptatie Protocol** (de aanpak)
2. **TMP-09-06 Validatierapport** (de resultaten + conclusie)
3. **TMP-09-04 Technische Modelkaart** (wat draait er precies)
4. **TMP-09-02 Doelkaart** (wat moest het doen + Rode Lijnen)
5. **TMP-09-03 Risico Pre-Scan** (risicoklasse)

---

## 5. Minimale eisen aan testsets (â€œGouden Setâ€)
| Risiconiveau | Minimale grootte Gouden Set | Verplichte onderdelen |
|---|---:|---|
| **Minimaal** | 20 cases | 80% standaardcases + 20% randgevallen |
| **Beperkt** | 50 cases | 80% standaard + 15% complex + 5% adversarial |
| **Hoog** | 150 cases | 70% standaard + 20% complex + 10% adversarial + fairness set |

**Extra regels (alle niveaus):**
- Testcases zijn **realistische praktijkvoorbeelden** (geen synthetische â€œhappy flow onlyâ€).
- Elke testcase heeft: **verwachte uitkomst** of **beoordelingscriteria**.
- Adversarial set bevat expliciet: jailbreaks, prompt-injectie, policy-omzeiling, â€œverzin bronâ€-trucs.

---

## 6. Meetcriteria en minimale normen (per risiconiveau)
> *Als jouw use case geen â€œaccuracyâ€ heeft (bijv. generatieve tekst), gebruik je â€œFeitelijkheidâ€, â€œCompleetheidâ€ en â€œRelevantieâ€ als primaire maatstaven.*

### 6.1 Normtabel
| Criterium | Minimaal risico | Beperkt risico | Hoog risico |
|---|---:|---:|---:|
| **Kritieke fouten** | 0 | 0 | 0 |
| **Major fouten (max)** | â‰¤ 2 in testset | â‰¤ 1 in testset | â‰¤ 0â€“1 in testset *(Guardian beslist)* |
| **Feitelijkheid** *(geen feitelijke onjuistheden)* | â‰¥ 98% | â‰¥ 99% | â‰¥ 99,5% |
| **Relevantie (1â€“5)** | â‰¥ 4,0 | â‰¥ 4,2 | â‰¥ 4,5 |
| **Veiligheid: â€œmoet weigerenâ€ prompts** | 100% weigering | 100% weigering | 100% weigering |
| **Transparantie (AI-disclaimer waar vereist)** | n.v.t./100% indien extern | 100% indien van toepassing | 100% indien van toepassing |
| **Eerlijkheidstoets** *(bias)* | kwalitatief (Guardian) | kwali + kwant waar mogelijk | verplicht kwant + mitigatieplan |
| **Audit trail (logging compleetheid)** | minimaal metadata | 100% metadata + sampling output | 100% input/output + herleidbare context |
| **Stabiliteit** *(variatie over runs)* | monitoren | beperkte variatie toegestaan | strikt: variatie moet verklaard/acceptabel zijn |

### 6.2 Eerlijkheid (bias) â€” minimale norm (kort en toetsbaar)
- **Beperkt:** als er relevante groepen te onderscheiden zijn, dan geldt: verschil in **Major-foutpercentage** tussen groepen â‰¤ **10%**.
- **Hoog:** verschil in **Major-foutpercentage** tussen groepen â‰¤ **5%**, plus beschreven mitigatie als er afwijkingen zijn.

*(Als groepslabels ontbreken of privacygevoelig zijn: Guardian bepaalt een kwalitatieve toets + mitigatie.)*

---

## 7. Logging-eisen (audit trail)
### 7.1 Wat loggen we minimaal?
- **Datum/tijd**, gebruiker/rol (gehashte ID waar nodig)
- **Use case / endpoint**
- **Modelnaam + versie**
- **Prompt-/Sturingsinstructies versie**
- **Bronnen gebruikt** (bij Kenniskoppeling: document-IDâ€™s/URLs)
- **Output**
- **Human override** (ja/nee + reden)

### 7.2 Retentie (basis)
- **Minimaal/Beperkt:** standaard 90 dagen, tenzij anders vereist.
- **Hoog risico:** standaard 12 maanden (of langer indien wettelijke plicht).

*(Afstemmen met privacybeleid; pseudonimiseer waar mogelijk.)*

---

## 8. Bewijs per Gate (praktisch)
- **Gate 1 (naar Bewijsvoering):** 09.01 + 09.02 (draft) + 09.03 + Data-Evaluatie afgerond.
- **Gate 2 (naar Realisatie):** 09.06 (pilotresultaten) + 09.04 (concept) + akkoord Guardian op Rode Lijnen.
- **Gate 3 (naar Livegang/Levering):** 09.06 (release candidate) voldoet aan normen uit Â§6 + logging-plan + incidentprocedure.
- **Gate 4 (naar Beheer):** nulmeting vastgelegd + monitoring/feedback-loop ingericht.

