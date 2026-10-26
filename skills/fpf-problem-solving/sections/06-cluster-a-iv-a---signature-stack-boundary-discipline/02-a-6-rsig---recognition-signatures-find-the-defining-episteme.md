## A.6.RSIG - Recognition Signatures: Find the Defining Episteme for a Description

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.6.RSIG:1 - Problem frame

**Use this when** an encountered description leaves it unclear which defining account to inspect. A boundary clause, method note, interface excerpt or pattern opening can identify a useful next reading if its purpose, applicability and defining source are recoverable.
**First useful move.** State what the encountered description is for and identify its defining `U.Episteme`, using `definitionEpistemeRef` when a reference is needed. Include an exclusion or rejected neighboring reading only when it changes recognition or use under §4.1.

This gives the reader a description to inspect before broader comparison or a decision to apply its contents. A summary or excerpt can guide that choice, while its source reference allows the reader to check the defining account.

Reuse an already adequate identification. If the question instead concerns full boundary-claim classification, publication/view conditions, the Method’s semantics, cross-pattern selection or durable naming, use the pattern for that question.

### A.6.RSIG:2 - Problem

A missing or ambiguous recognition cue can leave the following questions unresolved:

1. One reader finds a boundary, method, interface, or pattern-local opening but
   cannot tell whether it is the right description to inspect.
2. An encountered carrier or public projection is misread as the defining `U.Episteme`.
3. Recognition cues drift into description semantics, workflow hints, graph
   metaphors, or lexical aliases that belong elsewhere.
4. Pattern-entry navigation is asked to identify the encountered description
   before the reader can begin pattern-language comparison.

### A.6.RSIG:3 - Forces

| Force | Tension |
| --- | --- |
| First-contact precision vs reader economy | The cue needs enough discriminating detail without turning every opening into a mini essay. |
| Neutral substrate vs local specialization | This pattern governs description-recognition signatures in general without absorbing pattern-entry discoverability, publication-face law, or boundary-claim routing. |
| Recognition vs semantics | The cue helps the reader recover the right description and defining `U.Episteme`, not silently redefine the description's full semantics. |
| Carrier/projection vs authority | An encountered carrier can help recognition without becoming the defining episteme. |
| Local wording vs controlled lexemes | Real reader language remains usable without minting uncontrolled aliases or shadow names. |
| Readability vs auditability | The signature stays usable by readers while remaining crisp enough for later review and boundary checking. |

### A.6.RSIG:4 - Solution

#### A.6.RSIG:4.1 - Recognition-cue discipline

A recognition cue makes the description, its purpose and relevant applicability conditions recoverable, with a reference to its defining account. Identify the encountered carrier or projection when that distinction affects recognition.
Reject a nearby reading or wrong defining `U.Episteme` only when it passes F.19's
grounded-guard test: the rejected reading has an independent local ground, is
plausible for the intended reader, and changes truth, understanding, selection,
safety, stop, reliance, or action. Use the
smallest clear correction; do not invent an alternative to fill the cue shape.

Here "description-recognition signature" is a lower-case authoring and reading
discipline, not by itself a typed `U.Signature` or a new formal kind. A typed
declaration requires the applicable neighboring pattern's explicit conditions.

The encountered carrier or projection may help recognition; it does not become
authoritative merely by being encountered.

Point to the defining `U.Episteme` through the available publication. Identify the E.24.PUB publication occurrence separately when its identity changes which definition or use is available. The publication and its carrier keep their own identities.

`A.6.RSIG` does not govern:

- general information architecture or search UX;
- documentation layout or publication-face selection;
- pattern-entry discoverability across a pattern language;
- the full semantics of the description itself;
- lexical repair, alias acceptance, or naming governance as such;
- graph ontology, workflow sequencing, or runtime route semantics.

#### A.6.RSIG:4.2 - Two-level description-recognition shape

**Reader-visible minimum.** Ordinary prose is sufficient when it makes these values recoverable:

1. what this description is for;
2. when it applies;
3. any exclusion that changes recognition or use;
4. which definitionEpistemeRef applies;
5. what nearby false reading or wrong defining `U.Episteme` to reject, when
   the grounded-guard condition in §4.1 holds.

**Expanded questions when needed.** Use the following questions when the shorter cue leaves a consequential recognition ambiguity unresolved. Existing prose can carry the answers; a separate form is optional.

```text
description_seen
encountered_carrier_or_projection
reader_viewpoint
case_signal_or_access_condition
applies_to
excludes
expected_first_recognition_gain
first_admissible_entry_stop_or_reroute
definitionEpistemeRef
projection_role_if_any
nearby_false_description_or_wrong_definition_episteme
```

Use the exclusion and false-neighbor fields only when the grounded-guard condition in §4.1 holds. The viewpoint field names the reader’s perspective; identify a formal U.Viewpoint episteme only when that separate relation matters.

The questions help distinguish the encountered description and its defining account from their publication or carrier when those differences affect the choice.

##### A.6.RSIG:4.2.1 - Minimal local repair and review sequence

Use this sequence when authoring or reviewing one recognition-signature repair:

1. Name the encountered description and the reader’s question.
2. Name the encountered carrier or projection if confusing it with authority is
   a live risk.
3. State the applicability and any exclusion needed to choose the description.
4. Name the defining `U.Episteme` to inspect first.
5. When the grounded-guard condition in §4.1 holds, name the nearby false
   description or wrong defining `U.Episteme` to reject.
6. State the useful next inspection or the missing basis that prevents it.
7. If that stop cannot be stated without A.6.B claim routing, publication-face law,
   lexical repair, or cross-pattern comparison, apply the appropriate neighboring pattern instead of
   stretching `A.6.RSIG`.

The result is the recognition statement, its defining source reference and the useful next inspection or limitation. Include a false-neighbor correction only under §4.1.

#### A.6.RSIG:4.3 - Common uses

The same recognition question occurs in several settings:

- **boundary-description recognition**: can one reader recover what one
  boundary-presented description is for before the reader needs to classify its
  claims as L/A/D/E;
- **method-description applicability recognition**: can one reader recover
  whether one method description is the right description to inspect, reject, or
  compare for the reader's question;
- **interface/access-description recognition**: can one reader recover the
  right access or interface description without confusing it with promise,
  execution, or downstream effect semantics;
- **pattern-local recognition-signature case**: can one reader recover one
  pattern opening as the right first description to inspect before broader
  pattern-language comparison begins.

#### A.6.RSIG:4.4 - Neighbor boundaries

Neighbor boundaries remain explicit:

- use `A.6.B` when the reader needs to classify the boundary claims as `L/A/D/E`;
- `E.17.0` tests viewpoint/view membership; `E.17` publishes reader-facing forms of an already accepted engineering account;
  use `E.24.PUB` when publication occurrence, form, or carrier identity affects the recognition use;
- `E.10.D2` recovers description-episteme and specification-use distinctions;
  use `E.10` cues within `F.19` for wording, `A.6.P` for under-specified direct relations, and `F.18` for durable naming and its collision checks;
- `C.16.Q` repairs overloaded recognition or discoverability quality wording;
  `C.25` applies when the quality-family claim depends on several differently typed contributors; a single-Characteristic claim stays with its direct Characteristic pattern;
- the relevant authoritative pattern body governs pattern semantics when the
  encountered description is one pattern-local opening.

The four-part split for pattern-local recognition is:

| Recognition concern | Governing FPF pattern or source | What it governs |
| --- | --- | --- |
| Generic first-contact description recognition | `A.6.RSIG` | The neutral cue shape: description, carrier or projection, definitionEpistemeRef, exclusions, and a false neighbor when §4.1's grounded-guard condition holds. |
| Local placement and form | `E.8` | How the pattern's `Problem frame` carries the first-reading role. |
| Actual local semantics | The pattern itself | The pattern's governed object, solution, consequences, and conformance law. |
| Cross-pattern comparison | `E.11` | Candidate patterns, tempting wrong patterns, reclassification of the reader's question, and expanded entry-disambiguation cases. |

#### A.6.RSIG:4.5 - When a neighboring pattern is needed

If the task requires a quality claim, typed signature declaration, reusable
description, or publication-face rule, use the neighboring pattern that governs
that object or claim, including its evidence requirements. The recognition cue
alone does not establish that result.

### A.6.RSIG:5 - Archetypal grounding

#### A.6.RSIG:5.1 - System-side worked recognition repair: boundary-presented description

Draft cue:

> "The system shall reject invalid requests."

Why the cue is not enough yet:

- the reader cannot tell whether they are reading one
  law, admissibility gate, duty, work effect, or evidence statement;
- one summary page or local paraphrase can be mistaken for the governing
  boundary description;
- a reviewer can start arguing full semantics before identifying which
  description to inspect.

Recognition repair:

First recover the defining description; the cue alone leaves its boundary claim unresolved. For the worked branch below, suppose inspection of that defining episteme establishes a request-admissibility condition. If the source instead prescribes a duty or states another boundary claim, recognize that content and apply its corresponding entry.

1. `description_seen` = one boundary-presented admissibility description.
2. `encountered_carrier_or_projection` = one clause or excerpt where the
   description is seen.
3. `reader_viewpoint` = the perspective of a practitioner or reviewer deciding whether this is
   the right boundary description to inspect first.
4. `applies_to` = requests presented at the boundary under the declared
   admissibility conditions.
5. `excludes` = downstream effect claims, duty allocation, or evidence claims
   not actually stated by this description.
6. `definitionEpistemeRef` = the governing boundary description, not one local
   paraphrase or summary note.
7. `nearby_false_description_or_wrong_definition_episteme` = an evidence/work claim or
   a different routed-quadrant statement mistaken for the governing admissibility
   description.
8. `first_admissible_entry_stop_or_reroute` = the reader can now say "this is the
   admissibility description to inspect first"; if the reader needs to classify
   the boundary claims, inspect `A.6.B`.

#### A.6.RSIG:5.2 - System-side anti-case: interface/access description over-read as promise

Draft cue:

> "`POST /deploy` triggers deployment."

Plausible but wrong first reading:

- the reader treats deployment initiation as a guarantee of successful
  completion or of the whole deployment result.

Recognition repair:

1. `description_seen` = one interface/access description.
2. `encountered_carrier_or_projection` = one API excerpt or endpoint note.
3. `applies_to` = request accessibility, invocation form, and the stated
   deployment initiation under the conditions in the defining description.
4. `excludes` = success, completion, rollout, or downstream effect guarantees
   not present in the access description itself.
5. `definitionEpistemeRef` = the defining episteme for the access description;
   inspect the specification or pattern governing downstream effect separately if that question is current.
6. `first_admissible_entry_stop_or_reroute` = "this is the access description to
   inspect first: it describes invocation of `POST /deploy` and deployment
   initiation, not guaranteed successful completion."

#### A.6.RSIG:5.3 - Episteme-side worked recognition repair: method-description applicability

Draft cue:

> "Use pairwise comparison."

Why the cue is not enough yet:

- the reader cannot tell whether the note applies to ranking alternatives,
  selecting one option, shaping a shortlist, or comparing method families;
- the method note can be mistaken for the defining `U.Episteme` of selection
  semantics;
- a team can prematurely choose `C.11` or `G.5` before identifying what the
  pairwise comparison is to determine.

Recognition repair:

With only the cue, first ask what the pairwise comparison is intended to determine. For the worked branch below, suppose the defining episteme supplies comparison under a declared comparator but no selection or publication rule. If the source also defines selection, recover and use that contribution.

1. `description_seen` = one method-description applicability note.
2. `encountered_carrier_or_projection` = one method-description note, pattern excerpt,
   or review comment that mentions pairwise comparison.
3. `applies_to` = comparison under a declared comparator set or characteristic
   family.
4. `excludes` = selection or publication rules absent from this defining description. Apply the governing pattern if either result is needed.
5. `definitionEpistemeRef` = the defining comparison or Method-description episteme identified from the source, which this short cue does not supply.
6. `nearby_false_description_or_wrong_definition_episteme` = selection/publication doctrine
   treated as if the method note had already settled it.
7. `first_admissible_entry_stop_or_reroute` = inspect the identified comparison description. Its actual applicability and any subsequent selection still need their own conditions established.

### A.6.RSIG:6 - Bias-Annotation

A familiar label can attract the reader to the wrong account. The boundary, access and pairwise-comparison cases show why recognizing the subject and recovering the defining source must work together. A cue that already does this needs no additional form, alias or classification.

### A.6.RSIG:7 - Conformance checklist

- **CC-RSIG-1 First-contact only.** The pattern governs recognition of the
  right description, not the full semantics of that description.
- **CC-RSIG-2 Carrier/definition-episteme split.** A conforming description-recognition signature
  distinguishes `description_seen`, encountered carrier or projection,
  defining `U.Episteme`, and projection role when those distinctions are
  load-bearing. The encountered carrier or projection may help recognition,
  but it does not become authoritative merely by being encountered.
- **CC-RSIG-3 Neighbor boundaries explicit.** The text states the conditions
  under which the recognition question calls for each relevant neighboring
  pattern in §4.4; use only the patterns that govern the current questions.
- **CC-RSIG-4 No kind inflation.** An ordinary recognition cue is not by itself a
  typed `U.Signature`; a task requiring a typed declaration uses the applicable
  neighboring pattern under §4.5.
- **CC-RSIG-5 Recoverable cue.** For a consequential recognition use, keep the description’s purpose, applicability, defining source and next inspection recoverable. Include viewpoint, carrier/projection distinctions, exclusions or a false-neighbor correction when they change the reading under §4.1.
- **CC-RSIG-6 No alias minting.** Query cues and ordinary phrasing do not by
  themselves establish a naming settlement or Bridge. Use `F.18` for naming
  settlement and `F.9` for a Bridge, each under its own conditions.

### A.6.RSIG:8 - Common Anti-Patterns and How to Avoid Them

- **Recognition-as-semantics.** The opening tries to define the whole
  description instead of making the right description recoverable. Repair by
  shrinking back to first-contact discrimination.
- **Carrier-as-authority.** A local excerpt, public projection, or retrieved
  fragment is treated as the defining `U.Episteme`. Repair by naming the
  encountered carrier or projection and the defining `U.Episteme` separately.
- **Boundary-routing collapse.** A boundary-description cue tries to absorb
  L/A/D/E-classified claim structure. Repair by classifying the boundary claims under `A.6.B`.
- **Pattern-language collapse.** Pattern-entry comparison is written as if it
  were just another description cue. Repair by routing cross-pattern selection
  to `E.11`.
- **Signature inflation.** Any recurring cue is treated as one typed signature
  object. Repair by keeping `description-recognition signature` lower-case
  unless one explicit promotion is justified.

### A.6.RSIG:9 - Consequences

A reader can identify the relevant defining account while leaving its full semantics, applicability judgment and any subsequent selection to the work that needs them.

The cost is recovering enough purpose, conditions and source identity to make that choice. Use the expanded questions only when the ordinary cue leaves a consequential ambiguity.

### A.6.RSIG:10 - Rationale

A recognition cue lets a reader choose what to inspect from the description’s stated purpose and conditions. The source reference then makes that first estimate checkable against the defining account. If the account does not support the cue, revise the cue or keep the choice unresolved; a recognizable label alone cannot settle the discrepancy. An adequate cue can finish this first-reading task without deciding whether the full Method is applicable or effective.

The same construction works for a boundary clause, an interface description or a Method note because each connects an encountered expression to a defining account and a bounded reading decision. Their domain meanings remain different. This shared relation explains the common questions without turning recognition into one universal entry or semantics pattern.

### A.6.RSIG:11 - SoTA-Echoing

The following sources contribute to cue economy, recoverable definition and bounded expectations. Their contributions apply to the recognition question; the defining subject account still supplies its substantive semantics.

| Recognition question | Source contribution | Connection to this pattern | Use and limits |
| --- | --- | --- | --- |
| First-contact recognition is narrower than general information architecture or documentation UX. | Jorge Arango (2018), *Living in Information: Responsible Design for Digital Places*; ISO/IEC/IEEE 26514:2022, *Systems and software engineering - Design and development of information for users*. | These sources support purposeful information places and user information shaped around what the user needs. `A.6.RSIG` narrows that to one encountered description: what it is for, what applies, what excludes, what carrier exposed it, and which `definitionEpistemeRef` identifies the defining episteme. | Use the recognition and information-need contribution for one encountered description; broader UX and layout remain outside this task. In the boundary sentence slice, the first repair is not "what does the complete Contract Bundle mean?" but "what description is this, what does it apply to, and which definitionEpistemeRef applies?" |
| Information scent helps first-contact cue economy but is not the defining episteme. | Raluca Budiu (2020), "Information Scent: How Users Decide Where to Go Next", Nielsen Norman Group. | Information scent treats visible labels, context, and prior knowledge as imperfect estimates of source value. `A.6.RSIG` uses the cue-economy insight and adds definition-episteme and exclusion discipline, with false-neighbor rejection under §4.1's grounded-guard condition. | Visible cues guide inspection; the defining episteme remains the source to inspect. In the API slice, an endpoint label can attract attention and state deployment initiation without promising successful completion. |
| Description-recognition signatures help human and AI-assisted readers manage applicability and limitation expectations. | Amershi et al. (2019), "Guidelines for Human-AI Interaction", CHI 2019. | Human-AI guidance emphasizes making capabilities and limits clear enough for users to calibrate trust. `A.6.RSIG` adapts that pressure into `applies_to`, `excludes`, `definitionEpistemeRef`, and admissible entry stop for human and AI-assisted readers. | Clarify expectations for the encountered description. In the method-note slice, the reader learns what the note can and cannot settle before using it for a decision. |
| Description-recognition cues need controlled wording without becoming synonym or alias governance. | Helen Lippell, ed. (2022), *Taxonomies: Practical Approaches to Developing and Managing Vocabularies for Digital Information*. | Taxonomy practice supports governed terms, validation, and maintenance for search and browse. `A.6.RSIG` uses stable cue language while leaving wording repair to `E.10` cues within `F.19`, durable naming, aliases, and collision checks to `F.18`, actual Bridge claims to `F.9`, and under-specified relation claims to `A.6.P`. | Use stable terms that discriminate the intended description. The worked slices state definitionEpistemeRef, exclusions, and a false neighbor when §4.1's grounded-guard condition holds, instead of adding more query phrases. |
| Thin echoes and projection snippets need definition-episteme anchors before a reader or retrieval system treats them as the defining episteme. | Lewis et al. (2020), "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"; Liu, Zhang, and Liang (2023), "Evaluating Verifiability in Generative Search Engines"; Gao et al. (2023), "Enabling Large Language Models to Generate Text with Citations". | Retrieval and citation work makes source context, support, and verifiability load-bearing. Before relying on a retrieved fragment, public projection, or local example to identify a particular defining description, recover the defining `U.Episteme` and the projection relation when relevant. An unresolved fragment may still guide further inspection. | Recover the defining source and support for the cue. A retrieved applicability cue does not by itself settle selection semantics. |
| Description-recognition-signature adequacy is reviewable through small, case-linked checks. | Riehle, Harutyunyan, and Barcomb (2020), *Pattern Discovery and Validation Using Scientific Research Methods*, Technical Report CS-2020-01. | Pattern-validation practice supports explicit evidence and case adequacy. `A.6.RSIG` keeps that pressure lightweight: use the first-contact shape, false-neighbor rejection when §4.1's grounded-guard condition holds, and worked slices first; add `C.25` only for a composite quality-family claim, `C.16.Q` only for overloaded evaluative wording, and empirical evidence when the recognition claim requires it. | Choose evidence for the recognition conclusion being made; an ordinary wording repair need not establish measured reader performance. |

### A.6.RSIG:12 - Relations

- **Builds on:** `A.6`, `A.6.P`, `F.18`, `E.10`
- **Does not specialise:** `A.6.0` / `U.Signature`; it uses "signature" only in the lower-case cue-pattern sense unless an explicit neighbouring pattern promotes the structure into a typed declaration.
- **Neighbors:** `A.6.B`, `A.6.C`, `E.17.0`, `E.17`, `E.10.D2`, `C.25`, `C.16.Q`
- **Supports:** `E.11` as the pattern-language application above this neutral substrate

### A.6.RSIG:End
