# Kernactiviteiten & RACI (Validatie)

## 3. Kernactiviteiten

### Activiteit 3.1: Technisch Bewijs: Proof of Value (PoV)
We testen de kernhypothese met een kleinschalig experiment.
*   **Hypothese Testen:** Valideer of de AI de beoogde taak daadwerkelijk kan uitvoeren.
*   **Nauwkeurigheid Check:** Behaal een minimale nauwkeurigheid (bijv. >90%) op een representatieve testset.
*   **Data Verificatie:** Bevestig dat de data de benodigde patronen bevat (o.a. via K-Fold cross-validation).
*   **Technische Haalbaarheid:** Evalueer de complexiteit voor productie (infra, latency, schaalbaarheid).

### Activiteit 3.2: Financiële Onderbouwing (ROI & TCO)
We maken de kosten en baten transparant.
*   **Total Cost of Ownership (TCO):** Raming van ontwikkelkosten (personeel) en operationele kosten (compute/GPU, API's, onderhoud).
    *   *Vuistregel budget:* 50-70% Personeel, 20-40% Compute, 10-20% Data.
*   **ROI Meting:** Kwantificeer baten: directe kostenbesparing, omzetgroei of efficiëntiewinst (tijd x uurtarief).
*   **Terugverdientijd:** Bereken wanneer de investering break-even draait.

### Activiteit 3.3: Strategische Prioritering
Is dit project de investering waard ten opzichte van andere opties?
*   **Value vs. Feasibility Matrix:** Plaats de gevalideerde resultaten op de matrix.
*   **Decision Criteria:** Stel harde criteria vast voor de Go/No-Go beslissing.
*   **Balanced Scorecard:** Evalueer impact op Financiën, Operatie, Klant en Strategie.

### Activiteit 3.4: Compliance & Risk Deep-Dive
We kijken dieper naar de risico's dan in de Discovery fase.
*   **Risicoanalyse:** Update het risico-register met specifieke bevindingen uit de PoV.
*   **Ethische Toetsing:** Voer een Fairness Audit uit op de PoV-resultaten. Is er bias?
*   **Leveranciersbeoordeling:** Als externe tools worden gebruikt: check compliance (EU AI Act, GDPR, Security).
*   **Classificatie:** Bepaal het definitieve risiconiveau (Laag/Matig/Verhoogd/Kritiek) volgens de [AI-Native Risk Classification](../../01-ai-native-fundamenten/05-risicoclassificatie.md).

## 4. Team & Rollen (RACI)

| Rol | Verantwoordelijkheid in Validatie |
| :--- | :--- |
| **Chief AI Officer (CAIO)** | **A**ccountable: Evalueert ROI en strategische fit. Keurt budget goed (Gate 2). |
| **Business Analist** | **R**esponsible: Stelt de Business Case en TCO op. |
| **AI Architect / Tech Lead** | **R**esponsible: Voert de PoV uit en valideert technische haalbaarheid. |
| **Ethicist / Guardian** | **C**onsulted: Beoordeelt bias in PoV en risico's (accountability). |
| **Security Officer** | **I**nformed: Wordt geïnformeerd over gebruikte tools en data. |

---
© 2026 AI Project Playbook. Gelicenseerd onder CC BY-NC-SA 4.0.
