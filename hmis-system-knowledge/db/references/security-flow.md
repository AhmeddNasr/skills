# Security: users, permissions and entity context

Reviewed 2026-10-21. Basis: user business explanation, visible table/FK metadata, bounded live aggregate/link samples, five visible view definitions and legacy source excerpts. This is a source/database-supported study; deployed end-to-end authorization, HR synchronization and all security editing workflows remain unverified. See security-evidence.json for provenance.

## Business meaning confirmed by the user

A user may map to a physician, an employee synchronized from external HR, or an outside user without either linkage. Users are assigned one or more entities and navigate between them: the selected entity is the operational context. EntityID 0 is shared data, mainly setup/configuration, visible across entities. Assignment to several entities does not itself mean a combined all-entity operational view.

HR employee synchronization is performed by a job using a linked server and job-defined criteria (user-confirmed). Its deployed command, selection criteria, identity mapping, schedule and deletion behavior have NOT been inspected; do not invent them.

## Backend permission chain

ProjectService -> APIController(ProjectServiceID) -> WebAction(APIControllerID) -> WebActionPermission(WebActionID,PermissionID) -> Permission -> RolePermission(RoleID,PermissionID) -> Role -> UserRole -> User.

The live dbo.VWuserServerPermission follows this chain and unions static permissions. Its shown role path filters RolePermission.IsDeleted=0 and User.IsDeleted=0; it does not explicitly filter every role/status/permission flag. Do not silently describe a more restrictive rule than the deployed view actually implements. dbo.VWRolePermission used by the client path explicitly filters deleted roles, so the server/client view predicates differ.

The reviewed legacy TokenAuthorizeAttribute verifies token/environment and delegates permission checks. It contains role-ID-1 admin and app-to-app branches. The reviewed permission repository matches controller/action names and user ID OR IsStatic; ProjectService matching was removed in that branch. Another legacy Security.Identity attribute uses the older project-aware signature. Therefore verify which assembly/filter the deployed module uses before explaining effective access. The conceptual ProjectService hierarchy exists even when a runtime check omits that field. Client visibility is not proof of backend authorization.

## Client chain

Module.ParentID forms the module/submodule hierarchy. Page.ModuleId attaches pages. ClientAction joins a page through PageActionAccess(PageID,ActionID); PageActionPermission(PageActionID,PermissionID) connects that page/action pair to the shared Permission/RolePermission/UserRole chain.

Live dbo.VWUserModules supplies module/page/client-action fields using dbo.VWRolePermission, including static permissions through a UNION branch. Pages with no ModuleId use dbo.VWUserUnModuledPage. A static permission row is not necessarily an ordinary role grant. Report.ReportID is also a shared FK to Page.ID; ReportParameter belongs to Report. Do not assume Report has an unrelated generated page identity.

## Entity context and sharing

- Security.User.EntityID is the main entity. Security.UserEntity contains additional entity mappings, optional EmployeeID and cached EmployeeCode/EmployeeName.
- Reviewed UserEntityRepository retrieves nondeleted additional mappings by UserID, and resolves employee mapping for a selected EntityID.
- SecurityController builds menus/client permissions and emits a token containing selected entity/identity information. Switching entity updates the in-memory context and selects the matching UserEntity employee data in the reviewed path. Confirm deployed entitlement validation; token creation alone is not proof a caller may choose any entity.
- MainDBContext.Get<T> adds selected EntityID OR EntityID0 when the entity model has EntityID. It can additionally include entities in object-specific sharing groups. GetWithoutShared uses selected entity only; GetNoEntity bypasses that filter. Model types without EntityID are not automatically filtered by this method. Raw SQL and other repository versions need separate review.
- SharedData.GetSharedEntity uses a process-local dictionary keyed by full domain type name and groups containing the selected entity. Security Global.asax initializes this dictionary from GetAllSharedEntityGroupDictionary at startup. DomainObject, ChildObject, DomainObjectSharing and SharedEntityGroup represent the sharing setup. Refresh propagation after editing is not verified. Empty sharing tables in this environment do not prove the capability is absent everywhere.

User entity navigation and domain-object sharing are distinct concepts. Do not automatically add all a user's assigned entities to each query.

## User mappings and copied data

UserEmployee owns the user/employee link, employee names/code, department/section names and MappedEmpEntityId. UserPhysician owns physician identity/code/name variants and MappedPhysEntityId. In the visible metadata EmployeeID and PhysicianID are not declared cross-schema FKs: verify HR/MedStp ownership and entity before joining them. Both mapping tables have disabled/untrusted FKs to User and employee-type lookup in the captured database.

Reviewed UserManagerFactory editing checks duplicate employee/physician mappings, copies selected employee/physician display fields and handles additional entity mappings. UpdateUserEntities marks omitted existing additional mappings deleted, adds new rows and updates cached employee fields. It is not a harmless append-only API: partial payloads can remove omitted mappings. Independent direct updates can leave these projections and issued session data stale. Verify refresh/relogin behavior and any job refresh before scripting changes.

## All-table ownership register

| Tables | Role in the cycle |
|---|---|
| User | Account/main entity/authentication and assignment type; secrets must never be sampled/exported. |
| UserEmployee, UserPhysician | User-to-person links and copied identity/entity display data. |
| UserEntity | Additional entity context and per-entity employee mapping; soft-deleted assignment history. |
| UserRole | Account-to-role links; no IsDeleted column in captured structure. |
| Role, RoleGroup, RolePermission | Role grouping/status, permission grants and entity-scoped grant records. |
| Permission, BusinessAction, BusinessEntity, BusinessEntityGroup | Business permission vocabulary and categorization; BusinessEntity is not a hospital Security.Entity. |
| ProjectService, APIController, WebAction, WebActionPermission | Backend service/action mapping to permissions. |
| Module, Page, ClientAction, PageActionAccess, PageActionPermission | Client navigation and page/action permission mappings. |
| Entity | Hospital/business-unit setup. Active/deleted state affects eligibility but exact caller filters must be checked. |
| SharedEntityGroup, DomainObject, ChildObject, DomainObjectSharing | Object-specific entity sharing setup; empty current rows do not establish deployment-wide nonuse. |
| Report, ReportParameter | Page-linked reports and report parameter metadata; report execution/filtering is separate. |
| SLKP_AssignmentType | Live:1 Internal Employee,2 Physician,3 None. These differ from employee internal/external type. |
| SLKP_AuthenticationType | Live:1 Windows Authentication,2 Form Authentication. |
| SLKP_EmployeeType | Live:1 Internal,2 External (both active in sample). |
| LKP_Role_Status | Live names1 Active,2 In Active. Lookup-row IsActive was true for both: that flag does not make an inactive-role status active. |
| __MigrationHistory | EF schema migration history, not security account audit or a business workflow. |

## Sample integrity and limits

Seven aggregate orphan checks found 15,418 UserRole rows whose UserID has no matching User and 12 UserEntity rows with no matching User; the other five checked link categories returned zero. These are test-data observations, potentially caused by scripts. Inner joins can hide these orphan records, so absence from an effective-permission view is not proof the mapping table is empty. No data was repaired. Every visible Security FK was untrusted at capture; some were disabled. Existing data is not guaranteed valid just because FK metadata exists.

Role/RolePermission records include EntityID0 and entity-specific values. DomainObjectSharing and SharedEntityGroup had zero rows in the sample. No password hashes, salts, PINs, tokens, email addresses or personal user names were read.

## Patient, visit and product perspectives

Security governs actor identity, effective permissions and entity context for all three domains. It is not an owned patient/visit/product child aggregate. A visit deletion must preserve user/role/entity setup and shared physician/product masters. Determine the target actor/entity and workflow authority before data operations, then trace the clinical/stock/financial ownership graph. Audit CreatedBy referencing a user is not an instruction to delete that user.

## Remaining verification

Deployed filter versions; exact entity-switch entitlement checks; client static permission behavior; grant change/relogin invalidation; sharing-dictionary refresh in each service; external HR job and linked-server criteria; physician/employee mapping refresh; report parameter security; account/role deletion and historical auditing. No generic security modification or visit-delete execution is authorized by this study.
