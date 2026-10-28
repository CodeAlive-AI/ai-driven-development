## B.3.5 - Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)
> **Status:** Stable
> **Type:** Pattern

**At a glance.** Use B.3.5 when a human-facing structural relation or a collection's own belongs-to relation has been selected for an additional assurance account without exposing constructive machinery as the public vocabulary.

**Use this when.** Use this assurance profile only when a publication choice or named current requirement elects it for a direct relation claim. State the readable relation first. After election, structural parthood and collection belonging follow separate trace and `validationMode` obligations. The trace reports the relation facts and their grounds for inspection.

**What goes wrong if missed.** The readable relation and its assurance account collapse: authors either lose usable relation sentences, treat collection belonging as parthood, prohibit separately grounded parthood by label, or make a trace look like the cause of the claim.

**What this buys.** Working-Model relations stay readable, while an elected assurance branch supplies the right inspectable account without changing the direct relation kind.

**Not this pattern when.** Not this pattern when a direct relation claim is sufficient and no publication choice or current requirement elects this assurance profile. Also not this pattern when the current question is how to construct the trace (`C.13`), which mereology relation kind is intended (`A.14`), whether a whole must be reidentified (`B.2`), or whether a candidate name deserves durable U-kindhood (`E.24.UK`).

> **One‑line summary.**
> CT2R-LOG keeps **ComponentOf**, ordinary belongs-to sentences, **PortionOf**, and **AspectOf** readable while respecting their different relation kinds. When this assurance profile is elected, structural parthood uses its applicable construction account; collection belonging uses a current `C.13 set` trace. The direct relation pattern supplies the conditions for each relation, including any separately claimed parthood.

### B.3.5:1 - Intent

*Keep **Working-Model** relations readable and, when this profile is elected, connect each covered assertion to inspectable grounding and a declared validation posture.*

**What you get (manager/engineer view).**
 The same relations you already know (e.g., **ComponentOf**) remain the **public relation vocabulary**.

**What changes when the profile is elected (auditor/ontologist view).**
* Each covered published edge carries two additional commitments:

  1. **`tv:groundedBy`** → points to the support required by the relation's branch: the applicable `sum` or `slice` trace for structural parthood, one current `C.13 set` trace for the collection's belongs-to relation, or an admissible argument or evidence object for another permitted claim.
  2. **`validationMode ∈ {axiomatic, inferential, postulate}`** → declares how the author justifies the assertion.

The pattern that defines the relation still decides when it obtains. CT2R-LOG records the branch-specific support link and declared assurance posture. An optional `tv:AliasOf` declaration resolves a local relation label to its accepted Tech designation under E.10 and Lang-CHR.

### B.3.5:2 - Problem Frame

B.3.5 exists where a readable Working-Model relation must remain usable by practitioners while assurance readers still need a grounding relation and declared validation stance. The pattern governs how a public relation claim connects to the support required by its selected assurance use.

### B.3.5:3 - Problem

Working-Model relations such as **ComponentOf** and an ordinary belongs-to sentence are easy to use but not self-justifying. Their declarations alone do not show which participants and occurrences obtain, which rule defines the relation, or what identifies the whole or collection. Conversely, exposing construction traces everywhere makes the graph unreadable to non-specialists.

**We need**: a stable **public relation layer** for relations and, where this profile is elected, a required, **reconstructible** **grounding channel** plus a visible **validation intent** that downstream assurance can reason about. The direct relation layer does not depend on electing the profile.

### B.3.5:3.1 - Forces

* **Readable claims and inspectable support.** Practitioners need stable relation meanings; assurance readers need the direct facts and identity conditions supporting each claim.
* **Parsimony constraint.** The Kernel stays minimal; construction is **outside** the Kernel.
* **Unification inside FPF.** We already unify external vocabularies; the same discipline is applied **internally** so patterns that publish structural claims can reuse one three-form construction-account discipline and one readable relation façade without making that account a second ontology.

### B.3.5:4 - Solution (thumbnail)

CT2R-LOG distinguishes an optional link between relation designations from the grounding link and validation flag required for each covered assertion:

1. **Alias link (lexical).**
   **`tv:AliasOf`** may link a local relation designation to the accepted Tech designation of the same relation in that use. The definition in :5 fixes both endpoints and the conditions for using this alternative label. Cite the direct relation pattern to recover the relation’s meaning.

2. **Grounding link (assurance level).**
   Each relation assertion covered by this elected profile carries `tv:groundedBy` according to its direct relation kind:

   * **ComponentOf, PortionOf, or AspectOf** requires one current C.2.1 construction-trace episteme in the applicable `sum` or `slice` form and `validationMode=axiomatic`. PortionOf uses the measured-portion profile in `C.13:4.1.1`; AspectOf uses the facet profile. This requirement follows the asserted relation, including measured text portions, and does not make those two profiles interchangeable.
   * **Collection belonging under the collection's own rule** requires one current C.2.1 `C.13 set` trace and `validationMode=axiomatic`. The trace reports the collection, the entity, the already established relation, the rule for belonging, and the identity conditions. It does not make the entity a constructive part, make belonging obtain, or prove that separately grounded parthood is impossible.
   * **Other epistemic or constitutive edges** use the support appropriate to their claim: an admissible evidence object for `postulate`, a followable argument for `inferential`, or a qualifying C.13 construction account for `axiomatic`. Constructive grounding is optional in this branch; select the mode from the basis actually used for this assertion.

3. **Validation flag (author intent).**
   Every relation or aggregation rule covered by this profile carries `tv:validationMode` with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence with a followable argument; or
   * **`axiomatic`** — one inspectable construction account is the declared assurance basis.

The applicable branch above selects the allowed modes and grounding targets. The mode declares the author's justification posture; B.3.3 judges what that support establishes for the receiving use.

> **Relation, grounding, and assurance.**
> **Published relation claim:** `:PumpA ut:ComponentOf :Skid12`. Assess its expression properties under C.2.3 when that assessment matters to the use.
> **Grounding account:** the assertion links to `:trace_Γm_sum_456`, a C.2.1 episteme about the direct construction facts.
> **Assurance posture:** `tv:validationMode=axiomatic` is the author's declaration. B.3.3 assesses the actual grounding for the receiving claim and use; a level is published only through an applicable justified profile. The declaration does not alter formality or establish empirical adequacy.

#### B.3.5:4.1 - Structural CT2R Typing-Grounding Unfolding Structure Block

When a constructive trace, working-model relation, and target kind or logical representation must be carried together across contexts, use this block or cite an equivalent `A.22.CGUS` specialization. The block is useful when the reader must see the passage from constructional material to a typed or logical claim without treating a readable relation label as proof.

```text
StructuralCT2RTypingGroundingUnfoldingStructureBlock:
  unfoldingStructureRef: exact independently selected A.22 structure, when needed
  workingModelOrConstructiveRepresentationRef:
  targetKindOrLogicalRepresentationRef:
  bridgeRef?:
  constructiveTraceRef?:
  preservedStructure:
  lostOrCollapsedStructure:
  CL_or_CLk?:
  admissibleReuse:
  blockedSubstitution:
  evidenceOrProofLinkageRef?:
```

`unfoldingStructureRef` names an independently selected A.22 structure; this block is a record describing its use. Recover the exact constituents, obtaining relations, applied constraints and named selection/use frame. `StructuralCT2RTypingGroundingUnfoldingStructure` is a local designator for the selected structure used to inspect this construction-to-typed/logical projection. Any A.22.CGUS qualification is tested separately under its potential-continuation rule; a local name or record does not establish it. C.13 supplies constructive-trace content and C.3 the kind intent, extent and subkind content actually used.

When an inadequate working account requires general diagnostic recovery of the exact subject construction, use `A.7.1`. That return may stop at a direct relation, system-role assignment, state or capability, Work occurrence, holon recognition, or the pattern for another subject without opening this structural CT2R specialization.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` is required when this use actually claims or consumes an obtaining semantic Bridge under F.9 or a kind correspondence under C.3.3. `CL_or_CLk` is required when the consumed assurance/calibration account requires that value. Entity, scheme, plane or notation changes alone establish no crossing; a same-sense unit conversion requires neither invented endpoints nor a Bridge. CL does not by itself authorize use. `preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries. Evidence linkage remains with B.3 evidence and assurance subject patterns; proof linkage remains with the proof or mathematical subject pattern that is current. The unfolding block only makes the structure of the passage inspectable.

### B.3.5:5 - Vocabulary & notation (normative)

* **Working-Model relations (front‑stage).**
 `ut:ComponentOf`, `ut:PortionOf`, and `ut:AspectOf` are publication-grade part relations under their direct A.14 rules. A collection uses the belongs-to predicate defined by the pattern for that collection; FPF has no public generic `ut:MemberOf` relation. Belonging is not a sub-property of `ut:PartOf`, `ut:StructPartOf`, or `ut:EpiPartOf`, but the same entities may separately stand in a constructive part relation when its own rule and all six A.1 matters pass.

* **Alias declaration (lexical).**
  `a tv:AliasOf t` states that local designation **a** denotes the same direct relation as accepted Tech designation **t** in the stated use. Both endpoints are designations. Identify the source or practice, effective scheme and local meaning under E.10:6.2.1; preserve the relation’s applicability and the roles and order of its participants. The direction points from the local expression to the Tech designation used to recover its meaning. Cite the defining passage, such as A.14 for `ComponentOf`, as the semantic source.

  A glossary sentence can make this declaration once for its stated use. An already clear Tech designation needs no additional alias. Apply F.17/F.18 when the naming task actually requires their records; an alias alone creates no need for a NameCard or SchemeSenseCell. E.10 separately governs the use of a Plain twin.

  To use an alias, recover the declared meaning and participant positions, then apply the direct relation’s rule to the assertion. Recheck the declaration when its meaning or use changes. A broader meaning, or an expression that reverses participant positions, needs its own account: for example, `hasComponent(whole, part)` expresses the inverse of `ComponentOf(part, whole)`. A bare alias declaration does not specify that reversal. When distinct local meanings require an actual semantic correspondence, use F.9; matching words alone leave that correspondence unresolved.

* **Grounding (per‑edge).**
 When this profile is elected for structural parthood, `tv:groundedBy` points to the applicable current C.2.1 construction trace and `validationMode=axiomatic`. When elected for collection belonging, it points to one current `C.13 set` trace under the collection's own rule and also uses `validationMode=axiomatic`. Other epistemic or constitutive claims may use a logical argument or evidence object under their permitted mode. Every target lets a reviewer inspect the assertion's basis.

* **Trace family.**
  `Γ_m.sum`, `Γ_m.set`, and `Γ_m.slice` are the C.13 forms used by the covered branches. `sum` and `slice` report structural-parthood constructions; `set` reports an already grounded collection and the belongs-to occurrences established under its own rule. Temporal and workflow claims retain their own patterns.

* **Validation flag.**
 `tv:validationMode ∈ {postulate, inferential, axiomatic}` is required on every claim covered by this elected profile. Structural parthood and collection belonging use `axiomatic` with their branch-specific current trace. A direct relation outside the profile has no B.3.5 field obligation.

### B.3.5:6 - Archetypal Grounding - Running example

> **Story.** A refinery team publishes `:PumpA ut:ComponentOf :Skid12`.

**Optional local wording.** The team’s glossary uses “assembly component of” for A.14 `ComponentOf`, with the component first and its containing whole second. It can state “In this assembly glossary, ‘assembly component of’ is an alias of `ut:ComponentOf` as defined in A.14.” This one declaration lets readers recover the relation intended by “PumpA is an assembly component of Skid12.” Whether PumpA actually satisfies that rule is examined in the account below.

Suppose a later inventory glossary widens that phrase to include uninstalled spares reserved for a skid. The earlier alias no longer covers the widened meaning. Keep the assembly meaning explicit or use the inventory’s separately defined reservation relation. PumpA’s existing component claim can remain valid while it stays installed; the label change alone supplies no new assertion about a reserved spare.

* **Publication — Working-Model relation layer.**
  They publish one assertion using the **Working-Model** relation **ComponentOf**, with exact named participants and the relation interpreted under its declared semantics. Those are its relevant expression properties under C.2.3; a universal F rank is unnecessary. The public view presents the Working-Model relation; a reviewer can follow its grounding link.

* **Constructive grounding (Γₘ).**
  In the background, the published assertion links to `:trace_Γₘ_sum_456`, a C.2.1 episteme that names the exact pump and skid, the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain, the applicable skid assembly rule, and the skid reidentification rule. An auditor replays that account to inspect the assertion's basis. The same listed parts under a different assembly can form another whole, while a permitted pump replacement can preserve Skid12; the direct relations and reidentification rule, not the trace or input list, decide.

* **Assurance stance & R-lane.**
Because the assertion is linked to the construction account required by its elected branch, authors set `tv:validationMode=axiomatic`. The account makes the relation's basis inspectable. B.3.3 considers the actual grounding and its currentness for the receiving claim and use.

* **Contrast (epistemic).**
When the same team asserts `:MassFlowRepresentation RepresentationOf :FlowModel`, they declare `validationMode=postulate` and attach a calibration dataset instead of a Γₘ trace. Judge that empirical basis for the claimed representation and receiving use; the declared mode alone does not establish lower confidence. Under B.3.4, a changed configuration, calibration qualification or other relevant premise can reopen the claim. The dataset's age alone does not defeat still-applicable support.

Result: **one** visible relation for engineers, a grounding reference and a validation-mode declaration for reviewers.

**Collection case — Fleet North.** First publish the ordinary sentence: “Vehicle 12 belongs to Fleet North under its registration rule.” Under that rule, the occurrence begins when Fleet North accepts the vehicle's registration, ends on withdrawal or transfer, and a later accepted registration begins another occurrence. If no current publication choice or requirement elects this profile, the direct sentence is sufficient and the author stops.

Here the fleet publication elects the profile. It links the assertion to one current C.13 `Γ_m.set` trace that names Fleet North and its identity rule, Vehicle 12, the obtaining registration occurrence, the registration rule, and its ending and recurrence conditions; it declares `validationMode=axiomatic`. If a vehicle enters or leaves the fleet, or the rule changes, the earlier trace remains an account of its earlier state but is not current support for the later assertion. The register and trace report this registration history. Any separately claimed ComponentOf relation needs its own grounds.

**Epistemic constituent case.** A proof of “the product of consecutive integers is even” uses the lemma “one of the two integers is even.” Inspection of that proof establishes `Lemma A ConstituentOf Proof P`. With no elected B.3.5 profile, the relation can be stated directly. A recipient may still require access to the proof under its own evidence requirement.

If that recipient elects B.3.5 and the basis is the followable argument, link the assertion through `tv:groundedBy` to that argument and choose `inferential`. If a qualifying C.13 account instead explains the proof's independently established constituent relations and assembly, it can supply an `axiomatic` basis. A later proof that omits the lemma requires a fresh content-part judgement; the earlier support remains about Proof P. Select and assess the support for the claim actually being used.

### B.3.5:7 - Author Standard (at a glance)

When you add or import a relation edge:

1. **Pick a Working-Model relation sentence** such as “Impeller ComponentOf Pump” or “Vehicle 12 belongs to Fleet North under its registration rule”; avoid raw `ut:PartOf` unless you are drafting meta-level axioms. If no current publication choice or requirement elects CT2R-LOG, publish that direct claim and stop.

2. **When CT2R-LOG is elected, attach `tv:groundedBy`**:

   * Structural parthood → the applicable current construction trace and `validationMode=axiomatic`.
   * Collection belonging under the collection's own rule → one current `C.13 set` trace and `validationMode=axiomatic`.
   * Another permitted epistemic or constitutive claim → the evidence object, argument or qualifying C.13 account actually used, with its corresponding mode from :4.
3. **Declare the selected `tv:validationMode`** for every covered claim.


> The public graph retains its relation vocabulary. For each assertion covered by the profile, a reviewer can follow the grounding reference to its construction or evidence account.

### B.3.5:8 - Compatibility & cross‑references

* **B.3 and the direct proof or mathematical pattern.** CT2R-LOG makes the relied-on construction or support account inspectable; B.3 judges its contribution to the current assurance claim. State the actual logic and proof basis when a formal conclusion is used.
* **B.3.3 (Assurance subtypes and levels).** The declared `validationMode` and actual `tv:groundedBy` account contribute only what they establish for the receiving assurance claim. They do not compute a universal L0–L2 progression; a published level requires an applicable justified profile.
* **B.3.4 (Evidence ageing and currentness).** A relation assertion, its construction-trace episteme, and the warrants or evidence used for it retain their own editions and currentness. `validationMode=axiomatic` does not freeze a trace or make described world-side facts timeless; changed participants, relations, rules, or identity conditions require direct reinspection.

### B.3.5:9 - Rule‑set — CT2R‑LOG (conceptual, human‑first)

**Intent (one line).** Publish readable Working-Model relation claims, resolve a useful alternative designation through an optional alias, and supply the assurance account required for assertions covered by an elected B.3.5 profile or named current requirement.

#### B.3.5:9.1 - Vocabulary and meanings in this pattern

* **Working-Model relation.** A human-oriented direct relation statement using a public name such as `ut:ComponentOf`, `ut:PortionOf`, or `ut:AspectOf`, or an ordinary sentence such as “this edition belongs to this product series.” It is the canonical public layer for readers; the direct pattern keeps the relation meaning fixed.

* **Assurance Layer.** Within the branch requirements, an author may combine these grounding contributions:

  * **Constructive** grounding: an inspectable account in one of the three C.13 forms (`Γ_m.sum | Γ_m.set | Γ_m.slice`). It names independently grounded participants, direct relation occurrences, the applicable construction rule, and identity or reidentification conditions. No formal notation is required, and the account does not create the relation it reports.
  * **Logical** grounding: a *reasoned* chain (think KD‑CAL style arguments) that shows why the relation follows from stated premises.
  * **Mapping** grounding: support for interpreting a relation designation or for a claimed correspondence between meanings. E.10/F.18 govern a same-meaning alias; F.9 governs a required correspondence between distinct local meanings.
    These contributions can be combined. Mapping supports interpretation or cross-context use; the assertion still needs the construction account, argument or evidence required by its branch in :4.

* **Empirical Validation.** Observations and calibration results support claims about the relation under the applicable conditions. Assess their contribution under B.3.

* **Grounding vocabulary (`tv:`).**

  * `tv:AliasOf` — links a local relation designation to the accepted Tech designation of that same relation under :5.
  * `tv:groundedBy` — links the covered assertion to the **author’s grounding account** required by its branch in :4. Interpretation or correspondence support may accompany that account; it cannot replace the branch’s required basis for the asserted relation. When a construction trace is recorded, it is a C.2.1 episteme with its own edition and currentness.
    The `tv:` namespace is part of the Core conceptual lexicon; it is **notation‑agnostic** and **tool‑agnostic**.

* **`tv:validationMode ∈ {postulate, inferential, axiomatic}`.** A **declaration by the author** of the *justification posture* for a relation instance:
  *postulate* — a pragmatic working claim;
  *inferential* — a reasoned consequence;
  *axiomatic* — the author declares that a constructive account is the assurance basis for this assertion. Assess that account under the relation's conditions and its receiving use.

> Use these terms consistently across notations; their meanings do not depend on one notation or execution environment.

#### B.3.5:9.2 - Normative rules (MUST/SHALL clauses for thinking‑and‑writing)

**S‑1 (Working-Model first).**
Authors **SHALL** state each covered direct relation claim in Working-Model form. Assurance accounts remain below that public layer. Electing this profile adds branch-specific trace and mode obligations; it is not a precondition for direct use.

**S‑2 (Alias declaration).**
When an alternative relation designation helps readers and carries the same meaning, the author **SHOULD** declare its `tv:AliasOf` link to the accepted Tech designation under :5. State the local use and cite the defining passage so readers can recover the intended relation. A direct claim using an already clear Tech designation needs no alias.

**S‑3 (Grounding by mode).**
For every relation instance covered by an elected B.3.5 profile, the author **MUST** set `validationMode` and follow the corresponding grounding stance:

* **S‑3.a `postulate`.** For a branch that permits it, state the working scope, link `tv:groundedBy` to an admissible evidence object, and give the empirical cues that would challenge the claim. No construction trace is required by this mode.

* **S‑3.b `inferential`.** For a branch that permits it, link `tv:groundedBy` to a short reasoned chain from admitted statements that a peer can follow.

* **S‑3.c `axiomatic`.** The author links the assertion to the current C.2.1 trace episteme required by its branch. A competent peer can recover the exact participants, direct relation occurrence, applicable rule, and identity or reidentification conditions. The account makes those facts inspectable.

* **S‑3.d Structural parthood.** A covered `ComponentOf`, `PortionOf`, or `AspectOf` assertion requires `validationMode=axiomatic` and the applicable current C.13 construction account; `postulate` is not available.

* **S‑3.e Collection belonging.** A covered belongs-to assertion uses the rule defined for that collection and requires `validationMode=axiomatic` and one current C.13 `set` trace. The trace reports already established belonging and collection identity. A logical argument or evidence object may support the inclusion decision separately, but neither substitutes for the elected set trace, turns belonging into parthood, or prohibits a separately grounded part claim.

**S-4 (Relation-kind sense-making).**
* For structural `ComponentOf`, `PortionOf`, and `AspectOf` claims, the elected profile requires the applicable current construction account and `validationMode=axiomatic`.

* For collection belonging, the elected profile requires one current `C.13 set` trace and `validationMode=axiomatic`. The collection's own rule still decides whether the occurrence obtains.

* For other epistemic or constitutive links, constructive grounding remains optional and the branch may prefer inferential or postulate reasoning with empirical cues.

**S‑5 (Order and time do not establish parthood).**
Execution order, parallelism or interval inclusion alone **SHALL NOT** establish a part-whole relation. State Method composition under B.1.5 and temporal facts under C.27; use B.1.4 when those recovered relations must be aggregated. Independently established A.15.1 Work-part relations and A.14 proper-phase relations for unchanged non-Work carriers remain admissible under their own rules.

**S‑6 (Unidirectional dependence).**
CT2R‑LOG may *consume* Compose‑CAL and KD‑CAL conceptually; it **SHALL NOT** redefine them. Meaning flows **downward only** (Kernel → Extension → Context → Instance).

**S‑7 (Register discipline).**
When naming relations in an alias declaration, authors **SHOULD** use the accepted Tech designation and, where available and permitted by E.10, its Plain twin. Obey the minimal-generality and rewrite rules (LEX-BUNDLE). Keep the declared local meaning and use recoverable when comparing labels across contexts.

**S‑8 (No tool talk).**
Core prose **MUST NOT** introduce CI/CD terms, file formats, APIs, or machine‑oriented notations in place of concepts. If examples are needed, they **MAY** be plain‑language narratives or domain vignettes.

#### B.3.5:9.3 - Scope & Non‑Goals (to keep the plane clean)

* **In scope.**
  Canonical publication of relations for humans; clarity of relation designations and their semantic sources; conceptual grounding stories; author‑declared *validationMode*; separation of structure vs order/time.

* **Out of scope.**
  Any machinery that *executes* checks; any binding to specific notations; any process/workflow mechanics; any discussion of file formats. (Those belong to tooling publications, pedagogy publications, and companion records; they SHALL NOT be imported by the Conceptual Core.)

* **Edge placements.**
  Choose the contribution for the question: resolve a same-meaning alias under E.10/F.18; use **Mapping** under F.9 for a required correspondence between distinct local meanings; use **Logical** grounding for an inference from premises and **Constructive** grounding for an account of a whole from its parts. Combine contributions when needed, retaining the claim support required by the elected branch, including its structural-parthood or collection-belonging trace.

#### B.3.5:9.4 - Author’s working moves (micro‑playbook, notation‑free)

**M‑1.** State the relation in **Working‑Model** form (e.g., “Impeller `ComponentOf` Pump”).
**M‑2.** If a publication choice or named current requirement elects this profile, pick `validationMode`; otherwise keep the direct relation claim and stop:

* For a permitted exploratory claim, choose **postulate**, link its empirical support, and state scope plus challenge cues.
* For a permitted conclusion from known statements, choose **inferential** and link the short argument.
* For structural parthood covered by the profile, choose **axiomatic** and link the applicable current construction account.
* For collection belonging covered by the profile, choose **axiomatic** and link one current `C.13 set` trace that reports the already established relation under the collection's own rule.
* For another permitted epistemic or constitutive claim whose chosen basis is a qualifying C.13 account, choose **axiomatic** and link that account.

**M‑3.** When an alternative designation helps readers, link that designation through `tv:AliasOf` to the accepted Tech designation of the same relation. State its local use and cite the definition; apply :5 when the meaning or participant order differs.
**M‑4.** If assembly uses two parallel lines, state the actual Method/Work and temporal facts. Add any independently obtaining part relation under its own rule; parallelism alone does not establish it.
**M‑5.** Stop when the selected readable relation and remaining non-use boundary are clear and, if this profile is elected, its validation mode and required current support are recoverable without guessing.

### B.3.5:10 - Bias-Annotation (auditable, human-first)

| Bias (name)                     | Symptom in the model                                                                                                          | Cognitive counter‑move (conceptual only)                                                                                                                                                                          | Where to check                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture** | A trace, constructor expression, or `validationMode` is treated as the source of the direct relation or whole identity. | Recover the exact participants, direct relation occurrences, construction rule, and identity or reidentification rule first. Treat the trace as a current C.2.1 account and the mode as the author's assurance posture. | CC‑CT2R‑1, CC‑CT2R‑2, CC‑CT2R‑3; C.13 trace separation. |
| **Canonical inversion** | B.3.5 fields are demanded before direct use, or one assurance branch is imposed on every relation. | Use the direct claim first. After election, use the applicable branch: structural parthood or collection belonging takes its required axiomatic trace; other permitted claims may use inferential or postulate support. | CC-CT2R-2, CC-CT2R-3, CC-CT2R-5. |
| **Order/time leakage** | Inferring parthood from sequence, parallelism or interval inclusion alone. | Recover the independent part relation under A.15.1 or A.14 when it obtains, and keep Method/order/time claims separate. | B.1.5, C.27 and B.1.4; A.15.1 or A.14 for the exact part/phase claim. |
| **Notation lock‑in**            | Letting a diagram or syntax define the meaning (“it’s true because the diagram says so”).                                     | Enforce **Notational Independence**: meaning is defined in prose/maths; renderings are illustrative only.                                                                                                         | Part E guard‑rail on notational independence.                        |
| **Unexamined mapping fit** | A composed claim relies on a mapping without inspecting preserved and lost distinctions. | State the exact mapping, its applicability and loss. Use a numeric reliability consequence only when the receiving model establishes its meaning and calculation; ordinal CL alone is insufficient. | B.3 and the direct mapping or representation pattern. |
| **Collection/composition swap** | A belongs-to predicate is used as `PartOf`, or a part claim is used as collection belonging, and reliability is carried over as if both were one construction. | State collection belonging and constructive parthood separately under A.14. When both obtain, keep both claims and their different `set` and `sum` accounts. | A.14 and C.13. |
| **DesignRunTag chimera**          | Mixing design‑time and run‑time evidence into one “assurance” line.                                                           | Split the **scope** of the claim: `S ∈ {design, run}`; compare side‑by‑side rather than merging.                                                                                                                  | B.3:4.8 and its “Design/run chimera” anti-pattern. |

### B.3.5:11 - Conformance Checklist (normative, author-facing)

| ID                                              | Requirement                                                                                                                                                                                                                                   | Purpose                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **CC-CT2R-1 (Canonical-first).**                | A relation published for readers **SHALL** be stated in Working-Model terms, such as `ut:ComponentOf` or an ordinary belongs-to sentence, as the canonical form; any constructive or logical justification is recorded as **grounding** (not as the definition).                                         | Preserve human-first canon and didactic primacy.                          |
| **CC‑CT2R‑2 (Mode declaration).**               | For every relation or rule covered by an elected B.3.5 profile, the author **SHALL** declare `tv:validationMode ∈ {postulate, inferential, axiomatic}` in prose. A direct relation outside the profile needs no B.3.5 mode. | Make elected assurance intent explicit without taxing ordinary direct use. |
| **CC‑CT2R‑3 (Structural axiomatic grounding).** | A covered structural parthood assertion uses `validationMode=axiomatic` and links to its applicable current C.2.1 `sum` or `slice` construction trace. The account reports independently grounded participants, occurrences, rule, and identity conditions. | Make elected structural assurance inspectable without turning it into a truth-maker. |
| **CC‑CT2R‑4 (No parthood from order/time alone).** | Authors **SHALL NOT** infer parthood from sequence, parallelism or temporal slicing alone. Any Work-part or proper-phase claim satisfies A.15.1 or A.14 independently; Method order and temporal relations use their direct patterns. | Preserve distinct relation meanings while allowing independently established temporal parts. |
| **CC‑CT2R‑5 (Collection vs part).** | Authors keep collection belonging under the collection's own rule distinct from every `PartOf` branch. A direct claim needs no profile fields; after B.3.5 election it uses `validationMode=axiomatic` and one current `C.13 set` trace. If constructive parthood also obtains, state and support that claim separately. | Prevent category errors without taxing ordinary belongs-to prose or prohibiting a stronger independently grounded claim. |
| **CC‑CT2R‑5a (Set trace reports).** | The elected set trace names the collection, the entity said to belong, the already established occurrence, the collection's own belongs-to rule, and the identity conditions. The set trace supplies no structural-composition reliability. | Keeps optional assurance from becoming ontology. |
| **CC‑CT2R‑6 (Fit is explicit).** | Where a claim relies on a mapping or alignment, the author **SHALL** state its actual applicability, preserved/lost distinctions and consequence for this claim. Any quantitative reliability adjustment needs a justified receiving model, compatible Scale and calculation; a CL label alone supplies none. | Keep integration limits inspectable without invented reliability arithmetic. |
| **CC‑CT2R‑7 (Notational independence).**        | Core meaning **MUST NOT** hinge on any specific diagram or syntax; illustrative renderings, if present, are labelled *informative*.                                                                                                           | Ensure longevity and cross‑discipline portability.                        |
| **CC‑CT2R‑8 (Layer direction).**                | Grounding flows **downwards** from Working‑Model to Assurance layers (Mapping/Logical/Constructive). Authors **SHALL** avoid back‑defining the canonical relation by its Mapping, Logical, Constructive, or Empirical grounding.                                                  | Preserve unidirectional dependence of layers.                             |
| **CC‑CT2R‑9 (Scope split).**                    | When assurance is discussed, authors **SHALL** state the **typed claim** and **scope** `S ∈ {design, run}` and keep them distinct in reasoning.                                                                                               | Prevent DesignRunTag chimeras.                                              |

### B.3.5:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Trace as relation or truth-maker | A `Gamma_m` trace is treated as the public relation, as proof that the relation obtains, or as the source of whole identity. | Keep the Working-Model relation canonical; recover the direct relation facts and reidentification rule independently; attach the trace only as their inspectable C.2.1 account. |
| Unchecked relation label or mode | A familiar relation label or `axiomatic` flag is published as though either settled relation obtaining or identity. | State and test the direct relation first. When B.3.5 is elected, add the branch-specific mode and support account. Stop when a fact required by the direct pattern is missing. |
| Order/time leakage | Sequence, phase labels or parallel timing are treated as sufficient evidence of parthood. | Recover each direct relation separately: A.15.1 for Work parts, A.14 for a proper phase of an unchanged non-Work carrier, and B.1.4 for aggregation of recovered order or temporal relations. |
| Assurance by notation | A diagram, graph display, or data format is treated as if it made the relation true. | Use the diagram, graph display, or data format to present the relation claim; keep the grounding relation and validation mode explicit. |

### B.3.5:13 - Consequences (benefits, trade-offs, mitigations)

**Benefits**

* **Cognitive clarity for authors and readers.** Working-Model relations remain canonical while assurance accounts stay beneath them. Every claim covered by the elected profile carries only its branch-specific support account; ordinary direct claims remain lightweight. CT2R preserves an inspectable assurance account while keeping collection belonging, constructive parthood, and order or temporal relations distinct. Order and time may organize a structure without establishing parthood.
* **Use-specific assurance without tooling commitments.** Teams choose the grounding that the relation's elected branch and receiving claim require. The declared modes distinguish justification postures; they are not an ascending scale of empirical confidence.
* **Explicit fit management.** Inspect the mapping and its losses before relying on a composed claim. Its actual limitations can qualify, narrow or block that conclusion; a quantitative effect requires the declared receiving model.
* **Cleaner separation of concerns.** Distinguish collection belonging, parthood, Method composition and temporal relations by their direct rules. Their separate meanings can coexist in one inspected account without inferring one relation from another.

**Trade‑offs & mitigations**

* **Extra prose discipline.** Declaring `validationMode` and writing a short grounding narrative (when *axiomatic*) adds authoring effort. *Mitigation:* reuse local templates; keep narratives concise and Γ\_m‑oriented by idea rather than notation.
* **Insufficient grounding for the receiving use.** An empirical or logical account can omit a premise or fail to satisfy the elected branch. Use B.3.3 to identify that gap and the worthwhile repair; retain sufficient support without demanding a more formal mode merely for its label.
* **Inspecting mapping limits costs effort.** Recover the correspondence, align units where lawful, and verify the links needed by the claim. Retain a qualitative limitation when no justified numerical reliability model is available.

### B.3.5:14 - Rationale (informative)

**14.1 Why canonical‑first?**
CT2R-LOG treats the **human-readable, task-appropriate relation** (e.g., `ut:ComponentOf`) as the **canonical publication form** because that is what engineers and managers actually use to reason, decide, and communicate. The formal layers **ground** that form; they do not replace it. Authors state the relation readers need, then point to the support required by the selected assurance use.

**14.2 Why distinguish the two `tv:` links?**
`tv:AliasOf` connects designations so a reader can recover which relation an expression names. `tv:groundedBy` connects a covered assertion to the account supporting that assertion. An agreed glossary meaning can remain stable while a component is removed and the earlier construction account ceases to support the current claim. Conversely, a changed glossary can require a new interpretation while the physical assembly stays unchanged. Keeping these subjects distinct tells the author what to re-examine. Both links can be expressed in prose or another suitable notation.

**14.3 Why a triad of `validationMode`?**
The triad **{postulate, inferential, axiomatic}** distinguishes permitted justification postures, not stages of formality or increasing confidence. The direct relation kind and elected profile determine which posture and support are appropriate for the receiving claim and use. A sufficient calibration account in a branch permitting `postulate` needs no mode promotion; an elected structural-parthood or collection-belonging claim still requires its respective current construction trace. Where a load-bearing claim needs stronger proof or an empirical check, select that contribution for the assurance gap it can resolve, not to advance through the three labels. The mode declaration changes neither the canonical relation nor the strength of its support.

**14.4 Why recover parthood independently of order and time?**
Order and temporal coverage answer different questions from parthood. A chronology or diagram supplies no part relation by itself. A.15.1 can independently establish a Work temporal part, and A.14 a proper temporal phase of an unchanged non-Work carrier. Preserve those relations alongside the applicable Method and temporal claims; B.1.4 aggregates only the relations already recovered.

**14.5 Why point to `Γ_m.sum | set | slice` (Compose‑CAL) for constructive grounding?**
The three C.13 forms—**sum, set, slice**—are sufficient to report the recurring construction accounts for integrated assemblies, collections, aspects and measured portions without expanding the kernel. They are not identity functions. A truthful account carries exact participants, direct relation occurrences, the applicable rule, and identity or reidentification conditions: the same inputs under another assembly can form another whole, while a permitted replacement can preserve one whole.

**14.6 Why mental obligations rather than process mandates?**
These obligations govern how a relation claim is justified and published: declare a permitted mode for an elected profile, supply the branch's required support, and keep order and temporal claims distinct from parthood. A tool can help inspect that account; its successful execution does not replace the relation's grounds. The requirements concern the claim's justification, not attainment of an axiomatic strength level.

### B.3.5:14.7 - SoTA-Echoing

The assurance profile uses the following contributions. The W3C recommendations supply established semantic distinctions for the alias account; they do not define the FPF-specific predicate.

| Source line | Contribution and boundary | Application in B.3.5 |
| --- | --- | --- |
| A.14's current constructional comparison | **Adopt** construction and identity before relation choice. **Reject** both a universal collection-membership predicate and any inference from belonging either to parthood or to the impossibility of parthood. | `S-3.d/e`, `CC-CT2R-3/5/5a`, and the Fleet North case keep collection belonging and a separately grounded part claim distinct. |
| [ISO/IEC/IEEE 15026-2:2022, *Assurance case*](https://www.iso.org/standard/80625.html) | **Adapt** its separate, maintained assurance-case structure: an elected support account stays inspectable and current beside the claim it supports. **Reject** a mandatory full assurance case for every direct relation. The FPF-specific `validationMode` triad is only the author's declared posture; the standard is not cited as its source. | The Solution, `S-3`, B.3.4 currentness relation, and conformance rows require support only after profile election and keep claim, support, and posture separate. |
| NIST's [Digital Thread for Manufacturing](https://www.nist.gov/programs-projects/digital-thread-manufacturing) programme | **Adapt** traceable model-based information, validation, and conformance across engineering, manufacturing, and quality. **Reject** a shared model, thread, exchange, or passing syntax check as proof of a world-side relation. | `tv:groundedBy`, the trace-family rule, and the two worked cases keep the support account versioned and inspectable while the direct relation and its own rule decide what obtains; a trace or evidence item creates neither the relation nor its identity. |
| [SKOS / SKOS-XL (W3C, 2009)](https://www.w3.org/TR/skos-reference/#xl-label-relations) and [OWL 2 Direct Semantics (W3C, 2012)](https://www.w3.org/TR/owl2-direct-semantics/#Object_Property_Expression_Axioms) | **Adopt** the distinction between labels, relations between labels, and the relations they designate. OWL distinguishes equal property extensions from inverse properties with reversed participants. **Adapt** a directed local alias under E.10; neither a generic SKOS-XL label relation nor property equivalence supplies that declaration’s complete meaning. | :5 defines designation endpoints, local use and participant positions. The assembly-glossary case shows why changing the label’s meaning and changing the actual assembly require different reconsideration. |

At comparable correctness and currentness, always exposing the heavier account costs more to write and read, while a bare direct sentence cannot meet an elected assurance need. B.3.5 therefore starts with one readable relation and adds one branch-specific account only when the publication elects the profile. The cost is that the relation assertion and its support must be checked for currentness separately.

Reconsider the affected assertion when its member, rule, trace, or evidence changes. Use the applicable relation and assurance rules when their editions change.

### B.3.5:15 - Relations

**Builds on**
- **A.14 Advanced Mereology** — supplies direct structural relations and the discipline for collection belonging under each collection's own rule and separately grounded parthood; B.3.5 adds only the assurance branch elected for the relation.
- **A.11 Ontological Parsimony (C‑5)** — constructive grounding lives in a calculus; the kernel remains minimal.
- **B.1 Universal Γ** — shared invariants and the placement of order/time in their respective Γ‑flavours.
- **Part E authoring rules** — canonical pattern template and notational independence, which CT2R‑LOG explicitly follows.

**Coordinates with**
- **Compose-CAL (`Γ_m`) and `C.13`** — supply current construction accounts for structural parthood and the `set` account for elected assurance of collection belonging. Each trace reports facts whose meanings and conditions come from the pattern that defines the relation.
- **A.22.CGUS / StructuralCT2RTypingGroundingUnfoldingStructureBlock** — provides the local structural CT2R unfolding block when a constructive trace, working-model relation, target kind or logical representation, bridge, preserved structure, and loss must be inspected together; `A.7.1` is the pattern for general diagnostic return to a subject construction.
- **KD‑CAL** — provides the **logical** shoulder (inferential justification) when authors pick `validationMode = inferential`.
- **E.10 / Lang-CHR (F.18)** — govern relation designations, local aliases and register use; F.17 supplies naming records when needed.
- **Kind-CAL / F.9** — govern actual kind correspondences and correspondences between distinct local meanings. A same-meaning alias follows the naming rules above.

**Constrained by**
- **Notational Independence (E.5.2)** — CT2R‑LOG refuses to prescribe formats, keeping all obligations conceptual.

**Specialises / feeds**
- **B.3, B.3.3 and B.3.4** — supplies the publication discipline (Working-Model relations, declared **relation kind** and **validationMode**; **F** per C.2.3 where relevant) that B.3’s trust calculus expects; interacts with ageing and assurance-level assessments without changing the relations themselves.

**Non‑relations**
**No introduction of order/time** — CT2R‑LOG does **not** define `SerialStepOf` / `ParallelFactorOf` / temporal **phases**; use `B.1.5` for Method-order claims, `A.14` and `B.1.4` for same-carrier temporal phases and their aggregation, and `A.15.1` for Work parts and occurrences.

### B.3.5:End
