# itreports: patient, visit and product review

## Observed business-flow study

Mixed operational extension/reporting schema, including admissions/consents/communications/AI/report caches. It is not read-only by definition: reviewed custom procedures insert package details and PowerApp admission projections or directly change goods-receipt/visit status. Some procedures hardcode entity/UOM/actor values and are not general migration adapters. Consumer apps, refresh and payload retention must be identified individually.

Evidence: Six visible custom stored procedure definitions; SQL dependency map; all-table safe/presence samples.

Read samples-bundle.json (schema itreports) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema itreports) for captured lookup/configuration keys (where present), and sql-objects/itreports.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| AdmissionNeed | product: ProductId | Review ownership | none named EntityID | 0/0 |
| AdmissionOrders | patient: PatientCode; visit: AdmittedVisit, VisitId | Review ownership | none named EntityID | 0/0 |
| AgentHousing | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| Agents | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| AggregatedCounter | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AiRagChunk | patient: PatientCode; visit: VisitId | Review ownership | none named EntityID | 0/0 |
| AttachmentOncologyTracking | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BillingGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CashAdmissionLastVisit | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CheckoutComments | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| ClaimsBundle | patient: PatientID | Review ownership | none named EntityID | 0/0 |
| Clients | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CodeDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Comments | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| ConsentRecords | visit: visitId | Review ownership | none named EntityID | 0/0 |
| ConsentRecordsActivityLogs | No exact anchor-name candidate | Review ownership | entityId | 0/0 |
| ConsentTypes | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Counter | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CriticalResultLastComponent | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DoctorsTargets | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| dsipaddress | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERAppPresence | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERAppUserProfile | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERCommunication | patient: PatientCode; visit: VisitID | Review ownership | none named EntityID | 0/0 |
| ERConversation | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERFeedback | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERNphiesAlertCursor | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERPushSubscription | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ERWhatsAppSpecialityGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| FileTrackingRequest | patient: PatientCode | Review ownership | none named EntityID | 0/0 |
| FormularyData | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| FormularyPageAcknowledgements | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| GeideaPosTransaction | patient: PatientCode; visit: VisitId | Review ownership | none named EntityID | 0/0 |
| GoodsReceiptAttachment | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| GoodsReceiptChatMessage | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| GoodsReceiptStatusHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| GoodsReceiptVendorStatus | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Hash | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| HospitalVendorMessage | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IitemCompanyPrice | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IntegrationLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| InvoiceSMS | patient: PatientCode | Review ownership | none named EntityID | 0/0 |
| jdc_contract | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Job | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| JobParameter | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| JobQueue | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LabResultUsers | patient: PatientCode | Review ownership | none named EntityID | 0/0 |
| LCDQueue | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| LeakageTable | patient: PatientCode; visit: VisitId; product: ProductID | Review ownership | none named EntityID | 0/0 |
| List | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MedicationDispenseTracking | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| MedicationNotDispensedReason | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| MedicationSalesPrice | product: ProductID | Review ownership | none named EntityID | 0/0 |
| NationalityLanguage | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OperationMigration | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OperationReservation | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OR_Cases | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PanicResultAcknowledge | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| PanicResultRegistration | patient: PatientCode; visit: VisitId | Review ownership | none named EntityID | 0/1 |
| PathologyServiceDetails | patient: PatientCode; visit: VisitID | Review ownership | none named EntityID | 0/0 |
| PatientfILEsCAN | patient: PatientCode; visit: VisitId | Review ownership | none named EntityID | 0/0 |
| PatientPaymentService | visit: VisitId; product: ServiceId | Review ownership | none named EntityID | 1/0 |
| PatientPaymentTransaction | patient: PatientCode, PatientId; visit: VisitId | Review ownership | none named EntityID | 0/1 |
| PatientVitals | patient: PatientId | Review ownership | none named EntityID | 0/0 |
| PaymentSmsLog | visit: VisitId | Review ownership | none named EntityID | 0/0 |
| PortalChatConversation | No exact anchor-name candidate | Review ownership | none named EntityID | 2/1 |
| PortalChatMessage | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| PortalSupportRequest | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PowerApp_Appointment | patient: PatientCode | Review ownership | none named EntityID | 0/0 |
| PowerAppAdmissions | patient: PatientCode; visit: VisitID | Review ownership | none named EntityID | 0/0 |
| prices_2025 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ProblemCardTemp2 | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| ProductCost | product: ProductID | Review ownership | none named EntityID | 1/0 |
| PurchaseRequisition | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PurchaseRequisitionProduct | product: ProductID | Review ownership | none named EntityID | 0/0 |
| ReceptionVisitServiceLastOrder | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ReferralFeedback | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ResponseReasonLookup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Roles | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ScheduleModificationLastException | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Schema | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SentEntWhatsAppOrders | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Server | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Servicesafterclinicaldischargedate | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| Set | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SMS_Logs | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SMSQueue | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| State | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| StoreProducts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SysConfig | No exact anchor-name candidate | configuration name | none named EntityID | 0/0 |
| TelemedicineSendLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| TenderItems | product: ProductID | Review ownership | none named EntityID | 0/0 |
| Tickets | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| Users | No exact anchor-name candidate | Review ownership | none named EntityID | 3/5 |
| VendorPortalUser | No exact anchor-name candidate | Review ownership | none named EntityID | 0/3 |
| VendorProfile | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| VendorProfileDocument | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| VendorProfileDocumentComment | No exact anchor-name candidate | Review ownership | none named EntityID | 2/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/itreports.json (one level above this folder) for full columns, indexes, defaults and FK mappings.