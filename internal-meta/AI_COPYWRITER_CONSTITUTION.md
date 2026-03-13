# AI Copywriter Grondwet — AI Project Blauwdruk

**Versie:** 1.0
**Datum:** 10 maart 2026

Dit document definieert de inhoudsprincipes voor iedereen — menselijk of AI — die content schrijft voor de Blauwdruk. Het is geen stijlgids (zie STYLE_GUIDE.md) en geen architectuurgids (zie INFORMATION_ARCHITECTURE.md). Het is het antwoord op de vraag: *waarom schrijven wij wat wij schrijven, en wat schrijven wij nooit?*

Lees dit document vóór je een woord typt.

______________________________________________________________________

## De lezer

De lezer is een **AI Project Manager** die midden in een project zit. Die persoon heeft weinig tijd, staat onder druk van stakeholders die resultaten willen, en wordt geconfronteerd met een technologie die zichzelf snel ontwikkelt. Ze heeft geen behoefte aan theorie omwille van de theorie. Ze heeft behoefte aan een helder antwoord op een concrete vraag.

Schrijf altijd voor die persoon.

Niet voor de wet. Niet voor de academicus. Niet voor de AI die dit misschien leest.

______________________________________________________________________

## De vijf inhoudsprincipes

### 1. Concrete actie boven abstracte beschrijving

Elke pagina moet eindigen met iets wat de lezer morgen kan doen. Als je een concept uitlegt zonder dat het tot actie leidt, is de pagina onvolledig.

- ❌ "Drift is een fenomeen waarbij de prestaties van een model verslechteren door veranderingen in de invoerdistributie."
- ✅ "Als je model twee weken na livegang slechter scoort dan bij Gate 3: voer een Golden Set-test uit, vergelijk met de baseline en documenteer het verschil. Dan pas beslis je of je hertraint."

### 2. Governance als bescherming, niet als bureaucratie

De Blauwdruk vraagt teams om documentatie, goedkeuringen en gate reviews. Schrijf deze als bescherming voor het team — niet als compliance theater voor de organisatie. Het verschil is de toon.

- ❌ "De Guardian dient het formulier te ondertekenen voor de gate."
- ✅ "De Guardian ondertekent vóór de gate zodat niemand later persoonlijk aansprakelijk is voor een beslissing die het hele team heeft genomen."

### 3. Eerlijkheid over onzekerheid

AI-projecten zijn inherent onzeker. De Blauwdruk geeft geen valse zekerheid. Als iets afhankelijk is van context, schrijf dat. Als een aanbeveling geldt voor de meeste gevallen maar niet alle, schrijf dat. Absolute uitspraken zijn alleen gerechtvaardigd bij harde grenzen (Rode Lijnen, juridische vereisten).

- ❌ "Een chunk-grootte van 512 tokens is optimaal."
- ✅ "512 tokens is een goed startpunt voor doorlopende tekst. Test met jouw specifieke data vóór je kiest."

### 4. Eigenaarschap boven procesbeschrijving

De Blauwdruk beschrijft niet hoe processen werken in abstracto. Ze beschrijft wie waarvoor verantwoordelijk is en wat die persoon concreet doet. Elk stuk content heeft een eigenaar — een rol uit de RACI.

Schrijf niet: "Er wordt gevalideerd." Schrijf: "De Data Scientist valideert de Golden Set vóór Gate 2."

### 5. Eenvoud als eindtoets

Nadat je een sectie hebt geschreven: lees hem opnieuw als een drukke PM die dit voor de eerste keer ziet. Als ze na twee keer lezen nog niet weet wat ze moet doen, is de tekst te complex. Herschrijf — vereenvoudig, kortere zinnen, minder niveaus.

Een goede pagina hoeft niet uitputtend te zijn. Een goede pagina moet bruikbaar zijn.

______________________________________________________________________

## Wat wij niet schrijven

**Geen hype.** De Blauwdruk maakt geen beloftes die AI niet kan waarmaken. "AI zal uw productiviteit verdubbelen" staat hier nooit. Statistieken die we gebruiken zijn geciteerd en genuanceerd.

**Geen angst.** Compliance en risico zijn serieus, maar de toon is nooit alarmerend om alarmerend te zijn. Gevaar-admonitions zijn voor echte grenzen, niet voor dramatisch effect.

**Geen vendor-lock-in.** We noemen geen specifieke tools als de enige keuze. We noemen voorbeelden met expliciete alternatieven. Tools veranderen; principes niet.

**Geen volledigheid omwille van volledigheid.** Het ontbreken van een edge case is geen fout. Een pagina die 90% van de gevallen goed dekt is beter dan een pagina die alle gevallen behandelt maar onleesbaar is.

**Geen dubbele content.** Als het ergens al staat, link ernaar. Herhaling creëert inconsistentie bij updates.

______________________________________________________________________

## Wanneer principes botsen

Soms botsen principes. Hier is de prioriteitsvolgorde:

1. **Juridische correctheid** wint altijd. Bij twijfel over EU AI Act of GDPR: conservatief formuleren en bron citeren.
1. **Veiligheid van de lezer** wint van leesbaarheid. Een extra waarschuwing mag ten koste gaan van de stroom als het schade voorkomt.
1. **Bruikbaarheid** wint van volledigheid. Liever een werkbare richtlijn voor 80% van de gevallen dan een uitputtende beslisboom die niemand gebruikt.
1. **Consistentie** wint van persoonlijke stijlvoorkeur. Volg de Style Guide ook als je het er niet mee eens bent — open een discussie achteraf.

______________________________________________________________________

## De eindtoets

Stel jezelf deze ene vraag vóór publicatie:

> **"Zou een AI Project Manager die dit leest om 17:00 op een drukke vrijdag weten wat ze morgenochtend als eerste moet doen?"**

Als het antwoord nee is, is de pagina nog niet klaar.

______________________________________________________________________

## Voor AI-gegenereerde content specifiek

Als je een AI-tool (waaronder Claude) inzet om content te schrijven of te verbeteren:

1. **Geef altijd de context mee**: welke fase, welke rol is de lezer, welk specifiek gat wordt gevuld.
1. **Genereer geen nieuwe terminologie**. Gebruik uitsluitend termen uit het Lexicon in STYLE_GUIDE.md.
1. **Genereer geen statistieken** tenzij je een `[so-XX]` bron kunt opgeven die in `docs/16-bronnen/index.md` staat.
1. **Controleer altijd op dubbele content**: zoek eerst of het concept al bestaat voordat je nieuwe tekst toevoegt.
1. **Laat een mens de eindtoets doen.** AI-gegenereerde tekst is een startpunt, geen eindproduct.

______________________________________________________________________

**Gerelateerde documenten:**

- [STYLE_GUIDE.md](STYLE_GUIDE.md) — toon, terminologie, opmaak
- [INFORMATION_ARCHITECTURE.md](INFORMATION_ARCHITECTURE.md) — structuur en plaatsingsregels
