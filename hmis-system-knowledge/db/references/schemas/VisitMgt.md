# VisitMgt: patient, visit and product review

## Observed business-flow study

Visit classification dispatch, visit details, service/order caches, billing/tax, package assignment/consumption, accommodation, financial state and invoice synchronization are distinct but connected cycles. Patient/product/physician masters are referenced, while extensions/history and service effects need owned-record tracing. OPD/IPD/AMB/ER plus virtual ER and package behavior differ.

Evidence: visit-evidence-study.md, core-flows.md, 120-query cohort, original package/service evidence.

Read samples-bundle.json (schema VisitMgt) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema VisitMgt) for captured lookup/configuration keys (where present), and sql-objects/VisitMgt.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AdmissionCompanion | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| AdmissionDiagnosis | visit: VisitID | Review ownership | EntityID | 1/0 |
| AdmittedDoctorLog | visit: VisitID | Review ownership | EntityID | 0/0 |
| AmbulatoryVisitDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| AppoinementRule | No exact anchor-name candidate | Review ownership | EntityID | 1/5 |
| AppoinmentRuleException | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ApprovalLetterStatusLog | visit: VisitID | Review ownership | EntityID | 5/0 |
| AppRuleDetail | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| AutomaticVisitServiceConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| BulkRePriceLogs | visit: VisitID | Review ownership | none named EntityID | 1/0 |
| CachedPateintVisits | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CashedOrderLine | visit: VisitID; product: ProductID | Review ownership | EntityID | 5/1 |
| CashPointAssignment | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ChangeContractRequest | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| ChangeContractRequestLog | visit: VisitID | Review ownership | EntityID | 1/0 |
| ClaimJobErrorLogs | visit: VisitId | Review ownership | EntityID | 1/0 |
| ClaimJobLog | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| ContractorSplitConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ContractorStatement | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| CoverLetterApprovalDurations | visit: VisitID | Review ownership | EntityID | 0/0 |
| DeletedApprovalLetterStatusLog | visit: VisitID | Review ownership | EntityID | 0/0 |
| DeletedCashedOrderLine | visit: VisitID; product: ProductID | Review ownership | EntityID | 0/0 |
| DentalChartNotationMapping | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DentalServices | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| DiscountDetail | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| DiscountRule | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| DiscountRuleDetails | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| DiscountRuleProductCategoryDetails | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| DiscountTransaction | visit: VisitID | Review ownership | EntityID | 3/1 |
| DiscountUserProductCategoryRuleDetails | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| DiscountUserRule | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| DiscountUserRuleDetails | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| DispensedItemsOfservice | product: ProductID | Review ownership | EntityID | 2/0 |
| DoctorProcedure | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| EmergencyVisitLinks | visit: VisitID | Review ownership | EntityID | 3/0 |
| EntityRuleAssignment | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Eposide | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| ExtensionOrder | visit: VisitId | Review ownership | EntityID | 3/0 |
| FinancialPercentageConfigurations | product: ProductID | configuration name | none named EntityID | 3/0 |
| InsuranceCardAttachment | patient: PatientID; visit: VisitID | Review ownership | EntityID | 1/0 |
| InvoiceSyncErrolLog | visit: VisitID | Review ownership | EntityID | 2/0 |
| InvoiceSynchronizationLog | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| IPDAdmissionNote | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| IPDRuledMappedService | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ItemsOfService | product: ProductID | Review ownership | EntityID | 0/1 |
| ItemsOfServiceItems | product: ProductID | Review ownership | EntityID | 1/0 |
| Journal | No exact anchor-name candidate | Review ownership | EntityID | 1/3 |
| LKP_AdmissionSource | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| LKP_DosageFrequancy | No exact anchor-name candidate | editable lookup name | none named EntityID | 1/1 |
| LKP_DosageRepeateUnit | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| LKP_ExtensionReason | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| LKP_Location | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| LKP_ReceiptClass | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| LKP_RelationDegree | No exact anchor-name candidate | editable lookup name | EntityID | 0/2 |
| LKP_StabilityType | No exact anchor-name candidate | editable lookup name | EntityID | 0/0 |
| LKP_VisitAttachementType | No exact anchor-name candidate | editable lookup name | EntityID | 1/1 |
| LKP_VisitReason | No exact anchor-name candidate | editable lookup name | EntityID | 1/4 |
| LKP_VisitSource | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| NphiesClaimResponseError | visit: VisitId | Review ownership | EntityID | 1/0 |
| NurseStationEmployeeAssignment | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| NurseStationWarehouseAssignment | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| OperationPhysician | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| OperationReservation | visit: VisitID | Review ownership | EntityID | 1/1 |
| OperationReservationDetail | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| OwnMedicationTransaction | visit: VisitID | Review ownership | EntityID | 1/2 |
| OwnMedicationWarehouseTransaction | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PartialCancelProcedureLog | visit: VisitID; product: ServiceID | Review ownership | EntityID | 1/0 |
| PatientSourceOfBusiness | patient: PatientID | Review ownership | none named EntityID | 1/0 |
| PaymentTransaction | visit: VisitID | Review ownership | EntityID | 8/1 |
| PharmacyOrderActionLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PhysicianSpecialityRuleAssignment | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| POSOutputLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PrintReceiptLog | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| Receipt | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 3/6 |
| ReceiptConfigField | No exact anchor-name candidate | configuration name | none named EntityID | 1/1 |
| ReceiptDetails | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| ReceiptIVDoses | patient: PatientCode | Review ownership | none named EntityID | 1/0 |
| ReceiptMasterTaxes | visit: VisitID | Review ownership | EntityID | 1/0 |
| ReceiptServiceTax | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ReceiptTemplate | No exact anchor-name candidate | Review ownership | EntityID | 4/4 |
| ReceiptTemplateField | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ReferralOrderLine | patient: PatientID; visit: VisitID | Review ownership | EntityID | 1/0 |
| ReferralPatientNumberLog | visit: VisitID | Review ownership | EntityID | 1/0 |
| RefundReceiptLog | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| SelfPaidTransactions | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| ServiceClassificationConfiguration | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| ServiceDose | product: ServiceID | Review ownership | EntityID | 5/0 |
| ServiceSyncStateLogs | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ServiceTax | visit: VisitID | Review ownership | EntityID | 2/0 |
| ServiceTreatmentType | product: ServiceID | Review ownership | EntityID | 1/0 |
| SetAcceptedQuantityConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| SLKP_ActionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_AddedBy | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ApprovalLetterStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_ApprovalLetterStatus_Ex | No exact anchor-name candidate | static lookup name | none named EntityID | 1/0 |
| SLKP_ApprovalRequestType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_BillingInvalidReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChangeContractRequestStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChangeStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChangeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimJobStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimsBasedType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ClaimSyncStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_CreationSource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Currency | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_DoctorServiceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DosageFrequencyPer | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_FinancialStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_GateWay | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_HRJobCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_InvoiceSyncLogType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_IPDStartTimeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_IVDosageFrequencyPer | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_MappingType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Module | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_OrderApprovalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_OrderFrequencyUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_OrderLineInstanceStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderLineStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderLineType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderUrgency | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ORServiceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PageSize | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentMethod | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_PharmacyConfirmStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PhysicianOperationRole | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReceiptFieldType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReceiptType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReceptionAction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Reports | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReportScopes | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RequestedJobCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RuleAssStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_SelfPaidType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_SendClaimToNphiesStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_ServedBy | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_ServiceNoteType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ServiceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_SourceOfBusiness | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_StatementStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_StatementType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SyncState | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_TransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_TreatmentPlanStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TreatmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TreatmentTypeForTreatingDoctor | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitAction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitClaimStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 1/8 |
| SLKP_VisitClassificationCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_VisitJobType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitNphiesStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_VisitServiceClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_VisitServiceStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_VisitType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_VMConfiguration | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_VMFailAction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| Statement | No exact anchor-name candidate | Review ownership | EntityID | 8/5 |
| StatementCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| StatementStatusLog | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SyncStateLog | visit: VisitID | Review ownership | EntityID | 1/0 |
| UndoData | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| VirtualVisitDetails | visit: VisitID | Review ownership | EntityID | 1/0 |
| VirtualWarehouseItem | visit: VisitID | Review ownership | EntityID | 1/1 |
| Visit | patient: PatientCode, PatientID | Review ownership | EntityID | 17/37 |
| VisitActionLog | visit: VisitID | Review ownership | EntityID | 4/0 |
| VisitAdmission | visit: VisitID | Review ownership | EntityID | 3/1 |
| VisitAdmissionConsent | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 2/0 |
| VisitAdmissionOrder | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 1/1 |
| VisitAllowedAction | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| VisitAppointment | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 4/2 |
| VisitAttatchement | patient: PatientID; visit: VisitID | Review ownership | EntityID | 4/2 |
| VisitChangesLog | visit: VisitID | Review ownership | EntityID | 3/0 |
| VisitClaimsReport | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| VisitClaimsReportScope | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| VisitCompanionAccommodation | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitDiagnosis | visit: VisitID | Review ownership | none named EntityID | 1/0 |
| VisitDischargeOrderDetail | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitEposide | visit: VisitID | Review ownership | EntityID | 3/0 |
| VisitFinincailInfo | visit: VisitID | Review ownership | EntityID | 2/0 |
| VisitJobLog | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| VisitJobLogDetail | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitMasterTax | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitNote | visit: VisitID | Review ownership | EntityID | 2/0 |
| VisitPackagesAssignment | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitPatientAccommodation | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitService | visit: VisitID; product: ServiceID | Review ownership | EntityID | 18/12 |
| VisitServiceAllocatedAmountLog | visit: VisitID; product: ServiceID | Review ownership | EntityID | 0/0 |
| VisitServiceMapping | product: ServiceID | Review ownership | EntityID | 3/0 |
| VisitServiceNote | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VisitServiceOperationReservation | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| VisitServicePerformer | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VisitServiceReportDisplayMapping | product: ServiceID | Review ownership | EntityID | 0/0 |
| VisitServiceReturnDetail | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| VisitServiceServedBy | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VisitServiceTransactionLastSync | product: ServiceID | Review ownership | none named EntityID | 1/0 |
| VisitStatement | visit: VisitId | Review ownership | none named EntityID | 3/0 |
| VisitStatusLog | visit: VisitID | Review ownership | EntityID | 3/0 |
| VisitTreatingPhysicianAssignment | visit: VisitId | Review ownership | EntityID | 2/0 |
| VisitTriageDetail | visit: VisitID | Review ownership | EntityID | 1/0 |
| VisitTypeClassification | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| VMConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| VMConfigurationType | No exact anchor-name candidate | configuration name | none named EntityID | 0/1 |
| VMFailAction | visit: VisitID | Review ownership | none named EntityID | 2/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/VisitMgt.json (one level above this folder) for full columns, indexes, defaults and FK mappings.