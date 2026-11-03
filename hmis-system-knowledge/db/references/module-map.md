# DotCare schema-by-schema study ledger

Study capture: 2026-10-21, AHJ Prelive. Scope is **48 visible object-bearing schemas**, including **44 containing 2,042 base tables** and four containing projections/SQL logic only. The earlier 44-schema statement counted table-bearing schemas.

Every base table received a bounded safe-column or presence-only sample query. Every declared FK received a bounded child-to-parent sample check. These are study observations, not exhaustive integrity tests or deployed end-to-end UAT. Source-dependent branches and unresolved writers remain explicitly qualified in each finding.

| Schema study | Base tables | Nonempty / empty table samples | SQL objects |
|---|---:|---|---:|
| [Allergy](schemas/Allergy.md) | 16 | 16 / 0 | 0 |
| [BIReport](schemas/BIReport.md) | 0 | projection samples / source review | 2 |
| [BedMgt](schemas/BedMgt.md) | 22 | 21 / 1 | 1 |
| [Billing](schemas/Billing.md) | 132 | 104 / 28 | 1 |
| [BloodBank](schemas/BloodBank.md) | 89 | 84 / 5 | 0 |
| [CN](schemas/CN.md) | 14 | 13 / 1 | 1 |
| [CPG](schemas/CPG.md) | 30 | 28 / 2 | 0 |
| [CPOE](schemas/CPOE.md) | 159 | 144 / 15 | 21 |
| [CS](schemas/CS.md) | 13 | 13 / 0 | 4 |
| [DBA](schemas/DBA.md) | 11 | 11 / 0 | 5 |
| [DotcarePortal](schemas/DotcarePortal.md) | 4 | 4 / 0 | 0 |
| [Drug](schemas/Drug.md) | 4 | 3 / 1 | 0 |
| [ER](schemas/ER.md) | 31 | 31 / 0 | 0 |
| [Finance](schemas/Finance.md) | 204 | 179 / 25 | 53 |
| [FreeChat](schemas/FreeChat.md) | 7 | 7 / 0 | 0 |
| [Gateway](schemas/Gateway.md) | 0 | projection samples / source review | 13 |
| [HR](schemas/HR.md) | 24 | 21 / 3 | 13 |
| [HSM](schemas/HSM.md) | 10 | 10 / 0 | 0 |
| [HangFire](schemas/HangFire.md) | 11 | 8 / 3 | 0 |
| [LR](schemas/LR.md) | 87 | 80 / 7 | 22 |
| [MPI](schemas/MPI.md) | 47 | 43 / 4 | 5 |
| [MedHistory](schemas/MedHistory.md) | 32 | 31 / 1 | 0 |
| [MedStp](schemas/MedStp.md) | 15 | 14 / 1 | 0 |
| [NP](schemas/NP.md) | 46 | 42 / 4 | 0 |
| [NS](schemas/NS.md) | 20 | 17 / 3 | 0 |
| [NewDental](schemas/NewDental.md) | 25 | 25 / 0 | 0 |
| [Nphies](schemas/Nphies.md) | 60 | 54 / 6 | 37 |
| [OPD](schemas/OPD.md) | 48 | 41 / 7 | 4 |
| [OR](schemas/OR.md) | 36 | 34 / 2 | 0 |
| [PA](schemas/PA.md) | 1 | 1 / 0 | 14 |
| [PMGT](schemas/PMGT.md) | 50 | 38 / 12 | 1 |
| [PatPrlm](schemas/PatPrlm.md) | 26 | 22 / 4 | 4 |
| [PatientSummery](schemas/PatientSummery.md) | 0 | projection samples / source review | 58 |
| [PhysicianDesktop](schemas/PhysicianDesktop.md) | 21 | 17 / 4 | 0 |
| [Physiotherapy](schemas/Physiotherapy.md) | 10 | 10 / 0 | 0 |
| [QMS](schemas/QMS.md) | 14 | 14 / 0 | 0 |
| [SC](schemas/SC.md) | 111 | 101 / 10 | 9 |
| [SHR](schemas/SHR.md) | 1 | 1 / 0 | 0 |
| [Screening](schemas/Screening.md) | 27 | 26 / 1 | 0 |
| [Security](schemas/Security.md) | 33 | 29 / 4 | 1 |
| [SerLoc](schemas/SerLoc.md) | 4 | 4 / 0 | 0 |
| [Shared](schemas/Shared.md) | 34 | 33 / 1 | 51 |
| [VS](schemas/VS.md) | 26 | 24 / 2 | 10 |
| [VisitMgt](schemas/VisitMgt.md) | 209 | 184 / 25 | 55 |
| [dbo](schemas/dbo.md) | 175 | 146 / 29 | 77 |
| [impreports](schemas/impreports.md) | 0 | projection samples / source review | 9 |
| [itreports](schemas/itreports.md) | 98 | 87 / 11 | 122 |
| [reports](schemas/reports.md) | 5 | 4 / 1 | 822 |

## How to use the evidence

- Start with the schema study for the observed cycle and its limits. Every base table remains listed there.
- catalog/<Schema>.json: full captured base-table structure, indexes and FK mappings.
- samples-bundle.json (schema <Schema>): two-row safe identifier/state samples or presence-only checks; not all rows.
- setup-vocabularies-bundle.json (schema <Schema>): static vocabulary/configuration key samples, TOP31 with truncation flags; configuration values require targeted review.
- sql-objects/<Schema>.json: view/function columns, procedure parameters and syntactic dependency map. Dynamic SQL and external calls can be missing.
- schema-study-evidence.json: source paths/ranges/hashes, SQL definition hashes and user-confirmed HR entry point.
- cache-writers.md and event-subscriptions.json: reviewed cache mechanisms and version-specific subscription discovery, including commented declarations.
- fk-sample-evidence.json: 2,132 constraint checks, up to two child rows per relationship.
- cohort-evidence.json: 120 indexed patient/visit/product seed predicates; nonindexed candidates were deferred to avoid broad scans.
- security-flow.md, core-flows.md and visit-evidence-study.md: deeper earlier studies.

## Completion meaning

The all-table sampling and structural/dependency passes are complete for the visible snapshot. The schema-level flow review includes source/database-supported findings, but does not certify every business branch, deployed assembly, external acknowledgement or cancellation path. Do not generate an exhaustive destructive script solely from this ledger.