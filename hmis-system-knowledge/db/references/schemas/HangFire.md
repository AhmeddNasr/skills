# HangFire: patient, visit and product review

## Observed business-flow study

Job/state/queue/parameter/counter/hash/list/set/server tables support background work. Reviewed UIUtilities startup selects Hangfire SQL storage, starts a server, configures automatic retries and registers the recurring message-queue error-handling job using configured interval/retry limit. Its SHR replay behavior is separate from deleting a business record. Other job producers and serialized arguments require job-specific review.

Evidence: UIUtilities Global.asax37-59; MQErrorHandlingManager29-170; safe state/presence samples.

These are reviewed source/sample findings, not proof that every deployed branch or external acknowledgement was exercised.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| AggregatedCounter | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Counter | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Hash | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Job | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| JobParameter | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| JobQueue | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| List | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Schema | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Server | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Set | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| State | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/HangFire.json (one level above this folder) for full columns, indexes, defaults and FK mappings.