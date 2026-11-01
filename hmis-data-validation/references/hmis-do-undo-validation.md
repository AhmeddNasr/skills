# HMIS Do/Undo And Rollback Validation

## Table Of Contents

- Purpose
- Do/Undo categories
- Mandatory checks
- Runtime Do/Undo rules
- Database migration rollback rules
- Risk classification
- Testing expectations
- Review checklist
- Examples

## Purpose

Use this reference when validation can affect a reversible workflow, rollback path, undo operation, merge reversal, soft-delete reversal, billing transaction reversal, or database migration rollback.

Do/Undo validation is a governance gate because a validation rule can be correct for the original operation but harmful when the system must recover or reverse state.

## Do/Undo Categories

| Category | Examples | Validation concern |
| --- | --- | --- |
| Runtime Do/Undo | `_Do`, `_Undo`, `UndoConfirm`, `UndoCancel`, `AddHSBed_Undo`, `DeleteHSBed_Undo` | Validation must not block legitimate recovery or reversal. |
| Soft-delete reversal | `SoftDeleteReverted`, restore/revert states | Validate delete and restore as a pair. |
| Patient merge undo | MPI merge/unmerge, undo confirmation/cancel models | Patient identity and `ModifiedTS` are consistency-sensitive. |
| Billing transaction undo | BillingEngine transaction reversal, payment/claim undo | Financial correctness and audit history are High/Critical. |
| Database migration rollback | `Up()`, `Down()`, unique indexes, constraints | New constraints need rollback and legacy data handling. |

## Mandatory Checks

Before implementing validation in a flow with potential undo:

1. Search for matching Do and Undo methods.
2. Identify the state fields used by both paths.
3. Identify rollback keys, IDs, transaction IDs, merge IDs, and concurrency timestamps such as `ModifiedTS`.
4. Determine whether the new rule applies to Do only, Undo only, or both.
5. Check whether old records may violate the new validation but still need to be undone.
6. Record the approval needed if the rule can block recovery.
7. Test Do and Undo together where feasible.

## Runtime Do/Undo Rules

Do:

- Validate request identity, rollback key, concurrency timestamp, and current state before reversal.
- Preserve local response payload and enum behavior for undo failures.
- Keep audit fields and original state reconstruction intact.
- Treat undo validation in billing, claims, payment, patient identity, merge, and clinical/order flows as High or Critical.
- Add tests for successful Do, failed Do, successful Undo, invalid Undo request, and stale/concurrent Undo when practical.

Do not:

- Add validation to the Do path without checking the Undo path.
- Add validation to the Undo path that blocks recovery because current master data has changed, unless that behavior is approved.
- Require fields in Undo that were not captured or persisted during Do.
- Recalculate business policy during Undo when the intent is to restore prior state, unless the module already does so.
- Convert undo failure response style to another module's pattern.
- Hide or rewrite existing undo status/error codes without compatibility review.

## Database Migration Rollback Rules

When validation requires a database constraint:

1. Add or update the migration in `Up()`.
2. Provide the rollback in `Down()`.
3. Check existing data for violations before adding a non-null, unique, FK, or check constraint.
4. Plan data cleanup or backfill when legacy data violates the new rule.
5. Keep application validation aligned with the database constraint, but do not rely only on database exceptions for user-friendly validation.
6. Get DBA/module owner approval when the constraint affects shared tables, cross-module data, billing, patient, clinical, insurance, or order flows.

Do not:

- Add a unique index without deciding how duplicate legacy rows are handled.
- Remove or relax a constraint without approval.
- Add application-only validation when the rule must be invariant at database level.
- Add database-only validation when users need deterministic SaveResult/message behavior before save.

## Risk Classification

| Flow | Default risk | Notes |
| --- | --- | --- |
| Patient merge/unmerge, MPI identity reversal | High/Critical | Critical when patient identity or merge reversal changes. |
| Billing transaction, claim, payment, refund, contract undo | High/Critical | Critical when amount, claim submission, payment, refund, or authorization behavior changes. |
| Clinical/order state reversal | Critical | Includes CPOE order state, admission/discharge state, medication, allergy, or care-impacting operations. |
| Hospital structure integration undo | Medium/High | High when bed availability, admission routing, or cross-system state is affected. |
| Configuration/master-data rollback | Medium | High when reused by clinical, billing, patient, or integration flows. |
| Pure UI/search/filter undo | Low/Medium | Escalate if persisted state or API contract changes. |

## Testing Expectations

At minimum, document whether each item is tested or not applicable:

- Valid Do succeeds.
- Invalid Do fails with the existing response family.
- Valid Undo succeeds after a successful Do.
- Invalid Undo key or ID fails safely.
- Stale `ModifiedTS` or concurrency mismatch behaves according to module convention.
- Undo remains possible for records created before the new validation, unless approval says otherwise.
- Response status, payload, enum, message, and exception behavior remain compatible.
- Database migration `Up()` and `Down()` both work when DB constraints are involved.

## Review Checklist

Ask these questions in review:

- What operation is being reversed?
- Which persisted state makes Undo possible?
- Does the new validation depend on current master data or original captured data?
- Can legacy records still be undone?
- Does Undo use `ModifiedTS`, row version, status, transaction ID, merge ID, or another concurrency key?
- Does the validation change response behavior for Undo consumers?
- Are Do and Undo covered in tests or manual verification?
- Does a database constraint include rollback and data-cleanup planning?
- Are High/Critical approvals present?

## Examples

### BillingEngine Service Approval

Pattern:

- Do method updates approval state.
- Undo method reverses approval state.
- Validation must preserve both payload and status semantics.

Rule:

- Do not add a service-approval validation that makes `_Undo` impossible for records already approved unless the business owner and module owner approve that behavior.

### MPI Merge Undo

Pattern:

- `UndoConfirm`, `UndoCancelPending`, and `UndoCancelDraft` reverse merge workflow states.
- Undo models include identity and timestamp fields such as `MergeRequestID` and `ModifiedTS`.

Rule:

- Treat patient merge undo as High/Critical. Validate identity and concurrency, but do not infer patient identity policy without approved source of truth.

### HospitalStructure Bed Integration Undo

Pattern:

- Add/delete bed integration flows have undo methods.

Rule:

- Validate Add and Delete with their Undo counterparts. Do not block a bed reversal solely because a current lookup changed unless approved.

### Migration Unique Index

Pattern:

- A unique index is added in `Up()` and removed in `Down()`.

Rule:

- Pair DTO/Manager duplicate validation with the database constraint. Check legacy duplicates before migration, and keep `Down()` rollback explicit.
