# OPD: patient, visit and product review

## Observed business-flow study

OPDPattern recurrence and generated instances support physician schedule/booking/arrival. Housing is separate. Pattern recurrence is also parsed by BIReport views; schedule changes can affect QMS and PhysicianDesktop pattern-instance projections. Booking, reschedule/cancel and historical visits must preserve already consumed schedule relationships.

Evidence: OPDPattern-Integration.md; original OPD visit source study; QMS booking source; BIReport definitions.

Read samples-bundle.json (schema OPD) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema OPD) for captured lookup/configuration keys (where present), and sql-objects/OPD.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| BK_Appointment | patient: PatientCode, PatientID | Review ownership | EntityID | 8/2 |
| BK_ApptProcedure | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| BK_ApptStatusTrack | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| BK_PatternInstance | No exact anchor-name candidate | Review ownership | EntityID | 2/3 |
| BK_PatternInstanceDetails | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| BK_SLKP_ApptCancelReason | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| BK_SLKP_ApptStatus | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| BK_SLKP_ConsultationType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| BK_Slot | No exact anchor-name candidate | Review ownership | EntityID | 1/1 |
| Campaign | No exact anchor-name candidate | Review ownership | EntityID | 5/1 |
| ExternalCampaignRecipient | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| LKP_Procedure | No exact anchor-name candidate | editable lookup name | EntityID | 0/2 |
| LKP_SourceOfBusiness | No exact anchor-name candidate | editable lookup name | none named EntityID | 0/1 |
| OPDConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| PHS_ClinicTag | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| PHS_ClinicType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| PHS_ExceptionTypeReason | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PHS_Housing | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| PHS_HousingDay | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PHS_LKP_ExceptionReason | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| PHS_LKP_SpecialtyBooking | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| PHS_OPDDivideCapacity | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PHS_OPDPattern | No exact anchor-name candidate | Review ownership | EntityID | 3/10 |
| PHS_PatternClinicTag | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PHS_PatternException | No exact anchor-name candidate | Review ownership | EntityID | 4/1 |
| PHS_PatternProcedure | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PHS_PatternSpeciality | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PHS_PatternVisitType | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PHS_QueueingModel | No exact anchor-name candidate | Review ownership | none named EntityID | 0/4 |
| PHS_SLKP_ConsultationType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |
| PHS_SLKP_ExceptionType | No exact anchor-name candidate | Review ownership | none named EntityID | 0/2 |
| PHS_SLKP_HousingType | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| PHS_SLKP_WeekDay | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| PHS_TempOPDPattern | No exact anchor-name candidate | Review ownership | EntityID | 3/0 |
| SLKP_BookingTabSlotStyle | No exact anchor-name candidate | static lookup name | EntityID | 0/0 |
| SLKP_CampaignDataSourse | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_CampaignPriority | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_CampaignStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_FinancialStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_RescheduleExceptionType | No exact anchor-name candidate | static lookup name | EntityID | 0/1 |
| SLKP_SMSStatus | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_TemplateUsage | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SMSParameters | No exact anchor-name candidate | Review ownership | EntityID | 0/1 |
| SMSSentMessage | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| SMSTemplates | No exact anchor-name candidate | Review ownership | EntityID | 2/1 |
| SMSTemplateTypePrameters | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| SMSTemplateTypes | No exact anchor-name candidate | Review ownership | EntityID | 0/3 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/OPD.json (one level above this folder) for full columns, indexes, defaults and FK mappings.