---
name: decisions-business-rules
description: >
  Model the decisions and business rules that sit underneath a process, using DMN
  (decision requirements + decision tables) and SBVR-style rule discipline. Use
  this whenever the logic that determines an outcome — eligibility, authorization,
  pricing/coding, approval thresholds, exception handling, calculations — needs to
  be made explicit, testable, and changeable, instead of being buried inside
  process gateways or narrative policy. Trigger it even when the user doesn't say
  "DMN" or "rules": phrases like "how do we decide X," "what are the eligibility
  criteria," "turn this policy into a decision table," "the logic here is a mess,"
  "extract the rules from this SOP," or "this gateway has too many conditions"
  should all activate it. It sits immediately downstream of process modeling and
  upstream of system requirements. It operationalizes DMN 1.5 and SBVR 1.5 as
  original working rules; it does not reproduce either specification.
---

# Decisions & Business Rules

A process model says **what** activity happens and in what order. A decision model
says **how** the outcome of a decision activity is determined. These are different
things, and the single most valuable move this skill makes is to **separate them**:
pull the rule logic out of the process flow and model it on its own.

Why it matters: rules buried inside process gateways or prose policy are hard to
find, hard to test, and dangerous to change — one edit can silently break a path
nobody remembers. Lifted out into named decisions and decision tables, the same
logic becomes auditable, individually testable, owned, and automatable, and the
process diagram stays clean.

This skill does **not** model the flow, and it does **not** define what the concepts
mean or where input data comes from. It models the determinations made *along* that
flow.

---

## Where this sits

- **Upstream:** process models surface decision points — every gateway, and every
  activity named "assess / determine / check / verify / approve / classify," is a
  candidate decision. Concept model and data analysis supply the controlled
  vocabulary and typed inputs.
- **Downstream:** each decision becomes system behavior: a validation, a calculated
  field, a gated action. Each decision-table row is a test case.
- **Cross-cutting:** the organizational overlay supplies the *content* of many rules;
  this skill supplies the *structure*. Keep the skill domain-neutral.

---

## Core working rules

### 1. Decision vs. process vs. rule — keep the three distinct
- A **business rule** is one atomic statement that constrains or guides ("an
  emergency service does not require prior authorization"). It is not, by itself,
  a decision.
- A **decision** takes input data and applies a set of rules to select **one
  outcome** ("Is prior authorization required? → Yes / No / Conditional").
- A **process** is a sequence of activities over time. If something is multi-step,
  stateful, or involves waiting/handoffs, it is **not** a decision table — send it
  back to process modeling. A decision is evaluated, not performed.

### 2. Build the Decision Requirements Diagram (DRD) before any table
For each decision, name four things:
- the **decision** itself (the question and its possible outcomes),
- the **input data** it needs (each input typed and traceable to a data element),
- the **rule set** behind it (the reusable logic),
- the **authority/source** that governs it (the contract clause, policy, or
  regulation).

A decision that depends on the output of another decision is **wired**, not merged
— draw the dependency. Decompose any decision whose table would need more than a
handful of inputs into sub-decisions.

### 3. Express the logic as a decision table, and design it for audit
- One decision = one table where possible.
- Inputs are the **conditions**; order by discriminating power.
- Keep inputs to the **minimum** that determine the output.
- Each **row is a rule**: a combination of input conditions → an output. Use
  "don't-care" deliberately to collapse rows.
- Pick a **hit policy** and state it. Default to **Unique** — rows must not
  overlap, and every input combination must be covered.

### 4. Verify completeness and consistency — this is non-negotiable
- **Completeness:** every realistic input combination maps to an output. Walk the
  ranges; the gaps are where production incidents come from.
- **Consistency:** no two rules fire contradictory outputs for the same inputs.
- **Subsumption:** no rule is a redundant subset of another.
  State explicitly what happens in the *unmatched* case. Silent gaps are defects.

### 5. Calculation rules are decisions too
Pricing, coding multipliers, co-pay, score thresholds — model these as named,
typed expressions, not magic numbers. Each calculation gets: a name, typed inputs,
the formula stated once, and a worked example.

### 6. Write each rule as a structured, sourced, owned statement (SBVR discipline)
Every rule in the catalogue carries:
- an **id** and a **structured statement** in controlled vocabulary,
- a **type** — definitional/structural vs operative/behavioural,
- a **source** (the authority it derives from) and an **owner** (who can change it),
- a **status** (draft / approved / retired).

An unsourced rule or an ownerless rule is a suspect rule — flag it.

---

## Mandatory outputs

- Business-rule catalogue (id, statement, type, source, owner, status)
- Decision Requirements Diagram (decisions, inputs, rule sets, authorities, and
  inter-decision dependencies)
- Decision table(s) with declared hit policy
- Eligibility criteria (as decisions/tables, not prose)
- Calculation rules (named typed expressions with worked examples)
- Approval rules (thresholds, authorities, segregation-of-duty constraints)
- Exception rules (what overrides the normal outcome, and under what authority)
- Rule sources and owners register

---

## Standards anchor

- **DMN 1.5** — decision-modeling: Decision Requirements Diagrams, decision
  tables, hit policies, and the FEEL expression language. Standardize on 1.5.
  Take the structure; express logic in your own controlled vocabulary.
- **SBVR 1.5** — structured business vocabulary and rules: the definitional vs.
  operative distinction, and the practice of stating rules in controlled natural
  language tied to a vocabulary.

Operationalize both as the working rules above. Do not paste specification text.

---

## Quality bar — common failure modes to catch

- **Logic trapped in the flow:** a gateway with five conditions. Lift it into a
  decision.
- **A "decision" that's actually a process:** multi-step, stateful, or with
  handoffs. Route it back.
- **Incomplete table:** input combinations with no defined outcome.
- **Overlapping/contradictory rows** under a Unique hit policy.
- **Unsourced or ownerless rules**, and rules that contradict the glossary.
- **Magic numbers** with no calculation-rule definition.
- **Hidden decisions** — determinations in narrative policy never modeled.
- **Definitional and operative rules mixed together** in one undifferentiated list.

---

## How to apply this skill

1. **Harvest** decision points from the process model and source policy.
2. **Triage** each: true decision (model it) or sub-process (return to process).
3. **Draw the DRD** — decision, inputs, rule set, authority; wire dependencies.
4. **Model the logic** — decision table (declare hit policy) or named calculation;
  verify completeness and consistency.
5. **Catalogue the rules** — id, structured statement, type, source, owner, status.
6. **Wire traceability** — up to the process activity and business requirement;
  down to the system requirement and the test case.
7. **Self-check** against the quality bar.

---

## Worked example (process → decision split)

A referral-management process contains an activity "Assess authorization
requirement." That activity is a gateway magnet. Lift it:

- **Decision:** *Is prior authorization required?* → {Required, Not required,
  Conditional}
- **Inputs:** service type, payer/plan, diagnosis, encounter setting, emergency
  flag.
- **Rule set / authority:** the payer contract's authorization schedule + national
  emergency-exemption regulation.
- **Decision table (Unique):** rows mapping input combinations to the outcome; an
  emergency encounter resolves to *Not required* regardless of service, captured as
  one row with don't-cares.
- **Downstream:** the outcome becomes a system rule — *submission is blocked when a
  service requiring authorization has no valid authorization number*; each row
  derives a test case.

---

## Composition

- **From** process models: take the flagged decision points.
- **With** concept and data skills: borrow the exact vocabulary and typed inputs.
- **To** system requirements and testing: hand off each modeled decision as behavior
  to implement and rows to test.

**Traceability:** business rule → decision → process activity → business
requirement → system requirement → test case.
