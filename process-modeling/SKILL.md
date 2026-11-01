---
name: process-modeling
description: Use when the user wants to build, redesign, review, or critique a business process model, process map, or workflow. This skill operationalizes Kevin Tan's "Process-bility" method (Simplicity, Visual Balance, Storytelling) and directly integrates it with your `bpmn_mcp_*` tools to generate valid BPMN 2.0 XML and your `mermaid_*` tools for markdown-based flowcharts.
---

# Process Modeling (Process-bility)

Process-bility is a discipline for producing process models that **communicate**, not just models that are technically correct. This skill integrates the Kevin Tan method directly with your BPMN 2.0 generation and Mermaid tools.

---

## Tool Selection Rule

- **Use BPMN 2.0 (`bpmn_mcp_*`):** When the user asks for a standard BPMN model, formal process diagram, or wants to export/save the workflow as a `.bpmn` or XML file.
- **Use Mermaid (`mermaid_*`):** When the user wants a quick, readable flowchart rendered inline in the markdown response.

---

## Core Process-bility Rules

### 1. Storytelling (The Object of Focus)
- Every process has a **main character**—the single object being tracked (e.g., *Invoice*, *Order*, *Complaint*, *Referral*).
- If you cannot name a single object of focus, the scope is too wide. Re-scope or split the process.

### 2. Naming Standards (Simplicity + Storytelling)
- **Activities (Tasks):** Must be **Verb-First**, action-oriented, and free of roles or systems.
  - *Correct:* "Review Application", "Approve Invoice"
  - *Incorrect:* "Manager Reviews Application" (Role is in swimlane), "Approve Invoice in ERP" (System is metadata/annotation)
  - *Goal-Oriented:* Name the *what*, not the *how*. A stranded person builds a fire to "Get Attention for Rescue", not "Create Smoke".
- **Events:** Must be **Noun + Past Participle** to signal a state reached.
  - *Correct:* "Application Received", "Invoice Approved", "Order Fulfilled"
  - *Incorrect:* "Start", "End", "Receive Application"
- **Gateways:** Do not name the gateway itself. Name the branching paths with the conditions evaluated (e.g., "Approved" / "Rejected").

### 3. Gateway Discipline
- **Gateways route; they do not decide.** The decision is always made in the **task immediately preceding** the gateway. The gateway only evaluates that decision.
- **No Exclusive Merging Gateways:** Do not use an exclusive gateway to merge multiple paths back into a single sequence flow. Simply connect the incoming sequence flows directly to the next activity. This keeps the model visually clean and avoids implying a second decision.

### 4. Visual Layout (Visual Balance)
- **Swimlanes/Pools:** Use a swimlane for each role/team. Use an external pool for parties outside the organization (e.g., *Customer*).
- **No System Swimlanes:** Do not create a swimlane for an application or database. Systems are embedded as labels inside the activity box or attached as a `textAnnotation` via `bpmn_mcp_add_association`.
- **Direction:** Flow strictly left-to-right. Loop-backs/rework are the only exceptions and should flow right-to-left.

---

## Operational Workflow: Generating BPMN 2.0 XML

When using `bpmn_mcp_*` tools, follow this exact sequence:

1. **Initialize the Diagram:**
   Call `bpmn_mcp_init_bpmn` with a descriptive name.
   ```python
   bpmn_mcp_init_bpmn(name="Order Fulfillment Process")
   ```

2. **Add Nodes (in Batch if possible):**
   Determine swimlanes, pools, and tasks. Use `bpmn_mcp_add_node` or `bpmn_mcp_add_multiple_nodes`.
   - Use `element_type="startEvent"` for the trigger (Noun + Past Participle).
   - Use `element_type="userTask"` or `element_type="serviceTask"` for activities.
   - Use `element_type="exclusiveGateway"` or `element_type="parallelGateway"` for routing.
   - Use `element_type="endEvent"` for outcomes (Noun + Past Participle).
   - Specify `pool_name` and `lane_name` to automatically group and lay them out.
   
   *Remember: For swimlanes, represent the role as a person. Embed systems within the tasks.*

3. **Connect Nodes:**
   Use `bpmn_mcp_add_sequence_flow` or `bpmn_mcp_add_multiple_sequence_flows` to draw arrows.
   - For gateways, provide the `condition` parameter to label the paths (e.g., "Yes", "No").
   - NEVER use an explicit exclusive gateway for merging; connect converging flows directly to the target node.

4. **Attach System Metadata / Annotations:**
   Use `element_type="textAnnotation"` to represent systems/databases (e.g., "ERP System").
   Connect it to the corresponding task using `bpmn_mcp_add_association`.

5. **Export:**
   Call `bpmn_mcp_export_bpmn` to compile and write the BPMN 2.0 XML to the filesystem. Provide a clear path (e.g., `order_fulfillment.bpmn`).

---

## Operational Workflow: Generating Mermaid Flowcharts

When using `mermaid_*` tools, follow this sequence:

1. Call `mermaid_mermaid_init(diagram_type="flowchart", direction="left_to_right")`.
2. Use `mermaid_mermaid_add_nodes` to add the steps, applying the Verb-First task naming and Noun + Past Participle event naming.
3. Use `mermaid_mermaid_add_links` to connect them, explicitly labeling decision outcomes.
4. Export the diagram using `mermaid_mermaid_export_diagram(output_filename="process.md")`.

---

## Quality Gate Checklist (The Process Guardian Pass)

Run this self-check before completing any process model:
1. Is there a single, clear **object of focus** moving through its journey?
2. Are all tasks **Verb-First** and free of roles/systems in their names?
3. Are all start/end events **Noun + Past Participle** (e.g., "Payment Settled")?
4. Do gateways purely **route** decisions made by preceding tasks?
5. Are there **zero exclusive merging gateways**?
6. Are systems embedded as annotations rather than given their own swimlanes?
7. Is the flow strictly left-to-right?
