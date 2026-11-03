# ER: patient, visit and product review

## Observed business-flow study

Triage patient transaction can precede a registered patient/visit; samples include a null PatientID. Regular ER and virtual ER paths have different extension requirements. Acuity/arrival/room/disposition configuration feeds the visit/order path; clinical and billing rows must be traced from the resulting visit rather than treating every triage row as a Visit extension.

Evidence: Original visit classification source/sample study; ER safe samples.

Read samples-bundle.json (schema ER) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema ER) for captured lookup/configuration keys (where present), and sql-objects/ER.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Bed | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| BedStatusLog | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| ConfigurationDetails | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| ConfigurationType | No exact anchor-name candidate | configuration name | none named EntityID | 0/2 |
| DischargeDetail | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| DischargeDetailDisease | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| ErConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| LKP_AccidentType | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| LKP_AdmissionSource | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| LKP_AssessmentAnswer | No exact anchor-name candidate | editable lookup name | EntityID | 1/1 |
| LKP_AssessmentResult | No exact anchor-name candidate | editable lookup name | EntityID | 0/0 |
| LKP_BlockReason | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| LKP_DischargeReason | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| LKP_MOHAssessmentQuestion | No exact anchor-name candidate | editable lookup name | EntityID | 1/1 |
| LKP_Room | No exact anchor-name candidate | editable lookup name | EntityID | 0/2 |
| NoteLog | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PatientAssessment | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| PatientAssessmentDetail | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| PatientTransaction | patient: patientCode, PatientID | Review ownership | EntityID | 7/6 |
| PatientTransactionLog | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SLKP_AcuityLevel | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ArrivalMode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BedStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_DischargeStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_LogType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_SummationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TriageType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| TriageDetail | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Zone | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/ER.json (one level above this folder) for full columns, indexes, defaults and FK mappings.