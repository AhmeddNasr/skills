# Nphies: patient, visit and product review

## Observed business-flow study

KSA-specific authorization/claim/communication/reconciliation owns request-response transactions and historical item/attachment snapshots. Reviewed claim logging copies patient/contract/visit context and item OrderLineId, ServiceId and ProductId and stores bundle file references. Cancellation sends external tasks, logs errors and updates visit NPHIES status; local deletion is not cancellation of the payer request. External acknowledgement was not executed/tested.

Evidence: ClaimRequestFactory.LogClaimRequest180-257; CancelClaimFactory.CancelClaimRequest146-270; safe claim/cohort samples.

Read samples-bundle.json (schema Nphies) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Nphies) for captured lookup/configuration keys (where present), and sql-objects/Nphies.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __EFMigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AdmissionContractor | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| ApprovalItem | product: ServiceId | Review ownership | EntityID | 3/0 |
| ApprovalTransaction | patient: PatientCode, PatientId; visit: VisitId | Review ownership | EntityID | 8/10 |
| ApprovalTransactionError | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| Attachment | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| AutomaticApprovalRequestLog | visit: VisitId | Review ownership | none named EntityID | 1/0 |
| ClaimItem | product: ServiceId | Review ownership | EntityID | 3/1 |
| ClaimItemResponse | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| ClaimLocationSetups | No exact anchor-name candidate | Review ownership | EntityId | 4/0 |
| ClaimResponseErrorsLog | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ClaimTransaction | patient: PatientId; visit: VisitId | Review ownership | EntityID | 2/9 |
| ClaimTypeConfiguration | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| CodeableConceptDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 1/6 |
| CodeableConceptMasters | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| CommunicationTransaction | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| CorrectiveDiagnosis | visit: VisitId | Review ownership | none named EntityID | 0/0 |
| DischargeDispositionConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| DrgCode | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| EligibilityTransaction | patient: PatientId; visit: VisitID | Review ownership | EntityID | 0/0 |
| ExternalResponses | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LKP_Locations | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| LogAutomatedApprovalJob | No exact anchor-name candidate | Review ownership | none named EntityID | 1/3 |
| LogAutomatedApprovalJobError | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| LogAutomatedApprovalJobTransactionDetail | visit: VisitId | Review ownership | none named EntityID | 2/0 |
| LogAutomatedClaimJob | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| LogAutomatedClaimJobError | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| LogAutomatedPollRequest | No exact anchor-name candidate | Review ownership | none named EntityID | 3/1 |
| LogAutomatedPollRequestError | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| NPHIESCategory | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| NphiesConfiguration | No exact anchor-name candidate | configuration name | none named EntityID | 0/0 |
| NPHIESProductCode | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| NphiesResponseCodes | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Payer | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PaymentNoticeTransaction | No exact anchor-name candidate | Review ownership | EntityID | 4/1 |
| PaymentReconciliationDetail | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| PaymentReconciliationTransaction | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| ProductStandardCode | product: ProductID | Review ownership | EntityID | 1/0 |
| Profile | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ProfileDetail | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| SendClaimRequestConfigurations | No exact anchor-name candidate | configuration name | none named EntityID | 0/0 |
| SeparateRequestConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| SLKP_ApprovalItemType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ApprovalTransaction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ApprovalTransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AttachmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AttachmentUploadType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimItemStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ClaimOutcome | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimSubType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimTransaction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_CommunicationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentNoticeStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RejectionReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TaskJopStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_ToothSurfaceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VMStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| TaskTransaction | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Nphies.json (one level above this folder) for full columns, indexes, defaults and FK mappings.