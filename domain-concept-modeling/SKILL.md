---
name: domain-concept-modeling
description: >
  Establish the controlled vocabulary, classification structure, and conceptual
  business model that every downstream artifact is built on. Phase 1: business
  glossary (terms + definitions) and taxonomy (classification). Phase 2: concept
  model (relationships, cardinality, structural rules). Use this whenever names are
  inconsistent, concepts need relating, or the domain needs pinning down before
  rules, data, or requirements are built. Trigger on: "what do we call this,"
  "these teams mean different things by the same word," "how do these relate,"
  "model the domain," "one-to-many or many-to-many," or "draw the business
  objects." It operationalizes ISO 704, W3C SKOS, SBVR 1.5, and UML 2.5.1 as
  original working rules; it does not reproduce them.
---

# Domain Concept Modeling

This skill produces the **names, the buckets, and the structure between them**:
a glossary that says what each business term means, a taxonomy that says where each
concept belongs, and a concept model that says how concepts relate. Every other
skill in the practice is *written in* these terms and built on these structures, so
getting them right once prevents drift everywhere downstream.

---

## Where this sits

- **Upstream:** business-architecture and stakeholder-experience surface raw domain
  terms.
- **Downstream:** decisions-business-rules and all requirements skills **must** write
  rules using these exact preferred terms. information-data-modeling maps each
  business term to a data element. KPI/reporting definitions reconcile on these
  categories.
- **Cross-cutting:** practice-governance owns term approval authority; this skill
  owns term content and structure.

---

## Phase 1: Terminology & Taxonomy

### Core working rules

#### 1. One concept, one preferred term
Cluster candidate words by the concept behind them, then pick **one preferred term**
per concept. Record the rest as synonyms (allowed alternates) or prohibited/deprecated
terms.

#### 2. Write definitions with discipline (ISO 704 style)
A sound definition:
- states the **broader category** then the **distinguishing characteristics**
  (genus + differentia),
- is **non-circular** and does not contain the term being defined,
- is **substitutable** — replacing the term with the definition keeps the sentence
  valid,
- uses only other defined terms.

#### 3. Taxonomy = one division principle per level, MECE children
- Each level splits its parent by **one** criterion. Never mix criteria at the same
  level.
- Children are **mutually exclusive and collectively exhaustive**, each with
  inclusion/exclusion criteria.
- The hierarchy carries only broader/narrower ("is a kind of") links.

#### 4. Make it machine-readable (SKOS style)
Each concept has a unique identifier, preferred label, alternate labels, hidden
labels, broader/narrower links, and a scope note.

#### 5. Every term and category is owned and has a status
Assign an owner and approval status (draft/approved/deprecated).

#### 6. Resolve collisions explicitly
- **Homonyms** — qualify or split into distinct preferred terms.
- **Synonyms** — merge to one preferred term.

---

## Phase 2: Concept Modeling

### Core working rules

#### 1. Concepts come from the glossary — never invent them here
Every concept is a preferred term from Phase 1. If you need a concept not in the
glossary, add it there first.

#### 2. State every relationship as a named fact type
Connect concepts with verb-phrase facts, read in both directions:
- "a *patient* **has** *appointments*"; "an *appointment* **belongs to** a *patient*."
Prefer binary facts. Ternary+ usually hides a missing concept.

#### 3. Every relationship carries cardinality and optionality — both directions
"Each *appointment* belongs to **exactly one** *patient*"; "a *patient* has **zero
or more** *appointments*." A relationship without stated cardinality is unfinished.

#### 4. Use generalization only when subtypes earn it
Subtypes must have distinct facts or behavior. If the only difference is a label,
that's a taxonomy attribute.

#### 5. Capture structural/definitional rules — route violable ones to decisions
- **Definitional rule** — necessarily true; breaking it produces nonsensical data.
  These live **here**.
- **Operative rule** — could be violated by a user action. These go to
  **decisions-business-rules**.
- **The test:** *could someone do the wrong thing and break this?* If yes →
  operative. If breaking it just produces gibberish → definitional.

#### 6. Stay conceptual, never physical
No primary/foreign keys, nullable columns, data types, surrogate identifiers. Those
are information-data-modeling.

---

## Mandatory outputs

### Phase 1
- Business glossary (term, definition, scope note)
- Taxonomy (parent/child hierarchy, one division principle per level)
- Preferred terms, synonyms, prohibited/deprecated terms
- Inclusion/exclusion criteria per category
- Unique identifiers and labels (SKOS-style)
- Term/category ownership and approval status
- Collision register

### Phase 2
- Concept definitions (traced to glossary terms)
- Conceptual business model (concepts + fact types)
- Cardinality and optionality on every relationship
- Structural/definitional business rules

---

## Standards anchor

- **ISO 704:2022** — terminology work: definition-writing discipline (genus +
  differentia, non-circular, substitutable).
- **W3C SKOS** — machine-readable taxonomy structure (identifiers, labels,
  broader/narrower/related).
- **SBVR 1.5** — fact-type modeling and the definitional vs. operative rule
  distinction.
- **UML 2.5.1 class modeling** — classes, associations, multiplicity,
  generalization at the conceptual level only.

Operationalize as the rules above; do not reproduce specification text.

---

## Quality bar — failure modes to catch

- Duplicate/overlapping categories or inconsistent naming.
- Mixed division criteria at one taxonomy level (not MECE).
- Circular definitions, or definitions that contain the term.
- Concepts invented here that bypass the glossary.
- Relationships with no cardinality.
- Definitional and operative rules mixed together.
- Physical modeling artifacts (keys, columns, types) at the conceptual level.
- Subtypes with no distinct facts.
- Downstream artifacts using terms not in the glossary.

---

## How to apply this skill

1. **Harvest** candidate terms from stakeholder, journey, and policy artifacts.
2. **Cluster** words into concepts; choose preferred terms; record synonyms.
3. **Define** each term (genus + differentia, non-circular, substitutable).
4. **Build the taxonomy** — one division principle per level, MECE children.
5. **Encode SKOS-style** — IDs, labels, broader/narrower, scope notes.
6. **Assign** owner and status to every term and category.
7. **State the facts** — named verb-phrase relationships between concepts.
8. **Add cardinality and optionality** on every relationship.
9. **Capture structural rules**; apply the "could someone break it?" test and route
  violable rules to decisions-business-rules.
10. **Self-check** against the quality bar.

---

## Composition

- **From** business-architecture and stakeholder-experience: raw domain vocabulary.
- **To** decisions-business-rules: the concept backbone and operative rules.
- **To** information-data-modeling: the conceptual model to realize as logical data.
- **To** system-requirements-modeling: the domain structure.
- **Governed by** practice-governance for approval authority.

**Traceability:** term → concept → fact/structural rule → operative rule → data
element → requirement → test case. The glossary is the first link in the chain.