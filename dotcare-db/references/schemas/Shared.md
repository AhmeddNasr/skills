# Shared: patient, visit and product review

## Observed business-flow study

Shared static vocabulary/configuration and cross-module repository views provide contracts for visit/order/product/billing consumers. Shared SLKP classifications are application enums, not independently generated IDs per import. Repository views do not imply duplicated writable tables. Entity-specific operational filtering still depends on the consuming writer/repository.

Evidence: Static vocabularies; Shared DAL source view repository inventory; SQL dependency catalog.

Read samples-bundle.json (schema Shared) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Shared) for captured lookup/configuration keys (where present), and sql-objects/Shared.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CISConfigurations | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| SLKP_ApprovalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BarcodeRole | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_BillingEngineStatusCode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_BMI_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ContactType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ContractorNationality | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ContractType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_CoverLetterType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_CPGCategories | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Currency | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Day | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Device | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_EpisodeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_FrequencyUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_GateWay | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_MedicationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OperationClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_OrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PriceListCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PricingType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ProductClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ProductContractorErrorMessage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ProductContractorType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_QualifierType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_SuspendType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Time | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TimeUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_VisitClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 1/0 |
| SLKP_VisitClassificationCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_VisitType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Shared.json (one level above this folder) for full columns, indexes, defaults and FK mappings.