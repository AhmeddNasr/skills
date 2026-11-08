# HMIS — Pharmacy

Dispensing, returns, RASD (SFDA track and trace), product serial / batch tracking. Supply-chain tables (`SC`, `PMGT`) hold stock and serial data; general configuration patterns live in `general.md`.

## Don't repeat (past corrections — always read this section)

- 2026-11-03 — [Pharmacy] Assumed: PBI 53834 changes the top Barcode field to read the 2D code (BN → batch, SN → Serial No.), has a separate required/optional configuration, and covers returns. → Actually: one configuration (on = mandatory Serial No. input, off = none); the 2D code is read into the Serial No. input and only `(21)` SN is kept; no returns, no scanning changes — never mention scanning in that story. (PBI 53834)
- 2026-11-03 — [Pharmacy] Assumed: with one row per scanned serial, scanning the same serial again (no duplicate check) adds another row. → Actually: a repeated serial adds to that row's Qty like scanning does today; only a new serial adds a row. (PBI 53834)

## Screens and navigation

- Dispense: `Pharmacy › Dispense Transactions › IPD / OPD` opens a dispense pop-up titled "Add Item" (patient banner with visit and room). It has Barcode / Search entry, a grid grouped by "Ordered By" with columns Ordered Qty, Calculated Qty, Qty, Own Med, UOM, Warehouse, Location, Batch, Price, P-Share, I-Share, Avail Qty, On Hand Qty, Actions, a Calculate Price button, and Cancel / Charge / Charge & Dispense buttons. [Confirmed — user screenshot, 2026-11-03, PBI 53834]
- Returns: `Pharmacy › Dispense History › Cancel Service` (whole service) or `Pharmacy › Dispense History › Bulk Action › Returns` (all or part of the quantity). [Confirmed — user, 2026-11-03, PBI 53834]

## Tables (prelive)

- There is no `Pharmacy` schema. Pharmacy-related tables seen: `VisitMgt.PharmacyOrderActionLog`, `VisitMgt.SLKP_PharmacyConfirmStatus`, `VisitMgt.DispensedItemsOfservice`, reports views `reports.VW_VM_ViewPharmcyReturn`, `reports.VM_View_PharmacySalesReport`. [Confirmed — prelive DB, 2026-11-03]
- Which table stores a pharmacy dispense line is not confirmed. [Unconfirmed — not traced in code]
- `VisitMgt.DispensedItemsOfservice`: per-service dispensed items with `Barcode`, `BatchExpiryDate`, product, unit, `Quantity`, warehouse, location, `ServiceTransactionID`. No serial column. [Confirmed — prelive DB, 2026-11-03]
- `NP.DispensedItem` (+ `NP.DispensedItemActionHistory` with `TransactionStatusID`, `TransactionQty`) has `BatchNumber`, `OrderLineID`, `ServiceTransactionID`, `IsCreatedByNurse`, `DeletionReasonID`; no serial column. Status lookup `NP.SLKP_DispensedItemTransactionStatus`: 1 Dispensed, 2 Returned, 3 Deleted. [Confirmed — prelive DB, 2026-11-03]
- Cancel reasons: `NP.SLKP_CancellationDispenseReason`. [Confirmed — prelive DB, 2026-11-03]

## Serial numbers, GTIN and tracking

- Serials already exist on the supply-chain side: `SC.ProductBarcode.SerialNo` (with `BatchNo`, `LotNo`, `ExpiryDate`, `Barcode`), `SC.GoodsReceiptProductDetail.SerialNo`, `PMGT.ProductReceipt.SerialNumber`, `SC.ItemsTrackingLog.SerialNoOld/SerialNoNew`, `Shared.VW_SC_ProductDispense.SerialNo` (by `ServiceTransactionID`, warehouse, location, batch). [Confirmed — prelive DB, 2026-11-03]
- `SC.BarcodeConfiguration.DisplaySerialNumber` (bit) exists. [Confirmed — prelive DB, 2026-11-03]
- Product tracking methods `SC.SLKP_TrackingMethod`: 1 Serial Number, 2 Batch Number, 3 Batch Number & Expiry Date, 4 No Tracking, 5 Serial, Batch & Expiry Date. [Confirmed — prelive DB, 2026-11-03]
- GTIN: `SC.Product.GTINCode`, `SC.Product.IsUnlistedGTIN`; also `Nphies.VW_Product.GTINCode`. [Confirmed — prelive DB, 2026-11-03]

## RASD

- No RASD table or column exists in prelive as of 2026-11-03. [Confirmed — prelive DB search on `%Rasd%`]
- Feature 53833 "RASD" (Module Pharmacy, Compliance & Risk, Critical) is the parent area; PBI 53834 adds a configurable mandatory Serial No. input to the dispense pop-up and sends the serial in the RASD dispense notification. [Confirmed — ADO, 2026-11-03]
- RASD notifications are sent on dispensing and on returning a product. [Confirmed — user, 2026-11-03]

## Configuration

- Configuration tables in `NP`: `NP.NP_Configuration`, `NP.NurseConfiguration`. Which table pharmacy configurations use is not confirmed. [Unconfirmed — not queried]

## Serial No. on dispensing — PBI 53834 (final scope, 2026-11-03)

- One pharmacy configuration: on = a mandatory Serial No. input on each item line of the dispense pop-up; off = no Serial No. input. On own medication (Own Med) lines the Serial No. input is disabled and not mandatory. There is no separate required/optional configuration. [Confirmed — user, 2026-11-03, PBI 53834]
- When the pack's GS1 2D barcode (DataMatrix: `(01)` GTIN, `(21)` SN, `(17)` XD expiry YYMMDD, `(10)` BN batch) is read into the Serial No. input, the system extracts `(21)` SN and keeps only it in the field. [Confirmed — user, 2026-11-03, PBI 53834]
- The serial is sent to RASD on dispensing in a new RASD contract parameter `serialNumber` (type string). Returns, the top Barcode field and batch handling are out of scope for 53834; the user asked that the story never mention scanning or returns. [Confirmed — user, 2026-11-03, PBI 53834]
- Earlier drafts (Barcode field reading the 2D code, BN feeding the batch, one row per serial, serial picking on returns) were dropped by the business. [Confirmed — user, 2026-11-03, PBI 53834]
- Medical consumable lines show a dash (-) instead of the Serial No. input and are not mandatory. Medical consumables = `Shared.SLKP_ProductClassification` ID 2 "Medical Consumables" (1 Medication, 3 Medical Services, 4 Procedures, 5 LAB, 6 RAD, 7 Other, 8 Packages, 9 Operations, 10 Blood Products, 11 Microbiology, 12 Offers). [Confirmed — user + prelive DB, 2026-11-03, PBI 53834]
- Also agreed for 53834: the serial can be typed by hand; one serial per item line with no Qty rule; nothing specified for input without `(21)`; with the configuration off the RASD notification is sent as today. [Confirmed — user, 2026-11-03, PBI 53834]

## 2D barcode scanning — PBI 54731 (under feature 53833, 2026-11-05)

- When the 53834 serial configuration is on and the dispense pop-up's Barcode radio is selected, a "Barcode Type" dropdown appears next to the Barcode field: 2D Barcode (default, GS1 DataMatrix) and 1D Barcode (today's line barcode, unchanged). Not shown with Search. [Confirmed — user, 2026-11-05, PBI 54731]
- 2D scan: `(10)` BN goes to a new Supply Chain API that returns the product details; the batch (with its warehouse/location) is assigned to the first eligible order (same product, quantity left); `(21)` SN goes to that row's Serial No. GTIN and expiry are ignored. [Confirmed — user, 2026-11-05, PBI 54731]
- No eligible order → the product is added as an order by pharmacist, as today. The only error is MSG-01 "Invalid barcode", shown for a code without BN/SN or a batch the API doesn't know. [Confirmed — user, 2026-11-05, PBI 54731]
- Each new serial for the same order duplicates the row (Qty 1, same or different batch) but dispenses on the same order line; RASD gets one `serialNumber` per row. A repeated serial adds Qty to its row. [Confirmed — user, 2026-11-05, PBI 54731]
- Story split: 53834 = configuration + mandatory Serial No. input (no scanning wording); 54731 = all scanning behavior. [Confirmed — user, 2026-11-05]
