# Screening: patient, visit and product review

## Observed business-flow study

Questionnaire is a visit/patient capture aggregate that orchestrates MedicalHistory, diagnosis, Allergy and MPI marital-status services before saving its local snapshot children. Success of a questionnaire is not independent of these domain writers. Deleting only Questionnaire cannot reverse longitudinal medical-history updates already made.

Evidence: QuestionnaireManager.SaveMedicalHistory317-475; questionnaire/main history matching patient/visit samples.

Read samples-bundle.json (schema Screening) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Screening) for captured lookup/configuration keys (where present), and sql-objects/Screening.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ConfigurationTabs | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| CurrentSymptoms | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Disease | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| FamilyMedicalHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| ObsGynContraception | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| ObsGynMedicalHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| PatientMedicationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 4/0 |
| Questionnaire | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/6 |
| SLKP_AlcoholUse | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AllergySeverity | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_AllergyType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_CaffieneDose | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Contraception | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Duration | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_EnvironmentalAllergy | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_FamilyType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_FoodAllergy | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_FrequencyUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_MaritalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MedicationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Mode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Occupation | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SmokingStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SnomedReaction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SocialMedicalHistory | No exact anchor-name candidate | Review ownership | EntityID | 8/0 |
| SurgicalMedicalHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Screening.json (one level above this folder) for full columns, indexes, defaults and FK mappings.