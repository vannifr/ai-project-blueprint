---
versie: '1.0'
pdf: false
---

# Cheatsheet — Incident Respons

**Bron:** [Incident Respons](../../07-compliance-hub/05-incidentrespons.md) | [Incident Playbooks](../../07-compliance-hub/06-incidentrespons-playbooks.md)

______________________________________________________________________

## Eerste 15 Minuten

```
1. DETECTEER — Is dit een echt incident of een valse alarm?
2. CLASSIFICEER — Welk type? (Drift / Security / Bias / Uitval)
3. ERNST — Rood / Oranje / Geel / Groen?
4. NOTIFICEER — Juiste mensen direct informeren
5. PRESERVEER — Logs veiligstellen, niets verwijderen
```

______________________________________________________________________

## Ernst & Actie

| Ernst         | Drempel                                   | Actie                                              | Wie                   |
| :------------ | :---------------------------------------- | :------------------------------------------------- | :-------------------- |
| 🔴 **Rood**   | Directe schade of wettelijke verplichting | Circuit Breaker activeren; CISO + Guardian + Legal | Tech Lead (commander) |
| 🟠 **Oranje** | Significant risico, geen directe schade   | Verhoogde monitoring; Guardian informeren          | AI PM + Tech Lead     |
| 🟡 **Geel**   | Kwaliteitsdaling, beperkte impact         | Monitoren; herstelplan binnen 24u                  | AI PM                 |
| 🟢 **Groen**  | Afwijking binnen bandbreedte              | Documenteer; geen actie nodig                      | Automatisch           |

______________________________________________________________________

## Circuit Breaker — Activeer bij

- Ongeautoriseerde toegang of datalekkage actief
- Outputs die directe schade kunnen veroorzaken
- Systeem buiten alle normale parameters
- Juridische verplichting tot direct handelen

**Circuit Breaker activeren:** → [Incident Respons Overzicht](../../07-compliance-hub/05-incidentrespons.md)

______________________________________________________________________

## Playbook per Type

| Type incident            | Playbook                                                                            |
| :----------------------- | :---------------------------------------------------------------------------------- |
| Kwaliteitsdaling / drift | [Playbook 1 — Model Drift](../../07-compliance-hub/06-incidentrespons-playbooks.md) |
| Beveiligingsincident     | [Playbook 2 — Security](../../07-compliance-hub/06-incidentrespons-playbooks.md)    |
| Ongelijke behandeling    | [Playbook 3 — Bias](../../07-compliance-hub/06-incidentrespons-playbooks.md)        |
| Systeem onbereikbaar     | [Playbook 4 — Uitval](../../07-compliance-hub/06-incidentrespons-playbooks.md)      |

______________________________________________________________________

## Meldingsplichten (Tijdlijn)

| Verplichting               | Termijn              | Trigger                        |
| :------------------------- | :------------------- | :----------------------------- |
| GDPR datalek               | 72 uur               | Persoonsgegevens betrokken     |
| EU AI Act (Hoog Risico)    | Per nationaal beleid | Incident met menselijke impact |
| Interne escalatie Guardian | Onmiddellijk         | Rood of Oranje incident        |
| Gebruikerscommunicatie     | 15 min (uitval)      | Systeem onbereikbaar           |

**Bron volledige aanpak:** [Incident Playbooks](../../07-compliance-hub/06-incidentrespons-playbooks.md)
