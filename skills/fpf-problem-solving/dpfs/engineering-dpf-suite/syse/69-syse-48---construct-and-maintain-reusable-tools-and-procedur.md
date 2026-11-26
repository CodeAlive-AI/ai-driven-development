## SYSE.48 - Construct and Maintain Reusable Tools and Procedures

> **Type:** Method pattern
> **Status:** Stable

### SYSE.48:1 - Problem frame

**Use this when** repeated work or a missing operation may justify a reusable tool or procedural aid. Evidence from earlier attempts and the available operations can suggest a candidate. Establish whether the intended performer can already obtain a suitable aid and use it reliably.

The subject is the reusable operation or aid and its usable edition: a supported implementation or procedure, varying inputs, applicability, result, failure behavior and discovery. A paper worksheet can guide a person through an operation. A machine-readable table can supply the same distinctions to a service. In each case, identify which actions the aid performs and which the recipient must perform. The result can be a qualified aid available to the receiving task, a decision to retain direct work, or an account of what still prevents construction or qualification.

Keep direct work when it already suffices or costs less overall. Do not package an incident's accidental sequence simply because it succeeded once. A code file, a description of a skill and demonstrated ability to perform the task are different results.

### SYSE.48:2 - Problem

A harvested trace contains useful operations beside incidental constants, permissions and state. Replaying it can affect the wrong subject or silently reuse an obsolete assumption. Generated code can return without error while doing nothing useful. Even a correct operator contributes nothing when the next agent cannot discover it or recognize its applicability.

### SYSE.48:3 - Forces

Generality can reduce repeated work while concealing unsupported cases. More operators increase choice and maintenance cost. Consolidation can remove duplication or erase a useful distinction. An easy interface can hide preconditions that still matter. A convenient verification script can share the implementation's mistake.

### SYSE.48:4 - Solution

#### SYSE.48:4.1 - Recover the reusable contribution and compare direct work

Identify the receiving task family and the result it needs. Compare any available successful and failed attempts with those requirements. Identify the operation that could be reused and what can remain stable across inputs. A trace motivates that candidate; it does not qualify its reuse. F.0.2.MA reconciles or allocates already recovered contributions only when that separate receiving-description question is unsettled.

Separate the stable operation from values that vary by task and from incidental data that must not be retained. Recover input meaning, required state, permissions, output and effect semantics, and known defeating conditions. Use qualified domain definitions for the underlying operation and its acceptance criteria. If a needed operation, its meaning or its acceptance criterion is missing, use a qualified source or supplier to obtain it, or identify what prevents construction.

Compare construction, discovery, selection, execution, repair and maintenance with direct work. For platform work, SYSE.39 develops this comparison. Construct the aid when its expected contribution, at the anticipated frequency of use, justifies that total effort. A one-off operation may be better left as a qualified direct invocation.

#### SYSE.48:4.2 - Construct the implementation or packaged procedure

Parameterize values that legitimately vary: subject identity, measurements, units, source edition or applicable regime. Validate them against the actual operation rather than guessing from the example trace. Preserve state preconditions and uncertainty about prior effects.

Compose supported primitives, design the physical layout or packaged instructions, or generate a software candidate and inspect it. Check dependencies, hidden constants, access needs and failure paths. For a packaged procedure or worksheet, make the variable inputs, steps and completion conditions available in a form the assigned performer can use. Establish which means that performer will need to carry out the steps. A software operator can supply the missing operation while the model that invokes it stays fixed.

State accepted inputs, effects or supported actions, outputs, error returns and compatibility. Use SYSE.26/SYSE.27 for the software operator's supported interaction and recovery. Reject missing or unsupported inputs with a useful return. For an effectful operation, preserve attempt identity and recovery; do not turn a lost reply into an automatic replay.

#### SYSE.48:4.3 - Test meaning and effect beyond the harvested trace

Establish the property the receiver needs across its claimed range. A derivation over permitted inputs, a complete finite check or a domain observation can provide the grounds. New applicable inputs and cases that defeat an assumption help when they expose an unresolved dependency. Use the domain’s result criteria and independently justified expected values or observations. Check the returned result and obtain or use evidence for each effect the criteria require. If that evidence is unavailable, identify the unverified effect. A run can return normally with an incorrect value or no effect.

Challenge hard-coded incident values, unrealistic arguments, omitted permissions, stale source editions and suppressed exceptions where they can defeat the operation. A wrapper that catches every error can look successful while failing every task. A generated test that copies the implementation's mistaken formula supplies no independent arithmetic evidence.

Use SYSE.46 for reliance on the complete configured agent, including discovery, invocation and receiving use. When estimating performance on new cases from a sample, evaluate on cases kept outside construction and selection, with coverage suited to the intended use. An established input rule can settle a property for every input it covers. Use SYSE.49 where informative feedback is missing. Establish success from the required effect or evidence with known correspondence to it. A message emitted by the aid can merely announce completion.

#### SYSE.48:4.4 - Expose an edition that the next task can use

Supply the supported operator with a concise applicability entry, invocation example, required inputs, outcome interpretation and failure return. Use A.15.8.MS to make it reachable in the selected support configuration. Where the receiving procedure needs it, expose it in the working material or tool view through SYSE.52 and connect it to the relevant step through SYSE.47. Use SYSE.42 for the selected aid or invocation.

For a claim about receiving use, establish whether the performer found the operator, chose it under its conditions, supplied valid inputs and used the result in the receiving task. Use an adequate existing observation or observe a representative use. If a step failed, locate it as far as the observations allow. Poor discovery, mistaken selection, binding failure, bad arithmetic and ignored output require different repairs.

Retain source provenance and relevant failure evidence separately from the callable operation. An episode in SYSE.43 can explain an operator's origin without becoming its specification.

#### SYSE.48:4.5 - Revise and consolidate without erasing meaning

When assumptions, primitives or interfaces change, identify the affected edition and supported uses. A.3.1.MV distinguishes Method-semantic changes, implementation editions, variants and retirement. Apply that distinction before relabeling a changed operator as the same result.

Compare apparently overlapping operators on the same supported situations and defeating cases. Consolidate only when the combined implementation preserves their useful distinctions and improves total use. Keep a fallback where the shared implementation cannot preserve a required case.

Withdraw the affected uses of a callable edition when their required assumptions no longer hold. Withdraw the edition when it has no remaining supported use. Retain historical evidence and unaffected primitives; direct specialist help may remain available. Update discovery to the supported edition and its limits. Stop when the receiving question is settled by a qualified aid, continued direct work or withdrawal of an unsupported use. Otherwise identify the missing operation, meaning or evidence.

### SYSE.48:5 - Archetypal Grounding


#### SYSE.48:5.1 - Construct a column-and-carry worksheet


Repeated interrupted arithmetic loses the relation between carry digits and their receiving columns. The supplied operation is three-digit non-negative integer multiplication by one digit, with its ordinary correctness criterion. The engineer compares intact and failed attempts and recovers the needed aid: a fixed place-value layout with explicit positions for the input, multiplier, carry into the next column and result. Leave the digit and carry positions open for the values of each case. The first example uses 347 and 6.

Construct enough result space for four digits and keep the carry row visibly aligned with its receiving column. On 347 × 6, a person puts units result 2 and carry 4 into tens, then tens result 8 and carry 2 into hundreds, then 20 across thousands/hundreds: the report reads 2082. The paper preserves those place-value relations. The person performs the arithmetic.

The place-value rule explains why the layout works for every permitted input when followed. After each column, the low digits already written and the carry in the next column together equal the product of the multiplier and the input digits processed so far. At the next column, add the incoming carry to the digit product, write the units digit and carry the tens into the next column. This preserves the equality. The largest permitted product, 999 × 9 = 8991, fits four places. On 268 × 4 the column results are 32, 27 and 10, giving 1072. A shifted carry row breaks the correspondence between a carry and the column that consumes it. Check the layout used, and observe use when the question concerns a person's performance. An input outside the integer or width conditions needs a suitable layout or Method.

Compare preparation, use and maintenance with ordinary paper or direct calculation. Retain an already adequate sheet when a new template adds no value. A reusable worksheet can enter an existing procedure, and SYSE.47 can build a procedure from an already adequate worksheet. The resulting aid and its tested use are different from a person's acquired unaided ability.


#### SYSE.48:5.2 - Parameterize a technical calculation


An engineering agent repeatedly asks a specialist to normalize measurements and perform a calculation. One successful trace contains a customer's value and an implicit unit convention. The engineer and specialist recover the stable operation: validate units and applicability, normalize using the supplied conversion, calculate under the selected equation, and return the quantity with its conditions.

They parameterize measurements, unit metadata and equation edition. They exclude the old customer's values and guessed conventions. The specialist supplies the equation, allowed region and comparison results.

A candidate function combines verified conversion and calculation primitives. One metre and 100 centimetres must produce the same normalized input. A new applicable measurement tests the calculation beyond the original trace. An unknown unit and an out-of-region value must return the specified unsupported condition rather than reuse a plausible convention.

Test whether the next agent can find the function through its applicability entry, invoke it and use the result with its units and equation edition. If it cannot find the function, repair discovery; changing arithmetic would not fix that failure. If a later equation edition changes an assumption, withdraw or repair the affected variant. Unaffected conversion primitives and direct specialist calculation can still support the task.

To establish whether the proposed function saves effort, compare its cost in use, including selection and maintenance, with repeated direct work. Retain direct work when it costs less overall.


#### SYSE.48:5.3 - Recover an outcome lookup from interruption traces


Accepted-but-unresolved traces identify another candidate operation: take the original attempt identity, call its supported outcome query, and return the observed known, unknown or failed status. The engineer recovers and parameterizes that operation; use F.0.2.MA if the recovered contributions still need allocation. Keep the actual interface as the status source and retain its failure meaning.

A wrapper queried for A19 must use A19, not a harvested A17 constant. Exercise another identity and an unsupported lookup. A wrapper that silently repeats the mutation on an unknown return fails the at-most-one-effect condition. A.15.8.MS makes the qualified implementation and use conditions reachable, A.3.1.MV maintains its variant meaning, and the receiving procedure uses the result before considering another action.

### SYSE.48:6 - Bias-Annotation

Successful traces favor familiar cases and hide failures that never produced a reusable artifact. Generated tests can inherit the same mistaken convention. For the proposed extension, establish which property must carry over and what could break it. One counterexample can refute a general claim. A domain argument covering every admitted input can establish the property directly.

### SYSE.48:7 - Conformance Checklist

- The receiving use and reusable contribution are distinguished from incident data.
- Variable inputs and preserved preconditions have domain-grounded meaning.
- Implementation, dependencies, permissions and recovery are inspectable.
- Grounds for each result cover its proposed use. The author can identify a condition that would defeat the result or the argument showing why the allowed variations preserve it.
- The supported edition can be found by its intended user. A claim about its actual use identifies the receiving task and the evidence for that use.
- Semantic change, implementation revision and retirement remain distinguishable.
- Consolidation preserves useful variants, evidence and required fallback.

### SYSE.48:8 - Common Anti-Patterns and How to Avoid Them

**Publish the successful trace as a universal skill.** Recover what varies and which conditions made that attempt work.

**Verify only that no exception escaped.** Check the requested result and effects against an independent predicate.

**Merge functions with similar names.** Compare their actual supported situations, results and defeating conditions.

### SYSE.48:9 - Consequences

A recurring contribution can become obtainable with less repeated construction. The new operator adds discovery, compatibility and maintenance obligations. For later use or adaptation, keep the explanations and access to specialists that the intended participants need. Check their actual use when the conclusion depends on it.

### SYSE.48:10 - Architectural Rationale

An external operator is independently reusable across procedures, so its construction has a result distinct from memory retention, controller construction and parameter training. Keeping implementation, contract, Method meaning and observed capability separate makes revision and withdrawal precise.

### SYSE.48:11 - SoTA-Echoing

[SkillWeaver v1](https://arxiv.org/html/2504.07079v1) is a historical constructive anchor: practice traces yield reusable browser functions and tested invocation guidance. Its reported false verification and unrealistic-input problems motivate checking effects and feasible cases. For another domain, qualify the underlying operation and any service contract it depends on using evidence applicable there.

Retain trace-based parameterization and testing within supplied domain semantics. Compare direct work or a manually written operator on the same receiving use and total burden. Reopen qualification when source assumptions, interface behavior, supported inputs or actual receiving use changes.

### SYSE.48:12 - Relations

Use applicable domain operations and any available traces to develop a candidate when the frequency or consequence of its use justifies construction. F.0.2.MA reconciles or allocates already recovered contributions when needed; A.3.1.MV preserves semantic repertoire and edition distinctions; A.15.8.MS supplies discovery and usable guidance. SYSE.26/SYSE.27 govern the consumed software interface. SYSE.39 develops the burden comparison for platform work. Use SYSE.42 to invoke the operator and SYSE.47 to connect it to the receiving procedure. SYSE.43 retains relevant provenance; SYSE.49 supplies missing informative experience and SYSE.46 tests configured use. C.36.RP retains explanation and adaptation when continuity of practice is the concern.

### SYSE.48:End
