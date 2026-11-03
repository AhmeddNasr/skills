# PatPrlm: patient, visit and product review

## Observed business-flow study

Patient/visit chief complaints, diagnosis problem cards and detail/history records connect ICD setup to visit diagnosis caches. Add can update MPI marital status for maternity, writes cards, synchronizes VM diagnosis code/name and checks treatment-plan relevance. Dated BKP tables also exist and are not automatically live clinical ownership.

Evidence: ProblemCardManagerFactory.Add101-190; cohort and backup-table samples.

Read samples-bundle.json (schema PatPrlm) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema PatPrlm) for captured lookup/configuration keys (where present), and sql-objects/PatPrlm.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CachedEntity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ChiefComplaint | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| ChiefComplaint_BKP_20261001 | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| LKP_DiagnosesAddedDays | product: ServiceID | editable lookup name | none named EntityID | 2/0 |
| LKP_Diagnosis | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/2 |
| LKP_DiagnosisICD10 | No exact anchor-name candidate | editable lookup name | none named EntityID | 1/0 |
| LKP_service | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| MorphologyFlaggedDiseases | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PhyscianChiefComplaint | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PhyscianDiagnoses | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| ProblemCard | patient: PatientID; visit: VisitID | Review ownership | EntityID | 4/1 |
| ProblemCard_BKP_20261001 | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| ProblemCardDetail | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ProblemCardDetail_BKP_20261001 | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| SignsAndSymptoms | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| SignsAndSymptoms_BKP_20261001 | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| SLKP_Configuration | No exact anchor-name candidate | static lookup name | EntityID | 0/0 |
| SLKP_DiagnosisType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MartitalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MorphologicalDiagnose | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Occurence | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_OutCome | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Problem | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SpectialityDiagnoses | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/PatPrlm.json (one level above this folder) for full columns, indexes, defaults and FK mappings.