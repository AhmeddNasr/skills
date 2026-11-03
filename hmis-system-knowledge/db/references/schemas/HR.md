# HR: patient, visit and product review

## Observed business-flow study

User-confirmed sync entry is HR.Proc_SyncData (job inactive in test). It reads per-entity source profiles, conditionally establishes linked servers, stages organization units then positions then employees, maps local to universal identities and applies staging to main HR tables. MaxId/LastUpdatedDate configuration supplies watermarks. TransactionType1/2 are applied and become3. Termination derives from last termination record; security user bindings remain a distinct layer.

Evidence: Live definitions of seven Proc_Sync procedures; security-flow.md; HR repository active/nonterminated filters.

Read samples-bundle.json (schema HR) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema HR) for captured lookup/configuration keys (where present), and sql-objects/HR.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| City | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| Configuration | No exact anchor-name candidate | configuration name | EntityId | 0/0 |
| ContractType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| Country | No exact anchor-name candidate | Review ownership | none named EntityID | 0/3 |
| Employee | No exact anchor-name candidate | Review ownership | EntityID | 7/0 |
| EmployeeStatus | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| EmployeeTemp | No exact anchor-name candidate | Review ownership | EntityID | 8/0 |
| Gender | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| Job | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| JobType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| LogError | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MaritalStatus | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| OrganizationUnit | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| OrganizationUnitTemp | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| OrgUnitClassification | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| Position | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PositionTemp | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Region | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| Religion | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| Server | No exact anchor-name candidate | Review ownership | EntityId | 0/0 |
| SLKP_JobTypeConfiguration | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| TablesName | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/HR.json (one level above this folder) for full columns, indexes, defaults and FK mappings.