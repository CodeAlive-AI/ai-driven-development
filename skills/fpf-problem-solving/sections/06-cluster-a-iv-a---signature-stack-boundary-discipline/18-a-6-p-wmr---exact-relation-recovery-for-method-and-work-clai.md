## A.6.P.WMR - Exact Relation Recovery for Method and Work Claims

> **Plain label:** recover the exact relation hidden by input, result, and handoff wording
> **Type:** Architectural precision-restoration pattern (A)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Specializes:** `A.6.P` Relational Precision Restoration

### A.6.P.WMR:1 - Problem Frame

**Use this when.** Practitioners **SHOULD** use this pattern after `A.6.P` generic relation recovery has isolated one current method-or-work boundary claim and the exact entity is already in view, but words such as `input`, `raw material`, `source data`, `source material`, `output`, `result`, `outcome`, `deliverable`, or `handoff` still do not reveal the direct relation that makes the sentence true. They **SHOULD** also use it when method, intended-work, actual-work, production, evaluation, delivery, acceptance, transfer, or receiving-use wording leaves that claim's participant meaning or orthogonal claim dimensions unclear.

The primary EntityOfConcern is one relation-bearing claim in an episteme. The trigger word helps a practitioner notice the problem; it is not the governed object, a participant kind, a relation kind, or a universal family of inputs and results.

The practical question is which relation can be stated for the receiving use. `SubjectPatternLocator` identifies the pattern description containing the defining or constraining ClaimGraph; case facts determine whether the relation obtains.

**First useful result.** Start at the boundary-word sentence and answer three ordinary questions: what exact thing is being named, relative to what exact method, plan, work, operation application, transformation, delivery, or receiving use, and what direct verb can safely be said now—or why can it not yet be said.

For example, a note says, `inspection report R-17 is the result of inspection`. `R-17` is an exact report episteme. If the current related object is independently identified inspection application `P-17` and its declaration-local result-binding predicate actually holds, write: `Inspection application P-17 returned report R-17.` Then stop unless the current use separately asks about report inception, inspection Work, evidence, publication, delivery, or acceptance.

The nearest three failures keep the same thing and related object while changing only the deciding deficit:

- if the binding governor is known and the case facts fail its positive predicate, the proposed positive binding is `factually unsupported`;
- if the governor is known but the fact needed to decide whether P-17 returned R-17 is unavailable, return `missing-information`;
- if no current result-binding predicate or direct report relation governs that pair, return `missing-governor` and name the exact participants, proposed predicate, affected use, and absent definition; name a future pattern or declaration need only when one is actually identifiable.

Only when another reading could change the answer should the practitioner make the formal distinctions explicit: reusable declaration versus intended, committed, current, or historical subject relation; exact extent; polarity; and whether the claim is assertable. A direct relation additionally names its exact `RelationKind` and resolving direct pattern or relation-declaration episteme. An operation binding or local claim instead names its declaration-local or admitted predicate and defining declaration. These assurance details check the ordinary answer; they are not prerequisites for understanding a simple positive past-tense sentence.

**What changes in practice.** The engineer stops debating which broad word is correct. They name the thing, the exact object it is relative to, and the direct verb they can safely say now; if the attempted claim is not assertable, they state the reason-specific stop under section 4.3. Formal claim dimensions and assurance apparatus appear only when they can change or check that answer. Planning, actual participation, production, evaluation, delivery, acceptance, and transfer no longer inherit one another through vocabulary.

**What goes wrong if missed.** A plan is read as actual participation; a method description is treated as a work occurrence; an operation result binding is mistaken for a produced entity; a changed continuing entity becomes a new output; a delivery or handoff package is treated as the transfer; or a convenient missing relation is replaced by a new universal kind.

**Ordinary non-use boundary.** Practitioners **SHOULD NOT** use this pattern when the exact direct relation and all claim dimensions needed by the receiving use are already readable; they **SHOULD** apply that direct pattern and stop. They **SHOULD** use `C.2.P` first when the unresolved question is which source expression, episteme, publication, or source-to-use relation is current; `A.15.PROD` directly when the only current question is production-work participation, entity-identity inception, or production completion and its participants are already exact; and the direct measurement, evaluation, commitment, delivery, acceptance, transfer, resource, premise, transformation, method, planning, or work pattern when that relation is already selected.

### A.6.P.WMR:2 - Problem

Boundary words are useful in ordinary language because they compress a relation into a role-like label. The compression becomes unsafe when a later claim depends on which relation actually obtains. The same entity can be a resource used by work, an argument bound in one operation application, an affected referent changed by work, a constituent of another entity, a premise used in reasoning, a newly constituted episteme, a delivered item, or an object used by receiving work. Those are not interchangeable positions.

The repair preserves ordinary readability without manufacturing a universal work-result ontology. It also recovers, without collapsing them, the claim subject, modality and temporal extent, polarity, and recovery or support state. A reusable declaration, an intended relation, an obtaining commitment, an actually obtaining or historically obtained subject relation, and an unresolved claim can overlap across those dimensions; they are not one posture axis. A sentence can be ontologically precise and still be false or unsupported; evidence and assurance remain separate questions.

### A.6.P.WMR:3 - Forces

| Force | Tension |
| --- | --- |
| Ordinary language vs exact relation | Practitioners need short sentences, while the receiving use needs exact participants and an obtaining condition. |
| Method semantics vs dated work | A reusable way of doing and its description can name participant roles without assigning or binding an entity in one actual occurrence. |
| Plan vs actuality | Intended work and planned fillings guide action but do not establish dated work or actual participation. |
| Operation binding vs work relation | An `A.6.1` application can bind an argument or result value without producing that entity or identifying the surrounding work. |
| Change vs production | Work can cause an actual change without constituting a new entity or completing production. |
| Readability vs ontology economy | A familiar label is cheap, but one universal input, output, result, or handoff kind would erase direct subject semantics. |
| Local blocker vs broad invention | A missing governor stops only the affected claim; independent claims continue, and ontology does not expand by convenience. |

### A.6.P.WMR:4 - Solution

Treat the boundary wording as a claim about one thing relative to another object. Recover the direct verb or reason-specific stop first. Keep claim subject, time, polarity and assertability independently recoverable when they can change the answer.

The method handles one relation-bearing claim at a time. The trigger word stays in view only until the exact thing, related object, and safe direct verb or stop are recoverable. The result replaces the compressed phrase with the shortest ordinary sentence. If a neighboring claim is still needed, apply the pattern whose Solution answers that exact question.

#### A.6.P.WMR:4.0 - Thin recovery core and conditional interfaces

The stable ordinary core is one `A.6.P`-isolated relation-bearing claim, one exact thing, one exact related object, one direct verb or reason-specific stop, exactly one of four truthful exit families, and one readable sentence. The fourth family explains why the attempted claim cannot be asserted: `factually unsupported`, `missing-information`, `missing-governor`, a governing rule's inapplicable result, or `missing-substrate`, as distinguished in section 4.3. `Missing-governor` names the affected use and absent definition, applicability, or occurrence rule; it names a future pattern or declaration need only when one is identifiable.

Claim subject, modality and temporal extent, polarity, and recovery or support state remain four independent assurance controls. Their values must be recoverable whenever they can change the answer, but a practitioner does not have to recite the four labels when an ordinary sentence already makes the only material reading clear. WMR supplies this recovery and stop. It does not absorb the algorithms, checklists, or ontics of rules applied to a separate question.

| Additional question and applicable rule | Apply it only when | Result used here |
| --- | --- | --- |
| the rule that defines or tests the exact direct relation, or `A.6.1` | the exact relation or one declared operation application is the current question | one readable direct subject-relation claim, one exact declaration-local application binding, or its exact non-assertability result |
| `A.6.RCD` | no direct relation closes the named use, and a substrate-admitted compound claim, repeated predicate semantics, or relation-kind question is current | its lightest local claim, reusable-definition or conditional kind-admission continuation, or exact blocker; WMR does not reproduce the derivation or disposition algorithm |
| `A.15.PROD` | production-work participation, entity-identity inception, or production completion is explicitly the current question | one local production claim or that branch's exact blocker; WMR does not reproduce the branch basis |
| `A.13` and `A.15.1`, then `F.18` when naming is needed | the sentence deliberately claims a particular performed Work occurrence | the A.13 basis and independent A.15.1 Work admission at the needed granularity, or the supported neighboring object or blocker; F.6 only for a separate precise assignment-bound attribution; F.18 only for a needed durable name |
| `A.3.4` and the rule for the current transformation-composition claim | the current claim actually depends on an actual change or positive transformation composition | one independently identified transformation, one governed composition result, or the exact missing-governor or missing-substrate blocker |
| the rule for evidence use, assurance, naming, delivery, acceptance, transfer, publication, or another subject | the current use additionally needs that distinct claim | only the separately established claim, judgment, name, occurrence, or blocker; none becomes a WMR field or makes the recovered relation obtain |

#### A.6.P.WMR:4.1 - Three ordinary questions and two conditional assurance questions

| Ask | Write |
| --- | --- |
| 1. What exact thing is this? | Name one exact referent under its admitted kind. `Input`, `Output`, `Result`, `Outcome`, `Deliverable`, and `Handoff` do not become kinds. |
| 2. Relative to what exact object is it being named? | Name one exact method description, plan, dated Work, operation application, transformation, evaluation, delivery, transfer, receiving work, or another directly governed object. Split several current related objects into separate claims. |
| 3. What direct verb can be said now—or why not? | Write the shortest direct relation sentence, declaration-local binding, local claim, or reason-specific non-assertability result. A synonym, shared time, plan row, diagram edge, or nearby record is not the deciding relation. |
| 4. Could a claim dimension change the answer? | Only then state the material claim subject, modality and extent, polarity, or recovery or support distinction. Keep them independent. |
| 5. Does a named later use need the formal governor or assurance replay? | Name the PatternID locator for the defining or testing content, exact `RelationKind` and relation-declaration episteme, declaration-local predicate, or local-claim rule that makes the answer checkable. Add occurrence identity, evidence, publication, or assurance only when that later use needs it. |

The practitioner stops after question 3 when the ordinary answer has one clear reading and no named later use needs more apparatus. Questions 4 and 5 inspect or reuse that answer; they do not replace it.

#### A.6.P.WMR:4.2 - Use the four claim dimensions only when they can change the answer

The four dimensions remain independent. Make a dimension explicit when two plausible values would change the sentence, the next action, or the stop. Otherwise let ordinary grammar carry it: `CF-17 was consumed by W-204 during I-204` already states a positive historical subject relation at one extent and does not require the reader to label four axes.

| Claim dimension | Recovered answer | Non-inference guard |
| --- | --- | --- |
| Claim subject | One reusable declaration, particular intended relation, commitment relation, or particular subject relation. | Selecting the subject decides neither whether it obtains nor its polarity, time, or support. |
| Modality and temporal extent | `generic`; `intended or planned`; `actually obtaining` at the current exact extent; or `historically obtained` at one exact past extent. State commitment fulfilment separately. | An obtaining commitment does not make the promised relation fulfilled; a past relation remains a historical claim at its governed extent. |
| Polarity | Positive or negative under one exact predicate, condition, and governor. | A governed negative claim individuates no obtaining relation occurrence. Absent support or missing information does not establish negative polarity. |
| Recovery or support state | `governed-and-assertable`, `factually unsupported`, `missing-information`, `missing-governor`, a rule-qualified inapplicable result, or `missing-substrate`. | This state reports whether the selected claim can be asserted; it neither makes nor prevents the subject relation from obtaining. |

**Well-formedness constraint `WMR-WF1` — orthogonal claim dimensions.** Whenever one of the four dimensions can alter the result, its value must be separately recoverable from the sentence or its immediate governed basis. No dimension supplies another. Explicit axis vocabulary is required only for a material ambiguity, comparison, assurance replay, or reusable formalization; it is not a prerequisite for every simple direct sentence.

`Factually unsupported` applies when an applicable governor and sufficient deciding facts are available but those facts fail the test for the proposed polarity. `Missing-information` applies when a fact needed to decide the test or its applicability is unavailable. `Missing-governor` applies when the participants and question are known but no direct rule supplies the needed predicate, condition or occurrence law. A failed test supplies no opposite polarity without its own basis.

A current commitment is expressible without collapsing fulfilment only when its exact commitment `RelationKind`, participant meanings, extent, obtaining predicate, and the `SubjectPatternLocator` for its defining or constraining content are named; a local id such as `COM-17` is not that settlement. The commitment does not establish fulfilment of the promised delivery. Judge that separate claim under its own predicate and case facts; unavailable facts leave fulfilment unresolved rather than proving non-fulfilment. A separately stated past case fact remains positive at its governed extent after its named participants satisfy the governor's predicate; it need not obtain now to remain historically true. A generic prescription from a policy or another normative episteme does not by itself assert an individual commitment. Open that individual branch only when the sentence claims a duty of an actual System or separately governed party under A.2.8.

A change in any dimension is substantive. A plan does not become an actually obtaining relation because its date arrives; a later observation does not retroactively manufacture a missing relation; and stronger support does not substitute for the subject relation's own facts.

#### A.6.P.WMR:4.3 - Choose one of four truthful exits

Choose by the kind of answer the receiving use needs:

1. If one direct subject pattern or declaration defines the relation between the exact participants, use the direct relation exit.
2. If the claim is only that one identified operation application used or returned one value, use the declaration-local `A.6.1` binding exit.
3. If the question is production-work participation, entity inception, production completion, or another substrate-admitted local conjunction, use the local `A.15.PROD` or `A.6.RCD` claim exit.
4. If the attempted claim lacks the required basis, stop with the reason distinguished below. A known inapplicability result and missing constructor semantics also use this exit; neither is forced into a failed-fact result.

The exit determines the next action; it is not a fifth claim classification.

| Exit | Use it when | Result |
| --- | --- | --- |
| Exact direct subject relation claim | The direct governor supplies the `RelationKind`, participant meanings, predicate, applicability, and defining source. A positive claim has separate case facts satisfying the predicate. A negative claim additionally has an explicit applicable non-obtaining criterion and separate facts satisfying it. | The shortest positive or negative direct sentence. A positive occurrence, assertion episteme, local id, and evidence remain distinct; a governed negative claim individuates no occurrence. |
| Exact `A.6.1` operation-application binding | One identified application and exact bound value satisfy the declaration-local argument or result predicate, extent, kind, cardinality, and identity rule. | A sentence stating only the binding. It says neither that dated work occurred nor that work produced, constituted, delivered, or accepted the bound entity. |
| Local `A.15.PROD` or `A.6.RCD` claim | One local production question or another local compound question admitted by the selected substrate is current, and no new occurrence kind is needed. | The readable local claim under its exact base governors and the lightest sufficient disposition. |
| Exact non-assertability result | The attempted claim is factually unsupported, lacks deciding information or a governor, is outside a known applicability rule, or lacks the constructor semantics needed to derive it. | A sentence naming the attempted claim and the corresponding reason below. Preserve the governing rule and known facts; infer no opposite polarity or fallback relation. |

For the fourth exit, retain the distinction that determines the next move:

- `Factually unsupported`: an applicable governor and sufficient case facts are available, but the test for the attempted polarity fails. An affirmative claim uses its positive test; a negative claim uses its negative or non-obtaining criterion or closure basis. Failure of one does not establish the other.
- `Missing-information`: a fact needed to decide the applicable test or its applicability is unavailable.
- `Missing-governor`: the required predicate, applicability condition, or occurrence rule is absent. Name the participants, affected use and missing rule; identify a future definition need only when one is identifiable.
- **Inapplicable under the named rule**: available facts establish that the case is outside that rule's applicability. Return its inapplicable result, not a negative relation claim. Select another rule only when it governs the receiving question.
- `Missing-substrate`: the proposed derivation needs constructor semantics that no current substrate supplies. Name that missing constructor basis under A.6.RCD:4.2; keep independently established base claims. This does not by itself justify a new relation kind.

These are reasons for withholding the attempted claim, not five truth values or new result kinds.

A positive direct-relation claim needs both a rule and case facts. The direct subject pattern or an applicable relation-declaration episteme supplies the admitted `RelationKind`, participant meanings, predicate, applicability and identity rule. Separate facts establish that the participants at the relevant extent satisfy that predicate. Within applicability, a failed positive test returns `factually unsupported`; an unavailable deciding fact returns `missing-information`; a case outside applicability retains the rule's inapplicable result. Reserve `missing-governor` for an absent governing rule. An additional published project declaration is unnecessary when the existing direct rule already supplies the needed meaning.

A governed negative sentence needs the analogous negative or non-obtaining criterion and separate facts satisfying it. Failure to support a positive claim, an absent record, or an unobserved event is not a negative premise.

A method-description field, planned filling, compatible type, stored reference, matching token or nearby record alone establishes no actual participant relation. Its content may make a claim or supply grounds; assess those under the direct predicate and, where reliance matters, A.10.

#### A.6.P.WMR:4.4 - Ordinary sentence shapes

These informative shapes help draft an answer once its meaning is known. Include only distinctions needed by the receiving use. Direct-relation wording is an ordinary reading of an admitted `RelationKind` under its defining rule; an assertion id does not replace that rule. Current and historical claims need facts for their participants and extent, but the compact sentence need not repeat the supporting account.

```text
Reusable declaration:
  Under <applicability>, <exact declaration> declares that <exact entity position>
  has <participant or predicate meaning>; no particular intended or obtaining relation follows.

Particular intended relation:
  <exact WorkPlan or other intended-work episteme> states that <exact entity>
  is intended to <direct relation> <exact related object> under <condition>;
  actual obtaining remains open.

Actually obtaining now:
  <exact entity> <direct relation in ordinary words> <exact related object>
  during <current exact extent>; governed by <RelationKind token> under <direct pattern or relation-declaration episteme>.

Historically obtained:
  <exact entity> <direct relation in ordinary words> <exact related object>
  during <exact past extent>; governed by <RelationKind token> under <direct pattern or relation-declaration episteme>.

Governed negative:
  During <exact extent>, <exact entity> did not <direct relation in ordinary words> <exact related object>
  under <RelationKind token>, with defining or constraining content at <SubjectPatternLocator>; <separate case facts> satisfy
  <the direct pattern's or declaration's explicit negative or non-obtaining criterion or closure basis>,
  and no relation occurrence is individuated.

Obtaining `U.Commitment`, promised relation separate:
  <U.Commitment occurrence> obtains for <actual duty-bearing System or separately governed party>, with <modality>, <referents>, <scope>, and <validity interval>;
  <current prescription>, <exact constitutive rule>, <rule-required actual instituting basis>, and <actual facts> satisfy the A.2.8 direct predicate;
  the promised relation remains <intended | unfulfilled | fulfilled at exact extent> under its own <RelationKind token> and <SubjectPatternLocator>.

Factually unsupported:
  Under <known governor>, the <positive or negative> claim that <exact relation sentence> is not assertable
  because <available facts> fail <applicable named condition>; no opposite polarity follows.

Missing information:
  Under <known governor>, whether <exact entity> <candidate direct relation> <exact related object> obtains
  is unresolved because <named deciding fact> is unavailable.

Missing governor:
  Whether <exact participant> <proposed direct relation> <exact related participant> obtains
  is unresolved for <named use> because no current definition supplies <predicate, applicability, or occurrence rule>;
  name a future pattern or declaration need only when one is identifiable. No PatternID or case fact is required for a rule that does not exist.
```

For example, `CF-17 was not consumed by W-204` does not follow merely because the positive consumption fact fails or is unavailable. It closes as a governed negative sentence only if the direct pattern or declaration for machining resource consumption supplies an applicable non-consumption criterion or complete closure basis for the exact quantity, work, and extent and separate case facts satisfy it. Otherwise the proposed positive claim remains `factually unsupported` or `missing-information`, or the relation question remains `missing-governor`, according to the independently recovered deficit.

A practitioner **MAY** retain the trigger word as optional Plain orientation after the direct sentence is recoverable. The direct sentence and its dimensions, not the familiar label or support state, carry the claim into planning, work, evaluation, delivery, acceptance, transfer, or receiving use.

#### A.6.P.WMR:4.5 - Composition and universal-result stop

**Invariant `WMR-I1` — ontology economy.** Recovering boundary wording does not introduce a universal input, result or handoff kind or relation; retain each recovered object and predicate under its own definition. **Invariant `WMR-I2` — transformation non-entailment.** A plan, desired state, model, description, evaluation, publication or flow representation does not establish an actual transformation merely by its presence or label. Claims and evidence in that material can support a transformation judgement under A.3.4; shared time, Work or referent alone does not.

When the repaired claim depends on transformation composition, state its exact participants and question, then apply `A.3.4` and the rule for that composition claim. Keep only the resulting independently identified transformations plus either one governed composition claim or the exact missing-governor or missing-substrate blocker. WMR does not restate or evaluate their contribution, compatibility, composition, or reidentification algorithm.

The blocker reaches only the composition-dependent claim; independent work, change, production, evaluation, delivery, acceptance, transfer, and receiving-use questions continue under their own governors.

#### A.6.P.WMR:4.6 - Recognition and assurance remain separate

For ordinary recognition, the first three questions and one of four truthful exits are enough. Use the two assurance questions and explicit claim-dimension vocabulary only when they can change the answer or a named later use needs to inspect it.

A practitioner **MAY** open a separate assurance branch when the receiving use additionally needs evidence, warrant, assurance, gate, currentness, publication, or reliance. Apply the relevant evidence, assurance, gate, currentness, publication, or reliance check to the exact direct subject claim, `A.6.1` application binding, local `A.15.PROD` or `A.6.RCD` claim, or non-assertability result together with its governor. Preserve the section 4.3 reasons and their different continuations. A missing subject rule may identify a future pattern or declaration need; unavailable constructor semantics retain their separate derivation question. Support or assurance changes neither polarity nor whether the subject relation obtains.

#### A.6.P.WMR:4.7 - Recover a result and reuse its established meaning

Start with the receiving question: what may someone do because this result is available? Applying a description, accepting a produced entity, closing Work, and relying on a later effect need different answers. When the trigger is `result`, use the deciding fact before any catalogue:

- if the statement describes what successful enactment should obtain or preserve, use A.3.1 for the Method's intended effect, or A.15.2 for the particular WorkPlan's target;
- if the same entity continues and changed, recover that continuing entity and its separately governed change;
- if a condition continued to hold, state that condition over its required extent; attribute its maintenance to Work only through the applicable maintenance predicate and its facts;
- if an entity first began to exist, or that is the question, open A.15.PROD's entity-inception branch;
- if one operation application returned a value, state only its A.6.1 result binding;
- if the referent is a measured characteristic value, keep that exact value and its direct measurement relation; if it is a comparison, diagnosis, or evaluation claim, identify that exact C.2.1 episteme and its direct basis;
- if an entity was delivered or transferred, use the direct delivery or transfer occurrence;
- if the question concerns fulfilment of a promise, use A.2.3's specified outcome and acceptance conditions;
- if the claim is a downstream effect, apply the pattern whose Solution answers that exact effect-relation question;
- if `result` names a `C.11` `ChoiceResult`, an acceptance verdict, a decision occurrence or record, or another value, entity, fact, or claim already identified under its applicable identity or occurrence rule, keep that exact kind and write only the direct relation current for this use.

If the selected reading lacks a deciding fact or governor, return its reason-specific non-assertability result. The word `result` does not establish one kind or relation family shared by these different readings. This does not prevent the same established meaning from recurring with different participants, including entities of different kinds.

**Reuse the meaning, then obtain the facts of this case.** A.15.PROD supplies one such repeated meaning: **a produced result of Work is an entity that first exists through that Work's governed effects under its applicable identity specification**. This is a readable summary of its local inception claim, not a new binary predicate. Keep the entity's own kind. A ship and an episteme use different identity specifications while instantiating this same production meaning. The Work, specification and applicability, first-existence boundary, and Work-to-change and change-to-identity grounds remain available in each claim. Use A.15.PROD:4.3–4.5 to obtain that answer; reusing its meaning does not supply a missing fact or subject rule.

The same discipline applies to other established relations. A.2.3:8.1 defines `deliversPromisedOutcome(W, OS)` and `fulfilsPromiseContent(W, SC)`; the latter additionally tests acceptance. Their second participants are the OutcomeSpec and PromiseContent epistemes respectively, even when the promised condition concerns a physical entity. Substituting the affected thing for the specification changes the predicate. A Method's intended effect or a plan target does not by itself establish a promise or fulfilment. A.2.8 separately governs an individual duty.

For another occurrence of the same claim, retrieve its existing predicate or compound definition and retain its participant meanings, applicability and limits. Substitute the new participants and check their facts. A changed entity kind calls for the applicable identity or subject rule; it does not by itself call for a new result meaning. A different receiving question may require another relation even when the entity is unchanged.

When the same needed rule is repeatedly missing, use A.6.RCD:4.1–4.5. Reuse a direct predicate where one suffices; keep a one-use compound claim local; define a repeated compound rule once in its subject practice. Distinguish a law limited to one exact subject from a predicate definition reusable across subjects. The latter has the definition itself as its EntityOfConcern. Only a use that consumes the identity of an obtaining relation occurrence opens relation-kind admission. Neither repeated wording nor heterogeneous participants requires that additional ontology.

**Keep useful preservation and later use visible.** Work may achieve its intended benefit by keeping an existing condition within limits. A.3.1 supplies the Method's intended preserved condition. The subject rule and observations over the required interval decide whether that condition held; a further Work-to-maintenance claim needs its own applicable basis. Unchanged endpoints alone establish neither continuous preservation nor its attribution. A new object is unnecessary for this benefit. Performing Work alone does not establish a change of the referent whose condition was preserved.

Likewise, an existing description can be used in several later actions without being produced again. State what was used and how. A.6.1 can supply a binding when the receiving action is an application of that declared operation. A.6.RCD:4.5a supplies repeated formal rule-content derivation and criterion-selection semantics for exact ClaimGraphs; it does not assert consultation, Work use or causal benefit. Use the receiving subject's rule for those claims. If the rule is known but the use fact is unavailable, obtain that fact. If the required use meaning has no definition, develop that definition. Do not turn either gap into a claim that the existing result was useless.

**Joint work and project results use the same subject meanings.** For jointly necessary work parts, A.15.PROD:4.5 uses their independently established A.15.1 composite Work as identity-closing Work. A.15.6:4.1 adds the qualifications for an actual project. A plan, a shared document or several contributors does not establish either whole. Once the whole and its effects satisfy the production claim, its produced entity has the same result meaning as for another Work occurrence.

A supported part result can already be reported: “Within P, W1 obtained x under this rule.” That conjunction preserves the result and work parthood. To claim that P itself obtained x, closed its production, fulfilled its promise or caused a downstream effect, establish the grounds of that further claim at P's extent. Work composition supplies no universal rule for inheriting results or adding unlike measures. Preserve independently supported part results when the whole claim remains open.

The broader boundary-word palette below is an informative recognition aid. A row suggests a likely related object and candidate semantics; the result then leaves the palette for the direct governor. Several rows may apply to the same entity at different times or for different uses, and they remain separate claims.

| Encountered wording | Recovery direction |
| --- | --- |
| `input` | Name the exact entity and related object. Test the concrete affected-referent, resource-use, parameter-binding, constituent-supply, premise-use, reference-use, operation-argument, transformation-participation, planned-filling, or other direct relation current in the case. No input family follows. |
| `raw material` or physical `source material` | Keep the physical entity distinct from its constituent, affected-referent, consumed-resource, transfer, supply, or transformation relation. `Source` alone does not open C.2.P. |
| epistemic `source data` or `source material` | Let C.2.P recover the exact source expression, episteme, publication, and source-to-use relation; then recover the separate relation to the current method, plan, work, transformation, evaluation, or receiver. |
| `output` | Apply the `result` split above. A changed continuing entity is not newly constituted merely because it is called an output. |
| `result` | Apply the deciding branches above. Keep the referent under its own kind and write only the direct relation or binding that makes this use true. |
| `outcome` | Distinguish a downstream subject effect from a measured value, comparison, or evaluation verdict. Each has its own related object and governor. |
| `deliverable` | Recover the entity separately in each planning, commitment, delivery, and acceptance claim. Planned, produced, delivered, and accepted are not inherited from one another. |
| `handoff` | Recover the actual transfer work or direct transfer relation. A package or record is a separate episteme; transfer, delivery, and receiving use remain distinct. Use E.10.MOVE only when that exact process-move question is current. |

When no direct governor closes a selected row, name the exact participants, proposed predicate and question, affected use, and absent definition, applicability, or occurrence rule. Name a future pattern or declaration need only when one is identifiable. A broader hypernym, another boundary word, or a new universal record does not settle the missing relation.

#### A.6.P.WMR:4.8 - Work-name grounding by morphology and occurrence

An action nominal such as `testing`, `assembly`, `maintenance`, `evaluation` or `inspection` does not identify an occurrence by its morphology. Recover what it names under the applicable subject rule: for example, an admitted Method, a MethodDescription about that Method, a plan item, a required effect or a performed Work. Use A.6.F when function-like wording still hides its object or relation; that pattern distinguishes the transformation, structure, view, capability and other functional claims. A WBS element or Work Package ordinarily describes intended work; an actual occurrence needs its own basis.

A use that needs only the recovered method, method description, plan, structure, or other already governed value closes under that direct pattern. Only reliance on the label as one performed occurrence handles the candidate designation and required granularity under `A.15.1`.

For a deliberately asserted particular Work occurrence, recover its A.13 basis and apply A.15.1 independently. Use the established Work at the needed granularity, a supported neighboring object, or the stated blocker. A material `workContinuityPolicyRef` belongs to the A.15.1 identity judgement. If the sentence additionally attributes Work to an assignment, use F.6 with that same A.13 assignment; missing or contrary attribution facts do not erase the Work. Apply F.18 only after the occurrence is established and needs a durable name.

Any output, result, outcome, production, delivery, or acceptance wording is a separate WMR claim only while its direct relation or claim dimensions remain hidden. Once readable, apply the rule for that relation or claim; it does not become part of work identity.

The preceding action-nominal classification is an FPF-scoped synthesis from recurring morphology-and-subject ambiguity, not a rule imported from PMI, PRINCE2, IDEF0, or IDEF3. A domain may conventionally use an action nominal as the durable name of an already grounded method, plan item, functional-view record, or dated work occurrence; that direct identity and exact predicate win over morphology. The synthesis reopens if repeated practice shows that the cue classifies a directly grounded value under the wrong predicate family, or if a trigger case cannot close through `A.6.F`, the exact subject predicate, or `A.15.1` without new ontology.

| Planning or description lineage | Bounded use here | Prohibited inference |
| --- | --- | --- |
| PMBOK WBS practice | Its deliverable-oriented naming pressure is used only to recognize that WBS elements and Work Packages are often named from expected deliverables. | The named plan element proves no dated occurrence, enacted method, actual participant, produced entity, result, or outcome. |
| PRINCE2 7 public Foundation page | Its description of seven broad project-management practices supplies a vocabulary comparison. Detailed product, product-description, activity and Work Package distinctions need their own official source. | The page alone supplies neither those detailed distinctions nor FPF occurrence identity, production, delivery or acceptance facts. |
| IDEF0 historical recognition lineage (non-authoritative here) | A box label remains source-side function-model wording. A still-hidden FPF claim requires `A.6.F`; otherwise the label names the already recovered required-transformation or required-effect claim, actual `U.Transformation`, functional-view record, method description, `TransformationFlowStructure` locus, or other exact governed value under its direct pattern. | This lineage supplies no positive FPF kind inference: neither box form nor function wording identifies `U.Function` or supplies identity evidence for a performed Work occurrence admitted under `U.Work`. |
| IDEF3 Units-of-Behavior historical recognition lineage (non-authoritative here) | The terminology remains only as wording that may occur in inherited process descriptions. | This lineage supplies no positive FPF kind or relation inference; a Unit-of-Behavior description or label is never identity evidence for a dated Work occurrence admitted under `U.Work`. |

**Inspection contrast.** `inspection method` names the way of doing. `planned Pump-14 inspection work` is intended-work content. `Pump-14 inspection on 2026-07-15 09:10-09:34` becomes an exact performed occurrence only when applying A.15.1 establishes it at the required granularity; otherwise retain the lowered object or blocker. If the current question is whether the work first constituted an inspection-report episteme, apply A.15.PROD and use its local entity-identity-inception claim or exact branch blocker. A measured or diagnostic result uses its direct result rule, and a pass/fail verdict remains a separately governed evaluation-result episteme rather than the inspected entity or a downstream effect.

### A.6.P.WMR:5 - Archetypal Grounding

These constructed cases show different recovery branches. Their project declarations and case facts are supplied assumptions; local relation tokens do not thereby become FPF kinds. Section 5.1 shows both the ordinary result and the rule-and-fact comparison supporting it.

#### A.6.P.WMR:5.1 - Inspection and machining: one ordinary result, one assurance replay

A source says, `the inspection report is the result of inspection`. First identify report episteme `R-17` and ask what it is relative to. If exact inspection application `P-17` actually returned `R-17` under its declaration-local result predicate, write: `Inspection application P-17 returned report R-17.` If the current question is when exact Work first constituted the report, apply A.15.PROD. If neither relation is governed, return `missing-governor` naming `R-17`, the proposed application or Work participant, proposed predicate, affected use, and absent definition; name a future pattern or declaration need only when one is identifiable. Do not invent `WorkResult`.

Now a traveler says, `raw stock WP-204 and cutting fluid CF-17 are inputs; the machined part and inspection report are outputs of machining`. Exact machining Work `W-204-MACHINE` and continuing workpiece `WP-204` are already identified. The ordinary result is:

- `Applying A.15.1 identifies W-204-MACHINE with affectedReferent WP-204.`
- `Cutting-fluid quantity CF-17 was consumed by W-204-MACHINE during I-204 under MachiningWorkConsumesResource.`
- `T-WP204-GEOMETRY is the bounded geometry change of continuing WP-204; W-204-MACHINE caused it under MachiningWorkCausesGeometryChange.`

The workpiece remains `WP-204`, not a newly constituted output. A report binding or inception claim stays open until its own application or A.15.PROD basis is present. If the consumption fact fails, the proposed positive fluid claim is `factually unsupported`; if it is unavailable, return `missing-information`; if the relation governor is absent, return `missing-governor` and name the missing machining-resource predicate and its defining pattern or declaration.

A later measurement-result episteme `R-204`, diagnostic finding, evaluation verdict, or accepted-deliverable claim is a separately governed claim; delivery or physical transfer of continuing `WP-204`, and transfer or publication of `R-204`, are separate again. Shared chronology and one machining case entail none of them: each current claim needs its own direct governor and facts.

**Case declaration and facts.** Relation-declaration episteme `MFG-WORK-REL-2026` contains the defining ClaimGraph for these case-local predicates:

| RelationKind | Direct participants and extent | Obtaining condition and applicability |
| --- | --- | --- |
| `MachiningWorkConsumesResource` | exact consumed resource quantity, exact Work individual admitted under `U.Work`, and `Γ_time` | the quantity was actually consumed by that Work during the named extent; applicable only to Plant-7 machining Work |
| `MachiningWorkCausesGeometryChange` | exact Work, independently A.3.4-grounded geometry transformation, and governed extent | that Work actually caused that transformation at the extent; applicable only to the named Plant-7 case |

Separate case facts establish that `CF-17` was consumed by `W-204-MACHINE` during `I-204` and that this Work caused `T-WP204-GEOMETRY`. Merely identifying the declaration, Work, transformation, chronology or assertion epistemes `MFG-RU-CF17-W204` and `MFG-WC-W204-TWP204` would not supply those facts. Assertion content and evidence can support them under the governing predicates. Comparing rule and case facts yields the ordinary sentences above and distinguishes the three failure reasons.

#### A.6.P.WMR:5.2 - ETL data: direct participation, then a receiving-use stop

An ETL note says, `RawOrders is the source input and WarehouseOrders is the delivered output`. Exact Work `ETL_Nightly_0811` and both dataset entities under their admitted subject kinds are known. Exact relation-declaration episteme `ETL-DATA-REL-2025` contains the defining ClaimGraph for `SourceDatasetParticipatesInETLWork` and `DestinationDatasetParticipatesInETLWork`; separate case facts say that `RawOrders_0811` and `WarehouseOrders_0811` satisfy the declared source-dataset and destination-dataset participant meanings and predicates for that job.

Write: `RawOrders_0811 participated as the source dataset in ETL_Nightly_0811`, and `WarehouseOrders_0811 participated as the destination dataset in ETL_Nightly_0811.` Those facts establish neither delivery nor use by analytics. If decision Work `D-0811` is now claimed to use `WarehouseOrders_0811` as a premise but no premise-use, reference-use, or application-binding governor is available, stop with `missing-governor` and name the missing analytics-decision predicate and receiving use. This case demonstrates a positive direct relation followed by a distinct blocked receiving use.

Before calling `WarehouseOrders_0811` a new output, decide which dataset continues. If the ETL job updates the same dataset in place, identify that dataset's bounded change under A.3.4. If a derived dataset begins, apply its dataset-identity rule and use A.15.PROD only when the exact inception basis closes. When a catalog entry, lineage view, or publication is the source from which a reader reaches either dataset, use C.2.P to identify the exact source expression, source-to-use path, allowed use, and reopen condition. An E.17 face or form, or an E.24.PUB publication or availability occurrence, neither creates the dataset nor proves that analytics used it. Row-count, quality, latency, and drift results remain separate measurement or evaluation objects; each evaluation names its own criterion and predicate and cites the `SubjectPatternLocator` for their defining or constraining content.

#### A.6.P.WMR:5.3 - Clinical work: administration is not a health outcome

A case note says, `the patient and dose were inputs; the summary and good outcome were results`. Exact clinical Work `Appendectomy_Case_8472` has affected referent `Patient_8472`. Relation-declaration episteme `MED-ADM-2026` defines `ClinicalWorkAdministersDoseToPatient`; the independent case fact states that this Work administered `MedicineDose_8472` to `Patient_8472` during the named interval, satisfying that predicate.

Write: `Appendectomy_Case_8472 administered MedicineDose_8472 to Patient_8472 during the named interval.` Keep `DischargeSummary_8472` as an episteme whose binding or inception needs its own basis. First ask whether `good outcome` means a measured value, an evaluation verdict, a patient-state change, or an effect attributed to this Work. Keep that question open when the case does not select a reading. Once the claim is exact, apply its subject rule and distinguish an unknown fact, a failed criterion and an absent governor. Return `missing-governor` only for an actually absent rule. This case demonstrates a positive administration claim and a separately unresolved outcome claim.

Administration is only one possible relation for `MedicineDose_8472`. The same medicine quantity may instead be a constituent of an administered preparation or compound therapy, or a resource consumed by the clinical Work; each alternative needs its own exact direct governor and case fact, and the positive administration sentence proves neither. If a patient-state change is current, first identify that exact transformation under A.3.4. Then ask separately whether a declared work-to-patient-change predicate with the exact Work, transformation, applicability, and a satisfying case fact obtains. Administration alone proves neither the change nor that the clinical Work caused it.

Keep a measured value, diagnostic finding, evaluation verdict, and claimed health effect as four different objects or claims. A discharge summary may cite any of them without becoming them. Each current claim names its own participants, temporal extent, predicate, criterion when applicable, and the content that supplies that predicate or criterion; a measurement or diagnosis does not establish a verdict, and a verdict does not establish the patient's later health effect.

#### A.6.P.WMR:5.4 - Pump 14: continuing entity and later decision use

A P2W note says, `the pressure problem was the input, adjustment was the work, and restored pressure was the result`. Keep accepted `ProblemCard@Context PC-P14-PRESSURE` as the separate problem-side object. Do not say that this accepted pressure-problem claim guided `U.WorkPlan WP-P14-2026-07-15`: the case supplies no direct relation for that use. Return `missing-governor` naming the ProblemCard and WorkPlan participants, proposed planning-use predicate, affected planning use, and absent definition; name a future declaration need only if one is identifiable. Do not infer that the problem caused `W-P14-ADJUST-1010-1020`. A.15.1 identifies that Work; A.3.4 identifies `T-P14-PRESSURE-RISE` as a bounded change of continuing `HydraulicLoop_P14`. Exact relation-declaration episteme `P14-REL-2026` contains the defining ClaimGraph for `AdjustmentWorkCausesPressureRise` and `MeasurementResultUsedByDecisionWork`; separate case facts satisfy both predicates.

Keep four values separate: `SetPointAdjustment@PlantOps-v3` is the selected `U.Method`; an A.3.2 `U.MethodDescription` has that admitted Method as its exact EntityOfConcern and makes a substantive claim about it as a way of doing; `WP-P14-2026-07-15` states intended Work; and `W-P14-ADJUST-1010-1020` is the dated Work occurrence. Naming any of them neither identifies an additional relation nor makes one obtain, so the unsupported ProblemCard-to-plan guidance claim remains `missing-governor`.

`P14-REL-2026` is available in the current case record. Independently, a separately stipulated world-side fact satisfies its actual-causation predicate, so write: `W-P14-ADJUST-1010-1020 caused T-P14-PRESSURE-RISE`. In the explicitly earlier case record, `P14-REL-2026` is absent; at that epistemic stage, keep that Work and transformation separate and return `missing-governor` naming both participants, the proposed causation predicate, the affected use, and the absent definition. No receiver or future declaration is required to state that blocker. Separately write: `Decision Work D-P14 used measurement-result episteme MR-P14-AFTER as its declared basis.` The loop continues; no entity begins, no production-completion criterion is current, and no transformation-composition claim follows. This case demonstrates work-caused change and later epistemic use without a production reading.

#### A.6.P.WMR:5.5 - Hair styling: a changed referent and an unresolved configuration

A salon record says, `hair and gel were inputs; the hairstyle, photo, and satisfaction were outputs`. A.15.1 identifies styling Work `W-STYLE-27` with affected referent `Hair_27`; A.3.4 identifies `T-HAIR-27` as the arrangement change of that continuing hair. Exact relation-declaration episteme `SALON-RESOURCE-USE-2026` contains the defining ClaimGraph for `StylingWorkConsumesResource` and `StylingWorkCausesHairArrangementChange`; separate case facts support the work-change claim and, when known, the gel-consumption claim.

Write: `Applying A.15.1 identifies W-STYLE-27 with affectedReferent Hair_27`, and `W-STYLE-27 caused T-HAIR-27 under StylingWorkCausesHairArrangementChange.` When the separate consumption fact is present, also write: `W-STYLE-27 consumed StylingGel_27 under StylingWorkConsumesResource.` Do not yet write `EveningArrangement_27 is the resulting configuration`: the case has not selected whether that name denotes an A.22 structure, a characteristic-state fact, a relation occurrence or a description episteme. Return the question of which subject and claim the receiving use needs, retaining the independently established hair change. Once that claim is recovered, apply its subject rule; distinguish a missing fact, a failed test and an actually absent governor. This case demonstrates a continuing changed entity and an unresolved configuration reading.

`Client_27` is the person receiving the service; `Hair_27` is the continuing affected referent. A hair-to-person part claim, a service-recipient claim, or a person-level effect claim needs its own exact direct governor and case fact; naming the client beside the hair establishes none of them. In this arrangement case, styling changes continuing `Hair_27`; the case supplies no new entity-identity inception. A separately individuated wig, extension, or other artifact may instead open its own identity-inception question under A.15.PROD when its identity rule and inception basis close.

For gel use, distinguish the three stops. With a current `StylingWorkConsumesResource` governor, a case fact that fails its predicate is `factually unsupported`, while an unavailable consumption fact is `missing-information`; an absent governing predicate or applicability condition is `missing-governor`. A method-description ingredient field or appointment-plan row substitutes for none of those bases. `Photo_27` remains separately identified: its identity, photography or record-forming Work, representation of `Hair_27`, and publication are separate questions. A measured satisfaction response, an evaluation verdict, and any downstream effect of the service likewise require separate predicates and subject patterns; none constitutes the hairstyle or follows from the photo's presence alone. Its content may supply relevant observations, interpreted under the applicable subject rule.

#### A.6.P.WMR:5.6 - Car 42: completion without inception

A finishing note says, `the last nut was the input and completed Car 42 was the output`. Car 42 already satisfies its identity rule before `NutFasteningWork-42`. Exact relation-declaration episteme `CAR42-WORK-REL-2026` contains the defining ClaimGraph for `FastenerParticipatesInFasteningWork` and `FasteningWorkCausesFastenerChange`; separate case facts say that `Nut-42-LAST` participated and the Work caused the two independently identified fastening transformations.

Write: `Nut-42-LAST participated in NutFasteningWork-42 under FastenerParticipatesInFasteningWork`, and `NutFasteningWork-42 caused the two named fastening transformations under FasteningWorkCausesFastenerChange.` Do not open entity inception: the car continues.

For the narrowly bounded finishing use, `NutFasteningWork-42` can be the whole Work selected by a local A.15.PROD production-work claim only when the fastening method's intended production effect and applicability, the exact work-to-change facts, and the current completion facts supply that narrow production basis. For the broader factory use, the same occurrence can be a proper operational part of `CarProductionWork-42` only when an exact A.15.1 work-part relation obtains and the containing Work has its own separate production basis. Neither reading supplies the other, and neither proves that the two fastening transformations are parts of one composite transformation.

When completion is current, use exact completion-criterion episteme `CAR-COMP-ED-42`, its named applicability basis, exact boundary state, and production Work to ask A.15.PROD for the historically indexed completion claim. The suffix `ED-42` and the criterion's publication establish no edition continuity. Assert a separate C.2.1 `EpistemeEditionRelation` only when its continuation predicate is established. Without that basis, retain the distinct criterion epistemes and leave continuity unresolved; a known non-continuing replacement may be stated on its own facts. If Car 42 had already completed earlier, classify the fastening separately as rework, repair, or maintenance. This case demonstrates completion distinct from inception and from automatic criterion lineage.

Production completion establishes neither delivery, acceptance, release, nor Car 42's present condition. Each current claim needs its own direct governor and facts.

#### A.6.P.WMR:5.7 - Authoring: a produced explanation, its continuing use, and the next missing fact

An authoring note says, `research notes were inputs; the draft was the output handed off to review`. The reader needs to decide whether to review an available explanation, finish its construction, or recover a missing basis. This constructed case first obtains a positive answer through the existing suppliers, then changes one fact.

**Identify what the author obtained.** Under C.2.1, `DraftEpisteme_31` has ClaimGraph `G31`, exact EntityOfConcern `PreparationMethodProposal_31`, and effective ReferenceScheme `StudioPreparation-2026`. G31 explains a proposed timing-correction procedure, its independently supplied error bound, and different limits for analysis and viewing. It is an episteme about a proposed way; writing it does not establish that the proposal is an identified Method or that a recording was edited.

If a later rendering leaves all three identity discriminators unchanged, keep DraftEpisteme_31 and state only the changed carrier, rendering, publication, evidence or transfer relation. If a discriminator changes, identify distinct `LaterDraftEpisteme_31`; assert `EpistemeEditionRelation(DraftEpisteme_31, LaterDraftEpisteme_31)` only when C.2.1's historical-continuation predicate obtains.

**Obtain the production claim from A.15.PROD.** In the positive case, an engineer's Work supplies the bounded technical argument and an author's Work connects that argument to the procedure and its uses. A.15.1 has independently established both occurrences, with their A.13 performer bases and enacted Methods, and their exact work-part relations to composite `W-AUTHOR-31`. The applicable authoring Method intends constitution of the complete explanation. The following is the case's supplied A.15.PROD basis, rather than an inference from the words `draft output`.

| Question the production claim needs | Supplied case basis |
| --- | --- |
| What changed? | A.3.4 identifies `ManuscriptContentChange_31` of continuing manuscript carrier `Manuscript_31`. Its before-state lacks the connected G31 content; its after-state contains that complete articulated content with the named concern and interpretation scheme. This is change of the carrier, not change of one continuing episteme's ClaimGraph. |
| Which Work effected it? | The case declaration `AuthoringContentPredicates-31` defines `authoredContentChange(work, change)`: within the applicable authoring Method, the performed content-editing operations of that Work target the exact manuscript and effect the edits that identify that change. The independent operation, target and edit-history facts satisfy this test for W-AUTHOR-31 and ManuscriptContentChange_31. |
| Which entity first exists? | The applicable `DraftContentIdentitySpec-31` uses C.2.1's three identity discriminators for this authoring practice. Its applicability claim covers the exact candidate content, manuscript and ordered boundaries. The complete history supplied in the case establishes that this exact episteme did not exist at an earlier candidate boundary. A distinctness test alone would not establish that history. |
| How did the change close that identity? | The same subject declaration defines `contentChangeConstitutesEpisteme(change, specification, candidateBasis, boundary, episteme)`: the change constitutes the exact articulated content, concern and effective interpretation scheme required by the applicable specification, with first satisfaction at that boundary. Separate case facts establish this link at 10:20. Before that boundary the candidate content is not a future episteme participant. |
| Whose joint result is it? | The two independently identified work parts are jointly necessary for this complete content; neither has constituted it alone. Their admitted composite W-AUTHOR-31 is the identity-closing Work. No composite Transformation or Method parthood is inferred. |

For this derivation, case substrate `AuthoringInceptionClaims-31-v1` uses A.15.PROD:4.7's time-indexed conjunction of these named governed facts. It retains the Work parts and change witnesses, uses the supplied ordered candidate boundaries 10:00, 10:10, 10:20 and 10:30, and selects the first boundary satisfying all inception conditions. These are all content-constitution boundaries in the complete case history, not samples of an otherwise unobserved interval. That history makes the identity test false at the two earlier boundaries and true at 10:20. Unavailable premises remain undecided; their absence supplies no negative fact. The replay yields the local inception claim with `EntityOfConcern = DraftEpisteme_31`, indexed by the exact specification and applicability basis. These case declarations supply no universal authoring, change or result relation kind.

The useful sentence is now: **“W-AUTHOR-31 jointly produced this explanation at 10:20; review its proposed procedure and stated limits.”** Work continues until 10:30, so the inception result is not its completion claim. Production completion, acceptance and publication each retain their separate question.

This reuses the same production meaning as Ship 27 in A.15.PROD:5.2. There the produced participant is a `U.System` under an applicable hull-identity rule; here it is a `U.Episteme` under the applicable content-identity rule. In both cases, first existence through the governed effects of the identified Work is the result meaning. Neither the ship's hull rule nor the author's content rule is substituted for the other. The practitioner reuses A.15.PROD and the applicable subject definitions, rather than inventing a result predicate for each noun.

**Remove one essential fact.** Keep the two work identities, their composition, the observed manuscript change, the content-identity specification, its applicability and the first-satisfaction history. In this variant, the facts establishing which Work's editing operations targeted Manuscript_31 and effected those edits are unavailable. The definition of `authoredContentChange` remains known. The result is `missing-information` for W-AUTHOR-31's asserted link to ManuscriptContentChange_31. Recover that operation-and-target history before claiming production by this Work in the variant. The available explanation can still be reviewed on its content; the unresolved production attribution does not erase it. If the corresponding subject predicate had never been defined, the different result would be `missing-governor`; repeated authoring uses would justify developing that definition under A.6.RCD, not guessing the missing case fact.

**Use the explanation outside its producing Work.** Exact relation-declaration episteme `AUTHORING-USE-REL-2026` supplies the already established source-premise and review-reference relations for this case. Its premise-use condition requires actual use of identified source claims in the Work's stated inference; its review-reference condition requires an actual bounded comparison using the identified reference content. Separate case facts support: `Authoring Work W-AUTHOR-31 used SourceNotes_31 as a premise`, and `Review Work W-REVIEW-31 used DraftEpisteme_31 as a reference`. The latter Work compares another proposal's viewing limit against G31's stated condition. It does not produce DraftEpisteme_31 again.

When only the content-basis question is current, A.6.RCD:4.5a's `derivedUsingRuleContent` or `evaluatedAgainstRuleContent` may already state it: name the exact dependent and base ClaimGraphs and the derivation or criterion-selection fact. Those predicates do not replace the separate Work-use claim above. The presence of a saved file, bibliography entry or handoff record alone supplies neither actual-use fact. Its content can supply a trace or other grounds for the actual-use claim. The next action after a missing reference-use fact is to recover the bounded comparison, not to assert that the reviewer benefited from receiving a file.

**Continue a useful condition without replacing the result.** A Method engineer can continue using that same explanation while its source-based qualification remains applicable. Suppose a source revision changes only the analysis limit. The applicable qualification rule requires the source argument, the selected use's limits and its dependencies to remain supported. The recovered dependency facts show that the viewing argument and its 8 ms condition are unchanged; the analysis claim depends on the revised argument. The engineer may continue the viewing use and return the analysis claim for requalification. A second description or a new production claim is unnecessary for that continuation.

Now remove the dependency information needed to bound the source change. Continued viewing use becomes unresolved too; absence of a visible edit cannot establish unaffectedness. Recover the affected dependencies or widen the recheck. This is a repeatable application of the qualification rule to a new situation. Claiming additionally that maintenance Work kept a condition true throughout an interval would require that Work's own predicate and interval facts. The useful preservation of an applicable result does not supply that further attribution.

**Keep availability and transfer at their own scope.** `DraftFile_31` is a separately identified form-bearing entity, not DraftEpisteme_31. File inception and episteme inception are separate A.15.PROD questions. Rendering work or changed bits alone settles neither. When publication is current, exact occurrence `PUB-31` obtains under E.24.PUB while its five fixed participants—the selected episteme edition, audience declaration, bounded-use declaration, exact publication form and presentation carrier—satisfy its availability predicate. Together with the maximal continuous availability interval, they identify the occurrence. E.17 governs the multi-view face or form instead. The declaration-local phrase `selected episteme edition` creates no edition continuity.

Established availability lets the named audience obtain that content through that form and carrier. Actual access, delivery, acceptance, transfer, reliance and review use still need their own facts. If ordinary `handed off` wording already names one exact transfer relation, apply its direct pattern and stop. A package or handoff record alone establishes neither transfer nor receiving use; examine any asserted content and supporting facts under those relations' own rules. Apply E.10.MOVE only when the wording still hides an FPF-governed move, workflow, next action or readiness claim; its recovery creates none of those occurrences or permissions.

### A.6.P.WMR:6 - Bias-Annotation

| Bias | Countermeasure |
| --- | --- |
| Artifact bias | The countermeasure distinguishes a changed continuing referent, newly constituted entity, episteme, resource, or delivered item before any `result` reading. |
| Workflow bias | Arrows, stages, WBS rows, and work-package names remain descriptions or plans until exact work and direct relations obtain. |
| Production bias | Work-caused change, entity-identity inception, and production completion remain separate claims. |
| Data bias | Epistemic source-to-use and premise or reference relations remain explicit; a datum does not become an operation argument or work input by default. |
| Evidence bias | A record's presence or an application binding alone establishes no truth, warrant, acceptance or downstream use. Examine the recorded claim and grounds for the particular inference. |
| Ontology-growth bias | An exact blocker replaces any convenience move toward a broad new kind. |

### A.6.P.WMR:7 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-A6PWMR-1` | A conforming practitioner **MUST** keep one exact relation-bearing claim as the `EntityOfConcern` and **MUST** treat trigger words only as recognition aids. |
| `CC-A6PWMR-2` | A conforming practitioner **MUST** name the exact entity and admitted kind independently of its boundary-word role. |
| `CC-A6PWMR-3` | A conforming practitioner **MUST** name the exact related object and **MUST** split several current related objects into separate claims. |
| `CC-A6PWMR-4` | Before every positive direct relation, a conforming practitioner **MUST** establish two independent premises: (1) the exact `RelationKind` resolves through a direct rule or applicable relation-declaration episteme to participant meanings, obtaining condition, applicability, and defining source; and (2) a separate case fact says that the exact participants at the exact extent satisfy that condition. The practitioner **MUST** keep the obtaining fact distinct from its assertion and evidence; an object's identity or a record's presence alone is insufficient, while its content may support the claim under the applicable rule. A failed positive test within the rule's applicability returns `factually unsupported`; an unavailable deciding fact returns `missing-information`; a case established outside applicability returns that rule's inapplicable result. Only an absent governor returns `missing-governor` with exact participants, proposed predicate, affected use, and absent definition. A future pattern or declaration need is named only when identifiable. |
| `CC-A6PWMR-4a` | Before every governed negative direct-relation claim, a conforming practitioner **MUST** recover the current exact governor, its applicable negative or non-obtaining criterion or closure basis, and separate case facts satisfying that basis at the exact extent. The practitioner **MUST NOT** infer negative polarity from failure or unavailability of the positive fact and **MUST NOT** individuate an obtaining relation occurrence. |
| `CC-A6PWMR-5` | A conforming practitioner **MUST** keep claim subject, modality and exact extent, polarity, and recovery or support state independently recoverable whenever any can change the answer and **MUST** check `WMR-WF1`. The practitioner **MUST NOT** require the four labels when a simple sentence already carries the only material reading. |
| `CC-A6PWMR-6` | A conforming practitioner **MUST NOT** substitute a direct subject-relation claim, `A.6.1` operation-application binding, local `A.15.PROD` or `A.6.RCD` claim, and non-assertability result for one another. |
| `CC-A6PWMR-7` | A conforming practitioner **MUST** return first the shortest ordinary direct sentence or reason-specific non-assertability result defined in section 4.3 and **MUST** open additional apparatus only for a named receiving use. |
| `CC-A6PWMR-8` | Authors and modelers **MUST NOT** introduce a universal input, output, result, outcome, deliverable, handoff, evidence, production, actual-filling, status, work-result, or transformation-result kind or relation. This checks `WMR-I1`. |
| `CC-A6PWMR-9` | A conforming practitioner **MUST NOT** infer an actual relation or transformation solely from a plan, label, record or representation being present, or from adjacency or a shared referent. Claims and grounds in that material are assessed under the direct rule. This checks `WMR-I2`. |
| `CC-A6PWMR-10` | For a composition-dependent claim, a conforming practitioner **MUST** preserve independently grounded claims and **MUST** return either the direct composition result or its exact blocker without stopping those independent claims. |
| `CC-A6PWMR-11` | When a sentence deliberately asserts a particular performed Work, a conforming practitioner **MUST** recover its A.13 basis and independent A.15.1 admission at the needed granularity. The practitioner **MUST** retain a supported neighboring object or blocker when admission is unresolved. Apply F.6 only for precise assignment-bound attribution; after admission, the practitioner **MAY** apply F.18 for a needed durable name. Neither supplies Work admission. |
| `CC-A6PWMR-12` | When entity-identity inception is current, a conforming practitioner **MUST** state the exact candidate entity or pre-inception basis, exact Work question, and receiving use, apply A.15.PROD, and use only the resulting local inception claim or blocker. The practitioner **MUST NOT** substitute Work, change, rendering, an identity rule, or proximity for that result. |
| `CC-A6PWMR-13` | When evidence, warrant, assurance, gate, currentness, publication, or reliance is current, a conforming practitioner **MUST** apply the relevant check or use to the exact direct subject claim, exact `A.6.1` application binding, exact local `A.15.PROD` or `A.6.RCD` claim, or exact non-assertability result and **MUST** use only the separately established result. For non-assertability, the practitioner **MUST** distinguish `factually unsupported`, `missing-information`, `missing-governor`, a known rule's inapplicable result, and `missing-substrate` under section 4.3. A missing subject rule and unavailable constructor semantics retain their different repair questions; neither inapplicability nor missing case evidence justifies inventing a relation kind. The practitioner **MUST NOT** treat support or assurance as polarity, obtaining, or a field of the relation-bearing claim. |

### A.6.P.WMR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Boundary word as kind | `Input`, `Output`, `Result`, or `Handoff` is used as the entity kind. | The repaired claim restores the entity's admitted kind, related object, direct relation, orthogonal claim dimensions, and governor. |
| Plan as actuality | A planned filling, work-package row, or intended deliverable is treated as an actual participant or result. | Intended relation content stays under the plan; actuality opens only from direct obtaining facts. |
| Binding as production | An operation result binding is treated as proof that work produced or constituted the bound entity. | The repaired claim states only the binding; `A.15.PROD` opens separately when exact production facts make that question current. |
| Result record as result relation | A report, log, or evaluation-result episteme is treated as the changed entity, work, or direct subject relation. | The repaired claim identifies the episteme and its claim content, then keeps any work, change, measurement, or evaluation relation separate. |
| Local id used as ontology | A project id or assertion id is cited where the `RelationKind`, obtaining predicate, relation-declaration episteme, or `SubjectPatternLocator` is needed. | Name the token and its exact reference scheme or resolver; keep any occurrence, assertion episteme, and local id separate. When no current exact predicate source exists, return the established `missing-governor` result. |
| Missing governor hidden by hypernym | A broad word makes an unresolved relation look complete. | The repaired result records exact participants, proposed predicate, obtaining question, affected use, and absent definition, applicability, or occurrence rule; a future definition need is optional. |
| Composition by proximity | Shared work, time, flow, or referent is treated as transformation composition. | The repaired result keeps independently identified transformations and returns the exact composition blocker. |

### A.6.P.WMR:9 - Consequences

- Practitioners retain short ordinary sentences while downstream users can recover the exact relation and its orthogonal claim dimensions.
- Method, plan, work, operation application, actual change, production, evaluation, delivery, acceptance, transfer, and receiving use remain independently inspectable.
- Local missing-governor blockers reveal where subject ontology is absent without forcing a new public kind.
- One compressed phrase may split into several claims; that is the cost of preserving different obtaining conditions and subject patterns.

### A.6.P.WMR:10 - Rationale

Boundary words describe a relation position only relative to an exact object. Treating them as entity kinds or universal relations erases the exact predicate, current facts, and subject assertion that determine obtaining. The three-question ordinary method restores the thing, related object, and direct verb or stop first; two conditional assurance questions expose claim dimensions and the formal predicate definition only when those distinctions can change or check the answer.

The worked-case relation tokens have meaning under their supplied project declarations. They neither add those kinds to FPF nor establish any occurrence by being named. Durable naming under F.18 follows recovery of the object and its identity basis.

Stop at the sufficient truthful result. Reuse a direct predicate when it answers the question; keep a compound claim local when no reusable definition is needed; develop such a definition only for its receiving uses. A missing rule remains a bounded definition question, rather than a reason to introduce a universal result relation.

### A.6.P.WMR:11 - SoTA-Echoing

These sources answer different practice questions. Provenance, metrology, and project-planning vocabularies expose useful distinctions and recurrent compression risks; none admits an FPF kind, makes a work or participant relation obtain, or replaces the three-question ordinary recovery and its two conditional assurance questions.

The three-question ordinary recovery, two conditional assurance questions, and four-exit architecture are an FPF-scoped synthesis hypothesis for one claim whose exact thing is known while its work or method boundary relation or one material claim distinction remains hidden. The cited traditions neither establish that architecture nor authorize it outside this boundary. The synthesis reopens if repeated subject practice yields a stable direct governor that replaces a branch, or if a trigger case cannot close through one of the four exits without new ontology.

| Source and contribution | Adopted or adapted move in A.6.P.WMR | Rejected overread and practical effect |
| --- | --- | --- |
| W3C, [*PROV-DM: The PROV Data Model*](https://www.w3.org/TR/prov-dm/) and [*Constraints of the PROV Data Model*](https://www.w3.org/TR/prov-constraints/), W3C Recommendations, 2013. Mature provenance-model lineage, not current work ontology. | **Adapt.** The distinction between usage and generation is preserved while sections 4.3, 5, 5.1, and 5.7 recover the exact FPF subject-use, operation binding, entity-identity inception, production, publication, and receiving-use claims separately. | A provenance activity, `used` or `wasGeneratedBy` record, or recorded time makes none of those FPF relations obtain by itself. PROV generation is not imported as a universal FPF production or result relation. |
| JCGM, [*International Vocabulary of Metrology, VIM 2.9 — measurement result*](https://jcgm.bipm.org/vim/en/2.9.html), official VIM3 online entry. Measurement-result subject comparator. | **Adopt and adapt.** The measurand, attributed values, uncertainty, and relevant-information discipline are retained; sections 4.7 and 5.1-5.5 therefore keep instrument or operation output, measurement-result episteme, diagnostic finding, evaluation verdict, and downstream subject effect separate. | A measurement-local input or output role does not create a work input/output kind, and a value, indication, report, or verdict does not become the changed entity or downstream outcome by the word `result`. |
| Project Management Institute, [*PMI Lexicon of Project Management Terms*, version 5.0](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf), January 2026. Planning and work-name vocabulary comparator. | **Adapt.** The Lexicon's distinct activity, WBS, work-package, output, result, and deliverable terms expose the metonymy repaired in 4.8 and the machining, Car 42, and authoring cases. A WBS or Work Package remains plan or assignment content until A.15.1 occurrence grounding is present. | A named plan element, scheduled activity, expected deliverable, output, or result proves no dated Work occurrence admitted under `U.Work`, enacted method, actual participant, production, delivery, acceptance, or downstream effect. The source vocabulary is not FPF ontology. |
| PeopleCert, [*PRINCE2 Project Management Foundation (Version 7)*](https://www.peoplecert.org/browse-certifications/project-programme-and-portfolio-management/PRINCE2-2/prince2-7-foundation-3579), official public Foundation certification/product page. Broad-practice comparator only. | **Bounded reference only.** The page establishes the public Version 7 offering and describes seven recurring project-management practices. It does not expose the detailed product, product-description, activity, or Work Package distinctions, so A.6.P.WMR does not attribute section 4.8's morphology or work-name rule to this page. | Neither Version 7 status nor broad practice language makes any planning entity, activity, Work Package, performed work, production, delivery, acceptance, or receiving-use claim obtain. An exact official locus is required before detailed product-planning distinctions can become load-bearing source evidence. |

For a practitioner encountering one of these standard vocabularies, the action is the same: preserve its bounded provenance, measurement, or planning meaning, then ask what exact thing is named, relative to what exact object, and what direct verb or stop is justified. Open the two assurance questions only when a material ambiguity or receiving use needs them. The standard term is evidence about likely interpretation, not the direct relation's governor.

Revisit the affected comparison when its source changes the relevant meaning: PMI activity, work-package, output, result or deliverable distinctions; an official PRINCE2 source proposed for a detailed planning claim; JCGM's measurement-result boundary; or provenance usage and generation semantics. Recheck the dependent adaptation rather than treating an unchanged source title as sufficient.

### A.6.P.WMR:12 - Relations

- **Specializes:** `A.6.P` for the focused method-and-work boundary-word recovery case.
- **Entry condition:** apply this pattern while a method-or-work boundary relation or a material claim dimension remains hidden. E.10 and E.10.ARCH can help locate that problem; they need not be reread when the object, direct relation and applicable rule are already clear.
- **Uses:** `A.6.RCD` when exact participants are known but no direct relation closes the receiving claim; `C.2.P` for epistemic source expression and source-to-use recovery before the exact relation involving a Work occurrence is recovered.
- **Coordinates with:** `A.3.1` method identity and generic participant meanings; `A.3.2` method descriptions; `A.6.1` actual operation applications and declaration-local bindings; `A.15.1` dated work; `A.15.2` intended work and plans; `A.15.3` planned fillings; `A.3.4` actual bounded change; and `A.15.PROD` production-work, entity-identity-inception, and production-completion recovery.
- **Durable naming condition:** apply `F.18` only after the exact governed value from a direct subject relation, exact `A.6.1` application binding, or exact local `A.15.PROD` or `A.6.RCD` claim, together with its receiving use, is recovered. The fourth family—an exact non-assertability result with its section 4.3 reason—does not authorize durable naming of the attempted relation. `Missing-governor` names a future pattern or declaration need only when one is identifiable; `missing-substrate` retains its separate constructor-semantics question. A durable performed-work name additionally requires the `A.15.1` occurrence basis.
- **Neighboring assertions:** state the recovered measurement, evaluation, commitment, delivery, acceptance, transfer, resource, premise, source-use, Transformation, evidence, assurance, publication, gate, decision, or Work claim under its exact predicate; cite its `SubjectPatternLocator` only when the locator is needed.
- **Boundary:** A.6.P.WMR is the pattern for the recovery method and ordinary direct sentence. It does not define direct subject ontics, create the work occurrence, make an operation binding obtain, admit a relation kind, supply evidence or warrant, or decide downstream reliance.

### A.6.P.WMR:End
