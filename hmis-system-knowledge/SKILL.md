---
name: hmis-system-knowledge
description: The single knowledge base for HMIS / DotCare — what we learned while working (configuration keys, lookups, screens, terminology, feature history by PBI, past corrections) plus the DotCare database study (schema catalog, FK and application links, visit/product/package flows, caches, SQL objects, migration conventions) with lookup scripts. Load it at the START of any HMIS work: writing, reformatting or reviewing a user story or PBI, investigating an ADO work item, querying an HMIS database, schema or dependency questions, business-flow reviews, SQL or migration design, or analysing a module such as CPOE, Physician Desktop, Lab and Rad, Blood Bank, Billing. It is self-updating — after every lookup (DB query, ADO read, code search) and every user correction, record what was learned before the turn ends.
---

# HMIS System Knowledge

Two mandatory jobs: **read** what is known before working, and **write back** what you learned before the turn ends. Read only what the task needs: this file is the index.

## Step 1 — Read (token-light)

1. **Always** read the `## Don't repeat` section at the top of `references/general.md`, and its `## Writing stories about how HMIS is built` section when writing a story.
2. For each module the work touches (use the table; modules overlap, e.g. lab orders live in `cpoe.md`), read that file's `## Don't repeat` section in full.
3. Then **search, don't read whole files**: Grep `references/` for the work's key terms (PBI IDs, screen, table, configuration and feature names), read the matching `##` sections. Read a whole module file only when the work is broad or the search finds little. Use the Grep tool (`grep -i` aborts in this Git Bash).
4. For schema/structure questions, run the DB scripts (below) before querying the live DB. Never open the big JSON files under `db/references` directly.
5. If a fact is **Unconfirmed** and matters, verify it (DB query, ADO read) or ask the user, then update its status.

| File | Topics |
|------|--------|
| `references/general.md` | configurations (DB values, no screens), configuration tables, query-tool quirks, shared lookups (visit classification, visits, visit status, physician per visit type), ADO conventions, `Custom.Module` values, permissions (`Security.*`), story-writing rules |
| `references/cpoe.md` | MediSpan, drug/allergy alerts, override, ordering (medication, lab, imaging, procedure, package), Order Entry screen, favorite list, order set, treatment plan / CPG, product classifications, NPHIES CS tracking, internal (predicted) approval → VM, `CPOE.*` tables |
| `references/lab-and-rad.md` | lab/rad results, statuses and types, reference ranges, normality, completing results, lab grid, visit popover, `LR.*` |
| `references/physician-desktop.md` | floating control bar, quick add, patient banner, episodes, widgets, feature 34938 unassigned-visit restrictions |
| `references/vital-signs.md` | vitals, vitals widget, normal ranges, high/low, SpO₂ / pain / consciousness scales, `VS.*` |
| `references/blood-bank.md` | blood bank, transfusion orders, units/bags, reserve, cross-match, dispense, return, discard, compatibility, donor, donation, questionnaire, consent, split, external units, ISBT 128 / DIN, eMAR blood, `BloodBank.*`, `CPOE.Transfusion*` |
| `references/corrections-log.md` | dated history of every correction (each one is also in its module's `## Don't repeat`) — search only |
| `db/GUIDE.md` | full DotCare DB study guide — read for DB flow studies, dependency/impact analysis, SQL scripts, migrations |
| `db/references/schemas/<Schema>.md` | per-schema worksheet (tables, setup/domain candidates) — read the one schema you need |
| `db/references/*.md` | `core-flows` (visit/product/package identities), `module-map`, `database-flow-study`, `configuration-audit`, `cache-writers`, `reversal-flows`, `review-procedure`, `action-script-design`, `migration-conventions`, `hospital-structure-rules` (HSM), `security-flow`, `*-Integration.md` |

Add `references/<module>.md` (with a `## Don't repeat` section) when a new module starts, and add a row above.

## DB study (`db/`) — reference, not proof

The DB study is a dated (Oct 2026), permission-limited snapshot. Use it to know where to look; verify against the live DB (`hmis-prelive-db`, `hmis-devtest-db`, `anc-prelive-db`), code or the user before relying on it. If they conflict, the live source wins and you tell the user. When citing it, say "per the DB study, not yet verified".

Scripts (run them from `db/`):

- `python -I scripts/inspect_schema.py --table CPOE.Configuration` · `--schema VisitMgt` · `--neighbors VisitMgt.VisitService` · `--search PackageServiceID` · `--required` (with `--table`) · `--readers <table>` · `--object <view/proc>` · `--limit n` (check `Truncated`)
- `python -I scripts/trace_dependencies.py --root VisitMgt.Visit --direction incoming --depth 2` — declared FK dependencies only, not a delete planner
- `python -I scripts/inspect_events.py --event MPI_PatientMerged` — cache/event subscriptions
- `python -I scripts/read_schema_evidence.py --kind samples|setup-vocabularies --schema HSM` — one schema's samples or setup vocabulary
- `python -I scripts/check_skill.py` — self-test of the DB study

Key invariants (details in `db/GUIDE.md` and `db/references/core-flows.md`): package header VisitService ID, PatientPackage purchase ID, master Package ID and member billing transaction ID all differ; `OrderlineID` is polymorphic (check order family, visit, product, classification before joining); matching numeric IDs are not relationship evidence; `IsDeleted` alone is not full cancellation; HSM assignment cache routing needs `AssignmentTypeID` and `AssignmentClassificationID`. Read-only: bounded SELECTs, no PHI, no NOLOCK as proof, no writes.

## Step 2 — Write back

Write back when, this turn, a DB lookup showed structure or reference data, an ADO item showed how a feature works, code showed an implementation, the user stated a fact, or **the user corrected an assumption** (highest value — always record).

1. Pick the file by **where the fact applies**: cross-module or a pattern → `general.md` (when unsure, here); one module → that module's file; DB-study gaps or errors → the module file for that schema (e.g. `VisitMgt` → `general.md`, `CPOE` → `cpoe.md`), noting "corrects DB study `<file>`". Update existing entries instead of duplicating; fix or remove wrong ones. Re-read a file just before editing it (other sessions edit too).
2. **Correction** → add the line to the module's `## Don't repeat` section **and** to `corrections-log.md` (newest first): `YYYY-MM-DD — [module] Assumed: … → Actually: … (PBI)`. Also fix the fact itself in the module file.
3. Tag each fact `[Confirmed — <source>, <YYYY-MM-DD>]` or `[Unconfirmed — <why>]`. One fact per bullet, names in `code`, no narrative.
4. Tell the user in one line ("Added to hmis-system-knowledge: …").

**Never record:** secrets or signed URLs (key name + "URL" only), patient data / PHI, real visit or patient IDs, employee names tied to records, one-conversation details (draft wording), large data dumps.

## With `user-story-template`

The rules in `general.md` § "Writing stories about how HMIS is built" and every `## Don't repeat` section override generic template habits (e.g. configurations are database values, not admin screens).
