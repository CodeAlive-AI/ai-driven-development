## E.4.PFR - Pattern-Framework Relation and Edition Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

**Use this when.** Use E.4.PFR when a named framework-maintenance, edition-impact, comparison, publication/dependency-repair, or refresh task needs a stable relation-specific row across patterns, framework editions, publication or access carriers, source packs, decisions, generated carriers, or quality results.

**First useful move.** State the exact subject assertion in ordinary C.2.1 form: name the subject or claim, exact relation function, exact defining or constraining ClaimGraph, polarity, and the current fact or condition. Stop there unless an identified maintainer or tool consumes standardized relation form.

**Primary working object.** One already identified subject assertion, optionally represented by one `PatternFrameworkRelationRecord@Context` for a named framework-maintenance use. The assertion, relation row, pattern description, relation kind or occurrence, framework edition, publication occurrence, form, carrier, access route, source use, Work, evidence, assurance, and currentness result remain distinct.

**Primary working reader.** A framework author or maintainer who must state one relation or edition claim now and decide whether a named maintenance use justifies a reusable row. A tool may consume that row; it is neither the reader nor an actor in the claim.

**What this buys.** Ordinary authoring stays light, while real edition and framework-maintenance consumers can still compare relation functions, inspect compatibility and dependency effects, preserve blocked stronger readings, and reopen only affected uses.

**Not this pattern when.** If a readable subject assertion closes the task, use C.2.1 and stop. Use E.11.PUR for pattern-use recommendations, E.17 and E.24.PUB for publication, G.2 for source selection and use, C.33-C.35 for carrier capture/preservation/admission, and the exact subject pattern for the direct relation. E.4.PFR does not define a generic governance relation, pattern owner, mandatory relation-record layer, workflow, runtime route, API call, build dependency, or performed Work.

### E.4.PFR:1 - Problem frame

Pattern frameworks need several relation functions. One pattern may specialize another. A local framework edition may depend on a domain framework or FPF Core edition. A publication occurrence may expose a selected set through a carrier. A skill pack or MCP-backed service may provide access to that set. A generated graph may suggest candidates. A quality result may evaluate a pattern version. Those claims differ in subject, predicate, identity, use, evidence, and change behavior.

### E.4.PFR:1.1 - Problem

Two opposite failures are common. Flattening everything into "related patterns" or "dependency" hides relation function and change effect. Requiring a PFR row for every load-bearing relation turns a readable assertion into a record-first ontology and encourages a fictitious fact that one pattern contains the defining content for or governs the other content.

### E.4.PFR:2 - Forces

| Force | Tension |
| --- | --- |
| Ordinary affordability | A direct assertion should remain one sentence when no maintenance receiver needs a row. |
| Stable maintenance form | Edition-impact, comparison, publication/dependency repair, and refresh may need consistent fields across many assertions. |
| Relation economy | Compact rows help inspection but can hide the exact defining or constraining ClaimGraph. |
| Dependency pressure | Edition dependency is useful but is not compatibility, specialization, recommendation order, publication grouping, derivation, or evaluation. |
| Compatibility pressure | Framework editions need compatibility, deprecation, supersession, and refresh boundaries without becoming software packages. |
| Actual-use truth | Definition, citation, or adjacency must not be mistaken for formal-premise use or criterion selection. |
| Conflict and replay | A high-cost receiver may need a closed candidate family and pairwise result, while ordinary use should not pay that cost. |
| Generated structure pressure | Search and graph outputs can suggest relations but cannot decide their meaning or admission. |
| Preservation | Source, carrier, publication, access, Work, evidence, assurance, authority, and currentness meanings must survive relation cleanup. |

### E.4.PFR:3 - Solution

Select the lightest lane that changes the named receiver's next action. A more elaborate representation is not intrinsically better.

#### E.4.PFR:3.1 - Lane 1: ordinary subject assertion

Name the exact subject or claim, exact relation function, exact defining or constraining ClaimGraph, assertion polarity, and current facts or constituting history. A pattern id, heading, field, file, or carrier may locate that ClaimGraph but does not own the subject and creates no governance relation.

If no actual formal-premise use or criterion selection is claimed, stop. Create no PFR row, actual-use predicate assertion, candidate universe, basis analysis, scope/time placeholder, edition pin, witness wrapper, evidence or assurance result, accepted-use record, or relation occurrence merely to make the sentence look complete.

#### E.4.PFR:3.2 - Lane 2: optional relation-specific maintenance row

Choose the smallest stable form the named receiver consumes. Use `PatternFrameworkRelationRecord` when a cross-relation comparison or maintenance index needs common endpoint, relation-function, use, and blocked-reading fields. Use `FrameworkEditionDependencyRecord` when an edition-impact or refresh receiver needs the relied-on content, dependency reason, direction, and refresh fields. Choose one by default; either form faithfully represents an already identified assertion and creates no relation.

If one named receiver genuinely needs both views, both cite the same `subjectAssertionRef`, the dependency record cites the generic row through `genericRelationRecordRef`, and every overlapping value is derived from that assertion. Rebuild both views when the assertion changes; never maintain duplicate facts independently.

```text
PatternFrameworkRelationRecord@Context:
  relationId
  sourceRef
  targetRef
  relationFunction
  governedUse
  subjectAssertionRef?
  relationFunctionClaimRef?
  dependencyOrEditionEffect?
  preservationOrAdmissionRef?
  blockedStrongerReading
  sourceReturnCondition?
  refreshOrSupersessionCondition?
```

`relationFunctionClaimRef`, when present, resolves the exact defining or constraining ClaimGraph used by the subject assertion. It is not an owner field, pattern-authority assertion, provenance claim, or actual-use predicate. `subjectAssertionRef` is present only when the receiver needs stable reference to the exact C.2.1 assertion. Source and target remain the exact endpoints for this relation function; row order creates no direction.

Dependency, specialization, publication, source reuse, quality, access, preservation, admission, and refresh retain their existing semantics. A PFR row translates none into derivation, evaluation, evidence, assurance, permission, authority, Work, or relation occurrence.

Use these companion forms only for their named maintenance receivers:

```text
FrameworkEditionDependencyRecord@Context:
  subjectAssertionRef
  dependencyPredicateClaimRef
  directionConstraintClaimRef
  genericRelationRecordRef?
  dependentEditionRef
  reliedOnEditionRef
  reliedOnContentRefs
  namedUse
  dependencyDirection
  dependencyReason
  refreshConditionRefs
  compatibilityClaimRefs?

FrameworkPackageManifest@Context:
  frameworkEditionRef
  selectedPatternSetResultRef
  relationRecordRefs
  dependencyAndEditionRecordRefs
  editionStatus
  deprecationOrSupersessionRefs?
  sourcePackRefs
  qualityEvidenceRefs
  refreshPlanOrCurrentnessRefs
  firstEntryCarrierRefs
  blockedRuntimeOrBuildReading
```

The dependency record mirrors exactly one already stated direct dependency and cites that assertion through `subjectAssertionRef`. It names one dependent edition, one relied-on edition, the exact content from that relied-on edition, the named use, direction, reason, and refresh conditions as one unit. If one edition has several direct dependencies, write one record per relied-on edition or use a keyed collection of those records; never pair parallel edition and content lists or read them as a cross-product. A useful aggregate is only a projection over those direct records, not a second maintained truth. The record contains no compatibility boundary. `compatibilityClaimRefs`, when present, points only to a separately stated pairwise compatibility claim because a named maintenance receiver needs that connection. The reference does not create or complete the compatibility claim. `genericRelationRecordRef` is present only when the same receiver also consumes the generic row; both views derive overlapping values from `subjectAssertionRef` and refresh together. Deprecation and supersession likewise remain separate assertions; a package manifest may index them when its named maintenance use needs those refs.

The manifest is a package-like index for a domain principle framework or local practice framework when authors actually need one. It indexes whichever generic relation rows or dependency-specific records its named operation consumes; either list may be empty, and one indexed form never requires its duplicate. When the operation genuinely needs both linked views, the manifest may index both without making either a second semantic source. The form of FPF itself uses E.4.FPF and its `FPFEditionRebuildabilityRecord`. A manifest entry, relation row, identifier, citation, or file path creates neither the referenced object nor any relation.

#### E.4.PFR:3.3 - Relation functions keep their own semantics

| Relation function | Admissible use | Exact defining or constraining locus |
| --- | --- | --- |
| Pattern-use recommendation | Recommends or sequences a candidate pattern use for a concern; actual application remains separate. | `E.11.PUR` |
| Specialization | Narrows parent content through exact inherited content plus child delta and stated use boundary. | parent content and `E.8` |
| Framework-architecture answer: initial pattern-relation choices | Asserts each direct relation among selected initial patterns whose truth changes the selected architecture answer or its stated consequences, using the predicate that defines that relation; the one `E.9` answer records which choices were selected and why. Add a PFR row only when a named maintenance use needs a stable representation. | the pattern that defines or constrains each asserted relation; `E.9` for the selected answer; `E.4.PFAD` for its framework-specific profile |
| Publication relation | Makes selected content available through a publication occurrence, form, unit, view, carrier, readme, preface, card, or table of contents. | `E.11`, `E.17`, `E.24.PUB` |
| Access relation | Describes bounded access to selected framework content or guidance through a skill pack, MCP-backed service, retrieval route, or assistant integration. | exact access claim plus `E.11`/`E.17`; `C.35`, `A.15`, `A.10`, `B.3`, `E.9`, or `G.11` only when their distinct output is current |
| Framework edition dependency | States that one dependent edition's content or result for a named use requires exact content from one relied-on edition: removing that content or changing it in a way relevant to the use would invalidate the dependent content/result or require that use to be reopened. It makes no compatibility claim. | E.4.PFR:3.4 for the defining predicate; `E.5.3` only for allowed direction and Core acyclicity; `G.11` only for currentness and refresh |
| Framework edition compatibility | States whether one exact pair supports a named overlapping use across a stated difference or interface, with its impact and reopen condition. If the basis is insufficient, make no positive compatibility claim. | C.2.1 assertion identity and E.4.PFR:3.4 |
| Preservation relation | States that one carrier, edition, profile, or projection preserves selected structure for a licensed use. | `C.34`, with `C.33` for local carrier loss |
| Produced-carrier admission | Admits generated, searched, mined, or transformed carrier content as input under declared conditions. | `C.35` |
| Quality framing, evaluation, or improvement | Frames a question, evaluates FPF/DPF/pattern adequacy, or records repeated improvement. | `E.22`, `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23` as selected by the exact object |
| Selected-set result declaration | States the selector-facing result kind, exact scope, selection or inclusion conditions, members, ordering, named use when required, and basis pins. It establishes no availability occurrence. | Use `G.5` for this declaration. If publication is separately current, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the publication occurrence and audience availability. |
| Source or decision reuse | Uses an exact source line, SoTA pack, DRR, selected answer, accepted decision, or evidence/source claim by value for a bounded use. | `G.2` for source/SoTA; `E.9` for the DRR and selected answer; the exact separate acceptance decision plus its authority relation or local rule for accepted-decision reuse; `A.10` only for an evidence-use claim |
| Direct subject relation | States one exact relation or classification under its defining predicate and current case facts. | the exact subject pattern and C.2.1 assertion identity |

The direct assertions, not a PFAD or PFR row, state the architecture-bearing relation facts. The `E.9` DRR records their selection and rationale; `E.4.PFAD` adds no relation or second decision result. An optional PFR row may point to an exact assertion for maintenance, but it neither creates that relation nor becomes a condition for accepting the answer.

There is no `Subject-pattern relation`. When earlier prose says that one pattern contains the defining content for or governs a value, claim, boundary, relation, record form, or use, recover the subject assertion and exact relation function. Preserve genuine non-pattern ownership, legal or institutional authority, source attribution, evidence, and other direct relations.

#### E.4.PFR:3.4 - Edition and package discipline

Domain and local frameworks depend toward more stable editions. A local practice framework may depend on a domain principle framework and FPF Core. A domain principle framework may depend on FPF Core. FPF as a First Principles Framework edition is handled through E.4.FPF; Core does not depend on domain or local frameworks except through a deliberate Core amendment.

Framework-edition dependency obtains for one dependent edition, one relied-on edition, exact content in the relied-on edition, and one named use only when the dependent edition's current content or result for that use requires the relied-on content: removing it or changing it in a way relevant to the use would invalidate the dependent content/result or require that use to be reopened. State that case fact and why the content is required. Edition labels, joint publication, joint-use membership, and an allowed direction do not establish dependency.

> `Domain@D` uses `Core@C` relation semantics as required constraints on framework review. Without those semantics, or after a relevant change to them, the affected review guidance cannot remain current without recheck. `Domain@D` therefore depends on that exact `Core@C` content for framework review.

E.5.3 constrains the allowed dependency direction and Core acyclicity after the relation has been identified. G.11 governs the edition pin, currentness, and refresh condition. Neither supplies the dependency predicate or makes the case fact obtain.

Compatibility answers whether one exact pair can support an overlapping use despite a stated difference or interface. State it separately and only when current:

> `Domain@D` and `Core@C` are compatible for framework review across relation-semantics interface I. Difference X changes no admitted review operation within boundary B; reopen when I, X, B, or either edition changes.

If that basis is insufficient, state the unresolved pair, overlap, or impact and make no positive compatibility claim. A dependency record may cite the independently stated compatibility claim only when a named maintenance consumer needs the link. Both claims may obtain for the same pair; neither is shorthand for the other. Deprecation and supersession are also separate claims and are indexed only when current.

Do not import binary compatibility, runtime import, build, module-call, API permission, or performed-work semantics. An edition label alone establishes no dependency, compatibility, deprecation, supersession, or refresh result.

These are heterogeneous neighboring objects, not members of one type: a selected pattern-set result; its stable public identity when one is needed; a publication occurrence; an access carrier; a relation row; a dependency pin; an edition status; a source-pack pin; a quality result; a refresh plan; and a first-entry carrier. Listing an access means—for example, a skill package, MCP endpoint, API route, or assistant integration—records only the exact access claim that obtains; it creates no framework dependency, method order, tool permission, or authority. Use G.5 for selector-facing set-result declaration, E.17 for a source-backed publication face and return to source, E.24.PUB for the publication occurrence and audience availability, G.11 for currentness, and C.33 or C.34 when a carrier is used as architecture or preservation evidence.

#### E.4.PFR:3.5 - Lane 3: exact actual rule-content use

Use `derivedUsingRuleContent(dependentContent, baseContent)` only when one identified derivation claim used the exact nonempty base subgraph as a formal premise under a declared inference rule or application to produce the exact dependent ClaimGraph. Use `evaluatedAgainstRuleContent(dependentContent, baseContent)` only when one identified criterion-selection claim selected the exact base for one bounded evaluation claim concerning that dependent ClaimGraph. These predicates are declared by `RuleContentBasisFindingDefinition@R7`; definition, constraint, applicability, consultation, influence, source use, evidence, evaluation Work, result, sufficiency, assurance, reliance, permission, and publication are independent.

Each positive or negative actual-use assertion is an ordinary C.2.1 episteme. It names exact subject `S`, dependent graph `U`, base subgraph `B`, mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, effective scheme, and only independently current scope, time, interpretation, source, or witness qualifications. A same-scheme use invents no Bridge. The serialized form is a representation, not a relation occurrence or new kind.

#### E.4.PFR:3.6 - Optional high-cost basis analysis

Open a basis analysis only for a named automated candidate comparison, reproducible cross-edition replay, same-subject conflict whose resolution can change the exact cell disposition or named receiver action, or bounded reliance/assurance receiver. One analysis is one C.2.1 episteme identified by `<AnalysisClaimGraph, BasisAnalysisQuestion@QGroup, effective ReferenceScheme>`. The question includes every independently current discriminator: `S`, `U`, derive/evaluate mode, bounded receiving use, exact actual-use claim identities, the receiving edition whenever changing it can change candidate applicability, the exact cell disposition, or the named receiver action, effective scheme, optional exact ClaimScope, and exact temporal-policy branch.

The analysis ClaimGraph carries a finite candidate universe containing only bases whose inclusion or exclusion can change the exact cell disposition or named receiver action. It carries a closure claim only when the enumeration rule, source boundary, completeness evidence, qualification window, and exclusion argument are exact. Each candidate is a finite nonempty set of semantic-base subgraphs used conjunctively. Each `CandidateEvaluation` keeps exactness, applicability, acceptance, witness, sufficiency, and minimality independent, with supporting claim refs and a reconsideration condition for every unresolved or negative axis. Duplicate graphs under one scheme collapse to one semantic atom while retaining source qualifications. Independently sufficient bases remain separate alternatives; jointly necessary bases remain one conjunctive alternative.

Compatibility is pairwise, not a candidate property. Every overlapping established pair whose resolution can change the exact cell disposition or named receiver action receives an exact result naming both alternatives, overlap, supporting claims, and, when conflicting, incompatible consequences plus a bounded E.9 decision. Candidate axes, pairs, conflicts, and receiving-edition distinctions enter the analysis only under that same effect test. The temporal partition is maximal and non-overlapping under the selected policy and this candidate set. A no-time-dependence policy yields one atemporal cell. Changes to scope, temporal policy, candidate inclusion, or applicability reopen only the assertions and cells whose disposition or named receiver action can change.

Exactly one disposition follows in each cell:

| Disposition | Truth condition |
| --- | --- |
| `established-conflict` | The established family is nonempty and at least one required overlapping pair conflicts. |
| `established-with-open-candidates` | The family is nonempty and has no established conflict, but the universe is open or an in-scope axis or required pair remains unresolved. |
| `established-compatible` | The family is nonempty, the universe is closed, all in-scope axes and required pairs are resolved, and all required pairs are compatible. |
| `open-no-established` | The family is empty and the universe is open or an in-scope required axis remains unresolved. |
| `closed-insufficient` | The universe is closed and nonempty, all required axes are resolved, and no candidate passes the conjunction. |
| `missing-candidates` | No candidate meeting the stated subject/use and source-boundary selection rule exists, and an exact absent-need claim states the needed content, subject/use, search boundary, and reconsideration condition. |

The basis answer is non-permissive. A downstream A.10 bounded-reliance claim or B.3 assurance result cites the exact analysis edition or cell-answer subgraph and supplies its own evidence, freshness, rival explanation, attempted use, and disposition. Neither grants permission, gate passage, decision, Work, actual use, publication, or authority. A reverse consumer lookup is derived rather than inserted into the upstream ClaimGraph.

#### E.4.PFR:3.7 - Bootstrap and stopping rule

A direct C.2.1 assertion always precedes optional PFR representation. The selected generic row or dependency-specific record cites the assertion and its exact defining or constraining ClaimGraph only when the named maintenance receiver needs that form. Neither representation can provide circular evidence for its own semantics.

After each assertion, ask: what named next action consumes more structure? If none, stop. A true stop has no pattern for the next question. When reconsideration is needed, state the condition or question and name a candidate pattern whose entry accepts it; do not model the pattern as receiver or destination.

### E.4.PFR:4 - Archetypal Grounding

#### E.4.PFR:4.1 - Ordinary subject assertion without PFR

In one CGUS position, `selectedConstituentRef` designates `result-42`. The exact C.11 `ChoiceResult` definition classifies that record from its stated disposition, selected option, comparison basis, rule, and stop-probing reason; A.22.CGUS constrains the position locator and selected-constituent reference. That sentence is the first useful output. It adds no owner field, PFR row, actual-use predicate, or basis analysis.

If a later Core relation-function maintenance replay must enumerate every CGUS position whose constituent-kind assertion cites a defining ClaimGraph, add one compact row for this position with the governed use, subject assertion ref, and exact C.11 definition ClaimGraph ref. That named receiver—not the importance of the relation—opens PFR.

#### E.4.PFR:4.2 - Framework edition dependency

Start with the readable dependency assertion:

> `CodexProcessFramework@current` uses the selected `FPFCorePatternSet@current` authoring and quality rules as required constraints on local process authoring. Without those rules, or after a relevant change to them, the affected local guidance cannot remain current without recheck. `CodexProcessFramework@current` therefore depends on that exact Core content for local process authoring.

Choose the representation from the receiver's job. A cross-relation comparison may use one generic PFR row. An edition-impact or refresh receiver may use one dependency-specific record. This receiver needs the relied-on content and refresh fields, so it uses only the dependency record:

```text
FrameworkEditionDependencyRecord@CodexProcessFramework:
  subjectAssertionRef: CodexProcessFramework-CoreDependencyAssertion
  dependencyPredicateClaimRef: E.4.PFR:3.4-framework-edition-dependency-predicate
  directionConstraintClaimRef: E.5.3-local-to-Core-direction-and-Core-acyclicity
  dependentEditionRef: CodexProcessFramework@current
  reliedOnEditionRef: FPFCorePatternSet@current
  reliedOnContentRefs: [selected_Core_authoring_and_quality_rules]
  namedUse: local_process_authoring
  dependencyDirection: local_to_Core
  dependencyReason: the selected Core rules are required constraints on the affected local guidance; removing or relevantly changing them invalidates or reopens that guidance
  refreshConditionRefs: [G.11-Core_pin_or_selected_rule_change]
```

If one named cross-relation receiver also needs the generic view, add one `PatternFrameworkRelationRecord`, give both forms the same `subjectAssertionRef`, and set the dependency record's `genericRelationRecordRef` to that row. In the generic row, `relationFunctionClaimRef` points to the E.4.PFR:3.4 dependency predicate, `dependencyOrEditionEffect` states the E.5.3-constrained direction, and `refreshOrSupersessionCondition` cites the G.11 refresh condition. Derive their shared endpoints, use, direction/effect, and refresh condition from the subject assertion. A change to that assertion refreshes both views together; neither carries an independently maintained copy of the dependency fact.

If this same pair also has a supported compatibility result for an overlapping use, state that C.2.1 assertion separately. Add its ref to `compatibilityClaimRefs` only when the named edition-impact receiver must traverse from this dependency record to that claim. The dependency record proves neither dependency nor compatibility, and E.5.3 does not own either edition.

#### E.4.PFR:4.3 - Source and decision reuse

```text
PatternFrameworkRelationRecord@HydroponicCucumberDomain:
  relationId: PFR-HC-SRC-001
  sourceRef: G2-HC-nutrient-source-pack
  targetRef: HC.NutrientMonitoringPattern@draft
  relationFunction: Source or decision reuse
  governedUse: the solution uses selected source-pack claims by value for nutrient-monitoring guidance
  subjectAssertionRef: HC-NutrientSourceUseAssertion
  relationFunctionClaimRef: exact G.2 bounded source-use ClaimGraph
  preservationOrAdmissionRef: C.33-source-pack-summary-loss-note
  blockedStrongerReading: not framework dependency, specialization, publication, derivation, evidence, or assurance
  sourceReturnCondition: reconsider when including an omitted rival horticulture tradition could change the selected source answer or bounded nutrient-monitoring use
```

A hydroponic framework may separately carry a Core-edition dependency, publication relation to its all-in-one carrier, access relation to a grower-assistant skill pack, specialization relation for a narrowed authoring pattern, and quality relations for evaluated drafts. Each remains a different assertion and optional row.

#### E.4.PFR:4.4 - Genuine overlap conflict

A named automated replay receiver has two exact, accepted, witnessed, independently sufficient bases for the same subject, use, scope, and time cell, and their consequences conflict. Lane 1 can state the conflict but cannot give that receiver a stable closed family-plus-pairwise result. The basis analysis retains both alternatives, records the exact pairwise conflict, returns `established-conflict`, and leaves unrelated work available. It selects no winner, grants no permission, and changes no actual-use fact.

### E.4.PFR:5 - Bias-Annotation

**Scope.** The assertion-first discipline is **Universal within this pattern's subject**: every claimed relation starts as a readable assertion with its subject, relation function, basis, polarity, and current facts. The reusable row, dependency record, package manifest, and high-cost basis analysis are **limited** tools for a named framework-maintenance use whose next action needs them; none is a prerequisite for ordinary relation prose.

| Lens | Boundary |
| --- | --- |
| **Gov** | A row or analysis grants no authority, acceptance, permission, or reliance. |
| **Arch** | Assertions, relations, records, editions, publications, carriers, and access routes stay distinct. |
| **Onto/Epist** | A representation cites an assertion but neither creates the relation nor proves more than its bounded basis. |
| **Prag** | Stop after the direct assertion unless a named next action needs more structure; keep high-cost analysis exceptional. |
| **Did** | Lead with the readable assertion and introduce optional machinery only through a concrete receiving use. |

The first drift is relation-word overread: words such as *depends*, *uses*, *supports*, *governs*, or *profiles* are treated as if they settled relation function. Recover the exact subject assertion and blocked stronger readings.

The second drift is record prestige: a standardized row is required before the assertion can count. Keep the direct assertion as default and demand a named receiver for every row.

The third drift is software-package analogy: compatibility, endpoints, and access carriers are useful, but framework relations are not build imports, module calls, APIs, runtime routes, permissions, or performed Work.

The fourth drift is basis inflation: definition, citation, evidence, or later sufficiency is mistaken for actual formal-premise use or criterion selection, and every actual-use claim receives a complete analysis. Keep actual use exact and open analysis only for its high-cost receiver.

### E.4.PFR:6 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFR.1 Assertion first | Every load-bearing claim has an exact subject, relation function, defining or constraining ClaimGraph, polarity, and current basis; a PFR row is optional. |
| CC-PFR.2 Named row receiver | Every row names a framework-maintenance, impact, comparison, repair, or refresh use that changes action; otherwise delete the row and retain the assertion. |
| CC-PFR.2a Smallest receiver form | A cross-relation consumer uses the generic PFR row; a dependency-impact or refresh consumer uses the dependency-specific record. Both forms appear only when one named receiver needs both, cite the same subject assertion, link explicitly, derive overlapping values from that assertion, and share one refresh rule. |
| CC-PFR.3 No owner field | No generic subject-pattern relation, owner field, pattern agency, authority, receiver, or destination is asserted. |
| CC-PFR.4 Function before label | Relation function is selected by what the claim does, not by word similarity, adjacency, table position, or graph direction. |
| CC-PFR.5 Dependency separated | Framework-edition dependency remains separate from compatibility, specialization, publication, recommendation, preservation, derivation, and evaluation. |
| CC-PFR.5a One direct dependency per record | Each `FrameworkEditionDependencyRecord` names one dependent edition, one relied-on edition, and that dependency's content refs, use, direction, reason, and refresh conditions together. Several dependencies use separate or keyed records; any aggregate is a derived projection, never parallel lists or a second maintained truth. |
| CC-PFR.5b Dependency predicate recoverable | Each positive dependency assertion names the dependent edition, relied-on edition, exact relied-on content, named use, and the case fact that makes the content required: removing it or relevantly changing it invalidates the dependent content/result or reopens the use. The assertion and any record cite the E.4.PFR:3.4 predicate. |
| CC-PFR.6 Stable direction | E.5.3 constrains allowed dependency direction and Core acyclicity only after dependency is identified; it cannot establish the relation. G.11 supplies currentness and refresh only. |
| CC-PFR.7 Compatibility independent | A positive compatibility claim names the exact pair, overlapping use, difference or interface, impact, and reopen condition. Insufficient basis yields no positive compatibility claim. |
| CC-PFR.7a Optional link only | A dependency record cites `compatibilityClaimRefs` only for a named maintenance consumer and only after the pairwise compatibility assertion exists independently; the ref creates neither claim. |
| CC-PFR.8 Carrier meanings preserved | Publication, access, preservation, admission, source, Work/tool, evidence, assurance, and currentness claims keep their exact patterns and identities. |
| CC-PFR.9 Actual-use truth | `derivedUsingRuleContent` or `evaluatedAgainstRuleContent` cites the exact actual-use claim and satisfies its strict truth condition. |
| CC-PFR.10 Analysis threshold | Candidate-family analysis exists only for a named comparison, replay, same-subject conflict, or reliance receiver and includes only candidates, axes, pairs, conflicts, and receiving-edition distinctions whose resolution can change the exact cell disposition or named receiver action. |
| CC-PFR.11 Analysis closure | The candidate universe, in-scope axes, required pairwise results, temporal cells, established family, and exactly one disposition are recomputed together for every cell whose disposition or named receiver action can change. |
| CC-PFR.12 Non-permissive boundary | A basis answer supplies no authority, permission, gate passage, Work, actual use, evidence, assurance, or reliance by implication. |

### E.4.PFR:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Related-pattern flattening | A relation list hides subject, function, predicate, and blocked reading. | Recover the exact subject assertion first; add a relation-specific row only for a named PFR receiver. |
| Mandatory row for every relation | Representation burden becomes an ontology and ordinary authoring becomes record-first. | Keep lane 1; open lane 2 only above its receiver threshold. |
| Pattern owner or governor | A pattern locator becomes a semantic owner, authority, or relation participant. | Cite the exact defining or constraining ClaimGraph and state the subject assertion. |
| Dependency as specialization | Edition reliance is read as child-pattern inheritance. | Use the exact dependency assertion; add a dependency-specific record only when a named dependency-impact or refresh receiver needs it, and state specialization separately if it also obtains. |
| Compatibility folded into dependency | A dependency sentence or record carries `compatibilityBoundary` and makes one relation stand for two claims. | State dependency and pairwise compatibility separately; add only an optional ref from the dependency record when a named maintenance consumer needs the link. |
| Compatibility by version label | An edition number is assumed to settle compatibility. | Inspect the exact pair, overlapping use, difference or interface, impact, and reopen condition; otherwise make no positive compatibility claim. |
| Generated graph as authority | A search or graph artifact decides relation meaning. | Use C.35 for candidate admission, then test the exact subject predicate. |
| Callable route as dependency | A skill, endpoint, or assistant integration is treated as framework dependency, method order, permission, or Work. | State only the exact bounded access relation; keep runtime/tool/work/currentness claims separate. |
| Source prose as basis truth | "supports" is read as formal-premise use, evidence, or sufficiency. | Separate bounded G.2 source use, actual-use predicate, evidence, and candidate evaluation. |
| Silent conflict winner | One sufficient base overwrites another in the same cell. | Preserve both and record pairwise conflict; return `established-conflict` and open bounded E.9. |
| Analysis as permission | A compatible or established family is treated as authorization or reliance. | Use the separate A.10/B.3 and authority/permission claims required by the attempted use. |

### E.4.PFR:8 - Consequences

**Benefits.** Readable assertions remain cheap. Named maintenance receivers gain stable rows for relation comparison, edition impact, publication/dependency repair, and refresh. Dependency and pairwise compatibility can change independently and reopen only affected claims. Actual use, candidate bases, conflicts, and downstream reliance become inspectable without adding governance kinds or owner relations.

**Costs.** Any selected generic row or dependency-specific record must resolve an existing assertion and exact ClaimGraph rather than citing a heading. High-cost analysis requires complete candidate and pairwise work. Existing record-first schemas and owner fields need repair.

**Limits.** E.4.PFR neither defines every subject relation nor decides source acceptance, evidence, assurance, permission, actual Work, publication, or currentness. A row cannot repair missing subject semantics. A basis analysis cannot manufacture a candidate, actual-use claim, or authority result.

### E.4.PFR:9 - Rationale

FPF pattern ecosystems are declarative relation systems. Their descriptions state predicates, constraints, dependencies, publication and access arrangements, quality relations, and source uses; the patterns themselves do not act on one another. A sequence of pattern descriptions may describe a method or constrain a separately admitted transformation-flow structure, but displayed order alone performs no Work and admits no Transformation or flow.

The assertion-first rule follows C.2.1 identity and A.22.CGUS declarativity. It avoids building a second ontology of pattern ownership while retaining exact relations already supplied by the Core. PFR is a projection for named maintenance use, not the semantic source.

The three-lane split also controls cost. Lane 1 dominates whenever it closes the task. Lane 2 adds standardized form only for a consumer. Lane 3 separates actual-use truth from optional basis analysis and keeps its output non-permissive.

### E.4.PFR:10 - SoTA-Echoing

| Source and status | Useful pressure | FPF mutation and boundary |
| --- | --- | --- |
| Official Dyad changelog, Components, and Analyses documentation, moving `/stable/` pages observed with release 3.2.0 dated 2026-07-08 | Current implementation comparator: reusable component declarations and connections remain distinct from analyses, solution objects, and generated artifacts. | Use the separation to stress declaration, actual use, analysis, and carrier boundaries. The moving pages are neither edition-pinned source nor FPF ontology; no Dyad object or dependency enters FPF. |
| Modelica Language Specification 3.6 | Historical acausal-modeling lineage illustrates declarative equations and connections distinct from solver execution. | Retain as lineage only, not the current comparator or SoTA claim. Import neither class-model, equation, solver, simulation, nor package ontology. |
| SysML v2, deliberately excluded | For this comparison it is neither a current practice comparator nor useful lineage; treat it as an intentionally excluded historical dead end, not as SoTA by search prominence or by the word “systems”. | Import no UML/SysML metamodel, diagram, package, or workflow semantics. Reopen only if concrete working-project evidence shows a non-dominated gain for this exact relation-maintenance question. |
| Semantic Versioning 2.0.0 and Chen et al., *Breaking Changes in Software Ecosystems: A Systematic Literature Review* (2026) | Compatibility requires explicit boundaries and impact inspection rather than labels alone. | Adapt compatibility, deprecation, supersession, and impact discipline to framework editions; reject binary/build dependency semantics. |
| Nazar, *Software Product Line Engineering: Adoption, Tooling and AI Era Challenges* (2026) | Related product families need core assets, variability, and evolution discipline. | Adapt stable-Core and variation reasoning to FPF/domain/local framework editions without making them software product lines. |
| Riehle, Harutyunyan, and Barcomb, *Pattern Discovery and Validation Using Scientific Research Methods* (2021) | Mined or proposed patterns require validation before reuse. | Generated relations remain candidates under C.35; exact subject assertions and source-use decisions remain separate. |
| ISO/IEC/IEEE 42010:2022 | Narrow architecture-description comparator distinguishes architecture, description, viewpoints, and views. | Use only for the C.30.AD architecture-description boundary. General entity/description and structure/description separation already comes from C.2.1, E.10.D2, A.22, and A.22.CGUS; ISO 42010 does not found a parallel description ontology. |

### E.4.PFR:11 - Relations

- **Builds on:** C.2.1 for subject-assertion and analysis-episteme identity; A.6.P and A.6.RCD for exact relation recovery and reusable predicate definition; A.6.0 for `RuleContentBasisFindingDefinition@R7`; A.6.5 for the boundary that keeps predicate parameters outside SlotSpec; and A.6.6 for claim-scoped basedness. This pattern's §3.4 defines framework-edition dependency; E.5.3 constrains only its allowed direction and Core acyclicity.
- **Coordinates with:** E.4 for framework-family architecture, G.5 for `JointUseSet` and other selected-set results without importing their membership into edition relations, E.4.FPF for FPF form and carriers, E.9 with the E.4.PFAD profile for a framework-architecture answer, C.32.PAD only for an exact project architecture decision, E.11.PUR for recommendation, E.11 for discovery, E.17 for a source-backed publication face and return to source, E.24.PUB for the publication occurrence, form, carrier, audience, bounded use, and availability, and F.18 for names after the value is settled.
- **Coordinates with:** G.11 for edition pins, currentness, and refresh after a dependency is established, never for the dependency predicate; E.22, E.2.DA, E.4.DPF.DA, E.21, and E.23 for quality framing, evaluation, and improvement; G.2 for source use; E.9 for DRR and selected-answer reuse; the exact separate acceptance decision and its authority relation or local rule for accepted-decision reuse; A.10 and B.3 for downstream evidence, reliance, and assurance; and C.33-C.35 for carrier capture, preservation, and admission.
- **Does not replace:** any direct subject pattern, C.2.1 assertion, publication or source decision, evidence or assurance result, authority or permission claim, Work, Method, Transformation, transformation-flow structure, or registered edition.

### E.4.PFR:End

