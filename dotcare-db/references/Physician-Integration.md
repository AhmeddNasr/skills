# MedStp physician migration

Implemented scope: physician records of all types, with contacts, qualifications and specialties on the same Excel row. The physician type is preserved through `IsExternal` and `IsEmployee`; importing these flags does not provision an employee, user, login or user binding.

## Entry and execution

Choose **Physicians - all types, contacts and specialties** in Medical Setup. The existing combined Medical Setup workbook also uses this adapter for its Physician sheet. Download while signed in to refresh the target lookup lists.

- Code and Arabic/English first and second names are required, as are a supervisory level and a main specialty.
- Up to two contacts, two qualifications and two specialties are accepted. Exactly one specialty must be main. At most one supplied contact is primary.
- Title, gender, contact type, qualification type, supervisory level and specialty resolve against the selected environment. Static lookup IDs are not fabricated.
- `NationalId`, `LicenseNumber`, marketing text, HealthID, exclusivity and supervisor fields are included. NPHIES is used only for environments configured as KSA.
- `IsActive=true`, `IsDeleted=false`, `IsDraft=false`, entity scope, audit values and SQL identity IDs are generated internally. Blank SourceRecordID receives a stable staging key.
- Supervisor links can use another physician source row or an existing target code/name. Parents are processed first. Self-links and cycles are rejected. The target supervisor must be active, in the current entity, marked as a supervisor and share a specialty.

Each physician and its supplied owned records is committed in one SQL transaction. A failed child insert rolls back the aggregate. Application locks and serializable code matching protect concurrent migration writes. Existing compatible code/entity records are reused; conflicting master setup is not overwritten. Compatible child records are reused by their logical fields; missing supplied child records can be added. Existing conflicting main/primary assignments require review.

The adapter records actual IDs for MedStp.Physician, MedStp.PhysicianContact, MedStp.PhysicianQualifier and MedStp.PhysicianSpecialty. Invalid rows retain their related values in the correction export. A lost commit acknowledgement is recorded as unknown; a retry verifies the code and compatible data instead of assuming a failed insert.

## Dependencies and later module data

Reviewed against the target schema and the compiled MedicalSetup physician models, PhysicianManager validation and repository code. The legacy `SaveExternalPhysician` endpoint forces external/nonemployee flags and does not assign NationalId or LicenseNumber. Its Resource Manager creation is commented out. The new database adapter therefore preserves all requested physician types in MedStp without that endpoint changing them.

Physician contacts, qualifications and specialty links belong to this migration. HR records and Security.UserPhysician are explicitly excluded at the user's request. ResourceManagerID and signature attachments are outside this workbook and are rejected if supplied through the combined legacy layout.

Scheduling is a separate next step. OPD patterns and housing contain physician, title, supervisory and specialty cache fields that must be populated through the scheduling workflow when schedules are migrated. This physician import does not manufacture schedule, visit, order or historical clinical rows to populate those caches. Existing unrelated records are not rewritten. Hospital setup remains deferred.

## Verification

Focused checks cover type preservation, flags, identity/license fields, KSA filtering, actual contact lookup mapping, main specialty constraints, email validation, duplicate specialties, supervisor ordering/cycles, source identity maps, consolidated workbook parsing and correction round-trips. Read-only AHJ Prelive checks verify existing physician/specialty samples, lookup availability and the live target columns. Native UAT insertion has not been exercised with a signed-in user during this implementation; perform a small authenticated upload before a bulk import.
