# Allergy: patient, visit and product review

## Observed business-flow study

Patient-level allergy status and transactions own reaction/history rows. The reviewed save updates status, prevents duplicate allergy entries, replaces reactions on edit and writes deletion history. AllergyID is type-dependent drug/ingredient/allergen context, not a universal product FK. Patient-summary views can display these longitudinal records without a visit-owned transaction.

Evidence: PatientAllergyManagerFactory.SavePatientAllergy161-310; DeletePatientAllergy641-674 (Release-Main).

Read samples-bundle.json (schema Allergy) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Allergy) for captured lookup/configuration keys (where present), and sql-objects/Allergy.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DrugAllergy | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IngredientAllergy | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PatientAllergyHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| PatientAllergyReaction | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PatientAllergyStatus | patient: PatientID | Review ownership | EntityID | 1/0 |
| PatientAllergyTransaction | patient: PatientID | Review ownership | EntityID | 5/2 |
| SLKP_Action | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Allergy | No exact anchor-name candidate | static lookup name | none named EntityID | 1/0 |
| SLKP_AllergyStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AllergyType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_DeletePatientAllergyReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Onset | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Reaction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Severity | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Allergy.json (one level above this folder) for full columns, indexes, defaults and FK mappings.