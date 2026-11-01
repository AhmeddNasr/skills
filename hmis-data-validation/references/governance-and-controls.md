# HMIS Validation Governance And Controls

## Table Of Contents

- Governance metadata
- Change log
- Source of truth
- Validation decision record
- Risk classification
- Approval flow
- Do and do not rules
- Backward compatibility rules
- Do/Undo governance
- QC checklist
- Code review checklist
- Release readiness

## Governance Metadata

Keep this section current when the skill is adopted by the team.

| Field | Value |
| --- | --- |
| Skill name | `hmis-data-validation` |
| Current version | `0.3.0-codebase-grounded` |
| Status | Draft engineering standard for team review |
| Owner | HMIS Engineering Team |
| Accountable approver | Engineering governance owner or module technical owner |
| Required reviewers | Module owner, QA owner, and business owner for High/Critical or compatibility-changing rules |
| Applies to | HMIS validation changes across DTO, Controller, Manager/Factory, Repository, Response, Database, Do/Undo, and API behavior |
| Does not replace | BRD, CR, approved user story, API contract, database constraints, clinical/billing/insurance policy, code review, QA sign-off, or architecture approval |

## Change Log

| Version | Date | Change | Approval |
| --- | --- | --- | --- |
| `0.1.0` | 2026-06-22 | Initial POC with implementation patterns and examples. | Draft |
| `0.2.0-governance-draft` | 2026-07-01 | Added governance gates, source-of-truth rules, risk classification, approval flow, compatibility controls, and QC checklist. | Draft |
| `0.3.0-codebase-grounded` | 2026-07-01 | Added codebase reconnaissance, HMIS response-family matrix, Do/Undo governance, migration rollback checks, module pattern map, and real HMIS examples. | Pending team review |

Do not create a separate change-log document. Keep governance history here so the skill remains compact.

## Source Of Truth

Use this priority order when rule sources conflict:

1. Approved regulatory, clinical safety, legal, or compliance requirement.
2. Signed BRD, CR, or business rules document.
3. Published API contract or integration agreement.
4. Database constraint, schema requirement, migration, or known data invariant.
5. Existing production behavior in the same module and response family.
6. Approved user story acceptance criteria.
7. Written confirmation from business owner, product owner, module owner, or architect.
8. Existing behavior in a neighboring HMIS module only when the target module has no local pattern and the module owner agrees.

If the source is missing, ambiguous, or conflicting, stop before implementing High/Critical validation or compatibility-changing behavior.

For Low and Medium validation, proceed only when the behavior can be safely inferred from the target module's existing code and does not change contracts, Do/Undo behavior, or persisted business outcome.

## Validation Decision Record

Before implementation, create a short decision record in the task notes or PR description.

| Field | Required content |
| --- | --- |
| Rule ID | Stable short name, such as `CampaignTemplateTypeExists`. |
| Source | BRD section, story ID, API contract, DB constraint, migration, existing code path, or named owner confirmation. |
| Module family | OutPatient, Billing, BillingEngine, CPOE, NursePortal, Notification, MPI, HospitalStructure, MedicalSetup, or other. |
| Flow | Clinical, billing, patient identity, insurance, order, configuration, notification, integration, Do/Undo, or other. |
| Risk | Critical, High, Medium, or Low. |
| Layer | DTO/Model, Controller, Manager/Factory, Repository, Response, Database, or shared validator. |
| Response family | SaveResult DTO, `BillingSaveResultModel`, ModelState, exception, OData, enum/custom payload, or other. |
| Behavior | What fails, when it fails, validation order, and what valid input looks like. |
| Response | SaveResult, message, response DTO fields, HTTP status, exception, payload status, or result model. |
| Do/Undo impact | Not applicable, Do only, Undo only, both, migration rollback, or unknown. |
| Compatibility | No change, additive, behavior change, contract change, message change, status-code change, enum change, exception change, or undo behavior change. |
| Approval | Not needed, reviewer required, module owner required, QA required, business owner required, architecture approval required, or blocked pending clarification. |
| Tests | Unit, controller/API, integration, architecture, migration, Do/Undo, regression, or manual verification. |

## Risk Classification

Use the highest applicable risk. Escalate one level when a rule affects multiple modules, integrations, batch jobs, reports, migrations, response contracts, Do/Undo, or backward compatibility.

| Risk | Applies when | Required control |
| --- | --- | --- |
| Critical | Patient safety, clinical orders, medication, allergies, admission/discharge eligibility, order state transitions, patient identity merge/unmerge, care-affecting insurance authorization, billing amount/claim/payment/refund correctness, or irreversible workflow blocking. | Approved source of truth, module owner approval, QA approval, business owner approval, regression tests for valid/invalid/undo paths. |
| High | Patient demographics, MPI, insurance eligibility, billing contracts, pricing, claims, payments, order status, clinical workflow state, Do/Undo recovery, shared configuration, or integration-facing validation. | Approved source of truth, module owner approval, QA review, focused regression tests. |
| Medium | Master data, configuration, lookup validity, uniqueness, non-critical status transitions, notification routing, or validation that affects operational workflow but not safety/financial correctness. | Module owner or senior reviewer approval, focused tests. |
| Low | Field shape validation, display-friendly messages, optional metadata, non-critical search/filter validation, or validation that cannot alter persisted business outcome or response contract. | Normal code review and smoke test. |

## Approval Flow

1. Classify the rule and compatibility impact.
2. Identify the module family and response family.
3. Identify required reviewers from the risk table.
4. Document the source of truth and expected behavior.
5. Inspect Do/Undo and migration rollback impact.
6. Implement only after required approval exists for High/Critical or compatibility-changing rules.
7. Ask reviewers to verify both the rule and the placement layer.
8. Record final approval in the PR, task, release note, or team-approved tracking system.

Approval is required before changing:

- Public API response schema.
- HTTP status codes.
- SaveResult numeric values or meanings.
- `BillingSaveResultModel` shape, ordering, or multiple-error behavior.
- Existing response message text consumed by clients or tests.
- Exception type, exception code, or error detail level.
- Workflow state transitions.
- Do/Undo behavior, soft-delete reversal, merge reversal, transaction reversal, or migration rollback.
- Billing, claim, payment, refund, insurance, order, clinical, or patient identity behavior.
- Database constraints or repository semantics shared by other modules.

## Do And Do Not Rules

Do:

- Use the target module's existing patterns before adding new abstractions.
- Keep DTO validation limited to intrinsic request shape.
- Keep Manager/Factory validation responsible for business rules.
- Keep Repository methods as data-access predicates, not business policy.
- Keep Controllers focused on orchestration, nested/list request validation when local style requires it, and response mapping.
- Preserve old behavior unless the approved requirement explicitly changes it.
- Add regression tests around changed validation paths.
- Validate update uniqueness checks with current-record exclusion.
- Validate Do and Undo together when applicable.

Do not:

- Move validation into a layer only because it is easier to code.
- Introduce a new validation framework without architecture approval.
- Return a different response DTO shape unless the API contract changed.
- Collapse multiple SaveResult or BillingSaveResult values into a generic result when callers distinguish them.
- Treat database constraints as a substitute for user-friendly validation.
- Guess clinical, billing, insurance, patient identity, payment, claim, order, or undo rules.
- Change validation ordering when clients depend on first-error behavior.
- Convert one module's response style into another module's style without approval.

## Backward Compatibility Rules

### SaveResult

- Do not change numeric values of existing enum members.
- Do not rename or repurpose existing members if serialized, logged, returned, or consumed by clients.
- Add new values at the end unless the module has a different established convention.
- Map every new result to a controller message and test it.
- Do not reuse `InValidData`, `NameExists`, or similar broad values for a different meaning when a specific value exists or is required.

### BillingSaveResultModel

- Preserve multiple-error behavior unless approved.
- Preserve field names and result codes consumed by UI/API clients.
- Treat result ordering as compatibility-sensitive when tests or clients rely on it.
- Do not replace a result list with a single enum or exception without architecture/API approval.

### Response Messages

- Preserve existing message text when clients, tests, reports, or integrations may depend on it.
- If improving wording, confirm no client parses or snapshots the message.
- Avoid leaking sensitive patient, clinical, insurance, billing, or internal data in validation messages.

### HTTP Status Codes

- Keep existing status codes for existing failure modes.
- Treat status-code changes as API contract changes.
- Validate whether the module uses `400 BadRequest`, exceptions, `200 OK` with failure payload, OData `BadRequest(ModelState)`, or another established pattern.

### API Consumers

- Check mobile apps, portals, integrations, reports, batch jobs, and downstream modules when changing validation behavior.
- Preserve first-error vs all-errors behavior unless approved.
- Preserve create/update behavior differences unless the story explicitly unifies them.
- Preserve detailed-vs-generic validation response behavior.

### Database

- Do not remove or relax database constraints without DBA/module owner approval.
- Add database constraints only with migration, rollback, and data-cleanup planning.
- Keep application validation aligned with database invariants when user-friendly errors are required.

## Do/Undo Governance

Use `hmis-do-undo-validation.md` when any validation touches:

- `_Do` / `_Undo` methods.
- `UndoConfirm`, `UndoCancel`, or other `Undo*` operations.
- `SoftDeleteReverted` or restore/revert status.
- Transaction, payment, claim, service approval, merge, bed integration, or order reversal.
- `ModifiedTS`, row version, merge ID, transaction ID, or rollback key.
- Migration `Up()` / `Down()`.

Rules:

- Review the Undo path before changing the Do path.
- Do not block recovery for historical records unless approved.
- Do not add required Undo input that was not captured by the Do path.
- Do not apply current master-data policy during Undo unless the module already does so or the requirement explicitly says so.
- Test Do and Undo as a pair when feasible.

## QC Checklist

Before marking validation implementation complete:

- Each validation rule has a source of truth.
- Each rule has a risk level.
- Each rule has a module family and response family.
- Each rule is assigned to the correct layer.
- Controller response behavior matches the module contract.
- Manager/Factory rules cover all persisted-data checks.
- Repository predicates are reusable and side-effect free.
- SaveResult or BillingSaveResultModel values are reused or extended safely.
- Create and update flows are both checked.
- Duplicate checks exclude the current record on update.
- Nested objects and collection items are explicitly validated when required.
- Null, empty, whitespace, boundary length, min/max, invalid FK, duplicate, invalid state, stale concurrency, and invalid undo cases are tested where applicable.
- Valid data still saves successfully.
- Existing behavior that is not part of the story remains unchanged.
- Logs follow the module pattern.
- Do/Undo or migration rollback impact is tested or documented as not applicable.
- Tests or manual verification evidence are listed in the PR/task.

## Code Review Checklist

Ask these questions in review:

- Is the rule backed by an approved source?
- Is the target module's local style identified?
- Is the risk classification correct?
- Is the validation in the right layer?
- Did the change alter architecture, response shape, message text, status code, exception behavior, SaveResult, BillingSaveResultModel, or Do/Undo behavior?
- Are API consumers protected from breaking changes?
- Are High/Critical approvals present?
- Are tests focused on invalid, valid, update, and regression paths?
- Does the implementation follow the module's existing single-error or multiple-error style?
- Are nested/list request objects validated where the local pattern requires it?
- Are exception paths logged consistently?
- Are database constraints paired with application validation, migration rollback, and data cleanup where needed?
- Are before/after examples or existing module patterns referenced when relevant?

## Release Readiness

A validation change is ready to share or release when:

- Required approvals are recorded.
- Compatibility impact is understood.
- Regression tests pass or manual verification is documented.
- Do/Undo and migration rollback are tested or explicitly not applicable.
- API contract updates are made when approved contract changes exist.
- Business owner sign-off exists for clinical, billing, insurance, patient identity, and order behavior changes.
- DBA/module owner approval exists for database constraint changes.
