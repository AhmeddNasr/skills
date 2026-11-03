# NS: patient, visit and product review

## Observed business-flow study

Notification type/template/configuration and recipient/entity context drive persisted notifications. Reviewed writer validates payload/template/type, commits notification creation then publishes IDs to clients; routing can target all entities, one entity or explicit entity list. Local row persistence does not prove delivery. Email/template/event/attachment paths are separate from this websocket notification path.

Evidence: NotificationManagerFactory.CreateNotificationsAndNotify49-218; safe samples and static vocabulary.

Read samples-bundle.json (schema NS) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema NS) for captured lookup/configuration keys (where present), and sql-objects/NS.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationsHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| Attachment | No exact anchor-name candidate | Review ownership | none named EntityID | 1/4 |
| AttachmentType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| EmailInlineAttachment | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| EmailTemplate | No exact anchor-name candidate | Review ownership | EntityID | 1/2 |
| EmailTemplateRecipient | No exact anchor-name candidate | Review ownership | none named EntityID | 2/0 |
| EventAction | No exact anchor-name candidate | Review ownership | none named EntityID | 3/0 |
| Notification | patient: PatientId | Review ownership | EntityID | 1/1 |
| NotificationEntity | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| NSConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Recipient | No exact anchor-name candidate | Review ownership | none named EntityID | 1/1 |
| SLKP_ActionType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_EmailInlineAttachmentType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_EventType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_NotificationTemplate | No exact anchor-name candidate | static lookup name | none named EntityID | 3/1 |
| SLKP_NotificationType | No exact anchor-name candidate | static lookup name | none named EntityID | 2/1 |
| SLKP_RecipientType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TemplateType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| Template | No exact anchor-name candidate | Review ownership | none named EntityID | 1/2 |
| UserTicket | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/NS.json (one level above this folder) for full columns, indexes, defaults and FK mappings.