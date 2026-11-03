# BIReport: projection schema

## Observed business-flow study

Read-only schedule projection: two views parse FREQ/INTERVAL/BYDAY recurrence strings from current and temporary OPD pattern tables. They are neither separate schedule masters nor patient-visit records. Safe recurrence-ID samples connect this schema to OPD setup.

Evidence: Two live view definitions and projection samples.

Read samples-bundle.json (schema BIReport) for base-table seed samples (where base tables exist), setup-vocabularies-bundle.json (schema BIReport) for captured lookup/configuration keys (where present), and sql-objects/BIReport.json for visible database-owned contracts (where present). These are source/sample-supported findings; do not interpret this study pass as every deployed branch having passed end-to-end UAT.


## Table/object worksheet

No base tables were visible in this schema. Do not invent insert/delete targets here. Read sql-objects/BIReport.json for column/parameter/dependency contracts. Selected definitions and safe representative samples were reviewed; not all object predicates are individually verified.

| Object | Type | Direct dependency candidates |
|---|---|---|
| OPDTempPatternRecurenceRule | VIEW | OPD.PHS_TempOPDPattern, Reports.SplitString_Shared |
| VW_OPDPatternRecurenceRule | VIEW | OPD.PHS_OPDPattern, Reports.SplitString_Shared |