# Finance migration and dependency verification

The Finance workbook handles chart-of-account setup, banks and branches, bank accounts, cost centers, cash points, journals, entity-type account links and owner account assignments. Related bank accounts, branches, contacts and account assignments remain in numbered columns on their master row. Journal rows now include two document-type selections from the destination database.

## Reviewed workflows

| Master | Related setup / generated data | Verification |
| --- | --- | --- |
| Finance.Account | Parent hierarchy, generated Code/DummyCode, nature derived from account type, payment priority and cash-flow group | Requested values and active/deleted state are compared; hierarchy parent and account nature are checked. New account codes are checked against generated DummyCode; legitimate previously edited codes can be reused. |
| Finance.Bank | Country, branches, branch cities, optional Finance.ContactPerson | Branch identities and supplied fields are checked. City must belong to bank country. Contacts are compared when supplied. |
| Finance.BankAccount | Bank/branch relationship, account type, generated bank-account code, Finance.VMPaymentMethodsMapping | Correct bank owns the branch. Payment names, bank payment type, credit-card flag, entity and owner link are verified. |
| Finance.CostCenter | Parent and hierarchy | Requested names/code/status and hierarchy parent are verified. |
| Finance.CashPoint | Finance.VMPaymentMethodsMapping | Names, cash payment type, false credit-card flag, entity and owner link are verified. |
| Finance.Journal | Document types, native child-fiscal-period links, manual/automatic timing conventions, one-day report limit | Supplied document-type IDs must exist uniquely. Fiscal-period links must exist. Manual/zero-period time units normalize to null as in native code. |
| Finance.EntityTypeAccount | Target account and owner-type setup | Requested link/display values and a valid active account/type are checked. |
| Finance.AccountAssignment | Owner master, main/posting account and cached OwnerCode/OwnerEnName/OwnerArName | Cached fields are compared with the owner-specific native projection. Bank-account owner code is BankAccountCode; employee/company names use their native columns. |

The source is the current BackOffice-Main/Finance native controllers, managers and manager factories, supported by the previously captured AHJ Prelive metadata. No new journal entries, payments, balances, visits or transaction history are manufactured by these setup flows. Required HMIS static enums and the fiscal calendar must already be installed/configured. This implementation does not migrate the fiscal calendar or general-ledger opening transactions.

## Existing data and safe retries

Compatible existing masters are reused; conflicting setup is reported. Missing branches on an existing compatible bank are added in a serializable transaction that preserves every existing branch/contact. This narrow append follows the reviewed native Bank.Add fields and audit behavior rather than using Bank.Edit, whose replacement semantics can delete omitted branches. A conflict in any supplied branch rolls back that append transaction. ContactPerson is scoped through its owning bank branch; the physical ContactPerson table has no EntityID column.

Generated hierarchy, nature, system flags, transaction flags and payment-mapping IDs cannot be assigned from source data. The ambiguous legacy BankAccountID reference remains excluded rather than treated as a verified GL-account link. Use the reviewed owner account-assignment flow for account mappings.

Source owner identities and destination business codes are supported. A numeric source identity is never automatically assumed to be a destination ID. Verified finance-owner identities emitted by the product migration graph are recognized; arbitrary graph table names are ignored.

A confirmed master whose related/cache check fails is recorded as SavedNeedsReview with its target ID and a warning. It counts as existing saved data and is excluded from ordinary duplicate input corrections. Validation can recheck it without issuing another native creation. Unacknowledged native submissions remain Unknown and are blocked from automatic retry.

## External integrations

Native bank-account and cash-point creation publish Odoo_JournalCreated after saving local payment mappings. SQL confirmation proves the local records only. It does not prove broker delivery, consumer processing or Odoo acknowledgement. The portal does not fabricate that acknowledgement or publish the event again.

## Current verification status

- Backend build passed with zero warnings/errors.
- 31 finance checks passed, including live lookups and rollback-only branch/contact insertion, reuse, conflict and batch rollback checks. No persistent test inserts remain.
- 47 existing adapter regression checks passed.
- Workbook exported and visually reviewed.
- AHJ Prelive is ONLINE and accessible again. Read-only review covered 16 existing finance records: 14 verified; two account assignments need owner-type projection coverage before their caches can be certified. Existing records were not repaired.
- Signed-in native API upload acceptance and external Odoo acknowledgement remain pending.

See Finance-Sample-Verification.json for individual sample results. SQL checks do not establish external-event delivery.
