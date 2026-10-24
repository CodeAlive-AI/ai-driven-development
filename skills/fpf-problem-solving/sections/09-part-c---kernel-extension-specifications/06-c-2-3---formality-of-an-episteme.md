## C.2.3 - Formality of an Episteme

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Formality assessment.

**One-line summary.** Formality concerns how explicitly and precisely an episteme's content is expressed. Assess the properties needed for its use, including the interpretation of terms, constraints, operations and inferences. These properties form a declared profile when several matter together; they do not supply a universal rank of languages, logics or tools.

### C.2.3:1 - Problem frame

Use this when a reader, engineer or researcher must decide whether an expression is precise enough to interpret, compute with, combine or check, or what formalization would make that use possible. A research hypothesis, interface specification, controller model, decision policy and formal proof can all need this judgement, but they need different properties of expression.

The first useful move is to name the expression and the operation it must support. A reviewer may need unambiguous acceptance conditions; an interpreter needs an execution rule; a proof checker needs a statement and derivation in its admitted calculus. This assessment identifies the needed repair without requiring a more elaborate formalism for every task. Use an already sufficient expression directly. Readability alone is a different question; truth, empirical support, organizational approval and permission to act retain their own grounds.

### C.2.3:2 - Problem

“More formal” can hide several different changes. A document can acquire a clear structure without fixing its ambiguous terms. A precise specification can be non-executable. An executable program can omit the property its user needs established. A checked proof in one logic need not become stricter when translated into another logic. Ranking these changes on one ladder can reject adequate work and reward an irrelevant change of notation or tool.

Composition adds a further difficulty. Several precisely expressed claims can be connected by an informal inference. Their presence does not make that whole argument a formal derivation. Conversely, an informal observation used as empirical evidence does not make the separately stated mathematical claim less precisely expressed. Without an explicit assessed expression and support relation, “the least formal part” can refer to the wrong object.

The practical problem is therefore to establish which expression properties the receiving operation needs, which are present, which must change and how those properties survive combination or translation.

### C.2.3:3 - Forces

| Force | Tension |
| --- | --- |
| Readability and precision | Familiar prose can communicate efficiently; formal syntax and semantics can enable operations that prose does not define. |
| Shared comparison and different uses | Common property meanings permit comparison; different uses can require different combinations of them. |
| Exploration and assurance | An early conjecture can be useful before its interpretation or proof is complete; a stronger use needs the missing contribution. |
| Notation and meaning | Different calculi can express the same required property; they can also differ in assumptions, expressiveness and available proof techniques. |
| Constituent and whole | Formal constituents help only when their meanings and the connections required by the whole are also established. |
| Sufficient explanation and assessment burden | A short assessment can settle an ordinary use; repeated comparison or automation may need a declared characteristic basis. |

### C.2.3:4 - Solution - Assess the required properties of expression

Formality is assessed on a named expression of an episteme's content. Establish what its next use requires, recover the relevant interpretation and inferential relations, and inspect the actual expression against those requirements. Keep independent properties distinct. A shared profile makes their combination visible; a local summary is useful only when its declared criteria preserve the distinctions the receiving use needs.

#### C.2.3:4.1 - Subject and representation of the assessment

**F** names the formality assessment in an account that also uses G and R. It is not a globally ordered atomic `U.Characteristic`, and this pattern supplies no universal `U.Formality` value or `F0...F9` scale. The assessed subject is an exact claim, declaration, model or argument expressed by an episteme. State which parts and connecting inferences belong to that assessment.

An ordinary assessment can be a sentence: “The budget condition has declared units, a typed variable and an explicit predicate; no derivation of its adequacy for the project is supplied.” That is enough when it answers the receiving question. For comparison, automation or repeated use, describe the selected expression properties and their values as a profile. The description remains an episteme; a reference such as `formalityRef` points to that assessment and its basis. This introduces no new root U-kind.

If a `CharacteristicSpace` is used, each assessed Characteristic has its own declared Scale and slot under A.18 and A.19. A profile is not one Coordinate containing several unnamed characteristics. Record missing or unknown assessments separately from values; unknown precision is not evidence of low precision. Keep the relevant calculus, assumptions and interpretation recoverable alongside the property assessments.

#### C.2.3:4.2 - Place beside G and R

A named assurance argument may consume F alongside G or R under B.3. The notation `[F,G,R]` is a view of distinct assessments, not automatically a point in one numeric space.

- F concerns expression properties. G concerns applicability or claim scope.
- A derivation expressed in a calculus is part of the assessed content. Evidence that a particular checker accepted it supports that checking claim. Confidence in the checker, its assumptions and the resulting conclusion belongs to the relevant assurance argument.
- A fully expressed empirical claim can have weak or missing empirical support. Formal validity under stated premises and applicability to the world answer different questions.
- Mapping loss is assessed for the receiving use. Any effect on R needs its B.3/C.2.2 basis; an ordinal CL label supplies no automatic penalty.
- A notation, carrier or rendering change preserves the assessment only when it preserves the expression properties on which that assessment rests.

#### C.2.3:4.3 - Comparison and local ordered summaries

Compare profiles only after aligning the assessed properties, their meanings and relevant conditions. One expression can provide a formal predicate while another provides an executable procedure; neither fact alone makes one more formal for every use. A changed use may need both, or may need only one.

When an order is useful, declare its domain and comparison rule. For a fixed compatible basis of independently established requirements, an expression that satisfies all requirements satisfied by another and some additional ones can dominate it under that declared rule. This does not rank the entire languages or establish a preference for every use. Preserve incomparability when different requirements are satisfied; unresolved assessment is a separate result. Use A.19:5.1.3 for an order overlay when a CharacteristicSpace is involved.

A local ordinal summary is possible when its levels have nested criteria. For example, one team's specification-expression scale can require: named objects and stable terms; those conditions plus explicit acceptance predicates and their interpretation; those conditions plus expressed derivations for a specified set of obligations. The last level includes the earlier criteria by declaration. Its proof-checking evidence is still assessed separately. State the exact scale, mapping from the profile, domain and conditions before using its levels or a threshold. Another team's levels are not comparable merely because they use the same numbers.

Arithmetic, averages and numerical differences are not licensed by an ordinal scale. Where a change is described as an increase in formality, identify the strengthened property or the established order that makes that claim meaningful. A new logic, extra subsystem or larger toolchain is not such a property by itself.

#### C.2.3:4.4 - Requirements for a receiving use

Express a formality requirement through what the recipient needs to do. “The invariant has explicit types and semantics, and every inference needed for this proof is expressed in the selected calculus” is a recoverable condition. If checked validity is also required, name that separate evidence requirement. A local ordinal threshold can abbreviate the expression condition only when its named scale captures the required criteria.

Normative content must make the expression conditions needed for its intended use recoverable. A suitable ordinary explanation can do this without a separate score, profile document or formal proof. A richer assessment is required when a comparison, assurance argument or automated consumer actually relies on it. Neither a satisfactory formality assessment nor a threshold result grants permission to act.

Improving the expression changes the assessed content. Correcting an erroneous assessment can instead leave that content unchanged. When the receiving requirement changes, return to the property, formal apparatus, derivation or external support it actually needs; do not automatically raise every part of the expression.

#### C.2.3:4.5 - Assess and improve an expression

1. Identify the exact claim or argument and the next operation: interpretation, execution, combination or checking. Name the required result and any applicable binding requirement.
2. Recover the terms, domains, variable bindings, constraints, operation meanings and inferential connections needed for that operation. Section 13 supplies common distinctions, not a mandatory assessment form.
3. Inspect the expression. State which needed properties it provides and where interpretation, an operation or an inference remains unspecified. Keep a proposed derivation separate from the result of checking it.
4. Test the receiving condition. A sufficient expression ends this inquiry. If a missing property prevents the use, repair that part or obtain a suitable expression. Use C.19.2 to choose and configure formal apparatus when that is the actual question; use C.39 when a way to obtain the needed result still has to be developed.
5. After the change, repeat the affected use, including any connecting inference. Preserve unchanged scope and support assessments unless their own grounds changed. If the repaired expression reveals a different claim or assumption, assess that change explicitly rather than calling it a purely notational improvement.

### C.2.3:5 - Archetypal Grounding

**Tell.** Ask what the expression enables its recipient to interpret or do, and which property enables it.

**Show (System).** A controller requirement in controlled language can state a clear bound. Typed invariants make its variables and condition explicit. An executable model enables simulation. A formal derivation can establish an invariant under declared plant assumptions. These contributions can be connected, but execution is not a required intermediate stage for every proof, and a proof does not establish the plant assumptions empirically.

**Show (Episteme).** A research conjecture can gain stable terminology, explicit predicates and an expressed argument. Each change removes a particular obstacle to examination. A mathematical conjecture may remain non-executable and unproved while being fully precise about what is conjectured.

### C.2.3:6 - Bias-Annotation

The pattern favors recoverable expression properties over a universal prestige ranking. This makes a comparison more explicit but can be unnecessary for an already adequate ordinary use. Keep the assessment as small as that use permits. Do not replace one compulsory score with a compulsory inventory of every possible property.

### C.2.3:7 - Conformance Checklist

- `CC-F-1` An assessment relied on in use **SHALL** identify the assessed expression, selected properties and their grounds. Normative content **SHALL** make its necessary expression conditions recoverable; a universal F value is not required.
- `CC-F-2` A local ordinal summary **SHALL** declare its scale and mapping. Arithmetic over its levels is invalid unless a separately justified quantitative scale is established.
- `CC-F-3` A claim of greater formality **SHALL** name the strengthened property or declared order. It **SHALL NOT** imply greater truth, trust or scope by itself.
- `CC-F-4` Status, maturity or tool labels **MUST NOT** substitute for the assessment of expression properties.
- `CC-F-5` A local refinement or sublevel **SHALL** preserve its declared parent criteria; a cross-scale comparison requires an explicit meaning-preserving basis.
- `CC-F-6` A composite assessment **SHALL** cover the essential content and inferences of the named whole. It **SHALL NOT** inherit a property from constituents without the composition preserving that property.
- `CC-F-7` Implementations **MUST NOT** average unrelated formality properties or local ranks into an undeclared score.
- `CC-F-8` Changes in G, R or CL **SHALL NOT** change an expression assessment unless its own grounds change.
- `CC-F-9` Transport **SHALL** preserve a formality assessment only when its relied-on properties and interpretation are preserved. A receiving rewrite that changes claim content, EntityOfConcern or the effective reference scheme has its own episteme identity under C.2.1.
- `CC-F-10` Translation and bridge limitations **SHALL** remain explicit for the receiving use. Assess assurance effects under their governing models.
- `CC-F-11` Assigned properties **SHALL** be supported by the actual terms, predicates, semantics, derivations or other assessed content. A claimed checking result needs its own evidence.
- `CC-F-12` A named notation, prover, calculus or execution harness **SHALL NOT** by itself establish the required expression property or a successful check.
- `CC-F-13` Publication and approval status **MUST NOT** substitute for formality.
- `CC-F-14` A policy consuming formality **SHALL** state the required properties, or a justified threshold on a named local scale, and keep separate assurance and authority conditions explicit.
- `CC-F-15` Language-state facets **MUST NOT** be hidden inside a formality rank. Each actual Characteristic used in a space retains its own Scale and slot.

### C.2.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | Repair |
| --- | --- | --- |
| Status leakage | Approved content is assumed to have a precise interpretation. | Inspect the terms, conditions and inferences needed for the use. |
| Tool prestige | A prover or fashionable foundation is named in place of a demonstrated property. | Inspect the actual expression and the relevant checking evidence. |
| Appendix inflation | A formal annex is used to describe the whole argument as formally derived. | Assess the essential connecting inferences as well as the annex. |
| One ladder for different capabilities | Execution, hybrid modeling and higher-order proof receive successively higher ranks. | Separate their contributions and test the receiving requirement. |
| Profile as one Coordinate | Several characteristics are concealed inside one atomic F slot. | Declare the real slots or use an ordinary structured assessment. |
| Assessment replaces improvement | A larger scorecard is produced while a necessary predicate remains unstated. | Supply the missing expression and repeat its receiving use. |

### C.2.3:9 - Consequences

| Benefit | Trade-off and response |
| --- | --- |
| Adequate expressions remain usable across different formal traditions. | Comparison needs shared property meanings, not only matching numbers. |
| Formalization work targets the actual obstacle. | The recipient must state the operation and result that matter. |
| Composite arguments expose missing connections. | The assessment must include the relevant whole and its essential inferences. |
| Expression, scope and support remain distinct. | A concise assessment sometimes needs more than one sentence; it need not become a universal form. |

### C.2.3:10 - Rationale

Formality matters because an expression can make interpretations, operations and inferential commitments available for shared examination. The properties that enable these uses are related but not identical. A formal specification can define what is required without giving a procedure; a procedure can run without expressing a proof of the required property. A richer logic can express additional distinctions without improving an already sufficient statement of an ordinary invariant.

A profile preserves these relations without pretending that every pair has one overall order. Declared local chains remain economical when their criteria are genuinely nested. Comparison then rests on the receiving operation and preserved meaning. Composition follows the same reasoning: a whole must supply the connections its result depends on, while evidence about the world retains its separate role.

### C.2.3:11 - SoTA-Echoing

| Source and scope | Contribution used here | Limit of the transfer |
| --- | --- | --- |
| Kuhn (2014), [A Survey and Classification of Controlled Natural Languages](https://aclanthology.org/J14-1005/), §§3–3.2 and the qualification at the end of §3.4; established classification basis. | Precision, expressiveness, naturalness and simplicity answer different questions. Even the paper's ordered summaries are deliberate simplifications rather than an overall quality ranking. | PENS classifies languages. It does not directly rate an individual episteme, and its classes are not imported as F values. |
| ter Beek et al. (2024; volume edition 2025), [Formal Methods in Industry](https://doi.org/10.1145/3689374), §§1–2.2; contemporary account of industrial formal methods. | Formal specification, verification, execution and different verification techniques have distinct roles. Formal reasoning can apply to a non-executable specification; tool choice depends on the question and available support. | The discussion principally concerns computing systems. The profile and transdisciplinary receiving-use rule here are FPF's construction, not a scale claimed by that survey. |
| [Isabelle overview](https://isabelle.in.tum.de/overview.html), maintained tool documentation, including its HOL and LCF account. | A higher-order environment supplies formal statements and checked reasoning with substantial reusable libraries. | The availability of these capabilities does not establish that a particular submitted expression or proof has passed its required checks. |
| [The HoTT Book](https://homotopytypetheory.org/book/), authors' description of univalent foundations; foundational source. | Univalence and higher inductive types change what can be expressed and how mathematical reasoning is organized. | A different foundation is not a higher universal formality rank. Its relevance depends on the needed structures and admitted assumptions. |

These sources support distinctions among actual capabilities and formal bases. They do not establish a total order from prose through execution to successive schools of logic. Apply the assessment method above to the expression and use at hand; consult the sources when their particular language or apparatus is in question.

### C.2.3:12 - Relations

- **Uses:** A.18 and A.19 for declared Characteristics, Scales, profiles represented in spaces and any order overlay.
- **Coordinates with:** C.2 and C.2.2 for epistemic composition and assurance; B.3 when an assurance argument consumes the assessment.
- **Coordinates with:** C.2.LS, A.16 and C.2.4–C.2.7 for language-state properties that retain their own meanings.
- **Uses:** C.19.2 when selecting or configuring a formal apparatus is the missing practical contribution; C.39 when a way to obtain the result must be developed.
- **Coordinates with:** F.9 for a cross-context transfer whose mapping and limitations affect the receiving expression.

### C.2.3:13 - Distinctions for describing expression

The following descriptions identify common contributions. They are neither mutually exclusive classes nor consecutive levels. Select only distinctions needed by the receiving operation.

#### C.2.3:13.1 - Unstructured prose

Free natural language may leave vocabulary, assumptions and connections unstable. It can still preserve an observation or start an inquiry. Identify the ambiguity that obstructs the next use before requiring a more elaborate form.

#### C.2.3:13.2 - Scoped notes

A note can identify its topic and use terms consistently while leaving criteria informal. Naming the subject helps interpretation; it does not by itself formalize a predicate or narrow claim scope. Assess scope separately.

#### C.2.3:13.3 - Structured outline

A coherent section structure helps readers find claims and their grounds. Placeholder criteria can remain inside a complete outline. Editorial organization is useful, but inspect what the filled content actually defines.

#### C.2.3:13.4 - Controlled narrative

Constrained prose can stabilize interpretation and state acceptance or refusal conditions. This may be sufficient for a competent reader's decision. Automatic interpretation needs an additional mapping or semantics when the prose itself does not supply one.

#### C.2.3:13.5 - Explicit predicates and constraints

Typed entities, bound variables, units, domains and an interpretation make a predicate recoverable. The claim's consistency or consequence can then be examined under the declared semantics. A written formula with undefined symbols does not supply this contribution; an explicit predicate need not be executable or proved.

#### C.2.3:13.6 - Executable semantics

An expression can define how an interpreter or procedure produces results. Declare the relevant input meanings, operation and output interpretation. This enables a run under those conditions; it does not establish a separate invariant or substitute for its specification. A non-executable formal statement can remain sufficient for a mathematical argument.

#### C.2.3:13.7 - Coupled formalisms

A hybrid controller model can relate discrete transitions to continuous evolution; another account can connect several formal subsystems. State their shared meanings and interconnection obligations. Additional formalisms introduce relations to establish, not an automatic increase in rigor. Assess whether the whole preserves the properties its intended use needs.

#### C.2.3:13.8 - Formally expressed derivation

A derivation states how its conclusion follows from declared premises under an identified calculus. Inspect the essential inferential steps, including their connection to the stated conclusion. A checked derivation in higher-order logic can satisfy this need without translation into dependent type theory.

#### C.2.3:13.9 - Properties expressed in types and proof terms

A dependent type can express a property of a program or mathematical object; a term can carry a derivation of that property under the calculus. Recover the exact proposition, assumptions and term. Distinguish that expression from evidence that the required checker accepted it. Its usefulness may include preventing a particular invalid construction or connecting a program to its specification.

#### C.2.3:13.10 - Higher equalities and univalent foundations

When a question needs relationships among equalities or a particular treatment of equivalence, name those structures and the foundation used to express them. This can change the available construction or proof. It does not strengthen every unrelated invariant or make simpler formal foundations inadequate.

#### C.2.3:13.11 - Keeping the distinctions together

A useful assessment explains which of these contributions cooperate. A controlled requirement can be related to a formal invariant and an executable model, with a derivation connecting the model to the invariant. The links carry claims of their own. Check the required link when its meaning or assumptions change; do not infer the whole connection from the presence of all three documents.

### C.2.3:14 - Assessing formality in practice

#### C.2.3:14.1 - First-pass questions

1. Which claim, declaration or argument must be understood, executed, combined or checked?
2. Are its terms, domains and interpretation sufficient for that operation?
3. Are the required predicates, operations and inference steps actually expressed?
4. Which calculus and assumptions matter, and what checking result is available when required?
5. Would changing the expression property change the receiving result, or would it only add unused apparatus?

#### C.2.3:14.2 - Short assessment

A short assessment names the subject, required properties, observed basis and consequential gap. For example: “The interface condition gives typed inputs and outputs and an explicit postcondition. The procedure has executable semantics. The preservation of this postcondition across the retry branch is not expressed.” The next useful change is the missing retry argument, not the acquisition of a more elaborate specification language.

For repeated comparisons, use the same property meanings and conditions for every candidate. A compact profile can record them. Add a local rank only when its declared mapping preserves the distinctions used by the comparison.

#### C.2.3:14.3 - Typical improvements

- Replace unstable terms with explicit definitions and consistent references when interpretation is blocked.
- State a necessary acceptance condition as a predicate with its types, units and meaning when it must be evaluated or reasoned about.
- Supply operational semantics when the result must be computed.
- State the relations and obligations joining formal subsystems when the whole must be analysed.
- Express the missing derivation when the result depends on a conclusion from premises, then obtain the checking evidence required for that use.

These changes can occur independently or together. Describe the property changed; use a local rank difference only when the named scale gives it meaning.

### C.2.3:15 - Composition and interaction

#### C.2.3:15.1 - Essential-content and connection rule

Identify the assessed episteme's expressed claim or argument and its compositional support relation. A property of the whole requires the relevant properties of its essential content and of the inferences that connect it. A machine-checked annex does not make an informal connecting inference machine-checked. Listing common constituent properties is also insufficient when the composition can fail to preserve them.

External evidence has a different role. A typed claim supported by an informal observation can retain its explicit predicate and interpretation while its empirical warrant remains weak or unresolved under B.3. If the assessed subject is instead the whole argument, include its essential observation-to-conclusion inference in that assessment. Do not take a minimum over every external source in an evidence chain.

A minimum can abbreviate an upper bound on a local ordered scale only when all assessed parts use that scale and the composition rule establishes the bound, including the connection. A minimum alone does not prove that the whole meets that level; additional joining obligations may remain. Without that basis, inspect the needed properties directly.

#### C.2.3:15.2 - Relation to G

Formality concerns expression; G concerns applicability or claim scope. Making an assumption explicit can reveal that the claim applies less widely than expected. Record that scope correction separately from the improvement in expression. A precise claim can still have broad scope.

#### C.2.3:15.3 - Relation to R

An explicit expression can make a claim easier to test or its derivation easier to check. It does not create empirical support. A checked formal argument establishes its conclusion under the admitted premises and calculus; applying that conclusion to the world additionally needs the relevant interpretation and evidence. Assess freshness, corroboration and mapping limitations under their actual assurance models.

#### C.2.3:15.4 - Relation to CL and Bridges

A Bridge may expose loss or mismatch across contexts. Preserve that limitation for the receiving use. Reuse a formality assessment only if the properties and interpretation on which it relies survive the transfer. A receiving rewrite that changes claim content, EntityOfConcern or the effective reference scheme identifies a new episteme under C.2.1; assess the expression of that episteme. A changed carrier alone does not require a new assessment.

### C.2.3:16 - Worked examples

#### C.2.3:16.1 - Research hypothesis

A short note proposes a scaling law with stable terms and acceptance conditions in prose. That can be enough to decide which measurement to attempt. Writing the relation with explicit variables, units and parameter conditions enables a quantitative comparison. The expression becomes more determinate in those respects; the fit to observations remains a separate question. A poor fit is not repaired by making the same formula typographically more formal.

#### C.2.3:16.2 - Interface specification

An interface specification declares preconditions, postconditions and invariants with their types and interpretation. It can be used to compare designs before an implementation exists. A faithful executable reference model adds the ability to run scenarios. A running implementation that omits the postcondition does not dominate that specification: the two expressions supply different contributions. To claim conformance, connect the implementation behavior to the required postcondition and supply the needed argument or test.

#### C.2.3:16.3 - Safety controller

A controller and plant model express discrete transitions, continuous evolution and the obligations connecting them. A proof of an invariant in higher-order logic can satisfy a requirement for an explicitly derived invariant under those assumptions. A checked dependent-type development can satisfy the same requirement. Choose between adequate options by compatibility, available proofs and application cost through C.19.2; there is no general requirement to replace HOL with a supposedly higher foundation. If the plant-assumption evidence is weak, retain that limitation even when the derivation is fully checked.

#### C.2.3:16.4 - Decision policy

A policy says in controlled prose that a request exceeding a thirty-minute planned-duration ceiling fails the budget condition. To evaluate that condition automatically, introduce a Plan variable p, define plannedMinutes(p) in nonnegative real minutes and state `meetsBudget(p) iff plannedMinutes(p) <= 30`. The expression now gives the needed domain, unit and predicate. Its evaluation can answer the budget question; it supplies neither the other eligibility conditions nor permission to proceed.

If “duration” later means elapsed duration rather than planned duration, retaining the formula's printed shape is insufficient. The input interpretation and therefore the condition have changed. Return to the affected policy meaning and uses.

#### C.2.3:16.5 - Proof-bearing algorithm

An algorithm's dependent type states a length-preservation property, and its term expresses a derivation under the chosen type theory. Inspect the property and term, then recover the required checking result. A separate HOL proof of the same stated property may be equally sufficient for the recipient. If a new task instead requires reasoning about higher equalities or a specific univalent construction, it changes the apparatus requirement. That new requirement does not retrospectively make the earlier sufficient derivation less rigorous.

#### C.2.3:16.6 - Executable ML recipe

A training-and-evaluation recipe declares the inputs, parameters, operations and output interpretation needed to repeat a run. This supplies executable meaning. It does not express a proof of generalization merely because the harness is sophisticated. If the receiving use needs an empirical performance estimate, obtain the corresponding observations and inference. If it needs a formal property of the procedure, state and derive that property under a suitable model. The two continuations repair different gaps.

### C.2.3:17 - Guidance for developing and examining expressions

#### C.2.3:17.1 - For authors

Make the expression sufficient for its intended use. State a remaining ambiguity, unspecified operation or missing derivation when it changes what a reader can do. An early informal expression can be the appropriate result. Improve the property that blocks the next use, and preserve its connection to the original question.

#### C.2.3:17.2 - For reviewers

Read the assessed claim or argument and its actual expression. Check its terms, predicates, semantics and required inferences, including essential connections. Recover the basis for any claimed checking result. Keep missing expression, missing proof, weak empirical support and inadequate readability distinct, because they call for different repairs. A complete template or named tool answers none of those questions alone.

#### C.2.3:17.3 - For integrators and assurance leads

State the expression properties a receiving operation consumes. For a composition or transfer, establish their preservation through its actual connections. Reuse a declared local scale when it captures those needs; retain the underlying meaning when several participants use different scales. Apply separate scope, evidence, authority and language-state conditions where they matter.

### C.2.3:18 - Glossary and notation

- **Formality assessment (F).** An assessment of selected properties of an episteme's expression, with its subject, interpretation and basis recoverable.
- **Formality profile.** A structured account of those selected properties; when represented in a CharacteristicSpace, each actual Characteristic has its own declared slot.
- **Local ordered summary.** An explicit mapping from such assessments to a named ordinal scale whose levels have justified nested criteria.
- **Change in formality.** A change in an assessed property or in a justified order, not a numerical difference between unrelated labels.
- **Essential content and inference.** The content and connecting reasoning required by the assessed whole under its named composition relation; external warrant is assessed separately.
- **Example notation.** `F: explicit typed invariant; derivation not supplied`, or a threshold on a specifically declared local specification-expression scale.

### C.2.3:19 - Reusing an earlier assessment

#### C.2.3:19.1 - Recover the assessed meaning

An earlier label such as F4 or F8 is a locator for an assessment, not enough information to use it. Recover the actual expression, criteria and basis. Preserve useful properties already established, such as explicit predicates, executable semantics or a checked derivation. Do not infer a new profile or admissibility result from the number alone.

#### C.2.3:19.2 - Reuse a sufficient result

When the same expression properties and conditions still answer the receiving question, reuse the assessment. If an earlier requirement was written only as a rank, recover what operation and guarantee it was meant to protect before replacing it with explicit criteria or a justified local threshold. A binding requirement is changed through its governing authority; a revised vocabulary does not silently waive it. Reassess only the properties or dependent conclusions whose basis has changed.

#### C.2.3:19.3 - Boundary to language-state facets

This pattern does not redefine `U.ArticulationExplicitness`, `U.LanguageStateClosureDegree`, `U.LanguageStateAnchoringMode` or `U.LanguageStateRepresentationFactorBundle`. C.2.LS and its subordinate patterns govern those facets. A formality assessment can refer to their results when relevant, but must not relabel them as steps of one rigor scale.

### C.2.3:End
