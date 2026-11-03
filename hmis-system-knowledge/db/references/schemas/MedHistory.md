# MedHistory: patient, visit and product review

## Observed business-flow study

Patient longitudinal social/family/symptom/obstetric/medication/surgical sections also carry visit context and separate logs. Reviewed save replaces existing rows for supplied nonnull sections and appends corresponding logs; social marital status may update MPI. Medication history is not equivalent to an active CPOE prescription. Profile/log tables are another aggregate.

Evidence: MedicalHistoryManager._SaveMedicalHistory748-879; same patient/visit main+log samples.

Read samples-bundle.json (schema MedHistory) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema MedHistory) for captured lookup/configuration keys (where present), and sql-objects/MedHistory.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ConfigurationTabs | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| CurrentSymptomsPatient | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| CurrentSymptomsPatientLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| Disease | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| FamilyPatientMedicalHistory | patient: PatientID; visit: VisitID | Review ownership | EntityID | 2/0 |
| FamilyPatientMedicalHistoryLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 2/0 |
| MedicationPatientHistory | patient: PatientID; visit: VisitID | Review ownership | EntityID | 3/0 |
| MedicationPatientHistoryLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 3/0 |
| ObsGynContraception | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| ObsGynPatientMedicalHistory | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/2 |
| ObsGynPatientMedicalHistoryLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/2 |
| ObsGynPregnancyComplications | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| PatientMedicalHistoryProfile | patient: PatientID | Review ownership | EntityID | 0/0 |
| PatientMedicalHistoryProfileLog | patient: PatientID | Review ownership | EntityID | 0/0 |
| SLKP_AlcoholUse | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_CaffieneDose | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Contraception | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Duration | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_FamilyType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_FrequencyUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_MaritalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_MedicationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Mode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Occupation | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_PregnancyComplications | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SmokingStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SocialPatientMedicalHistory | patient: PatientID; visit: VisitID | Review ownership | EntityID | 7/0 |
| SocialPatientMedicalHistoryLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 7/0 |
| SurgicalPatientMedicalHistory | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| SurgicalPatientMedicalHistoryLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/MedHistory.json (one level above this folder) for full columns, indexes, defaults and FK mappings.