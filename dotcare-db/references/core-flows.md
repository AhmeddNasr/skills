# Visit and product anchors

Evidence: October 2026 source and read-only samples; detailed citations and limitations in visit-evidence-study.md. These are not a substitute for deployed workflow tests.

VisitClassification: OPD=1, IPD=2, AMB=3, ER=4. FinancialStatus is separate (cash=1, insured=2). Do not substitute VisitType IDs for classification. Virtual ER has a separate extension path and cannot be assumed to have ordinary triage rows.

SC ProductType distinguishes stockable=1, nonstockable=2 and service=3. Classification follows category and affects projections. Visit service classifications observed: medication1, consumables2, medical services3, procedure4, lab5, radiology6, other7, package8, operation9, blood10, microbiology11. Offers12 exists in SC classification but was not present in the reviewed VisitService classification lookup. A name containing package/offer does not establish classification.

## Service path

Visit -> VisitService -> Billing.PatientTransaction -> Finance.InvoiceTransaction is the reviewed billing chain. Validate visit, service and product across links. OrderlineID can identify medication-order lines or selected CPOE.Orders rows; legacy order-line tables also exist. Resolve family before joining. Clinical result/administration and stock execution are additional lifecycles, not implied by service creation.

71 sampled products had matching identity sets in SC/Billing/PMGT, which does not prove every cached attribute is correct. A product migration adapter's supported setup must not be confused with full laboratory/specimen/operation/package setup. Use Product-Drug-Integration.md for explicit exclusions.

## Package identity and cycle

1. Billing.Package is master configuration; purchase creates a Billing.PatientPackage snapshot sharing its primary key with its purchase Billing.PatientTransaction. That key is not an ordinary independent SQL identity.
2. The package header is a VisitMgt.VisitService classified as package. VisitPackagesAssignment.PackageServiceID references this header VisitService.ID (user-confirmed and supported by source/samples), not PatientPackage.ID.
3. A consumed member's VisitService.ServicePackageID links to the header VisitService; member.PatientPackageID links to the purchased PatientPackage. Member.BillingTransactionId links to its OWN billing transaction. These identities must remain separate.
4. Non-IPD package ordering source expands configured children; investigation families can expand one child per quantity unit. IPD source skips immediate expansion and later admission services price against timed packages. Assignment alone does not prove consumption.
5. Purchase-time rules are historical snapshots. Master edits and purchase snapshots may legitimately differ; script changes can also cause drift. Do not blindly resynchronize them.
6. IsConsumed alone was not authoritative in the reviewed samples. Compare relationships, quantities, assignment and billing state.
7. Cancellation checks use/assignment in current and other visits. Soft deleting one row bypasses that business cycle.

No active operation-class example or active cross-visit package consumption was demonstrated by the checked sample set. Do not claim those paths verified. Blood quantities can use different normalized units: do not infer a payable remainder by subtracting displayed values without UOM/pricing verification.

## Limits

Visible metadata does not expose all trigger/writer definitions. The deployed writer populating ServicePackageID was not located in reviewed source. Historical tax rows on cancelled parents and an IPD time-window anomaly are observations potentially affected by scripts, not confirmed product defects. Active-parent filtering and financial reconciliation need deliberate review. SQL scale differences can explain rounded VisitService prices versus high-precision billing values.
