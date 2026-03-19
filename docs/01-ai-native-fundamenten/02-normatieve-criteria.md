---
versie: '1.3'
type: foundation
layer: 1
---

# Toetsingscriteria & AI-Native Principes

!!! abstract "Doel"
    Deze pagina beschrijft de vijf kernprincipes die een AI-native aanpak onderscheiden van traditionele softwareontwikkeling, en de toetsingscriteria om te bepalen of een project onder deze principes valt.

______________________________________________________________________

## 1. Wanneer is dit van toepassing?

Een project valt onder de AI-native aanpak zodra het voldoet aan minstens twee van deze drie voorwaarden:

| Voorwaarde                 | Beschrijving                                                                                                  |
| :------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **Materiële impact**       | Het systeem beïnvloedt productie-outputs, beslissingen of klantinteracties.                                   |
| **Contextgestuurd gedrag** | Inputs die het gedrag sturen (prompts, RAG-bronnen, fine-tuning data) worden actief beheerd en geversioneerd. |
| **Niet-deterministisch**   | De output is probabilistisch — dezelfde input kan verschillende resultaten opleveren.                         |

> Zodra gekwalificeerd, gelden de vijf principes hieronder als leidraad voor governance, ontwikkeling en monitoring.

______________________________________________________________________

## 2. De Vijf AI-Native Principes

### Principe 1 — Gedragssturing boven modelkeuze

Het gedrag van een AI-systeem wordt primair bepaald door **specificaties, prompts en harde grenzen** — niet door welk model eronder draait. Investeer in helder gedefinieerd verwacht gedrag vóór je investeert in modeloptimalisatie.

**In de praktijk:**

- Schrijf een [Goal Card](../09-sjablonen/06-ai-native-artefacten/doelkaart.md) vóór je een model kiest.
- Definieer [Harde Grenzen](../09-sjablonen/12-cheatsheets/07-rode-lijnen.md) als ononderhandelbare randvoorwaarden.
- Behandel prompts als geversioneerde artefacten, niet als wegwerp-experimenten.

______________________________________________________________________

### Principe 2 — Proportionele governance

De zwaarte van controle, validatie en documentatie moet in verhouding staan tot het **risico** van het systeem. Een interne samenvattingstool vraagt om een lichtere aanpak dan een klantgericht beslissysteem.

**In de praktijk:**

- Gebruik de [Risicoclassificatie](05-risicoclassificatie.md) om het niveau te bepalen (Kritiek → Laag).
- [Fast Lane](../02-fase-ontdekking/06-fast-lane.md) voor minimaal risico; volledig traject voor hoog risico.
- Pas de bewijslast aan per Gate Review — niet elke gate vraagt dezelfde diepgang.

______________________________________________________________________

### Principe 3 — Bewijs boven aannames

Elke claim over prestatie, veiligheid of waarde moet onderbouwd zijn met **meetbare resultaten**. Intuïtie en demo's zijn geen bewijs; gestructureerde tests en validatierapporten wel.

**In de praktijk:**

- Stel een [Golden Set](../09-sjablonen/07-validatie-bewijs/template.md) samen vóór ontwikkeling.
- Valideer op drie niveaus: syntactisch (werkt het?), gedragsmatig (doet het wat verwacht?), doelgericht (helpt het de gebruiker?).
- Documenteer resultaten in een [Validatierapport](../09-sjablonen/07-validatie-bewijs/validatierapport.md).

______________________________________________________________________

### Principe 4 — Mens in de regie

AI-systemen opereren binnen door mensen bepaalde kaders. Bij hogere [Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md) (gedelegeerd, autonoom) worden de kaders strikter, niet losser.

**In de praktijk:**

- Elke modus heeft expliciete escalatiecriteria en een noodstop.
- De [Guardian](../07-compliance-hub/index.md) heeft vetorecht bij overschrijding van harde grenzen.
- Human-in-the-loop is standaard; human-on-the-loop alleen na expliciete goedkeuring.

______________________________________________________________________

### Principe 5 — Continue validatie

AI-gedrag verandert over tijd door datadrift, modelupdates en veranderende context. Validatie is daarom geen eenmalige activiteit maar een **doorlopend proces**.

**In de praktijk:**

- Stel [Monitoring & Drift Detectie](../06-fase-monitoring/05-drift-detectie.md) in vanaf dag één.
- Herhaal Golden Set tests bij elke significante wijziging.
- Gebruik [Retrospectives](../10-doorlopende-verbetering/01-retrospectives.md) en [Kaizen Logs](../10-doorlopende-verbetering/02-kaizen-logs.md) om de aanpak continu te verbeteren.

______________________________________________________________________

## 3. Gerelateerde Modules

- [AI-Native Definitie](01-definitie.md) — wat maakt een systeem AI-native?
- [Artefact Model](03-artefact-model.md) — de vijf beheerde artefacten
- [Validatie Model](04-validatie-model.md) — de drie validatiedimensies
- [Bewijsstandaarden](07-bewijsstandaarden.md) — wat moet je bewijzen per gate?
