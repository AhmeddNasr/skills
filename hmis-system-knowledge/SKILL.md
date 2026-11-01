---
name: hmis-system-knowledge
description: Living knowledge base of how the HMIS system actually works — database tables and configuration keys, lookups, screens, module terminology, feature history by PBI, and past corrections. Load it at the START of any HMIS work (writing, reformatting or reviewing a user story or PBI, investigating an ADO work item, querying an HMIS database, analysing a module such as CPOE, Physician Desktop, Lab and Rad, Billing) and read the module's reference file before drafting anything. It is self-updating — after every lookup (DB query, ADO read, code search) and every time the user corrects an assumption, append what was learned before the turn ends.
---

# HMIS System Knowledge

## Purpose

This skill is the memory of what we have learned about the HMIS system while working together. It grows with every investigation and every correction, so the same mistake is not made twice and the same lookup is not repeated.

It has two jobs, and **both are mandatory**:

1. **Read** — before writing or analysing anything, read what is already known.
2. **Write back** — after looking something up or being corrected, record it here before the turn ends.

## Reference Files

| File | What it holds | Topics (read it when the work touches any of these) |
|------|---------------|------------------------------------------------------|
| `references/general.md` | Facts that apply across modules | configurations, database conventions, query tools, shared lookups (visit classification), ADO conventions, story-writing rules — **always read** |
| `references/corrections-log.md` | Every correction the user has made | **always read** |
| `references/cpoe.md` | CPOE / Order Entry specifics | ordering anything (medication, laboratory, medical imaging, procedure, package orders), Order Entry screen, favorite list, order set, treatment plan / CPG, product classifications, `CPOE.*` tables |
| `references/lab-and-rad.md` | Lab and Rad (`LR` schema) specifics | lab or radiology results, result statuses and types, reference ranges, normality, completing results, `LR.*` tables |
| `references/physician-desktop.md` | Physician Desktop / physician portal specifics | floating control bar, quick add, patient banner, physician workspace design, feature 34938 unassigned-visit restrictions |
| `references/vital-signs.md` | Vital signs (`VS` schema) | vital signs, vitals widget, normal ranges, high/low status, SpO₂ / pain / consciousness scales, `VS.*` tables |

Add a new `references/<module>.md` when work starts on a module that has no file yet (e.g. `physician-desktop.md`, `billing.md`), and add a row with its topics to the table above.

**Files are split by where a fact lives, not by which story found it.** A Lab story may need `cpoe.md` (lab orders are placed in Order Entry), and a CPOE story may need `lab-and-rad.md`. Modules overlap, so never read only "the module's" file.

## Step 1 — Read Before Working

1. Read `references/general.md` and `references/corrections-log.md` in full (always, whatever the module).
2. Read **every** module file whose Topics column touches the work, not just the file for the story's `Custom.Module`. When in doubt, read it — the files are short.
3. Search **all** reference files for the work's key terms (screen names, table names, feature names, PBI IDs), e.g. `grep -ril "favorite\|order entry" references/`. Read any file that matches, even if its module seems unrelated.
4. Use what is there. If a fact is marked **Unconfirmed** and it matters for the work, verify it (DB query, ADO read) or ask the user — then update its status.

## Step 2 — Write Back After Learning

**Trigger — write back whenever any of these happened in the turn:**

- A database lookup returned something about structure or reference data (table names, columns, configuration keys and value formats, lookup values, IDs).
- An ADO work item was read and revealed how a feature works, which PBI introduced it, or its current state.
- A code search or file read showed how something is implemented.
- **The user corrected an assumption** (terminology, how something is configured, how a screen behaves, what a story should or should not say). Corrections are the highest-value entries — always record them.
- The user stated a fact about the system or about how they want it described.

**How to write back:**

1. Choose the file by **where the fact applies**, not by which story found it:
   - Applies to more than one module, or is a pattern (how configurations work, naming conventions, shared lookups, story-writing rules) → `general.md`. **When unsure, use `general.md`.**
   - Only true inside one module (a specific table, key, screen or PBI) → that module's file.
   - Learned during a story for another module (e.g. a CPOE fact found while writing a Lab story) → still goes in the module where it lives, and add any new topic words to that file's row in the table above.
   Update an existing entry rather than adding a duplicate; fix or delete entries that turn out to be wrong. If a module-file fact turns out to apply elsewhere too, move it to `general.md`. Other sessions may be editing these files at the same time — re-read a file just before editing it.
2. For a correction, also add a dated line to `corrections-log.md`.
3. Mark each fact with its status and source:
   - `[Confirmed — <source>, <YYYY-MM-DD>]` e.g. `[Confirmed — prelive DB CPOE.Configuration, 2026-10-31]`, `[Confirmed — user, 2026-10-31]`, `[Confirmed — PBI 32423]`
   - `[Unconfirmed — <why we think so>]` for inferences
4. Keep entries short — one fact per bullet, names in `code`, no narrative.
5. Do it in the same turn as the lookup or correction, not "later". Mention it in one line to the user ("Added to hmis-system-knowledge: …").

## Never Record

- Secrets or signed URLs (some configuration `Value`s contain tokens/`sig=` links — record only the key name and "URL").
- Patient data or any PHI, employee names tied to records, or real visit/patient IDs.
- Things that only mattered to one conversation (draft wording, temporary decisions).
- Large data dumps — record the shape and a few representative values instead.

## Applying the Knowledge in Stories

When this skill is used together with `user-story-template`, the rules in `references/general.md` § "Writing stories about how HMIS is built" override generic template habits (e.g. configurations are database values, not admin screens).
