# Migration conventions, not universal business rules

Read the matching integration document before import design. Revalidate against the selected database and entity; production/prelive lookup equivalence was a user statement about those environments, not permission to reuse IDs everywhere.

- SLKP tables provide static target choices and application enums; never fabricate missing enum IDs. The under-30-row export filter is a size policy, not a definition of a static lookup. Editable LKP/master setup can require migration or native creation.
- Resolve names/codes to target IDs in environment scope. Preserve source-to-target mappings and ambiguity errors. Parent country/city/region creation must respect actual relationships. Excel dropdowns are convenience, not server validation.
- Arabic blank -> English is a migration fallback, not translation. IsActive=true and IsDeleted=false are reviewed import conventions, not permission to reactivate unrelated existing records.
- MigrationCreatedBy is configurable per environment (reviewed default77777). Patient OccupationID13, false boolean defaults and null LastClassificationID are adapter-specific choices. Do not generalize them to clinical transactions.
- Preserve Excel patient code. One row carries patient/address/contact aggregate; insert dependent masters first and owned children atomically. A blank SourceRecordID uses stable migration tracking, distinct from SQL identity.
- Product rows resolve category, up to four descending UOM levels and ratios. Read 1 preceding UOM = QuantityOfNext next UOM. Reuse only complete compatible unit structures including reference unit; reject ambiguity/different ratios. Do not duplicate a shared structure just because category labels differ.
- Physician migration includes all types without HR/user provisioning. Scheduling means OPDPattern; housing is separate.
- HSM setup migration was deferred. Studying assignment-dependent cache routing does not authorize implementing it.
- NPHIES is conditional on KSA environment configuration.
- Valid imported rows can save directly where the adapter supports it. Invalid rows remain correctable. Lost acknowledgement is Unknown, not a safe automatic retry; reconcile actual target state first.
- Native events/index rebuilds are separate postcommit effects. Local SQL confirmation does not prove broker delivery, consumer acknowledgement or completed search indexing.

Migration portal persistence uses its existing protected local store; do not assume a DotcarePortal schema table is the migration state store merely from its name. Never include credentials in skill files or logs.
