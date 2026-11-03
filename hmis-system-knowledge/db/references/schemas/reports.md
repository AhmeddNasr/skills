# reports: patient, visit and product review

## Observed business-flow study

Mostly functions/views/procedures over source domains, not owned transaction tables. Base tables include ActiveEntity and linked_visits. Reviewed stock functions calculate quantity/cost from barcode/balance/transfer states and UOM conversions. One current-quantity function assigns a single warehouse-location variable; one last-cost function uses a global TOP1 over the supplied list. Do not assume these are universally correct multi-location/multi-product reconciliation helpers without checking input scope.

Evidence: Selected live SC report function definitions; 822 SQL object contracts; all base-table safe samples.

Read samples-bundle.json (schema reports) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema reports) for captured lookup/configuration keys (where present), and sql-objects/reports.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| __MigrationsHistory_RBO | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| __MigrationsHistory_RFinance | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ActiveEntity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| linked_visits | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/reports.json (one level above this folder) for full columns, indexes, defaults and FK mappings.