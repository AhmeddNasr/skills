---
name: business-architecture
description: >
  Connect strategy to capabilities, value streams, information, organization, and
  initiatives — so change is targeted at the right capability before any process or
  system work begins. Use this whenever a problem needs locating in the business
  before it's treated as a process or software fix: "where exactly is this breaking,"
  "which capabilities does this initiative touch," "are we solving the right part of
  the business," "map our value streams," or "is this one problem or six." Trigger
  it even without "business architecture": phrases like "capability map," "value
  stream," "where should we invest," "this problem spans several teams," or
  "align these initiatives to capabilities" should activate it. It sits
  after strategy and before detailed process, rules, and requirements work. It
  operationalizes the BIZBOK Guide as original working rules; it does not reproduce
  it.
---

# Business Architecture

This skill locates change. Before a problem is modeled as a process or scoped as a
system, business architecture asks *which capabilities and value streams it
actually touches* — so effort lands where the business is weak, not where the
symptom happens to surface.

Its discipline is to resist premature solutioning. A claim-rejection problem is
rarely "a software problem"; it usually spans contract management, authorization,
coding, claim quality, submission, and collection. Naming the affected capabilities
first prevents fixing the wrong layer.

---

## Where this sits

- **Upstream:** strategy sets the objective and the change worth making.
- **Downstream:** the affected capabilities/value streams scope the work for
  process modeling, decisions-business-rules, and the requirements skills.
- **Cross-cutting:** practice-governance ties initiatives to capabilities in
  the traceability chain.

---

## Core working rules

### 1. Build a capability map (what the business does, not how)
Capabilities are stable, noun-based abilities ("Authorization Management,"
"Claim Adjudication") — independent of org chart, process, or system. They change
far less often than processes do, which is why they anchor investment.

### 2. Map value streams (end-to-end value to a stakeholder)
A value stream is the sequence of value-adding stages from a triggering need to a
realized outcome for a specific stakeholder. Map the stream, then cross it with
capabilities to see which capabilities enable which stages.

### 3. Locate the problem on the map before modeling it
Take the strategic problem and mark every capability and value-stream stage it
touches. The set of marked capabilities is the true scope — often wider, and in a
different place, than the symptom suggested.

### 4. Align initiatives to capabilities
Every initiative names the capabilities it changes and the value streams it
improves. Initiatives with no capability target are solutions looking for a problem;
capabilities targeted by nothing may be silent gaps.

### 5. Assess capability maturity / gaps
For the targeted capabilities, rate current maturity against what the strategy
needs. The gap — not a feature list — is what justifies the change.

---

## Mandatory outputs

- Capability map
- Value-stream map
- Organization and ownership map
- Product and service map
- Initiative-to-capability alignment
- Capability maturity / gap assessment

---

## Standards anchor

- **BIZBOK Guide** — the body of knowledge for linking strategy with capabilities,
  value streams, information, organization, and initiatives. Take the capability/
  value-stream constructs and the strategy-to-execution linkage.

Operationalize as the rules above; do not reproduce BIZBOK text.

---

## Quality bar — failure modes to catch

- Capabilities defined as processes or systems (they should be stable nouns).
- Jumping to "it's a software problem" before mapping affected capabilities.
- Value streams drawn without a named triggering need and stakeholder outcome.
- Initiatives with no capability target, or capabilities no initiative touches.
- Maturity gaps asserted without a current-vs-needed comparison.

---

## How to apply this skill

1. **Take** the objective from strategy.
2. **Map** the relevant capabilities and value streams.
3. **Locate** the problem across them — mark every capability it touches.
4. **Align** the initiative to those capabilities; flag orphans both ways.
5. **Assess** maturity gaps on the targeted capabilities.
6. **Hand off** the scoped capability set to process, rules, and requirements work.

---

## Composition

- **From** strategy: the objective and change strategy.
- **To** process modeling and the requirements skills: a scoped set of
  capabilities, not a vague problem.
- **Governed by** practice-governance for initiative-to-capability traceability.

**Traceability:** strategic objective → **capability / value stream** → stakeholder
need → process/decision → requirements. This skill owns the capability link in the
chain.
