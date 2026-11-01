---
name: security-privacy-compliance
description: >
  Build security, privacy, and regulatory compliance into the solution from the
  start — information classification, access and segregation of duties, consent and
  lawful basis, audit trails, retention and deletion, privacy-impact assessment, and
  compliance traceability — and serve as the controlled hook for the organization's
  jurisdiction-specific overlay (e.g. national privacy laws, payer contracts,
  industry regulations). Use this whenever a change touches personal, clinical, or
  financial data, access rights, consent, auditability, or regulated records: "who's
  allowed to see this," "do we need consent," "what must we log," "how long do we
  keep this," "is this compliant," or "what are the privacy risks." Trigger it even
  without "security": "PII," "audit trail," "data retention," or "regulatory
  requirement" should activate it. It's a cross-cutting gate from the start of
  design. It operationalizes ISO/IEC 27001 and 27701 as original working rules; it
  does not reproduce them, and it does not give legal advice.
---

# Security, Privacy & Compliance

Security and privacy cannot be added after the system is designed — they shape the
process, data model, permissions, integrations, logging, and user experience from
the start. This skill specifies those requirements early, and is the **controlled
overlay point** for the organization's regulated context.

It specifies *requirements and controls*; it is not legal counsel. Where a rule
turns on interpreting a law or contract, name the authority and route the
interpretation to the accountable owner.

---

## Where this sits

- **Upstream:** information-data-modeling supplies the data and its classification;
  stakeholder-experience supplies who needs access.
- **Constrains:** process modeling, system-requirements-modeling, and
  solution-architecture-alignment — security/privacy requirements are inputs to
  all three, not a later review.
- **Overlay home:** the industry-specific and country-specific rules (healthcare
  regulations, national privacy laws, payer contracts) live as an overlay on this
  skill; keep the generic skill stable and let the overlay carry jurisdiction
  values.

---

## Core working rules

### 1. Classify information and set handling rules
Classify data (e.g. public / internal / confidential / clinical-sensitive) and
define handling, access, and transmission rules per class. Everything downstream
keys off the classification.

### 2. Specify access, authorization, and segregation of duties
State who may do what, on the principle of least privilege, and where duties must be
separated (the person who requests a payment can't also approve it). These become
permission requirements.

### 3. Require consent and lawful basis for personal data
For personal/clinical data, capture the lawful basis and consent requirements, with
purpose limitation — data collected for one purpose isn't silently reused for
another.

### 4. Define audit-trail requirements
State what must be logged, with what fields, and how the log is protected from
tampering. Auditability is a requirement, not a side effect.

### 5. Set retention and deletion rules
Per data class and regulation, define how long records are kept and how they're
deleted. Indefinite retention is a liability, not a default.

### 6. Run a privacy-impact assessment
For processing of personal data, assess the privacy risk and the mitigations before
build.

### 7. Maintain a regulatory source register and compliance traceability
Every control traces to the authority that requires it (law clause, contract term,
policy). A control with no authority is unexplained; a known authority with no
control is a gap.

---

## Mandatory outputs

- Information-classification requirements
- Access/authorization rules and segregation of duties
- Consent requirements and lawful basis
- Audit-trail requirements
- Retention and deletion rules
- Privacy-impact assessment
- Security risks
- Regulatory source register and compliance traceability

---

## Standards anchor

- **ISO/IEC 27001:2022** — information-security management system requirements.
- **ISO/IEC 27701:2025** — privacy information-management system requirements for
  processing personal data.
- **Applicable laws, industry regulations, and contracts** — carried by the
  organizational overlay.

Operationalize as the rules above; do not reproduce the standards, and do not render
legal conclusions.

---

## Quality bar — failure modes to catch

- Security/privacy treated as a post-design review rather than a design input.
- Controls with no traceable authority, or known regulations with no control.
- Personal/clinical data processed with no lawful basis or consent captured.
- Missing or tamperable audit trail; retention left undefined.
- Segregation-of-duties conflicts unflagged.
- Jurisdiction-specific values hardcoded into the generic skill instead of the
  overlay.

---

## How to apply this skill

1. **Classify** the data and set handling rules per class.
2. **Specify** access, authorization, and segregation of duties.
3. **Capture** consent and lawful basis for personal data.
4. **Define** audit-trail and retention/deletion requirements.
5. **Run** a privacy-impact assessment.
6. **Register** every control against its authority; apply the organizational
   overlay for jurisdiction-specific rules.

---

## Composition

- **From** information-data-modeling and stakeholder-experience.
- **Constrains** process modeling, system-requirements-modeling,
  solution-architecture-alignment.
- **Governed by** practice-governance; jurisdiction rules via the org overlay.

**Traceability:** regulation/contract → **control requirement** → system requirement
→ test/audit. This skill owns the compliance link.
