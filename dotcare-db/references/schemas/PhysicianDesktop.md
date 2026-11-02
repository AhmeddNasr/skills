# PhysicianDesktop: patient, visit and product review

## Observed business-flow study

Desktop assignments are polymorphic left/right items typed by SLKP_Relation, not universal physician FKs. Add prevents duplicate physician/specialty/nurse-station assignments and copies labels; access list combines Security physician roles, assignments and the current physician. Widgets/configuration query patient/visit source projections; they do not own the underlying clinical history.

Evidence: AssignmentTransactionManagerFactory.AddAssignmentTransaction32-133; widget manager entry points and table samples.

Read samples-bundle.json (schema PhysicianDesktop) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema PhysicianDesktop) for captured lookup/configuration keys (where present), and sql-objects/PhysicianDesktop.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AssignmentTransaction | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| DiagnosisConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| MenuItem | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| MenuItemVisitClassification | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| MenuItemVisitClassificationStatus | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PatternInstanceDetail | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PdfConfig | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| PdfHeaderFooterConfig | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| SLKP_Entity | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Relation | No exact anchor-name candidate | static lookup name | none named EntityID | 2/1 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_VisitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| VisitClassification | No exact anchor-name candidate | Review ownership | EntityID | 0/3 |
| Widget | No exact anchor-name candidate | Review ownership | EntityID | 0/4 |
| WidgetHideVisitSpeciality | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WidgetMenuItem | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WidgetVisitClassification | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| WidgetVisitClassificationStatus | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WidgetVisitSpeciality | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/PhysicianDesktop.json (one level above this folder) for full columns, indexes, defaults and FK mappings.