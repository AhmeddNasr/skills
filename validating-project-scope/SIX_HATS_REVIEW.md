# Six Thinking Hats Review (de Bono)

A structured technique for reviewing a requirement or backlog item from six distinct perspectives. Apply this between the INVEST check and the DoR alignment to catch qualitative gaps that mechanical checklists miss.

**The core principle:** Examine the item one perspective at a time. Do not mix optimism with caution in the same breath. Each hat gets its own focused pass.

---

## The Six Hats

| Hat | Perspective | Key Question | What to Look For |
|-----|-------------|--------------|-----------------|
| **White** | Facts & Data | "What do we know, and what is missing?" | Missing metrics, undefined baselines, unverified assumptions, gaps in data. |
| **Red** | Emotion & Intuition | "How do we feel about this without justifying it?" | Stakeholder resistance, gut-level concerns, excitement that might bias judgment, unspoken fears. |
| **Black** | Caution & Risk | "Why might this fail, and what are the dangers?" | Technical risks, integration failure points, security vulnerabilities, dependency on uncommitted teams, single points of failure. |
| **Yellow** | Optimism & Value | "What is the value, and why is this a good idea?" | Business value, user satisfaction, competitive advantage, cost savings, alignment to strategic goals. |
| **Green** | Creativity & Alternatives | "What are the alternatives, and can we do this differently?" | Simpler solutions, existing tools that already solve the problem, process changes instead of code changes. |
| **Blue** | Process & Control | "What is our goal, and what is the next step?" | Scope alignment, readiness to proceed, missing governance steps, unclear ownership. |

---

## How to Apply the Review

Run each hat as a separate pass over the requirement. Do not skip any hat. Record findings per hat:

1. **White Hat:** List all known facts and all missing data. If critical data is missing (e.g., no baseline metric for "improve performance"), the requirement is not ready.
2. **Red Hat:** Note any stakeholder resistance, team fatigue, or political concerns. These are real risks even if unquantified.
3. **Black Hat:** Identify every plausible failure mode. Cross-reference with `ado_ado_get_test_results_by_build` or `tfs_tfs_get_test_results_by_build` for historical failure patterns.
4. **Yellow Hat:** Confirm the requirement delivers measurable value. If the Yellow hat finds no clear value, the Black hat wins by default.
5. **Green Hat:** Challenge whether a simpler alternative exists. Could a process change solve this instead of a code change? Could an existing tool or feature be configured instead of built?
6. **Blue Hat:** Confirm the requirement is scoped, owned, and has a clear next step. If accountability is unclear, route to [Stakeholder Analysis](../eliciting-business-needs/STAKEHOLDER_ANALYSIS.md) for RACI assignment.

---

## Decision Rule

- If **Black** finds a critical, unmitigated risk → **Reject** and flag for risk resolution.
- If **White** finds missing essential data → **Reject** and flag for data gathering.
- If **Yellow** finds no measurable value → **Reject** and flag for value justification.
- If **Green** finds a simpler existing alternative → **Reject** and flag for alternative evaluation.
- Only if all six hats produce acceptable findings → **Pass** to DoR alignment.
