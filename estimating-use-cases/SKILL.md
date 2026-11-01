---
name: estimating-use-cases
description: Use whenever the user asks for sizing, complexity analysis, time, or effort estimations for a feature or set of requirements. This skill strictly enforces the autonomous calculation of Technical and Environmental factors via code inspection and uses the UCP calculation tool to provide objective sizing limits.
---

# Estimating Use Cases

## Core Mandate
You MUST use the `ucp_ucp_calculate_from_factors` tool for all UCP calculations.
**Do not ask the user for factor ratings.** You must objectively analyze the provided requirements and the ACTUAL CODEBASE, determine all factor values (Actors, Use Cases, Technical, Environmental) yourself, and then call the calculation tool.

## Workflow

1. **Analyze Requirements & Codebase:** Read the provided user stories or feature descriptions. For existing systems, use `glob`, `grep`, `read`, or `ado_ado_search_code` to inspect the actual repository architecture.
2. **Determine Factors:** 
   - Count Use Cases and Actors.
   - Evaluate Technical Complexity Factors (T1-T13) and rate them 0-5. **Do not guess!** Look at the code. Are there microservices? (T1=5). Complex SQL joins? (T4=5). 
   - Evaluate Environmental Factors (E1-E8) and rate them 0-5.
   - *CRITICAL:* Read [UCP_FACTORS.md](UCP_FACTORS.md) for the exact definitions of these factors and how to score them.
3. **Calculate:** Compile your determined factors into the required JSON payload and CALL the `ucp_ucp_calculate_from_factors` tool.
4. **Enforce Size Limits:** Analyze the tool's result. **If the returned `standard_weight` (business points) is >= 13, you MUST advise the user that the user story/feature is too large and needs to be broken down into smaller pieces.**
5. **Push Back:** If the user disputes your estimation, require them to provide specific architectural or design details that justify lowering the technical or environmental complexity scores.