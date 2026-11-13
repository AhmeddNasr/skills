---
name: openrouter-limit
description: Check the user's current OpenRouter key usage and remaining key limit using their locally saved script and token. Use when the user asks "my limit", "check my limit", "how much limit is left", "my OpenRouter usage", or asks for today's, this week's, or this month's OpenRouter spending. Return only those four values; do not confuse these with an account balance or another provider's quota.
---

# OpenRouter limit check

Run the local script on every request for a current limit. Do not reuse old results.

```powershell
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "C:\Users\ahmed-abdelwahed\.config\opencode\check-openrouter.ps1" -LimitOnly
```

The script reads the user's saved token from its `SavedApiToken` setting, falling back to `OPENROUTER_API_KEY`. It calls only `GET https://openrouter.ai/api/v1/key`; the account credits endpoint is not needed.

## Response

Return the four values using exactly this layout: a **Usage:** title, a three-column Markdown table with one data row, then the remaining limit below the table. Preserve the returned precision and USD units. All usage periods are UTC.

```markdown
**Usage:**

| Today (UTC) | Week (UTC) | Month (UTC) |
| ---: | ---: | ---: |
| USD ... | USD ... | USD ... |

**Limit remaining:** USD ...
```

Render this as Markdown, not inside a code block. Do not add other metrics or explanatory text on a successful check.

The first three values are spending, not remaining allowances. Weeks run Monday-Sunday in UTC. The fourth is the key's remaining spending limit, not the account balance. If the script reports no key-specific limit, say that; do not claim unlimited account credits. Never convert a missing value to zero.

## Safety and failures

- Execute the `.ps1` directly with `-LimitOnly`; the `.cmd` launcher pauses and is for interactive double-click use only.
- Do not read, print, copy, embed in commands, or add the token to this skill or responses. Execute the saved script without inspecting its credential setting.
- Do not use `-ShowJson`, alter limits, rotate credentials, or call inference endpoints.
- If the script is missing, credentials are unconfigured, the request fails, or any value is unavailable, report the actual failure or unavailable values without inventing a result. Ask the user to configure `SavedApiToken` locally if necessary; never ask them to paste the token into chat.
- If context clearly refers to another service's limit, do not run this skill for that service.
