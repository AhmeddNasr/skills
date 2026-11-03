# DBA: patient, visit and product review

## Observed business-flow study

Database monitoring owns blocking, size, index, query and restart diagnostic data. Visible monitoring procedures include blocked-session/heavy-query/missing-index collectors. These are infrastructure records, not owned patient/visit/product children; SQL text/plan payloads can contain sensitive content and were excluded from data samples. Exact scheduling/retention is not inferred from table names.

Evidence: SQL object metadata, safe/presence samples and visible DBA procedure list.

Read samples-bundle.json (schema DBA) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema DBA) for captured lookup/configuration keys (where present), and sql-objects/DBA.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| BlockedSessions | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DailyMonitoringReport | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DatabaseFileDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Databases_Size | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| HeavyQueryAnalysis | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IndexExecutionPlans | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IndexUsageStats | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IndexUsageStats_History | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Last_restart | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Logchanges | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MissingIndex | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/DBA.json (one level above this folder) for full columns, indexes, defaults and FK mappings.