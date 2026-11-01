---
name: dal-scaffold
description: >
  Scaffold DAL layer files from a natural language table design description
  for any system module. Dynamically detects architectural variations (EF Core vs EF6,
  DI frameworks, base repositories, and naming conventions) by analyzing existing module files.
  Use this whenever a user wants to add a new database table, entity, or repository.
---

# DAL Scaffolding Skill

This skill generates a structurally sound DAL layer for a new database table in any system module. Because our modules share a semi-unified architecture (~60% similarity), this skill relies on dynamic pattern detection of the target module rather than hardcoded assumptions.

## Step 0: Archetype Discovery

To prevent breaking module-specific architectures, do not guess conventions. If the workspace context is unavailable, explicitly prompt the user to provide:
1. A sample repository implementation file from the target module.
2. A sample entity model file from the target module.

Analyze the provided samples or codebase to map the following architectural vectors:

| Target Vector | Detection Strategy & Patterns to Look For |
|:---|:---|
| **EF Version** | Look for `Microsoft.EntityFrameworkCore` (EF Core) vs `System.Data.Entity` (EF6). |
| **DI Engine** | Look for `services.AddScoped` (Microsoft DI) vs `builder.RegisterType` (Autofac). |
| **Base Repository** | Identify the exact inheritance pattern: `: {BaseRepoClass}<T, TKey>`. |
| **Unit of Work** | Extract the constructor injection type: `(I{Prefix}UnitOfWork unitOfWork)`. |
| **Mapping Strategy** | Detect if the module uses separate mapping files (`IEntityTypeConfiguration`) or handles configuration inline within the `DbContext`. |

---

## Step 1: Schema & Design Interpretation

### 1.1 Schema Selection
Prompt the user for the target database schema (Default: `dbo`). 
* If schema is `dbo`: Use `[Table("TableName")]` (Omit explicit schema parameter).
* If schema is custom: Use `[Table("TableName", Schema = "SchemaName")]` or the module's exact Fluent API equivalent.

### 1.2 Table Type Classification
* **Lookup Tables (`SLKP_` prefix):** Key type is typically `short` or `int` with value generation disabled (`[DatabaseGenerated(DatabaseGeneratedOption.None)]` or `.ValueGeneratedNever()`). Name columns (`NameEn`/`NameAr`) are strictly required.
* **Regular Tables:** Key type is typically `long` with auto-increment. Includes audit trailing and soft-delete properties if established by the module's base patterns.

---

## Step 2: Code Generation Rules & Alignment

Generate files sequentially to maintain dependency integrity. Match the namespaces, casing rules, and formatting observed during Step 0.

### 2.1 Entity Model
* Match the module's nullability conventions (e.g., nullable reference types usage).
* Keep properties clean. If the module utilizes separate mapping configuration files, do not mix Data Annotations (like `[MaxLength]`) inside the POCO model unless existing entities do so.
* **Foreign Key Placement Rule:** Place the `[ForeignKey]` attribute strictly according to the module's pattern—never guess.

### 2.2 Repository Interface & Implementation
* Inherit cleanly from the discovered `{BaseRepoClass}` and `I{Prefix}UnitOfWork`.
* Bring in the exact namespaces discovered in Step 0.
* If the module requires explicit query expressions for non-deleted records (common in older EF6 setups), implement the filtering method matching the exact signature of the module.

### 2.3 Configuration & DI Registration
* **DbContext Update:** Append the new `DbSet<{EntityName}>` property. Register the entity mapping inline or via configuration class depending on the discovered mapping strategy.
* **DI Update:** Register the new interface and implementation using the exact syntax of the module's dependency container (Autofac or Microsoft DI).

---

## Step 3: Deployment & Validation Commands

Provide the exact Visual Studio Package Manager Console (PMC) commands for the target project:
```powershell
Add-Migration Add_Table_{EntityName} -Project {DiscoveredModelProject}
Update-Database -Project {DiscoveredModelProject}