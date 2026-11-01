---
name: business-rule-tiering
description: Classify any business rule as Tier 1 (protects the person), Tier 2 (controls the process), or Tier 3 (stores the value) — the "Business Rules for Beginners" T1/T2/T3 method, validated against the CPOE assessment. Use when the user asks to classify business rules into tiers, tier a rule, check which tier a rule belongs to, build or review a business rule register, decompose a mixed rule into T1/T2/T3, or identify safety-critical rules in a requirement, BRD, or existing rule list (e.g. "classify these rules as T1/T2/T3", "is this a safety rule?", "split this rule into tiers", "which rules are T1 in this register").
---

# Business Rule Tiering (T1 / T2 / T3)

Classify every business rule into exactly one tier. The tier says **WHO may change the rule and HOW** — it is not a priority ranking. Mixed rules are split; rules without evidence are marked honestly, never forced.

## The tier model — pocket card

| Tier | Meaning | Test question |
|------|---------|---------------|
| **T1** | Protects the person | Could this harm a person (physically, financially, or legally in this domain)? |
| **T2** | Controls the process | Are we changing HOW the system works? |
| **T3** | Stores the value | Are we changing only a governed value or setting? |
| **?** | Waits for evidence | Not proven yet? Say so. |

- **Safety is tested first** — even when the rule looks like ordinary data.
- **Unclear is never "no".** If the answer to Q1 is unclear, keep T1 protection until someone proves the person is safe without it.

## Classification workflow — 4 questions, always in this order

The order is what keeps tiers mutually exclusive (MECE): every rule has exactly one home; nothing falls through.

1. **Could failure cause harm to a person?** (physical, financial, or legal — use the domain's own definition of harm)
   - **YES → T1.** A safety floor: built into the system, impossible to switch off through normal administration.
2. **Does the change need new system logic or structure?** (new calculation, workflow, decision, integration, state transition)
   - **YES → T2.** Engineered behavior; changed by Engineering through a code release.
3. **Does it change only a governed value/setting used by existing logic?** (rate, limit, date, mapping, threshold, choice)
   - **YES → T3.** Configurable by an authorised business administrator — configurable is NOT unguarded.
4. **Otherwise → ? (Unclassified).** Not enough evidence, or not a business rule at all. "Unclassified — pending investigation" is a legal, honest answer.

### Rules of the flow
- Never start at T3. Never classify upwards to look thorough, never downwards to avoid work.
- A rule forced into the wrong tier is worse than one marked "we do not know yet" — nobody revisits a forced rule.
- If a rule genuinely contains several tiers, **split it into atomic rule parts** and classify each part.

## T1 — Protect the person

**Definition:** a rule whose failure or removal could cause a person to be harmed. In a clinical domain this is the patient; in an HR domain this is an employee (e.g. statutory leave entitlements, salary payable correctly, sensitive personal data protected).

### The test
"If this rule fails, or someone disables it, could a person be physically, financially, or legally harmed?"

### What a T1 rule must be
- Built into the system, not into a setting. Impossible to switch off through normal administration.
- Approved by the governing authority for the domain (e.g. Clinical Governance for health, statutory/HR governance for HR).
- Tested for failure scenarios, not only normal ones.

### T1 rule categories — check against every place a person is exposed
Walk each category against each way a safe action can go wrong. Every filled cell is a candidate T1 rule; an empty cell is a written question, not a comfort.

| Category | Protects against |
|----------|------------------|
| Access & triage | Care/service cannot be reached in time |
| Identity & context | Wrong person or context is used |
| Clinical/business decision | The wrong option is chosen |
| Execution | Right decision, wrong delivery |
| Monitoring & escalation | Failure is never detected |
| Continuity & transition | Service stops during a handover |

### Eight required fields — a T1 rule missing any is not finished
1. **Context** — when does the protection apply?
2. **Hazard** — what harm is prevented?
3. **Safety invariant** — what must always/never happen?
4. **Safe fallback** — what happens when a dependency fails?
5. **Override policy** — is an override allowed, by whom?
6. **Escalation** — who is notified when it activates?
7. **Evidence** — how do we prove it works?
8. **Owner** — which governing authority approves it?

One-sentence form:
> In [clinical/business context], the system must never [unsafe outcome].
> If [dependency fails], it must [safe fallback] and notify [role].

### Two cross-cutting controls (run on every T1 rule)
- **Failure & recovery:** what happens during an outage, a timed-out integration, missing/stale data, partial deployment, or unloadable configuration? Is the default response safe? *Silence is not a safe default* (e.g. an allergy service that is down must never report "no known allergies").
- **Protection integrity:** can an administrator, an ordinary setting, a manual override, or an old version disable or bypass it? A T1 protection a setting can switch off was never a T1 protection.

### What is NOT automatically T1
Financial loss, fraud, regulatory non-compliance, privacy breach, slow performance, incorrect reports, poor UX. These become T1 **only** when there is a credible path to personal harm.

## T2 — Control the process

**Definition:** the recipe — how the system behaves. If a change needs new machinery, it is T2 whatever it is called.

| Category | What it governs | Example |
|----------|-----------------|---------|
| T2.1 Decision & validation | How conditions are evaluated and an outcome is chosen | A new eligibility algorithm |
| T2.2 Calculation & transformation | How values are calculated, allocated, converted, rounded | A new tax or allocation formula |
| T2.3 Workflow & state lifecycle | How something moves through states, approvals, reversals | Add a second approval step |
| T2.4 Orchestration & execution | Order of rules, sources, fallbacks, retries, jobs | Try source A, then B, then fallback |
| T2.5 Integration & interface | How the system talks to another system | Add a government or insurer link |
| T2.6 Persistence & integrity | How data is versioned, locked, committed, recovered | Locking or version history |
| T2.7 Output & document structure | How reports, invoices, documents are constructed | A new invoice generation engine |

- If a change genuinely contains two structures, it is two T2 rules. Split it.
- **T2 ladder** (stop at the first yes): Integration → Workflow → Calculation → Persistence → Output → otherwise Decision logic.

## T3 — Store the value

**Definition:** ingredients and measurements fed to machinery that already exists and is tested. Only the data changes; the method stays the same.

| Category | What it holds | Example |
|----------|---------------|---------|
| T3.1 Quantitative | Rate, amount, threshold, limit, factor, quantity | Tax rate = 15% |
| T3.2 Temporal | Date, duration, window, deadline, frequency, schedule | Approval valid 30 days |
| T3.3 Eligibility & scope | Who or what is included or excluded | Products excluded from cover |
| T3.4 Mapping & reference | Relationship or translation between entities/codes | Product type → price list |
| T3.5 Policy selection | Choice between existing, tested behaviours | Use purchase date or service date |
| T3.6 Content & template | Governed text, messages, document content | Invoice footer wording |

- **Classify by business meaning, not database type**: a numeric product ID that links a product to a category is a MAPPING, not a quantity.
- **T3 ladder** (stop at the first yes): Content → Mapping → Eligibility & scope → Policy selection → Temporal → Quantitative.
- **T3 is configurable, NOT unguarded**: a named owner, min/max validation, effective from/to dates, approval, audit trail, rollback.

### Boundary cases that catch everyone
- **A new option is T2.** Choosing between two existing, tested options can be T3. Adding a behaviour that never existed is T2.
- **A threshold is two rules.** "Above 100,000, require two approvals" splits into a T2 workflow rule and a T3 quantitative parameter (100,000).
- **A toggle is only T3 if it is harmless.** Both behaviours must already exist and be tested, the administrator authorised — and the toggle must not be able to bypass a T1 protection. A switch that disables safety is never an ordinary setting.
- **Effective dates are T3 — the selector is not.** The configured date is T3; the algorithm that picks the latest effective record is T2.

## Domain adaptation

The method is health-anchored ("patient" / "Clinical Governance"). Translate it to the domain you are classifying:
- **Person harmed:** patient → employee (or citizen/customer) as defined by the domain.
- **Governing authority for T1:** replace Clinical Governance with the domain's authority (statutory/HR governance, regulatory body, chief medical officer, etc.); record it by name.
- **Safety-relevant values:** in HR, statutory leave balances, salary/tax rates, and payroll data protection are the analog of safety-critical clinical data — test T1 on them even when they look like ordinary settings.

## Rule writing format

> When [condition], the system must [action].

One sentence. Present tense. No "should probably". If a sentence holds two conditions, you are holding two rules — split it.

## Gap identification — six gap types

For each rule part, write current vs required, then name the gap. The corrective action follows from the gap type.

| Gap | Meaning | Action |
|-----|---------|--------|
| A · Safety | A decision can harm a person and no T1 protection exists | Fix first, always. Highest attention. |
| B · Wrong-tier | Real rule, controlled in the wrong place (hard-coded value, admin-editable workflow) | Move it to the right tier. |
| C · Mixed-rule | Safety, logic and values in one big rule | Decompose into T1 / T2 / T3. |
| D · Governance | A setting editable with no owner, approval, audit, dates or rollback | Add the controls, keep the tier. |
| E · Implementation | Approved policy and actual system behaviour differ | Fix one of the two, deliberately. |
| F · Evidence | Nobody can prove how the rule works today | Mark "needs validation". Never assume. |

Fix in risk order: Safety → Compliance & financial integrity → Wrong-tier & mixed → Governance → Evidence.

## Worksheet — six columns

One line per rule part. Nothing else needed to start.

| Rule | Current situation | Required situation | Tier | Gap | Action |
|------|-------------------|--------------------|------|-----|--------|
| (one sentence) | (what happens today) | (what should happen) | T1/T2/T3/? | A–F | (one owner + one next action) |

- Write both sides in plain language. If you cannot write the required side, you have not agreed it yet.
- Add columns later (evidence, business owner, technical owner, current controls, status) — but do not start with 16 columns.

## Workflow — classifying an existing register

1. **Harvest:** every rule record is the start, but rules also hide in service contracts, dependency notes, lookup lists, feature descriptions, and code comments.
2. **Split:** one record often holds several rules. Decompose before classifying.
3. **Classify:** run the four questions in order on each atomic part.
4. **Cover:** walk the T1 categories × failure modes; every empty cell becomes a written question.
5. **Check:** test new rules against rules already live in other modules. Name and resolve every conflict. "No rule changes on either side; one integration call closes three safety gaps" is a valid resolution.

### Start small
Open five rules, not the whole register. Finish five properly and the next twenty take half the time. Five rules a week clears a 100-rule register in a quarter — with evidence.

## Definition of done — a rule is "done" only when ALL of these hold

- [ ] Expected behaviour written in one plain sentence.
- [ ] Actual behaviour proven — code, configuration, test or interview. An undocumented assumption is not a confirmed rule.
- [ ] Tier agreed and recorded.
- [ ] Mixed-tier parts separated.
- [ ] Business owner AND technical owner named.
- [ ] Required controls exist (validation, dates, approval, audit).
- [ ] Normal AND failure scenarios tested.
- [ ] T1 rules carry the domain governing authority's approval.
- [ ] T3 changes authorised, validated, audited, reversible.

Otherwise it is still open. Mark it "needs validation" and move on — honestly recorded beats confidently wrong.

## Rules / anti-patterns

- **Everything becomes T1.** If all rules are safety rules, none of them are. T1 is for personal harm — not revenue, not embarrassment.
- **T3 = anyone can edit.** Configurable and ungoverned are different words. Owner, limits, dates, approval, audit, rollback.
- **Tier treated as importance.** A wrong T3 value can cost real money. Tier is about control, not value.
- **The register becomes the goal.** A beautiful sheet with no owners and no actions has changed nothing. Every line ends in a name and a date.

## Output

Deliver the classified rules as the six-column worksheet (extended with owners and status when the user asks). Show all eight required fields for every T1 rule. Ensure every line ends in a business owner, a technical owner, and a next action. Present a concise summary of the tier distribution (counts per tier, gap counts) and any rules left as "?" with the reason.