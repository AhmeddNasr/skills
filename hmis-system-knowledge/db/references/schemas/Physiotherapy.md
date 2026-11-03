# Physiotherapy: patient, visit and product review

## Observed business-flow study

Visit/patient order -> product-specific order details -> scheduled/performed sessions. Perform validates quantities, state and unique CPOE order linkage, creates session and calls VM then CPOE before success. Scheduling, partial session execution, cancellation and rescheduling are distinct states; remaining quantity is not merely a service-row count.

Evidence: PhysioOrderManagerFactory.PerformOrderDetails329-427; order3/detail3 sample and cohort.

Read samples-bundle.json (schema Physiotherapy) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema Physiotherapy) for captured lookup/configuration keys (where present), and sql-objects/Physiotherapy.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| AppointmentDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| PhysicianAssignation | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PhysioOrder | patient: PatientCode, PatientId; visit: VisitId | Review ownership | EntityID | 1/2 |
| PhysioOrderDetails | product: ProductId | Review ownership | none named EntityID | 1/1 |
| PhysiotherapyConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Session | No exact anchor-name candidate | Review ownership | none named EntityID | 3/1 |
| SessionDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| SLKP_PhysioOrderStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_SessionStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/Physiotherapy.json (one level above this folder) for full columns, indexes, defaults and FK mappings.