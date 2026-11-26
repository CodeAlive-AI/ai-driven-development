## SIE.6 - Fuse Source-Qualified Claims without Erasing Conflict

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SourceQualifiedClaimFusion@Use` that preserves each source claim, subject and any relied-on identity premise, scope, interval, authority, uncertainty, derivation, and relation to other claims, then returns a qualified view, explicit conflict, non-comparability, or unresolved result for one receiving use.

### SIE.6:1 - Problem Frame

**Use this when** a receiving answer must combine claims from separately governed sources and a simple union, priority rule, average, overwrite, or “golden record” would hide differences in meaning, subject, time, authority, or uncertainty. The recognizable failure is one clean value whose provenance can be displayed but whose conflict or non-comparability can no longer be recovered.

For one receiving question, state the source claims and the subject relation it requires. The first result is either a qualified view with its derivation or a conflict, non-comparability or unresolved branch.

The receiver can interpret the answer and its grounds. Do not use SIE.6 to decide domain truth, authoritative value, survivorship, risk acceptance, or action. The authorized domain or receiving participant may use the composition to choose. Preserve the basis for that choice.

### SIE.6:2 - Problem

Claims that share a field name can concern different concepts, entities, grains, intervals, or authority scopes. Claims that do concern the same entity can disagree without either being malformed. A timestamp does not settle whether one claim supersedes another; a source rank does not explain why the rank applies; and an average can be meaningless across different measurement definitions.

If composition silently collapses these differences, later validation can test only the fused value. It cannot test the losing claim, the identity premise, the conflict rule, or the receiver's permitted use. Provenance survives as a list of sources but no longer constrains meaning.

### SIE.6:3 - Forces

| Force | Tension |
| --- | --- |
| Simplicity | Receivers may prefer one view even when the source claims warrant several qualified rows or an explicit conflict. |
| Authority | Some sources are authoritative for bounded claims, while no source may own the whole receiving question. |
| Time | Newer claims may supersede older ones, while differing intervals, effectivity, or observation times can make them jointly informative. |
| Identity | Composition needs a subject relation, while an unresolved identity premise must stop only the dependent branch. |
| Uncertainty | Quantification can support comparison, while unlike confidence, status, or evidence forms should not be normalized without warrant. |
| Performance | Precomputed canonical values are convenient, while preserving source-qualified alternatives and derivation costs storage and query work. |

### SIE.6:4 - Solution

Compose claims only after their meanings, subjects, scopes, intervals, authority, uncertainty, and provenance are explicit. Classify the relation among claims before applying a rule. Preserve the source claims and any relied-on identity premises in the result. Return a qualified view only under a stated rule and use boundary; otherwise return conflict, non-comparability, or unresolved.

#### SIE.6:4.1 - Pattern-Use Unfolding

1. **Name the receiving question and action.** State what the composed answer may change and which outcomes are acceptable: one qualified row, several rows, conflict, non-comparability, unresolved, or stop.
2. **Identify the source claims.** Reference `SIE.2` rows and `SIE.4` correspondences. Record each proposition or data-derived claim, scope, interval/effectivity, units, status, uncertainty, derivation, source, and authority.
3. **Bind the subject relation needed by the use.** Reference `SIE.5` when composition depends on claims concerning the same entity. For separately attributed claims about distinct subjects, preserve their subjects and attribution. Keep an explanation of unused identity only when it affects interpretation or later reliance. A correspondence alone does not establish subject identity.
4. **Test comparability.** Decide whether claims use compatible concepts, subjects, grains, units, intervals, and observation/decision roles. Preserve non-comparability as a result.
5. **Classify the claim relation.** Distinguish compatible conjunction, refinement, overlap, duplication, supersession under a justified rule, contradiction, non-comparability, and unresolved relation. For refinement, compare what the two claims permit for the same receiving question under the established interpretation. Match their subjects, meanings and applicable times or conditions. Show a case the proposed refinement admits and why every such case satisfies the earlier claim. To establish a strictly narrower answer, identify an answer to the receiving question that has been ruled out. A later report about a different time can instead supersede an earlier report for a current decision under the applicable rule.
6. **Choose a bounded composition rule.** Examples include retaining all qualified claims, selecting one claim under an explicit domain authority/effectivity rule, deriving a new claim through a stated calculation, or returning conflict. Choose from the receiving operation. For a threshold, use the admissible joint values to bound the quantity that actually matters. For a common action, check that the same option is admissible across the cases the receiver cannot distinguish in time. For a list of individual claims, retain the distinctions needed to settle membership. Explain any loss that affects reliance.
7. **Construct the qualified output.** Include the source claims or stable references, applied rule, any relied-on identity premise, derived value if any, provenance/trace, authority boundary, uncertainty, conflict/non-comparability status, and permitted receiving use.
8. **Expose failure and challenge.** Define missing-source, stale-source, unresolved-identity, incompatible-unit, contradictory-authority, and unsupported-default branches. Do not convert them into null or a chosen value without the contract's permission.
9. **State downstream and reopen conditions.** Identify mappings and interfaces that consume the composition and the source, identity, rule, authority, or use change that reopens it.

#### SIE.6:4.2 - Record the Result

| Composition position | Required content |
| --- | --- |
| receiving use | question, action changed, acceptable output branches |
| source claims | propositions or data claims, meanings, subjects, scopes, intervals/effectivity, units, status, uncertainty, source and derivation |
| identity premise | referenced `SIE.5` disposition when composition relies on identity; an explanation of unused identity only when it affects interpretation or later reliance |
| comparability | compatible dimensions and any difference that prevents comparison |
| claim relation | conjunction, refinement, overlap, duplicate, qualified supersession, contradiction, non-comparability, unresolved |
| composition rule | rule, authority/evidence basis, conditions, rejected alternatives, semantic loss |
| output | qualified view or explicit conflict/non-comparability/unresolved result, provenance/trace, permitted use |
| downstream and reopen | mapping/interface references, failure branches, changes that reopen the composition |

#### SIE.6:4.3 - What Changes in Practice

The team stops treating a canonical value as the natural output of integration. A receiver can see why claims were combined, retained separately, or stopped, and can return to the source, identity, authority, or rule that changes the answer.

### SIE.6:5 - Archetypal Grounding - Provider Availability Claims

Two providers expose availability for the same buyer-recognized product family. Provider A returns `onHand = 12` at 10:00; Provider B returns `availableToPromise = 9` at 10:02. A purchasing integration initially proposes a single `available = 21` value.

The source inventory shows that `on hand` is current physical stock before reservations, while `available to promise` is a provider-governed commitment quantity after its own reservation and horizon rules. The values are not additive and are not globally equivalent. A product-family correspondence exists, but individual inventory objects are not asserted identical.

| Claim relation question | Constructed result |
| --- | --- |
| Can the two values be summed? | non-comparable for summation because definitions, allocation rules, and authority scopes differ |
| Which provider can supply eight units now? | One provider whose qualified promise covers the product, quantity and time suffices if the buyer wants one source. For a complete list, settle both providers under their own rules. Use A's reservations and B's promise horizon where their values determine eligibility. |
| What if Provider A reports 12 and a later status reports 4? | classify by source occurrence, observation interval, and justified supersession rule; retain both claims and derivation rather than overwriting silently |
| What if product identity is unresolved? | retain the `SIE.5` alternatives. If there are admissible bindings and all of them give the same answer to the buyer’s question, return it with the identity limit. Withhold an individual match or recommendation that changes with the binding |
| What if one API times out? | return available source-qualified rows plus an incomplete-result flag if the contract permits; never substitute zero |

The interface can return two qualified provider rows, explicit non-comparability for arithmetic aggregation, and a missing-source branch. Purchasing owns supplier choice and risk acceptance.

### SIE.6:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | A source priority table silently decides truth or business action. | Name the authority and claim scope for every selection or supersession rule. |
| Architecture | The target schema requires one value and erases alternatives. | Change the output shape or expose conflict/non-comparability as first-class branches. |
| Ontology/Epistemology | Data values, claims, facts, and decisions collapse. | Record propositions, scope, uncertainty, derivation, and receiver decision separately. |
| Pragmatics | Every disagreement becomes an elaborate dispute. | Classify only relations that can change the receiving answer; retain independent claims without forced comparison. |
| Didactics | “Fusion” is read as merge or averaging. | Show examples where the correct fusion is a qualified set, conflict, or non-comparability. |

### SIE.6:7 - Conformance Checklist

- [ ] The receiving question and every allowed output branch are explicit.
- [ ] Source claims retain meaning, subject, scope, interval/effectivity, units, status, uncertainty, source, and derivation.
- [ ] Every load-bearing subject identity premise is referenced and tested.
- [ ] Comparability is judged before aggregation or selection.
- [ ] Compatible, refining, overlapping, duplicate, superseding, contradictory, non-comparable, and unresolved relations are distinguishable.
- [ ] A composition rule states its authority/evidence basis, conditions, rejected alternatives, and loss.
- [ ] Source claims remain recoverable from the output.
- [ ] Missing, stale, unresolved-identity, incompatible-unit, contradictory-authority, and default branches are explicit where applicable.
- [ ] The result does not claim domain truth, authoritative value, preference, authorization, or action beyond its source and receiver boundaries.

### SIE.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Last write wins | State why time establishes supersession for this claim and interval; otherwise retain both. |
| Trusted source always wins | Name the scope of the source’s authority and preserve losing claims and conflict. |
| Average the values | Establish compatible meaning, subject, unit, interval, and aggregation semantics first. |
| Null means zero or absent | Preserve missing, unavailable, unknown, not applicable, and zero as distinct branches. |
| Provenance after fusion | Keep source claims and derivation as inputs to the composition, not decoration on the result. |
| One canonical fact | Return a qualified view only when the use and authority rule warrant it; otherwise return plural claims or conflict. |

### SIE.6:9 - Consequences

Receivers obtain explainable views and conflict branches. Corrections can target the source claim, identity premise, composition rule, or receiving use without reconstructing an opaque golden record. Different receiving uses can justify different bounded views of the same preserved claims.

The cost is richer output and explicit rule ownership. Some applications must handle plural, incomplete, or conflicting results instead of one scalar value.

### SIE.6:10 - Rationale

A source claim asserts something about a subject within a stated scope. Composition is a new derivation whose premises and authority must remain inspectable. Preserving the inputs is what makes conflict, correction, and changed-use replay possible.

### SIE.6:11 - SoTA-Echoing

The best-known line combines claim individuation, provenance, authority-aware data integration, and explicit uncertainty. The serious default is master-record survivorship or source ranking. Those Methods can be valid under an authorized MDM use, but they are defective as a universal semantic-integration default because they hide non-comparability and transfer authority. SIE.6 adapts the line by making the qualified composition or explicit conflict the domain result.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `C.2.1` | adopt | Keeps claims as distinct representational objects; SIE supplies the cross-source use composition. |
| Current FPF `A.10` | adopt | Governs claim-bound evidence and provenance reliance; evidence law does not choose the domain truth or action. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Supports derivation, attribution, revision, and invalidation traces; provenance alone establishes no truth, priority, or comparability. |
| MDM survivorship and golden-record practice | adapt only under direct authority | May supply an authoritative-value result for a bounded domain; SIE preserves its source and scope rather than generalizing it. |
| last-write, average, or global source-rank defaults | reject as universal | Each may be a justified local rule, but none is semantically safe without compatible claims and authority. |

Reopen when a source claim, identity premise, authority rule, interval, uncertainty model, or receiving use changes, or when representative conflict cases cannot be expressed without hiding action-changing information.

### SIE.6:12 - Relations

- `SIE.2` supplies source claims, meanings, editions, authority, provenance, currentness, and gaps.
- `SIE.4` supplies the qualified correspondences needed to compare claim predicates or values.
- `SIE.5` supplies load-bearing subject identity dispositions; claim conflict does not alter those identities by itself.
- `SIE.7` may implement the qualified composition rule but must preserve its branches and trace.
- `SIE.9` exposes qualified views, plural claims, conflict, non-comparability, and incomplete-source states to the receiver.
- `SIE.10` tests the composition rule and negative branches. MDM, domain, and application owners retain truth, value, preference, authorization, and action.

### SIE.6:End
