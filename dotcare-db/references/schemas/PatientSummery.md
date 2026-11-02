# PatientSummery: projection schema

## Observed business-flow study

Patient/visit summary projections compose allergy, notes, sheets, problems, histories, medications, investigations, operations and vitals. View naming is not ownership: reviewed allergies-per-visit is patient-level, notes filter signed2, histories UNION six sections and vitals derive grouped rows with NEWID. Some display rows have no persistent identity and should never be delete targets.

Evidence: Ten reviewed projection definitions/columns/dependencies and safe projection samples.

Read samples-bundle.json (schema PatientSummery) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema PatientSummery) for captured lookup/configuration keys (where present), and sql-objects/PatientSummery.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

No base tables were visible in this schema. Do not invent insert/delete targets here. Read sql-objects/PatientSummery.json for column/parameter/dependency contracts. Selected definitions and safe representative samples were reviewed; not all object predicates are individually verified.

| Object | Type | Direct dependency candidates |
|---|---|---|
| UDF_CPOE_PatientSummary_LR_Investigation | SQL_INLINE_TABLE_VALUED_FUNCTION | CPOE.Orders, LR.AntibioticSensistivity, LR.AntibioticSensistivityResult, LR.Investigation, LR.InvestigationComponent, LR.InvestigationResult, LR.InvestigationResultComponent, LR.Organism, LR.SLKP_AntibioticClass, LR.SLKP_AntibioticGroup, LR.SLKP_AntibioticSensistivity, LR.SLKP_ResultReasons |
| CPOE_SP_MedicationOrderLineDetails | SQL_STORED_PROCEDURE | ?.MedicationIds, PatientSummery.CPOE_VW_MedicationOrderLineDetails |
| CPOE_SP_MedicationPatientSummery | SQL_STORED_PROCEDURE | ?.MedicationPtientDataType, PatientSummery.CPOE_VW_MedicationPatientSummery |
| GetCheifComplainByVisitID | SQL_STORED_PROCEDURE | PatientSummery.VWPSGetChiefComplaintByVisitID |
| GetLabFinalResults | SQL_STORED_PROCEDURE | PatientSummery.VW_LabFinalDetailDSCSH |
| GetMedicationsByVisitID | SQL_STORED_PROCEDURE | PatientSummery.CPOE_VW_MedicationPatientSummery |
| CPOE_VW_MedicationOrderLineDetails | VIEW | CPOE.MedicationOrderLine, CPOE.MedicationOrderLineDetails, CPOE.SLKP_FrequencyUnit |
| CPOE_VW_MedicationPatientSummery | VIEW | CPOE.MedicationOrderLine, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_OrderLineStatus, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.CPOE_VW_MedicationOrderLineDetails, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| CPOE_VW_MedicationPatientSummeryWithoutUser | VIEW | CPOE.MedicationOrderLine, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.CPOE_VW_MedicationOrderLineDetails, SC.Product, SC.ProductCategory |
| GetVSConfigurationForWidget | VIEW | VS.VSConfiguration |
| OR_OperationSurgeonsAndAssists | VIEW | OR.OperationPhysicians, OR.Reservation, OR.ReservationOperation |
| OR_OperationView | VIEW | OR.Product, OR.Reservation, OR.ReservationOperation, OR.ReservationStatusHistory, OR.SKLP_AnesthesiaType |
| PerformPhysicianDetails | VIEW | NP.PerformTransaction |
| VW_Allergy_PHR | VIEW | Allergy.PatientAllergyTransaction, Allergy.SLKP_AllergyType, Allergy.SLKP_Onset, Allergy.SLKP_Severity, Security.Entity |
| Vw_CPOE_PatientSummary_CompletedProcedureDetails | VIEW | CPOE.OrderLineDetail, CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderLineStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| VW_CPOE_PatientSummary_LabFinal_Details | VIEW | LR.Investigation, LR.InvestigationResult, LR.InvestigationResultComponent, LR.SLKP_ResultType, PatientSummery.VW_CPOE_PatientSummary_LR_Master, PatientSummery.VW_LR_GetLastCollectionDate |
| Vw_CPOE_PatientSummary_LabFinalDetails | VIEW | CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_ResultType, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| VW_CPOE_PatientSummary_LR_Details | VIEW | LR.Investigation, LR.InvestigationComponent, LR.InvestigationResult, LR.InvestigationResultComponent, LR.SLKP_ResultType, PatientSummery.VW_CPOE_PatientSummary_LR_Master, PatientSummery.VW_LR_GetLastCollectionDate |
| VW_CPOE_PatientSummary_LR_Investigation | VIEW | CPOE.Orders, LR.AntibioticSensistivity, LR.AntibioticSensistivityResult, LR.Investigation, LR.InvestigationComponent, LR.InvestigationResult, LR.InvestigationResultComponent, LR.Organism, LR.SLKP_AntibioticClass, LR.SLKP_AntibioticGroup, LR.SLKP_AntibioticSensistivity, Shared.VW_SC_Product, Shared.Vw_MedStp_Physician |
| VW_CPOE_PatientSummary_LR_Master | VIEW | CPOE.Configuration, CPOE.Orders, CPOE.SLKP_ProductClassification, MPI.Patient, MedStp.Physician, SC.Product, SC.ProductCategory |
| Vw_CPOE_PatientSummary_LRDetails | VIEW | CPOE.OrderLineDetail, CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_ResultType, CPOE.SLKP_Urgency, CPOE.TreatmentPlanVisit, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| Vw_CPOE_PatientSummary_LROrderlines | VIEW | CPOE.OrderLineDetail, CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderLineStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_ResultType, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| Vw_CPOE_PatientSummary_MedicationDetails | VIEW | CPOE.MedicationOrderLine, CPOE.MedicationOrderLineDetails, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderLineStatus, CPOE.SLKP_Urgency, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| Vw_CPOE_PatientSummary_ProcedureDetails | VIEW | CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| Vw_CPOE_PatientSummary_ProcedureOrderLineInstances | VIEW | CPOE.OrderLineDetail, CPOE.OrderLineInstance, CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderLineInstanceStatus, CPOE.SLKP_OrderStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.PerformPhysicianDetails, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| Vw_CPOE_PatientSummary_ProcedureOrderlines | VIEW | CPOE.OrderLineDetail, CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| VW_CPOE_PatientSummary_RadFinal_Details | VIEW | LR.Investigation, LR.InvestigationResult, LR.InvestigationResultComponent, LR.SLKP_ResultType, PatientSummery.VW_CPOE_PatientSummary_LR_Master, PatientSummery.VW_LR_GetLastCollectionDate |
| Vw_CPOE_PatientSummary_RadFinalDetails | VIEW | CPOE.Orders, CPOE.SLKP_CreationOrderModule, CPOE.SLKP_FrequencyUnit, CPOE.SLKP_OrderStatus, CPOE.SLKP_ProductClassification, CPOE.SLKP_ResultType, CPOE.SLKP_Urgency, MPI.Patient, MedStp.Physician, PatientSummery.VW_Security_User, SC.Product, SC.ProductCategory |
| VW_LabFinalDetailDSCSH | VIEW | PatientSummery.VW_CPOE_PatientSummary_LabFinal_Details |
| VW_LR_GetLastCollectionDate | VIEW | LR.CollectionSpecimen, LR.Investigation, LR.InvestigationCollectionSpecimen |
| VW_NP_ORTransactionAfterEndOrClose | VIEW | NP.ORTransaction |
| Vw_OR_OperationDetails | VIEW | PatientSummery.OR_OperationView, PatientSummery.VW_NP_ORTransactionAfterEndOrClose |
| VW_Security_User | VIEW | Security.User |
| VW_VM_GetPatientData | VIEW | MPI.Patient, MPI.PatientContact, MPI.SLKP_Gender, MPI.SLKP_MaritalStatus, MPI.SLKP_Nationality |
| VWGetChiefComplaintPerVisitForWidget | VIEW | PatPrlm.ChiefComplaint |
| VWGetProblemCardDetailForWidget | VIEW | PatPrlm.ProblemCardDetail |
| VWGetProblemCardPerVisitForWidget | VIEW | MedStp.Physician, MedStp.PhysicianSpecialty, MedStp.Speciality, PatPrlm.ProblemCard, PatPrlm.SLKP_Occurence, PatPrlm.SLKP_OutCome, PatPrlm.SLKP_Problem |
| VWPatientFamilyMedicalHistoryPerVisit | VIEW | MedHistory.Disease, MedHistory.FamilyPatientMedicalHistory, MedHistory.SLKP_FamilyType |
| VWPatientMedicationMedicalHistoryPerVisit | VIEW | MedHistory.MedicationPatientHistory |
| VWPatientObsGynMedicalHistoryPerVisit | VIEW | MPI.Patient, MedHistory.ObsGynContraception, MedHistory.ObsGynPatientMedicalHistory, MedHistory.SLKP_Contraception |
| VWPatientPastMedicalHistoryPerVisit | VIEW | PatPrlm.ProblemCard, PatPrlm.ProblemCardDetail |
| VWPatientSocialMedicalHistoryPerVisit | VIEW | MedHistory.SLKP_AlcoholUse, MedHistory.SLKP_CaffieneDose, MedHistory.SLKP_Duration, MedHistory.SLKP_MaritalStatus, MedHistory.SLKP_Mode, MedHistory.SLKP_Occupation, MedHistory.SLKP_SmokingStatus, MedHistory.SocialPatientMedicalHistory |
| VWPatientSurgicalMedicalHistoryPerVisit | VIEW | MedHistory.SurgicalPatientMedicalHistory |
| VWPSGetAllergiesPerVisit | VIEW | Allergy.PatientAllergyTransaction, Allergy.SLKP_AllergyType, Allergy.SLKP_Onset, Allergy.SLKP_Severity, Allergy.SLKP_Status |
| VWPSGetBMIPerVisitForWidget | VIEW | VS.BMI_Transaction, VS.SLKP_BMI_Status |
| VWPSGetChiefComplaintByVisitID | VIEW | PatPrlm.ChiefComplaint |
| VWPSGetClinicalNotesPerVisit | VIEW | CN.ClinicalNote, CN.SLKP_Type |
| VWPSGetClinicalNotesPerVisitForWidget | VIEW | CN.ClinicalNote, CN.Reply, CN.SLKP_Type |
| VWPSGetClinicalSheetsPerVisit | VIEW | CS.Form, CS.PatientClinicalSheet |
| VWPSGetClinicalSheetsPerVisitForWidget | VIEW | CS.Form, CS.PatientClinicalSheet, CS.SLKP_Type |
| VWPSGetDiagnosisPerVisit | VIEW | PatPrlm.ProblemCard, PatPrlm.ProblemCardDetail |
| VWPSGetDraftClinicalNotesPerVisitForWidget | VIEW | CN.ClinicalNote |
| VWPSGetDraftClinicalSheetsPerVisitForWidget | VIEW | CS.Form, CS.PatientClinicalSheet |
| VWPSGetPatientMedicalHistoryPerVisit | VIEW | PatientSummery.VWPatientFamilyMedicalHistoryPerVisit, PatientSummery.VWPatientMedicationMedicalHistoryPerVisit, PatientSummery.VWPatientObsGynMedicalHistoryPerVisit, PatientSummery.VWPatientPastMedicalHistoryPerVisit, PatientSummery.VWPatientSocialMedicalHistoryPerVisit, PatientSummery.VWPatientSurgicalMedicalHistoryPerVisit |
| VWPSGetVitalSignPerVisitForWidget | VIEW | VS.SLKP_VitalAgeStatusRange, VS.VitalSignTransaction |
| VWPSGetVitalSignsPerVisit | VIEW | MPI.Patient, Security.Entity, VS.VitalSignTransaction |
| VWPSGetVitalSignTypePerVisitForWidget | VIEW | VS.LKP_VitalSign |
| VWSPGetBMIPerVisit | VIEW | VS.BMI_Transaction, VS.SLKP_BMI_Status, VS.VSConfiguration |