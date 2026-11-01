---
name: skill-creator
description: Guide for creating universally compatible Agent Skills for AI coding agents (OpenCode, Claude, Gemini CLI). Use this when tasked with creating, designing, or updating an agent skill.
---

# Agent Skill Creator

Guide for creating Agent Skills that extend AI agent capabilities.

> **CRITICAL RULE - WRITE ONCE, RUN ANYWHERE:**
> NEVER create separate skills for different platforms (e.g., one for OpenCode, one for Claude, one for Gemini). 
> The Agent Skill format is universally compatible. A single skill directory containing a `SKILL.md` file with YAML frontmatter works seamlessly across OpenCode, Claude Desktop, and Gemini CLI.

## About Skills

Skills are modular, filesystem-based knowledge packages that transform general-purpose agents into specialized experts. They provide:

1. **Procedural knowledge** — Multi-step workflows for specific domains
2. **Framework expertise** — Best practices, architecture patterns, and conventions
3. **Domain context** — Schemas, business logic, company-specific patterns
4. **Bundled resources** — Scripts, reference docs, templates for complex tasks

---

## Core Principles

### 1. Universal Compatibility

All modern agents (OpenCode, Claude, Gemini CLI) share the same underlying skill architecture.
- **Do not** write platform-specific prompts or logic.
- **Do not** duplicate skills across different `.claude/`, `.opencode/`, or `.agents/` directories for the same repository.
- Pick one standard directory (e.g., `.opencode/skills/` or `.agents/skills/`) and put your skill there. The agent will discover it.

### 2. Concise is Key

The context window is a shared resource. Challenge each piece of information: "Does this justify its token cost?"
Agents are already capable coders. Only add what they don't already know (e.g., custom organizational standards, undocumented internal APIs, specific workflow sequences).

### 3. Progressive Disclosure (The 3 Levels)

Skills leverage the agent's VM/filesystem access to load information in stages, rather than consuming context upfront.

| Level | When Loaded | Token Cost | Content |
|-------|------------|------------|---------|
| **1: Metadata** | Always (at startup) | ~100 tokens | `name` and `description` from YAML frontmatter. Used for discovery. |
| **2: Instructions** | When Skill is triggered | < 5k tokens | `SKILL.md` body with instructions and guidance. Loaded via `bash` or `read`. |
| **3: Resources** | As needed | Unlimited | Bundled files (scripts, markdown docs) executed or read only when referenced. |

**Keep SKILL.md under 500 lines.** Split into reference files in a `references/` directory when approaching this limit.

---

## Skill Structure & Placement

Create one folder per skill name and put a `SKILL.md` inside it.

### Valid Locations

Agents search these locations (walking up from the current directory to the git root, plus global configs):
- `.opencode/skills/<name>/SKILL.md`
- `.agents/skills/<name>/SKILL.md`
- `.claude/skills/<name>/SKILL.md`
- Global: `~/.config/opencode/skills/`, `~/.agents/skills/`, `~/.claude/skills/`

### Directory Layout

```text
<name>/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/      — Executable code (e.g., python scripts the agent can run via bash)
    ├── references/   — Documentation loaded via file reading as needed
    └── assets/       — Output resources (templates, boilerplate)
```

### Frontmatter Rules (REQUIRED)

Every `SKILL.md` must start with YAML frontmatter. Unknown fields are ignored.

```yaml
---
name: your-skill-name
description: Extract text and tables from PDF files. Use when working with PDF files or when the user mentions document extraction.
---
```

**Name Rules:**
- 1–64 characters.
- Lowercase alphanumeric with single hyphen separators (`^[a-z0-9]+(-[a-z0-9]+)*$`).
- **Must match the directory name** containing the `SKILL.md`.

**Description Rules:**
- 1-1024 characters.
- **Crucial:** Must describe BOTH *what* the skill does AND *when* the agent should use it (trigger conditions).

---

## How to Author a Great Skill

### 1. Define the Trigger
Write a clear description in the frontmatter. The agent reads this to decide if it should load the skill.
*Good*: "Create consistent React components. Use when the user asks to create a new UI component, button, or layout."

### 2. Write the Core Instructions (`SKILL.md`)
Provide clear, step-by-step guidance.
- Give a **Quick Start** or minimal example.
- Define **Rules/Anti-patterns** ("Never do X, always do Y").
- Link to bundled resources for edge cases.

### 3. Use Bundled Resources
If a workflow is complex, don't bloat `SKILL.md`.
- Provide templates in `assets/`.
- Provide deep-dive explanations in `references/edge-cases.md`.
- Provide deterministic helper scripts in `scripts/validate.py` that the agent can run via bash.

### 4. Security Considerations
- Remind users that skills have filesystem and bash access.
- Avoid instructing the agent to blindly execute code fetched from unverified external URLs.

## Example Skill

**File:** `.opencode/skills/git-release/SKILL.md`

```yaml
---
name: git-release
description: Create consistent releases and changelogs. Use this when preparing a tagged release or bumping versions.
---

# Git Release Workflow

## What I do
- Draft release notes from merged PRs
- Propose a version bump
- Provide a copy-pasteable `gh release create` command

## Workflow
1. Run `git log --oneline $(git describe --tags --abbrev=0)..HEAD` to get recent commits.
2. Read `references/changelog-format.md` to see how to format the output.
3. Ask the user to confirm the version bump (Major/Minor/Patch).

## Rules
- Never push tags directly without user confirmation.
```

---

## Advanced: Permissions (OpenCode specific)
*(Note: While skill structure is universal, permissions configuration is specific to the OpenCode runner)*

You can control which skills agents can access using pattern-based permissions in `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```