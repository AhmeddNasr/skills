# Agent Skills Repository

A curated collection of modular, filesystem-based skills that transform general-purpose AI coding agents into specialized experts. Each skill is a self-contained knowledge package compatible with **OpenCode**, **Claude Desktop**, and **Gemini CLI**.

## What Are Skills?

Skills are procedural knowledge packages that provide:

- **Procedural knowledge** -- Multi-step workflows for specific domains
- **Framework expertise** -- Best practices, architecture patterns, and conventions
- **Domain context** -- Schemas, business logic, company-specific patterns
- **Bundled resources** -- Scripts, reference docs, and templates for complex tasks

## Available Skills

### Business Analysis & Architecture

| Skill | Description |
|-------|-------------|
| [business-architecture](./business-architecture/) | Connect strategy to capabilities, value streams, information, and organization |
| [architecture-review](./architecture-review/) | Review system architecture -- module boundaries, layer patterns, integration points |
| [domain-concept-modeling](./domain-concept-modeling/) | Establish controlled vocabulary, taxonomy, and conceptual business models |
| [information-data-modeling](./information-data-modeling/) | Turn conceptual models into logical data models, dictionaries, and lineage |
| [process-modeling](./process-modeling/) | Build, redesign, or critique business process models and workflows (BPMN 2.0) |
| [decisions-business-rules](./decisions-business-rules/) | Model decisions and business rules using DMN and SBVR discipline |
| [practice-governance](./practice-governance/) | Convert external standards into daily operating rules and traceability |

### Requirements & Validation

| Skill | Description |
|-------|-------------|
| [eliciting-business-needs](./eliciting-business-needs/) | Root cause analysis and clarifying questions to define true business requirements |
| [structuring-requirements](./structuring-requirements/) | Create PRDs, Epics, User Stories, and Architecture-Aware Acceptance Criteria |
| [validating-project-scope](./validating-project-scope/) | Review and audit requirements applying INVEST criteria and Definition of Ready |
| [estimating-use-cases](./estimating-use-cases/) | Sizing, complexity analysis, and effort estimations using UCP |
| [evaluating-solution-value](./evaluating-solution-value/) | Define success metrics, KPIs, and prove ROI after release |
| [verification-validation-testing](./verification-validation-testing/) | Prove conformance to requirements and meet the real business need |

### Development & Engineering

| Skill | Description |
|-------|-------------|
| [refactor](./refactor/) | Surgical code refactoring to improve maintainability without changing behavior |
| [angular-new-app](./angular-new-app/) | Scaffold new Angular applications and configure workspaces |
| [angular-component-architecture](./angular-component-architecture/) | Build Angular components with Container/Presentational separation and signals |
| [angular-security-perf](./angular-security-perf/) | Optimize performance, configure SSR, and prevent XSS in Angular |
| [dotnet-best-practices](./dotnet-best-practices/) | Ensure .NET/C# code meets best practices |
| [dotnet-design-pattern-review](./dotnet-design-pattern-review/) | Review .NET code for design pattern implementation |
| [dotnet-upgrade](./dotnet-upgrade/) | Comprehensive .NET framework upgrade analysis and execution |
| [temporal-developer](./temporal-developer/) | Develop, debug, and manage Temporal applications in .NET |
| [legacy-orchestration-migration](./legacy-orchestration-migration/) | Migrate distributed-transaction endpoints to orchestrated workflows |
| [frontend-design](./frontend-design/) | Create production-grade frontend interfaces and design systems |
| [frontend-design-review](./frontend-design-review/) | Review frontend interfaces against design quality and accessibility standards |

### Security, Compliance & Governance

| Skill | Description |
|-------|-------------|
| [security-privacy-compliance](./security-privacy-compliance/) | Build security, privacy, and regulatory compliance into solutions |
| [ai-integration-governance](./ai-integration-governance/) | Govern AI integrations -- classify risk, assess safety, make Go/No-Go decisions |

### DevOps & Research

| Skill | Description |
|-------|-------------|
| [devops-rollout-plan](./devops-rollout-plan/) | Comprehensive rollout plans with deployment, verification, and rollback |
| [conducting-market-research](./conducting-market-research/) | Industry landscape, competitors, SWOT analyses, and Voice of Customer summaries |

### Meta

| Skill | Description |
|-------|-------------|
| [skill-creator](./skill-creator/) | Guide for creating universally compatible Agent Skills |

## Skill Structure

Each skill follows the same layout:

```text
<skill-name>/
├── SKILL.md              # Required -- YAML frontmatter + markdown instructions
└── (optional)
    ├── scripts/          # Executable code the agent can run via bash
    ├── references/       # Documentation loaded on demand
    └── assets/           # Templates, boilerplate, and output resources
```

### SKILL.md Format

Every skill must contain a `SKILL.md` with YAML frontmatter:

```yaml
---
name: your-skill-name
description: What the skill does and when to use it (trigger conditions).
---

# Skill Title

Instructions, workflows, rules, and references...
```

**Name rules:** 1-64 characters, lowercase alphanumeric with hyphens, must match the directory name.

**Description rules:** 1-1024 characters, must describe both *what* the skill does AND *when* the agent should use it.

## Installation

Place skills in any of these locations (agents search from current directory up to git root, plus global configs):

```text
.opencode/skills/<name>/SKILL.md
.agents/skills/<name>/SKILL.md
.claude/skills/<name>/SKILL.md
```

Global locations:

```text
~/.config/opencode/skills/
~/.agents/skills/
~/.claude/skills/
```

## Contributing

### Creating a New Skill

1. **Create a directory** named after your skill using kebab-case (e.g., `my-new-skill/`)
2. **Add `SKILL.md`** with required YAML frontmatter (`name` and `description`)
3. **Write clear instructions** in the markdown body:
   - Start with a brief summary of what the skill does
   - Provide step-by-step workflows
   - Define rules and anti-patterns
   - Link to bundled resources for edge cases
4. **Add bundled resources** (optional):
   - `scripts/` for executable helper scripts
   - `references/` for deep-dive documentation
   - `assets/` for templates and boilerplate
5. **Keep it concise** -- `SKILL.md` should be under 500 lines. Split into reference files when approaching this limit.

### Skill Quality Checklist

- [ ] `name` in frontmatter matches the directory name exactly
- [ ] `description` includes both *what* the skill does and *when* to trigger it
- [ ] Instructions are clear, step-by-step, and actionable
- [ ] No platform-specific logic -- skills must work across OpenCode, Claude, and Gemini CLI
- [ ] `SKILL.md` is under 500 lines (split into `references/` if needed)
- [ ] No secrets, API keys, or sensitive data included
- [ ] Bundled scripts are deterministic and safe to execute

### Submission Process

1. Fork or clone this repository
2. Create a feature branch: `git checkout -b skill/my-new-skill`
3. Add your skill following the structure above
4. Test your skill with at least one agent (OpenCode, Claude, or Gemini CLI)
5. Commit with a descriptive message: `git commit -m "Add my-new-skill skill"`
6. Push and **create a pull request**
7. **Add the R&D team as reviewers** on the pull request -- all contributions require R&D team approval before merge

> **No pull request will be merged without R&D team review and approval.** Please ensure the R&D team is added as a reviewer when creating your PR.

### Updating an Existing Skill

1. Create a branch: `git checkout -b update/skill-name`
2. Make your changes (keep backward compatibility in mind)
3. Update the description in frontmatter if trigger conditions changed
4. Test and **create a pull request**
5. **Add the R&D team as reviewers** -- approval is required before merge

## Principles

1. **Universal compatibility** -- One skill works across all agents. Never duplicate for different platforms.
2. **Concise is key** -- Challenge each line: "Does this justify its token cost?"
3. **Progressive disclosure** -- Metadata for discovery, instructions on trigger, resources on demand.

## License

Internal use only. All rights reserved.
