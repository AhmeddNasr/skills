# DotcarePortal: patient, visit and product review

## Observed business-flow study

Jobs portal audit writes ActionLog header and per-row ActionLogDetail in a local SQL transaction after execution; logging failures are best-effort and do not prove a job failed. JobToggle controls job availability and PortalAdmin is a separate portal admin list. VisitId in audit detail is an execution reference, not clinical ownership. This is different from the migration portal protected store.

Evidence: DotCareHMIS-JobsPortal/Handlers/Helpers/PortalActionLogger.cs LogJobExecution; JobToggleService; PortalAdminService.

Read samples-bundle.json (schema DotcarePortal) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema DotcarePortal) for captured lookup/configuration keys (where present), and sql-objects/DotcarePortal.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| ActionLog | No exact anchor-name candidate | Review ownership | EntityId | 0/1 |
| ActionLogDetail | visit: VisitId | Review ownership | none named EntityID | 1/0 |
| JobToggle | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PortalAdmin | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/DotcarePortal.json (one level above this folder) for full columns, indexes, defaults and FK mappings.