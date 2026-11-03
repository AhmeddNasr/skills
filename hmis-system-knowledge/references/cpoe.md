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
- Medication urgency: `CPOE.MedicationOrderLine.UrgencyId` → `CPOE.SLKP_Urgency` (`UrgencyNameEn` / `DisplayNameEn`): 1 Routine ("Normal"), 2 STAT ("Urgent"), 3 PRN ("PRN", `IsNotMedication = 0`). In 2026 data, **every STAT and PRN medication line has no `EndDate`**; Routine lines almost always have one (exceptions: ~30k IPD, ~370 ER, 1 OPD). [Confirmed — prelive DB, 2026-11-02]
- Consultation: `CPOE.ConsultationOrderLine` (`ConsultationLineId` = `OrderLine.OrderLineId`, `ConsultationSpecialtyFrom/ToID` + names, `ConsultationDrFrom/ToID` + names, `ReasonID`, `UrgencyID`, `VisitClassificationID`). Referral: `CPOE.ReferralOrderLine` (`ReferralTypeId` → `CPOE.SLKP_ReferralType` 1 Internal / 2 Cross (ArName holds English), `ReferralSpecialtyFrom/ToID` → `CPOE.Speciality`, `ReferralDrFrom/ToID` + names — to-doctor NULL in ~54%). Referrals use only Ordered/Complete/Discontinued. `CPOE.SLKP_OrderLineType` 13 Referral, 16 Consultation, 18 CrossReferral. [Confirmed — prelive DB]
- PBI 49454 "Referral/consultation widget" (CPOE, New, Feature 4707 "Patient Summary"): one widget with Consultations/Referrals tabs, read-only, "No records to display" / "لا توجد سجلات للعرض". For the new summary it is split into two widgets with no switch (51357, 51358). [Confirmed — ADO + user]

## MediSpan drug alerts [2026-11-02]

- MediSpan screening response shape: `Alerts[]` with `Index`, `ApiName` (`Allergy`, `Interaction`, `Multiple`, `Pregnancy`, `Lactation`, `Age`, `Disease`, `Gender`, `Duplication`, `Route`), `Text`, `Summary`, `Importance` (`Very High`, `High`, `Medium`, `Low`, `Very Low`), `Icon.ScreeningType` (`ALG`, `INTD`, `PCI`, `LCI`, `ACI`, `DCI`, `GCI`, `DUP`, `RCI`, `DOS`), `MessageId`, `Monograph` (HTML). Plus aggregate `InlineAlertIcons` / `SummaryAlertIcons`, whose `Importance` is the highest of the alerts they group — so rules must read `Alerts[]`, not the icons. [Confirmed — user-pasted payloads, 2026-11-02]
- "Not Screened - Not Loaded" (`ApiName` `Multiple`, Medium) = a patient diagnosis MediSpan couldn't load; "Not Screened - Content Expired" = MediSpan content past its expiry date. [Confirmed — payloads]
- Calls are logged in `Drug.MediSpanCallLogs` (`RequestTimestamp`, `RequestBody`, `ResponseTimestamp`, `StatusCode`, `ResponseBody`, `ExceptionMessage`, `ExceptionBody`). [Confirmed — prelive DB, 2026-11-02]
- `CPOE.SLKP_OverrideReason` category 1 (IDs 33–41) = drug interaction override reasons (e.g. "Therapeutic benefit outweighs risk", "No safer alternative available"). Whether the Drug Alerts popup uses them is not confirmed — the current popup shows no reason field. [Confirmed lookup — prelive DB; usage Unconfirmed]
- Drug Alerts popup (Order Entry): title "Drug Alerts", heading "Check Drug Interactions Alerts Below", importance legend, columns Type Of Alert / Cause Of Alert / Message, buttons Cancel and Override, X to close. [Confirmed — user screenshot, 2026-11-02]
- ADO: Epic 52813 "Medispan" (CPOE, child 52815). PBI 46857 "Medispan display icons in order popup" (parent Feature 30700 "Order popup"). PBI 52816 "Prevent override if medispan returned a very high allergy alert". Existing MediSpan items have no story text on popup/override behaviour. [Confirmed — ADO, 2026-11-02]
- Rule (PBI 52816): Override is disabled only when an alert has `ApiName = Allergy` AND `Importance = Very High`; every other combination stays overridable. [Confirmed — user, 2026-11-02]
- PBI 52816 applied rev 2 (2026-11-02), parent 52815, ticket 5972, Compliance & Risk / High. Confirmed by user: popup holds alerts for all medications with one Override (one very high allergy blocks the whole popup); Cancel/X close without saving and keep the medication in the order list; note = red banner at top of popup, no medication named; no special row highlight. No server-side override check — user said not applicable. [Confirmed — user, 2026-11-02]

## Active medication logic — PBI 52819 [2026-11-02]

- PBI 52819 "Change active medication logic" (CPOE, parent Feature 46876 "Active medication list"; siblings 46879/46881/46882 empty). Applies to **Portal › Orders › Order entry**, where an "active medications" **checkbox** filters the medication list: checked → only active medications; unchecked → everything. STAT is always hidden when checked; **PRN is active by status only** (no end date, no duration), Routine by status + end date (no +24 h). [Confirmed — user, 2026-11-02]
- The story changes **logic only** (what counts as active and as ending soon); how "ending soon" is displayed is out of scope. Do not mention routine orders without an end date. [Confirmed — user, 2026-11-02]
- Previous rule (51355 Patient summary medication widget, 16611): active = status not Complete/Discontinued/Dismissed AND end date + 24 h not past; IPD-only All/Active/Ended tabs. "Ending soon" is not defined in any ADO item before 52819. [Confirmed — ADO, 2026-11-02]
- PBI 12536: display names swapped — internal Discontinued shows as "Cancelled", internal Dismissed shows as "Discontinued" (patient summary, eMAR, previous orders). [Confirmed — ADO]
- Applied 52819 rev 4 (2026-11-02), 9 ACs, all assumptions confirmed: checkbox label "Active medications" / «الأدوية النشطة» already exists in Order entry; status rule (not Complete/Discontinued/Dismissed) unchanged; ending soon (Routine only, end date within next 24 h) shows only while the checkbox is checked; Order entry only — the Patient summary widget (51355) keeps its own rule. Ticket 6072 (rev 5). [Confirmed — user, 2026-11-02]

## NPHIES CS send tracking — `CPOE.NphiesCSRequestTracking` [Confirmed — prelive DB schema + production export, 2026-11-03]
- One row per send attempt state: `Id`, `OrderId`, `BundleId`, `CompositionId`, `VersionNumber`, `LastStatus` (`Success` / `Failed` / `Skipped`), `LastAttemptDate`, `ErrorMessage`, `PayloadType`, `PhysicianNphiesCode`, `OrderStandardCode`, `VisitStartDate`, `DosageFormCode`, `RouteOfAdministrationCode` (SNOMED, e.g. 26643006 oral, 47625008 IV), `PrescriptionTypeCode` (`U` / `C`), `DispenseQuantityUnit` (e.g. `{tablet}`, `mL`).
- `PayloadType` values (prelive): `OrderEvent`, `OrderEventUpdate`, `LabResult`, `RadReport` (radiology result), `DispenseEvent`, `DischargeSummary`, `MaternalDischargeSummary`, `NewbornDischargeSummary`, `OperativeNotes`. A 4-hour production export (2026-11-03) had only the first three. `RadReport` skip reasons: `No NPHIES license for the reporting radiologist '…'`, `No radiology report text.`, `Not a completed radiology investigation.` [Confirmed — prelive DB, 2026-11-03]
- `LastAttemptDate` is UTC; LR timestamps (`InvestigationHistory.StatusChangingDataTime`, `InvestigationResult.CreatedDate`) are local KSA time (UTC+3). Subtract 3 h before comparing. [Confirmed — prelive data, consistent ~10,795 s offset, 2026-11-03] Medication rows are the ones with `DosageFormCode` filled (FHIR profile `bundlePrescription`); lab orders use `bundleLabOrder` + LOINC codes; rad orders carry NICIP codes (e.g. `XCHSP`). Medication `OrderId`s are in a different number range from lab/rad.
- `ErrorMessage` shapes: plain text for pre-send validation (`Not sent to NPHIES: PatientHealthId must be a positive number.`, `Not sent to NPHIES: PhysicianNphiesCode (ordering physician) is required.`, `No standard code (LOINC / NICIP / generic medication code) found for product.` → `Skipped`); a wrapper JSON `{success,error,message,orderResults,bundleJsons}` for transport errors (e.g. HttpClient 120 s timeout; one wrapper can hold several bundles); or a NPHIES FHIR `OperationOutcome`.
- `LabResult` rows take `PhysicianNphiesCode` from the order's `OrderEvent` tracking row, not from `CPOE.Orders`: in the 2026-11-03 production export all 100 `LabResult` failures ("PhysicianNphiesCode (ordering physician) is required") had no `OrderEvent` row, even though the orders had a physician; all 19 successes had one. 84 of the failures were for orders created before tracking started; 16 were created after it started but never got an `OrderEvent` (one 15-order save on a single visit, plus one cross-match). [Unconfirmed in code — strong pattern in production export, 2026-11-03]
- `CPOE.Orders.CreatedDate` is local time (UTC+3), like the LR tables; an `OrderEvent` is sent ~2 s after the order is created. [Confirmed — production export, 2026-11-03]

## Internal (predicted) approval → Visit Management

- PBI 49432 "[Internal Approval] Apply internal approval results to the visit in Visit Management": CPOE sends the internal approval API's approved items to VM. The internal approval API returns a decision for every order on the visit. [Confirmed — PBI 49432 rev 7]
- Contract (2026-11-03, "CPOE Predicted Approval Contract.docx") replaced `ProcessPendingAuthorizationRequest` (Source 2) with `POST api/Insurance/ProcessPredictedApproval`. Request: `VisitId` + `Items[]` (`OrderLineId` = CPOE order line ID, `ProductClassificationId`, `ApprovalStatusId`). CPOE uses only `ApprovalStatusId` 4 (Approved); stories must not mention any other status or `ApprovedQuantity`. Response: a single `VmErrorCode`; anything but 1 applies nothing; 107 NoItemsToUpdate = all items already decided, not an error. No 106 Concurrency code in this contract. [Confirmed — contract doc, 2026-11-03]
- 49432 behaviour agreed with the user (rev 10): CPOE sends only items with an "Approved" decision, always with status 4; it does **not** filter lines by authorization status (VM skips already-decided lines, 107); no CPOE pre-check for cash/discharged visits; no retry on any code; failures are logged with the VisitId. Parent 34597; related 32849 (predict approval API call and rejection alerts), 49431 (predict approval contractors configuration). [Confirmed — user, 2026-11-03]
