## B.3.3 — Assurance Subtypes & Levels

> **Status:** Stable

### B.3.3:1 - Problem Frame

**Use this when.** A team needs to assess a claim for a receiving use, interpret a published assurance level or design criteria for recurring decisions. Start with what the recipient needs to decide, the applicable conditions and the choices left to the assessor. A published profile may have settled some of those choices.

A performance test, a proof and a terminology comparison answer different questions. Treating their presence as a maturity recipe can approve a poorly supported performance claim while demanding an irrelevant proof from a well-supported empirical result.

**Practical gain.** Choose the assurance contribution that can change the receiving judgement, and retain a sufficient qualified result without purchasing evidence merely to raise its label.

**Ordinary boundary.** A source locator, permission, status report or direct domain result that makes no assurance claim needs no B.3.3 classification. An ordinary assurance judgement can use B.3's compact result without constructing a level scheme. A domain's required proof, study or assurance profile applies when its claim and use require it.

### B.3.3:2 - Problem

How can a recipient distinguish relevant conceptual, logical and empirical support without mistaking a link, evidence type, score or maturity label for an argument that the relied-on claim is adequately supported?

The tension is between comparable reporting and unlike assurance questions. Repeatable criteria help a shared use; a universal ladder hides differences in claim scope, consequences, assumptions and admissible evidence. Formal precision helps inspect an inference, but cannot compensate for an inapplicable premise.

### B.3.3:3 - Solution

Use B.3 to identify the target claim and receiving use. Ask what could make the proposed conclusion fail. Follow that possibility to the correspondence, inference or observation that can resolve it. A single applicable argument can settle the use. For a decision requiring several contributions, check that their subjects, conditions and conclusions fit together. A result can be given without an `AssuranceLevel`.

#### B.3.3:3.1 - Assurance subtypes answer different questions

| Subtype | Code | Question answered | Contribution and boundary |
| --- | --- | --- | --- |
| Concept-Bridge Assurance | CBA | Do the load-bearing terms and participants correspond across the descriptions being used? | Compare the relevant meanings, referents and conditions through B.5.3 when movement across vocabularies can change the argument. A discovered or repaired mismatch can change the assurance conclusion. Performing a comparison does not itself improve a relation's congruence. |
| Verification Assurance | VA | Does the claimed consequence follow under the stated specification and assumptions? | Inspect the proof, logical argument or applicable construction. The result supports that consequence under those premises; it does not establish that a running system satisfies its environmental assumptions. |
| Validation Assurance | LA | Does the empirical basis support the claimed performance in the receiving conditions? | Examine relevance, coverage, measurement quality, limitations and contrary results. A simulation supports a claim about its modelled conditions; transfer to a system needs the applicable model-to-world warrant. |

Select the contributions needed by the claim, rather than demanding all three types for every judgement. A mathematical consequence may need a proof and no field trial. An engineering performance claim may have sufficient empirical support without an additional formal proof. A safety-related claim needs the protective argument and required evidence; neither `FV ≥ threshold` nor `EV > 0` establishes that adequacy.

Terms such as `FV`, `EV` or `CL` can be used only with the bearer, scale and interpretation the receiving argument consumes, as in B.3. A field called `verifiedBy` or `validatedBy` identifies a support relation to inspect, not a positive judgement by its presence.

#### B.3.3:3.2 - Use a level only through its justified profile

A domain may define an assurance profile or ordered levels when a recurring receiving decision benefits from that comparison. Its definition states the claim class and use, conditions, meaning of any levels used, evidence rules, the basis for any thresholds, and reconsideration conditions. State the measure and its scale where a threshold is used.

To design such a profile, take the actions its recipients must distinguish and work back to what would justify each. Hold the apparent level fixed and change the subject, the part tested or the conditions of operation. Would the same level now warrant a different action? Retain the difference in the criteria or limit their applicability. Select the grounds for meeting each criterion, including alternative sufficient arguments where the decision permits them. Ask which cases the proposed rule could accept despite a missing condition and which sufficiently supported cases it would exclude. A general argument can settle either question. Adjust the rule to the intended use or retain an exclusion required by that use.

Where levels are ordered, establish the ordering their meanings promise. If one level is said to support every use allowed by another, establish that implication across the applicable conditions. A narrower operating range with better accuracy need not contain a wider range with looser accuracy. State what each qualifies when the uses differ.

To assign or endorse an assurance level on its merits, apply the profile and show how the evidence meets its criteria. To report the level an authority actually assigned, identify the decision, the designation or profile it used and its scope. An error in applying the criteria can change what the assignment warrants while the historical fact of assignment remains established. The legacy names `Unsubstantiated`, `Substantiated` and `Axiomatic` do not supply default criteria. In particular, an axiomatic or constructive justification concerns a consequence or construction, not a universally higher assurance state than empirical support. A conjecture's origin in abduction likewise does not assign it `L0`.

Examine whether a demanded threshold or evidence requirement protects the relevant quantity well enough to justify its cost, delay and displaced work. Keep that judgement distinct from the conditions binding the action. A recommendation to amend a requirement does not change it or confer amendment authority.

For a one-off receiving use, stop with the sufficient qualified assurance result. Do not create a profile, fill unused level fields or explain the omission of a level solely to complete this pattern.

#### B.3.3:3.3 - Preserve scope and inspect the grounding

A claim about a design-time `MethodDescription` and one about performed `Work` or its `Trace` have different subjects. For an inference across composition scales, identify the relation the receiving claim uses. A condition established for every operating mode applies to a specified mode within that range. A rate for the whole constrains its parts to the extent their sizes and overlap permit. If passing and failing exhaust the outcomes on this criterion and at most two of 100 distinct readings failed, at least eight of any ten of those readings passed. Conversely, two groups of ten can each report nine passes yet share the same nine passing readings and have different failures. Their combined set then has nine passes among eleven readings. Establish the coverage and common conditions needed for the conclusion in the chosen direction.

State structural claims as readable Working-Model relations. When a publication choice or current requirement elects B.3.5's CT2R-LOG profile, follow its relation-specific grounding: structural parthood uses the applicable C.13 `sum` or `slice` construction trace; collection belonging uses the collection's `set` trace. These elected branches declare `validationMode=axiomatic`. Other permitted relation claims retain their applicable logical or empirical support. A level label alone does not elect this profile.

A grounding account and the author's `validationMode` are inputs to inspect. Neither creates the relation, makes an empirical premise true, nor decides its currentness. Assurance publications remain downstream of the Working-Model surface under E.14.

#### B.3.3:3.4 - Worked case: a useful empirical result and an irrelevant fresh test

A team is deciding whether a converter can be used for non-safety-critical measurements within a declared temperature and input range. In this example, the receiving task's justified tolerance is 2%. Calibration results covering that range, an adequate measurement-error account and applicable operating observations support error below that tolerance. The team can return “supported for this measurement use within the stated range,” with its limitations. A formal proof of unrelated program properties is unnecessary.

Now replace that basis with a newly passed boot test and a glossary mapping. These establish startup behaviour and the intended term correspondences, not measurement accuracy. The same requested measurement use remains unsupported. Neither fresh evidence nor one link of each required type repairs the missing performance basis.

If the recipient instead needs a mathematical invariant, inspect the proof under its assumptions. If the application introduces a protective function or a different operating range, reopen the affected assurance question under its threshold and evidence rules. The earlier limited result remains an account of what it supported.

To design a profile for later converter assignments, recover what each recipient uses the measurement to decide. An offset that stays the same in two readings cancels in their difference. The same offset can decide whether an absolute limit has been crossed. Develop criteria for the quantity being accepted and the operating conditions that could change its error. Applying the existing 2% criterion remains sufficient for the original assignment when its grounds still hold.

### B.3.3:4 - Conformance Checklist

A Target of Assurance (ToA) denotes the claim being assessed for the named use, not an undifferentiated score for its whole system.

- **CC-B3.3.1 (Relevant support):** A positive assurance conclusion MUST identify the relied-on claim and use and explain how the cited basis supports it. A `verifiedBy` or `validatedBy` link is insufficient.
- **CC-B3.3.2 (Needed correspondence):** Where differing terms or participants can change the argument, the assessor MUST resolve the load-bearing correspondence through the applicable bridge. Other judgements have no general term-mapping prerequisite.
- **CC-B3.3.3 (Qualified levels and thresholds):** An endorsed level MUST have an applicable profile and evidence meeting its criteria. Reporting a past assignment requires grounds for what the authority decided, including its scope. A commissioned profile explains how its criteria distinguish the intended decisions and what grounds justify the claims of ordering or coverage it makes. The target claim and receiving use determine which formal, empirical or constructive support is required.
- **CC-B3.3.4 (Bridge scope):** A required bridge MUST cover the differences on which the conclusion depends. It SHALL NOT demand mapping every mechanism term to FPF as the price of a sufficient ordinary judgement.
- **CC-B3.3.5 (Scope of support):** Design and performance claims MUST retain their subjects, evidence and conditions. An assurance conclusion transferred from a whole to a constituent, from constituents to a whole or from a design to an execution states what warrants that inference under the receiving conditions.
- **CC-B3.3.6 (CT2R-LOG grounding):** When B.3.5's profile is elected, the structural and collection branches MUST retain their distinct current construction traces and declared modes. A level assignment SHALL NOT replace the required grounding or impose the profile on unrelated claims.
- **CC-B3.3.7 (Downward-only dependence):** Assurance publications or records SHALL NOT impose vocabulary or layout back onto the Working-Model surface.

### B.3.3:5 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure in use | Repair |
| --- | --- | --- |
| Tested but referring to different things | Requirements and architecture use “Sensor” for different participants; the test concerns only one. | Resolve that correspondence and re-examine affected claims; more test links do not fix it. |
| Perfect blueprint, unsupported operation | A proof assumes conditions that the actual system has not been shown to meet. | Obtain or use the needed empirical and assumption evidence for the claim, or narrow the conclusion. |
| Maturity by receipt | A fresh smoke test and a term mapping receive a positive performance label. | Judge the support for the requested performance, not the receipt count or type combination. |
| Proof as an admission toll | Sufficient empirical support is rejected because an unrelated formal proof is absent. | Apply the receiving claim's evidence rules; retain formal proof obligations where their contribution is necessary. |

### B.3.3:6 - Consequences

Recipients can inspect which claim and use an assurance result supports, its grounds and its limits. Teams direct effort towards relevant gaps and can reuse evidence that covers the claim.

Comparability becomes profile-specific. Defining a useful shared profile takes judgement about consequences, criteria and evidence; routine uses avoid that overhead.

### B.3.3:7 - Rationale

A claim, argument and evidence have different functions. Assurance improves when a contribution closes a relevant gap under applicable assumptions. Counting evidence types or increasing formality cannot guarantee that improvement.

B.3 supplies this claim-and-use structure and its source account. [ISO/IEC/IEEE 15026-2:2022](https://www.iso.org/standard/80625.html) concerns the structure and maintenance of assurance cases. This pattern adapts maintained, inspectable support to a receiving use; its subtype distinction and optional level profiles are FPF choices, not a level ladder attributed to that standard. Reconsider a local profile when its evidence model, receiving decision or threshold basis changes.

### B.3.3:8 - Relations

- **B.3, A.10 and C.2.1:** define the assurance result, evidence-use references and target claim.
- **B.5.3 and B.3.5/C.13:** supply needed concept correspondence and the elected, relation-specific construction account.
- **C.2.1 and E.14:** keep the identified Working-Model claim distinct from its assurance publication. A.4 supplies a System design/operation comparison only when that is the claim being assured.
- **B.3.4 and C.27.TA:** qualify currentness by the relied-on use, conditions and temporal reference.
- **C.11 and C.19.2:** support the choice of worthwhile additional evidence when that decision is live.
- **B.4 and Part D:** may consume a qualified assurance result in their transition or decision rules; this pattern supplies neither an automatic evolution gate nor risk-acceptance authority.

### B.3.3:End
