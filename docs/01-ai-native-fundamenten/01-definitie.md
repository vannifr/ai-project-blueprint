# ?? De Kernprincipes

## ?? 1. Wat Zijn de Kernprincipes?
Wij beschouwen AI-voorzieningen niet als statische software, maar als **gedragssturing**. Dit betekent dat we AI-systemen niet programmeren in de traditionele zin, maar sturen door middel van informatie en context.

Een project valt onder dit regime als aan **drie voorwaarden** is voldaan:

### 1. Impact
Het systeem raakt de business direct. Het neemt beslissingen, genereert content of beïnvloedt processen die waarde creëren of risico's met zich meebrengen.

### 2. Traceerbaarheid  
Alle instructies en configuraties zijn beheerd als code (version control). We kunnen altijd terugkijken: "Waarom deed het systeem dit op dat moment?"

### 3. Continue Toetsing
Het systeem wordt niet één keer getest en dan "klaar" verklaard. We valideren doorlopend of het gedrag nog aansluit bij de bedoeling.

## ?? Governance-as-Code (Automatisering)
Documentatie alleen verandert gedrag niet; de implementatie doet dat wel. We hanteren het principe van **Verifieerbaarheid door Code**:
*   **Technisch Dossier in Git:** Artefacten zoals de **Technische Modelkaart** worden bij voorkeur opgeslagen als code (YAML/JSON) in de repository.
*   **Automated Gates:** De CI/CD-pipeline checkt automatisch op compliance-criteria (bijv. accuraatheid > 85%) voordat een model naar productie gaat.

---

## ?? De Drie Kernvoorwaarden

Om AI-systemen beheersbaar te maken, werken we met vier kerndocumenten:

### 2.1 Doeldefinitie (Intent)
**Wat proberen we te bereiken?**

Dit is de hypothese of het doel van het systeem. Bijvoorbeeld:
- "Automatisch facturen categoriseren met 95% nauwkeurigheid"
- "Klantvragen beantwoorden binnen 30 seconden"

### 2.2 Rode Lijnen (Constraints)
**Wat mag absoluut niet gebeuren?**

Dit zijn de harde grenzen waar het systeem zich aan moet houden:
- Privacy: Geen persoonsgegevens delen zonder toestemming
- Veiligheid: Geen medische adviezen geven
- Compliance: Voldoen aan AVG/GDPR

### 2.3 Sturingsinstructies (Context)
**Welke informatie stuurt het gedrag?**

Dit omvat alle inputs die de AI gebruikt:
- Prompts en instructies
- Gekoppelde documenten en kennisbanken
- Configuraties en parameters
- Voorbeelden (few-shot learning)

### 2.4 Validatierapport (Evidence)
**Hoe weten we dat het werkt?**

Het rapport dat aantoont dat de AI zich aan de Rode Lijnen houdt en het Doel bereikt:
- Testresultaten
- Prestatiemetrics
- Audit logs
- Gebruikersfeedback

---

## 3. Van Code naar Gedrag

Het verschil met traditionele software:

| Traditionele Software | AI als Gedragssturing |
|----------------------|----------------------|
| We schrijven expliciete regels | We sturen met voorbeelden en context |
| Logica is deterministisch | Gedrag is probabilistisch |
| Eenmalige test = klaar | Continue validatie vereist |
| Bug = code fout | "Bug" = context probleem |

**Context Engineering** wordt de nieuwe kerndiscipline: het ontwerpen en beheren van de informatie die het AI-gedrag stuurt.

---

## 4. Waarom Dit Belangrijk Is

Deze aanpak zorgt voor:
- **Controleerbaarheid:** We weten altijd waarom het systeem iets deed
- **Aanpasbaarheid:** Gedrag wijzigen = context aanpassen, niet herprogrammeren
- **Verantwoording:** Duidelijke eigenaarschap van doelen en grenzen
- **Compliance:** Aantoonbaar voldoen aan wet- en regelgeving

---

## Gerelateerde Modules
*   [AI-Samenwerkingsmodi](../00-strategisch-kader/06-has-h-niveaus.md)
*   [Artefact Model](03-artefact-model.md)
*   [Validatie Model](04-validatie-model.md)

---
**Versie:** 2.0
**Datum:** 31 januari 2026
**Status:** Definitief

---
---
**Versie:** 2.1
**Datum:** 31 januari 2026
**Status:** Definitief

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
