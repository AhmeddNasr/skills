---
name: hmis-data-validation
description: Implement, review, or govern validation for HMIS Medical system user stories and APIs. Use when working on validation rule placement (DTO, Controller, Manager, Repository, Response, Database layers), SaveResult or BillingSaveResultModel mappings, Do/Undo and migration rollback behavior, foreign key or uniqueness checks, source-of-truth governance, backward compatibility, or validation code review across HMIS modules.
---

# HMIS Data Validation

## Purpose

Use this skill as the HMIS Medical validation engineering standard. It governs how to place validation rules, preserve existing module behavior, classify risk, protect API consumers, and review validation output before team adoption.

This skill is portable across Codex, Claude Code, OpenCode, and similar coding agents. Follow the Markdown instructions directly. `agents/openai.yaml` is Codex UI metadata only.

## Non-Negotiable Rules

1. Start from a source of truth: BRD, approved story, API contract, database constraint, existing production behavior, or named business/module owner confirmation.
2. Inspect the target module before writing code. Do not apply an OutPatient pattern to Billing, Notification, CPOE, MPI, or another module without checking the local style.
3. Preserve module architecture, response DTOs, HTTP status codes, message text, SaveResult values, exception behavior, and first-error/all-errors behavior unless explicit approval is documented.
4. Classify each rule by risk before implementation.
5. Decide the validation layer before writing code.
6. Check Do/Undo and migration rollback impact when the flow has state reversal, soft-delete reversal, merge undo, transaction undo, or database constraints.
7. Implement only approved and sufficiently specified High/Critical or compatibility-changing rules.
8. Return a review note that lists source, risk, layer, response impact, Do/Undo impact, tests, and approvals.

## Mandatory Reconnaissance

Before changing validation, answer these questions from the codebase:

| Question | Required check |
| --- | --- |
| Which module family is this? | OutPatient, Billing, BillingEngine, CPOE, NursePortal, Notification, MPI, HospitalStructure, MedicalSetup, or another local module. |
| What response family is used? | SaveResult response DTO, `List<BillingSaveResultModel>`, ModelState, exception, OData, enum failure, or custom payload. |
| Where is similar validation already implemented? | Search DTOs/models, controllers, managers/factories, repositories, enums, response DTOs, migrations, and tests. |
| Does the rule need persisted data? | If yes, keep the decision in Manager/Factory and data access in Repository predicates. |
| Is there a Do/Undo or rollback path? | Inspect `_Do`, `_Undo`, `Undo*`, `SoftDeleteReverted`, merge undo models, `ModifiedTS`, migrations `Up()`/`Down()`. |
| What compatibility surface exists? | API consumers, response messages, status codes, enum values, first-error vs all-errors behavior, exception shape, and integration payloads. |
| Which tests exist? | Unit tests, controller/API tests, integration tests, TDD projects, architecture tests, or manual verification paths. |

## Layer Placement Criteria

| Layer | Put validation here when | Do not put here |
| --- | --- | --- |
| DTO / Model | The rule is intrinsic to the request shape: required, length, range, regex, simple format, or simple cross-field validation without repositories. | Persisted-data checks, workflow state, permissions, clinical policy, billing policy, or external-service checks. |
| Controller | The controller orchestrates validation, calls existing validators/managers, validates nested/list request objects when the local pattern does so, and maps outcomes to the established response contract. | New business decisions, database checks, response schema changes, or changed status codes without approval. |
| Manager / Factory | The rule is business behavior: uniqueness, foreign key existence, workflow state, eligibility, clinical/order/billing/insurance rules, patient identity rules, Do/Undo state checks, or persisted-data checks. | Raw query mechanics that belong in repositories, or response formatting that belongs in controllers/response DTOs. |
| Repository | The rule needs a reusable data-access predicate such as `Exists`, `Any`, `NameExists`, `HasActiveContract`, or update duplicate checks that exclude the current record. | Business policy, SaveResult selection, response messages, validation orchestration, or controller behavior. |
| Database / Migration | The rule must be enforced by schema, unique index, foreign key, constraint, or migration. | User-friendly validation messages or application business decisions. |
| Response | The layer maps validation outcomes to the existing API contract, messages, fields, status codes, enum values, and payload shape. | New validation decisions or breaking consumer changes. |

## Response Family Rules

Preserve the local response family:

| Family | Common examples | Preserve |
| --- | --- | --- |
| SaveResult + response DTO | OutPatient Campaign | Enum numeric values, enum meanings, message mappings, `ProcessIsDoneSuccessfully`, HTTP status behavior. |
| `List<BillingSaveResultModel>` | Billing Contract | Multiple-error behavior, result ordering if consumers rely on it, field names, result model shape. |
| `ModelState.IsValid` + exception | Notification, BillingEngine parts | Exception type, error-code behavior, detailed-vs-generic response behavior. |
| Explicit nested DataAnnotation | CPOE, NursePortal | Parent, child, and collection item validation; do not assume nested collections validate automatically. |
| OData `BadRequest(ModelState)` | Some modular controllers | OData response shape and ModelState behavior. |
| Enum or custom failure payload | NursePortal, BillingEngine | Existing enum values, status fields, and payload contract. |

## Governance Gates

Use `references/governance-and-controls.md` for the full governance model.

- Critical or High risk validation must have source-of-truth evidence and explicit approval from the module technical owner plus QA. Add business owner approval when clinical, patient safety, billing, insurance, patient identity, order, or Do/Undo behavior changes.
- Medium risk validation needs module owner or senior reviewer approval.
- Low risk validation may follow normal code review if it preserves behavior and contracts.
- Any compatibility change, even low risk, requires approval before implementation.
- Any validation affecting Do/Undo, migration rollback, merge reversal, soft-delete reversal, payment/claim reversal, or transaction restoration requires explicit review.

## Boundaries

The skill can:

- Classify validation rules by layer, source, risk, response family, and Do/Undo impact.
- Implement validation using existing HMIS patterns.
- Add focused tests and review checklists.
- Propose approval notes and compatibility impact summaries.
- Recommend where a rule belongs when the source of truth is clear.

The skill must not:

- Redesign module architecture.
- Introduce a new validation framework without architecture approval.
- Change public API response contracts, HTTP status codes, messages, exception types, or payload shape without approval.
- Rename, renumber, or repurpose existing SaveResult values.
- Collapse multiple Billing validation results into a single error.
- Move business rules into DTOs or controllers for convenience.
- Infer clinical, billing, insurance, patient identity, order, payment, claim, or undo policy when no source of truth exists.
- Add validation that blocks undo/recovery without approval.

## Workflow

1. Read the story, API contract, existing module code, and any BRD/business-rule source.
2. Run the mandatory reconnaissance checklist.
3. Build a validation rule table with source, risk, layer, behavior, response family, compatibility impact, Do/Undo impact, tests, and approval status.
4. Load reference files as needed:
   - `references/governance-and-controls.md` for governance, risk, approval, compatibility, QC, and change log rules.
   - `references/hmis-codebase-pattern-map.md` for observed HMIS module families, response styles, and codebase evidence.
   - `references/hmis-validation-patterns.md` for C# implementation patterns and placement guidance.
   - `references/hmis-do-undo-validation.md` for runtime Do/Undo and migration rollback validation rules.
   - `references/hmis-before-after-examples.md` for practical HMIS module examples.
5. Implement only approved and sufficiently specified rules.
6. Preserve existing module style unless an approved change requires otherwise.
7. Verify invalid, valid, update, duplicate, nested/list, response compatibility, and Do/Undo paths where applicable.
8. Return a concise implementation or review summary with risk and compatibility notes.

## Required Output For Reviews

When reviewing or implementing validation, include:

- Source of truth used for each rule.
- Risk level and impacted HMIS flow.
- Chosen layer and why.
- Existing module response family.
- Compatibility impact for API consumers, SaveResult, BillingSaveResultModel, messages, exceptions, and status codes.
- Do/Undo or migration rollback impact.
- Tests run or missing tests.
- Approval needed or approval already present.

## Final Adoption Checklist

- Every rule has a documented source of truth.
- Every rule has a risk classification.
- Validation placement follows the layer criteria.
- Existing module response family is preserved or approved.
- Architecture, response contract, status codes, SaveResult, messages, exceptions, and Do/Undo behavior are preserved or approved.
- QC checklist from `references/governance-and-controls.md` is satisfied.
- Codebase pattern map and before/after examples are used when the change matches an existing HMIS module pattern.
