## SYSE.48 - Construct and Maintain Reusable Tools and Procedures

> **Type:** Method pattern
> **Status:** Stable

### SYSE.48:1 - Problem frame

**Use this when** repeated work or a missing operation may justify a reusable tool or procedural aid. Successful and failed attempts, together with supplied operations, suggest a candidate that a later person or technical agent cannot yet obtain and use reliably.

The subject is the reusable operation or aid and its usable edition: a supported implementation or procedure, varying inputs, applicability, result, failure behavior and discovery. A worksheet supports human execution; a program performs its implemented operation. The first result is a tested candidate available to a receiving task, or the construction or qualification gap.

Keep direct work when it already suffices or costs less overall. Do not package an incident's accidental sequence simply because it succeeded once. A code file, a description of a skill and demonstrated ability to perform the task are different results.

### SYSE.48:2 - Problem

A harvested trace contains useful operations beside incidental constants, permissions and state. Replaying it can affect the wrong subject or silently reuse an obsolete assumption. Generated code can return without error while doing nothing useful. Even a correct operator contributes nothing when the next agent cannot discover it or recognize its applicability.

### SYSE.48:3 - Forces

Generality can reduce repeated work while concealing unsupported cases. More operators increase choice and maintenance cost. Consolidation can remove duplication or erase a useful distinction. An easy interface can hide preconditions that still matter. A convenient verification script can share the implementation's mistake.

### SYSE.48:4 - Solution

#### SYSE.48:4.1 - Recover the reusable contribution and compare direct work

Identify the receiving task family and the result it needs. The engineer compares successful and failed traces with those requirements, recovers the useful operation and proposes what can remain stable across inputs. A trace motivates that candidate; it does not qualify its reuse. F.0.2.MA reconciles or allocates already recovered contributions only when that separate receiving-description question is unsettled.

Separate the stable operation from values that vary by task and from incidental data that must not be retained. Recover input meaning, required state, permissions, output and effect semantics, and known defeating conditions. Obtain missing primitive or acceptance meaning from the relevant domain owner.

Compare construction, discovery, selection, execution, repair and maintenance with direct work. For platform work, SYSE.39 develops this comparison. The expected frequency or consequence must justify the added artifact. A one-off operation may be better left as a qualified direct invocation.

#### SYSE.48:4.2 - Construct the implementation or packaged procedure

Parameterize values that legitimately vary: subject identity, measurements, units, source edition or applicable regime. Validate them against the actual operation rather than guessing from the example trace. Preserve state preconditions and uncertainty about prior effects.

Compose supported primitives, design the physical layout or packaged instructions, or generate a software candidate and inspect it. Check dependencies, hidden constants, access needs and failure paths. For a packaged procedure or worksheet, supply the varying positions, required human operations, available means and observable completion in a usable form. For a software operator, the model can remain fixed.

State accepted inputs, effects or supported actions, outputs, error returns and compatibility. Use SYSE.26/SYSE.27 for the software operator's supported interaction and recovery. Reject missing or unsupported inputs with a useful return. For an effectful operation, preserve attempt identity and recovery; do not turn a lost reply into an automatic replay.

#### SYSE.48:4.3 - Test meaning and effect beyond the harvested trace

Exercise a new applicable input and a case that defeats an assumption. Use the domain's result predicates and independently obtained expected values or observations. Verify the returned result and relevant effects, not merely the absence of an exception.

Challenge hard-coded incident values, unrealistic arguments, omitted permissions, stale source editions and suppressed exceptions where they can defeat the operation. A wrapper that catches every error can look successful while failing every task. A generated test that copies the implementation's mistaken formula supplies no independent arithmetic evidence.

Use SYSE.46 for reliance on the complete configured agent, including discovery, invocation and receiving use. Keep construction cases distinct from final comparison cases. If the environment cannot supply informative feedback, SYSE.49 constructs that contribution; the operator cannot certify its own success by printing a positive message.

#### SYSE.48:4.4 - Expose an edition that the next task can use

Supply the supported operator with a concise applicability entry, invocation example, required inputs, outcome interpretation and failure return. Make it reachable through A.15.8.MS's selected support configuration. Make it usable in SYSE.52's working material/tool view and SYSE.47's procedure; SYSE.42 applies the selected aid or invocation.

Observe at least one receiving use appropriate to the qualification sought: the agent finds the operator, chooses it under its conditions, supplies valid inputs and incorporates the result. Localize a miss. Poor discovery, mistaken selection, binding failure, bad arithmetic and ignored output require different repairs.

Retain source provenance and relevant failure evidence separately from the callable operation. An episode in SYSE.43 can explain an operator's origin without becoming its specification.

#### SYSE.48:4.5 - Revise and consolidate without erasing meaning

When assumptions, primitives or interfaces change, identify the affected edition and supported uses. A.3.1.MV distinguishes Method-semantic changes, implementation editions, variants and retirement. Apply that distinction before relabeling a changed operator as the same result.

Compare apparently overlapping operators on the same supported situations and defeating cases. Consolidate only when the combined implementation preserves their useful distinctions and improves total use. Keep a fallback where the shared implementation cannot preserve a required case.

Withdraw an affected callable edition when its assumptions are defeated. Retain historical evidence and unaffected primitives; direct specialist help may remain available. Update discovery to the supported edition and its limits. Stop at an obtainable, qualified candidate or return the missing primitive, meaning or evidence.

### SYSE.48:5 - Archetypal Grounding


#### SYSE.48:5.1 - Construct a column-and-carry worksheet


Repeated interrupted arithmetic loses the relation between carry digits and their receiving columns. The supplied operation is three-digit non-negative integer multiplication by one digit, with its ordinary correctness criterion. The engineer compares intact and failed attempts and recovers the needed aid: a fixed place-value layout with explicit positions for the input, multiplier, carry into the next column and result. The digits vary; 347, 6 and the particular carries are example values, not constants printed into the reusable operation.

Construct enough result space for four digits and keep the carry row visibly aligned with its receiving column. On 347 × 6, a person puts units result 2 and carry 4 into tens, then tens result 8 and carry 2 into hundreds, then 20 across thousands/hundreds: the report reads 2082. The paper preserves those relations; the person executes the supplied arithmetic.

Try a new input, 268 × 4. Units 8 × 4 = 32 gives 2 with carry 3; tens 6 × 4 + 3 = 27 gives 7 with carry 2; hundreds 2 × 4 + 2 = 10 gives the complete 1072. Check against independently obtained arithmetic, not a copied completed worksheet. A malformed template with carry positions shifted one column loses the needed relation and is rejected. An input outside the supplied integer/width conditions returns for a suitable layout or Method rather than truncating digits.

Compare preparation, use and maintenance with ordinary paper or direct calculation. Retain an already adequate sheet when a new template adds no value. A reusable worksheet can enter an existing procedure, and SYSE.47 can build a procedure from an already adequate worksheet. The resulting aid and its tested use are different from a person's acquired unaided ability.


#### SYSE.48:5.2 - Parameterize a technical calculation


An engineering agent repeatedly asks a specialist to normalize measurements and perform a calculation. One successful trace contains a customer's value and an implicit unit convention. The engineer and specialist recover the stable operation: validate units and applicability, normalize using the supplied conversion, calculate under the selected equation, and return the quantity with its conditions.

They parameterize measurements, unit metadata and equation edition. They exclude the old customer's values and guessed conventions. The specialist supplies the equation, allowed region and comparison results; the framework does not supply an engineering formula.

A candidate function combines verified conversion and calculation primitives. One metre and 100 centimetres must produce the same normalized input. A new applicable measurement tests the calculation beyond the original trace. An unknown unit and an out-of-region value must return the specified unsupported condition rather than reuse a plausible convention.

The next agent finds the function through its applicability entry, invokes it and uses the result with units and equation edition. If it cannot find the function, repair discovery; changing arithmetic would not fix that failure. If a later equation edition changes an assumption, withdraw or repair the affected variant. Unaffected conversion primitives and direct specialist calculation can still support the task.

This is a construction and qualification plan. If selection and maintenance cost exceed the repeated benefit, retain direct work.


#### SYSE.48:5.3 - Recover an outcome lookup from interruption traces


Accepted-but-unresolved traces identify another candidate operation: take the original attempt identity, call its supported outcome query, and return the observed known, unknown or failed status. The engineer recovers and parameterizes that operation; F.0.2.MA is unnecessary unless already recovered contributions need allocation. Keep the actual interface as the status source and retain its failure meaning.

A wrapper queried for A19 must use A19, not a harvested A17 constant. Exercise another identity and an unsupported lookup. A wrapper that silently repeats the mutation on an unknown return fails the at-most-one-effect condition. A.15.8.MS makes the qualified implementation and use conditions reachable, A.3.1.MV maintains its variant meaning, and the receiving procedure uses the result before considering another action.

### SYSE.48:6 - Bias-Annotation

Successful traces favor familiar cases and hide failures that never produced a reusable artifact. Generated tests can inherit the same mistaken convention. Include a new applicable case, a defeating case and an independent result basis before extending the operator's reach.

### SYSE.48:7 - Conformance Checklist

- The receiving use and reusable contribution are distinguished from incident data.
- Variable inputs and preserved preconditions have domain-grounded meaning.
- Implementation, dependencies, permissions and recovery are inspectable.
- New applicable and defeating cases test actual results and effects.
- The supported edition is discoverable and enters a receiving task.
- Semantic change, implementation revision and retirement remain distinguishable.
- Consolidation preserves useful variants, evidence and required fallback.

### SYSE.48:8 - Common Anti-Patterns and How to Avoid Them

**Publish the successful trace as a universal skill.** Recover what varies and which conditions made that attempt work.

**Verify only that no exception escaped.** Check the requested result and effects against an independent predicate.

**Merge functions with similar names.** Compare their actual supported situations, results and defeating conditions.

### SYSE.48:9 - Consequences

A recurring contribution can become obtainable with less repeated construction. The new operator adds discovery, compatibility and maintenance obligations. Technical reuse alone does not ensure that future participants understand, adapt or even use it; retain explanation and specialist return where those are needed.

### SYSE.48:10 - Architectural Rationale

An external operator is independently reusable across procedures, so its construction has a result distinct from memory retention, controller construction and parameter training. Keeping implementation, contract, Method meaning and observed capability separate makes revision and withdrawal precise.

### SYSE.48:11 - SoTA-Echoing

[SkillWeaver v1](https://arxiv.org/html/2504.07079v1) is a historical constructive anchor: practice traces yield reusable browser functions and tested invocation guidance. Its reported false verification and unrealistic-input problems motivate checking effects and feasible cases. That browser-function scope does not by itself qualify another domain's primitive or service contract.

Retain trace-based parameterization and testing within supplied domain semantics. Compare direct work or a manually written operator on the same receiving use and total burden. Reopen qualification when source assumptions, interface behavior, supported inputs or actual receiving use changes.

### SYSE.48:12 - Relations

The engineer performs trace-to-candidate recovery here. F.0.2.MA reconciles or allocates already recovered contributions when needed; A.3.1.MV preserves semantic repertoire and edition distinctions; A.15.8.MS supplies discovery and usable guidance. SYSE.26/SYSE.27 govern the consumed software interface. SYSE.39 develops the burden comparison for platform work. SYSE.42 executes, and SYSE.47 integrates the operator. SYSE.43 retains relevant provenance; SYSE.49 supplies missing informative experience and SYSE.46 tests configured use. C.36.RP retains explanation and adaptation when continuity of practice is the concern.

### SYSE.48:End
