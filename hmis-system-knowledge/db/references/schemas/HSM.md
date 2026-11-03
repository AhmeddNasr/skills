# HSM: patient, visit and product review

Read [extended configuration/lifecycle/projection review](../hospital-structure-rules.md) and its evidence register before relying on this summary. Full deployed-workflow coverage remains incomplete.

## Observed business-flow study

Hospital structure hierarchy, beds and assignment type/classification determine projection routing. Reviewed room save writes HSAssigment, refreshes OPD medical nurse-station specialties, updates BedMgt copies, removes old ER/OR projection when classification changes and calls the new classification owner. Delete guards nurse-station use, deactivates assignments/deletes specialty links and calls ER/OR removal. This study does not implement deferred setup migration.

Evidence: HospitalStructureManagerFactory room-save815-965 and delete1101-1183; assignment samples/lookups.

Read samples-bundle.json (schema HSM) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema HSM) for captured lookup/configuration keys (where present), and sql-objects/HSM.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| HospitalStructure | No exact anchor-name candidate | Review ownership | EntityID | 2/5 |
| HospitalStructureBed | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| HSAssigment | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| HSSpecialities | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| LKP_FloorName | No exact anchor-name candidate | editable lookup name | EntityID | 0/0 |
| SLKP_AssignmentClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AssignmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 1/2 |
| SLKP_HospitalStructureType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/HSM.json (one level above this folder) for full columns, indexes, defaults and FK mappings.