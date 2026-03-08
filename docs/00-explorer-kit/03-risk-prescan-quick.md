---
versie: '1.0'
---

# Risk Pre-Scan Quick

## 1. Doel

Deze verkorte risicoscan identificeert de meest kritische blokkades voor uw AI-prototype in **20–30 minuten**. Voer dit uit op dag 3–4 van de [30-Dagen Verkenner Kit](01-30-dagen-plan.md).

!!! info "Relatie tot de volledige Pre-Scan"
    Dit is een vereenvoudigde versie van de [volledige Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md). Bij oranje of rood resultaat, of bij twijfel, voert u altijd de volledige versie uit.

______________________________________________________________________

**Project:** \[Naam\]
**Ingevuld door:** \[Naam + rol\]
**Datum:** \[Datum\]

______________________________________________________________________

## 2. Deel A — Harde Blokkades (Stop-vragen)

*Als u één van deze vragen met "Ja" beantwoordt: **STOP dit project direct** en raadpleeg de [Compliance Hub](../07-compliance-hub/index.md).*

!!! danger "Verboden praktijken (EU AI Act Art. 5)"

- [ ] Gebruikt het systeem subliminale of manipulatieve technieken om menselijk gedrag te beïnvloeden zonder dat de persoon het weet?
- [ ] Past het systeem biometrische categorisering toe op basis van gevoelige kenmerken (ras, politieke opvattingen, religie)?
- [ ] Voert het systeem real-time biometrische identificatie uit in openbare ruimten?
- [ ] Beoordeelt het systeem personen op basis van sociaal gedrag ("social scoring")?

**→ Indien één of meer "Ja": PROJECT BLOKKADE. Raadpleeg [EU AI Act](../07-compliance-hub/01-eu-ai-act/index.md).**

______________________________________________________________________

## 3. Deel B — Hoog-Risico Indicatoren

*Score elke vraag: 0 = Nee / 1 = Gedeeltelijk / 2 = Ja*

### B1 — Toepassingsdomein

| Vraag                                                                             | Score (0/1/2) |
| :-------------------------------------------------------------------------------- | :------------ |
| Wordt het systeem ingezet in kritieke infrastructuur (energie, water, transport)? |               |
| Beslist het over toegang tot onderwijs, werk of sociale voorzieningen?            |               |
| Beslist het over krediet, verzekering of financiële diensten?                     |               |
| Wordt het ingezet in rechtshandhaving, migratie of justitie?                      |               |
| Heeft het systeem invloed op veiligheid (fysiek letsel mogelijk)?                 |               |

**Subtotaal B1:** \_\_\_/10

### B2 — Data & Privacy

| Vraag                                                                                           | Score (0/1/2) |
| :---------------------------------------------------------------------------------------------- | :------------ |
| Verwerkt het systeem persoonsgegevens (AVG/GDPR)?                                               |               |
| Bevat de trainings- of inferentiedata bijzondere categorieën (gezondheid, politiek, biometrie)? |               |
| Wordt data van minderjarigen verwerkt?                                                          |               |
| Is de datasource extern/onbekend (bijv. web scraping)?                                          |               |
| Worden gebruikersinteracties opgeslagen zonder expliciete toestemming?                          |               |

**Subtotaal B2:** \_\_\_/10

### B3 — Autonomie & Impact

| Vraag                                                                                         | Score (0/1/2) |
| :-------------------------------------------------------------------------------------------- | :------------ |
| Neemt het systeem beslissingen zonder menselijke tussenkomst die impact hebben op individuen? |               |
| Zijn de gevolgen van een fout moeilijk terug te draaien?                                      |               |
| Zijn er geen alternatieve controlemaatregelen als het systeem faalt?                          |               |
| Heeft het systeem directe interactie met eindgebruikers die niet weten dat het AI is?         |               |
| Raakt het systeem aan arbeidsrechtelijke beslissingen (beoordeling, selectie, ontslag)?       |               |

**Subtotaal B3:** \_\_\_/10

______________________________________________________________________

## 4. Scoreberekening

**Totaalscore Deel B:** Subtotaal B1 + B2 + B3 = \_\_\_/30

| Totaalscore | Kleurcode     | Interpretatie                             | Actie                                                                                                     |
| :---------- | :------------ | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| 0–6         | 🟢 **Groen**  | Laag risico — ga door                     | Documenteer en ga naar dag 5                                                                              |
| 7–15        | 🟡 **Oranje** | Verhoogd risico — aanvullende maatregelen | Voer volledige Pre-Scan uit; plan risicosessie met stakeholder                                            |
| 16–30       | 🔴 **Rood**   | Hoog risico — stop of herdefinieer        | Voer [volledige Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) uit; raadpleeg juridisch adviseur |

______________________________________________________________________

## 5. Deel C — Transparantie & Governance (Basischecks)

*Altijd invullen, ongeacht score Deel B.*

!!! check "Minimale vereisten voor prototype"

- [ ] **Transparantie:** Eindgebruikers weten dat ze met een AI-systeem werken (geen verborgen AI)
- [ ] **Menselijk toezicht:** Er is altijd een mens die de AI-output kan controleren en corrigeren
- [ ] **Rode Lijnen:** We hebben minimaal 2 concrete grenzen gedefinieerd aan wat het systeem NOOIT doet
- [ ] **Logging:** We loggen inputs en outputs van het prototype (ook voor troubleshooting)
- [ ] **Verantwoordelijke:** Er is één persoon die eindverantwoordelijkheid draagt voor dit systeem

______________________________________________________________________

## 6. Conclusie & Vervolgstap

**Risicoscore:** \[ \] Groen    \[ \] Oranje    \[ \] Rood

**Opmerkingen:**

\[Noteer specifieke risico's die extra aandacht verdienen, ook als de totaalscore groen is.\]

**Vastgestelde Rode Lijnen:**

1. \[Bijv. Het systeem verstuurt nooit automatisch communicatie zonder menselijke goedkeuring.\]
1. \[Bijv. Het systeem verwerkt nooit persoonsgegevens buiten de EU zonder expliciete toestemming.\]

**Vervolgstap:**

- [ ] Groen: Documenteer in [Project Charter Light](02-project-charter-light.md), sectie 5, en ga verder
- [ ] Oranje: Plan risicosessie en voer [volledige Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md) uit vóór dag 9
- [ ] Rood: Bespreek met Sponsor. Overweeg herdefiniëring van de use case

______________________________________________________________________

## 7. Gerelateerde Modules

- [Volledige Risico Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)
- [EU AI Act Overzicht](../07-compliance-hub/01-eu-ai-act/index.md)
- [Risicoclassificatie Framework](../01-ai-native-fundamenten/05-risicoclassificatie.md)
- [AI-Samenwerkingsmodi (HAS-H)](../00-strategisch-kader/06-has-h-niveaus.md)
- [Privacy & Data Blad](../09-sjablonen/11-privacy-data/privacyblad.md)
