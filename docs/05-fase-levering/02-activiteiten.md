# Kernactiviteiten & RACI (Levering)

## 3. Kernactiviteiten

### Activiteit 3.1: Technische Implementatie & Infrastructuur
Schaalbaar en veilig uitrollen.
*   **Schaalbaarheid:** Opzetten van productie-infrastructuur (autoscaling, load balancing) voor verwachte workloads.
*   **API & Integratie:** Koppelen van het AI-model aan bestaande systemen (CRM, ERP, Web) en valideren van data-consistentie end-to-end.
*   **Scoping Gates:** Gefaseerde uitrol (Canary deployment, Blue/Green) en monitoring van initiële prestaties (>90% nauwkeurigheid handhaven).
*   **Access Controls:** Implementeren van strikte IAM (Identity & Access Management) en encryptie (at-rest & in-transit).

### Activiteit 3.2: Change Management & Adoptie
De menselijke kant van de implementatie.
*   **Mensgerichte Aanpak:** Transparante communicatie over de rol van AI als ondersteuning (niet vervanging).
*   **Adoptie Programma's:** Gebruik methodieken zoals ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) om weerstand te verminderen.
*   **Training & Mentorschap:** Oprichten van Centers of Excellence.
    *   Koppelen van ervaren 'Champions' aan nieuwe gebruikers.
    *   Aanbieden van hands-on training en handleidingen.
*   **Feedback Kanalen:** Inrichten van laagdrempelige procedures voor het melden van fouten, bias of onverwacht gedrag.

### Activiteit 3.3: Juridische Afronding & Compliance
De puntjes op de i voor de wetgever.
*   **Registratie:** Registreren van hoog-risico systemen in EU-databases.
*   **CE-Markering:** Toevoegen van vereiste markeringen (indien van toepassing).
*   **Technisch Dossier Definitief:** Consolideren van alle documentatie (modelarchitectuur, risico-assessments, data-oorsprong).
*   **Menselijk Toezicht:** Implementeren en testen van de 'Human-in-the-loop' mechanismen.

### Activiteit 3.4: Voorbereiding op Beheer (Handover)
Overdracht naar de beheerorganisatie.
*   **Handoff Processen:** Formele overdracht van Development naar Operations/Support.
*   **Incident Response:** Activeren van het calamiteitenplan (wat als het model faalt of discrimineert?).
*   **Traceability:** Zorgen dat elke beslissing terug te leiden is naar een specifieke modelversie en dataset (Intent -> Change -> Evidence).

## 4. Team & Rollen (RACI)

| Rol | Verantwoordelijkheid in Levering |
| :--- | :--- |
| **DevOps / Systems Architect** | **R**esponsible: Verantwoordelijk voor deployment, automatisering en monitoring setup. |
| **AI Product Manager** | **A**ccountable: Leidt de lancering, coördineert stakeholders en borgt adoptie. |
| **Data Scientist** | **R**esponsible: Ondersteunt technische integratie en monitort initiële performance (o.a. A/B tests). |
| **Guardian (Ethicist)** | **C**onsulted: Flagt real-time risico's tijdens uitrol; bouwt vertrouwen. |
| **Eindgebruikers** | **I**nformed/Consulted: Ontvangen training en geven feedback. |

---
© 2026 AI Project Playbook. Door **Frederik Vannieuwenhuyse** & **Hadrien-Joseph van Durme**. Gelicenseerd onder CC BY-NC-SA 4.0.
