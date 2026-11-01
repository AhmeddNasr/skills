---
name: verification-validation-testing
description: >
  Prove the solution both conforms to its requirements (verification) and meets the
  real business need (validation) — through a requirements traceability matrix, test
  scenarios, acceptance tests, rule/decision tests, integration and data-migration
  tests, security and performance tests, and defect/coverage tracking. Use this
  whenever the question is whether a solution actually works and is provably
  complete: "how do we test this," "what's the acceptance criteria," "did we cover
  everything," "build the traceability matrix," "is this requirement testable," or
  "validate this against the need." Trigger it even without "testing": "RTM," "UAT
  plan," "test the decision table," or "coverage gaps" should activate it. It closes
  the lifecycle, consuming requirements, rules, data, NFRs, and security. It
  operationalizes ISO/IEC/IEEE 29148 and the 29119 series as original working rules;
  it does not reproduce them.
---

# Verification, Validation & Testing

This skill proves two different things: **verification** — the solution conforms to
the specified requirements; and **validation** — the solution addresses the actual
business and user need. A requirement that can't be tested is usually a requirement
that isn't clear yet, so this skill also acts as a back-pressure on the whole chain.

---

## Where this sits

- **Upstream:** every specifying skill — system-requirements-modeling,
  decisions-business-rules, information-data-modeling,
  nonfunctional-requirements, security-privacy-compliance.
- **Pairs with:** completeness checks — they verify the cycle closes; this
  checks each requirement and rule is *proven*.
- **Downstream:** adoption-value-realization — passing tests is necessary,
  not sufficient, for realized value.

---

## Core working rules

### 1. Build the requirements traceability matrix
Every requirement maps to a verification method and at least one test. Any
requirement with no test, or any test tracing to no requirement, is a defect in the
matrix — coverage gaps are where escaped defects come from.

### 2. Keep verification and validation distinct
Verification asks "did we build it to spec?"; validation asks "is the spec the right
thing for the need?" A solution can pass verification and fail validation — design
the tests to expose that, not hide it.

### 3. Derive tests from the source artifacts, not from intuition
- each decision-table row → a test case,
- each legal/illegal state transition → tests,
- each NFR threshold → a performance/availability test,
- each control → a security/audit test.
This makes coverage mechanical and arguable.

### 4. Cover the unglamorous paths
Integration, data migration, security, performance, and **exception paths** — not
just the happy path. Most production failures live exactly where testing usually
doesn't.

### 5. Make acceptance business-owned and benefit-linked
User acceptance tests are owned by the business and trace to business requirements
and the intended benefit — they validate the need, not just the build.

### 6. Track defect and requirement coverage
Report coverage continuously; an untested requirement is an unverified one,
regardless of how confident anyone is.

---

## Mandatory outputs

- Requirements traceability matrix
- Verification method per requirement
- Test scenarios and acceptance tests
- Rule and decision tests
- Integration and data-migration tests
- Security and performance tests
- User acceptance plan
- Defect and requirement-coverage reporting

---

## Standards anchor

- **ISO/IEC/IEEE 29148:2018** — keeps requirements verifiable, validatable, and
  traceable. Take the traceability and verifiability discipline.
- **ISO/IEC/IEEE 29119 (Parts 1–3)** — testing concepts, processes, and
  documentation. Take the test-process and documentation structure.

Operationalize as the rules above; do not reproduce the standards.

---

## Quality bar — failure modes to catch

- Only the happy path tested; integration, migration, exceptions skipped.
- Requirements with no test, or tests tracing to no requirement.
- Verification and validation conflated.
- Decision-table rows or state transitions left untested.
- Acceptance tests written by the build team, not the business.
- Coverage asserted ("we tested it") rather than tracked.

---

## How to apply this skill

1. **Build** the RTM linking requirements → methods → tests.
2. **Separate** verification from validation explicitly.
3. **Derive** tests from decision-table rows, state transitions, NFR thresholds,
   security controls.
4. **Cover** integration, migration, security, performance, and exception paths.
5. **Plan** business-owned UAT tied to benefits.
6. **Track** defect and requirement coverage to closure.

---

## Composition

- **From** system-requirements-modeling, decisions-business-rules,
  information-data-modeling, nonfunctional-requirements,
  security-privacy-compliance.
- **Pairs with** completeness checks; **to** adoption-value-realization.
- **Governed by** practice-governance.

**Traceability:** requirement → **test case → coverage**. Together with
adoption-value-realization this closes the chain from objective to realized benefit.