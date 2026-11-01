# HMIS Validation Patterns Reference

## Table Of Contents

- How to use this reference
- Requirement classifier
- File locations
- Response-family selection
- DTO and model validation
- DataAnnotation limitations
- Controller validation
- Manager and factory validation
- Repository predicates
- Database validation
- SaveResult and BillingSaveResult guidance
- Exception and ModelState validation
- Common scenarios
- Review checklist

## How To Use This Reference

Implementation patterns in this file are subordinate to `governance-and-controls.md`.

Before applying a pattern:

1. Confirm the source of truth.
2. Identify the target module family.
3. Identify the existing response family.
4. Classify risk and approval needs.
5. Check compatibility and Do/Undo impact.
6. Reuse the nearest local pattern.

Do not standardize all modules to one pattern.

## Requirement Classifier

| User story wording | Validation type | Preferred layer |
| --- | --- | --- |
| `required`, `mandatory`, `cannot be empty` | Required field | DTO/Model attribute |
| `cannot exceed X characters` | String length | DTO/Model attribute |
| `must be between X and Y` | Range | DTO/Model attribute |
| `must match format`, `pattern` | Regex or format validation | DTO/Model attribute |
| `must be unique`, `cannot duplicate` | Unique persisted value | Manager/Factory plus Repository predicate, optionally Database unique constraint |
| `must exist in ...` | Foreign key or lookup existence | Manager/Factory plus Repository predicate |
| `cannot be in state ...` | Workflow state validation | Manager/Factory |
| `depends on another field` | Cross-field rule | DTO `IValidatableObject` if local-only; Manager/Factory if data-backed |
| `date before/after` | Cross-property date rule | DTO `IValidatableObject` if local-only; Manager/Factory if policy/data-backed |
| `cannot undo when ...` | Undo state or concurrency rule | Manager/Factory or service layer matching the module pattern |
| `must be enforced in database` | Invariant or data integrity rule | Database migration plus application validation if user-friendly response is needed |

## File Locations

Legacy HMIS modules commonly use:

| Component | Location pattern |
| --- | --- |
| DTOs | `{Module}/Model/{Module}.Model/Custom/{Entity}DTO.cs` |
| Controllers | `{Module}/Services/{Module}.Services/Controllers/{Entity}Controller.cs` |
| Managers | `{Module}/BL/{Module}.BL/BusinessFlow/Managers/{Entity}Manager.cs` |
| Repositories | `{Module}/DAL/{Module}.DAL/Repositories/{Entity}Repository.cs` |
| Enums | `{Module}/Utilities/{Module}.Enums/{Module}Enums.cs` |
| Validation mechanism | `Core/Utilities/DataAnnotationsValidation/ValidationMechanism.cs` |
| Base exception | `Core/Utilities/Exception/Infrastructure/BaseException.cs` |

Newer modular services commonly use:

| Component | Location pattern |
| --- | --- |
| BL managers/factories | `{Product}/BL/{Product}.BL/Managers*` |
| DAL repositories | `{Product}/DAL/{Product}.DAL/*` |
| Models | `{Product}/Model/{Product}.Model/*` |
| Service controllers | `{Product}/Service/{Product}.Service/Controllers/*` |
| Unit tests | `{Product}/UnitTests/*` or `{Product}/BL/*.TDD/*` |
| Architecture tests | `{Product}/UnitTests/*ArchitecturesUnitTests/*ArchitectureTestRunner.cs` |

## Response-Family Selection

Always preserve the local response family.

| Response family | Use when existing module already uses | Implementation posture |
| --- | --- | --- |
| SaveResult + response DTO | `SaveResult`, `GetSaveResultMessage`, `ProcessIsDoneSuccessfully` | Keep enum meanings and message/status mapping. |
| Billing result list | `List<BillingSaveResultModel>` | Accumulate validation results; do not collapse to one error. |
| ModelState + exception | `ModelState.IsValid`, custom `*Exception` | Preserve exception type/code and response detail level. |
| Explicit nested DataAnnotation | Multiple `DataAnnotation.ValidateEntity` calls over child/list models | Validate every required nested object/item explicitly. |
| OData ModelState | `ODataController`, `BadRequest(ModelState)` | Preserve OData response shape. |
| Custom payload | `IsValid`, `StatusCode`, domain output models | Preserve payload contract and consumer-facing fields. |

## DTO And Model Validation

Use DTO/model attributes for intrinsic request-shape rules.

```csharp
[Required(ErrorMessage = "{FieldName} is required")]
public string FieldName { get; set; }

[StringLength(250, ErrorMessage = "{FieldName} cannot exceed {1} characters")]
public string FieldName { get; set; }

[Range(1, long.MaxValue, ErrorMessage = "{FieldName} must be a positive number")]
public long FieldName { get; set; }

[RegularExpression(@"^\d+(\.\d{1,3})?$", ErrorMessage = "Must be Decimal (18,3)")]
public decimal Amount { get; set; }

[EmailAddress(ErrorMessage = "Invalid email format")]
public string Email { get; set; }
```

Use `IValidatableObject` only for local cross-field rules that do not need database access.

```csharp
public class ContractDTO : IValidatableObject
{
    public DateTime? StartDate { get; set; }
    public DateTime? EndDate { get; set; }

    public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
    {
        if (StartDate.HasValue && EndDate.HasValue && StartDate >= EndDate)
        {
            yield return new ValidationResult(
                "Start date must be before end date",
                new[] { nameof(StartDate), nameof(EndDate) });
        }
    }
}
```

Do not inject repositories or services into DTO validation.

## DataAnnotation Limitations

Observed HMIS wrappers call `Validator.TryValidateObject` for the direct object.

Implications:

- Parent validation does not automatically prove all nested objects and collection items are valid.
- CPOE and NursePortal show explicit validation of nested/list payloads.
- If the API contract requires nested validation, validate each nested object or item in the controller or an approved shared validator, matching the local module style.

Example nested validation shape:

```csharp
var parentValidation = DataAnnotation.ValidateEntity(model);
if (parentValidation.HasError)
{
    return BuildValidationResponse(parentValidation);
}

foreach (var item in model.Items ?? Enumerable.Empty<ItemModel>())
{
    var itemValidation = DataAnnotation.ValidateEntity(item);
    if (itemValidation.HasError)
    {
        return BuildValidationResponse(itemValidation);
    }
}
```

Use the module's actual response builder, not a generic helper, unless the module already has one.

## Controller Validation

Controllers should orchestrate validation and preserve response contracts.

SaveResult response DTO pattern:

```csharp
var validationResult = DataAnnotation.ValidateEntity(dto);
if (validationResult.HasError)
{
    response.Message = validationResult.ValidationErrors
        .Select(v => v.ErrorMessage)
        .FirstOrDefault();
    response.ProcessIsDoneSuccessfully = false;
    return Request.CreateResponse(HttpStatusCode.BadRequest, response);
}

var result = _manager.Add(dto);
response.Message = GetSaveResultMessage(result);
response.ProcessIsDoneSuccessfully = result == ModuleEnums.SaveResult.Success;

return Request.CreateResponse(
    response.ProcessIsDoneSuccessfully ? HttpStatusCode.OK : HttpStatusCode.BadRequest,
    response);
```

ModelState pattern:

```csharp
if (!ModelState.IsValid)
{
    throw new NotificationException("Missing Required Fields", 1000);
}
```

OData pattern:

```csharp
if (!ModelState.IsValid)
{
    return BadRequest(ModelState);
}
```

Controller rules:

- Keep business decisions in Manager/Factory.
- Keep database predicates in Repository.
- Do not change `BadRequest` to `OK` with failure payload, or the reverse, unless approved.
- Do not add detailed validation errors when the existing API intentionally returns generic errors unless approved.

## Manager And Factory Validation

Use Manager/Factory validation for business and persisted-data rules.

Single SaveResult style:

```csharp
public OPDEnums.SaveResult AddCampaign(CampaignDTO campaign)
{
    if (!_smsTemplateTypeRepository.TemplateTypeExists(campaign.SMSTemplateTypeID))
    {
        return OPDEnums.SaveResult.InValidData;
    }

    if (_campaignRepository.EnNameExists(campaign.EnName))
    {
        return OPDEnums.SaveResult.NameExists;
    }

    if (_campaignRepository.ArNameExists(campaign.ArName))
    {
        return OPDEnums.SaveResult.ArabicNameExists;
    }

    // Existing mapping and save logic.
    return OPDEnums.SaveResult.Success;
}
```

Billing accumulated result style:

```csharp
public List<BillingSaveResultModel> AddContract(ContractDataModel model)
{
    var saveResult = new List<BillingSaveResultModel>();

    bool enNameDuplication;
    bool arNameDuplication;

    ContractNameValidation(model, saveResult, out enNameDuplication, out arNameDuplication);
    bool isValidBeneficiaryType = BeneficiaryTypeValidation(model, saveResult);
    bool isValidMaxAmount = MaximumAmountValidation(model, saveResult);

    if (!enNameDuplication &&
        !arNameDuplication &&
        isValidBeneficiaryType &&
        isValidMaxAmount)
    {
        saveResult.Add(new BillingSaveResultModel(BillingEnums.SaveResult.Success, string.Empty));
    }

    return saveResult;
}
```

Manager/Factory rules:

- Return the module's existing result type.
- Preserve single-error or multiple-error behavior.
- Keep validation ordering when consumers/tests rely on it.
- For update uniqueness checks, pass the current ID to exclude the current row.
- Do not format HTTP responses here.

## Repository Predicates

Repositories should answer data questions only.

```csharp
public bool EnNameExists(string enName, long? excludeId = null)
{
    var normalizedName = enName.Trim().ToLower();

    return _dbSet.Any(a =>
        !a.IsDeleted &&
        a.EnName.Trim().ToLower() == normalizedName &&
        (!excludeId.HasValue || a.ID != excludeId.Value));
}
```

Repository rules:

- Keep predicates side-effect free.
- Return booleans or data needed by Manager/Factory.
- Do not return SaveResult, messages, HTTP status, or response DTOs.
- Normalize values consistently with the local module.
- Preserve current-record exclusion on update duplicate checks.

## Database Validation

Use database constraints when the rule must be invariant at the data layer.

Examples:

- Unique index for a name that must never duplicate.
- Foreign key for a required relationship.
- Non-null or check constraint for critical invariants.

Rules:

- Add migration `Up()` and rollback `Down()`.
- Check legacy data before adding constraints.
- Pair database constraints with application validation when users need friendly errors.
- Do not remove or relax constraints without approval.

## SaveResult And BillingSaveResult Guidance

### SaveResult

When adding validation errors:

1. Reuse an existing enum value only if it has the exact meaning.
2. Add a new enum value only when reuse would be misleading.
3. Add controller response mapping for every new Manager result.
4. Keep numeric values stable.
5. Test both message mapping and status behavior.

### BillingSaveResultModel

When adding Billing validation:

1. Add to the existing `List<BillingSaveResultModel>`.
2. Preserve accumulated error behavior.
3. Include field names when the module convention does so.
4. Preserve `Success` behavior and only add it when all validations pass.
5. Add/update tests for all invalid and valid combinations.

## Exception And ModelState Validation

Use exception-based validation only when the module already follows that pattern.

```csharp
var validationResult = DataAnnotation.ValidateEntity(model);
if (validationResult.HasError)
{
    throw new ModuleException(validationResult);
}
```

```csharp
catch (ModuleException ex)
{
    LogFactory<Controller>.LogException(ex);
    return Request.CreateResponse(HttpStatusCode.BadRequest, new { Message = ex.Message });
}
```

Rules:

- Preserve exception type and code.
- Preserve logging style.
- Preserve generic vs detailed response behavior.
- Do not convert exceptions to SaveResult or response DTOs without approval.

## Common Scenarios

| Scenario | Preferred implementation |
| --- | --- |
| Required field | DTO `[Required]` and existing controller validation trigger. |
| Max length | DTO `[StringLength]`, optionally DB max length alignment. |
| Numeric range | DTO `[Range]`, Manager if policy/data-backed. |
| Decimal precision | DTO regex or custom local validator, DB precision alignment when needed. |
| Duplicate name | Manager calls Repository `NameExists`, update excludes current ID, optional unique index. |
| Foreign key existence | Manager calls Repository/lookup predicate. |
| Invalid workflow state | Manager/Factory validates current persisted state. |
| Nested list item invalid | Controller or approved shared validator loops items and preserves response style. |
| Billing amount rule | ManagerFactory validation with `BillingSaveResultModel`, High/Critical risk. |
| Clinical order rule | CPOE/clinical Manager or controller orchestration per existing style, Critical risk. |
| Undo validation | Use `hmis-do-undo-validation.md`; validate Do and Undo together. |

## Review Checklist

Before implementation:

- Extract every validation requirement from the story.
- Identify source of truth and risk.
- Identify module family and response family.
- Separate field/format validation from business validation.
- Search for existing validation in the same module.
- Resolve missing limits, messages, status behavior, and approval needs.

During implementation:

- Place format validations on DTO/model.
- Place FK, uniqueness, state, Do/Undo, and persisted-data rules in Manager/Factory.
- Use Repository predicates for data checks.
- Reuse or extend SaveResult/BillingSaveResult values carefully.
- Follow single-error, multiple-error, ModelState, exception, OData, or custom payload behavior from the module.
- Log exceptions with the local logging pattern.

After implementation:

- Confirm validation runs before save/business side effects.
- Test valid and invalid data.
- Test create and update flows.
- Test nested/list payloads where applicable.
- Test Do/Undo where applicable.
- Check response status codes, messages, enum values, exceptions, and payload shape.
- Confirm update duplicate checks exclude the current record.
- Confirm architecture tests when validation dependencies or layers changed.
