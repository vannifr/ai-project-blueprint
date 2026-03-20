---
versie: '1.1'
type: guide
layer: 2
phase: [1]
roles: [AI Product Manager]
summary: Accelerated track for low-risk AI applications to safely and quickly test value with minimal governance overhead.
answers: [How does Fast Lane work?, How do I classify the risk of my AI project?]
---

# 1. Fast Lane

!!! abstract "Purpose"
    Accelerated track for low-risk AI applications to safely and quickly test value with minimal governance overhead.

!!! tip "When to use this?"
    You have a low-risk AI use case and want to know whether you can skip the full lifecycle via the accelerated Fast Lane track.

## 1. Objective

The Fast Lane is designed to **safely and quickly** test value for **low-risk** AI applications, without unnecessary bureaucracy — but **with minimal governance**.

## 2. Admission Criteria (all mandatory)

A use case may only use the Fast Lane if **all** of the following conditions are met:

1. **EU AI Act risk level = Minimal** (see Compliance Hub)
1. **Collaboration mode = 1 or 2** (Instrumental or Advisory; see AI Collaboration Modes)
1. The AI **makes no decisions about people** (no selection/allocation/rejection)
1. No processing of **special categories of personal data** (health, religion, biometrics, etc.)
1. Output is **always** reviewed by a human before use (no autonomous sending/execution)
1. Internal use only, or (if external) **100% transparency** ("You are interacting with AI")

**If one criterion is not met:**
→ *no Fast Lane* — follow the standard lifecycle (Discovery & Strategy through Monitoring & Optimisation).

### Hard exclusions

The Fast Lane is **not permitted** for the following categories:

1. **External customer-facing chatbots or public content generation** without demonstrable Art. 50 disclosure/labelling implementation.
1. **Tool-using agents with write-access** to business systems (e.g. ERP, CRM, HRM) — even in "pilot" form.
1. **Systems with autonomous decisions** affecting individuals (screening, scoring, allocation).

!!! check "Evidence for Art. 50 implementation (if applicable)"

- [ ] Screenshot or UX copy of disclosure/labelling in the user interface
- [ ] Test cases in the Golden Set that validate disclosure/labelling behaviour
- [ ] Reference in the Validation Report with links to evidence

## 3. Minimum deliverable package (Fast Lane)

- **[Project Charter](../09-sjablonen/01-project-charter/template.md)** (Fast Lane variant: brief)
- **[Risk Pre-Scan](../09-sjablonen/03-risicoanalyse/pre-scan.md)** (must confirm "Minimal")
- **[Goal Definition](../09-sjablonen/06-ai-native-artefacten/doelkaart.md)** (incl. Hard Boundaries)
- **[Golden Set Test & Acceptance Protocol](../09-sjablonen/07-validatie-bewijs/template.md)** (light: minimum 20 cases)
- **[Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md)** (evidence of test results)

**What you may skip in Fast Lane:**

- Extensive business case (ROI) *may come later*, but note a "value hypothesis" in the Charter.
- Extensive technical dossier (only relevant at high risk).

## 4. Fast Lane Gates (simple and verifiable)

### Gate FL-1 — Start experiment (max. 2 weeks)

**Go** if:

- Risk Pre-Scan = Minimal
- Goal Definition contains Hard Boundaries
- Minimum test plan is ready (Golden Set ≥ 20)

### Gate FL-2 — Internal live pilot (max. 4 weeks)

**Go** if:

- [Validation Report](../09-sjablonen/07-validatie-bewijs/validatierapport.md) meets [Evidence Standards](../01-ai-native-fundamenten/07-bewijsstandaarden.md) norms for Minimal risk
- Logging/traceability is set up at basic meta-level
- Incident procedure is known to the team

## 5. When Fast Lane stops (escalation)

The Fast Lane stops immediately and we switch to the standard lifecycle if:

- Collaboration mode shifts to **3+**
- The tool will be used externally with impact on customers
- Data usage expands to (special categories of) personal data
- 1 Critical error occurs (Hard Boundaries breached)

______________________________________________________________________

## 6. Related Modules

- [Pitfalls Catalogue — G-05: Governance as blocker](../17-bijlagen/valkuilen-catalogus.md)
- [Risk Classification](../01-ai-native-fundamenten/05-risicoclassificatie.md)

______________________________________________________________________

**Next step:** If you qualify for the Fast Lane, start directly with [Phase 2 — Validation](../03-fase-validatie/01-doelstellingen.md)
→ See also: [Explorer Kit](../00-explorer-kit/index.md)
