# Security: patient, visit and product review

## Observed business-flow study

Actor identity and entity context apply across patient/visit/product domains. Backend API and frontend page-action permission chains share Permission/Role grants, with static/admin/version-dependent exceptions. Additional entity assignment controls navigation, not automatic combined visibility. Shared EntityID0 is mainly setup/config; copied employee/physician bindings and token/menu state require refresh-aware handling.

Evidence: security-flow.md and security-evidence.json; user-confirmed entity rule.

Read samples-bundle.json (schema Security) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Security) for captured lookup/configuration keys (where present), and sql-objects/Security.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| APIController | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| BusinessAction | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| BusinessEntity | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| BusinessEntityGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| ChildObject | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| ClientAction | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| DomainObject | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| DomainObjectSharing | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| Entity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| LKP_Role_Status | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| Module | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| Page | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| PageActionAccess | No exact anchor-name candidate | Review ownership | none named EntityID | 2/1 |
| PageActionPermission | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| Permission | No exact anchor-name candidate | Review ownership | none named EntityID | 2/3 |
| ProjectService | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| Report | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| ReportParameter | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Role | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| RoleGroup | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| RolePermission | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SharedEntityGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SLKP_AssignmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AuthenticationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_EmployeeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| User | No exact anchor-name candidate | Review ownership | EntityID | 3/4 |
| UserEmployee | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| UserEntity | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| UserPhysician | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| UserRole | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| WebAction | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| WebActionPermission | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Security.json (one level above this folder) for full columns, indexes, defaults and FK mappings.

Read ../security-flow.md for reviewed security behavior and all-table ownership notes.