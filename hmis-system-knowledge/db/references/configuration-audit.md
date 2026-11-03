# Configuration and allowed-action verification

Coverage is incomplete. Table coverage and two-row samples are not verification of every setting or allowed transition. configuration-audit.json is a candidate backlog, not a completed rule register.

## Reviewed findings

- VisitMgt.VisitAllowedAction: STF VisitAllowedActionHelper caches by EntityID, VisitClassificationID, VisitStatusID and VisitActionEnum. Manager passes current user OrgId. Missing key returns false. Exact entity comparison has no shared-zero fallback in this helper. Build reads GetNoEntity; nonempty cache is reused. Refresh clears and rebuilds. Nullable IDs and IsAllowed are dereferenced without local null guards; duplicate keys overwrite in enumeration order. Repository filtering and deployed behavior still require confirmation.
- MemoryCachingController exposes RefreshAllowedActions and RefreshVMConfiguration GET methods in reviewed source. No endpoint was called. Route, authorization, deployed version and multi-instance cache invalidation are not established by this source excerpt.
- OR.ActionsAllowedStatusConfig repository filters ActionID and returns StatusID list through GetAll. Base repository entity/deletion filtering must be checked; this method alone does not prove the effective entity scope. Manager logs exceptions and returns null, distinct from an empty allowed list.
- CPOE.ClinicalTransferAllowedStatus manager returns StatusID from repository GetAll. Effective scope depends on repository behavior and the caller. Do not assume it uses the same rule as VisitAllowedAction.

## Required evidence for each rule

Record actual key/value semantics; type and permitted values; entity/shared precedence; classification and status predicates; missing/null/default handling; permission checks; all known consuming writers/readers; update/cancel behavior; cache initialization/refresh; related records and downstream effects; source version and contradictory samples. Mark incomplete branches explicitly.

Before mutation-related advice, verify the relevant effective rules in the target environment. A source match or sampled row does not qualify a destructive script as verified. No generic shared-entity fallback, allowed transition or cache refresh may be invented.

## Caller and precedence checks

- STF VMConfigurationHelper differs by API: GetConfigurationValue checks exact entity first, then zero, then null. GetConfigurationByID filters entity OR zero and takes FirstOrDefault without explicit entity priority; list methods can return both. Do not treat these APIs as equivalent when both rows exist. Cache refresh has the same explicit rebuild pattern; the observed read does not establish automatic invalidation.
- Main CPOE SaveClinicalTransferOrder reads allowed statuses. An empty list defaults to enum Discontinued. It checks orders for the selected visit/physician with a status outside that list and at least one non-clinical-transfer line; such orders block the reviewed save path. A separate check rejects a second Ordered clinical-transfer order. This table is a prerequisite-status exemption list, not a generic permission grant.
- Main OR CheckChangeStatusAllowed checks whether the reservation current StatusID belongs to statuses configured for ActionID. Empty list denies. Exceptions (including a null returned by manager) are logged and return false.

Source locations in configuration-source-candidates.json are discovery leads only. Models, migrations excluded by filename glob where recognized, comments and name collisions can appear; no match counts as a reviewed consuming rule. The inventory's name heuristic also misses settings embedded in other tables.
