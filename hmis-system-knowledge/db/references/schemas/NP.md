# NP: patient, visit and product review

## Observed business-flow study

Nursing order/dispensed-item/perform records connect order instances, product/UOM, visit, service and optional warehouse. The reviewed perform path compares total performed versus requested/charged quantities, dispensed origin and service-kit presence to decide VM charging or local perform-only. Bed accommodation/milk/OR/discharge records are separate subcycles, not all children of one perform transaction.

Evidence: ProcedureTransactionsManagerFactory.PerformProcedureInstance272-369; module-source-findings.md; IPD dispensed-item/service cohort.

Read samples-bundle.json (schema NP) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema NP) for captured lookup/configuration keys (where present), and sql-objects/NP.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BedStatusAccommodation | visit: VisitID | Review ownership | EntityID | 2/0 |
| ConfirmPatientPreMedication | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DismissTransaction | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| DispensedItem | visit: VisitID; product: ProductID | Review ownership | EntityID | 1/1 |
| DispensedItemActionHistory | visit: VisitID; product: ProductID | Review ownership | EntityID | 1/0 |
| Fridges | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| LKP_Reason | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| MilkUnits | patient: PatientID | Review ownership | EntityID | 4/0 |
| NP_Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| NurseConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| NurseOrderLineInstance | visit: VisitID; product: ProductID | Review ownership | EntityID | 0/0 |
| NurseStationEmployeeAssignment | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| NurseStationWarehouseAssignment | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| ORTransaction | visit: VisitID | Review ownership | EntityID | 2/0 |
| PerformServiceKitItem | product: ProductID | Review ownership | EntityID | 1/0 |
| PerformTransaction | product: ProductID | Review ownership | EntityID | 0/1 |
| PhysicalDischargeConfirmation | visit: VisitID | Review ownership | EntityID | 0/0 |
| Reason | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| ReasonCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ServiceKitItem | product: ProductID | Review ownership | EntityID | 1/0 |
| SLKP_AdminstrativeOverrideReasons | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_AllowedAdministrationTime | No exact anchor-name candidate | static lookup name | EntityID | 1/0 |
| SLKP_CancellationDispenseReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_CPOEOrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DispensedItemTransactionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DoseAction | No exact anchor-name candidate | static lookup name | none named EntityID | 1/0 |
| SLKP_DoseActionReason | No exact anchor-name candidate | static lookup name | none named EntityID | 1/0 |
| SLKP_DoseReasonClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_DoseStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_IPDPatientStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MedicationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MilkUnitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ORActionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_OrderLineInstanceStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderLineStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderTypeConfig | No exact anchor-name candidate | static lookup name | EntityID | 0/0 |
| SLKP_ORReservationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_StorageState | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Urgency | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_VisitServiceClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_VisitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_VolumeUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| UnitIntegrity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| VisualInspection | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/NP.json (one level above this folder) for full columns, indexes, defaults and FK mappings.