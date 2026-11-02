---
name: dotcare-db
description: Reference guide (not a source of truth) for DotCare HMIS structures, visit/product dependencies, package billing, cached module data and migration mappings. Use for DotCare schema questions, business-flow reviews, dependency analysis and SQL or migration design, always verifying its claims against the live database, source code or the team.
---

# DotCare database and business flows

> **Trust level: reference only.** The team does not trust this skill 100%. Use it as a guide to know where to look and what to check, never as proof. Before relying on anything from it in a deliverable (user story, query, script, migration, design decision):
> - Verify schema facts against the live database (the HMIS DB tools) or the source code.
> - Treat its flows, rules and "invariants" as hypotheses until confirmed by current data, code or the user.
> - When you cite it, say so explicitly (e.g. "per the dotcare-db reference, not yet verified") and state what still needs confirming.
> - If it conflicts with the live database, code or what the user says, the live source wins; tell the user about the conflict.
>
> **Keep improving it.** When work reveals something this skill is missing or gets wrong (a table, link, flow, configuration rule or correction confirmed by the live database, code or the user), append it to references/team-learnings.md before the turn ends, with the date, source and evidence. Read that file alongside the other references; where an entry there conflicts with an older reference, the dated, confirmed entry wins.

Study every module from three perspectives: patient, visit and product. Record setup, configuration, static/editable lookups, entity context, authoritative data, copied caches, write/update/cancel paths and evidence gaps. Security is a cross-cutting actor/permission layer, not an owned patient child. Read references/security-flow.md for the reviewed permission and entity behavior.

Start with references/database-flow-study.md for the three-domain overview, then references/module-map.md for schema evidence coverage and references/core-flows.md for visit/product identities. Read only the relevant catalog and module evidence. The catalog is a dated, permission-limited snapshot, not a live database guarantee.

## Inspect structure

Run `python scripts/inspect_schema.py --schema VisitMgt`, `--table VisitMgt.VisitService`, `--neighbors VisitMgt.VisitService`, or `--search PackageServiceID`. Use --limit and check Truncated. With --table, --required lists structural input candidates excluding identity/computed/defaulted/rowversion fields; application requirements still apply.

Per-schema worksheets in references/schemas list every table and domain/setup name candidates; treat these as discovery leads, not verified flow.

Catalog files in references/catalog contain visible columns, indexes and incoming/outgoing FK column mappings for 44 table-bearing schemas. Four additional projection schemas bring visible object-bearing scope to 48; see references/database-scope.json. Preserve composite key order, disabled/untrusted FK status, nullability, precision and shared keys. Do not assume every ID is an identity. Matching numeric IDs are not relationship evidence. references/application-links.json records separately reviewed non-FK links and their conditions.

Use `python scripts/trace_dependencies.py --root VisitMgt.Visit --direction incoming --depth 2` for bounded declared dependency discovery. Outgoing links identify referenced parents; they are not deletion targets. This tool is not an affected-row or delete planner and does not traverse application links. Read its truncation and boundary warnings.

Use `--readers Allergy.PatientAllergyTransaction` to find captured SQL references, separately from owned FK children; dynamic/external usage can be missing.

For database-owned logic, use `--object PatientSummery.VWPSGetAllergiesPerVisit` to read its contract and dependencies from references/sql-objects. For cache paths read references/cache-writers.md and run `python scripts/inspect_events.py --event MPI_PatientMerged`; explicitly commented subscriptions are excluded by default. Source declarations do not prove deployment or delivery.

Read references/samples-bundle.json (schema <Schema>) and references/setup-vocabularies-bundle.json (schema <Schema>) only for the module in question. Samples are bounded and environment-local; configuration keys are not verified configuration values.

## Trace a business question

1. Establish target environment, entity, module, classification and intended action. Revalidate metadata and configuration before executable changes.
2. Follow visit/product anchors through declared links, then reviewed application links. Identify source writers, callbacks, caches, billing snapshots and reversal paths. Follow references/review-procedure.md.
3. Label conclusions structural, source-supported, sample-observed, user-confirmed or end-to-end verified. State missing evidence. Source can differ from deployed binaries; a sample does not prove intended behavior.
4. Compare active and historical/cancelled rows separately. Scripts may have modified samples. Do not repair suspicious rows during a study or turn anomalies into rules.
5. Report ownership, configuration, write order, downstream caches, financial/stock effects, cancellation and unresolved cases, with concrete evidence.

## Completion standard

references/verification-ledger.json tracks unfinished evidence for every visible schema. Do not assert 100% coverage or infer write safety from catalog/sample counts. For HSM, read references/hospital-structure-rules.md, including classification 6, exact callback semantics and remaining gaps.

## Configuration verification

Read references/configuration-audit.md before interpreting settings or allowed actions. Its JSON inventory is an incomplete discovery backlog. Do not claim full business coverage from table sampling. Verify effective entity precedence, defaults, status/classification predicates, consuming writers and cache refresh for the requested action. Visit allowed-action cache uses exact entity matching in the reviewed STF helper; do not assume EntityID 0 fallback.

## Important invariants

- Package header VisitService ID, PatientPackage purchase ID, master Package ID and member billing transaction ID differ. Read core-flows before package queries.
- OrderlineID is polymorphic: validate order family, visit, product and classification before joining.
- Historical package purchases snapshot rules. Do not overwrite them from current master setup as cache maintenance.
- HSM assignment cache routing depends on AssignmentTypeID AND AssignmentClassificationID.
- IsDeleted alone does not implement complete cancellation. Review clinical, stock, billing, tax, package and finance reversals.
- Read references/migration-conventions.md before import design. Adapter defaults are not universal HMIS rules.

## Scope

This skill grants no write authorization. Studies use bounded SELECT queries and minimal de-identified samples. Do not expose patient demographics, clinical text, credentials or tokens. Prefer indexed key paths, timeouts and accurate isolation; do not use NOLOCK results as consistency proof. Never run destructive sample scripts.

For dependency-aware action/script requests, read references/action-script-design.md and references/reversal-flows.md. For authorized writes, verify business writers and dependencies, then use reviewed transactions, duplicate/retry handling and environment-scoped lookup resolution. Identify unsupported classifications and genuinely missing business decisions.

The October 2026 study includes all 48 visible object-bearing schemas, safe/presence samples for every base table, declared-link samples, SQL contracts, event discovery and schema-specific flow findings. These do not certify every deployed branch or external integration end-to-end. Consult the ledger and source evidence before claiming complete coverage for a particular action.



## Claude upload layout

Sample and setup vocabulary files are consolidated without data loss. Read one schema using `python scripts/read_schema_evidence.py --kind samples --schema HSM` or `--kind setup-vocabularies --schema HSM`. References to former per-schema files resolve to their schema keys in the matching references/*-bundle.json. These are skill knowledge resources, not separate team handover documents.
