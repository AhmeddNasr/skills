# QMS: patient, visit and product review

## Observed business-flow study

Outpatient booking creates/reuses pattern-instance details and a patient booking with queue-model-dependent code. Cutting/rebooking marks old booking deleted and may reuse its code. VM arrival/cancellation updates and clinic-state integration are separate actions. Queue/monitor/SMS effects are not reproduced by inserting appointment rows alone.

Evidence: GenerateQueueCodeManagerFactory.SavePatientAppointmentBooking74-129; source callback entry points; safe samples.

Read samples-bundle.json (schema QMS) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema QMS) for captured lookup/configuration keys (where present), and sql-objects/QMS.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Configuration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| MissedConfigurationSetup | No exact anchor-name candidate | configuration name | EntityID | 2/0 |
| Monitor | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| MonitorRoom | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| MonitorsConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| PatientAppointmentBooking | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 3/0 |
| PatternInstanceDetail | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| SLKP_MissedConfigurationType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_ModelType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PatientSource | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PatientStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_VisitStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| VIPNumber | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/QMS.json (one level above this folder) for full columns, indexes, defaults and FK mappings.