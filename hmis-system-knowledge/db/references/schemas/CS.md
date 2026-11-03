# CS: patient, visit and product review

## Observed business-flow study

Form/category/configuration setup feeds patient clinical-sheet records and state. Reviewed add checks the form and sets draft/sign state and timestamps; edit selects an existing draft and uses ModifiedTS; cancellation selects a signed sheet and sets cancel reason/comment/date with concurrency control; soft deletion is a separate operation. Related-visit retrieval can display episode sheets. The merge handler updates identity/display fields for transferred visits.

Evidence: ClinicalSheetManager.AddPatientClinicalSheet364-459 and DeleteClinicalSheet332-363; ClinicalSheetFactoryManager.CancelClinicalSheet94-130; PatientClinicalSheetManager.UpdateCSPatientMQ46-85.

These are reviewed source/sample findings, not proof that every deployed branch or external acknowledgement was exercised.

Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Category | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| ConfigurationSheet | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Form | No exact anchor-name candidate | Review ownership | EntityID | 1/3 |
| FormVisitClassification | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PatientClinicalSheet | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 4/1 |
| PatientClinicalSheetSignLog | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| SLKP_CancelReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_FormType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Type | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| UserFavoriteForm | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/CS.json (one level above this folder) for full columns, indexes, defaults and FK mappings.