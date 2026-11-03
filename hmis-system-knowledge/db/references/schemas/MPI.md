# MPI: patient, visit and product review

## Observed business-flow study

Patient master owns reviewed registration address/contact/relationship aggregates and lookup-derived demographics; identification validation and MPIConfiguration govern input rules. Patient merge moves selected visit references and publishes cache updates to consumers such as CS/Allergy. Corrected import, merge and longitudinal history deletion are distinct operations. Search indexing is a separate postcommit effect.

Evidence: Patient-Direct-Import.md; Security and CS source evidence; MPI safe samples and prior registration study.

Read samples-bundle.json (schema MPI) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema MPI) for captured lookup/configuration keys (where present), and sql-objects/MPI.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BlackListRequest | patient: PatientID | Review ownership | EntityID | 3/0 |
| BloodGroupLog | patient: PatientID | Review ownership | none named EntityID | 0/0 |
| BusinessUnitMails | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| DictionaryNames | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LKP_BlackListReason | No exact anchor-name candidate | editable lookup name | EntityID | 1/1 |
| LKP_IdentificationType | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| MergedVisit | visit: VisitID | Review ownership | EntityID | 2/0 |
| MergeLog | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| MergeRequest | No exact anchor-name candidate | Review ownership | EntityID | 6/2 |
| MergeResponse | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| MPIConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| MPIConfigurationType | No exact anchor-name candidate | configuration name | none named EntityID | 0/1 |
| MPIEntity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/4 |
| NewBorn | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| PateintFileSyncLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Patient | No exact anchor-name candidate | Review ownership | EntityID | 10/14 |
| PatientAddress | patient: PatientID | Review ownership | EntityID | 4/0 |
| PatientCenterOfExcellence | patient: PatientID | Review ownership | EntityID | 2/0 |
| PatientChangesLog | patient: PatientID | Review ownership | none named EntityID | 1/0 |
| PatientClassificationLog | patient: PatientID | Review ownership | EntityID | 2/0 |
| PatientContact | patient: PatientID | Review ownership | EntityID | 1/0 |
| PatientDeathInfo | patient: PatientID | Review ownership | none named EntityID | 1/0 |
| PatientSurgeryCandidate | patient: PatientID | Review ownership | EntityID | 1/0 |
| RelativePatient | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| SLKP_BlackListRequestType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_BloodGroup | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_CenterOfExcellence | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_City | No exact anchor-name candidate | static lookup name | none named EntityID | 1/2 |
| SLKP_Country | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_MaritalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MergeCancelReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MergeReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MergeResponseStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MergeStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MergeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Nationality | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Occupation | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PatientClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_PatientRelativeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Region | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_Religion | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ValidationSchemaType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| ValidationSchema | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| ValidationSchemaColumns | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ValidationSchemaDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/MPI.json (one level above this folder) for full columns, indexes, defaults and FK mappings.