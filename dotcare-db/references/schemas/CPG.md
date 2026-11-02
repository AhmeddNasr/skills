# CPG: patient, visit and product review

## Observed business-flow study

CPGVisit and CPGVisitNeed represent master treatment-plan visit definitions and their configured needs/products/UOMs. VisitId here refers to CPGVisit.ID, not directly to VisitMgt.Visit. Setup deletion soft-deletes specialties, diagnoses, objectives, physicians, visit definitions and needs. Patient execution must be traced through its CPOE treatment-plan linkage rather than deleting these shared definitions.

Evidence: CPGSetupManagerFactory.DeleteCPG127-195; GetCPGVisits(cpgId); visible FKs and samples.

Read samples-bundle.json (schema CPG) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema CPG) for captured lookup/configuration keys (where present), and sql-objects/CPG.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CDSRule | No exact anchor-name candidate | Review ownership | EntityID | 1/3 |
| CDSRuleCondition | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| CDSRuleLog | patient: PatientID; visit: VisitID | Review ownership | EntityID | 3/0 |
| CDSRuleTrigger | No exact anchor-name candidate | Review ownership | none named EntityID | 3/1 |
| CDSRuleTriggerService | product: ProductID | Review ownership | none named EntityID | 1/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| CPGDiagnosisType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| CPGDisease | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| CPGObjective | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| CPGObjectiveType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| CPGPhysician | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| CPGReferralSpeciality | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| CPGSetup | No exact anchor-name candidate | Review ownership | EntityID | 3/8 |
| CPGSpecialty | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| CPGVisit | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| CPGVisitNeed | visit: VisitId; product: ProductId | Review ownership | EntityID | 9/0 |
| SLKP_CDSPostponeReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChartType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_DiagnosisType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DurationUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/5 |
| SLKP_Need | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_NeedType | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_Objective | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_ObjectiveType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ToothNumber | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_ToothSurface | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TreatmentArea | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Unit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/4 |
| VisitClassification | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/CPG.json (one level above this folder) for full columns, indexes, defaults and FK mappings.