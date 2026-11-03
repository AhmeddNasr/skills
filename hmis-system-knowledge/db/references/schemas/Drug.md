# Drug: patient, visit and product review

## Observed business-flow study

Drug schema is configuration, frequency/duration reference conversion and MediSpan request/response logging, not the primary medication master. Reviewed patient mapper combines requested patient/drugs, configured previous-order range, CPOE previous orders and renal lab values before normalization; home-medication/current-visit rules differ. Request/response payloads were not sampled.

Evidence: DrugDB PatientMapperManagerFactory.Map42-132; configuration/key and safe log-state samples.

Read samples-bundle.json (schema Drug) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Drug) for captured lookup/configuration keys (where present), and sql-objects/Drug.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistoryDrug | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| FrequancyDurationDDL | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MediSpanCallLogs | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Drug.json (one level above this folder) for full columns, indexes, defaults and FK mappings.