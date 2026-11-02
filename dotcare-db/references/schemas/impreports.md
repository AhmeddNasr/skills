# impreports: projection schema

## Observed business-flow study

Investigation turnaround/final/cancel timing projections combine LR/CPOE and visit classification. Final-result date view groups by investigation with ResultType2 and IsDeleted<>1; null deletion flags have SQL three-valued behavior. These are derived timing views, not result-write ownership.

Evidence: Live LR_GetLastFinalInvestigationResultDate and VW_VM_GetVisitIdByClassification definitions; safe classification samples.

Read samples-bundle.json (schema impreports) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema impreports) for captured lookup/configuration keys (where present), and sql-objects/impreports.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

No base tables were visible in this schema. Do not invent insert/delete targets here. Read sql-objects/impreports.json for column/parameter/dependency contracts. Selected definitions and safe representative samples were reviewed; not all object predicates are individually verified.

| Object | Type | Direct dependency candidates |
|---|---|---|
| VW_CPOE_RequestedPhysicianOrdersOPD | SQL_STORED_PROCEDURE | CPOE.Order, CPOE.OrderLine, impreports.VW_VM_GetVisitIdByClassification |
| LR_GetLastFinalInvestigationResultDate | VIEW | LR.InvestigationResult |
| VW_CPOE_PatientSummary_LR_Master | VIEW | CPOE.Orders, CPOE.SLKP_ProductClassification, MPI.Patient, MedStp.Physician |
| VW_LR_CPOE_TurnAroundTime_Details | VIEW | ImpReports.VW_LR_CPOE_TurnAroundTime_Master, ImpReports.VW_LR_GetLastInvestigationCancelDate |
| VW_LR_CPOE_TurnAroundTime_Details_RAD | VIEW | ImpReports.VW_LR_CPOE_TurnAroundTime_Master_RAD, ImpReports.VW_LR_GetLastInvestigationCancelDate |
| VW_LR_CPOE_TurnAroundTime_Master | VIEW | LR.Investigation, impreports.LR_GetLastFinalInvestigationResultDate, impreports.VW_CPOE_PatientSummary_LR_Master, reports.VW_LR_GetLastCollectionDate |
| VW_LR_CPOE_TurnAroundTime_Master_RAD | VIEW | LR.Investigation, impreports.LR_GetLastFinalInvestigationResultDate, impreports.VW_CPOE_PatientSummary_LR_Master, itreports.VW_LR_GetLastCollectionDate_RAD |
| VW_LR_GetLastInvestigationCancelDate | VIEW | LR.Investigation |
| VW_VM_GetVisitIdByClassification | VIEW | VisitMgt.SLKP_VisitClassification, VisitMgt.Visit |