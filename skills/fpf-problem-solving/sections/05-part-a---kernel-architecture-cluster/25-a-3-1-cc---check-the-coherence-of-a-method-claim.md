## A.3.1.CC - Check the Coherence of a Method Claim

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** a verified bounded claim, one correction returned to the maintained result that owns the contradicted claim, or a named gap. Construction, MethodDescription, representation, support, and trial-evidence claims remain separately governed; coherence establishes neither situational fit nor practical worth.

### A.3.1.CC:0 - Use This When

Use this pattern when Method construction commitments, a MethodDescription, a selected representation, an enactment-support result, or trial evidence no longer agree well enough for a named use. Begin with the possible contradiction and the decision it blocks: which maintained claim may be wrong, incomplete, stale, or unsupported?

The first useful result is a coherence-finding row. It names the claim being checked, its maintained owner and edition, the comparison basis, the observed agreement or defect, the one result to reconsider, and the stop. A truthful `owner-not-recoverable` or `missing-comparison-basis` result is better than declaring the whole Method incoherent.

Here *coherence* is Plain practice wording for checking whether claims relied on for the declared use agree where they should. It is not a new FPF relation, Method admission, fit result, effectiveness result, or universal consistency proof.

Do not use this pattern to decide whether the Method fits another situation, transfers, is worth keeping, caused a result, or is preferable to alternatives. A.3.1.FT owns fit and transfer; C.11.MV owns practical worth. A favourable trial can supply evidence for A.3.1.CC without making its conclusion.

#### A.3.1.CC:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| construction commitment | A maintained B.1.5.CM requirement, component decision, operation declaration, or obtaining-relation claim about the Method under construction. | It is not a sentence in a later description merely because the sentence refers to it. |
| MethodDescription claim | A claim in one A.3.2.DE edition for a named use, including coverage, omission, correspondence, evidence limit, or stop. | Description agreement does not admit a Method or establish that Work occurred. |
| Method representation profile | An C.37.MP result for several unlike Method-related actions. It contains one complete C.37-bearing row per action and a separate cross-use result naming the shared Method source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and changes that reopen several rows. | It does not select a representation for an arbitrary entity, make row colocation a composition result, or establish view, mathematical-lens, publication, or structure conformance by itself. |
| support claim | One A.15.8.MS task, configuration, A.22 proposal or selection position, collection, membership, edition, publication, direct-relation, test, or reliance claim. | A repository or successful tool task cannot repair a contradiction in another maintained result by being convenient. |
| trial evidence | A.3.1.WT occurrence-level observations and gaps qualified for a named later use. | An observation can bear on a claim. Any correction belongs in the maintained result that owns that claim. |
| coherence finding | A bounded agreement, contradiction, missing-information, failed-declared-conformance, or currentness result about one named claim. | “The Method is coherent” is too broad unless every claim relied on and its qualification window are actually in scope. |
| maintained owner | The result whose claim must change if the finding is sustained: B.1.5.CM, A.3.2.DE, C.37.MP, one exact A.15.8.MS result, or another named governor. | The file that displays a claim is not necessarily its owner. |
| declared conformance | A conformance claim with its named scheme, criteria, represented entity, use, and qualification window. | Passing description-side conformance does not establish Method fit, Work performance, or worth. |

### A.3.1.CC:1 - Problem Frame

A Method can be internally plausible while its description omits a required stop, a representation hides a relation needed by its use, or a support route serves an obsolete edition. Trial Work can expose the mismatch, but the mismatch still has to be located. Otherwise every defect is blamed on “the Method”, or every observed failure is pushed into the document that happens to be easiest to edit.

The practical question is narrower: which claim was relied on, what should it agree with, what evidence bears on that agreement, and which maintained result owns the smallest correction?

### A.3.1.CC:2 - Problem

Coherence checks often collapse several questions. Construction conformance is treated as document completeness; description consistency is treated as practical fit; a failed representation is repaired by changing Method semantics; a stale support edition is called a Method defect; or one trial success is taken to verify the whole package.

This makes correction expensive and unsafe. Several maintained results are changed together, the original contradiction becomes unrecoverable, unaffected claims lose their evidence status, and later fit or worth decisions inherit a verdict that A.3.1.CC never established.

### A.3.1.CC:3 - Forces

| Force | Tension |
| --- | --- |
| Local correction | A small owner-specific repair preserves working claims, while a package-wide rewrite feels safer. |
| Construction and description | They must correspond for relied-on uses, while they remain different results with different tests. |
| Representation | A representation must expose what its use needs, while omission can be deliberate for another use. |
| Trial evidence | Actual Work can reveal contradictions, while failure can also come from situation, capability, support, or another direct relation. |
| Conformance | Named schemes can make checks repeatable, while scheme passage can be mistaken for practical adequacy. |
| Currentness | Editions and sources change, while a once-valid claim may remain syntactically consistent and practically stale. |
| Candidate status | Candidate accounts benefit from correction, while coherence must not launder them into admitted Methods. |

### A.3.1.CC:4 - Solution

This is a claim-to-basis comparison for Methods, descriptions, representations and support. Use A.10 for the relied-on evidence and each subject pattern for its positive claim. The local construction below identifies the consequential contradiction or missing basis and returns it to the maintained explanation that can be corrected.

Check one claim relied on for the named use against its declared basis, classify the result, and return any correction only to the maintained result that owns the defeated claim. Recheck the repaired claim while preserving every unaffected status and open question.

When the parts appear locally consistent but the required whole result still has no adequate explanation, use `B.1.5.EW:4.3–4.5` to work back from that result to the constituent contributions and their connections. That supplier covers actual work and proposals for future work; it can expose a required operation or connection whose account is missing. Bring the particular contribution, dependency and supporting basis into step 1 below. Then distinguish a missing construction, an omitted description and an unsupported claim before choosing a correction owner. Agreement among the available parts alone does not settle the whole-result question.

#### A.3.1.CC:4.1 - Pattern-Use Unfolding

1. **Name the blocked use and possible contradiction.** Identify the reader or decision, the claim needed, its qualification window, and what would count as agreement, contradiction, missing information, or a stop. Do not begin with “verify the Method”.
2. **Preserve the subject and status branch.** Identify the admitted Method under `A.3.1`, or keep the proposed whole as a candidate account. Keep Work, WorkPlan, description, representation, support, evidence, publication, and structure claims at their current statuses.
3. **Recover the maintained claim and owner.** Record the claim text or predicate, owning result, edition or occurrence, source or construction basis, intended use, and currentness condition. If ownership cannot be recovered, return `owner-not-recoverable` before editing several carriers.
4. **Check construction claims at B.1.5.CM.** Test construction requirements, component decisions, operation declarations, and obtaining-relation claims separately. Cite the governing FPF predicate where needed rather than recreating its admission test. A failed construction claim returns to that exact B.1.5.CM result.
5. **Check MethodDescription claims at A.3.2.DE.** Test coverage, internal consistency, correspondence with admitted Method claims, navigation for the named use, stated evidence limits, omissions, stops, and any declared description-side conformance. Do not make section count or scheme passage a proxy for useful coverage.
6. **Check representation-use results at the right owner.** For one action, recover its complete representation-use result under C.37 and stop without C.37.MP. For several unlike Method-related actions, recover the [complete C.37.MP profile](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c37mp42---record-the-result), including its shared source and separate cross-use result. Test the contradicted action's claim group and whether the profile relation still holds. The direct FPF governor owns view, mathematical-lens, publication, and structure conformance; if a governed result fails, return that lower result and reopen only the affected use result and cross-use relations that actually depended on it.
7. **Check support results at A.15.8.MS.** Use A.15.8.MS's result distinctions to locate the specific support claim contradicted by the evidence and the result that owns it. Return the repair there; one defeated claim is not a verdict on the whole support configuration.
8. **Use trial evidence to check the maintained claim.** From A.3.1.WT, recover the actual Work occurrence, performer, enacted admitted Method, situation, capability and support conditions, direct relations, result, burden, observation source, and evidence reach. Ask which named claim the observation bears on. A success or failure does not by itself identify the owner.
9. **Classify the finding.** Distinguish: `agreement-within-window`; `contradicted-claim`; `missing-information`; `failed-declared-conformance`; `stale-source-or-edition`; and `owner-not-recoverable`. Do not turn uncertainty into contradiction or a local defect into a whole-Method verdict.
10. **Select one correction owner.** Return the smallest correction to B.1.5.CM construction, A.3.2.DE description, one direct C.37 use row, one complete C.37.MP Method representation profile, one exact A.15.8.MS result, or the direct governor of a lower representation result. If one observation defeats several independent claims, create separate findings with separate owners; do not copy one vague correction into every upstream result.
11. **Repair and repeat the same check.** Preserve unaffected claims, statuses, evidence, and windows. Recheck the repaired claim against the same basis. If the use, subject, source, edition, or criteria changed, start a new coherence use instead of calling the old check passed.
12. **Return the bounded result and non-use.** State the verified claim, correction or gap, owner, affected downstream uses, preserved claims, and reopen condition. Say explicitly that fit, transfer, worth, capability, contribution, causality, admission, and publication remain separate.

#### A.3.1.CC:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| coherence use | Blocked decision, reader, relied-on claim, qualification window, agreement and stop conditions. |
| subject status | Admitted Method or candidate account, plus separately identified Work, WorkPlan, description, representation, support, and evidence results in scope. |
| maintained claim | Claim or predicate, owner, edition or occurrence, source or construction basis, intended use, and currentness. |
| comparison basis | Construction requirement, description claim, selected representation rule, support premise, trial evidence, or declared conformance criterion actually used. |
| finding | Agreement, contradiction, missing information, failed declared conformance, stale source or edition, or missing owner; include the evidence reach. |
| repair routing | One maintained result to reconsider, smallest correction, unaffected claims and statuses, and downstream uses that must be rechecked. |
| rerun | Same-check result after repair, or the changed use or basis that requires a new check. |
| return | Verified bounded claim, corrected claim, or named gap; non-use and reopen condition. |

#### A.3.1.CC:4.3 - What Changes in Practice

Teams stop repairing the nearest document or declaring the whole Method inconsistent. They can identify the defeated claim, distinguish construction from description, representation, support, and evidence, and send one correction to its maintained owner.

The correction becomes cheaper to review and safer to reuse. Unaffected claims keep their status, and later fit and worth judgments receive a precise repaired input rather than a package-wide confidence label.

#### A.3.1.CC:4.4 - Minimal Constructed Coherence Replay

Continue the constructed A.3.1.WT trial of admitted `M-Unit-Review-1`. Construction result `CCR-UR-1` states that unit identification and normalization precede tolerance comparison. MethodDescription edition 4 says the same and exposes the unresolved-mismatch stop.

Only one current action is at issue: `Reviewer-17` must use the flow representation to guide pre-release unit review. Direct use result `C37-UR-Flow-4` therefore takes the C.37 exit rather than opening C.37.MP. It returns to that Method and description edition, requires unit identification, normalization before tolerance comparison, the comparison branch, and the unresolved-mismatch stop, and uses governed representation result `REP-UR-Flow-4`.

Exact claim: that representation exposes those operations in order for the named review action. A.2.4 classifies the intended preparation use; A.10 path `P-UR-Flow-4` carries the current-edition premise with `RelianceDisposition=pass` for the review window. Receiving task criterion `UR-PreRelease-Guide-4` permits use only while those claims remain exposed. The row omits unrelated support-edition detail, preserves Method, description, representation, and Work status, is `select` for that action, and returns a missing exposure to the direct representation governor and this use row.

A.15.8.MS supplies the current conversion table used in `W-Disc-1`.

The trial evidence records that `Reviewer-17` normalized the Celsius/Kelvin values before comparison and stopped the release decision. Inspection of `REP-UR-Flow-4`, however, shows identification followed directly by tolerance comparison; the normalization operation is absent. The finding is not “the Method is incoherent”. The construction claim, description claim, support edition, and observed Work agree within this slice. The contradicted claim is the `C37-UR-Flow-4` exposure claim for its exact action; no C.37.MP profile exists or is needed for this one-use case.

Return `CORR-C37-UR-1`: revise governed representation result `REP-UR-Flow-4` and its direct use row to expose normalization and the unresolved-mismatch branch, or narrow the row's action, required claim, and omission account. Preserve `M-Unit-Review-1`, MethodDescription edition 4, `W-Disc-1`, its task result, and the conversion-table support result. Recheck the same exposure claim after repair. Do not infer fit or worth from the successful Work occurrence.

| If the observed defect were instead... | Owner to reconsider | Result not to change automatically |
| --- | --- | --- |
| The admitted construction omitted any normalization requirement while the named problem required one. | The exact B.1.5.CM construction or requirement result. | A.3.2.DE and every affected direct C.37 use row or complete C.37.MP profile until their own action claims and dependent cross-use relations are checked against the changed construction. |
| MethodDescription edition 4 reversed the declared operation order while construction and Work supported the original order. | The exact A.3.2.DE description claim and edition. | Method identity and the Work occurrence. |
| The retrieved conversion table used a stale scale while construction, description, and representation were correct. | The exact A.15.8.MS edition, retrieval, or named-user task result. | B.1.5.CM construction and every unaffected direct C.37 use row or complete C.37.MP profile. |
| The source cannot show which of those positions is wrong. | `owner-not-recoverable` with the missing comparison basis. | All maintained results until evidence distinguishes them. |

### A.3.1.CC:5 - Archetypal Grounding - Representation Difficulty in SSFD

The SSFD workplace evidence reports that Project 32 had difficulty representing the relation between a closed-loop sensor and controller. This is a useful coherence trigger because the difficulty may concern Method semantics, a MethodDescription claim, a selected representation, support material, or a situation-specific applicability boundary.

The report does not by itself identify which maintained result owns the defect. Recover the receiving action, contradicted claim and its complete use basis through §4.1(3,6) before choosing a correction owner.

For one sensor-controller representation use, inspect C.37 and the direct representation governor without invoking C.37.MP. If several unlike Method-related actions are current, use the complete C.37.MP profile identified in §4.1(6) and locate the affected action and dependent cross-use relation. The report does not establish that profile by itself.

If the facts locate a failed exposure claim, return the owning row and only the cross-use relations that depended on it; if they locate a construction or description contradiction, return it to B.1.5.CM or A.3.2.DE. If the report cannot distinguish the owner, return `owner-not-recoverable` rather than calling SSFD incoherent.

Project 11 records a different application and many reported results. It is neither the counterfactual for Project 32 nor proof that the same representation claim was coherent there. The 41-report set and its 95 reported benefit instances concern later evidence use; they do not erase the Project 32 difficulty or establish practical worth inside A.3.1.CC.

#### A.3.1.CC:5.1 - EC-417 Early Stop

The [full EC-417 application](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#fpfreference169---choose-the-smallest-method-development-result-needed-for-release-ec-417) supplies the receiving problem, alternatives, calculations and the distinct limits used below.

`C-EC-Release-v2` remains a candidate account and the three-release statement remains a WorkPlan. A.3.1.CC may check current description, representation, A.15.8.MS task, collection, edition, reliance, permission, application, Work, result-binding, and proposed-organization claims against their own bases. It must not verify planned releases as performed Work or call the candidate whole coherent as a Method.

For every correction, name the exact maintained position. A stale method-base edition returns to that edition result. A failed viewpoint rule returns the lower episteme and failed `E.17.0` rule to their direct governor. Recheck the action's complete C.37 basis when that use relied on the failed result. For an C.37.MP profile, follow §4.1(6) and recheck only its actually dependent cross-use relations. A missing A.22 selection-use basis remains the already named gap. Keep the observed support results separate from the missing tailoring definition and untested permission/authority stop; none supplies release evidence.

### A.3.1.CC:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| package-coherence bias | One local contradiction becomes a verdict on the whole Method package. | Bound the claim, use, owner, and window before checking. |
| document-owner bias | The document displaying a claim is edited even when construction or support owns it. | Recover the maintained result and direct governor. |
| success-verifies-all bias | One favourable Work occurrence verifies construction, description, representation, and support together. | Ask which named claim the observation actually bears on. |
| conformance-as-performance bias | Description-side conformance becomes fit or effectiveness. | Keep scheme passage inside the declared description use. |
| repair-fanout bias | The same correction is copied into every upstream carrier. | Route each contradicted claim to one owner; create separate findings only for separate claims. |
| source-authority bias | A published report is treated as direct admission and owner identification. | Preserve the evidence path and return missing occurrence or owner facts. |

### A.3.1.CC:7 - Conformance Checklist

- [ ] The blocked use and one claim relied on for that use are named.
- [ ] The Method is admitted or the proposed whole remains a candidate account.
- [ ] Construction, MethodDescription, representation, support, Work, and evidence results retain separate identities and statuses.
- [ ] The claim owner, edition or occurrence, intended use, source, and currentness window are recoverable.
- [ ] Trial evidence is qualified, and the claim's maintained owner remains explicit.
- [ ] Agreement, contradiction, missing information, failed declared conformance, staleness, and missing owner are not merged.
- [ ] Every correction returns to one maintained result and preserves unaffected claims.
- [ ] A repaired claim is rechecked against the same basis, or a changed basis starts a new use.
- [ ] No coherence result is overread as fit, transfer, worth, contribution, causality, capability, admission, or publication.

### A.3.1.CC:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The trial failed, so rewrite the Method.” | Locate the contradicted claim and rule out situation, capability, support, and relation gaps first. |
| “The standard checklist passed, so the Method is coherent.” | State the declared conformance use and every claim outside its scope. |
| “Fix the diagram and the description together.” | Determine whether one or two independent claims are contradicted and route each separately. |
| “Project 32 proves SSFD is inconsistent.” | Treat the reported representation difficulty as evidence that opens an owner-specific check. |
| “No contradiction was observed, so coherence is proven.” | Return agreement only for the claims, evidence, and window actually checked. |

### A.3.1.CC:9 - Consequences

Coherence work becomes a repair-routing practice rather than a package-wide verdict. A practitioner can see which claim failed, why it failed, what remains valid, and which downstream decisions need the repaired result.

The cost is explicit ownership and comparison recovery. Some checks end with a missing owner or missing basis, and a team may have to preserve several plausible defect locations instead of choosing the easiest file to edit.

### A.3.1.CC:10 - Rationale

Method construction, description, representation, support, and trial evidence are coupled by use but are not interchangeable. Their claims can agree, disagree, or become stale independently. Returning each correction to one maintained owner protects that independence and keeps coherence separate from Method admission and effectiveness assessment.

The same evidence may support several checks, but its use relation is different in each. Treating evidence as a common source rather than a common verdict lets later fit and worth decisions reuse it without inheriting A.3.1.CC's scope.

### A.3.1.CC:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Ralyté, Koutsopoulos, and Stirna, [verification, validation, and evaluation of modeling methods](https://doi.org/10.1007/s10270-025-01304-2) | Keep verification, validation, and evaluation questions separate and use evidence to locate the claim under check. | The source is modeling-Method focused and does not supply one universal FPF owner map or prove practical worth. |
| [ISO/IEC/IEEE 24774:2021](https://www.iso.org/standard/78981.html) | Use description elements, rules, views, and declared description-side conformance as selectable comparison bases. | The standard does not make description conformance a Method admission, fit, or performance result and is not imported as FPF ontology. |
| Cash, Daalhuizen, and Hekkert, [method efficacy and effectiveness](https://doi.org/10.1016/j.destud.2023.101204) | Preserve the difference between internal or use-side adequacy questions and practical effect questions. | The contribution does not supply a universal coherence score or make one successful occurrence decisive. |
| Current FPF `A.3.1`, `A.10`, `C.2.1`, `E.17.0`, `A.22`, and the direct governors cited by the maintained claim | Reuse Method admission, claim-bound evidence, episteme and edition identity, view conformance, structure selection, and direct predicate tests. | A.3.1.CC contributes owner-specific comparison and correction routing; it does not redefine those identities or predicates. |

Reopen the pattern when practitioners cannot identify one maintained owner without changing the architecture, when repeated findings require a distinct independent coherence problem, when a source supplies a stronger owner-discrimination method, or when a governing FPF predicate changes the repair route.

### A.3.1.CC:12 - Relations

- B.1.5.CM supplies construction commitments and obtaining-relation results; A.3.2.DE supplies MethodDescription claims and use coverage; C.37 supplies one-action representation-use results; C.37.MP supplies complete Method representation profiles for several unlike Method-related actions, with their action rows and separate cross-use result; A.15.8.MS supplies task, support, collection, edition, publication, relation, test, and reliance results. Each remains the owner of its own claim, while a lower representation result remains with its direct FPF governor.
- A.3.1.WT supplies occurrence-level observations and gaps. It neither identifies the correction owner automatically nor establishes coherence.
- A.3.1.FT consumes coherent-enough claims and situation evidence for fit or transfer. C.11.MV consumes results and evidence limits for practical worth. Neither conclusion is returned by A.3.1.CC.
- `A.3.1` governs Method admission; `A.10` governs claim-bound evidence use; `C.2.1` governs episteme and edition identity; `E.17.0` governs view conformance; `A.22` governs selected structures. Cite the direct governor for every other predicate checked.
- A.3.1.MV receives a variant question only when a proposed repair changes reusable Method semantics; a document, representation, support, or local Work correction alone does not identify a Method variant.

### A.3.1.CC:End
