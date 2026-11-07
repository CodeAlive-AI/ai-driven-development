## NOT.4 - Construct Transformations of Expressions That Preserve Their Use

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### NOT.4:1 - Problem frame

**Use this when** an expression is difficult to read, derive from or change, and you need a rule for turning it into a more useful expression without losing the consequence on which the work relies. Examples include naming a repeated construction, exposing a hidden intermediate step, regrouping a diagram, or replacing a long sequence by an expandable abbreviation.

Start with the reader operation that is difficult. Construct a proposed manipulation from the expression's formation and interpretation rules. State where the manipulation applies, explain what it preserves, then obtain and use a transformed expression. The result can instead be a located condition that prevents the proposed transformation.

The reader needs the notation's interpretation and the subject laws used in the manipulation. NOT.2 supplies grouping and reference rules; NOT.3 supplies interpretation and reading operations. Elementary arithmetic and ordered sequences suffice for the worked cases. More specialized laws can be supplied by a collaborator.

Apply an existing transformation directly when its rule and conditions already answer the question. Use this method when that rule must be constructed, extended or repaired. A change of notation calls for NOT.5's translation and recovery work. Constructing an effective interpreter or compiler calls for CMP.12. Choosing a different physical process or working method requires the corresponding subject methods as well as a way to express the change.

### NOT.4:2 - Problem

How can a notation provide useful transformations whose applicability and preserved consequences remain understandable when the expression or its context changes?

A visually simpler expression can hide a necessary distinction. Reusing a name can bind an occurrence that previously referred elsewhere; combining repeated signs can combine two actions that were meant to occur separately. A valid equality may hold only under a local assumption. Without those conditions, a transformation can preserve one displayed answer while changing the work it is supposed to support.

### NOT.4:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Easier use and retained distinctions | A compact or regular expression can discard information needed by another operation. |
| Local manipulation and surrounding context | Replacing a part must respect the names, connections and assumptions supplied by its surroundings. |
| One useful result and a reusable rule | A successful instance supports that instance; a rule for a family needs an argument covering that family. |
| More alternatives and search cost | Keeping several equivalent forms can enable a later move while increasing the work of finding and comparing them. |
| Meaning and execution | Equal mathematical values can come from computations or actions with different effects and costs. |

### NOT.4:4 - Solution

**Choose the use to preserve → construct the manipulation → establish its conditions → transform and read → challenge the changed condition → retain the useful rule or alternatives.**

#### NOT.4:4.1 - Choose the operation and the observations to preserve

Identify the expression, its interpretation and the next operation that should become easier. The aim may be to see a shared construction, carry out an inference, change one definition, or recover a particular step in a sequence. A shorter expression is useful only insofar as it helps such work.

State what must remain obtainable. A numeric value, a sequence of actions, the identity of a shared component and an explanation of intermediate steps are different demands. Retain the distinctions used by the actual question. If users need both a compact result and the derivation, keep the derivation available rather than assuming the result reconstructs it.

For a computation or action description, include the effects that matter: repeating a measurement twice can produce different inputs from reading one measurement twice. CMP.12 develops the corresponding execution-preservation question. A purely mathematical reading may require only equality of values under its stated interpretation.

#### NOT.4:4.2 - Build a rule from the structure causing the difficulty

Follow the difficult reading or edit and locate the expression structure responsible for it. Propose a manipulation using the available constructors and interpretation laws. For repeated subexpressions, try a named definition and references to it. For a long regular sequence, try an abbreviation with a defined expansion. To expose an inference, try expanding a definition or introducing an intermediate expression justified by a subject law.

Describe the matched form and its replacement, including which parts may vary. Preserve the surrounding expression and the connections through which it uses the replaced part. A diagram rule needs the relevant input and output places, not only similar-looking boxes. NOT.2 supplies those structural distinctions.

Introduce a name with a scope that reaches the intended occurrences. Choose a fresh name, or rename conflicting bound occurrences consistently, when the new scope would otherwise change an existing reference.

For a growing rule family, construct several candidates and reuse previously established laws. Automatic enumeration or an AI proposal can help generate candidates. Their source of generation does not establish their validity: connect each used rule to its interpretation or an already established derivation. The search and validation algorithms belong to the applicable computational methods; this method determines the notation operation they must realize.

#### NOT.4:4.3 - Establish where replacement preserves the needed consequence

Interpret the matched form and the replacement under the same allowed inputs and context. Follow the meaning of their parts and composition far enough to obtain the required agreement. Use a known law where its premises hold; derive the missing law when that is the unresolved mathematical contribution. MATH.17 and MATH.18 supply operations-on-operations and interpretation reasoning.

Check the conditions that the proposed rule actually uses. Freshness of a name matters for introducing a binding; defined division matters for cancellation; an ordered boundary matters for a diagram connection. For a rule such as `x/x -> 1` over real numbers, `x != 0` is necessary. A condition established inside one branch remains local to that branch.

When replacement may occur inside a larger expression, show that the relevant enclosing constructors respect the chosen agreement. If the rule preserves a final value but changes an intermediate observation used outside the replaced part, restrict the replacement or retain that observation. A local equality under one assumption is not permission to merge every occurrence of the same printed term.

For a single bounded use, a direct derivation can suffice. For every expression in a family, establish the corresponding general argument. A separating case can refute the proposed rule; agreement on a few examples cannot establish a universal law. Choose additional checking when uncertainty about the rule can change its permitted use.

#### NOT.4:4.4 - Construct and use the transformed expression

Match the rule to the selected expression, instantiate its varying parts and satisfy its side conditions. Replace only the matched part, reconnect it to its surroundings and read the resulting expression using the notation's rules. Obtain the answer or perform the edit that motivated the transformation.

Compare the actual work before and after. A named definition can remove repeated edits while adding reference-following. An expanded derivation can be longer while making a missing inference accessible. Preserve both forms when they serve different needed operations; NOT.6 develops their maintained correspondence.

If the new form loses information needed to continue, restore that information or narrow the claim to the uses it still supports. Retaining a link to a derivation or an expandable definition can be enough.

#### NOT.4:4.5 - Challenge the condition most likely to fail in reuse

Change a relevant binding, assumption, input class or intended observation. Repeat the affected transformation and reading, or explain why the rule no longer applies. Test the rule's boundary rather than adding an unrelated difficult example. Sections :5.1 and :5.3 show changed bindings and local assumptions.

If a transformation is to run automatically, give CMP.12 the admitted expression structures, matching and replacement rules, and observations to preserve. An algorithm for repeatedly applying rules also needs a search strategy and a stopping condition. The availability of several valid rewrites does not imply that applying them in arbitrary order terminates or finds the most useful form.

#### NOT.4:4.6 - Retain a useful rule or a useful set of forms

Keep the rule, the conditions that matter to its use and a recoverable reason for the preserved consequence. A short explanation beside a simple rule is enough when no larger account is needed. Reopen the affected rule when its interpretation, allowed context or required observation changes.

For one known operation, stop after a suitable transformed expression is obtained. When committing to one form repeatedly blocks other useful transformations, retain alternatives and defer the choice. Equality saturation is one computational way to represent many equivalent forms and select from them. It requires a suitable expression theory, valid rules, a selection criterion and resource limits.

Compare retained forms by the work they support, using NOT.1's comparison and NOT.7's redesign where needed.

### NOT.4:5 - Archetypal Grounding

#### NOT.4:5.1 - Name a repeated construction without capturing another input

A reader wants to see and change the repeated construction in `(x + 1) * (x + 1)`. The expression denotes ordinary integer arithmetic with a fixed input x. Introduce a local definition: `let v = x + 1 in v * v`. Here `let` gives v the value of its defining expression within the following body.

At x = 3 the original expression gives `4 * 4 = 16`; the new one first obtains v = 4 and then the same result. For any integer x, substitution of v's definition recovers the original expression, establishing the general equality under this interpretation. To change the repeated construction to x + 2, change the one definition. The new value at x = 3 is 25, and expansion shows both occurrences received that change.

Now use a larger expression `u + (x + 1) * (x + 1)` with external inputs u = 10 and x = 3. Introducing `let u = x + 1 in u + u * u` is wrong: it turns the external u into a local reference and produces 20 instead of 26. A fresh v gives `let v = x + 1 in u + v * v`, which produces 26. The repair changes the binding choice, not the arithmetic law.

The rule applies to the pure arithmetic interpretation supplied here. If each occurrence instead instructs a fresh observation, sharing their results changes the operation. For example, two sensor reads may return 4 and 5, whose product is 20; one read returning 4 reused twice gives 16. Retain two observations unless their consolidation is justified for the intended use.

#### NOT.4:5.2 - Compress a sequence while preserving its order

A notation describes ordered cues A and B. The sequence `A; B; A; B` is to be shortened without changing the order of cues. Define `repeat 2 { E }` to expand into two copies of the entire finite sequence E, preserving its order. Then:

```text
A; B; A; B  ->  repeat 2 { A; B }
```

Expansion returns A, B, A, B. The third cue remains A. A reader changing B in every repeated unit can now change it once in the repeated body. If only the final B must change to C, expand or separate that occurrence: `A; B; A; C`. The earlier abbreviation no longer expresses the intended two identical units.

The tempting form `repeat 2 { A }; repeat 2 { B }` expands to A, A, B, B. It preserves counts but changes the third cue to B. Counts are insufficient for the selected ordered reading. No rule for exchanging cues was supplied.

This notation states cue order. If intervals, accents or bodily actions distinguish the repetitions, retain those distinctions in E or choose a different abbreviation. The order-preservation result alone supplies no claim about those further observations.

#### NOT.4:5.3 - Keep a cancellation inside the condition that permits it

For real x, consider `if x != 0 then x/x else 0`. Only the selected branch is evaluated. Within the first branch, division is defined and the quotient is 1, so the expression can become `if x != 0 then 1 else 0`.

At x = 2 both expressions return 1; at x = 0 both return 0 without evaluating the quotient. More generally, the two branches cover all real inputs and give the same result in each. Replacing the whole expression by 1 would fail at zero. Replacing an unrelated occurrence of x/x outside that guarded branch would also need its own domain condition. The useful transformation follows the local assumption through its scope.

#### NOT.4:5.4 - Reconnect an ordered pair after removing two swaps

A diagram carries an ordered pair of integer values on two wires: port 1 carries a and port 2 carries b. A swap exchanges the two values. Its output is (b, a); a second swap restores (a, b). Replace the two swaps by straight connections preserving port numbers. This argument holds for every integer pair.

The enclosing operation subtracts port 2 from port 1. In compact diagram notation:

```text
(1:a, 2:b) -> swap -> swap -> subtract(1, 2)
(1:a, 2:b) -> straight     -> subtract(1, 2)
```

Both forms return a - b. The replacement makes the source of each subtraction input directly traceable. If the replacement's outgoing wires are accidentally crossed, the enclosing operation instead receives (b, a) and returns b - a. Inputs (5, 2) then give -3 instead of 3; inputs (2, 5) give 3 instead of -3. Retaining two ports without retaining their correspondence loses the required use.

The diagram describes pure value operations, and the enclosing operation consumes only the ordered pair. That interpretation justifies this replacement in its context. Physical wire length or signal delay would be additional observations requiring a different preservation argument.

### NOT.4:6 - Bias-Annotation

A familiar algebraic identity can be applied under a different interpretation without notice. Integer or real arithmetic, finite machine arithmetic and effectful actions can admit different replacements. Recover the interpretation that the actual expression uses before transferring a rule.

The preference for a short final expression can hide the operation a learner or collaborator needs to recover. Retain an expandable or explanatory form when it enables that work. Conversely, keep a fluent compact form when repeated expansion only adds effort to an already understood operation.

### NOT.4:7 - Conformance Checklist

When the proposed transformation needs checking, examine the questions that bear on its intended use.

- Is the reading or edit to improve stated, together with the consequence to preserve?
- Can the matched structure, replacement and their connection to the surrounding expression be recovered?
- Do references, local assumptions and side conditions remain valid at each place where the rule is used?
- Does the preservation argument cover the stated family, or is the conclusion limited to the instances examined?
- Has a transformed expression actually supported the intended reading or change?
- Does the nearby failing case reveal the condition that blocks an invalid reuse?
- Can the work stop with this result, or does a stated further use justify retaining or searching additional forms?

### NOT.4:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Choosing a fresh-looking spelling without checking its scope | Check the existing references. The u-to-v repair in :5.1 preserves the external input. |
| Sharing repeated signs that denote distinct actions | Retain the distinct executions or observations unless their consolidation preserves the needed behavior. |
| Keeping counts while changing order | Expand the sequence rule and inspect the ordered result; :5.2 separates these observations. |
| Promoting a branch-local equality to a global rule | Carry the assumption to each permitted use, as in guarded cancellation. |
| Treating one equality check as a rule for every context | Establish the context-sensitive argument, or keep the conclusion at the checked scope. |
| Applying transformations indefinitely because each is valid | Choose the needed form or use a bounded search with a stopping and selection rule. |

### NOT.4:9 - Consequences

The notation gains a usable way to derive, expose or change expressions. A reader can apply the rule, recognize a failed condition and preserve a useful earlier form when the new one supports different work.

Constructing the rule costs interpretation and sometimes a mathematical argument. More forms can improve choice while making reading, search and maintenance harder. Preserving one consequence leaves other observations to their own conditions; widening use can therefore require retaining additional structure.

### NOT.4:10 - Architectural Rationale

Transformation rules are operations on expressions with an interpretation. Their useful content includes both the replacement and the conditions under which it preserves the relevant consequence.

Mathematical construction and computational realization supply different contributions. MATH.17 and MATH.18 establish laws for the transformed operations and interpretations; CMP.12 makes a translation or evaluator effective. The present method constructs a notation-level manipulation for an intended reading or edit. It can be used manually, in an editor or in an automated transformation without identifying those implementations with one another.

The retained observation determines the strength of the rule. Identifying expressions by the same value can discard a derivation, evaluation order or history that another use needs. Selecting that equivalence and respecting it in surrounding constructions makes the limitation explicit. A richer needed result calls for a richer interpretation or another retained form.

### NOT.4:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Piedeleu and Zanasi, [An Introduction to String Diagrams for Computer Scientists](https://arxiv.org/abs/2305.08768), §§2 and 6.1 | Adopt rewriting relative to declared structural laws and matching that respects the expression's boundaries. Their graphical rewriting constructions concern specified categorical structures; an arbitrary diagram does not inherit those equations. |
| Willsey and colleagues, [egg: Fast and Extensible Equality Saturation](https://arxiv.org/abs/2004.03082), POPL 2021, §§2.2, 4 and 5 | Use the distinction between committing to one rewrite and retaining equivalent forms for later selection. Conditional rules and binding analysis show why syntax matching alone can be insufficient. An e-graph relies on supplied valid equations; its compact storage does not establish those equations or guarantee affordable saturation. |
| Hou, Laddad and Hellerstein, [Towards Relational Contextual Equality Saturation](https://arxiv.org/abs/2507.11897), 2025 work in progress, §§1–3 | Retain the distinction between context-local and general equality in :4.3. The proposed contextual reasoning still has implementation and cost questions; it supplies no completed general engine here. The guarded-division case derives a permitted local replacement from its own stated arithmetic conditions. |
| Pal and colleagues, [Equality saturation theory exploration à la carte](https://arxiv.org/abs/2609.14527), 2026 extended preprint, §6.3.1 and §8 | Rule generation can combine guided search and LLM proposals with separate validity checks and derivability from prior rules. The study remains domain-specific; its discussion leaves conditional rule inference partly open. Do not infer a sound general rewrite system from plausible generated rules. |

**Choice of method.** Prefer a directed, justified manipulation when one known operation needs a better expression. An automated search that retains many forms becomes useful when early commitment repeatedly prevents later improvements and the expression theory admits such search. Equality saturation addresses that alternative. Its cost and supplied validity conditions still matter; the current [egglog scheduling tutorial](https://egraphs-good.github.io/egglog-tutorial/04-scheduling.html) shows why deriving a needed condition before expanding alternatives can avoid wasted work. Reopen the choice when the number of interacting rules or repeated uses makes the small direct route inadequate.

The source contributions are combined here with notation requirements and reader operations. The worked arithmetic, cue and guarded-division cases demonstrate distinct conditions of that synthesis.

### NOT.4:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1 | Supplies the operation to improve and the comparison of work enabled and displaced. |
| NOT.2/.3 | Supply expression structure, binding, interpretation and reading operations. |
| MATH.17/.18 | Construct operations on operations and establish the interpretation or composition laws used by a transformation. |
| CMP.12 | Constructs an effective interpreter or translation and relates source and target execution where automation is needed. |
| C.2.8 | Characterizes what a prepared reader can recover from the transformed expression; a formal equality alone does not establish reader accessibility. |
| NOT.5/.6 | Develop translation between schemes and coordination of retained complementary representations. |
| NOT.7/.8 | Develop reader-operation redesign and temporal or embodied notation where those are the affected demands. |

### NOT.4:End
