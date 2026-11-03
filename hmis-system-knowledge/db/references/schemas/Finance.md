# Finance: patient, visit and product review

## Observed business-flow study

Visit billing feeds invoice/service/tax and payment synchronization; VMPaymentTransaction wrapper attempts payment then visit invoice synchronization, with a suppressed-transaction recovery branch. Journal entry editing is limited to draft/unposted state, validation/fiscal period/account setup drives details, posting writes history and can be automatic for zero-period journals. Reversal mapping swaps debit/credit and retains account/owner/cost center context.

Evidence: VMPaymentTransactionManagerFactory.AddVMPaymentTransaction24-80; JournalEntryManagerFactory.SaveJournalEntry283-386 and ReverseJournalEntryMap732-769; Finance-Integration.md.

Read samples-bundle.json (schema Finance) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Finance) for captured lookup/configuration keys (where present), and sql-objects/Finance.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Account | No exact anchor-name candidate | Review ownership | EntityID | 6/11 |
| AccountAssignment | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| AccountEndingBalance | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| AccruedInvJE | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| AccruedRevenue | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| AccruedRevenueInvoice | patient: PatientID; visit: VisitID | Review ownership | EntityID | 6/2 |
| AccruedRevenueInvoiceTransaction | product: ProductID | Review ownership | EntityID | 2/1 |
| AccruedRevenueMasterTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| AccruedRevenueServiceTransactionTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| AccruedVisitClassification | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| APISecurityConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Bank | No exact anchor-name candidate | Review ownership | EntityID | 2/3 |
| BankAccount | No exact anchor-name candidate | Review ownership | EntityID | 5/3 |
| BankBranch | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| CashFlowSubGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 1/8 |
| CashPoint | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| Cheque | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| Claim | No exact anchor-name candidate | Review ownership | EntityID | 7/13 |
| ClaimContract | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ClaimJournalEntries | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| ClaimLines | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| ClaimLineTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ClaimObjectType | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| ClaimOpenning | No exact anchor-name candidate | Review ownership | EntityID | 1/4 |
| ClaimPaymentAllocation | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| Compnay | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| ContactPerson | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| Contractor | No exact anchor-name candidate | Review ownership | EntityID | 3/6 |
| CostCenter | No exact anchor-name candidate | Review ownership | EntityID | 2/9 |
| DirectPaidSelfPayment | patient: PatientID; visit: VisitID | Review ownership | EntityID | 3/0 |
| DocTypeDetail | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| EffectDetails | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| EInvoiceAPILog | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| EInvoiceConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| EInvoiceGroupLog | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| EInvoiceLine | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| EInvoiceLog | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| EInvoiceStatusLog | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| EInvoiceStatusLogDetail | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ElectronicInvoice | No exact anchor-name candidate | Review ownership | EntityID | 5/2 |
| Employee | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| EntityTypeAccount | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| EntityTypeAssignmentLevel | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ErrorLog | visit: VisitID | Review ownership | EntityID | 1/1 |
| ErrorLogDetails | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ExpensesCash | No exact anchor-name candidate | Review ownership | EntityID | 6/0 |
| FilterClaim | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| FinanceSpeciality | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| FinanceSpecialityMapping | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| FiscalPeriod | No exact anchor-name candidate | Review ownership | EntityID | 4/10 |
| FiscalPeriodHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| FiscalPeriodJournal | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| GeneralConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Invoice | patient: PatientID; visit: VisitID | Review ownership | EntityID | 13/9 |
| InvoiceClaim | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| InvoiceGroup | No exact anchor-name candidate | Review ownership | EntityID | 0/3 |
| InvoiceTransaction | product: ProductID | Review ownership | EntityID | 3/2 |
| InvoiceTransactionPayment | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| JEAccountMonthSummation | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| JEAccountOwnerMonthSummation | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| Journal | No exact anchor-name candidate | Review ownership | EntityID | 3/4 |
| JournalDocType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| JournalEntry | No exact anchor-name candidate | Review ownership | EntityID | 7/18 |
| JournalEntryConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| JournalEntryDetails | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| JournalEntryHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| ManualEntity | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| MasterTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| MemoNote | visit: VisitID | Review ownership | EntityID | 9/3 |
| OpeningBalance | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| OwnerEndingBalance | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| OwnersOpenningBalance | No exact anchor-name candidate | Review ownership | EntityID | 4/3 |
| Patient | No exact anchor-name candidate | Review ownership | EntityID | 3/5 |
| PatientMerge | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| PayableMemo | No exact anchor-name candidate | Review ownership | EntityID | 5/2 |
| Payment | No exact anchor-name candidate | Review ownership | EntityID | 5/11 |
| PaymentBank | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| PaymentCash | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| PaymentCheque | No exact anchor-name candidate | Review ownership | EntityID | 6/1 |
| PaymentCollectCheque | No exact anchor-name candidate | Review ownership | EntityID | 4/1 |
| PaymentTransfer | No exact anchor-name candidate | Review ownership | EntityID | 6/0 |
| PaymentVendorBill | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| PaymentVisitManagement | patient: PatientId; visit: VisitId | Review ownership | EntityID | 3/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 1/4 |
| ProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| ProductEInvoiceLog | product: ProductId | Review ownership | EntityID | 0/0 |
| ProductUOM | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| RecurringJournalEntryRunLog | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| RecurringJournalEntryRunLogErrors | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| RecurringJournalEntryTemplate | No exact anchor-name candidate | Review ownership | EntityID | 7/1 |
| RecurringJournalEntryTemplateDetails | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| RejectedDocument | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| RejectedDocumentDetail | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| RoomGroupCostCenter | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| SalesInvoice | No exact anchor-name candidate | Review ownership | EntityID | 6/5 |
| SalesInvoiceDetail | product: ProductId | Review ownership | EntityID | 5/0 |
| SalesInvoiceOpenning | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| SalesInvoicePaymentAllocation | No exact anchor-name candidate | Review ownership | EntityID | 6/0 |
| ServiceTransactionTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SLKP_AccountNature | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_AccountStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AccountType | No exact anchor-name candidate | static lookup name | none named EntityID | 2/2 |
| SLKP_AllocationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_AssignmentLevel | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BankAccountType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BankStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_BasedType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_CashFlowGroup | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_CashPointStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChequeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_City | No exact anchor-name candidate | static lookup name | none named EntityID | 1/4 |
| SLKP_ClaimDeducation | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ClaimError | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ClaimMemoStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ClaimPaymentStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ClaimStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ContractType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_CostCenterStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Country | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_DiscountMeasuring | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_DocType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_DocTypeTemplate | No exact anchor-name candidate | static lookup name | none named EntityID | 3/1 |
| SLKP_Effect | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_EndType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_EntityType | No exact anchor-name candidate | static lookup name | none named EntityID | 1/19 |
| SLKP_ErrorDocType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ErrorLogMessage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ErrorSource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_FinancialStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_FiscalPeriodConfiguration | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_FiscalPeriodStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_FiscalPeriodType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_FrequencyType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_InvoiceStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_JournalEntryErrorMessage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_JournalEntrySource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_JournalEntryStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_JournalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ManualEntityStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MemoStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MemoType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_OnDay | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_OnMonth | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PayableMemoStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PayableVoucherType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentMethod | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_PaymentOrigin | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentPriority | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentSource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentTerm | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_RecurringJournalEntryTemplateStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReferenceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Region | No exact anchor-name candidate | static lookup name | none named EntityID | 1/2 |
| SLKP_Scope | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SelfPaidType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SubLedgerField | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_SubmittedStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 1/9 |
| SLKP_TaxMeasuring | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_TaxStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TaxType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TimeUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ValidateErrorMessage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_VisitCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_VisitClaimStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 1/2 |
| SLKP_VMPaymentTransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VMPaymentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ZatcaMemoReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ZatcaVATCategoryCode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SplitClaim | No exact anchor-name candidate | Review ownership | EntityID | 2/7 |
| SplitClaimClient | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| SplitClaimContract | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| SplitClaimInvoice | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SplitClaimLoss | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| SplitClaimRevision | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| SplitClaimSubmission | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| Tax | No exact anchor-name candidate | Review ownership | EntityID | 6/14 |
| TempClaim | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| TempClaimInvoice | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| TempClaimLine | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| TempClaimLineTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Test | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| TransferredVisits | visit: VisitID | Review ownership | EntityID | 1/0 |
| UOMCategory | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| Vendor | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| VendorBill | No exact anchor-name candidate | Review ownership | EntityID | 5/5 |
| VendorBillConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| VendorBillDetails | product: ProductID | Review ownership | EntityID | 7/0 |
| VendorBillDiscount | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VendorBillGoodsReceipt | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| VendorBillOpenning | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| VendorBillSummary | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| VendorGroup | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| Visit | patient: PatientId; visit: VisitId | Review ownership | EntityID | 6/1 |
| VMPaymentMethodsMapping | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| ZatcaConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ZatcaLog | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| ZatcaPreparedDocument | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| ZatcaSLKPDetail | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| ZatcaSLKPMaster | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ZatcaSubmittedInvoice | No exact anchor-name candidate | Review ownership | EntityID | 6/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Finance.json (one level above this folder) for full columns, indexes, defaults and FK mappings.