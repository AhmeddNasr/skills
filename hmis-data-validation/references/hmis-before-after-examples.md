# HMIS Before And After Validation Examples

## Table Of Contents

- How to use these examples
- OutPatient Campaign
- Billing Contract
- CPOE nested order validation
- NursePortal list validation
- Notification ModelState validation
- BillingEngine Do/Undo validation
- MPI merge undo validation
- Anti-pattern examples

## How To Use These Examples

Use these examples as implementation shapes based on observed HMIS module patterns.

Before copying any pattern:

1. Confirm the target module already uses the same response family.
2. Confirm the validation source of truth.
3. Confirm risk and approval needs.
4. Confirm compatibility impact.
5. Confirm Do/Undo or migration rollback impact.

These examples are intentionally module-relative. Do not hardcode one developer's absolute path into production code or team standards.

## OutPatient Campaign

Scenario: A campaign requires Arabic name, English name, valid SMS template type, unique names, valid priority, and optional database uniqueness protection.

Observed module-relative files:

- `OutPatient/Model/OPD.Model/Custom/CampaignDTO.cs`
- `OutPatient/Services/OPD.Services/Controllers/CampaignController.cs`
- `OutPatient/BL/PSch.BL/PSch.BL/BusinessFlow/Managers/CampaignManager.cs`
- `OutPatient/DAL/OPD.DAL/Repositories/CampaignRepository.cs`
- `OutPatient/Model/OPD.Model/Migrations/202606081012596_uniqueCampaignNames.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | User story/API contract plus existing OutPatient Campaign behavior and DB migration. |
| Flow | OutPatient / notification campaign configuration. |
| Risk | Medium; escalate to High if campaign delivery affects clinical outreach. |
| Response family | SaveResult + response DTO + `ProcessIsDoneSuccessfully`. |
| Layers | DTO for required/range/length; Controller for orchestration; Manager for FK and uniqueness; Repository for predicates; Database for unique indexes. |
| Compatibility | Preserve response DTO, status behavior, SaveResult meanings, and messages. |

Before:

```csharp
public HttpResponseMessage AddCampaign(CampaignDTO dto)
{
    var result = _campaignManager.AddCampaign(dto);
    return Request.CreateResponse(HttpStatusCode.OK, result);
}
```

Problems:

- DTO annotations may not be triggered.
- Invalid template type may reach business logic.
- Duplicate names may fail late or inconsistently.
- Response contract may not carry the expected module message.

After:

```csharp
public class CampaignDTO
{
    public long? ID { get; set; }

    [Required(ErrorMessage = "Arabic Name is required")]
    [StringLength(250, ErrorMessage = "Arabic Name cannot exceed 250 characters")]
    public string ArName { get; set; }

    [Required(ErrorMessage = "English Name is required")]
    [StringLength(250, ErrorMessage = "English Name cannot exceed 250 characters")]
    public string EnName { get; set; }

    [Required(ErrorMessage = "SMS Template Type ID is required")]
    public long SMSTemplateTypeID { get; set; }

    [Range(0, 3, ErrorMessage = "Invalid priority value")]
    public OPDEnums.CampaignPriority Priority { get; set; }
}
```

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
```

```csharp
public OPDEnums.SaveResult AddCampaign(CampaignDTO campaign)
{
    if (!_smsTemplateTypeRepository.TemplateTypeExists(campaign.SMSTemplateTypeID))
    {
        return OPDEnums.SaveResult.InValidData;
    }

    if (_campaignRepository.EnNameExists(campaign.EnName, campaign.ID))
    {
        return OPDEnums.SaveResult.NameExists;
    }

    if (_campaignRepository.ArNameExists(campaign.ArName, campaign.ID))
    {
        return OPDEnums.SaveResult.ArabicNameExists;
    }

    return OPDEnums.SaveResult.Success;
}
```

QC checks:

- Missing Arabic name returns current validation error style.
- Missing English name returns current validation error style.
- Invalid template ID returns mapped `InValidData` message.
- Duplicate English and Arabic names return distinct results.
- Update duplicate check excludes the current campaign ID.
- Valid campaign still saves.
- Unique index migration has rollback in `Down()`.

## Billing Contract

Scenario: Contract validation includes duplicate names, date rules, active contractor, beneficiary type, maximum amount, references, and concurrency behavior.

Observed module-relative files:

- `HMIS.Billing/BL/Billing.BL/ManagersFactory/ContractManagerFactory.cs`
- `HMIS.Billing/Service/Billing.Service/Controllers/ContractController.cs`
- `HMIS.Billing/BL/Billing.BL.TDD/ContractTest.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | Billing BRD/story plus existing ContractManagerFactory and tests. |
| Flow | Billing contract. |
| Risk | High; Critical if amount, claim, payment, or authorization behavior changes. |
| Response family | `List<BillingSaveResultModel>`. |
| Layers | ManagerFactory for accumulated business validation; Repository for predicates; Controller preserves pass-through result style. |
| Compatibility | Preserve multiple-error behavior, result model, and consumer-visible fields. |

Before:

```csharp
if (_contractRepository.EnNameExists(model.EnName))
{
    return BillingEnums.SaveResult.EnglishNameExists;
}
```

Problems:

- Stops at one error in a module that accumulates validation results.
- May skip Arabic duplicate, date, beneficiary, amount, or reference checks.
- Does not represent the established `BillingSaveResultModel` response family.

After:

```csharp
public List<BillingSaveResultModel> AddContract(ContractDataModel model)
{
    var saveResult = new List<BillingSaveResultModel>();

    bool enNameDuplication;
    bool arNameDuplication;
    bool isStartEndDateValid;
    bool isValidEndDate;

    ContractNameValidation(model, saveResult, out enNameDuplication, out arNameDuplication);
    ContractStartEndDateValidation(model, saveResult, out isStartEndDateValid, out isValidEndDate);
    bool isActiveContractor = ContractContractorValidation(model, saveResult);
    bool isValidBeneficiaryType = BeneficiaryTypeValidation(model, saveResult);
    bool isValidMaxAmount = MaximumAmountValidation(model, saveResult);

    if (!enNameDuplication &&
        !arNameDuplication &&
        isStartEndDateValid &&
        isValidEndDate &&
        isActiveContractor &&
        isValidBeneficiaryType &&
        isValidMaxAmount)
    {
        saveResult.Add(new BillingSaveResultModel(BillingEnums.SaveResult.Success, string.Empty));
    }

    return saveResult;
}
```

QC checks:

- Multiple invalid fields return multiple result models.
- Duplicate checks exclude the current contract during update.
- Date edge cases are covered.
- Maximum amount precision and range are verified against source of truth and database contract.
- No Billing consumer loses expected result values.
- Existing Billing tests are updated or extended.

## CPOE Nested Order Validation

Scenario: An order payload contains a parent request, nested order object, products, diagnoses, or other collection items.

Observed module-relative file:

- `CPOE/Services/CPOE.Service/Controllers/SaveOrderController.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | API contract and CPOE order workflow requirement. |
| Flow | Clinical/order. |
| Risk | Critical. |
| Response family | Existing CPOE response/exception behavior. |
| Layers | Controller for request graph validation orchestration; Manager for clinical/order business rules; Repository for state/existence predicates. |
| Compatibility | Preserve response shape, error ordering, and order state behavior. |

Before:

```csharp
public HttpResponseMessage SaveOrder(OrderInputModel model)
{
    return Request.CreateResponse(HttpStatusCode.OK, _manager.Save(model));
}
```

Problems:

- Parent validation does not guarantee nested object or collection item validation.
- Invalid clinical order data can reach business logic.

After:

```csharp
var validationOrder = DataAnnotation.ValidateEntity(model);
if (validationOrder.HasError)
{
    return BuildCpoeValidationResponse(validationOrder);
}

var validationNestedOrder = DataAnnotation.ValidateEntity(model.OrderObject);
if (validationNestedOrder.HasError)
{
    return BuildCpoeValidationResponse(validationNestedOrder);
}

foreach (var product in model.ListofProducts ?? Enumerable.Empty<ProductModel>())
{
    var validationProduct = DataAnnotation.ValidateEntity(product);
    if (validationProduct.HasError)
    {
        return BuildCpoeValidationResponse(validationProduct);
    }
}
```

QC checks:

- Null parent model is handled according to existing module behavior.
- Null nested object is handled safely.
- Invalid collection item returns expected error style.
- Valid order still reaches Manager.
- Clinical/order state validation is not bypassed.
- Critical approvals are present.

## NursePortal List Validation

Scenario: An endpoint receives a list of performing-detail models and must validate each item.

Observed module-relative file:

- `NursePortal/Service/NP.Service/Controllers/NursePatientOrdersController.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | API contract and existing NursePortal controller behavior. |
| Flow | Clinical/nurse order activity. |
| Risk | High/Critical depending on clinical effect. |
| Response family | DataAnnotation + `NursePortalException` + module enum/custom failure behavior. |
| Layers | Controller validates list items; Manager handles business state; response preserves module enum behavior. |
| Compatibility | Preserve exception logging and returned enum/result semantics. |

Before:

```csharp
public SaveResult LogPerformingDetails(List<LogPerformingDetailViewModel> model)
{
    return _manager.LogPerformingDetails(model);
}
```

After:

```csharp
foreach (var item in model ?? new List<LogPerformingDetailViewModel>())
{
    var validationResult = DataAnnotation.ValidateEntity(item);
    if (validationResult.HasError)
    {
        throw new NursePortalException(validationResult);
    }
}

return _manager.LogPerformingDetails(model);
```

QC checks:

- Every list item is validated.
- Empty/null list behavior matches existing module expectations.
- Exception logging remains consistent.
- Returned enum/failure behavior remains compatible.

## Notification ModelState Validation

Scenario: A Notification endpoint validates required fields through ASP.NET ModelState and throws a module exception.

Observed module-relative file:

- `Notification/Services/NS.Services/Controllers/NotificationController.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | API contract and existing Notification controller behavior. |
| Flow | Notification. |
| Risk | Low/Medium; escalate to High when patient outreach or clinical reminders are affected. |
| Response family | `ModelState.IsValid` + `NotificationException`. |
| Layers | DTO attributes and controller ModelState orchestration. |
| Compatibility | Preserve current exception code/message behavior unless approved. |

Before:

```csharp
if (!ModelState.IsValid)
{
    return BadRequest(ModelState);
}
```

Risk:

- This may expose more detail than the module currently exposes.
- It may change error codes or client parsing.

After, preserving the module family:

```csharp
if (!ModelState.IsValid)
{
    throw new NotificationException("Missing Required Fields", 1000);
}
```

QC checks:

- Required and format errors are covered.
- Exception code remains compatible.
- No sensitive patient or clinical data appears in validation messages.
- The API is not converted to SaveResult style.

## BillingEngine Do/Undo Validation

Scenario: BillingEngine exposes Do and Undo operations for service approval, claims, cancellation, or payment state changes.

Observed module-relative file:

- `HMIS.Billing/Service/BillingEngine.Service/Controllers/BillingEngineController.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | BillingEngine workflow source of truth and existing Do/Undo behavior. |
| Flow | Billing transaction/payment/claim/service state. |
| Risk | High/Critical. |
| Response family | Existing BillingEngine output model/status payload. |
| Layers | Controller validates request shape/ModelState; Manager/service validates business state; Undo validates rollback identity/concurrency. |
| Compatibility | Preserve failure payload, status fields, and undo behavior. |

Before:

```csharp
public OutputModel ServiceApprovalStatus_Do(ApprovalModel model)
{
    return _manager.ServiceApprovalStatus_Do(model);
}
```

Problem:

- A new Do validation can accidentally make the matching Undo impossible for existing records.

After:

```csharp
if (!ModelState.IsValid)
{
    return BuildExistingBillingEngineInvalidRequestPayload();
}

var result = _manager.ServiceApprovalStatus_Do(model);
return result;
```

Undo rule:

```csharp
if (!CanUndoServiceApproval(model.TransactionId, model.ModifiedTS))
{
    return BuildExistingBillingEngineUndoFailurePayload();
}
```

QC checks:

- Valid Do succeeds.
- Invalid Do returns existing failure payload.
- Valid Undo succeeds after Do.
- Invalid rollback key or stale timestamp fails safely.
- Existing records can still be undone unless the approved requirement says otherwise.

## MPI Merge Undo Validation

Scenario: MPI merge workflow has undo actions such as undo confirm or undo cancel.

Observed module-relative files:

- `HMIS.MasterPatientIndex/Services/MPI.Service/MPI.Service/Controllers/MergeRequestController.cs`
- `HMIS.MasterPatientIndex/Model/MPI.Model/MPI.Model/Custom/PatientMerge/MergeRequestModel.cs`

Decision record:

| Field | Value |
| --- | --- |
| Source | MPI merge workflow source of truth and existing models. |
| Flow | Patient identity merge/undo. |
| Risk | High/Critical. |
| Response family | Existing MPI controller response/OData/module style. |
| Layers | Controller request validation; Manager validates merge state, identity, and concurrency. |
| Compatibility | Preserve undo response and patient identity behavior. |

Before:

```csharp
public IHttpActionResult UndoConfirm(UndoConfirmRequestModel model)
{
    return Ok(_manager.UndoConfirm(model));
}
```

After:

```csharp
if (!ModelState.IsValid)
{
    return BadRequest(ModelState);
}

if (!_mergeManager.CanUndoConfirm(model.MergeRequestID, model.ModifiedTS))
{
    return BuildExistingMergeUndoFailureResponse();
}

return Ok(_mergeManager.UndoConfirm(model));
```

QC checks:

- `MergeRequestID` is validated.
- `ModifiedTS` or concurrency field is validated according to module convention.
- Undo does not infer new patient identity policy without approved source.
- Patient merge reversal remains possible for valid historical records.
- High/Critical approvals are present.

## Anti-Pattern Examples

Do not put repository calls in DTO validation:

```csharp
public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
{
    if (_repository.Exists(SMSTemplateTypeID))
    {
        yield return ValidationResult.Success;
    }
}
```

Why this is wrong:

- DTO validation should not depend on data access.
- It violates layer boundaries and is hard to test.

Do not change response contracts for convenience:

```csharp
return Request.CreateResponse(HttpStatusCode.OK, new
{
    errors = validationErrors
});
```

Why this is wrong:

- Existing clients may expect `400 BadRequest`, `Message`, and `ProcessIsDoneSuccessfully`.
- Contract changes require approval.

Do not collapse Billing validation results:

```csharp
return BillingEnums.SaveResult.Failure;
```

Why this is wrong:

- Billing consumers may expect multiple `BillingSaveResultModel` entries.
- Field-level error behavior may be lost.

Do not repurpose SaveResult values:

```csharp
return OPDEnums.SaveResult.NameExists; // Used for invalid template type.
```

Why this is wrong:

- The enum meaning becomes misleading.
- Clients and logs may treat the failure incorrectly.

Do not rely on parent validation for nested items:

```csharp
var validation = DataAnnotation.ValidateEntity(order);
if (!validation.HasError)
{
    Save(order.Products);
}
```

Why this is wrong:

- Direct-object validation may not validate each product item.
- CPOE/NursePortal patterns show explicit item validation.

Do not block Undo with new current-state policy without approval:

```csharp
if (!CurrentPolicyAllowsUndo(model))
{
    return Failure;
}
```

Why this is risky:

- Historical records may need recovery even when current master data changed.
- Undo behavior changes require explicit approval.

Do not guess high-risk rules:

```csharp
if (order.Priority == Critical && patientAge < 18)
{
    return SaveResult.InValidData;
}
```

Why this is wrong:

- Clinical/order rules require approved source of truth and business owner confirmation.
