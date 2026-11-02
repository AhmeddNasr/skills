# HMIS — Lab and Rad (LR schema)

## Databases

- AHJ prelive = MCP `hmis-prelive-db` → database `AHJ.Env.HCMS_prelive` on `AHJ-HMISDBTEST1`. ANC prelive = `anc-prelive-db` → `ANC.Env.HCMS.Prelive`. [Confirmed — prelive DB, 2026-10-31]
- The query login cannot read view/routine definitions (`sys.sql_modules` and `INFORMATION_SCHEMA.VIEWS.VIEW_DEFINITION` come back empty). `INFORMATION_SCHEMA.VIEW_TABLE_USAGE` works for finding which views read a table. [Confirmed — prelive DB, 2026-10-31]
- `execute_query` rejects `UNION`; run separate queries. [Confirmed — prelive DB, 2026-10-31]

## How a lab result is stored [Confirmed — prelive DB, 2026-10-31]

- `LR.Investigation` — one row per ordered test. `LastStatusID` → `LR.InvestigationState` (1 Not Performed, 2 Performed, 3 Specimen Collected, 4 Completed, 5 Specimen Received, 6 Specimen Rejected). Donor tests carry `DonationID` / `BloodUnitID`.
- `LR.InvestigationResult` — result header, `TransactionInstanceID` = `Investigation.ID`. `ResultTypeID` → `LR.SLKP_ResultType` (1 Provisional, 2 Final). Updated in place: practically one row per investigation.
- `LR.InvestigationResultComponent` — one row per component. `Result` is free-text `nvarchar`; also stores `NormalityID`/`Normality`, `Min`/`Max`, `IsPanic`, `AnalyzerId`, `EditResultReasonID`.
- "Final complete" = `ResultTypeID = 2` **and** `LastStatusID = 4`. Final-but-not-completed and Completed-with-Provisional both exist in data.
- `LR.InvestigationComponent` is product-scoped (`ProductID`): the same test (e.g. HIV) exists as many component rows across products/panels. Has `LoincId`.
- `LR.ComponentReferenceRange` — bands by `ComponentID`, gender, age, analyzer, with `Min`/`Max`, `NormalityID`, `IsNormal`, `IsPanic`. HIV: 0–1 NON REACTIVE, ≥1.01 REACTIVE (`IsPanic = 1`).
- `LR.ComponentPredefinedValue` — per-component dropdown values (`ComponentID`, `PredefinedValue`); no normality column.
- `LR.SLKP_Normality` — 21 values, e.g. 13 NEGATIVE, 14 NON REACTIVE, 15 NORMAL, 16 NOT DETCTED, 17 POSITIVE, 19 REACTIVE, 21 WEAK POSITIVE.
- `LR.InvestigationHistory.ActionTypeId` → `LR.SLKP_ActionType` (1–15: Collect … Add Provisional/Final Result, Edit provisional/final result, Print, Reprint).
- `LR.InvestigationResultAudit` + `LR.InvestigationResultAuditComponent` — full copy of the result on each save; started 2026-10-25.
- LR table naming for component-level config: `Component<Thing>` with a `ComponentID` column plus standard columns (EntityID, IsDeleted, DeletedBy, DeletedDate, CreatedDate, CreatedBy, UpdatedDate, UpdatedBy, ModifiedTS). Single EntityID 102 on AHJ.

## Data quality facts [Confirmed — prelive DB, 2026-10-31]

- Text results are accepted on numeric components (22,791 in 2026 on 182 components, mostly `< 10.0`-style comparators).
- `NormalityID` is often not saved: 17 of 60 positive HIV results in 2026 had none.
- `AnalyzerId` is empty on result components since July 2026, so analyzer vs manual entry can't be told apart from data.
- Labs type MOH-pending notes by hand in HIV results ("SENT TO MOH", "waiting for confirmation from MOH", ...).

## Feature history

- **Feature 34246 — HIV Result block** (ticket 5205). Merged into a single PBI 34255 (rewritten in ADO, rev 35: 10 ACs, 2 messages, both on selecting Complete; completion is also checked server-side); 35849 and 37234 set to Removed with a comment pointing to 34255. Permission: "Manage restricted lab results" on the Lab Rad business entity. [Confirmed — user + ADO, 2026-11-01]
  - Config: `LR.ComponentRestrictedNormality` (ComponentID + NormalityID), DB-only. A result is restricted when its saved normality is configured for its component.
  - Analyzer results save normally as provisional/final. In the Add/Edit Result popup the restriction is checked **before saving**; a lab user without "Manage restricted lab results" cannot save a restricted result. Only users with the permission can complete an investigation with a restricted result.
  - On complete, a restricted result is saved as "Awaiting MOH confirmation" / "بانتظار تأكيد وزارة الصحة" with no normality, unless the "MOH confirmed" checkbox is ticked. The checkbox is **not saved**; it only lets the entered value be kept on that completion.
  - MOH negative: user undoes complete and edits value/normality; the check runs again before saving.
  - Lab grid: red highlight + blocked icon only (no filter, no hover message). Blood bank is not mentioned in the story at all (user's choice).

- **PBI 37217** (module Lab and Rad, iteration R12.6_Sprint 2): originally "physician + location in the lab patient banner for OPD/ER". User redirected it on 2026-11-01 to the **lab grid**: clicking the visit number opens a popover with visit number, physician and full location (clinic name / ER bed / IPD floor + bed), replacing today's hover tooltip that only repeats the visit number. [Confirmed — user + ADO, 2026-11-01]
  - Rules [Confirmed — user, 2026-11-01]: applies to **both lab and radiology grids**; physician = the physician assigned to the visit (nothing else); ambulatory = physician only, no location; missing values are simply not shown (no "Not recorded"); popover closes with a small X at top right or a click outside (no Esc); the popover shows the clicked row's visit (no "latest visit" wording — the row is already linked to its visit).
  - Applied 2026-11-01 (rev 31, 11 ACs, title "Show visit physician and location in the lab and radiology grid visit popover"). Also confirmed: IPD location = latest bed of the visit; OPD "clinic name" written without naming its source; popover is read-only. Parent 37216, child 43066. Ticket number still empty. [Confirmed — user + ADO]

## Results for the summary widgets (verified prelive, 2026-11-01)

- `LR.Investigation.OrderLineId` = `CPOE.Orders.ID`; usually one investigation per order (705 of 114k orders had 2–4). `InvestigationClassificationId` → `LR.SLKP_InvestigationClassification` 5 Lab, 6 MI, 11 Microbiology (`IsMicrobiology` flag is false even for 11). MI investigations only use statuses 1 Not Performed, 2 Performed, 4 Completed.
- Lab components: `LR.InvestigationResultComponent` (`InvestigationComponentEN/AR`, `Result`, `Unit`, `Min`, `Max`, `ShowRefrenceRanges`, `NormalityID` → `LR.SLKP_Normality` with `Name`/`Color`, `ComponentGroupEnName`, `Type` (2 = organism), `OrganismId`, `Notes`). Header `LR.InvestigationResult` (`ResultTypeID`, `ReportPrintableNotes`, `CreatedByName`, `TemplateBody`).
- Microbiology sensitivities: `LR.AntibioticSensistivityResult` (`Resistance` → `LR.SLKP_AntibioticSensistivity` 1 Resistant, 2 Sensitive, 3 Intermediate, 4 Not tested; `MIC`).
- Radiology report = free text in `LR.InvestigationResult.ReportPrintableNotes`; no components, no separate Findings/Impression fields.
- Existing views in schema `PatientSummery`: `Vw_CPOE_PatientSummary_LRDetails`, `VW_CPOE_PatientSummary_LabFinal_Details`, `VW_CPOE_PatientSummary_RadFinal_Details`, `VW_CPOE_PatientSummary_LR_Investigation`, `Vw_CPOE_PatientSummary_ProcedureOrderlines`, `CPOE_VW_MedicationPatientSummery`.
