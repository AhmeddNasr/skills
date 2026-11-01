---
name: azure-tasks
description: Use whenever the user wants to create Azure DevOps Tasks or work items for time tracking — including requests that just list task names and hours (e.g. "Demo 2, Farewell 1"), "create tasks", "log my work", "fill timesheet", "log meeting hours", or anything about the "Nasr" PBI. ALWAYS load this skill before using any Azure DevOps MCP tool for task creation.
---

# Purpose

This skill creates Azure DevOps Tasks for time logging using the connected Azure DevOps MCP.

---

# General Rules

## MANDATORY: Always Use This Skill for Tasks
Any request to create Azure DevOps Tasks or log time MUST go through this skill's flow. Do NOT use the raw Azure_ado_create_work_items / Azure_ado_update_work_items MCP tools directly. For every task: determine the current Business Analysis sprint, ensure it is linked to the PBI "Nasr", set Activity = Meeting, Actual Work = Original Estimate, assign to Ahmed Nasr Younes Abdelwahed, create as To Do, then set State to Done.

## Determine Current Sprint

Before performing any other action:

1. Query Azure DevOps to determine the current iteration/sprint for the Business Analysis team.
2. Use this sprint for every Product Backlog Item and Task created by this skill.
3. Never hardcode or assume the sprint name.

If the current sprint cannot be determined, stop and report the error.

---

## Product Backlog Item

Every task must belong to a Product Backlog Item.

1. Search the current Business Analysis sprint for a Product Backlog Item named exactly:

Nasr

2. If it exists:
   - Ensure it belongs to the current sprint.
   - If it does not, move it to the current sprint.
   - Link every created task to it.

3. If it does not exist:
   - Create a Product Backlog Item named exactly:
     Nasr
   - Assign it to the current Business Analysis sprint.
   - Link every created task to it.

Never create more than one Product Backlog Item named "Nasr" for the current sprint.

---

## Assignment

Assign every created Task to:

Ahmed Nasr Younes Abdelwahed

(@me)

Never ask who the assignee should be.

---

## Task Defaults

Every created task must have:

- Activity = Meeting
- State on creation = To Do
- Original Estimate = provided hours
- Actual Work = exactly equal to Original Estimate

Immediately after successfully creating the task:

- Change the State to Done.

Never leave any of these fields empty.

---

# Flow 1 - Explicit Task Creation

Use this flow whenever the user supplies task names and hours.

Example input:

Live support, 2
Meeting with Pharmacy, 1
Update documentation, 3

For each entry:

- Create one Azure DevOps Task.
- Title = supplied task name.
- Original Estimate = supplied hours.
- Actual Work = supplied hours.
- Activity = Meeting.
- Assign to Ahmed Nasr Younes Abdelwahed.
- Link to Product Backlog Item "Nasr".
- Create as To Do.
- Update State to Done.

Do not modify task titles.

---

# Flow 2 - Fill Remaining Hours

Only use this flow when the user explicitly requests it.

Never invoke this flow automatically.

## Step 1

Determine the total Actual Work already logged by Ahmed Nasr Younes Abdelwahed today.

## Step 2

Calculate:

Remaining Hours = 8 − Logged Hours

If Remaining Hours ≤ 0:

Stop and report that today's 8-hour target has already been reached.

## Step 3

Generate enough tasks so that:

- Total Original Estimate = Remaining Hours
- Total Actual Work = Remaining Hours

Allowed task titles:

- Live support
- Team support
- Update user stories

Rules:

- Every task duration must be a whole number.
- Durations must be randomized.
- The total must equal Remaining Hours exactly.
- Do not always generate the same distribution.
- Any title may appear more than once if necessary to reach the required total.

Every generated task follows all General Rules.

---

# Completion Summary

After all operations succeed, report:

- Current sprint used
- Product Backlog Item reused or created
- Number of tasks created
- Total hours logged