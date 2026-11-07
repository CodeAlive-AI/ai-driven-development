## A.8 - Universal Core Principle: Test a U-Kind Across Domains

> **Type:** Kernel admission discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.8:0 - Use This When

Use this pattern when a candidate durable U-kind is proposed as a kernel-level universal primitive rather than as a local concept, C.3 `U.Kind`, direct subject-pattern value, Concept-Set row, slot, relation, record, publication form, or dependent durable value.

**What goes wrong if missed.** A local domain noun enters the kernel as if it were universal, or a genuinely universal primitive is rejected because its domain projections use different words.

**What this buys.** Kernel admission becomes a falsifiable cross-domain claim: the candidate must keep the same abstract contribution across diverse domain families while losses and local differences stay visible.

Typical moments:

- a candidate U-kind is proposed because several domains use similar words;
- a local subject value starts being treated as universal because it is useful in one field;
- a new U-kind proposal includes a universal-core claim, or an already admitted kind is being considered for kernel placement;
- source or draft type wording claims kernel-level status and must be recovered into current U-kind governance.

**Primary EntityOfConcern.** The EntityOfConcern is the universal-core admission claim for one candidate U-kind.

**First useful move.** Recover the candidate and its proposed membership or identity rule through `E.24.UK`. If kernel-level status is claimed, test whether it makes the same abstract contribution in at least three foundationally different domain families. Use the applicable accepted admission result for an already admitted kind; a new proposal supplies the shared decision's independently recovered candidate inputs.

**Not this pattern when.**

- If the issue is C.3 typed claim quantification, use `C.3` and `C.3.1`.
- If the issue is whether the public `U.*` spelling should survive at all, use `E.24.UK`.
- If the candidate can be expressed by composition, dependent value, slot relation, or direct subject pattern, use `A.11` and the direct pattern before A.8.

### A.8:1 - Problem Frame

FPF needs universal primitives while keeping domain-specific concepts outside the kernel. A term used in software, finance, biology or physics may still name a local kind. A kernel-level U-kind must retain its defined contribution when applied across the foundational domains in its claimed scope.

When source wording proposes a kernel-level U-kind, recover its admission claim: `E.24.UK` decides durable U-kind admission basis, and A.8 tests the universal-core claim.

### A.8:2 - Problem

Without A.8:

1. **Parochial drift.** A local domain concept enters the kernel and later cracks outside its home domain.
2. **Kernel bloat.** Near-universal values accumulate because each domain asks for its own core noun.
3. **False universality.** Search frequency, source prestige, or familiar spelling replaces cross-domain evidence.
4. **C.3 confusion.** A context-local `U.Kind` is mistaken for a universal FPF U-kind.

### A.8:2.1 - Forces

| Force | Tension |
|---|---|
| Universality vs parsimony | FPF needs a small kernel, but some concepts really do carry the same modeling work across domains. |
| Domain familiarity vs abstract contribution | Familiar words and prestigious sources can hide that the candidate only works in one tradition. |
| Same word vs same work | Different domains may use different words for the same abstract contribution, and the same word may name different local objects. |
| Stable kernel vs evolving FPF | A kernel primitive must survive new pattern families without forcing every local distinction into U-kind status. |

### A.8:3 - Solution

Recover the basis for the three-domain falsification test through `E.24.UK`:

- **Already admitted kind.** Use its applicable accepted admission result and the candidate facts it establishes. Reconsider kernel placement at the claimed scope; an unchanged, still-applicable admission does not need to be repeated.
- **New admission proposal.** Use the independent candidate inputs of the shared decision in `E.24:4.0a`: governed individuals, proposed membership or identity rule, intended extent, nearest non-member and receiving use. Complete the A.8 test alongside the other applicable admission tests, before E.24.UK closes the decision. The projections provide evidence for the core-placement claim; the complete E.24.UK test decides admission.

In either case, the candidate description and the domain evidence must support the comparison independently of the conclusion being sought.

The candidate passes A.8 only when all four conditions hold:

1. **Distinct domain families.** At least three projections come from foundationally different domain families.
2. **Same abstract contribution.** Each projection shows the same kernel contribution, not merely a similar word.
3. **Non-trivial diversity.** Each projection supplies a distinct test of the contribution, with facts or correspondence evidence not subsumed by the other projections.
4. **Recorded losses.** Differences, losses and comparison risks are visible enough to distinguish the shared contribution from local conditions. An F.9 Bridge is needed only for the semantic-correspondence claim governed by that pattern.

Use the following fields to make each projection inspectable. Equivalent prose or a shared table is sufficient when it preserves these values:

```text
UniversalCoreProjection:
  CandidateUKind:
  UKindAdmissionResultRef: exact accepted E.24.UK output, when available; follow it to the shared decision only when common inputs or decision mode are needed.
  DomainFamily:
  DomainTerm:
  LocalEoC:
  SameAbstractContribution:
  DifferenceOrLoss:
  EvidenceRef:
```

For a new proposal, `CandidateUKind` identifies the candidate under consideration. Keep its projection findings with the shared decision's ClaimGraph. Supply `UKindAdmissionResultRef` when an applicable accepted result exists; a pending decision reference is not an accepted-result reference. The other projection values can be supplied and tested before that result exists.

At least three supported projections are required. Try to defeat the proposed universal-core claim: a supported counterexample within its claimed scope refutes that form of the claim. A misidentified local object or invalid projection first needs correction. Three successful cases support this admission test; they do not prove universality over every future case.

### A.8:3.1 - Archetypal Grounding - Diversity Evidence

Test one proposed contribution across different domain families. If it fails a valid projection, reconsider the proposed core claim. Any local, dependent or subject-constrained use of the content still needs the conditions supplied by E.24.UK, A.11 and the defining subject rule.

| Candidate under test | Domain-family projections | What must stay the same | What may differ |
| --- | --- | --- | --- |
| `U.System` | thermodynamic control volume; biological cell or organism; cyber-physical system | acting physical or operational holon satisfying all six constructive components and the applicable kind-specific condition in A.1:4.2–4.3 | boundary physics, substrate, observability, and control style |
| `U.Episteme` | theorem or proof text; clinical guideline; model card or safety case | claim-bearing non-agentive knowledge object that can be used, cited, revised, or published | carrier, notation, authority source, and assurance regime |
| `U.Work` | machining run; lab assay; review or approval act | dated performed occurrence: use the complete A.15.1 admission, including A.1:4.2's six common constructive components, A.13's actual-performer basis, grounded performance history, enacted Method and extent, and facts establishing containment of the complete occurrence under a declared System boundary; F.6 adds an assignment check only when the current use must also say under which assignment the Work was performed | physical medium, institutional form, measurement trace, and evidence carrier |

These rows identify candidate comparisons, not completed admissions. Each needs an E.24.UK basis, actual projection evidence and stated differences or losses.

**Worked projection and counterexample.** Consider an illustrative U.Episteme core claim, with an accepted E.24.UK admission result already available. The receiving team must decide whether one claim-bearing, non-agentive kind can cover mathematical, clinical-research and engineering knowledge objects. Assume the three source epistemes below are independently identified under C.2.1; their stated content is the evidence for this projection exercise.

| Domain family and source | Local EntityOfConcern, claim and effective scheme | Preserved contribution and local limit |
| --- | --- | --- |
| Mathematics: Theorem-e1 | Integer addition; `2 + 2 = 4` under its arithmetic scheme, with a derivation as warrant and no experimental verification. | A non-acting episteme bears a claim about its subject. Mathematical derivation supplies this claim's warrant. |
| Clinical research: StudyReport-e2 | Study S; its report states that 12 of 100 observed cases met outcome criterion O in population P under observation scheme Q. | The same claim-bearing contribution remains; empirical design, measurements and population limits govern this claim's warrant. |
| Engineering: Assessment-e3 | Pump P; the assessment reports 10 L/min at 100 kPa and conformity to R, which requires at least 8 L/min under those same conditions. | The same contribution remains; measurement conditions and the acceptance rule govern this claim's use. |

The three cases test distinct warrant and application conditions while preserving the proposed contribution. The comparison retains the derivation, population boundary and acceptance rule locally; it transfers none of them into a universal assurance rule. Under the stipulated evidence, it supports the claim-bearing U.Episteme contribution in this A.8 test.

Now strengthen the proposed core definition to “every episteme is experimentally verified.” The mathematical case supplies a counterexample within the intended scope: its warrant is derivation, not an experiment. Reject that stronger core claim, retain the supported contribution, and keep experimental verification under the subject and evidence rules that require it. A new counterexample reopens the affected universality claim and uses that depend on it; independently supported claims remain reusable.

**First-admission replay.** Stipulate a proposed edition in which this claim-bearing kind has no accepted admission result. Its candidate description and the independently identified source objects, claims and schemes above supply inputs to the shared E.24 decision. The same projection test can establish the supported core contribution from those inputs. Keep that finding in the decision while the other admission conditions are examined. If the required by-value dependence of downstream uses remains unsupported, admission remains unresolved despite the successful projections. After all conditions for the selected positive form pass, the accepted E.24.UK result supplies `UKindAdmissionResultRef` and naming can proceed. The existing-kind example instead consumes its already applicable result.

Record domain-family coverage, each distinct test, and the differences or losses needed to assess the comparison. Quality-diversity telemetry such as `Diversity_P` or `IlluminationSummary` can contribute only under its governing C.17, C.19 or direct rule; it does not itself admit a U-kind or establish the projection.

### A.8:3.2 - Bias-Annotation

A.8 resists kernel growth based on familiar names because downstream patterns may rely on each admitted primitive. The three-domain test also resists rejection based only on different spellings: compare the actual contribution and retain differences and losses.

### A.8:4 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A8-1` | The test uses the applicable accepted E.24.UK result for an already admitted kind, or the independent shared-decision candidate inputs for a new proposal. `UKindAdmissionResultRef` identifies only an actual accepted result. A new proposal completes the other applicable admission conditions before admission. |
| `CC-A8-2` | The A.8 claim is kernel-level universal-core admission, not C.3 typed reasoning. |
| `CC-A8-3` | At least three domain-family projections are recorded. |
| `CC-A8-4` | Each valid projection tests the same abstract contribution and contributes distinct evidence; repair a misidentified object or invalid projection before judging the candidate. Successful cases support the test rather than proving all future applications. |
| `CC-A8-5` | Differences and losses are explicit; same-word evidence alone is insufficient. |
| `CC-A8-6` | A failed A.8 test does not support the proposed universal-core claim. Reconsider local use, a dependent value, a Concept-Set row, C.3 `U.Kind`, or a subject-pattern expression under E.24.UK, A.11 and the defining subject rule; select an alternative only when its own conditions hold. Rejection or an unresolved proposal remains possible. |

### A.8:4.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| Same-word admission | A term is admitted because many domains use the same word. | Require three domain-family projection records that show the same abstract contribution. |
| Prestige admission | A famous source or standard is treated as universal-core evidence by itself. | Record how the candidate is used in multiple domain families and state difference and loss. |
| Local success as kernel status | A local pattern works well and is therefore promoted to universal primitive. | Try dependent value, Concept-Set row, C.3 `U.Kind`, or direct subject-pattern value first. |
| False demotion by vocabulary mismatch | A universal candidate is rejected because domains use different names. | Compare abstract contribution, not spelling. After the ontic test, use F.18 for naming and F.9 only for a remaining cross-local semantic-correspondence claim. |

### A.8:4.2 - Consequences

A passed A.8 test strengthens the case for kernel placement but does not bypass E.24.UK admission predicates, A.11 parsimony, or the exact subject assertion. A failed test does not support the proposed universal-core claim. Reconsider the useful content under E.24.UK, A.11 and the defining subject rule; a local, dependent, or subject-constrained alternative needs its own basis. The failed placement test does not invalidate an independently established admission. The cost is evidence work across at least three domain families.

### A.8:4.3 - Rationale

Universal core primitives are expensive because every downstream pattern can rely on them. A.8 therefore treats universality as a claim about repeated abstract contribution across different foundational domains, not as a claim about lexical frequency, popularity, or early convenience.

### A.8:4.4 - SoTA-Echoing

The design combines the separation of upper-level commitments from domain concepts, comparison across heterogeneous cases, and explicit treatment of diversity. A.8 uses them as an FPF admission test: identify the same contribution, preserve local conditions, and seek a counterexample. The minimum of three domain families is this pattern's admission rule, not a logical proof of universality. C.17/C.19 govern any quality-diversity telemetry used as evidence.

### A.8:5 - Relations

- **Builds on:** `E.24.UK`, `A.11`, `C.3`, `C.3.1`, `F.8`, and `F.18`.
- **Coordinates with:** Concept-Set and F.18 for naming domain-family projections after the ontic question is settled. Use F.9 only for a cross-local semantic-correspondence claim in comparison, naming or translation: resolve two exact F.17 `SchemeSenseCell` values with different semantic-context projections and test the F.9 predicate under its profile, applicability and dependency conditions. State any proposed use of an obtaining Bridge in a separate bounded-use claim. Ordinary designation or an already shared meaning follows its direct rule.
- **Does not replace:** `E.24.UK` for U-kind admission, `A.11` for parsimony, or `C.3` for typed claim quantification.

### A.8:End
