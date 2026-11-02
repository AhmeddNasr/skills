# CN: patient, visit and product review

## Observed business-flow study

Clinical notes copy patient/visit context and use type/status/cancel setup. Add stamps draft/sign/cancel dates according to status and copies actor display name; replies reject a cancelled note. The reviewed patient-summary note view selects signed status2 and nondeleted rows, so absence there does not establish missing storage.

Evidence: ClinicNoteManagerFactory.AddClinicNote45-85; PatientSummery.VWPSGetClinicalNotesPerVisit live definition.

Read samples-bundle.json (schema CN) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema CN) for captured lookup/configuration keys (where present), and sql-objects/CN.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ClinicalNote | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 3/2 |
| ClinicalNoteMacro | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| CNConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Macro | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| MacroPredefinedFunction | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Reply | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SLKP_CancelReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_NoteClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PredefinedFunction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_PredefinedFunctionOutput | No exact anchor-name candidate | static lookup name | none named EntityID | 1/0 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Type | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_UserType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/CN.json (one level above this folder) for full columns, indexes, defaults and FK mappings.