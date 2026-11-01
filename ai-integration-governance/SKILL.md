---
name: ai-integration-governance
description: >
  Govern AI integrations — classify risk, define decision levels, assess safety
  (hallucination, PHI, audit, human review, cost, fallback), and make explicit
  Go/Conditional Go/No-Go recommendations. Use this whenever AI is proposed in a
  product or workflow: "should we add AI here," "is this AI integration safe," "what
  AI risk level is this," "review this AI feature," or "AI governance review."
  Trigger on: "LLM," "GPT," "copilot," "AI feature," "machine learning," or
  "automated decision."
---

# AI Integration Governance

This skill governs AI integrations through risk classification, decision-level
assessment, and a structured Go/No-Go framework. It prevents unsafe AI from reaching
production and prevents over-caution from blocking safe AI opportunities.

---

## AI Decision Levels

| Level | AI Role | Human Oversight | Example |
|-------|--------|----------------|---------|
| 0 | None — traditional logic | Full | Standard CRUD, business rules |
| 1 | Suggestion — AI recommends, human decides | Required | Code completion, search ranking |
| 2 | Draft — AI produces, human reviews before action | Required | Draft email, summarize record, code suggestion |
| 3 | Action — AI acts, human reviews after | Post-hoc audit | Auto-tag, auto-categorize, triage |
| 4 | Autonomous — AI decides without human review | None (monitor only) | Do not use for clinical, financial, or PII decisions |

**Rule:** No Level 4 for decisions affecting patient safety, financial outcomes, or personal data. Level 3 requires a post-hoc audit trail.

---

## Risk Classification

| Level | Criteria | Approval |
|-------|----------|----------|
| Low | Non-sensitive data, human-reviewed output, reversible action | Team lead |
| Medium | Internal data, draft output with review gate | Product owner + tech lead |
| High | Sensitive data (PII/PHI/financial), consequential output, irreversible action | Product owner + tech lead + compliance |
| Critical | Patient safety, financial loss, legal liability, autonomous Level 4 | Executive sponsor + compliance + legal |

---

## Review Checklist

### 1. Business Fit
- Is AI solving a real, evidenced problem — or is it AI for AI's sake?
- Could a simpler deterministic approach solve this?

### 2. Data & Privacy
- What data does the AI consume? Is it PII/PHI/financial?
- Is data minimized? Only send what the model needs.
- Is consent/lawful basis established for AI processing?
- Is data retained by the AI provider? For how long?

### 3. Output Safety
- Can the AI hallucinate? What's the worst-case hallucination?
- Is output factually verifiable before action?
- Is there a guardrail for toxic/biased/harmful output?

### 4. Human Review
- Which decision level applies? Is the human review gate enforceable?
- Can a human override the AI? How easily?

### 5. Architecture & Integration
- Is the AI call idempotent and retry-safe?
- Is there a timeout and fallback for AI unavailability?
- Does AI latency affect the user experience or SLA?

### 6. Audit & Traceability
- Is every AI call logged with input, output, model version, and timestamp?
- Can an auditor trace an AI decision from output back to input and model?

### 7. Cost & Performance
- Is token/call cost estimated and budgeted?
- Is there a cost alert or cap?
- Is the AI call on the critical path, or can it be async?

### 8. Rollout
- Is there a pilot/preview phase before production?
- Is there a rollback plan if the AI feature fails?
- Are success metrics defined (accuracy, adoption, cost)?

---

## Red Flags

1. AI proposed without a specific, evidenced problem
2. PHI/PII/financial data sent to AI without minimization or consent
3. No human review gate for Level 2+ decisions
4. No fallback when AI is unavailable or slow
5. Hallucination risk in consequential output with no verification
6. No audit trail for AI calls
7. AI on the critical path with no SLA protection
8. No cost estimate or cap
9. No rollback plan for AI feature failure
10. Level 4 autonomy for clinical/financial/PII decisions
11. AI provider retains data without governance
12. Output used as factual data without verification
13. No model versioning — can't reproduce past decisions
14. AI-trained output fed back as training data without governance
15. "AI will figure it out" used as a design decision
16. No bias/fairness assessment for user-facing AI
17. AI replaces a deterministic check that should remain deterministic
18. Prompt injection not mitigated
19. No monitoring for drift or degradation
20. Success metrics not defined before deployment
21. AI cost exceeds value of the problem being solved
22. AI feature approved without the required risk-level approvers
23. AI-generated code invents APIs or standards that don't exist
24. "Conditional Go" treated as "production approved" — it's not

---

## Go/No-Go Framework

| Decision | Criteria |
|----------|----------|
| **Go** | All checklist items satisfied; risk classified and approved at the right level; human review gate enforceable; audit trail; fallback exists; cost known |
| **Conditional Go** | Core safety satisfied; specific conditions must be met before production (e.g., add audit logging, add fallback, complete pilot); **Conditional Go ≠ production approval** |
| **No-Go** | Unresolved PHI/PII exposure, no human review for Level 2+, hallucination risk in irreversible action, cost exceeds value, Level 4 for clinical/financial |
| **Not Recommended** | A simpler deterministic approach would work; AI adds cost without proportional value |
| **Prohibited** | Level 4 for patient safety, financial loss, or legal liability decisions |

---

## AI Use-Case Categories

1. **Developer productivity** — code completion, test generation, doc generation (Low risk)
2. **Engineering governance** — code review, security scanning, dependency analysis (Low-Medium)
3. **Operational support** — log analysis, incident triage, alert correlation (Medium)
4. **Billing/claims** — auto-coding, claim validation, denial prediction (High — requires human review)
5. **Clinical** — decision support, image analysis, risk scoring (High-Critical — always human-reviewed)
6. **Patient-facing** — chat, Q&A, appointment scheduling (High — PHI exposure, hallucination risk)
7. **Production automation** — auto-scaling, self-healing, auto-remediation (Medium-High — depends on blast radius)

---

## Composition

- **From** security-privacy-compliance (data classification, consent)
- **To** practice-governance (AI risk in the traceability chain)
- **Pairs with** evaluating-solution-value (ROI assessment for AI features)

**Traceability:** AI use case → risk classification → decision level → approval → audit trail → outcome KPI.
