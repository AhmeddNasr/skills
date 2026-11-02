# HMIS — Blood Bank (`BloodBank` schema)

Studied in the AHJ prelive DB (`hmis-prelive-db`, Andalusia Hospital Jeddah — label config `FIN`/`LicenseNumber` = `H1088`). Data runs from May 2025 to Oct 2026. Unless marked otherwise every fact below is `[Confirmed — prelive DB, 2026-11-02]`.

## Module map — four sub-areas

1. **Transfusion orders**: physician orders blood in CPOE → the Blood Bank work list reserves, cross-matches and dispenses units → the nurse administers them (eMAR/NP).
2. **Donation**: donor → questionnaire, consent, vital signs → collection → processing (diffract/split) → donor lab tests → approved units go into stock.
3. **External blood units**: units received from other hospitals, approved and then stocked.
4. **Setup**: products, compatibility matrix, lab investigation setup, machines, reasons, questionnaire, configuration.

`BloodBank` has 93 tables, no views and no stored procedures. It also keeps its own `__MigrationsHistory`, so it is EF Core code-first. [Unconfirmed — inferred from the table name]

## 1. Transfusion order flow (CPOE → Blood Bank → nursing)

### CPOE side (ordering)
- `CPOE.TransfusionOrderLine`: one row per blood order line. `TransfusionOrderLineId` = `CPOE.OrderLine.OrderLineId` (all 16.5k rows join). Columns: `BloodComponentID`, `UrgencyID`, `TransfusionReasonID`, `DispensingNote`, `ProductBloodTypeID/ProductBloodType`, `UOMID/UOMEnName` (ML or Bag), `BloodBagOverrideReasonId`, `WristOverrideReasonId`, `IsFromScanner`, `IsPrepared`.
- On `CPOE.OrderLine`, blood orders are `ProductClassificationId = 10` (Blood Products) and `OrderLineTypeId = 14`. Statuses used: 1 Ordered (most), 8 Stopped, 3 InProgress, 4 Complete, 7 Started, 5 Dismissed.
- `CPOE.SLKP_BloodComponent`: 1 RBC, 2 reagent, 3 Plazma (sic), 4 Platelets, 5 Cryoprecipitate. **The IDs differ from `BloodBank.SLKP_BloodComponent`** (where 2 = Whole Blood and 6 = reagent).
- `CPOE.SLKP_TransfusionReason`: 1 Surgery (most), 2 Injury, 3 Bleeding, 4 Diseases, 5 others.
- `CPOE.SLKP_Urgency` (`IsTransfusion` flag): 1 Routine (shown as "Normal"), 2 STAT (shown as "Urgent"). PRN is not offered for transfusion.
- `CPOE.TransfusionSpecificRequirements` → `CPOE.SLKP_SpecificRequirements`: 1 Irradiated, 2 HLA Matched, 3 CMV Negative, 4 filtered & washed. Multi-select; about 1% of orders have one.
- `CPOE.TransfusionRelatedLabOrders` (`TransfusionOrderLineId`, `RelatedLabOrderId`) links the blood order to its lab orders, e.g. cross-match and grouping.
- `CPOE.AdmissionBloodNeeds`: blood needs captured on the admission order (component, reason, urgency, blood group, specific requirement IDs, related lab order IDs).
- `CPOE."Order".TransfusionEditReasonId` → `CPOE.SLKP_TransfusionEditReason`: 1 Change Management Plan, 2 Patient Discharged.

### Blood Bank side (work list, reserve, dispense)
- `BloodBank.BloodOrder` has **one row per CPOE order-line instance** (`OrderlineID` + `OrderlineInstanceID` → `CPOE.OrderLineInstance.OrderInstanceId`). It holds a denormalised snapshot: patient, visit, classification (IPD ≈ 69%, ER ≈ 31%; no OPD), product, component, `PatientBloodTypeID`, `ProductBloodTypeID`, `Quantity` / `ChargedQuantity` / `DueQuantity`, UOM, `SpecificRequirementEnName` (comma-joined), the physician, and notes (dispensing, reception, physician).
- `BloodOrder.StatusID` → `BloodBank.SLKP_OrderStatus`: 3 Pending, 4 Inprogress, 5 Completed, 6 Cancelled, 7 Dismiss. In prelive only 3 (≈ all) and 7 are used, so progress is tracked per unit in the transactions instead.
- `BloodBank.BloodOrderTransaction` has **one row per blood unit assigned to an order instance** (`OrderlineInstanceID`, `BloodUnitID`). Key columns: `StatusID`, `DispenseDateTime`, `DispenseOnPatientDateTime`, `IsHeld` + `HoldEndDateTime`, `IsLabResultConfirmed` + `ConfirmedBy/ConfirmationDateTime`, `ReturnReasonID`, `UnReservedReasonID`, `DiscardReasonId`, `ServiceTransactionID` (billing), `NATServiceTransactionID` + `IsNATServiceCancelled`.
- Transaction `StatusID` → `SLKP_TransactionStatus`: 1 New, 2 Reserved, 3 Testing, 4 Matched, 5 Not Matched, 6 Discarded, 7 Dispensed, 8 Returned, 9 UnReserved, 10 Canceled, 11 Perform, 15 Rejected. Prelive mix: Dispensed 54%, Matched 31%, Canceled 13%, then Returned, Discarded, Reserved, Perform.
- `TransactionTypeID` → `SLKP_TransactionType`: only 1 Active.
- `SLKP_ReturnReason`: 1 Patient Reaction, 2 Doctor Decision (most returns). `SLKP_UnReservedReason`: 1 Doctors fault, 2 Other. `SLKP_DiscardReason`: 1 Discard from automatic, 2 Discard action, 3 Expired blood unit.
- `BloodOrderTransactionVisualInspection` stores the answers (`QuestionID` → `SLKP_VisualInspectionQuestion`, `Answer` bit). `IsReturnVisualInspection` = 1 for the inspection done on return.
- `BloodOrderTransactionWitnessStep` stores the witness per step (`StepId` → `SLKP_BloodUnitStep`: 1 Discard, 2 VisualInspection, 3 Return).
- `BloodTransactionTag` (`GeneratedName`, `OrderTransactionID`) is the printed cross-matching tag (permission "Print Cross matching tag").
- `BloodTransactionLog` is the history snapshot per unit/order (patient, product, component, type, status, `IsUnReservedByJob`).
- `LabInvistgationResult` (sic) holds per-transaction lab checks (`BloodOrderTransactionID`, product = test, `InvistgationStatusID` → `SLKP_InvistgationStatus` 1 Yes / 2 No / 3 Not Done, `ServiceTransactionID`).
- `dbo.BloodOrder_Staging` is a staging table for imported blood orders. [Unconfirmed — purpose inferred from the columns]

### Nursing administration (outside `BloodBank`)
- `CPOE.TransfusionOrderWitnessEvents`: start, stop and dismiss events with a witness (`TransfusionOrderEventId` → `CPOE.TransfusionOrderEvents` 1 Start, 2 Stop, 3 Dismiss Blood Transfusion). Also holds `TransfusionReactionName` (rare: Itching, Fever, Hypo/Hyper-tension), the authorising physician, and start/complete dates.
- `NP.VisualInspection` (correct unit number, ABO/Rh, product, volume, expired), `NP.UnitIntegrity` (leaking, clotting, hemolysis), `NP.ConfirmPatientPreMedication`. All are keyed by `TransfusionOrderLineId` and carry a witness.
- `VS.VitalSignTransaction.TransfusionOrderLineID` links vitals taken during a transfusion.
- `CPOE.PerformTransfusion` (`OrderLineInstID`, `PerformedQuantity`, `BloodUnitBarcodes`) has only 5 rows, so it is barely used.
- Barcode overrides: `TransfusionOrderLine.WristOverrideReasonId` → `CPOE.SLKP_OverrideReason` category 3 (13 ID band unreadable, 14 scanner malfunction, 15 downtime). `BloodBagOverrideReasonId` uses category **6** IDs 28–32 (emergency draw, label unreadable, scanner, downtime, limited access). About 3% of lines are overridden.

## 2. Blood units (stock)

- `BloodBank.BloodUnit` is the bag that gets dispensed: `Serial`, `BloodUnitNo`, `Barcode`, `ProductID`, `BloodComponentID`, `BloodTypeID`, `ExpireDate`, `BagStatusID`, `BloodSourceID`, `Quantity`, `UnitOfMeasure`, `Volume`, `Temperature`, warehouse location, nurse, `MatchedBy`, `DiscardNotes`.
- `BagStatusID` → `SLKP_BagStatus`: 1 New, 2 Reserved, 3 Under Testing, 4 Matched, 5 Not Matched, 6 Discarded, 7 Dispensed, 8 Returned, 9 Cancelled, 10 UnReserved, 11 Draft, 12 Hold, 13 Perform, 14 Under Visual Inspection, 15 Rejected. Prelive: 89% Dispensed, then Matched, New, Discarded.
- `BloodSourceID` → `SLKP_BloodSource`: 1 Patient (the only one marked `Selectable`), 2 Purchase, 3 External, 4 Donation. Prelive: Donation 52%, Patient 30%, External 18%.
  - Source 4 units match `DonationBloodUnit.SerialNumber` on `BloodUnit.Serial`. Source 3 units match `ExternalBloodUnit.SerialNumber`. [Confirmed — join counts]
- `BloodBank.BloodProduct` (59 rows) is the catalogue of orderable blood products, one per component × blood type (e.g. "RBC A+" code `BB51`, "Plasma O-" `BB71`). It also holds reagents and kits. All rows are in Supply Chain category 4072 "Blood Bank Products". `ProductID` is the Supply Chain product ID.
- `BloodBank.BloodProcess` (`BloodUnitID`, `ModifierID`, `ExpiryDate`, `SerialNumber`, `IsCancel`) and `BloodProcessGroup` (`ProcessGroupChildID`, `IsParent`) hold ISBT 128 processing attributes applied to a unit (irradiation etc.).

### Compatibility matrix — `BloodBank.CompatibilityMatrix` (110 rows)
`BloodComponentID` + `PatientBloodTypeID` → allowed `CompatibleBloodTypeID`s. It is used when scanning a unit (config `CompatibilityMatrixEnabled`) and when adding or editing a unit with source Patient (`ApplyCompMatrixInAddEditBloodUnit`).
- RBC (1): standard ABO/Rh red-cell rules. O− patient → O+, O− (**O+ is allowed for O−**). AB+ → all types.
- Whole Blood (2): only A+, A− and O+ patients are configured. Other types have no rows.
- Plasma (3), Platelets (4), Cryo (5) have site-specific rows (e.g. platelets A+/B+/O+ patients → any type).
- **Treat the matrix rows as the source of truth. Don't restate textbook rules in stories.**

## 3. Donation flow

- `BloodBank.Donor` is one row per donor and is tied to an MPI patient (`PatientID`). Columns: `Code`, `DonorIdentifier`, demographics, `BloodTypeID`, `DonorStatusID` → `SLKP_Donor_Status` 1 Active, 2 Permanent blocked, 3 Temp Deferral, plus deferral fields (`DeferralTime`, `DeferralTimeType` = duration unit 1 Days … 4 Years, `DeferralFrom/EndDateTime`, `DeferredBy`). About 6% of donors are permanently blocked.
- `BloodBank.Donation` is one row per donation visit (`DonorID`).
  - `DonationStatusID` → `SLKP_Donation_Status`: 1 Under Testing, 2 Approved, 3 Rejected, 4 Blocked.
  - `DonorTypeID` → `SLKP_DonorType`: 1 Volunteer (99%), 2 Directed (`IsDefault`), 3 Autologous.
  - `DonationComponentTypeID` is 1 or 2 (no lookup table). It likely means 1 = Whole Blood and 2 = Platelets/apheresis. [Unconfirmed — matches config `Next Donation_WholeBlood_Days` / `_Platelets_Days`]
  - Also holds pre-donation CBC (`HB`, `PlateletsCount`, `WBC` — fed from `BloodUnitInvestigationConfig`: HB, WBC, Platelets Count components), witness and consent-witness employees, `IsUseDINSerial`, `IsConsentBlacklisted` + reason, and the rejecting employee.
  - The flags `BeforeVitalSigns` / `BeforeQuestionnaire` / `BeforeConsent` are 0 on most rows and 1 on newer ones. [Unconfirmed — likely legacy rows from before those steps existed]
- Pre-donation steps, each with a witness and a status:
  - **Questionnaire**: `DonationQuestionnaire` (`StatusID` 1/2/3, most 2 — likely Pending/Approved/Blocked like vital signs [Unconfirmed — no lookup table]) + `DonationQuestionnaireAnswer` (`IsBlocked`). Setup: `QuestionnaireGroup` (Group A–D) → `QuestionnaireSection` (10, e.g. "In the Past 48 hours", "Have you EVER") → `QuestionnaireQuestion` (55, gender-specific via `SLKP_QuestionnaireGenderType` Male/Female/Both, control `RadioButton`/`DDL`) → `QuestionnaireQuestionAnswer` (227; each answer has a `QuestionnaireActionId` → `SLKP_QuestionnaireAction` 1 NoAction, 2 BlockedPermanently, 3 Defer, plus `DurationValue` + `QuestionnaireDurationUnitId`).
  - **Consent**: `ConsentQuestions` (7 yes/no items) + `DonationConsentAnswers`. The full consent text is in config `ConsentEnText` / `ConsentArText`. `DonationConsentBlacklistDetails` (deferral from consent) is empty.
  - **Vital signs**: `DonationVitalSigns` (weight, height, temperature, pulse, SBP/DBP, `VitalSignsStatusID` → `SLKP_VitalSignsStatus` 1 Pending, 2 Approved, 3 Blocked). Ranges come from `BloodBank.VitalSignsRanges` (separate from `VS`), e.g. weight normal ≥ 50 kg, temperature 36.5–37.5 °C, pulse 50–100, SBP 90–180, DBP 50–100.
- **Collection and processing**: `BloodBank.DonationBloodUnit` is a tree of units per donation.
  - `ActionID` → `SLKP_Actions`: 1 Collect (root bag, `ParentID` NULL), 2 Diffract (component separation), 3 Split (aliquot). `ParentID` points at the source unit. `SplitLevel` is 1–2 (config `MaxSplitLevel` = 2).
  - `StatusID` → `SLKP_DonationBloodUnitStatus`: 1 Under Testing, 2 Approved (most), 3 Rejected, 4 Blocked, 5 Draft, 6 Discarded.
  - `AnticoagulantID` → `SLKP_Anticoagulant`: 1 CPD (21 d), 2 ACD-A (5 d), 3 CPDA-1 (35 d), 4 CPD > SAGM (42 d). `ExpiryDays` drives the default expiry.
  - Also: blood bag product, warehouse IDs, `Volume`, `DrawingStart/EndTime` (config `MaxDrawTimePerMinute` = 10), `HasClots`, `IsRBCDiffract`, `DiffractedStatusID`, violation fields, the visual-inspection witness, `IsDiffractionLabelsPrinted`, `IsOldData` (rows before 2025-08-30 are migrated legacy data).
  - Related tables: `DonationBloodUnitVisualInspection`, `DonationBloodUnitWitnessStep`, `DonationBloodUnitMachine` (machines used), `DonationBloodUnitLog` (full history).
- `DonationDIN` (`DIN`, `CheckCharacter`, `FlagCharacter`) is the ISBT 128 Donation Identification Number. `SLKP_RHDBloodGroupCode` holds the ISBT 128 ABO/RhD codes per blood type × donor type (e.g. O− volunteer = `95`, A+ volunteer = `62`).
- `DonationPatient` / `DonationPatientVisit` link a directed donation to the recipient patient and visit.
- **Donor lab tests** live in `LR.Investigation` with `DonationID` (+ `BloodUnitID` for after-donation tests). `InvestigationDonationTypeID` → `LR.SLKP_DonationType` 1 Before, 2 After. `LR.DonationData` mirrors the donation for LR (`DonationStatusID` → `LR.SLKP_DonationStatus` 1 Under Testing, 2 Approved, 3 Reject, 4 Blocked, 5 Draft). The test catalogue is `BloodBank.LabInvestigation` (`ProductID`, `InvestigationTypeID` → `SLKP_LabInvestigationType` 1 Before Donation, 2 After Donation, 3 Before Transfusion, 4 On Dispense; `IsDefault`):
  - Before donation: Complete Blood Count.
  - After donation: Donor Blood Group & Rh, Antibody Screening, Donor Screening, RBCs Phenotyping, Malaria Ag (defaults); Calcium, Blood Culture, Syphilis TP Abs, NAT (HBV/HCV/HIV) (optional).
  - Before transfusion: Antibody Screening, Cross-Match, Blood Group & Rh, Blood Typing Patient Serum.
- **Supply Chain**: `SC.ReceiveDonation` (+ `ConsumedProduct` / `ReceivedProduct`) posts the stock movement when a donated unit is received into the blood bank warehouse (consumes the empty bag, receives the blood product).
- Reasons: `BloodBank.Reason` (94) grouped by `SLKP_ReasonClassification`: 1 Reject, 2 Add To Blacklist Permanent, 3 Split With New Blood Bag, 4 Diffraction With New Blood Bag, 5 Add To Blacklist Temporary Deferral (36 reasons with durations, e.g. "HB below 12.5 g → 30 days", "Whole blood donation → 56 days"), 6/7 Blacklist Vital Signs (temp/permanent), 8 Reject Visual Inspection, 9 Blacklist from Consent.
- `SKLP_BloodUnitValidationReason` (sic prefix): 6 draw-time/volume validation messages (e.g. "Risk of inadequate anticoagulation").

## 4. External blood units

- `BloodBank.ExternalBloodUnit`: a unit received from another hospital (`HospitalID` → `BloodBank.Hospital`, 7 Jeddah hospitals; ID 7 "Andalusia Hai al jamea hospital" accounts for 98%). Columns: `SerialNumber`, product, component, type, quantity, dates, `IsDraft`, `IsApproved` + decision user and date, `IsDiscarded` + witness. Also `ExternalBloodUnitVisualInspection` and `ExternalBloodUnitLog`.

## 5. Setup / reference data

- `BloodBank.SLKP_BloodComponent`: 1 RBC (PRBCs, 42 d), 2 Whole Blood (WB, 35 d), 3 Plazma (FFP, 365 d), 4 Platelets (P, 5 d), 5 Cryoprecipitate (CRY, 365 d), 6 reagent; 7 and 8 are deleted test rows. Flags per component: `Collectable` (WB, Platelets), `Difractable` (WB, Cryo), `Splittable` (RBC, FFP, Platelets), `IsUrgent`, `PrintRH` (RBC, WB). Also an ISBT `Code` (C0001…) and storage/transport temperature IDs.
- `SLKP_ComponentStorageTemperature`: 1 (1 : 6)°C, 2 (−18 : −40)°C, 3 (20 : 24)°C. `SLKP_ComponentTransportTemperature`: 1 (1 : 10)°C, 2 (20 : 37)°C, 3 (20 : 24)°C.
- `BloodBank.SLKP_BloodType`: 1 A+, 2 A−, 3 B+, 4 B−, 5 O+, 6 O−, 7 AB+, 8 AB−, 10 "-" (unknown). Names are "A Positive" etc.; `InvestigationComponentName` "(A+)" maps lab results. **Different IDs from `MPI.SLKP_BloodGroup`** (the patient's group, see `physician-desktop.md`). Patient group changes are logged in `MPI.BloodGroupLog`.
- ISBT 128 coding: `SLKP_ProductDescriptionCode` (18k product description codes), `SLKP_Modifier` (43, M0000 No Modifier, M0001 Washed, M0002 Frozen, M0007 Apheresis, M0008 Thawed, …), `ClassModifierCombinations`, and `SLKP_ProcessGroupParent` (30 attribute groups V00xx, e.g. Irradiation, Residual Leukocyte Content, Storage Conditions) → `SLKP_ProcessGroupChild` (1,040 values).
- `BloodBank.Machine` (24): devices per `PhaseID` → `SLKP_MachinePhase` 1 Donation, 2 Diffraction, 3 Split. Preventive maintenance: `PPMStartTime`, `DurationMonths` (all 6), `PPMExpiryTime`. `PPMHistory` is empty.
- `BloodBank.Product` (24) is a local copy of Supply Chain lab products used by `LabInvestigation`.
- `SKLP_ProductUOM`: ML (ratio 1), Bag (ratio 500 mL).

## Configuration — `BloodBank.Configuration`

Columns: `Name` (**not** `Key`), `Value`, `Desc`, `MinValue`, `MaxValue`, `UnitEnName`, `EntityID` (0 or 102). Some names contain spaces. Notable keys:

| Name | Value | Meaning |
|------|-------|---------|
| `WarehouseID` | 793 | Blood bank warehouse in Supply Chain |
| `ApplyCreateService` / `ApplyCancelService` | true | Create or cancel billing services |
| `ApplyConfirmLabResult` | true | Lab result must be confirmed before dispense (`IsLabResultConfirmed`) |
| `BloodUnitHoldPeriod` | 240 (min) | Hold period for a unit |
| `UnReserveBloodOrderTransactionHour` | 72 | A job auto-unreserves reserved units after 72 h (`IsUnReservedByJob`) |
| `Discard Blood Unit` | 240 (min) | Discard a returned unit if return time − dispense time exceeds this |
| `Undo Action` | 30 (min) | Window to undo an action |
| `PartialReturnEnabled` / `ShowReturnAndUnReserveReason` | true | Return behaviour |
| `CompatibilityMatrixEnabled` / `ApplyCompMatrixInAddEditBloodUnit` | true | See compatibility matrix |
| `AddLabInvestigationServiceWhenDiscard` | false | |
| `Next Donation` | 60 (days, min 60) | General donation interval |
| `Next Donation_WholeBlood_Days` / `_Platelets_Days` | 56 / 14 | Per-component donation interval |
| `MaxSplitLevel` | 2 | |
| `MaxDrawTimePerMinute` | 10 | Max collection draw time |
| `BloodUnitVolumeRange` | 400–550 mL (Min/MaxValue) | Acceptable bag volume |
| `WholeBlood…MachineNum` / `Platelets…MachineNum` | 2 / 1 | Machines required per collection |
| `PlasmaBloodComponent` / `PlasmaDiffractionDurationPerHour` | 3 / 480 | Plasma diffraction expiry monitoring |
| `ProcessGroupIrradiationChild` / `…ExpiryDay` | "341,342,343,344" / 28 | Irradiation shortens expiry to 28 days |
| `InvestigationPhenoTypeID` / `ComponantRPCID` | 77306 / 1 | Phenotype test and RBC component printed on the label |
| `DonationDateType` | 1 | 1 Gregorian, 2 Hijri |
| `Attachment…` | 5 MB, jpg/png/pdf | Donation attachments (`DonationAttachment` is empty) |
| `DonationBloodUnitLabel*` | 10×10 cm, logo, statement | Unit label |
| `LabJobType` / `LabInvestigationEmployeeIds` | 11 / list of employee IDs | Lab job integration |

- `BloodBank.DonationBloodUnitLabelConfiguration` holds the label header: FIN, collection center name, city, country, postal code, license number, instruction text, tests-result statement.
- `BloodBank.DispenseConfiguration` (`UOMID`, `BelowZeroLimit`) is empty.

## Permissions (prelive `Security.Permission`)

- **BloodBank** entity (400019): `444516 View Blood Bank Work List`, `444515 View Blood Bank Order Details`, `444517 Get Compatible Blood Component`, `444568 Reserve Blood Units`, `444567 Confirm Result`, `444571 Return Blood Units`, `444572 Partially Return`, `444590 DiscardBloodUnit`, `444586 Edit the expiry date`, `444573 Cancel NAT Service`, `300227 Manage Visual Inspection`, `400031 Print Cross matching tag`, `444518 Lab Admin`.
- **Blood Bank Donation** (400023): Donors Management, Accept/Reject, Add To Blacklist, Remove From Blacklist, Undo, Delete Donation, Add/Edit or Delete Blood Unit, Diffraction, Split, view details, questionnaire (add/edit/approve/blacklist), vital signs (manage/edit/approve/blacklist), DonorConsent, Override Next Donation Date, label printing, Add Lab Investigation Before/After Donation, Manage Blood Processes.
- **Blood Bank Investigations** (400025): view, collect, recollect, perform, cancel perform, undo collect, add or edit provisional and final results, change to final, print provisional or final.
- **Blood Bank Setup** (400022): view/add-edit/delete setup, view/manage lab investigation setup. **External Blood Units** (400026): view, add/edit, delete. **Machine** (300049): `305066 Edit blood bank machine`. **Donations** (300044): `300203 View Donations`.
- Ordering and nursing: **Order Management** `100227 Blood Transfusion Order`, `100228 Perform Blood Order`, `100229 Cancel Perform Blood Order`, `100230 Dismiss Blood Order`, `100234 Undo Dismiss Blood Order`, `100231 Edit Blood Order`, `11000000172 EditTransfusionPreparationForms`; **eMAR** `100513 administer blood by barcode`, `100512 override administer blood by barcode`; **Patient** `444511 Edit Blood Group`.

## Feature history (ADO, project HMIS) — `[Confirmed — ADO, 2026-11-02]` unless marked

- Every Blood Bank work item in this ADO project was created in **May 2026 or later**, but blood bank data in prelive goes back to May 2025. So the original build must have been tracked somewhere else, and this backlog only covers the revamp and later changes. [Unconfirmed — inferred from the dates]
- `Custom.Module` is "Blood Bank" (a few items use "Blood bank"). Transfusion-order work is under module `CPOE`, and eMAR work under `Nurse Portal`.
- **Epics and features:**
  - Epic 11392 "Blood Transfusion Cycle" → features 11393 Emergency transfusion request, 11398 Request by units/volume, 12540 Blood Transfusion ER-IPD, 25164 "Blood bank".
  - Epic 1892 "Blood bank Machines" → feature 1893 Machine setup.
  - Other features: 5124 "Blood bank transfusion order", 5981 "CPOE Merged Module - Episode Boundaries & Blood", 35508 "Post donation investigation - Blocking configurations" (no child PBIs yet; dev due 2026-12-01).
  - Most features and epics are still New even when all their children are Done.
  - Epic 516 "Revamp DTC Blood Bank" is New. Epics 646 and 848 "Revamp - Blood bank" were Removed.
- **Revamp, May–Jul 2026:** about 25 Done PBIs titled after service operations (SaveDiffraction, FinishSplit, SaveDonationBloodUnitAsDraft/AsValidated, ReturnBloodUnit, SaveExternalBloodUnit, CancelBloodUnitNATService, …). About 31 "[Remove DTC]" PBIs (6081–6106, 6155–6157) are still New. "DTC" most likely means distributed transaction coordinator. [Unconfirmed — inferred from the titles]
- **Ordering (CPOE):**
  - 5126 (Done): blood components are synced from `BloodBank.SLKP_BloodComponent` into `CPOE.SLKP_BloodComponent`.
  - 5991 (Done): smoke test of the transfusion order. It needs a compatible product and a consent reason, and covers Edit, Perform, Dismiss/Undo Dismiss, the Blood Work List and the Blood Bank Work List.
- **11394 (Done, R12.4)**, ER transfusion request for a patient with no blood group:
  - Plasma or Platelets → AB+. RBC or Whole Blood → O−. (Before: always O−.)
  - A warning banner shows the assumed group.
  - The assumed group is sent to the blood bank when it looks up compatible products.
- **11417 (New, Egypt):** config "Create instances for blood transfusion request". On = one order instance per unit (current behaviour). Off = a single instance.
- **12541 (New):** eMAR should also load pending blood orders from the ER source visit.
- **37050 (New):** print the product on the dispensing label.
- **25166 (Done, Egypt):** on the scan-barcode popup, tube number allows up to 15 characters, and unit number allows letters.
- **Add Blood Unit / labels (feature 25164, Aug–Oct 2026):**
  - 25560 (still New): split into a Pre-Donation popup and a Post-Donation popup.
    - Pre-Donation Save auto-prints **8 bag labels** and sets status Draft.
    - Post-Donation has "Save & Validate" (prints the ISBT label) and "Save as Draft".
    - New permission "Edit Pre Donation Details".
  - 25562: only users with "Print Additional Donation Labels" can print more labels.
  - 25837: 5-question visual inspection; any "No" blocks Save with "blood bag/set is defective".
  - 26371: patient name, DOB and blood type removed from the unit label.
  - 28009 / 30110 / 32145: when saving as a draft, quantity, UOM, draw times, expiry time, blood type, product and fridge are optional. They are all required on Save & Validate.
  - 29920: expiry = donation date + anticoagulant days (CPD 21, CPD-A 35, CPD SAGM 42, ACD-A 5). The time is fixed at 11:59 PM. This matches `SLKP_Anticoagulant.ExpiryDays`, but there the names are CPDA-1 and "CPD > SAGM".
  - 29948: the employee name and code are shown for blocking, rejection and deferral actions.
  - 41600: the entity name prints at the top of the label.
  - 47203: "Print Diffraction Labels" prints a PRBC and an FFP label, with "-WB" in the DIN replaced by "-PRBCs" / "-FFP".
- **Machines (1894):** the diffraction phase needs at least 2 machines (multi-select). An inactive machine clears the field. This matches config `WholeBloodDonationBloodUnitMachineNum` = 2.
- **Open contradictions in the stories (check with the user before relying on them):**
  - 29920 AC-07 says expiry follows the blood component "as old behavior", while AC-01..06 base it on the anticoagulant.
  - The reprint permission is named "Print Additional Donation Labels" in 25562 but "Print Additional Labels" in 47203. Prelive has `305072 Print Additional Donation Labels` and `300226 Allow Printing More Labels`.
  - Stories use the status "Validated", but `SLKP_DonationBloodUnitStatus` has no Validated row (it has Draft 5, Approved 2).
  - 10493 (blood ordered without a blood group is not accepted) overlaps with 11394's default group.

## Open business needs (still to be written as stories) — `[Confirmed — user, 2026-11-02]`

1. **Automatic collection labels for donated bags.** At donation, staff take sample tubes from the bag for the post-donation investigations. Those tubes need labels printed automatically, so analyzers can post results straight into the system and less is entered by hand. Before writing it, check how it differs from the 8 bag labels in 25562. [Unconfirmed — 25562 may cover bag labels only, not sample-tube labels]
2. **Group units in the blood work list.** Each unit creates its own order instance (one `BloodOrder` row per `OrderlineInstanceID`), so reserving 4 bags for one patient means repeating the reserve once per instance. Staff need to reserve several units in one action. Related: 11417 (New), a setting for one instance per order.
3. **Automatic rejection of bags and/or donors from investigation results**, for both pre- and post-donation investigations. Related: feature 35508 (post-donation blocking configurations, no child items yet).
4. **Find a donor by DIN in the donor list.** Today staff search for the donor, expand the row, guess which bag is the right one and select it.
5. **Reorder the donation screen steps.**
   - Today the order is: questionnaire → consent → pre-donation (this part is fine) → donation → post-donation → splitting.
   - The donation form asks for the blood group, drawing start and end times and other values that are only known after post-donation. The blood group is unknown until some post-donation tests are done.
   - Splitting often has to happen before post-donation finishes: it must be done within 8 hours, but NAT runs only twice a week.
6. **The blood group ignores the post-donation result.** The donor/unit blood group does not take the value from the post-donation blood group test ("Donor Blood Group & Rh"). This needs investigation. [Not yet checked in the DB]

## Gotchas

- Typos in names: `LabInvistgationResult`, `SLKP_InvistgationStatus`, `BloodComponant`, `ComponantRPCID`, "Plazma", `SKLP_` prefix on 3 lookups, `Difractable`.
- Three blood-type/group lookups exist (`BloodBank.SLKP_BloodType`, `MPI.SLKP_BloodGroup`, CPOE `ProductBloodTypeID`), and two component lookups (`BloodBank` vs `CPOE`) with different IDs. Always name which one you mean.
- Lab-and-rad stories leave blood bank out (see corrections log, PBI 34255).
