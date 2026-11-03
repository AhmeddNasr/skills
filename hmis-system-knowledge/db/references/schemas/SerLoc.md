# SerLoc: patient, visit and product review

## Observed business-flow study

ServerService and ServiceAction map an action name to base URL+relative URL and method. Reviewed locator retrieves the row and builds the proxy from these values; a missing action fails and the reviewed proxy rejects calls to a module marked optional. Endpoint configuration affects every cross-module callback; it is not owned patient/visit data. Logs can contain payloads and were excluded.

Evidence: ServiceLocatorModel.GetServiceProxy50-108; ServiceProxy optional-module branch109-121; table relationship samples.

Read samples-bundle.json (schema SerLoc) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema SerLoc) for captured lookup/configuration keys (where present), and sql-objects/SerLoc.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Log | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ServerService | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ServiceAction | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/SerLoc.json (one level above this folder) for full columns, indexes, defaults and FK mappings.