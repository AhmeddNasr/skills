# Gateway: projection schema

## Observed business-flow study

Statement service/diagnosis/lab/vital projections compose insured visit/service/tax, financial contract and report-display mapping for external gateways. Reviewed SumServiceTax filters active insured services with CompanyShare>0 and nondeleted tax; it is not a universal all-visit tax total. Zero rows for selected samples can reflect these filters.

Evidence: WSL_StatementData_Service and SumServiceTax live definitions; projection sample query.

Read samples-bundle.json (schema Gateway) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Gateway) for captured lookup/configuration keys (where present), and sql-objects/Gateway.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

No base tables were visible in this schema. Do not invent insert/delete targets here. Read sql-objects/Gateway.json for column/parameter/dependency contracts. Selected definitions and safe representative samples were reviewed; not all object predicates are individually verified.

| Object | Type | Direct dependency candidates |
|---|---|---|
| ContracotrGatewayMapping | VIEW | Billing.ContractorGateWayMappings |
| DHS_StatementData_Details | VIEW | Gateway.SumServiceTax, Reports.VW_Billing_ProductContractor, Reports.VW_PMGT_Drug, Reports.VW_ProductDetails, VisitMgt.ServiceTreatmentType, VisitMgt.Statement, VisitMgt.VMConfiguration, VisitMgt.Visit, VisitMgt.VisitFinincailInfo, VisitMgt.VisitService |
| DHS_StatementData_Header | VIEW | Gateway.ContracotrGatewayMapping, Gateway.GetVM_ArrivalDate, Reports.PatientProblemUCAFVW, Reports.VWGetLastVitalSignPerVisit, Reports.VW_GetLastPatientandVisitBMIMeasurement, Reports.VW_VM_GetPatientData, VisitMgt.Statement, VisitMgt.Visit, VisitMgt.VisitAdmission, VisitMgt.VisitAppointment, VisitMgt.VisitFinincailInfo, VisitMgt.VisitService, VisitMgt.VisitTriageDetail |
| GetVM_ArrivalDate | VIEW | VisitMgt.Visit, VisitMgt.VisitAdmission, VisitMgt.VisitStatusLog |
| SumServiceAmount | VIEW | VisitMgt.Visit, VisitMgt.VisitService |
| SumServiceTax | VIEW | VisitMgt.ServiceTax, VisitMgt.Visit, VisitMgt.VisitService |
| SumVisitTax | VIEW | VisitMgt.ServiceTax, VisitMgt.Visit, VisitMgt.VisitService |
| ViewStatementDiagnosisComponent | VIEW | PatPrlm.ChiefComplaint, PatPrlm.ProblemCard, PatPrlm.ProblemCardDetail |
| ViewStatementLabComponent | VIEW | Reports.VW_LR_PatientInvestigationResults, VisitMgt.VisitService |
| ViewStatementLabResult | VIEW | Reports.VW_LR_PatientInvestigationResults, VisitMgt.VisitService |
| WSL_LastVitalSignPerVisit | VIEW | VS.VitalSignTransaction |
| WSL_StatementData_GeneralAndInvoice | VIEW | Gateway.ContracotrGatewayMapping, Gateway.GetVM_ArrivalDate, Gateway.SumServiceAmount, Gateway.SumVisitTax, Gateway.WSL_LastVitalSignPerVisit, MPI.Patient, MPI.SLKP_Gender, MPI.SLKP_Nationality, MedStp.Physician, MedStp.SupervisoryLevel, Reports.VM_VW_GetFirstVisitAppointment, Reports.VW_Billing_ContractorClient, Reports.VW_GetLastPatientandVisitBMIMeasurement, Security.Entity, VisitMgt.SLKP_VisitType, VisitMgt.Statement, VisitMgt.Visit, VisitMgt.VisitAdmission, VisitMgt.VisitFinincailInfo, VisitMgt.VisitPatientAccommodation, VisitMgt.VisitService, VisitMgt.VisitStatusLog, VisitMgt.VisitTriageDetail |
| WSL_StatementData_Service | VIEW | Gateway.SumServiceTax, Reports.VW_Billing_ProductContractor, Reports.VW_ProductDetails, Reports.VW_VM_GetVisitPhysicianData, Reports.VW_VM_ReportDisplayMapping, VisitMgt.CashedOrderLine, VisitMgt.DentalChartNotationMapping, VisitMgt.Statement, VisitMgt.VMConfiguration, VisitMgt.Visit, VisitMgt.VisitFinincailInfo, VisitMgt.VisitService |