# From an explanation to an action script

A script request needs an affected-row plan, not just a list of tables reachable through foreign keys. This applies to maintenance, migration correction, cache refresh, soft delete and hard delete. A discussion/example of visit deletion is not a request to execute it.

For each target record, classify related data:

| Relationship | Action reasoning |
|---|---|
| Owned detail/extension/status history | Follow requested history retention and the supported workflow; a shared PK extension can be owned even without a VisitID column. |
| Cached projection or search index | Identify authoritative writer and refresh mechanism; SQL copying/deleting one cache may leave others stale. |
| Financial or stock transaction | Find reversal/refund/return/posting behavior; determine whether physical removal is supported in the requested environment. |
| Shared reference/master | Preserve the referenced patient/product/physician/user/lookup merely referenced by the target. |
| Package header/member/purchase | Resolve all distinct package identities, assignments and cross-visit consumption before selecting rows. |
| Audit/integration/job/external record | Determine retention and downstream reconciliation; a database transaction cannot guarantee remote reversal. |
| Unverified link | Show the uncertainty and collect writer/sample evidence; do not label script coverage complete. |

Build a parameterized read-only preview by actual keys/entity and include soft-deleted history when the requested scope includes history. Use the schema catalog to check indexes and composite/shared keys. Trace non-FK links, order family, polymorphic IDs and application-only ownership. Review configuration-dependent callbacks, triggers if visible, events and jobs. A result of zero rows under limited metadata visibility does not prove absence of dependencies.

When script creation is authorized, prefer the reviewed business writer for its supported cycle. If direct SQL is appropriate, generate an explicit affected-row plan, transaction/error handling, concurrency/row-count conditions, dependency-safe changes and a verification query. Preserve shared masters. Explain any excluded side effects and the confidence of coverage. Do not relax preview checks automatically after a row-count mismatch: compare the selected key set and state first. Avoid arbitrary fixed counts copied from a different sample.

For visit work, distinguish cancelling an active visit, removing erroneous test data, deleting service lines, and deleting historical records. For product work, distinguish retiring master setup from removing stock/clinical history. For patient work, distinguish correcting an import from deleting longitudinal medical history. Ask about only genuinely unresolved action scope, rather than assuming these are equivalent.

No generic cascading DELETE is bundled: the dependency explorer is evidence discovery, and its direction/reachability does not establish ownership. After verifying the requested cycle, give a concrete script tailored to that cycle and environment.
