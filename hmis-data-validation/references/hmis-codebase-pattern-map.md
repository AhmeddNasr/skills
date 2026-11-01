# HMIS Codebase Pattern Map

## Table Of Contents

- Purpose
- Reviewed roots
- How to use this map
- Module family matrix
- Response family matrix
- Layer evidence
- Pattern search checklist
- Red flags

## Purpose

Use this reference to identify the validation style already used by an HMIS module before implementing or reviewing validation changes.

This map is codebase-grounded. It is based on observed patterns from HMIS Medical monolith branches and the newer modular repositories (Billing, MPI, HospitalStructure, MedicalSetup).

Do not treat these examples as permission to standardize all modules to one style. The correct action is to preserve the local module style unless an approved architecture/API change says otherwise.

## Reviewed Roots

| Root | Role |
| --- | --- |
| `ADS_Medical-branch-Release-Main` | Primary legacy HMIS Medical behavior reference. |
| `BackOffice-Main` | BackOffice, CPOE, Notification, generated/migration-heavy reference. |
| `ADS_Medical` | Comparison branch for HMIS Medical module patterns. |
| Modular service repos | Newer modular services: Billing, MPI, HospitalStructure, MedicalSetup. |

Use module-relative paths in documentation and PR notes when possible. Avoid hardcoding one developer's absolute path inside production guidance.

## How To Use This Map

1. Identify the module and solution.
2. Search for the same entity or operation in DTO/model, controller, manager/factory, repository, enum, response DTO, migration, and tests.
3. Determine the response family before changing validation.
4. Determine whether the flow has Do/Undo, soft-delete reversal, merge undo, transaction undo, or migration rollback.
5. Use the matching pattern reference and examples.

## Module Family Matrix

| Module family | Common validation entry points | Response style | Notes |
| --- | --- | --- | --- |
| OutPatient / OPD | DTO DataAnnotations, controller `DataAnnotation.ValidateEntity`, Manager SaveResult checks, Repository predicates, migrations | SaveResult + response DTO, often `ProcessIsDoneSuccessfully` | Campaign is the strongest full-chain example. Preserve response DTO and SaveResult mappings. |
| Billing | ManagerFactory validation, repository predicates, `BillingSaveResultModel`, controller pass-through | `List<BillingSaveResultModel>` and module-specific payloads | Do not collapse accumulated errors into one SaveResult. Billing validations are High/Critical when amounts, claims, payments, contracts, or insurance are affected. |
| BillingEngine | Controller `ModelState.IsValid`, business/service calls, custom failure payloads, `_Do` / `_Undo` methods | Failure payloads and status fields; not always HTTP 400 | Validate Do and Undo as a pair. Preserve payload fields such as validity/status/message indicators. |
| CPOE | Controller-level DataAnnotation orchestration for parent, nested objects, and collection items | Module-specific response and exception behavior | Clinical/order flows are Critical by default. Nested validation must be explicit. |
| NursePortal | List item validation, `DataAnnotation.ValidateEntity`, module exceptions, enum failure results | Exception plus enum/custom failure behavior | Preserve local exception logging and returned enum semantics. |
| Notification | `ModelState.IsValid`, Notification exceptions, error codes | ModelState/exception family | Do not convert to SaveResult response style without API/architecture approval. |
| MPI | OData or service controllers, merge/undo models, `ModifiedTS`, merge status enums | OData/ModelState or module-specific response | Patient identity and merge undo are High/Critical. Treat rollback keys and timestamps as consistency-sensitive. |
| HospitalStructure | Integration controllers, add/delete undo methods, module managers | Module-specific service response | Validate add/delete and undo paths together. |
| MedicalSetup | Modular service/controller/model patterns | Usually module-specific ModelState/business validation | Inspect local controller and manager style before applying patterns from another module. |

## Response Family Matrix

| Family | Detect by searching for | Preserve |
| --- | --- | --- |
| SaveResult + response DTO | `SaveResult`, `GetSaveResultMessage`, `ProcessIsDoneSuccessfully`, `Request.CreateResponse` | Enum numeric values, meanings, message mapping, response DTO fields, HTTP status behavior. |
| BillingSaveResultModel list | `List<BillingSaveResultModel>`, `saveResult.Add`, `BillingEnums.SaveResult` | Multiple-error collection behavior, field references, order if consumers depend on it, success/failure markers. |
| ModelState + exception | `ModelState.IsValid`, custom `*Exception`, error code constructors | Exception type, error code, detailed-vs-generic response shape, logging style. |
| Explicit nested DataAnnotation | Repeated `DataAnnotation.ValidateEntity` calls for parent/child/list items | Validation order, first-error behavior, nested item coverage. |
| OData ModelState | `ODataController`, `BadRequest(ModelState)` | OData response shape and ModelState behavior. |
| Custom failure payload | `IsValid`, `StatusCode`, `Message`, domain-specific output models | Existing payload contract and consumer-visible status/message fields. |

## Layer Evidence

### DataAnnotation Wrapper

Observed locations include:

- `Core/Utilities/DataAnnotationsValidation/ValidationMechanism.cs`
- `Base/Utilities/DataAnnotations/Base.DataAnnotationsValidation/ValidationMechanism.cs`

The wrapper calls `Validator.TryValidateObject(..., validateAllProperties: true)` for the direct object. It does not remove the need for explicit validation of nested objects and collection items.

### OutPatient Campaign Full Chain

| Layer | Module-relative evidence |
| --- | --- |
| DTO | `OutPatient/Model/OPD.Model/Custom/CampaignDTO.cs` |
| Controller | `OutPatient/Services/OPD.Services/Controllers/CampaignController.cs` |
| Manager | `OutPatient/BL/PSch.BL/PSch.BL/BusinessFlow/Managers/CampaignManager.cs` |
| Repository | `OutPatient/DAL/OPD.DAL/Repositories/CampaignRepository.cs` |
| Migration | `OutPatient/Model/OPD.Model/Migrations/202606081012596_uniqueCampaignNames.cs` |

Use this when a rule has request-shape validation plus persisted uniqueness or FK checks.

### Billing Contract

| Layer | Module-relative evidence |
| --- | --- |
| ManagerFactory | `HMIS.Billing/BL/Billing.BL/ManagersFactory/ContractManagerFactory.cs` |
| Service controller | `HMIS.Billing/Service/Billing.Service/Controllers/ContractController.cs` |
| Tests | `HMIS.Billing/BL/Billing.BL.TDD/ContractTest.cs` |

Use this when a Billing rule needs accumulated business validation results.

### CPOE Nested Validation

Search for repeated `DataAnnotation.ValidateEntity` in:

- `CPOE/Services/CPOE.Service/Controllers/SaveOrderController.cs`

Use this when validating parent, nested child, and collection item models.

### NursePortal List Validation

Search for list item validation and `NursePortalException` in:

- `NursePortal/Service/NP.Service/Controllers/NursePatientOrdersController.cs`

Use this when a list payload must validate every item and preserve module exception behavior.

### Notification ModelState

Search for `ModelState.IsValid` and `NotificationException` in:

- `Notification/Services/NS.Services/Controllers/NotificationController.cs`

Use this when a module already treats invalid input through ModelState and custom exceptions.

### Do/Undo Modular Flows

Search for `_Do`, `_Undo`, `UndoConfirm`, `UndoCancel`, `SoftDeleteReverted`, and `ModifiedTS` in:

- `HMIS.Billing/Service/BillingEngine.Service/Controllers/BillingEngineController.cs`
- `HMIS.MasterPatientIndex/Services/MPI.Service/MPI.Service/Controllers/MergeRequestController.cs`
- `HMIS.HospitalStructure/Services/HS.Services/Controllers/HSBedIntegrationController.cs`
- module enum projects such as `Billing.Enums` and `MPI.Enums`

Use this when validation can affect recovery or state reversal.

## Pattern Search Checklist

Use fast text search first:

- DTO/model: `Required`, `StringLength`, `Range`, `RegularExpression`, `IValidatableObject`.
- Controller: `DataAnnotation.ValidateEntity`, `ModelState.IsValid`, `BadRequest`, `CreateResponse`, custom exceptions.
- Manager/factory: `Validate`, `Check*Validation`, `NameExists`, `TemplateTypeExists`, `SaveResult`, `BillingSaveResultModel`.
- Repository: `Exists`, `Any`, `NameExists`, `ArNameExists`, `EnNameExists`, `excludeId`.
- Response: `ProcessIsDoneSuccessfully`, `Message`, `StatusCode`, `IsValid`, result DTOs.
- Database: `CreateIndex`, `unique`, `ForeignKey`, `Up()`, `Down()`.
- Do/Undo: `_Do`, `_Undo`, `Undo*`, `SoftDeleteReverted`, `ModifiedTS`, transaction IDs, merge IDs.
- Tests: `TDD`, `UnitTests`, `ArchitectureTestRunner`, invalid/valid/duplicate/concurrency test names.

## Red Flags

Stop and ask for approval or clarification when:

- The rule changes clinical order, billing amount, payment, claim, insurance authorization, patient identity, or undo behavior.
- The source of truth conflicts with existing production behavior.
- The change would alter response status, message, enum value, payload shape, or exception type.
- A DTO validation needs repository access.
- A controller starts making business decisions instead of orchestration.
- A repository returns SaveResult or messages instead of data predicates.
- Parent validation is used as a substitute for nested collection item validation.
- A new database constraint lacks migration rollback and data-cleanup planning.
- Billing accumulated errors would be collapsed into one error.
- Do path is changed without reviewing Undo path.
