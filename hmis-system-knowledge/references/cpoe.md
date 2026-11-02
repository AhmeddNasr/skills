# CPOE / Order Entry

Orders of every kind (medication, laboratory, medical imaging, procedure, package) are placed through CPOE Order Entry, so Lab, Rad and Pharmacy stories often need this file too. General configuration patterns live in `general.md`; this file holds only CPOE-specific keys and tables.

## Terminology

- **CPG** (clinical practice guideline) and **treatment plan** mean the same thing. In stories always call it the **"treatment plan tab"**; don't mention that the two terms are interchangeable. [Confirmed — user, 2026-10-26]
- Order Entry has a **favorite list** (with a product classification filter), an **order set** section, and a **treatment plan** tab. [Confirmed — PBI 32423 / user]
- Navigation used in stories: `Portal › Order Entry`. [Confirmed — PBI 32423]
- The favorite list's product classification filter **mirrors the Order Entry search filter**: the classification selected in search is the one selected in the favorite list. [Confirmed — user, 2026-11-01]
- "Favorite items of a non-allowed classification are hidden under any filter selection" is not a real case — don't write an AC for it. [Confirmed — user, 2026-11-01] Likely because the favorite list only shows items of the one selected classification. [Unconfirmed]

## Configuration table — `CPOE.Configuration` [Confirmed — prelive DB, 2026-10-31]

- Structure and value conventions: see `general.md` § Configuration tables. Example CPOE keys:
  - `ShowFluidInOrderEntryVisitClassifications = "2,4"` (visit classification IDs)
  - `PackageOrderVisitClassifications = "1"`
  - `IncludedMinimumIntervalVisitClassifications = "2,1,3,4"`
  - `CallVMPublishProductClassification = "4,6,5,11"` (product classification IDs)
  - `CallVMCachingOrderlinesForClassification = "1,2,…,11"`
- Some CPOE values are signed Power Automate URLs (`*PoweApp_Link`) — never copy those values anywhere.
- Other CPOE config tables exist: `MinimumIntervalConfiguration`, `PhysicalDischargeConfiguration`, `IsOutstandingStatusesStopClinicalDischargeConfig`, `OutstandingOrderlineStatusesConfiguration`, `AdmissionDrConfigurations`, `CallVisitManagementConfig`, `ReportImagesConfiguration`.

## Product classification lookups [Confirmed — prelive DB, 2026-10-31]

`CPOE.SLKP_ProductClassification` (ID, Name, OrderLineTypeId, NameAr):
1 Medication · 2 Medical Consumable · 3 Medical Service · 4 Procedure · 5 Laboratory · 6 Medical Imaging · 7 Other · 8 Packages · 9 Operations · 10 Blood Products · 11 Microbiology

`CPOE.SLKP_OrderEntryProductClassification` (ID, Name, NameAr, ClientActionName, Order) — the classifications shown in Order Entry, in display order:
1 Laboratory (5) · 2 Medical Imaging (6) · 3 Medication (1) · 4 Procedure (4) · 5 Package (8)

- The favorite list's product classification filter uses these Order Entry classifications, in this display order (so "first in the list" = lowest `Order`). [Confirmed — user, 2026-11-01]
- In stories use the real names: "Laboratory", "Medical Imaging" (not "Radiology"), "Medication", "Procedure", "Package".

## Feature history

### PBI 32423 — Hide favorite list if matching CPG is found [Confirmed — ADO, Done, R12.5 Sprint 4, module Physician Desktop]
- Configuration "Disable Favorite list for CPG", per visit classification.
- When enabled for the visit's classification and a CPG is found for the selected diagnosis: favorite list and order set are hidden, treatment plan tab is activated.
- No CPG found → old behavior (favorite list and order set visible, favorite list active).
- The configuration key was **not** found in prelive `CPOE.Configuration` under a name containing "CPG" or "Favorite" (2026-10-31). Real key name unknown — ask or search code. [Unconfirmed]

### PBI 49468 — Disable favorite list categories instead of favorite list tab if a CPG was found [ADO, New, module CPOE, parent 32422; story applied rev 10, 2026-11-01]
- Builds on 32423: instead of hiding the whole favorite list, a whitelist of product classifications stays visible in the favorite list filter.
- Whitelist is a **single system-wide configuration** that defines how the rule behaves — not per visit classification. [Confirmed — user, 2026-10-31]
- Key: `CPGFavoriteListProductClassifications` in `CPOE.Configuration` (name proposed in the story; developers may rename). Value = comma-separated `CPOE.SLKP_ProductClassification` IDs, e.g. `"1,4"`. [Confirmed — user, 2026-11-01]
- Empty value **or missing key** → favorite list hidden entirely (same as 32423). IDs → favorite list shown, filter limited to those classifications. Treatment plan tab is activated in both cases. [Confirmed — user, 2026-11-01]
- Order set stays hidden when a CPG is found, as in 32423; the story doesn't mention it. [Confirmed — user, 2026-11-01]
- If the classification mirrored from the search filter is not in the whitelist, the favorite list filter selects the first classification in its list and ignores the search filter. [Confirmed — user, 2026-11-01]

## Medication favorites / order set lines — tables [Confirmed — prelive + devtest DB, 2026-11-01]

- Favorites and order sets share `CPOE.OrderSet` (`IsFavorite` bit) and `CPOE.MedicationOrderSetLine` (`TradeId`, `TradeNameEn/Ar`, `TradeCode`, `RouteOfAdministrationId`, `DosageFormId`, `UrgencyId`, `IsTaperDose`, `AllowAlternatives`, `IsFluid`, `ParentFluidID`, `IsMainAdditive`, `IsHomeMedication`, `IsChronic`, `SFDACode`, `AdministrationNotes`, `ModifiedTS`). No generic columns (`OrderingMethodId`, `DisplayName`, clinical form IDs) on it yet.
- Dose details: `CPOE.MedicationOrderSetLineDetails` — quantity + UOM, `FrequencyEvery/UnitId`, `DurationFor/DurationDayId`, `MaxDosePerDay`, `MinVarianceTime*`, `InfusionDuration`, `InfusionDurationUnitId`, `InfusionRate`, `IsStrengthBased`. Infusion duration is already saved for favorites.
- Orders: `CPOE.MedicationOrderLine` (devtest) already has `OrderingMethodId`, `DisplayName`, `GenericOrderLineId`; `CPOE.MedicationOrderLineDetails` has the same infusion columns. No "given over time" / administration type column on order lines.
- Administration type lookup `PMGT.SLKP_AdministrationType`: 1 Once · 2 Over time · 3 Diluent. Per clinical form in `PMGT.ClinicalFormAdministrationType` (`ClinicalFormID`, `AdministrationTypeID`, `IsActive`, `IsDeleted`). "Supports type 1 and 2" = the form has both Once and Over time active.

### PBI 49885 — Favorite list - Generic Medications [ADO, New, module CPOE]
- Rev 10 (2026-11-01): rewritten as favorites only, title renamed from "Favorite list & Order sets - Generic Medications". 15 ACs, 3 MSGs. **Never mention order sets in this story** (search, add, public/assigned, previous order sets): the user wants it written as if they do not exist. The only allowed trace is the storage names (`CPOE.OrderSet` with `IsFavorite = 1`, `CPOE.MedicationOrderSetLine`, `OrderSetId` / `MedicationOrderSetLineId`), described as favorite storage. BVC stays Compliance & Risk, BIV "-". [Confirmed — user, 2026-11-01]
- User (2026-11-01): a favorite must save display name, a **list of trade IDs**, the entered dose incl. infusion duration, and whether the physician chose "given over time" (only when the product supports administration types 1 and 2) — all on "Add to favorites". Ordering from a favorite sends the saved product ID(s) to the Supply Chain "select product and get clinical form setup" API. [Confirmed — user, 2026-11-01]

## Order storage and statuses (verified prelive, 2026-11-01)

- `CPOE.Orders`: one row per order line for Lab (classification 5), Medical Imaging (6), Microbiology (11), Procedure (4), Packages (8), Medical Consumable (2). Columns: `ID`, `VisitId`, `PatientId`, `StartDate`, `CreatedDate`, `ProductId`, `ProductNameEn/Ar`, `ProductClassificationId`, `StatusId`, `ResultTypeId`, `PhysicianNameEn`, `IsUrgent`, `ParentId`. No `EndDate`. [Confirmed — prelive DB]
- `CPOE.OrderLine` / `CPOE."Order"` hold administrative lines only (discharge, admission, clinical transfer, referral, consultation, blood bank). The prelive query parser rejects `CPOE.[Order]` — write `CPOE."Order"`. `Order.OrderDate` = `OrderLine.StartDate`; `CreatedDate` is the save time. [Confirmed — prelive DB]
- Blood (transfusion) orders: `CPOE.TransfusionOrderLine.TransfusionOrderLineId` = `OrderLine.OrderLineId`, with `ProductClassificationId` 10 and `OrderLineTypeId` 14, plus `CPOE.TransfusionSpecificRequirements`, `TransfusionRelatedLabOrders`, `TransfusionOrderWitnessEvents` and `AdmissionBloodNeeds`. Full details are in `blood-bank.md`. [Confirmed — prelive DB, 2026-11-02]
- `CPOE.SLKP_OrderLineStatus` (`OrderLineStatusId`, `OrderStatusNameEn/Ar`, `Color`): 1 Ordered `#7a7a7a`, 2 Discontinued `#fd0004`, 3 InProgress `#fbad31`, 4 Complete `#3db3a3`, 5 Dismissed `#fd0004`, 6 Altered, 7 Started, 8 Stopped. `CPOE.SLKP_OrderStatus` has 1–5 with the same names. `CPOE.Orders` uses 1–4 only. [Confirmed — prelive DB]
- `CPOE.SLKP_ResultType`: 1 Provisional, 2 Final, 3 Both (`CPOE.Orders.ResultTypeId`). "Final complete result" = `StatusId = 4` and `ResultTypeId = 2`. [Confirmed — prelive DB]
- Medication: `CPOE.MedicationOrderLine` (`MedicationOrderLineStatusId` → `SLKP_OrderLineStatus`, uses 1–5; `EndDate` datetime2, empty when there is no `CPOE.MedicationOrderLineDetails` row — ~45% of IPD lines in 2026; `TradeNameEn/Ar`, `CreatedDate`, `StartDate`, `IsHomeMedication` (all OPD lines, ~18% of IPD), `IsFluid`, `VisitClassificationId`). [Confirmed — prelive DB]
- Active medication logic (user, 2026-11-01): not Complete, not Discontinued, not Dismissed, and `EndDate` + 24 hours not in the past. ADO Feature 46876 "Active medication list" has empty child PBIs (46879, 46881, 46882). [Confirmed — user + ADO]
- Consultation: `CPOE.ConsultationOrderLine` (`ConsultationLineId` = `OrderLine.OrderLineId`, `ConsultationSpecialtyFrom/ToID` + names, `ConsultationDrFrom/ToID` + names, `ReasonID`, `UrgencyID`, `VisitClassificationID`). Referral: `CPOE.ReferralOrderLine` (`ReferralTypeId` → `CPOE.SLKP_ReferralType` 1 Internal / 2 Cross (ArName holds English), `ReferralSpecialtyFrom/ToID` → `CPOE.Speciality`, `ReferralDrFrom/ToID` + names — to-doctor NULL in ~54%). Referrals use only Ordered/Complete/Discontinued. `CPOE.SLKP_OrderLineType` 13 Referral, 16 Consultation, 18 CrossReferral. [Confirmed — prelive DB]
- PBI 49454 "Referral/consultation widget" (CPOE, New, Feature 4707 "Patient Summary"): one widget with Consultations/Referrals tabs, read-only, "No records to display" / "لا توجد سجلات للعرض". For the new summary it is split into two widgets with no switch (51357, 51358). [Confirmed — ADO + user]
