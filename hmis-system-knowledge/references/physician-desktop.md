# Physician Desktop / Physician Portal

## Don't repeat (past corrections — always read this section)

- 2026-11-01 — [Physician Desktop] Assumed: banner menu actions (Print Wristband, Attachment) are out of scope. → Actually: the ⋯ menu has Print wristband, Attachment and Print summary, each opening the existing dialog. (PBI 41634)
- 2026-11-01 — [Physician Desktop] Assumed: episode rows show date range + specialty; visit type is multi-select; filters hide non-matching visits inside an episode; search matches dates; Episode history replaces Clinical notes; only widgets reload on episode change. → Actually: rows show classification, date+time, physician (+ count for folders); visit type is a single-choice dropdown; any match keeps the whole episode; search = physician/specialty only; no Clinical-notes replacement rule; the patient banner reloads too. (PBI 41635)
- 2026-11-01 — [Physician Desktop] Assumed: Quick add belongs in the floating bar story and visible Orders is always enabled. → Actually: no Quick add in 46813; Orders is disabled with "Add diagnosis to order" when a diagnosis is required and missing. (PBI 46813)
- 2026-11-01 — [Physician Desktop] Assumed: notes widget has read/unread, separate episode/all-visits See all, Print. → Actually: no read/unread, notes+sheets combined, 3 per page, cancelled never shown. (PBI 51349)
- 2026-11-01 — [Physician Desktop / Vitals] Assumed: vitals arrows compare with the previous reading, abnormal rows get a red "critical" highlight, See all opens a trend popup, widget has Print. → Actually: arrow = the vital's High/Low status (normal = no arrow), no highlight, See all goes to the Vital Signs screen, Print out of scope. (PBI 51348)
- 2026-11-01 — [Physician Desktop] Assumed: speciality widget tables could be described in 51420. → Actually: never mention speciality-based order/hiding; mention the default order instead. Removed step-3 wording, config bullet and AC-07 (rev 14). (PBI 51420)
- 2026-11-01 — [Physician Desktop] Assumed: Business Value Category follows the category rules (permission restrictions → Compliance & Risk). → Actually: user wants `Cost & Efficiency` for every floating-bar story. (PBI 46813)
- 2026-11-01 — [Physician Desktop] Questioned: PBI 51420 described speciality order/hide behaviour (AC-07) from `WidgetVisitSpeciality` / `WidgetHideVisitSpeciality` tables that exist but are empty; usage was never verified, so it should have been an assumption. (PBI 51420)


## Feature 34938 — Physician input restrictions [Confirmed — ADO, 2026-11-01]

- 34941 Prevent changing ordered by in admission & discharge order (Done) — permissions "Edit Requesting Physician - Admission/Discharge" (Order Management).
- 35258 Prevent adding and editing/delete diagnosis on non-assigned visit (Done) — "Manage diagnosis on unassigned OPD visit" (ProblemCard); disables New Diagnosis, favorite list, edit/delete on unassigned OPD visits.
- 37270 Prevent adding Clinical Notes / Sheets for non-assigned visit (Done, module Clinical Notes) — "Add clinical notes to unassigned OPD visits", "Add clinical sheets to unassigned OPD visits"; disables Add Note, Voice Dictation, Add Sheet with tooltip.

## Floating control bar — PBI 46813 [Confirmed — ADO + design, 2026-11-01]

- PBI 46813 "Floating control bar", module Physician Desktop, no parent, was empty (no description) on 2026-11-01.
- In the design `physician-workspace-offline.html` the bar is `nav.phys-sticky-actions` with: Quick add, Orders (count = sent + saved draft), Notes (count), Sheet template, Consult reply (pending count). All disabled with "Select a visit to document/add orders" when no visit is selected.
- Quick add popup steps in the design: History, ROS, Physical Exam, Assessment, Diagnosis, Orders, Clinical sheet, Review.
- User rules for the bar (2026-11-01): shown on any physician-portal page only when a patient is captured and the user can see at least one button; each button shown only with its permission; Consult reply is out of scope (separate story). [Confirmed — user]
- PBI 46813 written (rev 9, one PBI, 20 ACs). Confirmed rules [Confirmed — user, 2026-11-01]:
  - Buttons: Orders, Notes, Sheet template (Quick add removed from 46813 on 2026-11-01) (Notes and Sheet template are separate buttons). A button without permission is hidden, not disabled.
  - Orders: any of Order Laboratory / MI / Procedure Investigations, Order Medication, Order Packages, Order fluids (View Order Entry Screen not required); unassigned OPD also needs "Order on any visit"; discharged visit also needs "order on discharged visit".
  - Notes/Sheet: IPD, ER, Ambulatory or assigned OPD need "Add Clinic Note" / "Add Sheet"; unassigned OPD needs only "Add clinical notes/sheets to unassigned OPD visits". Assigned = visit physician is the logged-in physician.
  - Quick add: role permissions only (AddNewScreening, Manage Allergies, Add Clinic Note, Add Sheet, Add Patient Problem, any order permission); no visit rules.
  - What each button opens and the counts on the buttons are other stories.

## Summary widget tables (`PhysicianDesktop` schema) [Confirmed — prelive DB, 2026-11-01]

- `Widget` (8 rows): `EnName`, `ArName`, `TemplateURL`, `URL`, `Icon`, `ToolTip`, `ToolTipAr`, `RowSize`, `ColSize`, `DefaultOrder`, `AllowPrint`, `AllowAdd`, `AllowCountRecords`, `IsDeleted`, `EntityID`.
- `WidgetVisitClassification` (25 rows): `WidgetID`, `VisitClassificationID`, `order`, `IsExpand`, `ClientActionName`, `StatusID`, `IsDeleted`. `WidgetMenuItem` (25 rows) links it to menu items.
- `WidgetVisitSpeciality` (`WidgetID`, `VisitSpecialityID`, `Order`, `ClientActionName`, `StatusID`, names) and `WidgetHideVisitSpeciality` (`WidgetID`, `VisitSpecialityID`, `StatusID`, names) **exist but have 0 rows**; `WidgetVisitClassificationStatus` also 0 rows.
- Whether the application reads the speciality tables is **not verified**. **Never mention `WidgetVisitSpeciality`, `WidgetHideVisitSpeciality` or any speciality-based widget order/hiding in stories** — treat them as if they don't exist. [Confirmed — user, 2026-11-01]
- Widget order in stories: order per visit classification (`WidgetVisitClassification.order`), falling back to `Widget.DefaultOrder`. Mention the default order explicitly. [Confirmed — user, 2026-11-01; PBI 51420 rev 14]

## Story preferences

- Floating bar / Physician Desktop stories (2026-11-01): Business Value Category = `Cost & Efficiency` for every story, whatever the category rules suggest. [Confirmed — user, 2026-11-01]

## Clinical notes and sheets (`CN`, `CS` schemas) [Confirmed — prelive DB, 2026-11-01]

- Notes: `CN.ClinicalNote` (`Title` optional — about half of notes have one, `Body`, `HTMLBody`, `TypeID` → `CN.SLKP_Type`, `StatusID` → `CN.SLKP_Status`, `SignDate`, `DraftDate`, `CancelDate`, `CreatedByDisplayName`, `CreatedByJobTitle`, `VisitID`, `IsCritical`).
- Note types `CN.SLKP_Type`: 1 Progress Note, 2 Nursing Note, 3 Consultation Note, 4 Physiotherapy Notes, 6 Operative Report, 9 Physician Instructions, 10 Medication Summary, 11 Physician Round, 12 Respiratory Therapy Note, 13 Physiotherapy Progress Notes, 14 Clinical Pharmacy, 15 Monitor Vitals, 16 Ventilator Readings, 17–20 COE types, 21 Dental Progress Note (5, 7, 8 are "-").
- Sheets: `CS.PatientClinicalSheet` (`FormID` → `CS.Form` with `Name`, `EnDisplayName`, `ArDisplayName`; `HTMLBody`, `JsonObject`, `Note`, `StatusID`, `SignDate`, `CreatedByDisplayName`, `PdfPath`). Sheets have no title of their own; they use the sheet (form) name.
- Status for both (`CN.SLKP_Status`, `CS.SLKP_Status`): 1 Draft, 2 Signed, 3 Cancelled.
- Summary views exist: `PatientSummery.VWPSGetClinicalNotesPerVisitForWidget`, `VWPSGetClinicalSheetsPerVisitForWidget` (+ Draft variants).

## Notes widget — PBI 51349 rules [Confirmed — user, 2026-11-01]

- Notes and sheets are **combined** in one widget (the current system has separate Notes and Sheets widgets) and ordered chronologically, newest first.
- Widget always shows 3 items per page with paging. Item title = note type + the author's own title (notes only); sheets show the sheet name. Under it, max 2 lines: author name, hour, note text, cut with "…". Sheets show no content.
- Clicking an item opens a popup with only that note's/sheet's content. See all = popup with all items untruncated (title, hour, content per note; sheets title + hour, click to view).
- No read/unread anywhere. Cancelled notes and sheets never appear.

## Floating bar update (2026-11-01) [Confirmed — user]

- Quick add is **not** part of 46813 — never mention it there.
- A visible Orders button is disabled until the physician desktop Orders tab requirements are met: if a diagnosis is required and the visit has none, Orders is disabled and hovering shows the existing message "Add diagnosis to order". Don't explain the requirement setup in the story.
- Confirmed and applied 2026-11-01 (46813 rev 11, 51349 rev 12): only signed notes/sheets shown (drafts hidden too); order and hour by sign time; date headings kept; name = `CreatedByDisplayName` (may be a nurse); clicking anywhere on an item opens it; See all = selected episode only; + Add note kept, Print out of scope; widget still called "Notes"; Orders re-enables without reload once a diagnosis is added; "Add diagnosis to order" Arabic must reuse the existing message's Arabic. [Confirmed — user]

## Episode history — PBI 41635 [Confirmed — ADO + user, 2026-11-01]

- PBI 41635 "Episode History widget", module Physician Desktop, parent 41610 (never change it), iteration `R12.6_Sprint 3`, dev due 2026-11-08; empty description and no custom fields on 2026-11-01.
- Applied 2026-11-01 (rev 10). Rules [Confirmed — user]:
  - "Episode history" button (right end of tab row) opens a right-hand panel taking 1 grid column (Summary max 2 columns); clicking again or X closes it; selection stays applied after closing.
  - Multi-visit episode = expandable folder showing: classification + physician of the **latest** visit, date + time of the **first** visit, visit count. Single-visit episode = just the visit. Each visit shows classification, date + time, assigned physician.
  - Filter popup: Visit type = single-choice dropdown (All visit types default, IPD/OPD/ER/AMB); "Show visits" = All visits / My visits / My specialty. Search = physician or specialty only (not dates).
  - Matching rule for every filter and search: an episode with any matching visit shows **in full with all its visits**; non-matching single visits and episodes with no match disappear.
  - Selecting an episode/visit reloads the patient banner **and** every widget for that episode/visit only. Banner and each widget load individually, no full-screen loader, floating control bar usable while loading.
  - No rule about replacing the Clinical notes panel (user removed it).
  - Default open/closed (rev 11): the physician's last open/closed choice wins (saved, used on the next Summary); with no saved choice the panel starts **open**, except **closed** when the patient's most recent visit (by arrival) is an IPD or ER visit with status Arrived. [Confirmed — user, 2026-11-01]

## Summary widgets batch (51350–51358), facts verified 2026-11-01

- `PhysicianDesktop.Widget` today: 4 Diagnosis (DiagnosisView, links via `WidgetMenuItem` to MenuItem 23 "Patient Problems"), 6 Procedure, 7 Medication, 8 Investigations (`ImagingView.html`, lab + radiology in one — the new design splits Lab and Radiology). [prelive DB]
- Medical history: tabs in `MedHistory.ConfigurationTabs` (`Rank`): 1 Social History, 2 Family History, 9 Past Medical History, 4 Surgical History, 5 Medication History, 7 Obs & Gyn. Tables `SocialPatientMedicalHistory` (≈1 per patient), `FamilyPatientMedicalHistory` (`DiseaseID` → `MedHistory.Disease`, `FamilyTypeId` → `SLKP_FamilyType` 1 Father … 5 GrandParents), `SurgicalPatientMedicalHistory`, `MedicationPatientHistory` (`SLKP_MedicationStatus` 1 Taking … 4 Unknown), `ObsGynPatientMedicalHistory`. Summary views `PatientSummery.VWPatient{Social|Family|Past|Surgical|Medication|ObsGyn}MedicalHistoryPerVisit` return `SectionName` + pre-formatted `ResultText`. [prelive DB]
- Chief complaint: `PatPrlm.ChiefComplaint` (`ChiefComplaintNotes`, `VisitID`, `IsDeleted`); max saved length 500; no validation message text in the DB. PBI 8206: Save disabled when empty or unchanged; PBI 51322 adds appointment ID. [prelive DB + ADO]
- No HPI, ROS, physical-exam template or treatment-plan tables exist yet. ADO Feature 41615 "Assessment widget" (Epic 30699) has empty PBIs 30718 (treatment plan/HPI), 41633 (follow-up), 46048 (PE generator), 46049 (ROS generator). `CPOE.FollowUpOrder(Clinic)` is the discharge follow-up, not the assessment one. [prelive DB + ADO]
- ROS / PE generators (applied 2026-11-01: 46049 rev 11, 46048 rev 12; 51351 rev 15 only refers to them). The ROS and PE templates are new (user: "there is no ros/pe template that already exists"); all template, popup, selection, saving and text logic lives in 46049/46048, never in 51351. The template is database-driven: read from the DB each time the popup opens (name, display order, active flag per system and value), no hardcoding, no setup screen; the default lists are only the initial seed (`pwcli/ros_seed.json` 14 systems/149 values, `pe_seed.json` 14 systems/128 values incl. new Breast and Lymphatic, expanded for OPD/ER coverage). Confirmed: one template for all patients; inactive values not offered but still shown on old visits; each system has a toggle Negative/Positive (ROS) or Normal/Abnormal (PE), and Positive/Abnormal can be saved alone ("Neck: Abnormal"); checking a value sets Positive/Abnormal; Negative/Normal clears and disables values; unchecking values keeps the status; clicking the selected option again clears the system; no "Mark unreviewed" button or counter; LMP is not a ROS value; saved as template IDs, saving again replaces; text = one line per documented system in template order, values in template order. Use the correct medical names (PE "Abdomen", ROS "Gastrointestinal"), not names the user types as placeholders. [Confirmed — user]
- Diagnoses: `PatPrlm.ProblemCard` (`VisitID`, `IsFinal`, `DiagnosisTypeID` → `PatPrlm.SLKP_DiagnosisType` 1 Final / 2 Provisional, `ProblemTypeID` → `PatPrlm.SLKP_Problem` 1 Secondary / 2 Primary, `OccurenceID` → `PatPrlm.SLKP_Occurence` (Acute, chronic, Subacute…), `OutComeID`, `IsDeleted`) + `PatPrlm.ProblemCardDetail` (`ICDDiagnoseID/Code/Name`). `IsFinal` and `DiagnosisTypeID` disagree on ~4k 2026 rows. ICD-10 master is the separate database `ICD10.dbo.tblDisease` (`DiseaseID`, `sex`, `AgeL/AgeH(InDays)`, `Valid`), reachable cross-database from hmis-prelive-db. `PhysicianDesktop.DiagnosisConfiguration` (`VisitClassificationID`, `IsRequired`) = diagnosis-required setting. No `IsCashOnly` column yet (PBI 49987 is New). [prelive DB + ADO]
- Design: all six order widgets share one component (All/Pending/Ready, See all, "Add {label} order", "n orders · n ready"); the paged widget fits as many rows as the height allows; assessment is read-only in episode mode. [design]
- Applied 2026-11-01 (51350–51358 rev 13) with all drafted assumptions confirmed by the user: history read-only, sections fixed order, empty hidden; assessment ROS "Negative" / PE "Normal", follow-up whole number ≥1 + Day/Week/Month, episode shows/edits latest visit; diagnosis Add per 35258 rules, disabled with hover message, classification = Occurrence; lab/rad Ready = Complete + Final, status = CPOE order status in lookup colour, Discontinued only under All; medication tabs IPD only, Ended = not Active, no end date = Active; consultation/referral = 49454 split into two read-only widgets; order widgets have no See all / Add. Page size and status colour still differ between widgets as drafted (fit-to-height vs 3 vs 5; colour vs name only). [Confirmed — user]

## Patient banner — PBI 41634 (facts verified 2026-11-01)

- PBI 41634 "Patient Banner": module field is `CPOE`, parent 32442, iteration R12.6_Sprint 6, empty description on 2026-11-01. [ADO]
- Data sources [prelive DB]: blood group `MPI.Patient.BloodGroupID` → `MPI.SLKP_BloodGroup` (1 A RhD positive … 8 AB RhD negative, 9–12 "RhD DU"); COE `MPI.PatientCenterOfExcellence` (`CenterOfExcellenceID`, `IsActive`) → `MPI.SLKP_CenterOfExcellence`; surgery candidate `MPI.PatientSurgeryCandidate` (`IsActive`, `MarkDate`); allergy status `Allergy.PatientAllergyStatus` → `Allergy.SLKP_AllergyStatus` 1 Allergic, 2 Not Allergic, 3 Doesn't have added allergies; financial `VisitMgt.VisitFinincailInfo` (`ContractorEnName`, `ContractEnName`, `ContractorClientEnName`, `ContractCategory…`, `InsuranceCardNo`); bed `BedMgt.PatientBedTransaction` (`BedID`, `EffectiveClassID`, `RoomGroupID`) → `BedMgt.LKP_Bed` (`ClassID`, `RoomGroupID`, `HospitalStructureID`), floors in `HSM`.
- Permission: "Access NPHIES Portal" (ID 100533, entity Portal). [devtest Security]
- Design banner "More" items: General Patient Info, Medical & social history, Diagnosis, Allergy, Body Measurements, Physician, Financial type, Location, COE, Surgery (+ Vital Signs filtered out); menu has Print Wristband, Attachment, Minimize. [design]
- User rules (2026-11-01): banner = name, gender icon, patient code, ledger icon (MRN, age, gender, DOB, blood group, visit, location, financial: "Cash" or "Insured" + contractor, contract, client); DOB Gregorian with age in brackets; allergy "Not allergic" / "Allergy not documented" / red "Allergy: X +n"; latest weight and height; "COE: X +n"; NPHIES CS button with permission; More panel items each open a popover, except Location: none on OPD/ER, expands to Bed/Class/Room/Floor on IPD. [Confirmed — user]
- Applied 2026-11-01 (41634 rev 9) with all assumptions confirmed: popover contents as in the design; compact banner shows weight and height only (BMI in More); "first" allergy/COE = most recent; Print Wristband, Attachment, Minimize, Scan and Vital Signs item excluded; banner follows the selected visit (visit, location, financial, diagnosis, physician change; allergy, COE, surgery, blood group, history are patient-level); "Not recorded" for missing popover values; module field left as CPOE. [Confirmed — user]
- Banner ⋯ (three dots) menu (user, 2026-11-01): Print wristband (current wristband print dialog), Attachment (current attachment popup), Print summary (current print summary dialog). This reverses the earlier exclusion of Print Wristband and Attachment; Minimize and Scan stay out. Applied 41634 rev 11 (24 ACs). [Confirmed — user]

## Notes drawer (41638) and Consultation reply (52286) — facts verified 2026-11-01

- 41638 "Add note drawer" and 52286 "Consultation reply button" are both module Physician Desktop, parent 41613, empty on 2026-11-01. [ADO]
- No per-note-type permission exists (Security has only "Add Clinic Note" etc.); `CN.SLKP_UserType` 1 Nurse / 2 Doctor is used on `CN.Reply`. How "note types the user can add" is decided today is unverified. [prelive + devtest DB]
- `CN.CNConfiguration` keys: PageSize 6, NoOfReplies 3, TimeToDelete 1440, IsSupportsVoiceDictation, VoiceToTextServiceUrl, ProgressNoteDefaultText / DentalProgressNoteDefaultText (default body templates), VoiceDictationProxyUrl, MedicalVoiceAssistantUrl (URLs — don't copy). [prelive DB]
- Consultation reply in data: `CN.ClinicalNote.OrderlineID` = `CPOE.ConsultationOrderLine.ConsultationLineId`; reply notes are TypeID 3 Consultation Note. Consultation order text = `CPOE.OrderLine.Notes` (OrderLineTypeId 16); request date = `OrderLine.StartDate`/`Order.OrderDate`; requesting physician = `ConsultationDrFromEnName`; consulted doctor = `ConsultationDrToID`. `ConsultationOrderLine.ServiceTransactionId` = the charge. [prelive DB]
- Today, **every InProgress consultation already has a ServiceTransactionId and a note** (1466/1466 since 2026-09) — i.e. the charge happens at perform today, while the user's new rule charges on sign (Complete). Only ~56% of Complete ones have a service transaction. [prelive DB]
- Permission "Undo Perform Consultaion" (500013, Administrative Order) exists. [devtest DB]
- Design: notes drawer = Note type dropdown, section prompts (SOAP…), text area, Save draft, Sign note; consult mode = consultation details on top, "Consultation response" text, Sign reply. [design]
- User rules (2026-11-01): drawer takes 1 column, visible across all portal screens like the control bar, shrinks other screens, closes Episode history; note type list = types the user can access; draft out of scope (say so in the description); on sign, Notes widget refreshes and the Clinical Notes screen refreshes if open. Consultation reply: button appears when the physician can reply to a consultation on the selected visit; shows requesting physician, request date/time, order text, from specialty, free text; Save draft = consultation performed + draft kept; Sign reply = consultation Complete + consultation fees charged. [Confirmed — user]
- Consultation reply: when several eligible consultations exist on the visit, the system always uses the latest one. [Confirmed — user, 2026-11-01]
- Applied 2026-11-01 (41638, 52286) with all assumptions confirmed: note types = what the user can add today in Clinical Notes; optional Title field; default template pre-fill kept; Sign disabled until type + text, drawer closes after sign; Close discards without confirmation; SOAP prompts and voice dictation excluded. Consultation reply: eligible = consulted doctor is the logged-in physician, Ordered/InProgress, latest one used; reply = Consultation Note (type 3) linked by OrderlineID, fixed type; order text = OrderLine.Notes; **charge moves from perform to sign** (Save draft must no longer charge); no other permission/visit checks; empty reply disables both buttons. [Confirmed — user]
