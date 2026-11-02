# PA: patient, visit and product review

## Observed business-flow study

The only visible base table is ICD10(ICDDiagnoseCode), but 14 views compose stock balance/price, OPD/IPD visit/service/authorization and physician scheduling data from SC, Billing, CPOE, VisitMgt, MPI and OPD/MedStp. These are projections rather than extra owned visit tables. CPG_Policy uses the ICD code reference; no integer identity should be invented for it. Exact view predicates remain source-specific.

Evidence: PA SQL object column/dependency contracts; base-table presence samples. No standalone patient-admission master inferred from abbreviation.

These are reviewed source/sample findings, not proof that every deployed branch or external acknowledgement was exercised.

## Table/object worksheet

Structural worksheet generated from visible metadata captured 2026-10-21. Name-based domain/role candidates below are discovery leads, not verified ownership or flow. See module-map.md for business evidence status.

| Table | Domain-column candidates | Setup/config candidates | Entity scope column | FK out/in |
|---|---|---|---|---|
| ICD10 | No exact anchor-name candidate | Review ownership | none named EntityID | 0/0 |

## Business review required

- Resolve each candidate through declared or reviewed application links; polymorphic ServiceID/DrugID names need source confirmation.
- Trace create/edit/perform/cancel and historical versus active behavior from source writers, configuration and representative samples.
- Record copied fields and authoritative owner, update trigger, event/job/index refresh and retry behavior.
- Determine selected-entity/shared semantics per repository path; absent EntityID does not mean public/shared access.
- Verify lookup enum meanings from target data and source; SLKP/LKP naming is a convention, not sole authority.
- See catalog/PA.json (one level above this folder) for full columns, indexes, defaults and FK mappings.