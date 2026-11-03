# VS: patient, visit and product review

## Observed business-flow study

Vital-sign/BMI setup includes measurement type, limits, age/sex ranges and indicators. Transactions can be patient-scoped or visit-linked. Reviewed external-device path validates time/duplicates/ranges and derives normal-range status before saving. Patient-summary projections group visit/timestamp measurements and expose derived display rows with NEWID, not stable base-record IDs.

Evidence: VitalSignTransactionManagerFactory.AddVitalSigns1302-1395; live PatientSummery vital view and cohort.

Read samples-bundle.json (schema VS) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema VS) for captured lookup/configuration keys (where present), and sql-objects/VS.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BMI_Transaction | patient: PatientID; visit: VisitID | Review ownership | EntityID | 2/0 |
| LKP_VitalSign | No exact anchor-name candidate | editable lookup name | none named EntityID | 1/5 |
| LKP_VitalSource | No exact anchor-name candidate | editable lookup name | EntityID | 1/1 |
| LKP_VSControlDataSource | No exact anchor-name candidate | editable lookup name | EntityID | 1/0 |
| SLKP_AgeRange | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BMI_AgeRange | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BMI_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_BMI_GenderAgeRange | No exact anchor-name candidate | static lookup name | none named EntityID | 2/1 |
| SLKP_BMI_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_BMI_TargetType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Control | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Status | No exact anchor-name candidate | static lookup name | none named EntityID | 0/2 |
| SLKP_VitalAgeNormalRange | No exact anchor-name candidate | static lookup name | none named EntityID | 2/3 |
| SLKP_VitalAgeScoreRange | No exact anchor-name candidate | static lookup name | none named EntityID | 1/1 |
| SLKP_VitalAgeStatusRange | No exact anchor-name candidate | static lookup name | none named EntityID | 2/1 |
| SLKP_VitalSignEntityAssignment | No exact anchor-name candidate | static lookup name | EntityID | 1/0 |
| SLKP_VitalSignEntrySource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VitalType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| VitalControl | No exact anchor-name candidate | Review ownership | EntityID | 2/2 |
| VitalSignEntity | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| VitalSignTransaction | patient: PatientID; visit: VisitID | Review ownership | EntityID | 7/1 |
| VitalSignTransactionControl | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| VSConfiguration | No exact anchor-name candidate | configuration name | none named EntityID | 1/0 |
| VSConfigurationType | No exact anchor-name candidate | configuration name | none named EntityID | 0/1 |
| WHOLMSReference | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/VS.json (one level above this folder) for full columns, indexes, defaults and FK mappings.