# Physician schedule migration: OPDPattern

## Scope and use

Choose Medical Setup > Physician schedules - OPD patterns. Download the signed-in template, fill OPD Patterns and upload the workbook. Each row is one recurring schedule with at most two specialties, two visit types, two clinic tags and two procedures. Existing setup must be available first. Housing is excluded. No rooms/beds, appointments, pattern instances, exceptions, temporary schedules or divided-capacity records are imported or pre-generated.

## Input and target mapping

Physician and location accept target business codes or dropdown names/qualified identities. Physician source codes preserved by physician migration can be used. The location is an existing HSM.HospitalStructure; this workflow does not migrate hospital structure. Clinics, queueing models, consultation types, specialties, clinic tags, procedures and outpatient visit types are read from the selected environment. Visit types are restricted to classification 1 and the selected entity. Specialties must be assigned to the physician. Unknown/ambiguous values require correction; no missing lookup is silently invented.

Dates use MM/dd/yyyy. Times use 24-hour HH:mm. Weekdays use distinct SU,MO,TU,WE,TH,FR,SA codes separated by commas. WeekRepeation is the positive number of weeks between occurrences. HasNoEnd=true clears EndDate. Native scheduling permits overnight/end-at-start patterns; the native end-rule calculation is preserved. Capacity must be positive; native OPD enforces its configured capacity/date/concurrency/duplication rules. Historical starts may be rejected by those native rules.

## Save and verification

The adapter reads SerLoc.ServerService.OutPatientServices, validates the route against the environment host/scheme/path and sends api/Pattern/SavePattern with the authenticated HMIS session. It builds weekly recurrence; the native endpoint appends UNTIL. Physician title/display/supervisory/name and specialty caches follow PatternManagerFactory.savePattern. Visit-type/procedure names, resource-manager ID and location color are sourced from current target setup. No HR/user bindings are created.

Before writing, an exact physician/location/start-date/time match is checked. Compatible patterns with matching scalar values, recurrence, child sets and current caches are reused. Conflicts/ambiguous matches are not overwritten. Persisted intent records block automatic retries of unknown native outcomes. A confirmed save with failed verification retains the target identity as SavedNeedsReview and is excluded from correction re-inserts. Invalid unsaved rows export in the same workbook format.

The request supplies the environment MigrationCreatedBy value (default 77777). Native HMIS can override audit values using its own authenticated context. Newly saved pattern/child creators are checked; a mismatch is SavedNeedsReview. Existing creators are preserved. Universal creator override requires an HMIS-supported migration identity contract.

## Validation evidence

- 22 focused checks passed: recurrence, overnight/open-ended dates, required/duplicate values, route trust, parsing, correction round-trip, live lookups and bounded existing-pattern verification.
- Three existing patterns (54371, 54370, 54369) passed checks for scalar/recurrence values, child identities and physician/title/supervisory/location/specialty/visit-type/procedure cached names.
- Existing adapter regression suite: 94 checks passed.
- Spreadsheet exported with no formula errors and visually reviewed.
- All live checks were read-only. No test schedules were created.
- Signed-in native upload acceptance, including whether this deployed HMIS preserves configured CreatedBy, remains pending. Booking generation/availability and external consumers are not certified by local pattern checks.

Source review: OutPatient PatternController.SavePattern; PatternManagerFactory.savePattern; PatternManager.SavePattern; PatternBusinessRulesManager; PhysicianSchedule.js.BuildJsonObject/RecurencdeRoles; MedicalSetup PhysicianManager physician cache projection; VisitManagerFactory.getOPDVisitTypesListModel. Live sample details are in OPDPattern-Sample-Verification.json.
