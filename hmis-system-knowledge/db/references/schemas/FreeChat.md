# FreeChat: patient, visit and product review

## Observed business-flow study

Chat owns its local user projections, chats, threads and messages. Reviewed pharmacist-physician chat resolves the physician through Security, creates missing local user projections, reuses/creates a visit-specific chat and matches order lines to threads. Message payloads are outside this study. Local chat-user records are not Security.User rows.

Evidence: ChatManagerFactory.StartPharmacistChat295-399 and GetPhysicianUser; safe samples.

Read samples-bundle.json (schema FreeChat) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema FreeChat) for captured lookup/configuration keys (where present), and sql-objects/FreeChat.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Chat | patient: PatientCode, PatientID; visit: VisitID | Review ownership | EntityID | 0/3 |
| Message | No exact anchor-name candidate | Review ownership | EntityID | 8/0 |
| Orderline | product: ProductID | Review ownership | EntityID | 2/1 |
| OrderlineDetail | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| Thread | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| User | No exact anchor-name candidate | Review ownership | EntityID | 0/6 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/FreeChat.json (one level above this folder) for full columns, indexes, defaults and FK mappings.