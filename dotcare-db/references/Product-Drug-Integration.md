# Consolidated product and drug migration

In Supply Chain, select **Products and drugs - category and UOM in one row** and download a fresh template after choosing the target environment and hospital entity. This template is separate from the older supply-chain staging workbook and the native HMIS bulk templates.

Each product occupies one row. The importer resolves or creates its category, builds up to four descending UOM levels, reuses an existing complete matching unit structure, and commits the SC, PMGT, Billing and Finance setup together. Medication rows also include drug details, enabled/default drug units, up to two ingredients, two routes and two therapeutic categories per ingredient.

Dropdowns read the selected database. Fixed SLKP values must already exist and retain their application enum meanings. Missing editable ingredient, dosage-form, strength-unit and therapeutic-category names are created in the product transaction. New categories require their prefix; existing parent categories are selected by name. An omitted UOM category name is generated from the unit hierarchy. Omitted Arabic unit names preserve existing names when a structure is reused.

Valid rows save automatically. Invalid rows remain in review and can be exported and uploaded again. The results workbook includes generated product and dependency identities. Existing conflicting setup is rejected rather than overwritten. A previous unconfirmed write blocks automatic resubmission until it is reconciled.

IsActive is true and IsDeleted is false internally. SC numeric codes and SQL identities are generated; the Excel product code is retained as the display code. NPHIES columns and mappings apply only to KSA environments. Blank source IDs receive a stable migration key, separate from the target SQL identity.

After committed drug setup, the portal queues the native CPOE trade-name index rebuild using the target's registered CPOE service and the current HMIS session. Its outcome is recorded in the audit log. Index failure does not undo committed setup. No external broker/Odoo events are emitted by the direct adapter.

Dental, package, operation-theatre and offer classifications are rejected until their specialized workflows are implemented. Basic laboratory/radiology/microbiology and blood-bank product copies do not create investigation tests, specimens or clinical configuration. Stock balances, average costs, prices and transactions use their separate native workflows.

Verification: 23 focused product checks passed, including live lookup binding, correction re-upload, complete drug insertion, and two products sharing a UOM structure under different category labels. SQL test inserts were enclosed in an outer transaction and rolled back. The 94 existing portal regression checks passed. A browser upload with a fresh authenticated HMIS session and the subsequent live CPOE indexing response remain user acceptance checks.


## UOM category selection after unit entry

UOMCategoryName and UOMCategoryArabicName follow all four UOM name/Arabic/conversion fields. Category name is optional. With a blank category, the importer first looks for a unique active category with exactly the same unit names, ratios and reference unit. It reuses that category even if its name differs from the generated hierarchy label. If none matches, a hierarchy-based name is generated. The SQL transaction rechecks existing category names and complete unit structures before reuse or insertion. Different ratios, partial structures and ambiguous equivalent categories are not silently merged or overwritten. Select an existing category explicitly to resolve ambiguity.

Older product column orders remain accepted by exact header names; unknown or duplicate headers are rejected. Unit-choice dropdown references are derived from the UOM headers rather than fixed Excel column letters.

Validation for this change: 105 adapter regression checks passed, including UOM matching, incompatible/ambiguous structures, category column ordering, non-KSA dropdown references and old-order product parsing. No target records were inserted for these checks.


## Arabic defaults and selected-category autofill

Across migration inputs, blank Arabic fields copy their corresponding English text before validation and insertion. Existing nonblank Arabic values are preserved. This is a text fallback, not translation; it includes nested row fields and legacy patient/role aliases.

Product downloads use a macro-enabled `.xlsm` workbook for desktop Excel. Changing UOMCategoryName loads the selected target category's unit names, Arabic names and adjacent conversions. Changing a UOM name or conversion matches the complete existing structure or generates a category name. Mixed category/UOM pastes prioritize the unit inputs. UOM names and their next-unit conversions remain interleaved for readability. New Arabic values default to English when blank; existing shared-unit Arabic names are preserved on reuse.

The hidden UOM Updates sheet records the last-edit direction. Upload independently rechecks current database setup: unit edits are retained rather than overwritten by the previous category; category edits must match the selected structure. Ambiguous structures remain invalid until an explicit category is selected. Legacy `.xlsx` uploads remain supported but do not provide same-cell two-way behavior. Product invalid-record exports also use `.xlsm`, retain edit direction, and include errors in Instructions.

External recipients need desktop Excel and permission to run this workbook's macros under their organization's policy. They do not need VBA project object-model access. Do not lower global macro warning settings. VBA only edits this workbook; it does not connect to SQL, call APIs, run shell commands or read/write other files. Database changes still occur only through the portal's authenticated validation/import workflow. Save the file as `.xlsm` to retain the behavior.

The reviewed VBA source is in backend/Data/Vba; the compiled project and worksheet code-name map are in backend/Data/Templates. The package is embedded into each target-scoped workbook at download time. Authoring VBA requires temporary Excel project-model access on the builder's computer only; disable it after building. A checked-in binary is supplied so deployment does not need Excel installed.


Only exact supplied UOM autofill formulas are accepted in product input cells. Other formulas remain rejected. The server ignores formula caches and the uploaded reference sheet's data when deriving the selected category. Invalid/ambiguous/unrepresentable target structures require correction rather than silent rounding or truncation.

117 adapter regression checks passed for the current baseline, including Arabic aliases, preservation, category-driven Excel calculation, unused levels, trusted formula upload and independent server-side category mapping. Tests inserted no target records.


UOM columns are interleaved for reading: UOM1 Name, UOM1 Arabic Name, UOM1 QuantityOfNext, UOM2 Name, UOM2 Arabic Name, UOM2 QuantityOfNext, then UOM3 and UOM4. Read each conversion as **1 previous UOM = quantity of the next UOM**; for example Box, 20, Tablet means 1 Box = 20 Tablets. Category fields follow the complete hierarchy. Category autofill uses field names and unit-choice dropdowns use row-specific name-only ranges, so conversion and Arabic cells are excluded.
