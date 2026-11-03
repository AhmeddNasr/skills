# SHR: patient, visit and product review

## Observed business-flow study

ErrorMessage stores failed message envelope, original queue/exchange/routing, pending/published/stopped/exception state and retry count. Reviewed UIUtilities job first republishes pending DB rows under the configured retry limit, then consumes the broker error queue into SQL. Duplicate checking uses an in-memory OriginalQueue+Message dictionary, not a durable global uniqueness guarantee. Payloads were excluded and no replay was executed.

Evidence: MQErrorHandlingManager.ConsumeErrorQueueMessages29-108, RepublishMessageFromDB110-124, SaveErrorMessageToDB130-170, PrepareErrorMessageModel264-280; model maps SHR.ErrorMessage.

These are reviewed source/sample findings, not proof that every deployed branch or external acknowledgement was exercised.

Cancellation/reversal evidence: see ../reversal-flows.md.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| ErrorMessage | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/SHR.json (one level above this folder) for full columns, indexes, defaults and FK mappings.