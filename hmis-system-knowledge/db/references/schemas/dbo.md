# dbo: patient, visit and product review

## Observed business-flow study

Mixed schema: contains legacy core views/order caches, import/staging tables, script work tables, backups and diagnostic snapshots. Names such as dummy, Temp or dated backups do not prove active use or safe deletion. Resolve the actual writer and consumer per table; some effective Security permission views live here. No single dbo business cycle can be inferred.

Evidence: Full table samples; SQL object dependency catalog; Security live views; original visit study.

Read samples-bundle.json (schema dbo) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema dbo) for captured lookup/configuration keys (where present), and sql-objects/dbo.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __EFMigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AHJAVGCost | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AHJAVGCost$ | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AHJBarcodes | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AHJServices | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Araby_Drugs | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Clients | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_FinalServicePrice | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_AL RAJHI_PriceList | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_NCCI_Price | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_NewContract2025 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_TCS_BillingGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_TCS_Contracts2025 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_TCS_UpdatePrice | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_TCS_UpdateShadow | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Hossam_TCSContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_ItemPrice | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_LabProfiles | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_MedicationUpdates | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NewBillingGroup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NewCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NewContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NewSpeciality02-01-2024 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NewUOM | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NotFound | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_NurseStationWarehouseAssignment | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_SAUDIENAYA | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Services | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Shadow | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Speciality | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Amr_Tarek-CashPL | product: ProductId | Review ownership | none named EntityID | 0/0 |
| Amr_Users | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrALRAJHITAKAFUL | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrALRAJHITAKAFUL_V2 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrBill | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrBupa | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrBupaAccommodation | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrBupaAccomodationClassShadowBilling | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrBupaShadow | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrCashAccommodationPrice | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrClient | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrFinalDentalservice | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrGlobMed | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrIPDContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrMalathContract | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrMedGulfContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrNcciMainContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrNCCIREFFERAL | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrNPHIESProductCode | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrOasisPriceList | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrPackages | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrPhysicianNphiesCode | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrProductNphiesCode | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrProducts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrProductsWithNphiesCode | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrTCS | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AmrTCS-ARABIANSHIELDCOOPERATIVEINSURANCE | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ApprovalLetterStatusLog | visit: VisitID | Review ownership | EntityID | 0/0 |
| AXAMainContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AXA-REF-Contracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BloodOrder_Staging | patient: PatientId; visit: VisitId | Review ownership | EntityId | 0/0 |
| BulkMigrationSetup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BupaContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BupaPriceList | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CashedOrderLine | visit: VisitID; product: ProductID | Review ownership | EntityID | 0/0 |
| CCHI_ICD10 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ChiefCompl | patient: PatientCode; visit: VisitID | Review ownership | none named EntityID | 0/0 |
| ClaimsResubmission | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| CodeDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ContractorPriceList | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| DiscontinueReasonCategory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| dummyFinalProducts | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProducts_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProducts_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProducts_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProducts_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProductsComparingResult | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProductsComparingResult_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProductsComparingResult_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProductsComparingResult_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProductsComparingResult_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyFinalProductsComparingResultToUpdate_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalance | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalance_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalance_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalance_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalance_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalanceAfterUpdate | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalanceAfterUpdate_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalanceAfterUpdate_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalanceAfterUpdate_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsAccumelatedBalanceAfterUpdate_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalance | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalance_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalance_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalance_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalance_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalanceAfterUpdate | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalanceAfterUpdate_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalanceAfterUpdate_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalanceAfterUpdate_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyProductsLatestBalanceAfterUpdate_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyStockableWarehouseProducts | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyStockableWarehouseProducts_1 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyStockableWarehouseProducts_2 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyStockableWarehouseProducts_3 | product: ProductID | Review ownership | none named EntityID | 0/0 |
| dummyStockableWarehouseProducts_audit | product: ProductID | Review ownership | none named EntityID | 0/0 |
| DuplicatedClaims | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| duplicatedGeberics | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| external_paresed_rejection_reasons | visit: VISIT_ID | Review ownership | none named EntityID | 0/0 |
| FirstBatchPatient$ | patient: PATIENT_ID | Review ownership | none named EntityID | 0/0 |
| GLAccountsOpeningBalance_Stage | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| GLOBEMED-ALLIANZ | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| 'HROisesData' | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Insurance_utilized | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ItemPriceList | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LAB_INV_COMP_NORMAL_VALUE$ | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| LAB_INVESTIGATION_COMPONENT$ | product: ProductID | Review ownership | EntityID | 0/0 |
| LastPatientBatch | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| LatestSMHproducts | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| LatestSMHproductsDeActivate | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LatestSMHproductsLAB | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| LatestSMHproductsRAD | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| locationtemp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MalathContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MarketingMigrationDoctors | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MedGulf | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MedicationOrders | patient: PatientCode; visit: VisitId | Review ownership | none named EntityID | 0/0 |
| MEDIVISA | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MEDIVISA-REFERRAL | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MigrationSetup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MilkUnits | patient: PatientID; visit: VisitID | Review ownership | none named EntityID | 0/0 |
| 'MissingUsersTemp' | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| MS_Oasis_CRD_PL | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NcciMainContracts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NcciRefferal | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NotifyPowerAppsLog | patient: PatientCode; visit: VisitID; product: ProductID | Review ownership | none named EntityID | 0/0 |
| NphiesDrug | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NphiesMedicalDevices | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| NursingStaffingEmails | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OasisMOHvisits | patient: PatientCode | Review ownership | none named EntityID | 0/0 |
| ODOOStockData | product: productid | Review ownership | none named EntityID | 0/0 |
| OperationListMigration | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OsisNewHRData | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| OSUsers | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| PatientsTemp$ | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| 'PatientsTempDataNew' | patient: PATIENT_ID | Review ownership | none named EntityID | 0/0 |
| PatientTempData | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PatientTempDataa | patient: PATIENT_ID | Review ownership | none named EntityID | 0/0 |
| PatientTempDatas | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PatternSpecialityTempData | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PatternTempData | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PhysicianTemp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ProblemCardTemp | visit: VisitID | Review ownership | none named EntityID | 0/0 |
| QueryStats | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ReplicationScripts | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Requests | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ROA_Split | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| RoleMatrix | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SBSV2TechnicalList | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SecurityMatrix$ | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| ServiceICD10 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Sheet1$ | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Stock_count_test | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| SyncUndoLog | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| sysdiagrams | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| tableName | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| tblPhysicianSchedule | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Temp_AHJAVGCost_Opening | product: product_Id | Review ownership | none named EntityID | 0/0 |
| test | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| UOM_Conversion_Map | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| userDataSID | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| WarehouseAssignmentTemp | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| WareHouseUserAssignment | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| WebActionPermissionBackup | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/dbo.json (one level above this folder) for full columns, indexes, defaults and FK mappings.