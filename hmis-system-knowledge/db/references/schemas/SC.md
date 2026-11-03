# SC: patient, visit and product review

## Observed business-flow study

Product/category/UOM/warehouse/vendor setup feeds procurement, receipt, balances, transfers, dispensing and returns. Reviewed validated receipt updates PO details/status, batch barcodes, location balances in reference UOM, average cost, Finance journal linkage and PMGT events; Saudi RSD is conditional. Active insert triggers generate barcode/code and transfer/return prefixes. Direct row imports must account for generated values and postcommit external effects.

Evidence: GoodsReceiptRSDNotificationMangerFactory.SaveAndValidateGoodsReceipt150-314; live three SC trigger definitions; product integration evidence.

Read samples-bundle.json (schema SC) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema SC) for captured lookup/configuration keys (where present), and sql-objects/SC.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| _LockEntity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| _LockEntityDetail | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| BarcodeConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| BulkMigrationSetup | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| BulkMigrationSetupWarehouse | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| GoodsReceipt | No exact anchor-name candidate | Review ownership | EntityID | 5/2 |
| GoodsReceiptProduct | product: ProductID | Review ownership | EntityID | 5/2 |
| GoodsReceiptProductDetail | No exact anchor-name candidate | Review ownership | EntityID | 5/1 |
| InternalRequest | No exact anchor-name candidate | Review ownership | EntityID | 3/3 |
| InternalRequestDetail | product: ProductID | Review ownership | EntityID | 4/2 |
| InternalTransfer | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| InternalTransferProduct | product: ProductID | Review ownership | EntityID | 3/1 |
| InternalTransferProductDetail | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ItemsTrackingLog | product: ProductID | Review ownership | EntityID | 2/0 |
| LKP_LocationType | No exact anchor-name candidate | editable lookup name | EntityID | 1/3 |
| ManufacturingOrder | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| ManufacturingOrderProduct | product: ProductID | Review ownership | EntityID | 5/1 |
| ManufacturingOrderProductDetail | product: ProductID | Review ownership | EntityID | 6/0 |
| NPHIESCategory | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| NPHIESProductCode | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| OperationsPackage | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 9/24 |
| ProductAverageCost | product: ProductID | Review ownership | EntityID | 2/0 |
| ProductBalance | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| ProductBarcode | product: ProductID | Review ownership | EntityID | 1/13 |
| ProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/5 |
| ProductCharacteristic | product: ProductID | Review ownership | EntityID | 2/0 |
| ProductClassificationEmployee | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| ProductRawMaterial | product: ProductID | Review ownership | EntityID | 3/0 |
| ProductUOM | No exact anchor-name candidate | Review ownership | EntityID | 2/32 |
| PurchaseOrder | No exact anchor-name candidate | Review ownership | EntityID | 5/3 |
| PurchaseOrderDetail | product: ProductID | Review ownership | EntityID | 7/1 |
| PurchaseRequisition | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| PurchaseRequisitionProduct | product: ProductID | Review ownership | EntityID | 4/1 |
| PurchaseRequisitionProductDetail | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| ReceiveDonation | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| ReceiveDonationConsumedProduct | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| ReceiveDonationReceivedProduct | No exact anchor-name candidate | Review ownership | EntityID | 5/0 |
| ReceiveInternalRequest | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| ReceiveInternalRequestProduct | product: ProductID | Review ownership | EntityID | 6/1 |
| ReceiveInternalRequestProductDetail | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| ReturnToVendor | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| ReturnToVendorGoodsReceipt | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| ReturnToVendorProduct | product: ProductID | Review ownership | EntityID | 7/1 |
| ReturnToVendorProductDetail | No exact anchor-name candidate | Review ownership | EntityID | 6/0 |
| ReturnToWarehouse | No exact anchor-name candidate | Review ownership | EntityID | 5/1 |
| RSDNotification | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| RSDNotificationTransaction | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| RSDNotificationTransactionsDetail | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| SLKP_City | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_ContactType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Country | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_DataMigrationTemplateType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_GoodsReceiptStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_InternalRequestStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_Manufacturer | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MOActionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_NotificationContent | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PaymentTerm | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProductCharacteristics | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProductClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ProductType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PurchaseOrderProductStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PurchaseOrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PurchaseRequisitionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReferenceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RSDReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_RSDStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/10 |
| SLKP_RSDTransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_StockCountStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TrackingMethod | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TransferStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_TransferType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Unit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_UomUnitType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_VarianceReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VendorClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_WarehouseClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_WarehouseFreezingType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_WarehouseFunction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| StockCount | No exact anchor-name candidate | Review ownership | EntityID | 4/3 |
| StockCountProductCategory | product: ProductID | Review ownership | EntityID | 4/1 |
| StockCountProductDetail | product: ProductID | Review ownership | EntityID | 7/0 |
| StockCountWarehouseLocation | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SystemConfig | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| TransferIn | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| TransferOut | patient: PatientID; visit: VisitID | Review ownership | EntityID | 6/4 |
| TransferTransactionProduct | product: ProductID | Review ownership | EntityID | 9/1 |
| TransferTransactionProductDetail | No exact anchor-name candidate | Review ownership | EntityID | 10/0 |
| UOMCategory | No exact anchor-name candidate | Review ownership | EntityID | 0/2 |
| Vendor | No exact anchor-name candidate | Review ownership | EntityID | 2/7 |
| VendorAddress | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| VendorBarcode | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| VendorContact | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VendorContactPerson | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| VendorContactPersonContact | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VendorGroup | No exact anchor-name candidate | Review ownership | EntityID | 2/3 |
| Warehouse | No exact anchor-name candidate | Review ownership | EntityID | 3/24 |
| WarehouseCategory | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| WarehouseEmployee | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| WarehouseFunction | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WarehouseLocation | No exact anchor-name candidate | Review ownership | EntityID | 4/16 |
| WarehouseLocationProduct | product: ProductID | Review ownership | EntityID | 2/0 |
| WarehouseLocationProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WarehouseProduct | product: ProductID | Review ownership | EntityID | 3/0 |
| WarehouseProductCategory | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WarehouseRoute | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| WarehouseStructure | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/SC.json (one level above this folder) for full columns, indexes, defaults and FK mappings.