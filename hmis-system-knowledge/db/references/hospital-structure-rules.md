# Hospital Structure: extended rule and projection review

Status: source-supported and live-data observed; NOT complete deployed-workflow verification. Evidence: hsm-deep-evidence.json. No API callbacks or data changes were executed.

## Configuration and visibility

HSM.Configuration key AllBuildingsRetrieveType is 0 in the captured shared EntityID 0 row. Reviewed manager defaults missing/non-numeric values to AllEntitiesBuildings (0). Parsed integers are cast without enum-range validation; downstream switch defaults to all-entity buildings. Mode 0 uses GetNoEntity; mode 1 uses GetAll, then active/nondeleted building filters. Entity-selection decoration is separate from row visibility.

Core MainDBContext.Get<T> includes current entity plus zero and configured SharedData entities when the current entity belongs to that sharing group. GetWithoutShared matches current only. GetNoEntity bypasses this filter. Get does not generically add IsActive/IsDeleted predicates. SharedData configuration must be resolved before asserting exact visibility; this is explicit configured sharing, not automatic union of every entity assigned to a user.

## Lifecycle and downstream effects

| Operation | Reviewed rules and effects |
|---|---|
| Building create | Creates active/nondeleted building, saves to obtain identity, creates requested floors, records actor/time in transaction. |
| Building/floor edit/delete | Name validation and ModifiedTS checks; deleting building/floor blocks nondeleted children, then soft deletes with actor/time. Reviewed direct edit methods do not themselves refresh every downstream path. Do not infer automatic renaming of cached descendants. |
| Room save | Validates parent floor, names, concurrency; edit rejects child structures or bed links. Prevents changing an in-use nurse station group and assigning a room as its own nurse station. Uses active first assignment, updates type/classification/station. Existing specialty links are retired; OPD medical nurse stations require MedStp specialty resolution and recreate copied names. |
| Room projection | Edits call BedMgt update-if-present. Changing away from OR/ER calls old-owner deletion; new OR/ER classification calls its add/edit contract with original HSM room ID. Both type and classification and previous state matter. No guarantee remote HTTP work rolls back with local TransactionScope. |
| Room delete | Timestamp, child and bed checks; OPD housing and QMS monitor/started-clinic callbacks; nurse-station-use guard; soft delete with actor/time; deactivate assignments, retire specialties; then OR/ER delete callback using first assignment. Callback failure aborts normal success path. |
| Zone save/delete | Validates parent room and names; edit/delete reject bed links or timestamp mismatch. Edits update existing BedMgt projection. ER parent assignment routes zone add/edit/delete to ER. Uses first assignment without local active filtering at that selection. |
| Bed save/delete | Resolves room from zone where necessary; copies room nurse-station ID into HSM.HospitalStructureBed. Calls ER bed contract when first room assignment classification is ER. Local delete is soft delete; receiver occupancy rules must still be followed. |
| Assignment type create/edit/delete | Names required, max 30 each, case-normalized duplicate checks. Permanent enum IDs cannot be edited/deleted. Active room use, active children, medical-state change and ModifiedTS constrain changes. Medical types create/update CPOE copy; medical-to-nonmedical removes it; medical edits update existing BedMgt room-group labels. HSM deletion deactivates type; CPOE deletion marks its copy deleted. |

## Receiving owners

- BedMgt.UpdateRoomGroupIfExisted and UpdateHospitalStructureIfExisted return success if the projection is absent. They do NOT create missing copies. Existing structure update copies building/floor/room/zone labels and paths; group update copies names.
- CPOE medical room-group create rejects an existing nondeleted ID, restores a deleted copy, or creates a new copy with the HSM ID. Edit requires an existing copy. Delete rejects admission order lines still outside Discontinued/Complete; missing target returns success.
- ER room create can restore a deleted row; existing live duplicate fails; edit rejects missing/deleted. Delete rejects occupied beds found through room zones, then soft deletes. Other bed relationships must not be assumed covered by that predicate.
- OR receiver requires Room type and operation classification. Create rejects existing live row; edit rejects missing/deleted. It preserves HSM ID and copies names/parent/code, current entity and active state. Delete returns success for absent target, rejects any noncancelled reservation, otherwise soft deletes with audit.

## Live-state observations and unresolved branches

Six classifications, 51 assignment types and five structure types were read in full with a 501-row cap; no result hit that cap. Six classifications include ID 6 OR - L&D, absent from the reviewed five-member HSClassification enum and explicit OR/ER routing. Its writer/consumer branch remains unresolved. Do not map it automatically to OR ID 5.

The grouped assignment query produced 32 state/entity/type/classification combinations. A full grouped check found no HospitalStructureID with multiple IsActive=1 assignments in this snapshot. This does not prove first-assignment queries always select active rows: some reviewed methods omit that predicate and historical/inactive assignments still require examination.

Remaining before workflow completion: deployed-source identity; class-6 routing; parent validation and defaults for every input subtype; all hierarchy/name-propagation paths; ER bed/zone receiving branches; OPD/QMS receiving guards; full configured sharing rules; transaction/partial-failure/retry behavior; representative positive/negative lifecycle verification. No numerical percentage is justified until the branch inventory is closed.

## Additional receiver and sample verification

ER bed receiving code requires both a nondeleted room and nondeleted zone; duplicate add and missing edit fail. New bed uses original BedID, selected entity, Available status and zone. Edit copies names/zone/entity; delete rejects occupied beds. HSM can send ZoneID 0 for a direct-room bed, so that combination cannot be assumed valid without a matching zone or another deployed branch. ER zone create uses EntityID 0, unlike room/bed selected entity; it assigns room/labels and rejects missing parent. Delete rejects occupied beds. A deleted-zone restore path is not explicitly implemented in this reviewed branch.

OPD IsRoomHoused requires a matching nondeleted room housing with PatternID and no expired end date/time. The reviewed predicate does not check StartDate, so future housing can block deletion too. QMS checks a nondeleted monitor-room link, then a nondeleted pattern detail with ClinicStartDateTime and no ClinicEndDateTime; open-clinic result takes precedence if both apply. These are branch-specific receiving predicates, not generic occupancy checks.

Projection query returned 25 active HSM rooms in classifications 3/5/6: six ER had ER rows, eighteen OR had OR rows and one OR-L&D had an OR row. This proves matched IDs in captured state, not fresh synchronization, correct names/entity/status or the class-6 writer. All 23 active medical assignment types returned had CPOE IDs. No historical multi-assignment group was returned by the grouped query. These observations do not certify callback retry or rollback behavior.

The database also has active hospital-structure type 4 Area, absent from the reviewed HospitalStructureTypes enum (Building/Floor/Room/Zone). Its origin and applicable hierarchy must be resolved separately; do not silently treat Area as Zone or Room.
