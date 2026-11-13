# HMIS — General / Cross-Module

## Don't repeat (past corrections — always read this section)

- 2026-11-01 — [ADO] Assumed: PBI 41635 had no parent because `ado_get_work_item` returned no `System.Parent`. → Actually: parent is 41610; the field only appears in some responses. Check relations before saying an item has no parent. (PBI 41635)
- 2026-11-01 — [All stories] Never add an Open Points section to a story; ask in chat instead. (PBI 51348)
- 2026-10-31 — [General/CPOE] Assumed: configurations are set on an admin screen (wrote admin USER steps, a Data Sections field and a "saves configuration" AC). → Actually: configurations are rows in `CPOE.Configuration`, set in the database; no screen. (PBI 49468)


## Writing stories about how HMIS is built

- **Configurations are database values, not screens.** A "configuration" is a row in a module's configuration table (e.g. `CPOE.Configuration`), set directly in the database. There is no admin screen or setup UI. [Confirmed — user, 2026-10-31]
  - In stories: describe the configuration in the context paragraph (key name, value format, what an empty value means) and in the GIVEN clauses of ACs.
  - Do **not** write USER scenario steps where an administrator "opens" or "saves" a configuration, do **not** add a Data Sections field for it, and do **not** write ACs about saving it.
- **"Keyed by visit classification"** for a configuration most likely means its `Value` is a comma-separated list of visit classification IDs (pattern seen in `ShowFluidInOrderEntryVisitClassifications = "2,4"`). [Unconfirmed — inferred from naming pattern in CPOE.Configuration]
- **Global vs per-classification:** a configuration that defines how a rule behaves is a single system-wide value unless the user says otherwise. Don't assume it is per visit classification. [Confirmed — user, 2026-10-31]

## Configuration tables (all modules)

- Modules keep configurations as key/value rows in their own table, e.g. `CPOE.Configuration` (`Id`, `Key`, `Value` nvarchar, `EntityID`, `UpdatedBy`, `UpdatedDatetime`). Other modules may have their own (seen: `VisitMgt.ServiceClassificationConfiguration`, plus several dedicated `CPOE.*Configuration` tables). Check the module's schema for a configuration table before naming a new key. [Confirmed — prelive DB, 2026-10-31]
- List values are comma-separated IDs, e.g. `"2,4"`. Booleans appear as both `"0"/"1"` and `"true"/"false"`. Key names are PascalCase and describe what they hold, e.g. `ShowFluidInOrderEntryVisitClassifications`. [Confirmed — prelive DB CPOE.Configuration, 2026-10-31]
- `EntityID` values seen: `0` (most rows), `102`, `-1`. Meaning not confirmed. [Unconfirmed — likely facility/entity scope, 0 = all]
- Some values are signed URLs with tokens — never copy those values.

## Databases and query tools

- HMIS databases are SQL Server. Available MCP servers: `hmis-prelive-db`, `hmis-devtest-db`, `anc-prelive-db`. [Confirmed — tool list, 2026-10-31]
- New MCP server `Scrum_1_DB` (first seen 2026-11-10): an HMIS database with the same schema family as prelive (Allergy…VS, incl. `CN`, `CPOE`, `Security`, `VisitMgt`) — NOT an ADO work-item store (no work-item tables in it). Its `execute_query` takes plain SELECTs; aliases, joins and LIKE work, and the `limit` parameter bounds rows. [Confirmed — tool listing + queries, 2026-11-10]
- The `execute_query` tool's SQL parser rejects `SELECT TOP n` — use the tool's `limit` parameter instead. `[Key]`-style bracket quoting works. [Confirmed — prelive DB, 2026-10-31]
- For the reserved table name `Security.User`, use `Security."User"` in MCP queries: `Security.[User]` was rejected by the parser and bare `Security.User` reached SQL Server but failed on the reserved keyword; double-quoted table syntax succeeded. This is distinct from the bracketed-column case above. [Confirmed — AHJ prelive query-tool behavior, 2026-11-13]
- Schema names are PascalCase/uppercase (e.g. `CPOE`, `Shared`, `PhysicianDesktop`, `VisitMgt`, `LR`, `Billing`). Lookup tables are prefixed `SLKP_` (e.g. `Shared.SLKP_VisitClassification`). Find tables with `information_schema.tables` and a `LIKE` filter. [Confirmed — prelive DB, 2026-10-31]
- Several modules have their own copy of common lookups (e.g. `SLKP_VisitClassification` exists in `Shared`, `VisitMgt`, `LR`, `CS`, `Finance`, `SC`; `SLKP_ProductClassification` in `Shared`, `CPOE`, `Billing`, `PMGT`, `SC`). Check the module's own schema first. [Confirmed — prelive DB, 2026-10-31]
- `execute_query` rejects a top-level `UNION` ("Query must be a SELECT statement. Found: Union"). Wrap it instead: `SELECT * FROM (… UNION ALL …) x` works. `CONVERT(varchar, date, 120)` inside string concatenation fails to parse, so return the dates as separate columns. `STRING_AGG(...) WITHIN GROUP (ORDER BY …)` and `sys.tables`/`sys.partitions` row counts work. [Confirmed — prelive DB, 2026-11-02]
- The query tool's keyword filter also rejects `REPLACE(` ("forbidden mutative keywords"); use `SUBSTRING`/`LEFT`/`CHARINDEX`. It also drops the connection now and then (`08S01`); just retry. [Confirmed — prelive DB, 2026-11-02]
- "AHJ prelive" = `hmis-prelive-db` (Andalusia Hospital Jeddah; `BloodBank` label config FIN/license `H1088`). [Confirmed — prelive DB, 2026-11-02]
- Database names (`DB_NAME()` / `@@SERVERNAME`): `hmis-prelive-db` → `AHJ.Env.HCMS_prelive` on `AHJ-HMISDBTEST1`; `anc-prelive-db` → `ANC.Env.HCMS.Prelive` on `AHQ-PRELIVE-01`. [Confirmed — live DB query, 2026-11-10]
- Not every module's configuration table uses `Key`: `BloodBank.Configuration` uses `Name` / `Value` / `Desc` (+ `MinValue` / `MaxValue` / `UnitEnName`), and some names contain spaces (e.g. `Next Donation`). [Confirmed — prelive DB, 2026-11-02]

## Packages — VisitMgt / Billing

- When package members are added to the visit, each member gets its own `VisitMgt.VisitService` with `ServicePackageID` = header VisitService ID, `PatientPackageID` = `Billing.PatientPackage.ID`, and `OrderlineID` = the child `CPOE.Orders.ID`. The child order then moves to `StatusId = 3` InProgress, with `TotalCharged = 1`, `TotalAccepted = 0` and `ServiceTransactionsId` = the member VisitService ID. [Confirmed — prelive DB, 2026-11-10]
- A healthy member has a `BillingTransactionId` (its own `Billing.PatientTransaction`) and `IsValidBillingState = 1`. A failed one has `Price`, `PatientShare` and `BillingTransactionId` all NULL and `IsValidBillingState = 0`. [Confirmed — prelive DB, 2026-11-10]
- `Billing.PatientPackage.StartDate`/`ExpiryDate` can come from the visit's creation date, not from when the package was assigned (`IsStartFromPurchasingDate = 1`). That means a package bought late in an old visit can already be expired at purchase. In the one case seen, members consumed after the expiry date were left unpriced, while two packages consumed before expiry were priced. Expiry as the cause is not proven. [Unconfirmed — prelive DB, n=3, 2026-11-10]
- `Billing.SLKP_TimeUnit`: 1 Day(s), 2 Week(s), 3 Month(s), 4 Year(s) (`Package.TimeUnitID` with `PackageExpireAfter`). [Confirmed — prelive DB, 2026-11-10]

## Hospitals and HMIS environments [Confirmed — user, 2026-11-03]

- Egypt hospitals: `AMH` = El-Maadi (Al Maadi; was wrongly called "AMC"), `ANC` = Antoniades, `ARC` = Roushdy, `ASH` = AlShallat (Shallalat). ANC, ARC and ASH run on one environment, `ANC` (AWS, full name "Antonidas/AlShallat/Roushdy") → MCP `anc-prelive-db`. `AMH` has its own environment (AWS).
- KSA environments (code · name · hosting): `ALW` Andalusia Willens Park (Local-KSA in use; an AWS copy is not used), `FWZ` Fawaz (Local-KSA, on Release 9), `HC` Home Care (AWS), `SRI` / `AKW` Sari (Local-KSA), `JDC` Jedda Dental Center (Local-KSA), `SNB` Sanbel (Local-KSA), `CHT` Chatou (Local-KSA), `AHJ` New Haii El-Gamaa (Local-KSA) → MCP `hmis-prelive-db`.
- The org structure (Operations / Technology / AHQ / companies, and the HMIS scrum split) is in the user's org-map artifact: Scrum 1 = Physician Desktop, Nurse Portal and their modules (CPOE, patient problems, screening, …) + Lab & Rad; Scrum 2 = Visit management, Pharmacy, OPD; Scrum 3 = Supply chain, Blood bank; Scrum 4 = NPHIES billing; Scrum 5 = Finance, MPI, Medical setup.

## Shared lookups

### Visit classification — `Shared.SLKP_VisitClassification` [Confirmed — prelive DB, 2026-10-31]

| ID | EnName | ArName |
|----|--------|--------|
| 1 | Outpatient | عيادات خارجية |
| 2 | Inpatient | داخلى |
| 3 | Ambulatory | خدمات |
| 4 | ER | طوارئ |

### Visits — `VisitMgt.Visit` [Confirmed — prelive DB, 2026-11-01]

- Visit type = `VisitClassificationID` (lookup above). Also has `VisitTypeID`, `SpecialtyID` / `SpecialtyEnName` / `SpecialtyArName`, `MainSpecialityID` (+ names), `RelatedIPDVisitID`, `ArrivalDateTime`, `DischargeDate`, `MergedDate`, `VisitStatusID`, `StatusID`.
- **No episode table or episode column exists** in the DB (only billing `EpisodeType` lookups and report views). How the physician portal groups visits into episodes is not confirmed — describe it as the existing episode grouping, don't define it. [Confirmed — prelive DB search, 2026-11-01]
- Visit status = `VisitStatusID` → `VisitMgt.SLKP_VisitStatus`: 1 Planned, 2 Arrived (تم الوصول), 3 Cancelled, 4 In Progress, 5 Discharged, 6 On Leave, 7 Finished. In prelive only 1, 2, 3 and 5 are used on visits. "Arrived IPD/ER visit" = `VisitClassificationID` 2/4 with `VisitStatusID` 2. [Confirmed — prelive DB, 2026-11-01]
- The visit's physician is not a column on `VisitMgt.Visit`. Where it lives, per visit type [Confirmed — prelive DB, 2026-11-01]:
  - OPD: `VisitMgt.VisitAppointment.PhysicianEnName/ArName` (+ `ClinicInstanceID`). Its `LocationEnName` is the **hospital** ("Andalusia jeddah Hospital"), not the clinic. No clinic-name table/column was found in the prelive DB (clinic setup likely lives in another DB). [Unconfirmed where clinic name comes from]
  - ER: `VisitMgt.VisitTriageDetail` (`AssignedDroctorEnName/ArName` — sic, `BedEnName` e.g. "Bed (RZ1-B14)", `ZoneEnName` e.g. "Red Zone", `RoomEnName` = "Emergency department"). View `VisitMgt.VM_VW_LatestVisitDoctorDetails` (`VisitID`, `AssignedDroctorEnName/ArName`).
  - IPD: admitting doctor `VisitMgt.VisitAdmission.AdmittedDoctorEnName/ArName` (+ `AdmittedDoctorLog`); treating physicians `VisitMgt.VisitTreatingPhysicianAssignment` (`PhysicianNameEn`, `AssignmentDate`, `EndAssignmentDate`). Bed history `VisitMgt.VisitPatientAccommodation` (`FloorNameEn` e.g. "Ninth Floor", `RoomEnName` ward e.g. "9th-Floor Ward", `ZoneEnName` room e.g. "ROOM-910", `BedEnName` e.g. "BED-910", `AccommodationStartDateTime/EndDateTime`).
  - Ambulatory: `VisitMgt.AmbulatoryVisitDetails.PhysicianID`. The table has no `VisitID`; its `ID` joins to `VisitMgt.Visit.ID` (shared key). [Unconfirmed — join used successfully, 2026-11-04]
  - Virtual: `VisitMgt.VirtualVisitDetails.PhysicianID` (+ `VisitID`).
- Physician ID columns per visit type, all → `MedStp.Physician.ID` (every ID matched in a 2-month sample; **no declared FKs** from `VisitMgt` to `MedStp.Physician`): `VisitAppointment.PhysicianID`, `VisitTriageDetail.AssignedDroctorID` (sic), `VisitAdmission.AdmittedDoctorID`, `VisitTreatingPhysicianAssignment.PhysicianID` (note `VisitId` casing), `AmbulatoryVisitDetails.PhysicianID`, `VirtualVisitDetails.PhysicianID`. [Confirmed — AHJ prelive DB, 2026-11-04]
- Physician master = `MedStp.Physician`: has `NationalId` (nvarchar, nullable), `HealthID`, `LicenseNumber`, `NPHIESCode`, `IsExternal`, `IsActive`, `IsDeleted`. In AHJ prelive, missing national IDs are `NULL` (never blank), and `IsExternal = 1` on every physician seen on recent visits, so `IsExternal` doesn't tell internal from external there. [Confirmed — AHJ prelive DB, 2026-11-04]
- The query tool rejects any SQL containing the word `merge` (even inside `LIKE '%Merge%'`) — use `'%erged%'`. [Confirmed — 2026-11-01]

## Azure DevOps conventions

- Project `HMIS`, area path `HMIS\Scrum01`. PBIs carry `Custom.Module` (seen values: `CPOE`, `Physician Desktop`). [Confirmed — PBIs 32423, 49468]
- Other people edit PBIs between our saves (tags, ticket number, business value). Re-read a work item before overwriting Description/Acceptance Criteria if time has passed. [Confirmed — PBI 49468 rev 2→8, 2026-10-31]
- `Custom.Module` also seen: `Clinical Notes` (PBI 37270). [Confirmed — ADO, 2026-11-01]
- More `Custom.Module` values: `VisitManagment` (sic — the module's own spelling in ADO, PBIs 23786/23788/29342). Business Value Category picklist string seen stored as `Customer & Strategic value` (lowercase v). [Confirmed — ADO, 2026-11-10]
- More `Custom.Module` values: `Blood Bank` (a few items use `Blood bank`), `Nurse Portal`, `Lab and Rad`, `Ticket`. To list a module's items, run WIQL with `[Custom.Module] CONTAINS '<word>'`. The `ado_query_work_items` tool returns IDs only, and `ado_get_work_item` responses are very verbose (identity blobs, AI review summaries), so hand bulk reads to a subagent. [Confirmed — ADO, 2026-11-02]
- Direct TFS REST calls from the shell (`Invoke-RestMethod -UseDefaultCredentials` to `http://ahq-tfs-azure/DefaultCollection/...`) now return 401, even outside the sandbox; they worked on 2026-10-28. Use the ADO MCP tools (`ado_get_work_item`, `ado_update_work_items`). Large reads get saved to a tool-results JSON file — parse it with node instead of reading it inline. [Confirmed — 2026-11-01]
- `ado_search_code` (project `HMIS`) returned "Search API is unavailable on this server (HTTP 500)" on 2026-11-08; fall back to `ado_cr_get_repo_tree` / `ado_cr_get_file_content`. [Confirmed — ADO MCP, 2026-11-08]
- WIQL on this server rejects `LIKE` ("Expecting comparison operator"); to find a work item's family (Feature/Epic, siblings) use `get_work_items` with `include_relations: true` on the parent and read the `Child`/`Parent` relations instead. [Confirmed — ADO MCP, 2026-11-12]
- PBI story-point "weight" the team sums is `Custom.Standaredweight` ("Standared weight", picklist 0/1/2/3/5/8/13/21), NOT `Microsoft.VSTS.Scheduling.Effort` — they can differ (floating-bar PBIs 46813/56373/56374: Standard weight 5, Effort 8). When asked for a story's weight or a sum, query `Custom.Standaredweight`. [Confirmed — ADO, 2026-11-09]
- To find WHEN a state changed (e.g. committed date): there is no revisions/history tool on the ADO MCP and `System.StateChangeDate` does not exist on this server (TF51535). Use WIQL `ASOF` snapshots instead: run `query_work_items` with `... AND [System.State] = 'Committed' ASOF '2026-11-08T21:59:59'` at day boundaries and diff the ID lists (works; timestamps in the ASOF clause are UTC). `System.ChangedDate` is NOT the commit date — post-commit edits overwrite it. [Confirmed — ADO, 2026-11-09]
- `get_work_items` returns fields under **inconsistent keys**: `System.Description` comes back as the friendly name `Description`, while `Microsoft.VSTS.Common.AcceptanceCriteria` and `Custom.*` come back under their reference names; empty fields are omitted from the response entirely. Read the returned keys before concluding a field is empty — a "missing Description" after `update_work_items` was actually a key-name mismatch. [Confirmed — ADO MCP, 2026-11-12]

## Security / permissions

- Permissions live in the `Security` schema: `Security.Permission` (`ID`, `Name`, `NameAr`, `Description`, `IsDeleted`, `BusinessEntityID`, `BusinessActionID`, `IsStatic`, `Order`), joined to `Security.BusinessEntity` (`ID`, `Name`, `Description`, `NameAr`, `GroupID`) and `Security.BusinessAction` (`ID`, `Name`). Groups: `Security.BusinessEntityGroup` (`ID`, `NameEn`, `NameAr`, `Description`, `Order`) — a group's display name is in `NameEn` (e.g. "Clinical Notes" 400004, "Clinical Sheets" 400005). Roles: `Security.Role`, `Security.RolePermission`, `Security.UserRole`. Filter `IsDeleted = 0`. [Confirmed — devtest DB, 2026-11-01; entity/group columns Scrum_1_DB, 2026-11-10]
- In stories, name a permission by its `Security.Permission.Name` and its business entity, e.g. "Order on any visit" (Order Entry). [Confirmed — PBIs 34941, 35258, 37270]
- Permissions by area (devtest, `ID — Name`): [Confirmed — devtest DB Security.Permission, 2026-11-01]
  - **Order Entry** entity: `100001 View Order Entry Screen`, `100002 Order Laboratory Investigations`, `100003 Order MI Investigations`, `100004 Order Procedure Investigations`, `100007 Order Medication`, `500057 Order on any visit`, `100521 order on discharged visit`, `100520 order with past date`, `100006/100015 View Order Sets`. Also `500003 Order Packages` (Order Entry Packages), `500012 Order fluids` (Medication Investigations).
  - **Order Management** entity: admission/discharge order, home medication, blood orders (IDs in `blood-bank.md`), `11000000186/187 Edit Requesting Physician - Admission/Discharge` (PBI 34941).
  - **ClinicalNotes** entity (ID 400015, group "Clinical Notes" 400004): `444486 View Clinical Notes`, `444488 Add Clinic Note`, `444489 Preview Clinical Notes`, `444490 Cancel Note`, `444491 Add Macro` (today's per-physician macro screen), `444492 Reply Note`, `444493 Delete Replay`, `100535 GetCNConfigurations`, `11000000188 Add clinical notes to unassigned OPD visits` (PBI 37270). [Confirmed — devtest DB 2026-11-01; full list Scrum_1_DB, 2026-11-10]
  - **ClinicalSheet** entity: `444504 Add Sheet`, `11000000189 Add clinical sheets to unassigned OPD visits` (PBI 37270), `444501 View Clinical Sheet`; plus one permission per sheet template (e.g. `SickLeave`, `ER Physician Assessment`).
  - **ProblemCard** entity (diagnoses): `400002 Add Patient Problem`, `444506 Edit Patient Problem`, `444527 Manage Patient Problems`, `11000000185 Manage diagnosis on unassigned OPD visit` (PBI 35258).
  - **Manage Allergies** entity: `210121 Manage Allergies`, `210124/210125 Edit (own/any) Allergy`, `210122/210123 Delete (any/own) Allergy`, `210126 View Allergy History`.
  - **Screening** entity: `500015 AddNewScreening`, `500014 ViewTheScreeningTab`. **VitalSign** entity: `444451 Add Vital Signs`.
- "Unassigned visit" restrictions (feature 34938 "Physician input restrictions") apply to **OPD visits only**; a physician assigned to the visit is never restricted by them. [Confirmed — PBIs 35258, 37270]
