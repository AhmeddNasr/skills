# Vital Signs (`VS` schema)

## Don't repeat (past corrections — always read this section)

- 2026-11-01 — [Physician Desktop / Vitals] Assumed: vitals arrows compare with the previous reading, abnormal rows get a red "critical" highlight, See all opens a trend popup, widget has Print. → Actually: arrow = the vital's High/Low status (normal = no arrow), no highlight, See all goes to the Vital Signs screen, Print out of scope. (PBI 51348)


## Tables [Confirmed — prelive DB, 2026-11-01]

- `VS.LKP_VitalSign`: vital sign catalogue (`EnName`, `ArName`, `ShortName`, `UnitOfMeasure`, `Icon`, `Color`, `MinValue1/2`, `MaxValue1/2`, LOINC/NPHIES codes). IDs: 1 Temperature (C°), 2 Blood Pressure (mmHg), 3 Pulse Rate (bpm), 4 Respiratory Rate (rpm), 5 Venous blood pressure, 6 Oxygen Saturation (%), 7 Level of Consciousness, 8 Pain Scale (/10), 9 Random Blood Sugar (mg/dL).
- `VS.VitalSignTransaction`: one row per recorded vital (`Value1`, `Value2` for BP, `VisitID`, `PatientID`, `TransactionDateTime`, `VitalStatusID`, `VitalScoreID`, `AgeNormalRangeID`, `IsDraft`, `IsDeleted`).
- Status chain: `VitalSignTransaction.VitalStatusID` → `VS.SLKP_VitalAgeStatusRange.ID` (`StatusID`, `IsNormal`, min/max per age range) → `VS.SLKP_Status.ID` (`EnName`, `ArName`, `Icon`, `Color`). Ranges are per age range via `VS.SLKP_VitalAgeNormalRange` (`AgeRangeID`, `VitalSignID`).
- Many readings have **no status** (`VitalStatusID` NULL — about 60% of readings since 2026-09 for temp, BP, pulse, resp, SpO₂, RBS).

## Statuses (`VS.SLKP_Status`) [Confirmed — prelive DB, 2026-11-01]

- **There is no "critical" status.**
- Temperature, Blood Pressure, Pulse, Respiratory Rate, Random Blood Sugar: 1 High (`#ff0109`), 2 Normal, 3 Low.
- Venous blood pressure: only 2 Normal.
- Oxygen Saturation: 4 Normal, 6 Mild hypoxemia, 7 Moderate hypoxemia, 8 Severe hypoxemia.
- Level of Consciousness (AVPU): 9 Alert, 10 Reacting to voice, 11 Reacting to pain, 12 Unresponsive (all flagged `IsNormal = 1` in the ranges table).
- Pain Scale: 13 No Pain, 14 Mild Pain, 15 Moderate, 16 Severe, 17 Very Severe, 18 Worst Pain.

## How vitals are shown in stories [Confirmed — user, 2026-11-01]

- The up/down arrow on a vital is **its status, not a comparison with the previous reading**: up = High, down = Low, Normal = no arrow.
- No red row highlight / "critical" styling on vitals — arrows only.
- The Summary vital signs widget's "See all" goes to the Vital Signs screen (no popup). Printing the widget is out of scope (2026-11-01).
- Confirmed for PBI 51348 (rev 12): arrows on both latest and previous values, each by its own status; no saved status = no arrow; Venous BP never shows an arrow (only Normal exists); SpO₂, Pain and Consciousness show the value only; See all opens the existing physician-portal Vital Signs screen for the same patient; widget is read-only; name "Random blood sugar". [Confirmed — user, 2026-11-01]
