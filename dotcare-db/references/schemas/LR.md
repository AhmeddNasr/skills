# LR: patient, visit and product review

## Observed business-flow study

Product investigation/component/sample/template setup drives patient/order-instance investigations. Result save checks ModifiedTS concurrency, persists results, attempts completion transition and appends history for successful noncompleted saves. A final-result projection selects result type2 and aggregates the latest result date; IsDeleted<>1 excludes SQL NULL, unlike ISNULL(...,0)=0. Lab/rad/micro and device result branches require their own status guards.

Evidence: InvestigationResultManagerFactory.SaveInvestigationResult186-285; impreports.LR_GetLastFinalInvestigationResultDate; cohort investigation/product links.

Read samples-bundle.json (schema LR) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema LR) for captured lookup/configuration keys (where present), and sql-objects/LR.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AnalyzerProducts | product: ProductId | Review ownership | EntityID | 1/0 |
| AnalyzerTransfareTypes | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| AntibioticSensistivity | product: ProductId | Review ownership | EntityID | 2/1 |
| AntibioticSensistivityResult | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| ArchivedInvestigationHistory | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| Bkp_26480_ComponentUnit | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Bkp_26480_ResultComponentUnit | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CollectionPrinting | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| CollectionSpecimen | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| Comp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ComponentPredefinedValue | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| ComponentReferenceRange | No exact anchor-name candidate | Review ownership | EntityID | 6/0 |
| CompRefRange | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| DifferentialCountConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/1 |
| DonationData | patient: PatientCode, PatientID | Review ownership | EntityID | 1/1 |
| DonorInvestigationsOperationLog | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| ErrorLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| HJHComp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| HJHCompWithNormality | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| IdsForWith | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| InvComp | product: ProductID | Review ownership | EntityID | 0/0 |
| Investigation | patient: PatientID; product: ProductID | Review ownership | EntityID | 5/7 |
| InvestigationAbsoluteConfiguration | product: ProductID | configuration name | EntityID | 0/0 |
| InvestigationCollectionSpecimen | No exact anchor-name candidate | Review ownership | EntityID | 6/0 |
| InvestigationComponent | product: ProductID | Review ownership | EntityID | 5/5 |
| InvestigationComponentAnalyzer | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| InvestigationGroupComponent | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| InvestigationHistory | No exact anchor-name candidate | Review ownership | EntityID | 5/1 |
| InvestigationPerformance | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| InvestigationResult | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| InvestigationResultAudit | No exact anchor-name candidate | Review ownership | none named EntityID | 2/1 |
| InvestigationResultAuditAntibiotic | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| InvestigationResultAuditComponent | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| InvestigationResultComponent | No exact anchor-name candidate | Review ownership | EntityID | 5/1 |
| InvestigationState | No exact anchor-name candidate | Review ownership | none named EntityID | 0/3 |
| InvestigationTemplate | product: ProductID | Review ownership | EntityID | 1/0 |
| LabAnalyzers | No exact anchor-name candidate | Review ownership | EntityID | 1/5 |
| LabIntegrationSwitchableActionLog | product: ProductId | Review ownership | EntityId | 1/0 |
| LabPhraseCategories | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| LabPhrases | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| NameForWithout | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NotifyPerformConfiguration | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| Organism | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| OrganismHJH | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PaymentConfiguration | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| PrintLog | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 2/4 |
| RecollectionReason | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| ReportImagesConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ResultStatusConfiguration | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| SampleDetails | product: ProductID | Review ownership | EntityID | 3/1 |
| SampleDetailsTest | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SampleDetailTubeType | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| SLKP_ActionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AnalyzerStatuses | No exact anchor-name candidate | static lookup name | EntityID | 0/3 |
| SLKP_AntibioticClass | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AntibioticGroup | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AntibioticSensistivity | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_AssignmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_CollectionSpecimentRejectionReason | No exact anchor-name candidate | static lookup name | EntityID | 0/1 |
| SLKP_CollectionSpecimentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_CollectionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ComponentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Configuration | No exact anchor-name candidate | static lookup name | EntityID | 0/0 |
| SLKP_DonationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_DonationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_InvestigationClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_Loinc | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Normality | No exact anchor-name candidate | static lookup name | EntityID | 0/1 |
| SLKP_PerformedType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PrintingModule | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RejectionReasons | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ResultReasons | No exact anchor-name candidate | static lookup name | EntityID | 0/2 |
| SLKP_ResultType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_SampleType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SampleUnit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_StateColors | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_TubeType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_UCUMCode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_UndoReasons | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Unit | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_VisitClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| temp_Migration_Service_with_OrderLine | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| UniversalComponentMapping | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| VisitClassification | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/LR.json (one level above this folder) for full columns, indexes, defaults and FK mappings.