# OR: patient, visit and product review

## Observed business-flow study

Reservation links patient/visit, room and operation products, with status history. Save creates/edits CPOE operation order, copies product category display data and calls VM according to reservation configuration. Product-specialty/anesthesia/duration/room setup influences the cycle. Cancellation and performed-operation financial behavior are not a generic reservation delete.

Evidence: ReservationManagerFactory.SaveReservation187-285; reservation12/operation14 sample; prior module findings.

Read samples-bundle.json (schema OR) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema OR) for captured lookup/configuration keys (where present), and sql-objects/OR.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ActionsAllowedStatusConfig | No exact anchor-name candidate | configuration name | none named EntityID | 2/0 |
| ActionStatusConfig | No exact anchor-name candidate | configuration name | none named EntityID | 2/0 |
| AdmissionNeedAnesthesiaAssistant | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionNeedAnesthesiologist | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionNeedCirculatingNurse | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionNeedDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 7/1 |
| AdmissionNeedOperation | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| AdmissionNeedScrubNurse | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionNeedSurgeon | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionNeedSurgeonAssist | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Configurations | No exact anchor-name candidate | configuration name | none named EntityID | 0/0 |
| HospitalStructure | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| OperationNurse | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| OperationPhysicians | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| ProductSpeciality | product: ProductID | Review ownership | EntityID | 1/0 |
| QualifierMappedServicesConfig | product: ServiceID | configuration name | EntityID | 2/0 |
| Reservation | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 6/2 |
| ReservationOperation | product: ProductId | Review ownership | EntityID | 8/10 |
| ReservationStatusHistory | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| SKLP_Action | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| SKLP_AnesthesiaType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| SKLP_DurationUnit | No exact anchor-name candidate | Review ownership | none named EntityID | 0/4 |
| SKLP_MappedServiceType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SKLP_NurseType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SKLP_PhysicianType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SKLP_QualifierType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| SKLP_Severity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SKLP_Status | No exact anchor-name candidate | Review ownership | none named EntityID | 0/4 |
| SLKP_AdmissionNeedOperationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ASAScore | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_CancelReservationReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_EmergencyLevel | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PostOperativeCare | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Priority | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/OR.json (one level above this folder) for full columns, indexes, defaults and FK mappings.