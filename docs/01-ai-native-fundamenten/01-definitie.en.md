---
versie: '1.1'
---

# 1. Core Principles

## 1. What Are the Core Principles?

We treat AI systems not as static software, but as **behaviour steering**. This means we do not programme AI systems in the traditional sense, but steer them through information and context.

Behaviour steering means not only formulating objectives and boundaries, but also explicitly managing all information, configurations and permitted actions that steer the system's behaviour. This steering is recorded, made version-controllable and verified, so that changes remain auditable.

A project falls under this regime if **three conditions** are met:

### Impact

The system directly touches the business. It makes decisions, generates content or influences processes that create value or carry risks.

### Traceability

All instructions and configurations are managed as code (version control). We can always look back: "Why did the system do this at that moment?"

### Continuous Validation

The system is not tested once and then declared "done". We continuously validate whether the behaviour still matches the intent.

## 2. Governance-as-Code (Automation)

Documentation alone does not change behaviour; the implementation does. We apply the principle of **Verifiability through Code**:

- **Technical Dossier in Git:** Artefacts such as the **Technical Model Card** are preferably stored as code (e.g. YAML, JSON or other structured formats) in the repository.
- **Automated Gates:** The CI/CD pipeline automatically checks compliance criteria (e.g. accuracy > 85%) before a model goes to production.

______________________________________________________________________

## 3. The Four Core Documents

To make AI systems governable, we work with four core documents:

### Goal Definition (Intent)

**What are we trying to achieve?**

This is the hypothesis or objective of the system. For example:

- "Automatically categorise invoices with 95% accuracy"
- "Answer customer queries within 30 seconds"

### Hard Boundaries (Constraints)

**What must absolutely never happen?**

These are the hard limits the system must adhere to:

- Privacy: Do not share personal data without consent
- Safety: Do not give medical advice
- Compliance: Comply with GDPR

### Steering Instructions (Context)

**What information steers the behaviour?**

This includes all inputs the AI uses:

- Prompts and instructions
- Linked documents and knowledge bases
- Configurations and parameters
- Examples (few-shot learning)

### Validation Report (Evidence)

**How do we know it works?**

The report demonstrating that the AI adheres to the Hard Boundaries and achieves the Goal:

- Test results
- Performance metrics
- Audit logs
- User feedback

______________________________________________________________________

## 4. From Code to Behaviour

The difference from traditional software:

| Traditional Software    | AI as Behaviour Steering           |
| ----------------------- | ---------------------------------- |
| We write explicit rules | We steer with examples and context |
| Logic is deterministic  | Behaviour is probabilistic         |
| Single test = done      | Continuous validation required     |
| Bug = code error        | "Bug" = context problem            |

**Context Engineering** becomes the new core discipline: designing and managing the information that steers AI behaviour.

______________________________________________________________________

## 5. Why This Matters

This approach ensures:

- **Accountability:** We always know why the system did something
- **Adaptability:** Changing behaviour = adjusting context, not reprogramming
- **Ownership:** Clear ownership of objectives and boundaries
- **Compliance:** Demonstrably complying with laws and regulations

______________________________________________________________________

## 6. Related Modules

- [AI Collaboration Modes](../00-strategisch-kader/06-has-h-niveaus.md)
- [Artefact Model](03-artefact-model.md)
- [Validation Model](04-validatie-model.md)

______________________________________________________________________
