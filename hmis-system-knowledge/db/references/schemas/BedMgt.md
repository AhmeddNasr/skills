# BedMgt: patient, visit and product review

## Observed business-flow study

Visit/patient bed assignment checks existing visit assignment, occupied/blocked/deleted bed, updates bed status/gender and room gender, writes companion and bed/transaction logs, clears reservation indicators and calls VM accommodation. Transfer/unreserve are separate operations. Shared bed/hospital structure setup is not owned by a visit.

Evidence: PatientBedTransactionManagerFactory.AddPatientBedTransaction70-159; prior read-path evidence.

Read samples-bundle.json (schema BedMgt) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema BedMgt) for captured lookup/configuration keys (where present), and sql-objects/BedMgt.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BedIndicator | patient: PatientCode, PatientID | Review ownership | EntityID | 4/0 |
| BedIndicatorLog | patient: PatientCode, PatientID | Review ownership | none named EntityID | 2/0 |
| BedMgtConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| BedStatusLog | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| CompanionTransaction | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| LKP_Bed | No exact anchor-name candidate | editable lookup name | EntityID | 6/4 |
| PatientBedTransaction | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 7/1 |
| PatientBedTransactionLog | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| SLKP_BlockReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChangeReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Class | No exact anchor-name candidate | static lookup name | EntityID | 0/5 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_GradeChange | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_HospitalStructure | No exact anchor-name candidate | static lookup name | EntityID | 2/1 |
| SLKP_HospitalStructureType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_HRJobCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Indicator | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_IndicatorStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 2/0 |
| SLKP_PatientBedStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RoomGroup | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/BedMgt.json (one level above this folder) for full columns, indexes, defaults and FK mappings.