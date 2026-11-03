# Warehouse setup migration

Choose **Supply Chain → Warehouse setup - categories, assignments and structures** and download a fresh workbook for the target environment and entity. Enter one warehouse per row.

Choose an existing warehouse category or fill the new category's English name, Arabic name and prefix on the same row. A new category can use an existing parent category. Optional related columns support two employees, functions, product categories and routes, plus two structure levels with two details each. Employee names, codes, departments and sections are populated from the target HR hierarchy. Active/deleted flags and native warehouse codes are generated internally.

The portal calls the native warehouse-category and warehouse-creation endpoints. Warehouse creation saves employee caches, functions, product-category assignments, bidirectional routes and structure details through HMIS. The native warehouse event synchronizes `PMGT.LKP_Warehouse` and `PMGT.WarehouseCategoryAssignment`.

The importer verifies the base warehouse and requested related setup. It confirms PMGT names, active state, entity and product-category assignments. A warehouse whose base setup is confirmed but cache is not ready is marked **SavedPendingCache**, counted as saved data, and excluded from input corrections. Background checks confirm synchronization without submitting warehouse creation again. Persistent pending or conflicting caches require review of the native event consumer. Unconfirmed native writes block automatic retry.

Existing warehouses are reused only when their base fields and requested assignments are compatible. Missing assignments on an existing warehouse are reported for review; the importer does not use a replacement edit that could remove other assignments. The native workflow generates warehouse codes from the category prefix, so source codes are not forced into the target code sequence.

The dedicated workbook covers warehouse-category and basic warehouse setup with structure definitions. Physical bin/location creation, location product assignments, opening stock and valuation remain separate workflows. The older consolidated supply-chain workbook can also invoke the warehouse adapter, but unrelated filled sheets remain staged and are reported separately.

Prerequisites: current HMIS login, target entity access, active HR employee/position/section/department setup for assigned staff, seeded warehouse functions/classifications, and compatible SC/PMGT product categories. Hospital setup is deferred. Its future cache rules must use both `HSM.HSAssigment.AssignmentTypeID` and `AssignmentClassificationID`.

Verification: 19 focused checks passed, including workbook parsing, nested structure source links, correction re-upload, native response handling and live target dropdowns. Two existing warehouse/cache samples matched. These checks only read the target; native warehouse insertion and broker delivery still require an authenticated user acceptance upload.
