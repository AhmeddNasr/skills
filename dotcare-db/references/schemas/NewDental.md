# NewDental: patient, visit and product review

## Observed business-flow study

Product/category/procedure mapping plus chart/treatment-area/numbering setup drives patient dental transactions. Add validates active patient treatment areas and applicable procedure mapping, writes audit/visualized status and creates CPOE orders for nonplanned items. Perform can create a VM service for insured state, updates CPOE instance to in-progress, then local status/audit. Planned procedures are not automatically charged services.

Evidence: ProcedureTransactionManagerFactory.AddPatientProcedureTransaction81-188 and PerformProcedureTransaction870-1008; treatment-area cohort samples.

Read samples-bundle.json (schema NewDental) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema NewDental) for captured lookup/configuration keys (where present), and sql-objects/NewDental.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AuditProcedureAction | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ChartSettings | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| DentalCategoryMapping | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| DentalConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| DentalProcedureMapping | No exact anchor-name candidate | Review ownership | EntityID | 2/3 |
| DentalProcedureTreatmentAreaType | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| DentalVisitInfos | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| PatientProcedureTransaction | visit: VisitID | Review ownership | EntityID | 4/1 |
| PatientRadImages | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/0 |
| PatientScreeningChart | patient: PatientID; visit: VisitID | Review ownership | EntityID | 0/1 |
| PatientScreeningChartProcedure | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| PatientTreatmentArea | patient: PatientCode, PatientID | Review ownership | EntityID | 7/2 |
| ScreeningProcedures | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| SLKP_ApprovalLetterStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_BillingApprovalStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_BillingStatusCode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ChartType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_NumberingNotation | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_ProcedureAction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProcedureStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_ToothSurfaceType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_TreatmentArea | No exact anchor-name candidate | static lookup name | none named EntityID | 5/2 |
| SLKP_TreatmentAreaType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_Visualization | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/NewDental.json (one level above this folder) for full columns, indexes, defaults and FK mappings.