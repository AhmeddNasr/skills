# PMGT: patient, visit and product review

## Observed business-flow study

Classification-specific product/drug projections serve clinical consumers and use category/UOM/reference-unit caches. Core master product setup is shared, while patient consumption belongs to order/service/stock records. Goods-receipt validation publishes product updates to PMGT; delivery/replay consistency is a separate integration check.

Evidence: Product-Drug-Integration.md; original product samples; SC GoodsReceiptRSDNotificationMangerFactory.

Read samples-bundle.json (schema PMGT) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema PMGT) for captured lookup/configuration keys (where present), and sql-objects/PMGT.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| __MigrationHistoryDrug | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| DosageForm | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| DoseAdministration | No exact anchor-name candidate | Review ownership | none named EntityID | 10/0 |
| Drug | No exact anchor-name candidate | Review ownership | EntityID | 8/5 |
| DrugAlternative | product: DrugID | Review ownership | EntityID | 2/0 |
| DrugGeneric | product: DrugID | Review ownership | EntityID | 4/0 |
| DrugRouteOfAdministration | product: DrugID | Review ownership | EntityID | 2/0 |
| DrugUOM | product: DrugID | Review ownership | EntityID | 2/1 |
| GenerecComplexReference | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| Generic | No exact anchor-name candidate | Review ownership | EntityID | 0/8 |
| GenericContraIndication | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| GenericTherapeuticCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| GenericToFoodInteraction | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| GenericToGenericInteraction | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| GenericToPregLactInteraction | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| GenericToTestInteraction | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| InvoiceGroup | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| LKP_UOMCategory | No exact anchor-name candidate | editable lookup name | EntityID | 0/2 |
| LKP_Warehouse | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| MedicineSheet | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MissedDosageUpdates | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MissedIngredientsUpdates | product: DrugID | Review ownership | none named EntityID | 0/0 |
| NonMedicineSheet | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OperationsPackage | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 6/5 |
| ProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 3/3 |
| ProductReceipt | product: ProductID | Review ownership | EntityID | 1/0 |
| ProductUOM | No exact anchor-name candidate | Review ownership | EntityID | 1/7 |
| ROA_Mapping | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SLKP_BodyUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DoseType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DrugInteractionRisk | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DrugNPHIESCode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_MedicationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PregLactRisk | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ProductClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProductType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RouteOfAdministration | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RouteOfAdministrationOLD | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TherapyType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TimeUOM | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_UOM | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_UOMOperator | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| StrengthUnit | No exact anchor-name candidate | Review ownership | EntityID | 0/3 |
| TherapeuticCategory | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| TherapyTypeDosageFromMapping | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| WarehouseCategoryAssignment | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/PMGT.json (one level above this folder) for full columns, indexes, defaults and FK mappings.