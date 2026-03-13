# Implementatieplan — AI Project Blauwdruk v2.3+

**Versie:** 1.0
**Datum:** 13 maart 2026
**Status:** Definitief
**Eigenaar:** AI PM / Hoofdredacteur

Dit plan vertaalt de redactionele audit van maart 2026 naar een geordende uitvoeringsagenda. Elk item heeft een doel, scope, concrete acties, acceptatiecriteria en prioriteit.

______________________________________________________________________

## Uitgangspunten

1. **Taal:** Alleen Nederlands (standaard) en Engels. Geen FR/DE.
1. **Anti-redundantie:** Alle dubbele uitleg wordt verwijderd na voltooiing van IP-02.
1. **Single Source of Truth:** Elk kernconceptus heeft één canoniek document; alle andere verwijzen daarnaar.
1. **Prioriteitvolgorde:** Blokkerend (IP-01–02) → Structureel (IP-03–06) → Inhoudelijk (IP-07–10) → Kwaliteit (IP-11–14)

______________________________________________________________________

## IP-01 — Samenwerkingsmodi integreren in alle gate-documenten

**Prioriteit:** KRITIEK — blokkeert geloofwaardige gate-reviews
**Scope:** `docs/09-sjablonen/08-gate-reviews/`, alle fase-modules (02–06), Project Charter

**Probleem:** De samenwerkingsmodi (Modus 1–5) zijn het meest onderscheidende concept van de Blauwdruk, maar ze verschijnen niet als ontwerpbeperking bij gate-reviews. Gates zijn daardoor incompleet.

**Acties:**

1. Voeg aan de Gate Review Checklist (alle 4 gates) een verplicht veld toe:
    ```
    Samenwerkingsmodus: [Modus X — naam]
    Bijbehorende bewijsvereisten: [verwijzing naar 01.07]
    ```
1. Voeg in het Project Charter template een veld toe: "Beoogde samenwerkingsmodus" met dropdown-uitleg (1–5).
1. Voeg aan elke fase-module (02–06) in de exit-criteria-sectie 1 zin toe die de modus koppelt aan de gate.
1. Verwijder alle stand-alone uitleg van de modi uit fase-modules — vervang door links naar `06-has-h-niveaus.md` (bestandsnaam ongewijzigd; displaynaam is "Samenwerkingsmodi").

**Acceptatiecriteria:**

- Elke gate-checklist bevat het modus-veld
- Geen fase-module herhaalt de definitie van de modi
- Project Charter heeft een modus-keuze als verplicht veld

**Geschatte omvang:** 8–12 bestanden aanpassen

______________________________________________________________________

## IP-02 — Redundantie verwijderen: één canonieke uitleg per kernconceptus

**Prioriteit:** KRITIEK — schaadt de autoriteit van het playbook
**Scope:** Alle fase-modules (02–06), Module 01, Module 00

**Probleem:** De AI-levenscyclus, kernartefacten en risicoclassificatie worden 3–4 keer uitgelegd. Dit vergroot het document onnodig, veroorzaakt inconsistentie en ondermijnt de "single source" filosofie.

**Acties:**

1. Maak een **inventaris** van alle passages die kernconcepten dubbel uitleggen (grep op "5 fasen", "Rode Lijnen", "Doeldefinitie", "risicoclassificatie" etc.).
1. Behoud de volledige uitleg **alleen** in de canonieke thuisdocumenten (zie tabel in STYLE_GUIDE.md).
1. Vervang alle duplicaten door een standaard verwijzingsblok:
    ```markdown
    !!! info "Verwijzing"
        Dit onderdeel maakt gebruik van [Conceptnaam](pad/naar/canoniek-document.md).
        Raadpleeg dat document voor de volledige uitleg.
    ```
1. Controleer na aanpassing dat het totale export-volume meetbaar daalt (target: >10% minder woorden in Modules 02–06).

**Acceptatiecriteria:**

- 0 modules bevatten een herhaling van de levenscyclus-definitie
- 0 modules bevatten een herhaling van de kernartefact-definitie
- Export-volume Modules 02–06 daalt met minimaal 10%

**Geschatte omvang:** 15–20 bestanden aanpassen

______________________________________________________________________

## IP-03 — CTA-blokken toevoegen aan alle Laag-2 modules

**Prioriteit:** HOOG — verbetert navigatie en conversie
**Scope:** Alle fase-modules (02–06), Module 10 (Doorlopende Verbetering), Module 11 (Afsluiting), Module 12 (90-Dagen Roadmap)

**Probleem:** Modules eindigen abrupt. Lezers weten niet wat de volgende stap is na het lezen van een fase-module.

**Acties:**

1. Voeg aan elke Laag-2 module een `______` gevolgd door een **"Volgende stap"-blok** toe als laatste sectie.
1. CTA formaat (zie STYLE_GUIDE.md § Module-CTA):
    - Één concrete actie
    - Link naar het primaire sjabloon van die fase
    - Maximaal 3 "Zie ook"-links
1. Prioriteer fase-eindpunten: einde van activiteiten-pagina's (02-activiteiten.md t/m 06-activiteiten.md).
1. Voeg de bijbehorende EN-versie gelijktijdig bij.

**Acceptatiecriteria:**

- Alle 10+ activiteiten-pagina's hebben een CTA-blok
- Elk CTA verwijst naar een bestaand sjabloon (geen dode links)
- EN- en NL-versies zijn gesynchroniseerd

**Geschatte omvang:** 10–15 bestanden aanpassen

______________________________________________________________________

## IP-04 — Module 15 (Accelerators) voltooien of depreciëren

**Prioriteit:** HOOG — lege module ondermijnt geloofwaardigheid
**Scope:** `docs/15-accelerators/`

**Probleem:** Module 15 staat in de navigatie maar bevat minimale content. Bezoekers die doorklikken vinden een incomplete sectie. Dit schaadt het vertrouwen in het gehele playbook.

**Keuze (beslis vóór uitvoering):**

- **Optie A — Voltooien:** Maak voor elk van de drie transformation tracks (Strategisch, Operationeel, AI-First) minimaal 1 concrete accelerator-tool:
    - Quick-scan checklist (1–2 pagina's)
    - Decision template
    - Faseversneller (bijv. "Hoe van 13 weken naar 6 weken voor Minimaal Risico-projecten")
- **Optie B — Depreciëren:** Verwijder Module 15 uit de navigatie. Voeg een `!!! info "Binnenkort"` admonition toe met een verwachte datum. Verwijder de vermelding in mkdocs.yml nav.

**Aanbeveling:** Optie A als er binnen 4 weken schrijfcapaciteit is; anders Optie B.

**Acceptatiecriteria (Optie A):**

- Minimaal 3 invulbare tools aanwezig (1 per track)
- Elke tool verwijst terug naar de relevante fase-modules
- EN-versie gesynchroniseerd

**Acceptatiecriteria (Optie B):**

- Module 15 verwijderd uit mkdocs.yml nav
- Placeholder aanwezig met "Binnenkort beschikbaar" + verwachte datum

**Geschatte omvang:** 6–10 nieuwe bestanden (Optie A) of 2 aanpassingen (Optie B)

______________________________________________________________________

## IP-05 — Geanonimiseerde praktijkvoorbeelden toevoegen

**Prioriteit:** HOOG — maakt het playbook geloofwaardig voor sceptische lezers
**Scope:** Primair `docs/17-bijlagen/`, secundair 1 voorbeeld per risicoklasse in fase-modules

**Probleem:** Het playbook is methodologisch sterk maar abstract. Organisaties die twijfelen of de aanpak "echt werkt" vinden geen bewijsmateriaal.

**Acties:**

1. Schrijf **3 geanonimiseerde mini-cases** (formaat: zie STYLE_GUIDE.md § Praktijkvoorbeelden):
    - **Case 1 — Minimaal Risico:** bijv. interne kennisbot (overheid of professionele dienstverlening)
    - **Case 2 — Beperkt Risico:** bijv. klantenservice-automatisering (retail of financiën)
    - **Case 3 — Hoog Risico:** bijv. CV-screening of kredietbeoordeling (HR of financiën)
1. Lange versie (500–800 woorden per case) in `docs/17-bijlagen/praktijkvoorbeelden.md`.
1. Korte versie (4–6 regels, admonition-formaat) in de meest relevante fase-module:
    - Case 1 → `docs/02-fase-ontdekking/01-doelstellingen.md`
    - Case 2 → `docs/03-fase-validatie/01-doelstellingen.md`
    - Case 3 → `docs/07-compliance-hub/` (risicoclassificatie)
1. EN-versie van bijlage gelijktijdig aanmaken.

**Acceptatiecriteria:**

- 3 cases beschikbaar in bijlage
- 3 mini-cases als admonition in fase-modules
- Alle cases vermelden sector, risicoklasse en toegepaste Blauwdruk-onderdelen
- Geen namen van organisaties of individuen

**Geschatte omvang:** 2 nieuwe bestanden + 3 aanpassingen

______________________________________________________________________

## IP-06 — Green AI integreren in fase-sjablonen

**Prioriteit:** HOOG — toekomstige compliance-vereiste (CSRD, EU AI Act reporting)
**Scope:** Business Case template, Risk Pre-Scan template, Fase 5 monitoring-module

**Probleem:** Green AI bestaat als technische standaard maar is geïsoleerd. Het verschijnt niet in de fase-sjablonen waar het beslissend is (bij de business case en bij monitoring).

**Acties:**

1. **Business Case template** (`docs/09-sjablonen/04-business-case/template.md`):
    - Voeg verplicht veld toe: "Ecologische voetafdruk"
    - Sub-velden: Inferentiekosten (CO₂ schatting), Trainingskosten (indien van toepassing), Vergelijking met baseline
    - Verwijzing naar Green AI-standaard in `docs/08-technische-standaarden/`
1. **Risk Pre-Scan template** (`docs/09-sjablonen/02-risk-pre-scan/template.md`):
    - Voeg trigger-vraag toe: "Vereist het systeem continue inferentie op grote schaal (>1.000 calls/dag)?"
    - Bij "ja": verplichte verwijzing naar Green AI-standaard
1. **Fase 5 — Beheer & Optimalisatie** (`docs/06-fase-monitoring/`):
    - Voeg in de driftmeting-sectie een paragraaf toe over kostenefficiëntie als KPI
    - Verwijs naar Green AI benchmarks
1. EN-versies van alle aangepaste bestanden synchroniseren.

**Acceptatiecriteria:**

- Business Case template heeft een "Ecologische voetafdruk" veld
- Risk Pre-Scan heeft de grote-schaal trigger
- Fase 5 vermeldt kostenefficiëntie als monitording-KPI
- Geen Green AI-uitleg wordt gedupliceerd in fase-modules (alles verwijst naar technische standaard)

**Geschatte omvang:** 4–6 bestanden aanpassen

______________________________________________________________________

## IP-07 — VP-10 voltooien: Besluitvormingsmatrix rollen & verantwoordelijkheden

**Prioriteit:** MEDIUM — lost bekende rolonduidelijkheid op (openstaand backlog-item)
**Scope:** `docs/08-rollen-en-verantwoordelijkheden/`

**Probleem:** Wie heeft de eindbeslissing bij Gate 1/2/3? AI PM is "operationeel" maar ook "accountable" voor de business case. Guardian heeft stop-recht maar geen veto op business-beslissingen. Dit is niet expliciet vastgelegd.

**Acties:**

1. Maak een **Besluitvormingsmatrix** (1 pagina) als nieuw bestand `docs/08-rollen-en-verantwoordelijkheden/besluitvormingsmatrix.md`:
    | Beslissing                        | Verantwoordelijk | Veto-recht    | Informeren       |
    | --------------------------------- | ---------------- | ------------- | ---------------- |
    | Go/No-Go Gate 1 (probleemdef.)    | Sponsor          | Guardian (RL) | AI PM, Tech Lead |
    | Go/No-Go Gate 2 (investering)     | Sponsor          | Guardian (RL) | AI PM, Finance   |
    | Go/No-Go Gate 3 (productie)       | Sponsor + Tech   | Guardian (RL) | AI PM, Legal     |
    | Stop-beslissing (circuit breaker) | Guardian         | —             | Sponsor, AI PM   |
    | Technische haalbaarheid           | Tech Lead        | —             | AI PM            |
1. Voeg expliciete vermelding toe: "Sponsor is eindverantwoordelijk voor go/no-go; Guardian heeft stop-recht op Rode Lijnen; Tech Lead tekent voor technische haalbaarheid."
1. Link vanuit alle gate-checklists naar dit document.
1. EN-versie aanmaken.

**Acceptatiecriteria:**

- Besluitvormingsmatrix bestaat als apart document
- Alle 4 gate-checklists linken ernaar
- Geen dubbelzinnigheid over wie de eindbeslissing heeft bij elke gate

**Geschatte omvang:** 1 nieuw bestand + 4 aanpassingen

______________________________________________________________________

## IP-08 — Toon harmoniseren: redactionele ronde Modules 02–07

**Prioriteit:** MEDIUM — verbetert professionele uitstraling
**Scope:** Modules 02–07 (operationele fasen + compliance hub)

**Probleem:** Sommige modules zijn academisch/formeel (compliance hub), andere zijn praktisch/directief (90-dagenplan, sjablonen). Voor een consulting-grade product signaleert dit multi-auteur-drift.

**Acties:**

1. Maak een **toon-audit** van alle Laag-2 modules: markeer elke passage die passief, academisch of onduidelijk is.
1. Voer een **redactionele ronde** uit per module:
    - Verander passieve constructies naar actief
    - Vervang "zal worden" en "dient te worden" door directe werkwoorden
    - Zorg dat elke H2-sectie begint met een imperatief of een direct handelingswoord
1. Prioriteer de compliance hub — deze is het meest academisch van toon en bereikt juist de Guardian/Legal-doelgroep die direct wil handelen.
1. EN-versies synchroon bijwerken.

**Acceptatiecriteria:**

- Geen passief-zinnen in kernactiviteiten-secties van fase-modules
- Compliance hub gebruikt dezelfde instructieve toon als de fase-modules
- Toon-check toegevoegd aan de publicatiechecklist in STYLE_GUIDE.md (reeds gedaan in v2.3)

**Geschatte omvang:** 20–25 bestanden aanpassen (redactioneel, geen structuurwijzigingen)

______________________________________________________________________

## IP-09 — VP-12 voltooien: "Levenscyclus in 1 pagina" maken

**Prioriteit:** MEDIUM — ondersteunt IP-02 en verbetert onboarding
**Scope:** `docs/00-strategisch-kader/` (nieuw bestand of uitbreiding van 01-ai-levenscyclus.md)

**Probleem:** De volledige levenscyclus wordt herhaald in meerdere modules omdat er geen compacte referentiekaart bestaat. Als die er is, kunnen modules ernaar verwijzen.

**Acties:**

1. Maak een **"AI Levenscyclus — snelle referentie"** (max. 1 pagina / 400 woorden) in `docs/00-strategisch-kader/00-levenscyclus-referentie.md`:
    - Tabel: 5 fasen × kolommen: doel, gate, kernactiviteit, primair sjabloon
    - Geen uitleg — alleen verwijzingen
1. Voeg dit document toe aan de nav als eerste item onder Strategisch Kader.
1. Verwijs vanuit alle fase-modules naar dit document als entry point.
1. EN-versie aanmaken.

**Acceptatiecriteria:**

- Document bestaat, max. 400 woorden, bevat de tabel
- Aanwezig in mkdocs.yml nav
- Fase-modules (02–06) linken naar dit document in hun intro-sectie

**Geschatte omvang:** 1 nieuw bestand + 5 aanpassingen in fase-modules

______________________________________________________________________

## IP-10 — VP-14 voltooien: Bronnen uitbreiden + EU AI Act op artikelniveau

**Prioriteit:** MEDIUM — verhoogt autoriteit en bruikbaarheid voor compliance
**Scope:** `docs/16-bronnen/index.md`, `docs/17-bijlagen/`

**Probleem:** Bronvermelding is sterk op strategisch niveau maar mist praktische referenties (MLOps, data governance) en EU AI Act-verwijzingen op artikelniveau.

**Acties:**

1. Voeg secties toe aan `docs/16-bronnen/index.md`:
    - **EU AI Act (artikelniveau):** Bijlage III (hoog risico), Art. 9 (risk management), Art. 13 (transparantie), Art. 17 (quality management), Art. 61 (post-market monitoring)
    - **Data governance & privacy:** ISO/IEC 27701, EDPB guidelines, NIST Privacy Framework
    - **MLOps & monitoring:** Google MLOps whitepaper, Microsoft MLOps maturity model, OECD AI Principles
    - **Duurzaamheid:** Green Software Foundation, EU Green Deal Digital Strategy
1. Voeg bij elke bron een 2-zinsannotatie toe: wat is het en wanneer gebruik je het.
1. EN-versie synchroniseren.

**Acceptatiecriteria:**

- Bronnenlijst bevat minimaal 5 nieuwe praktische referenties
- EU AI Act verwijzingen zijn op artikelniveau (niet alleen "EU AI Act" als generieke bron)
- Elke bron heeft een korte annotatie

**Geschatte omvang:** 1 bestand uitbreiden (NL + EN)

______________________________________________________________________

## IP-11 — VP-13 voltooien: Organisatieprofielen met exit-criteria en actiepaden

**Prioriteit:** MEDIUM — maakt Module 13 actionabel
**Scope:** `docs/13-organisatieprofielen/`

**Probleem:** De drie profielen (Verkenner, Bouwer, Visionair) beschrijven kenmerken maar geven geen duidelijke overgangsroute.

**Acties:**

1. Voeg per profiel toe:
    - **Instapcriteria** (5 meetbare criteria om te bepalen of je in dit niveau zit)
    - **Exitcriteria** (wat moet je aantonen om naar het volgende niveau te gaan)
    - **Top-5 acties** (de vijf meest impactvolle acties voor dit niveau)
    - **Meetpunten** (KPI's: bijv. % use cases met Doelkaart, % met testset, aantal incidenten)
1. Voeg een **zelfbeoordelingsvragenlijst** (15 ja/nee-vragen) toe als bijlage of sectie.
1. EN-versie synchroniseren.

**Acceptatiecriteria:**

- Elk profiel heeft instapcriteria, exitcriteria, top-5 acties en meetpunten
- Zelfbeoordelingsvragenlijst leidt tot een duidelijk profiel-oordeel
- Overgang tussen profielen is objectief toetsbaar

**Geschatte omvang:** 3–4 bestanden uitbreiden

______________________________________________________________________

## IP-12 — Engelse vertalingen voltooien voor hoog-traffic modules

**Prioriteit:** MEDIUM — ontsluit internationale doelgroep
**Scope:** Alle modules die nog geen volledige EN-versie hebben

**Hoog-prioriteit pagina's voor EN-vertaling (volgorde):**

| Module                         | Bestand                                          | Status            |
| :----------------------------- | :----------------------------------------------- | :---------------- |
| Compliance Hub index           | `07-compliance-hub/index.en.md`                  | 🔴 ontbreekt/stub |
| Fairness audit                 | `07-compliance-hub/fairness-audit.en.md`         | 🔴 ontbreekt      |
| Privacy-by-design              | `07-compliance-hub/privacy-by-design.en.md`      | 🔴 ontbreekt      |
| Rollen & Verantwoordelijkheden | `08-rollen-en-verantwoordelijkheden/index.en.md` | 🔴 ontbreekt      |
| Organisatieprofielen           | `13-organisatieprofielen/index.en.md`            | 🔴 ontbreekt      |
| Doorlopende Verbetering        | `10-doorlopende-verbetering/index.en.md`         | 🔴 ontbreekt      |
| Project Afsluiting             | `11-project-afsluiting/index.en.md`              | 🔴 ontbreekt      |
| Drie Tracks                    | `14-drie-tracks/index.en.md`                     | 🔴 ontbreekt      |

**Aanpak:**

1. Vertaal in volgorde van de bovenstaande tabel (compliance en rollen eerst — meest gevraagd door internationale bezoekers).
1. Na elke vertaling: voeg toe aan `mkdocs.yml` nav_translations.
1. Controleer cross-links (EN linkt naar EN).

**Acceptatiecriteria:**

- Alle 8 bovenstaande bestanden zijn volledig vertaald
- Geen EN-pagina linkt naar een NL-bestand zonder `(NL)` suffix-notatie
- mkdocs.yml nav_translations bijgewerkt

**Geschatte omvang:** 8–10 nieuwe bestanden

______________________________________________________________________

## IP-13 — Accelerators (IP-04) koppelen aan 90-Dagenplan

**Prioriteit:** LAAG — vervolgstap na IP-04
**Afhankelijkheid:** IP-04 moet voltooid zijn

**Acties:**

1. Voeg in Module 12 (90-Dagenplan) per week een verwijzing toe naar de relevante accelerator-tool.
1. Maak een "versnelde route" variant voor Minimaal Risico (6–8 weken) als aparte view of tabel.

**Acceptatiecriteria:**

- 90-dagenplan bevat links naar accelerator-tools per week
- Minimaal Risico fast-lane is als zelfstandig schema leesbaar

______________________________________________________________________

## IP-14 — Validate_docs.py uitbreiden met nieuwe controles

**Prioriteit:** LAAG — automatiseert handhaving van v2.3-regels
**Scope:** `scripts/validate_docs.py`

**Acties:**

1. Voeg controle toe: bevat elke Laag-2 module een `**Volgende stap:**` CTA-blok?
1. Voeg controle toe: bevat elke gate-checklist het woord "Samenwerkingsmodus"?
1. Voeg controle toe: bevat geen fase-module de frase "vijf fasen zijn" of "de levenscyclus bestaat uit" (redundantie-marker)?
1. Rapporteer overtredingen als warnings (niet als fouten — niet blokkerend voor CI).

**Acceptatiecriteria:**

- Script draait zonder fouten op huidige codebase
- Nieuwe controles produceren 0 warnings na voltooiing van IP-01–03

______________________________________________________________________

## Uitvoervolgorde (aanbevolen)

| Ronde | Items               | Reden                                                                                       |
| :---- | :------------------ | :------------------------------------------------------------------------------------------ |
| **1** | IP-01, IP-02        | Blokkerend — gates zijn incompleet zonder Samenwerkingsmodi, redundantie schaadt autoriteit |
| **2** | IP-03, IP-04        | Structureel — navigatie en module-completheid                                               |
| **3** | IP-05, IP-06        | Inhoudelijk — geloofwaardigheid en toekomstige compliance                                   |
| **4** | IP-07, IP-08, IP-09 | Kwaliteit — rollen, toon, referentiekaart                                                   |
| **5** | IP-10, IP-11, IP-12 | Uitbreiding — bronnen, profielen, vertalingen                                               |
| **6** | IP-13, IP-14        | Automatisering — koppeling en validatie                                                     |

______________________________________________________________________

## Relatie tot backlog

| Backlog-item       | Implementatieplan-item    | Status na IP-voltooiing |
| :----------------- | :------------------------ | :---------------------- |
| VP-10              | IP-07                     | ✅ Voltooid             |
| VP-12              | IP-02, IP-08, IP-09       | ✅ Voltooid             |
| VP-13              | IP-11                     | ✅ Voltooid             |
| VP-14              | IP-10                     | ✅ Voltooid             |
| Nieuw (audit 2026) | IP-01, IP-03–06, IP-12–14 | Nieuw toegevoegd        |

______________________________________________________________________

**Gerelateerde documenten:**

- [STYLE_GUIDE.md](STYLE_GUIDE.md) — schrijfregels v2.3
- [BACKLOG.md](BACKLOG.md) — geprioriteerde roadmap
- [INFORMATION_ARCHITECTURE.md](INFORMATION_ARCHITECTURE.md) — structuur en plaatsingsregels
