# Cache and projection writers

Use schema-study-evidence.json, event-subscriptions.json and the matching schema worksheet. The subscription registry contains 162 source matches across two branches, including 22 explicitly flagged commented declarations. It is a discovery index, not proof that a consumer runs in the selected deployment. Do not combine legacy/newer branches into one guaranteed writer chain.

| Authoritative/change context | Reviewed downstream behavior | Implication for scripts |
|---|---|---|
| MPI patient merge | Source subscriptions across clinical modules; reviewed CS handler refreshes patient identity/display fields only for transferred visits. | Preserve merge scope; not a blanket replacement of every row with an old patient ID. |
| Patient questionnaire | Screening calls MedicalHistory, diagnoses, Allergy and MPI then stores its own questionnaire children. | The snapshot is not the sole source and deleting it does not reverse all prior updates. |
| MedStp physician/setup | OPD has physician/setup and hospital-location subscription candidates; exact selected handler fields must be traced before a rename. | A copied specialty/physician name in another schema is not proof this event updates it. |
| HSM room assignment | Room-save branches update BedMgt and ER/OR projections; OPD medical nurse-station specialty links have a specific condition. | Assignment type AND classification determine which copies to update/remove. |
| PMGT product | Reviewed legacy SaveProduct validates category/UOM/invoice group/type, adds or updates master then emits PMGT_ProductCreated/Updated; delete emits Deleted. | Retiring a product is different from deleting historical orders/stock. |
| CPOE trade-name index | Reviewed legacy subscriber adds/updates only active medication products; update of nonmedication/inactive product removes the trade name; delete removes it. MedicationUpdated refreshes medication-specific index fields. | Index presence is classification-dependent; all products do not belong in trade-name search. |
| Billing and Dental product consumers | Reviewed legacy broker handlers route product create/update/delete through named Service Locator actions and reject non-200 responses. | Follow the destination writer; subscription alone does not establish all copied fields or successful delivery. |
| SC validated goods receipt | Updates PO state, batch barcodes, location balances/reference UOM, average costs, journal identity and publishes PMGT product receipt information. | Copying a balance row cannot reproduce receiving, valuation, finance and external effects. |
| Bed assignment | Updates bed/room state, companions, status/transaction logs and VM accommodation. | Removing one bed transaction leaves other state unless the reviewed reversal is followed. |
| Visit payment synchronization | Payment/invoice synchronization includes recovery and suppressed-transaction behavior in reviewed source. | A success-shaped response/local transaction is not proof all remote components synchronized. |
| NPHIES claim | Historical request/response items, copied patient/contract context, file attachments and external cancellation tasks. | Historical integration snapshots are not ordinary master caches; local delete does not cancel an external claim. |
| NS notifications | Persistence transaction completes before websocket publication; routing uses user/entity/all-entity context. | Do not equate SQL save with message delivery or resend without checking outcome. |
| PatientSummery/Gateway/report views | Derived display and aggregation from base records, sometimes patient-wide or filtered signed/final/insured only. Some rows use NEWID. | Never delete a derived row or infer storage absence from a filtered display. |

## Database-generated fields

Three enabled SC insert triggers were visible in the latest review: ProductBarcode generates Code/Barcode; TransferOut and ReturnToWarehouse append the inserted ID to their prefixes and set Code. Preserve generated values and verify the trigger behavior after a direct insert. Earlier metadata-only results that did not return triggers are not proof of absence.

Historical rules and contractual/claim snapshots can deliberately differ from current master setup. Distinguish those from a stale current projection before proposing updates. Unknown acknowledgement, unprocessed messages and failed-message storage require reconciliation rather than automatic blind replay.
