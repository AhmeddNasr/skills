# Notation & Gateway Reference (Process-bility)

This reference document defines the precise semantics of process elements, gateway behaviors, and modeling patterns. Use it to ensure exact compliance with Kevin Tan's Process-bility methodology.

---

## 1. The Five Core Elements

Every business process is modeled using a combination of these five building blocks:

### Event
Something that occurs in the process (starts it, ends it, or marks a milestone).
- **Start Event:** Triggers the process (green). Named as *Noun + Past Participle* (e.g., "Invoice Received").
- **End Event:** Concludes the process (red). Named as *Noun + Past Participle* (e.g., "Refund Issued").
- **Intermediate Event:** Marks a major milestone mid-flow (yellow). Named as *Noun + Past Participle* (e.g., "Document Validated").

### Activity (Task / Sub-Process)
Work being performed.
- **User Task:** The standard activity performed by a human. Left untyped (blank icon) for simplicity.
- **Service Task:** Automated activity performed by an external application/service.
- **Sub-Process:** A decomposable activity containing its own child workflow. Used to hide complexity and keep the high-level diagram on a single page.

### Gateway
Controls the routing of flow. **Gateways route; they do not decide.**
- **Exclusive (XOR):** Splits flow into exactly *one* of several paths based on a decision made in the preceding task.
- **Parallel (AND):** Activates *all* outgoing branches concurrently. Merging waits for *all* branches to finish.
- **Inclusive (OR):** Activates *one or more* paths by evaluating conditions. Use sparingly.
- **Event-Based:** Routes based on which of several *events* occurs first (e.g., waiting for a Customer response OR a 3-day timer).

### Swimlane (Pool & Lane)
Represents a role, team, or department.
- **Pool:** Represents an organization or external party (e.g., "Company", "Customer").
- **Lane:** Sub-divisions within a pool representing specific roles (e.g., "Billing Clerk", "Approving Manager").
- **Rule:** Never create a swimlane for a software system or database. Keep lanes strictly human/role-oriented.

### Connecting Flow
- **Sequence Flow:** Order of activities *within* a single pool (solid line).
- **Message Flow:** Communication *between* separate pools (dotted line with open circle).
- **Association:** Links notes, annotations, or documents to activities (dotted line).

---

## 2. Gateways in Depth

### Exclusive Gateway (XOR)
The branching exclusive gateway evaluates conditions and sends the process down a single path.

**The Restroom-Signage Analogy:**
The sign on a restroom door does not decide your gender; you made that decision before approaching the door. The sign merely routes you to the correct room. Similarly, an exclusive gateway evaluates a decision that has **already been recorded** by the preceding task.

*Example:*
- Task: "Review Insurance Claim" (The claim status is set to Approved or Denied).
- Gateway: XOR routes to "Pay Claim" if status is Approved, or "Send Denial Letter" if Denied.

**Merging XOR Gateway (PROHIBITED):**
Do not use a gateway symbol to merge multiple sequence flows back into a single path. BPMN allows sequence flows to connect directly to the target task. Merging gateways add visual clutter and imply that a decision is taking place at the merge point when none exists.

---

## 3. Event-Based Gateway Rules

Only **Intermediate Catching Events** may follow an Event-Based Gateway. This represents waiting for external triggers:
1. **Message Catch Event:** Waiting for a document, email, or webhook to arrive.
2. **Timer Event:** Waiting for a specific duration or deadline to elapse (e.g., "Wait 48 hours").
3. **Signal Catch Event:** Waiting for a broadcast signal from another running process.
4. **Conditional Catch Event:** Waiting for a specific database/system state to become true.

---

## 4. Modeling Patterns

### Pattern A: Sequential Gateway Consolidation
Instead of chaining multiple XOR gateways sequentially to evaluate multiple conditions, combine them into a single gateway with distinct, clear outflows representing the logical combinations. This maintains Visual Balance and Simplicity.

### Pattern B: The Happy Path (L3 vs L4 Leveling)
- **L3 (E2E Level):** Focus entirely on the "Happy Path"—the standard flow that completes successfully without errors or exceptions. Keep this view extremely clean.
- **L4 (Process Level):** Show the exceptions, rework loops, and edge cases. Decompose L3 tasks into L4 sub-processes to contain this complexity.
