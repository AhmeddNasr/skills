# Schema-by-schema verification procedure

## Preparation

Read catalog/index.json for capture provenance and visibility. Obtain the target environment through its protected configuration without printing secrets. Use read-only credentials or ApplicationIntent ReadOnly where supported (the latter alone does not enforce read-only). Studies must issue SELECT only. Set bounded command and lock timeouts; use indexed predicates and inspect indexes before expensive queries. Do not launch whole-database data scans.

## For each module

1. Enumerate visible tables and incoming/outgoing FK mappings, including composite keys, untrusted/disabled constraints and lookup ownership. Same-name columns are candidates only.
2. Locate the owning save/update/perform/cancel writer and its business guards. Record file, symbol, line and source revision/hash. Include callbacks, jobs, triggers if visible, events and cache consumers. A filename/method-name search alone is not source review.
3. Choose one de-identified visit per applicable classification, product type and state. Query minimal identifiers/status/quantity/configuration, not demographics or clinical note contents. Include positive, cancelled, partial and reuse examples when available. Avoid interpreting script-modified rows as normal behavior.
4. Trace master setup -> operational order -> visit/service -> billing/tax -> finance, and clinical/stock/bed effects as applicable. Infrastructure/report-only schemas may have no transactional ownership. Say so with evidence rather than inventing a cycle.
5. Distinguish master projection/cache from historical contractual snapshots. Identify entity scope, writer ownership, update timing, stale-data checks and cancellation/reversal semantics. Follow HSM assignment type AND classification when applicable.
6. Reconcile row counts, keys, quantities/UOM, amounts/rounding and active/history state. A missing extension/result can mean pending work; a mismatching value needs corroboration before calling it a defect.
7. Verify deployed flow with authorized UAT: create, edit, perform, cancel/reverse and retry. Read-only samples plus source are not end-to-end UAT. Do not create test patients/orders unless explicitly authorized in the correct environment.
8. Update module-map.md with evidence, counterexamples, unresolved writers and exact verification status. Update application-links.json only for reviewed links, preserving conditions and provenance. Regenerate structure after environment/version changes.

## Deliverable per module

Ownership and entry points; dependencies and lookups; stepwise writes; downstream caches/events; cancellation and reversal; duplicate/retry rules; sample observations; source citations; unresolved risks; next UAT cases. Never promote discovery leads to verified business rules.

The bundled Trace-Visit-ReadOnly.sql is a parameterized study aid from the previous review. Read its header and change its identifiers for the target; it is not a generic production maintenance script. Catalog and script identifiers are evidence, not authorization to operate on those records.
