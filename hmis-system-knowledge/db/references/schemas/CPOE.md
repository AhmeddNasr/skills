# CPOE: patient, visit and product review

## Observed business-flow study

Orders connect visits/patients to product classification, accepted quantity and execution instances. OrderlineID links are version/family-dependent. Medication administration, lab/rad investigation, nursing performance and dental execution are downstream writers, with conditional VM charges. Package expansion differs for IPD versus other classifications. Order sets and treatment-plan setup are shared definitions.

Evidence: visit-evidence-study.md; module-source-findings.md; two sampled MedicationOrderSetLine parent misses in fk-sample-evidence.json.

Read samples-bundle.json (schema CPOE) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema CPOE) for captured lookup/configuration keys (where present), and sql-objects/CPOE.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AdministrativeNotes | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| AdmissionBloodNeeds | No exact anchor-name candidate | Review ownership | none named EntityID | 4/0 |
| AdmissionDiagnosis | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionDrConfigurations | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| AdmissionNeed | product: ProductId | Review ownership | EntityID | 5/13 |
| AdmissionNeedAnesthesiaAssistant | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionNeedAnesthesiologist | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionNeedAuthorization | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AdmissionNeedCirculatingNurse | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionNeedDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 8/0 |
| AdmissionNeedOperation | No exact anchor-name candidate | Review ownership | none named EntityID | 2/1 |
| AdmissionNeedScrubNurse | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionNeedSubOperation | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionNeedSurgeon | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionNeedSurgeonAssist | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| AdmissionOrderLine | visit: AdmittedVisit, NewVisitID | Review ownership | EntityID | 6/2 |
| AnesthesiaDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 4/0 |
| AuthorizationData | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| CallVisitManagementConfig | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| ClinicalTransferAllowedStatus | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ClinicalTransferOrderLine | No exact anchor-name candidate | Review ownership | EntityID | 6/1 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ConsultationOrderLine | No exact anchor-name candidate | Review ownership | EntityID | 4/1 |
| ConsultationOrderLineNote | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| DentalOrder | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DentalOrderLine | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DischargeOrderLine | No exact anchor-name candidate | Review ownership | EntityID | 4/1 |
| DiscontinueReasonCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| EntityCurrency | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| FavoriteInstruction | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| FollowUpOrder | patient: PatientId; visit: VisitId | Review ownership | none named EntityID | 1/1 |
| FollowUpOrderClinic | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| Instruction | patient: PatientID; visit: VisitID | Review ownership | EntityID | 3/0 |
| IsOutstandingStatusesStopClinicalDischargeConfig | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| MedicationAuthorizationData | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MedicationOrderLine | patient: PatientCode, PatientId; visit: VisitId | Review ownership | EntityID | 13/12 |
| MedicationOrderLineDetails | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| MedicationOrderLineGenericName | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MedicationOrderLineHistory | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| MedicationOrderLineInstance | visit: VisitId | Review ownership | EntityID | 3/4 |
| MedicationOrderLineInstanceActionHistory | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| MedicationOrderLineInstanceHistory | visit: VisitId | Review ownership | EntityID | 2/1 |
| MedicationOrderLineInstancePreparationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MedicationOrderLineInstanceRescheduleHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MedicationOrderLineTherapeuticCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MedicationOrderSetLine | No exact anchor-name candidate | Review ownership | EntityID | 2/3 |
| MedicationOrderSetLineDetails | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| MedicationOrderSetLineGenericName | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MedicationOrderSetLineTherapeuticCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| MilkOrder | patient: PatientCode, PatientId; visit: VisitId | Review ownership | EntityID | 9/3 |
| MilkOrderHistory | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| MilkOrderInstance | visit: VisitId | Review ownership | EntityID | 3/1 |
| MilkOrderInstanceHistory | visit: VisitId | Review ownership | EntityID | 4/0 |
| MilkOrderInstanceHistoryTempdata | visit: VisitId | Review ownership | EntityID | 0/0 |
| MinimumIntervalConfiguration | product: ProductID | configuration name | EntityID | 1/0 |
| MinimumIntervalOrder | patient: PatientId; visit: VisitId; product: ProductID | Review ownership | none named EntityID | 0/0 |
| NphiesCSRequestTracking | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Order | patient: PatientCode, PatientId; visit: VisitId | Review ownership | EntityID | 6/3 |
| OrderBodySource | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| OrderDiagnosis | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| OrderLine | No exact anchor-name candidate | Review ownership | EntityID | 11/13 |
| OrderLineAuthorizationData | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| OrderLineBodySource | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| OrderLineDetail | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| OrderLineInstance | visit: VisitId | Review ownership | EntityID | 7/3 |
| OrderLineInstanceHistory | visit: VisitId | Review ownership | EntityID | 2/0 |
| OrderOverrideLog | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Orders | patient: PatientCode, PatientId; visit: VisitId; product: ProductId | Review ownership | EntityID | 12/18 |
| OrderSet | No exact anchor-name candidate | Review ownership | EntityID | 0/5 |
| OrderSetDiagnoses | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| OrderSetLine | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| OrderSetLineDetail | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| OrderSetPhysicianAssignments | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| OrderSetSpecialties | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| OutstandingOrderlineStatusesConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| PerformProcedureHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| PerformTransfusion | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| PhysicalDischargeConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| PredefinedInstruction | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| PrintedOrder | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PrintLog | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| ProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| ReasonCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ReferralOrderLine | No exact anchor-name candidate | Review ownership | EntityID | 7/0 |
| RelatedLabOrders | product: ProductId | Review ownership | EntityID | 0/1 |
| ReportImagesConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| SKLP_Currency | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SLKP_AdminstrativeOrderReason | No exact anchor-name candidate | static lookup name | none named EntityID | 1/3 |
| SLKP_AdmissionNeedOperationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AnesthesiaType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ApprovalLetterStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ApprovalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ASAScore | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AssignmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BloodComponent | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_BodySource | No exact anchor-name candidate | static lookup name | EntityID | 0/2 |
| SLKP_CancellationReason | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_CreateMedicationOrderlineOutputStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_CreationOrderModule | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DeliveryMethod | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_DischargeCondition | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DischargeDestination | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DischargeOutCome | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Discontinue_Reason | No exact anchor-name candidate | static lookup name | none named EntityID | 1/3 |
| SLKP_EmergencyLevel | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_FrequencyUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/29 |
| SLKP_IgnoreMaxRadiation | No exact anchor-name candidate | static lookup name | EntityID | 0/0 |
| SLKP_IgnoreMinimumInterval | No exact anchor-name candidate | static lookup name | EntityID | 0/1 |
| SLKP_InstructionReason | No exact anchor-name candidate | static lookup name | EntityID | 0/1 |
| SLKP_InstructionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MedicationDismissReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_MedicationOrderLineQuantitiesNotAllowedReasons | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_MilkType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Need | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_NeedType | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_OrderEntryProductClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderLineInstanceStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_OrderLineSetAuthorizationOutputStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderLineStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_OrderLineType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_OrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/7 |
| SLKP_OverrideReason | No exact anchor-name candidate | static lookup name | none named EntityID | 1/6 |
| SLKP_PostOperativeCare | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_PriceInquiryErrorMessage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Priority | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProductClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 1/7 |
| SLKP_ReferenceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_ReferralType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ResultType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_RouteofAdministration | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Side | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_SpecificRequirements | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_StatusLevel | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TransfusionEditReason | No exact anchor-name candidate | static lookup name | EntityID | 0/1 |
| SLKP_TransfusionReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_TreatmentPlanStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TreatmentPlanStopedReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Urgency | No exact anchor-name candidate | static lookup name | none named EntityID | 0/11 |
| SLKP_UrgencyJustification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| Speciality | No exact anchor-name candidate | Review ownership | none named EntityID | 1/9 |
| SpecialityProduct | product: ProductID | Review ownership | none named EntityID | 2/0 |
| TransfusionOrderEvents | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| TransfusionOrderLine | No exact anchor-name candidate | Review ownership | EntityID | 6/3 |
| TransfusionOrderWitnessEvents | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| TransfusionRelatedLabOrders | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| TransfusionSpecificRequirements | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| TreatmentPlan | patient: PatientId | Review ownership | EntityID | 2/7 |
| TreatmentPlanData | patient: PatientCode; visit: VisitId | Review ownership | none named EntityID | 1/0 |
| TreatmentPlanDiagnosis | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| TreatmentPlanSpecialty | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| TreatmentPlanVisit | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| TreatmentPlanVisitNeed | product: ProductId | Review ownership | EntityID | 5/1 |
| UndoData | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ValidationSchemaColumns | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| ValidationSchemaDetails | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VisitClassificationList | No exact anchor-name candidate | Review ownership | EntityID | 0/9 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/CPOE.json (one level above this folder) for full columns, indexes, defaults and FK mappings.