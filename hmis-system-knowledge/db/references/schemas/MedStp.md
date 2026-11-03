# MedStp: patient, visit and product review

## Observed business-flow study

Specialty hierarchy and physician master feed visit/order/schedule caches across modules. Physician contacts/qualifications/specialties belong to the master aggregate; exactly one main specialty and supervisor compatibility matter in reviewed import. Physician flags do not provision HR or Security users. Renames require writer-specific cache handling, not blanket replacing all text.

Evidence: Physician-Integration.md; original specialty confirmations and target metadata/samples.

Read samples-bundle.json (schema MedStp) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema MedStp) for captured lookup/configuration keys (where present), and sql-objects/MedStp.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| __MigrationHistory | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |
| LKP_QualifierType | No exact anchor-name candidate | editable lookup name | EntityID | 0/1 |
| MSConfiguration | No exact anchor-name candidate | configuration name | EntityID | 0/0 |
| Physician | No exact anchor-name candidate | Review ownership | EntityID | 4/4 |
| PhysicianContact | No exact anchor-name candidate | Review ownership | EntityID | 1/0 |
| PhysicianQualifier | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PhysicianSpecialty | No exact anchor-name candidate | Review ownership | EntityID | 2/0 |
| PhysicianSpecialtyDeleted | No exact anchor-name candidate | Review ownership | EntityID | 0/0 |
| SLKP_Gender | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_PhysicianIdentifierType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| SLKP_PhysicianTitle | No exact anchor-name candidate | static lookup name | none named EntityID | 0/1 |
| SLKP_Pys_ContactType | No exact anchor-name candidate | static lookup name | none named EntityID | 0/0 |
| Speciality | No exact anchor-name candidate | Review ownership | none named EntityID | 1/3 |
| SpecialityDiagnosis | No exact anchor-name candidate | Review ownership | none named EntityID | 1/0 |
| SupervisoryLevel | No exact anchor-name candidate | Review ownership | none named EntityID | 0/1 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/MedStp.json (one level above this folder) for full columns, indexes, defaults and FK mappings.