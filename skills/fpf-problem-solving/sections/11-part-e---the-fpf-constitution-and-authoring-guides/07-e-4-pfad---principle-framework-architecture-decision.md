## E.4.PFAD - Principle-Framework Architecture Decision

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.PFAD:1 - Problem frame

Use this pattern when an author is choosing among a new or revised principle framework, a thinner publication or access route, and no new framework, and that choice will settle a boundary that later work must use. The boundary may concern the framework edition, dependencies, initial pattern placement or relations, or the publication or access consequence. Another author or reviewer must need the answer and its rationale for later action.

If a cheap search, curated reading route, or stop answers the immediate need without settling such a boundary, use that result and stop. Do not open a framework-architecture DRR merely because `E.4.PFAD` exists.

When the architecture question is live, use `E.4.PFAD` to state the framework-specific content of one ordinary `E.9` DRR. The pattern is a practitioner-facing profile and locator; its result is that DRR. No PFAD relation or second decision record is created, and acceptance remains separate.

### E.4.PFAD:2 - Problem

Framework authors repeatedly need to decide the intended edition boundary, FPF Core dependency, first patterns and their relations, and the publication or access consequence. Generic decision prose can hide those choices. A large framework-specific form creates the opposite problem: it makes proposal, acceptance, DRR, framework edition, authoring, quality review, and publication look like one extra decision object.

The useful result is one answer whose framework consequences are visible without adding a second decision stage or making cheap exploratory work produce decision paperwork.

### E.4.PFAD:3 - Forces

| Force | Tension |
| --- | --- |
| Discoverability | Authors need a recognizable framework question, but a locator must not become another decision object. |
| Decision memory | Later work needs rationale and consequences, but the DRR is not the accepted answer, performed authoring, or framework edition. |
| Framework detail | Edition, dependency, pattern placement, relations, and publication consequences matter, but unrelated quality, naming, and package apparatus must stay conditional. |
| Cheap exit | A small access result may solve the immediate problem without a framework decision. |
| Relation precision | Initial pattern relations may shape the architecture, but a row or schema does not make those relations obtain. |
| Evolution | The answer needs a reopen condition without turning every refresh concern into a mandatory field. |

### E.4.PFAD:4 - Solution

#### E.4.PFAD:4.1 - Decide whether the architecture question is open

Ask whether choosing a framework, a thinner route, or stop will settle at least one boundary used by later authoring or review:

- a governed or intended framework edition;
- an FPF Core or other current dependency;
- initial pattern placement or a relation among those patterns that changes the architecture; or
- a publication or access consequence.

If no such boundary and receiving use are present, close the exploratory use without `E.4.PFAD` or an `E.9` DRR. If they are present, record whichever answer is selected—including access-only or stop—in one `E.9` DRR. The cheap exit and the architecture decision are alternative entry outcomes, not serial stages.

#### E.4.PFAD:4.2 - State the compact framework answer

The framework-specific part of the DRR states:

1. the intended reader, recurring problem, and bounded architecture question;
2. the selected outcome: a new or revised framework edition, a thinner publication or access route, or no new framework now;
3. the governed edition, the intended-edition boundary before realization, or that no new edition is governed;
4. the selected FPF Core dependency and only the other edition dependencies current for this answer;
5. the first patterns, their placement, and only the relation choices among them that change the selected architecture;
6. the publication or access consequence; and
7. material alternatives, accepted costs or losses, practical consequences, the first authoring action or stop, and the reopen condition.

Keep the ordinary `E.9` grounds, sources, affected loci, rationale, and consequences in the same DRR. Add source-return, naming, quality, admission, currentness, or package details only when they change this answer or a named later use requires them. Use the pattern that defines, constrains, or tests each added claim; do not make it a standing PFAD field.

#### E.4.PFAD:4.3 - State initial pattern relations directly

When an initial pattern relation changes the selected architecture, state the relation and its participants as an ordinary assertion. For example: `Pattern A frames the recurring problem; Patterns B and C specialize its reusable move for two stated situations.` Use the pattern that defines or constrains each relation function.

An optional `E.4.PFR` row may later represent these assertions for maintenance. The row neither makes the relations obtain nor becomes mandatory for the architecture answer. A generic relation catalogue is not a prerequisite for the decision.

#### E.4.PFAD:4.4 - Keep the answer, DRR, authoring, and publication distinct

The `E.9` DRR records the selected answer and rationale. A separately governed decision accepts, redirects, rejects, or reopens that answer. Later authoring realizes an accepted answer. A framework edition is the resulting maintained pattern framework, not the DRR or the authoring work. An ADR-like document, site, PDF, or other carrier publishes or projects claims about these objects; its form does not create the answer, acceptance, authoring, edition, or pattern relations.

Use `C.32.PAD` only when the question is an exact project architecture decision about a named composite project Work, and use `C.32.ADR` only to project that project decision. For an ordinary framework answer, publish the selected decision episteme or a reader-specific projection through `E.17` and `E.24.PUB`. None of these is a mandatory stage of principle-framework authoring.

### E.4.PFAD:5 - Archetypal Grounding

#### Positive DPF

A systems-management group identifies a recurring coordination failure, a practitioner audience, a useful reusable move, current FPF provision, and three provisional patterns. A curated route does not cover the recurring problem. Because the choice will settle edition, dependency, pattern-placement, relation, and publication boundaries for later authors, the group opens one architecture question. Its `E.9` DRR records the intended edition, Core dependency, initial placement, the material relations among the three patterns stated directly, publication consequence, first authoring action, and reopen condition. No PFAD relation or mandatory PFR row is created.

#### Exploratory access result

Existing FPF and source material answer the immediate need through a curated route. No later author or reviewer needs a settled framework boundary. The inquiry closes with that route and no PFAD or DRR.

#### Decision-level access result

A team needs a maintained choice among a DPF, an access route, and stop because later work depends on the rationale. The architecture question is therefore open. One `E.9` DRR selects no new framework edition, states the maintained access consequence and stop, and records when to reconsider the answer.

#### Existing framework

A local practice framework already has an accepted architecture answer and a source record. Changing an example or publication carrier creates no new PFAD stage. Reopen only when its selected edition boundary, dependencies, initial pattern architecture, or publication or access consequence changes.

### E.4.PFAD:6 - Bias-Annotation

The first drift is form-first decision making: a team starts from a schema, row, ADR heading, or status field and assumes that filling it has settled the architecture. Start from the reader's problem, alternatives, downstream-used boundary, and practical consequence instead.

The second drift is machinery-first entry: proposal, dependency, quality, naming, and publication apparatus appears before the reader knows whether a framework decision is needed. Keep that apparatus conditional on its own receiving use.

The third drift is relation-by-representation: a table row or reference list is treated as the relation it records. State the relation directly; add a representation only when a named maintenance or checking use needs it.

### E.4.PFAD:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFAD.1 Opening discriminator | A later-use edition, dependency, pattern-placement or relation, or publication/access boundary makes the architecture question live. |
| CC-PFAD.2 Cheap exit | A route or stop that settles no such boundary closes without PFAD or a DRR. |
| CC-PFAD.3 One decision record | Every selected DPF, access-only, or stop answer after the question opens is recorded in one ordinary `E.9` DRR. |
| CC-PFAD.4 Compact payload | The DRR carries the seven framework-specific content groups in `E.4.PFAD:4.2` and ordinary E.9 rationale. |
| CC-PFAD.5 Direct relation assertions | Relations among initial patterns are stated directly under their actual relation functions; no PFR row is required. |
| CC-PFAD.6 Object boundaries | Answer, acceptance, DRR, authoring, edition, and publication remain distinct. |
| CC-PFAD.7 Conditional apparatus | Proposal, source-return, naming, quality, admission, currentness, and package details appear only when they change the answer or serve a named later use. |
| CC-PFAD.8 Reopen condition | The DRR states what change in framework boundary or receiving use requires reconsideration. |

### E.4.PFAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| PFAD as a second decision | Authors reconcile an E.9 answer with another PFAD result. | Keep one selected answer in one E.9 DRR; use PFAD only as the framework-specific profile. |
| Paperwork on the cheap exit | A curated route or stop triggers a DRR without settling a later-used boundary. | Close the exploratory use directly. |
| Mandatory relation row | A PFR row is required before relations among initial patterns can be understood. | State each relation directly and add a row only for a named maintenance use. |
| ADR as decision | A publication projection is treated as the answer or acceptance. | Name the answer and acceptance separately; use ADR only as a projection. |
| Conditional detail made universal | Every decision must supply proposal, naming, quality, admission, source-return, and package records. | Include only details that change this answer or serve a named use. |
| Hidden Core change | A domain or local framework decision silently changes FPF Core meaning. | State dependency direction and keep Core changes in their own accepted decision. |

### E.4.PFAD:9 - Consequences

Authors get a recognizable framework question, one cheap stop rule, one compact decision account, and one next action. Later authors can recover the edition boundary, dependencies, initial pattern architecture, publication or access consequence, rationale, and reopen condition without reconciling two decision objects.

The cost is one additional locator to maintain and a coordinated carry-through when several FPF passages still teach the old relation schema. An optional machine-readable representation remains future work until a named catalog or checker identifies the fields it consumes and the error it prevents.

### E.4.PFAD:10 - Rationale

Framework authors do need a recurring set of framework-specific questions, so removing every PFAD locator would make the entry harder to discover. They do not need a separate PFAD relation or record: `E.9` already carries one bounded answer, alternatives, rationale, consequences, action, and reopen condition. Direct assertions preserve the selected initial pattern relations without making their representation authoritative.

PFAD is therefore a profile by practical question and content, not a new ontological kind or a second stage.

### E.4.PFAD:11 - SoTA-Echoing

| Claim | Source and status | FPF use |
| --- | --- | --- |
| One bounded decision account carries alternatives, rationale, consequences, action, and reopen condition. | Current `E.9`; current FPF ground. | Use one ordinary E.9 DRR rather than a PFAD-specific result kind. |
| A relation needs actual participants, an obtaining condition, identity when later use needs the occurrence, and a receiving use. | Current `A.6.RCD`, `A.6.REL`, and `E.10:0.0a`; current FPF ground. | Refuse a PFAD relation; state material initial pattern relations directly. |
| Direct framework statements precede optional rows or manifests. | Accepted R3 decision and current `E.4.PFR`; current FPF ground. | Keep PFR representation optional under a named maintenance use. |
| Framework editions, publications, forms, and carriers remain distinct. | Current `E.24.PUB`; current FPF ground. | Treat ADR-like text, sites, and PDFs as projections or publications, not as the decision or framework. |
| Compact ADR sections help preserve decision memory but do not supply FPF ontology. | Nygard, `Documenting Architecture Decisions`, 2011; historical lineage source, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`; MADR, maintained template practice, `https://adr.github.io/madr/`. | Reuse concise question, alternatives, rationale, consequences, and supersession cues only when an ADR-like projection is useful. |

### E.4.PFAD:12 - Relations

- **Uses:** `E.9` for the one bounded selected answer and DRR.
- **Uses:** `A.6.RCD`, `A.6.REL`, and the exact relation patterns for material relation assertions among initial patterns.
- **Coordinates with:** `E.4` and `E.4.DPF` for framework family architecture and authoring.
- **Coordinates with:** `E.4.PFR` for optional relation and edition maintenance representations.
- **Coordinates with:** `C.32.PAD` for an exact project architecture decision, `C.32.ADR` for its ADR-like projection, and `E.17` with `E.24.PUB` for publication of an ordinary framework answer.
- **Coordinates with:** `E.24.PUB` for publication occurrences, forms, carriers, audiences, and uses.
- **Coordinates with:** `F.18`, `G.2`, `G.11`, `E.4.DPF.DA`, `E.21`, `E.23`, and `E.19` only when naming, source synthesis, refresh, quality, improvement, or admission is current for the selected answer.

### E.4.PFAD:End

