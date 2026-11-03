# Billing: patient, visit and product review

## Observed business-flow study

Product/category/UOM and contractual setup feed service price inquiry. Each visit service has its billing transaction; package sales create purchased snapshots with separate member/header/assignment identities. Tax and contractual state are part of the pricing cycle; payment and invoice synchronization belong to additional flows. Do not refresh purchased terms from current package master setup.

Evidence: visit-evidence-study.md; core-flows.md; Product-Drug-Integration.md.

Read samples-bundle.json (schema Billing) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Billing) for captured lookup/configuration keys (where present), and sql-objects/Billing.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AlRajhiPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AXAPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BarcodeConfiguration | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| BeneficiaryType | No exact anchor-name candidate | Review ownership | EntityID | 1/4 |
| BillingConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| BillingGroup | No exact anchor-name candidate | Review ownership | EntityID | 2/13 |
| BupaPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CashPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 3/0 |
| Contract | No exact anchor-name candidate | Review ownership | EntityID | 7/10 |
| ContractAttachment | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ContractBeneficiaryType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ContractCategory | No exact anchor-name candidate | Review ownership | EntityID | 1/4 |
| ContractClient | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ContractDetail | product: ProductID | Review ownership | EntityID | 4/2 |
| ContractDetailTerm | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| ContractDetailTermQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ContractEpisodeType | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| ContractExcludedDiagnoses | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ContractExcludedProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| Contractor | No exact anchor-name candidate | Review ownership | EntityID | 5/15 |
| ContractorAddress | No exact anchor-name candidate | Review ownership | EntityID | 4/0 |
| ContractorClient | No exact anchor-name candidate | Review ownership | EntityID | 1/6 |
| ContractorClientBranch | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| ContractorContact | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ContractorContactPerson | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| ContractorContactPersonContact | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ContractorGateWayMappings | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ContractorMedication | product: ProductID | Review ownership | EntityID | 3/0 |
| ContractorUnAssignProdCoverTracking | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ContractorVisitValidityPeriod | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CoverLetter | patient: PatientCode, PatientID | Review ownership | EntityID | 7/3 |
| CoverLetterAttachment | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| CoverLetterDetail | product: ProductID | Review ownership | EntityID | 3/3 |
| CoverLetterDetailTerm | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| CoverLetterDetailTermQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| EngineLog | visit: VisitID | Review ownership | EntityID | 0/0 |
| Fix_PT_VisitID | visit: NewVisitID | Review ownership | none named EntityID | 0/0 |
| GlobMedPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| InsuranceCard | patient: PatientID | Review ownership | EntityID | 6/5 |
| InsuranceCardAttachment | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| InsuranceCardDetail | product: ProductID | Review ownership | EntityID | 3/2 |
| InsuranceCardDetailTerm | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| InsuranceCardDetailTermQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| InsuranceCardExcludedProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| InvoiceGroup | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| IslamicBankPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ItemCashPricePlanWithMarkUp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ItemCashPricePlanWithNoMarkUp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LKP_UOMCategory | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| LogContractExpireNotification | No exact anchor-name candidate | Review ownership | EntityId | 0/0 |
| MalathPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MedGulfPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MOHPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NCCIPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OfferAttachment | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| OfferExcludedProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| OfferRole | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| OperationsPackage | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Package | product: ProductID | Review ownership | EntityID | 5/9 |
| PackageDetail | product: ProductID | Review ownership | EntityID | 4/1 |
| PackageDetailTerm | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| PackageDetailTermQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PackageEpisodeType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PackageExcludedProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| PackageSpecility | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PatientOfferExcludedProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| PatientPackage | product: ProductID | Review ownership | EntityID | 7/5 |
| PatientPackageDetail | product: ProductID | Review ownership | EntityID | 4/2 |
| PatientPackageDetailTerm | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| PatientPackageDetailTermQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PatientPackageEpisodeType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PatientPackageExcludedProduct | product: ProductID | Review ownership | none named EntityID | 2/0 |
| PatientPackageSpecility | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PatientTransaction | patient: PatientID; visit: VisitID; product: ProductID | Review ownership | EntityID | 22/4 |
| PatientTransactionDetail | No exact anchor-name candidate | Review ownership | EntityID | 13/0 |
| PatientTransactionTax | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PatientTransactionTaxMaster | visit: VisitID | Review ownership | EntityID | 1/0 |
| PriceList | No exact anchor-name candidate | Review ownership | EntityID | 2/10 |
| PriceListConfiguration | No exact anchor-name candidate | configuration name | EntityID | 3/0 |
| PricePlan | product: ProductID | Review ownership | EntityID | 4/4 |
| PricePlanRangeSet | No exact anchor-name candidate | Review ownership | EntityID | 1/4 |
| PriceRange | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PriceRangeSetQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 8/20 |
| ProductBillingGroups | product: ProductID | Review ownership | EntityID | 3/2 |
| ProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 3/5 |
| ProductContractor | product: ProductID | Review ownership | EntityID | 3/0 |
| ProductContractorCodesConfigurations | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ProductReceipt | product: ProductID | Review ownership | EntityID | 1/0 |
| ProductUOM | No exact anchor-name candidate | Review ownership | EntityID | 1/8 |
| RuleGroup | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| SLKP_BarcodeRole | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_City | No exact anchor-name candidate | static lookup name | none named EntityID | 1/2 |
| SLKP_ContactType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ContractorNationality | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ContractType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Country | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_CoverLetterType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Day | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Device | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_EpisodeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_GateWay | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MedicationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_Nationality | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_OperationClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PaymentTerm | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PriceListCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PricingType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_ProductClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ProductContractorErrorMessage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ProductContractorType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProductType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_QualifierType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/6 |
| SLKP_Region | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/10 |
| SLKP_SuspendType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Time | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TimeUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| SLKP_UOMOperator | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SuspendingSchedule | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| Tax | No exact anchor-name candidate | Review ownership | EntityID | 2/7 |
| TaxAssignedProduct | product: ProductID | Review ownership | EntityID | 4/0 |
| TaxEpisodeType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| TaxExcludedProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| TaxExemptedNationality | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| TCSMainPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| TCSReferralPricePlan | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| UndoData | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| UnitPricePlan | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VisitDiagnosis | visit: VisitID | Review ownership | EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Billing.json (one level above this folder) for full columns, indexes, defaults and FK mappings.