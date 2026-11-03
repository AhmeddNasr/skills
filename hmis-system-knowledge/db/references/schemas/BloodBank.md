# BloodBank: patient, visit and product review

## Observed business-flow study

Patient donation and blood-unit inventory are distinct from a visit blood order and dispense transaction. Product/component/type/UOM/warehouse configuration drives unit handling. Reviewed dispense guards order status, returned state and expiry; expiry can discard the unit and conditionally add an investigation service, with transaction logging. Full compatibility, return and witness branches need targeted review.

Evidence: BloodUnitManagerFactory.DispenseBloodUnit921-1007; sample BloodUnit36 and order/log patient/visit anchors.

Read samples-bundle.json (schema BloodBank) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema BloodBank) for captured lookup/configuration keys (where present), and sql-objects/BloodBank.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BloodOrder | patient: PatientCode, PatientID; visit: VisitID; product: ProductID | Review ownership | EntityID | 2/2 |
| BloodOrderTransaction | No exact anchor-name candidate | Review ownership | EntityID | 7/4 |
| BloodOrderTransactionVisualInspection | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| BloodOrderTransactionWitnessStep | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| BloodProcess | No exact anchor-name candidate | Review ownership | none named EntityID | 2/1 |
| BloodProcessGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| BloodProduct | product: ProductID | Review ownership | EntityID | 2/1 |
| BloodTransactionLog | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 1/0 |
| BloodTransactionTag | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| BloodUnit | patient: PatientCode; product: ProductID | Review ownership | EntityID | 6/1 |
| BloodUnitInvestigationConfig | No exact anchor-name candidate | configuration name | EntityID | 1/0 |
| ClassModifierCombinations | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| CompatibilityMatrix | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| ConsentQuestions | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| DispenseConfiguration | No exact anchor-name candidate | configuration name | none named EntityID | 0/0 |
| Donation | No exact anchor-name candidate | Review ownership | EntityID | 6/8 |
| DonationAttachment | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| DonationBloodUnit | product: ProductID | Review ownership | EntityID | 12/6 |
| DonationBloodUnitLabelConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| DonationBloodUnitLog | product: ProductID | Review ownership | EntityID | 0/0 |
| DonationBloodUnitMachine | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| DonationBloodUnitVisualInspection | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| DonationBloodUnitWitnessStep | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| DonationConsentAnswers | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| DonationConsentBlacklistDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| DonationDIN | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| DonationLog | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| DonationPatient | patient: PatientCode, PatientID | Review ownership | EntityID | 1/1 |
| DonationPatientLog | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| DonationPatientVisit | visit: VisitID | Review ownership | EntityID | 1/0 |
| DonationQuestionnaire | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| DonationQuestionnaireAnswer | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| DonationVitalSigns | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Donor | patient: PatientID | Review ownership | EntityID | 2/1 |
| ExternalBloodUnit | product: ProductID | Review ownership | EntityID | 3/1 |
| ExternalBloodUnitLog | product: ProductID | Review ownership | EntityID | 0/0 |
| ExternalBloodUnitVisualInspection | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| Hospital | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| LabInvestigation | product: ProductID | Review ownership | EntityID | 2/1 |
| LabInvistgationResult | product: ProductID | Review ownership | EntityID | 2/0 |
| Machine | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| PPMHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Product | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| QuestionnaireGroup | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| QuestionnaireQuestion | No exact anchor-name candidate | Review ownership | EntityID | 3/2 |
| QuestionnaireQuestionAnswer | No exact anchor-name candidate | Review ownership | EntityID | 3/1 |
| QuestionnaireSection | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| Reason | No exact anchor-name candidate | Review ownership | EntityID | 1/3 |
| SKLP_BloodUnitValidationReason | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SKLP_ProductUOM | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| SKLP_QuestionnaireDurationUnit | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| SLKP_Actions | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Anticoagulant | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BagStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BloodComponent | No exact anchor-name candidate | static lookup name | EntityID | 2/6 |
| SLKP_BloodSource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BloodType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/9 |
| SLKP_BloodUnitStep | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_BUDeleteReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ComponentStorageTemperature | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ComponentTransportTemperature | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DiscardReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Donation_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DonationBloodUnitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_Donor_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_DonorType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_InvistgationStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_LabInvestigationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_MachinePhase | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Modifier | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_OrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProcessGroupChild | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_ProcessGroupParent | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ProductCategory | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_ProductDescriptionCode | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_QuestionnaireAction | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_QuestionnaireControllerType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_QuestionnaireGenderType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReasonClassification | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ReturnReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_RHDBloodGroupCode | No exact anchor-name candidate | static lookup name | none named EntityID | 2/0 |
| SLKP_TransactionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TransactionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_UnReservedReason | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisualInspectionQuestion | No exact anchor-name candidate | static lookup name | none named EntityID | 0/3 |
| SLKP_VitalSignsStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| VitalSignsRanges | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/BloodBank.json (one level above this folder) for full columns, indexes, defaults and FK mappings.