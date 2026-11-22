## NSTD.8 - Design a Narrative Learning Route for Reconstruction and Use

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** a narrative learning route and the source relations learners need to reconstruct and use.

### NSTD.8:1 - Problem frame

Use this method to design or assess a narrative learning route for a complex subject. Start from what learners will need to reconstruct or do. A source publication may already serve a lookup or professional decision directly.

Begin at one consequential transition. What question is open, what material has the learner encountered and what will the next task require? Inspect the support available there. A missing prerequisite can be visible in the material. To find out how someone used it, examine a suitable earlier attempt or arrange one if the question warrants it.

Choose the learning order from the learner's next action and intended later use. The source organization can support lookup, a first explanation, or a comparison of what several cases share. When later work requires choosing among similar cases, a route that names the topic for every task can leave that choice unpractised. Keep the source organization available and select the comparisons, mixed tasks, or later returns that the learning purpose requires.

A learner may remember the examples and lose the relations needed to use them. In a technical lesson these can include the architecture, the conditions of a proof, when to select a method, where to verify a claim or how to improve a result.

A usable route makes the material available where a learner needs it to explain a relation or perform the next task.

### NSTD.8:2 - Problem

A learning narrative uses sequence, examples, repetition, analogy and motivation to help the learner reconstruct and use source ideas. Those choices can also conceal a prerequisite or make an illustrative route appear to be the only way to perform a method.

A topic heading can tell learners which method to use. Success inside that block leaves open whether they could choose among methods without the heading. Select cases that reveal the relevant similarities or differences, and supply enough material for learners to work with them. Arrange the order of exercises and the reasoning within each exercise for the actions they support.

### NSTD.8:3 - Forces

| Force | Tension |
| --- | --- |
| Learning order and source order | A sequence for teaching can differ from a publication’s organization, a proof’s dependencies or the architecture being explained. |
| Reference and learning use | Keep source modules accessible for lookup. Use their grouping for teaching when it supports the learner’s next action. |
| Shared basis vs distinguishing cases | A block can make a common relation visible across instances; a close comparison or mixed task can expose differences between similar alternatives. The learner's missing operation determines which arrangement is useful. |
| Coverage and later retrieval | Encountering every topic once leaves open what learners can retrieve at the time of later use. |
| Engagement and reconstruction | A learner may enjoy an analogy and still miss the relation it illustrates. Ask what they can reconstruct when that is the learning goal. |
| Local teaching and authority | A lesson trial can show what particular learners did. Authority for a subject claim comes from its relevant source or practice. |

### NSTD.8:4 - Solution

Design the transition the learner needs and connect it to its next use. If learners must interpret unfamiliar material, teach them how to develop and compare interpretations through NSTD.9. When independent selection is the aim, leave that choice to them and give them an opportunity to use feedback on their reasoning. For story construction, use NSTD.10. A workable scene under fixed premises may fulfil the assignment. Let learners revise the scene under a changed premise when that is part of what they must learn. A narrative lesson on a proof or technical method takes its operations and criteria from that subject.

A course team may want a note connecting several lessons, comparing versions or keeping their source relations traceable. Use the fields its work needs.

```text
LearningNarrativeRoute@Context:
  learnerUse:
  sourceRelationsNeeded:
  unfoldingStructureRefs?:
  demonstrativeSliceRefs?:
  sourceArchitectureRef?:
  organizationOfLearningEpisodes:
  reasoningAndOrderWithinEpisodes:
  interleavingPlanRefs?:
  spacingOrRetrievalScheduleRefs?:
  recurringExamplesOrPrompts?:
  whereToReturnToTheSource:
  learnerReconstructionTaskRefs:
  applicationTaskRefs?:
  intendedUseOfInterestOrMotivation?:
  routeEvaluationIfNeeded?:
  improvementLoopInputRef?:
  learningPublicationCarrierRefs:
  choicesSuppliedByTopicLabels?:
  limitsOnWhatTheResultsShow:
  refreshCondition:
```

A maintained course may have separate lessons, slides, exercises and recordings. Link them to the source ideas and learner tasks they serve. The size and publication form depend on the teaching work.

When teaching an unfolding sequence with several permissible paths, decide what the learner will have to do with it. To follow one prescribed path, learners may need only that path and its conditions. To choose a path, they need to recognize the circumstances that change the choice and the alternatives or stopping points then available. To design such a sequence, they also need to practise deciding which circumstances and alternatives to represent. A route note can link the wider structure and the demonstrated path when that helps maintenance.

These questions can guide planning or the examination of an existing route. Return to the affected question when an attempt supplies new information.

| Design question | Useful result | Failure it addresses |
| --- | --- | --- |
| Which source ideas will the learner need? | The relations and operations needed for later reconstruction or application. | A memorable example with no usable connection to the subject. |
| Does the source organization suit learning here? | A reasoned choice of learning order, with the source organization still accessible. | Copying a reference topic map without considering the learning task. |
| What must be available before the next task? | A sequence or usable return that supplies the prerequisite at that point. | Requiring an operation before its necessary relation is available. |
| Which comparison or choice does the learner need? | Select cases with enough material to see the shared relation or distinguishing condition. HCD.10:4.5 helps choose an order for human practice when that choice matters. | The relevant difference is unavailable, or the heading makes the choice for the learner. |
| Must learners retrieve the idea after a delay? | Compare an earlier demonstration with work after the relevant interval, under the help permitted then. Account for intervening practice that matters to a claim of retention. | Immediate recognition alone leaves later retrieval open. |
| How does an aid connect to the current question and next use? | A meaningful term, diagram, question or case with its relation recoverable. | Remembering the aid but not what to do with it. |
| What must the learner recover or perform? | A task whose response can show the relevant distinction or operation. | A report of satisfaction alone leaves capability open. |
| What result would change the route? | Use an applicable NSTD.6 assessment to retain a sufficient version or choose a worthwhile repair. | A change is credited with improvement before its effect on the relevant quality is established. |

Start from the intended task and the preparation learners can use. When people must notice a common relation or distinguish similar alternatives, HCD.10:4.5 helps choose whether to retain a block, place cases side by side or mix further cases for practice in choosing. Make the deciding relations accessible in the narrative. When the basic operation itself needs explanation or supported practice, use the subject method and §4.1.

Arrange an episode around one action or connected attempt. A two-sentence comparison can expose the difference between two alternatives. Applying a method to a system may need several pages and cases. Keep the information needed for the action accessible together.

Order the episodes and the reasoning within them. A reader should be able to recover the question the next claim addresses, the premise it needs or how the next case changes the account. Alternate within an episode when the comparison calls for it. A mixed sequence of tasks can contain a sustained explanation for each.

An author can open a question, develop it through intervening cases and return to it later. Let the learner find the earlier question again. Make its needed relation accessible before a task requires it. Section 4.1 helps distinguish a preparatory attempt from a missing connection or support.

When people need later access to what they learned, use HCD.10:4.4 to choose a suitable interval. Decide separately what they must retrieve and what support they may use. Keep the cases of a needed comparison jointly accessible during that task, even when practice resumes after a delay. To judge actual use, examine the learner’s response under those conditions (§4.1 and NSTD.6).



#### NSTD.8:4.1 - Check what the learner must do next and what help is available


Connect the teaching material to the question at hand and to the use that follows. What can a learner do with this example, diagram or exercise, and where will that matter? A question, caption, worked example, short transition or later return may supply the connection. Check the endpoints of a repeated term or a diagram arrow when its meaning is unclear.

Examine what is available by the time of the next task. Identify what this audience can already use, what the route has introduced, which questions remain open and which prerequisites the task needs now. An overview or a link can supply a missing relation if it makes that relation usable at this point. Inspect the material for a design judgement. Use a learner’s attempt when the question concerns what that learner actually did.

Compare the work the author was commissioned to teach with the task the finished narrative actually gives the learner. Read the whole narrative with that difference in view. When must the learner choose something the storyteller has already chosen? Trace where the learner gets the grounds for making that choice and where the task lets them make it. If all the episodes fit together but the design of the procedure is still missing, use EXD.Reference:3 to develop that explanation from the subject practice. When the goal is to explain one incident or perform one specified operation, its own story may already suffice. Use EXD.6:4.1 to check the complete account against either goal. Read the caption, the exercise issued on its own and any help the learner normally receives. A heading that names a suspected cause supplies the hypothesis. The learner might still design the test. A supplied test can leave its interpretation open. Credit each decision the learner made. If both forming explanations and selecting evidence are commissioned, give the available observations and let the learner make both choices before showing the worked answer.

Choose the continuation that fits the transition.

- **The connection is missing.** Show how the block or aid bears on the current question and the next use. Correct a misleading diagram edge or a link to the wrong passage.
- **The task needs support that is absent.** Check the expected prerequisite and permitted help. Supply the relevant contrast, map, worked operation, recap or accessible representation, or introduce it earlier. Preserve the subject relation the learner must use.
- **The initial attempt prepares subsequent instruction.** A bounded problem can bring out alternatives before the explanation. Keep those attempts available and use the subsequent teaching to compare and resolve them. A later response can establish what the learner then did. To determine how the preparation contributed, use evidence that distinguishes its contribution, such as an applicable comparison.

A supported initial case can help a learner form the distinction. To teach the learner to select what a whole narrative must explain, give them the material and the next reader’s question. Before suggesting the units or a plot, let them decide which changes belong to one episode, which differences the telling must preserve and why. A suggested grouping can still leave the order of disclosure or its justification for them to choose. Use their attempt to show what each choice lets the reader infer and let them repair a consequential loss. Earlier work can show what a learner already does with the permitted help. Choose grouping, interleaving, spacing and retrieval for the particular action and time of later use.

To assess first recognition, preserve the response before supplying the deciding cue. State which help was permitted, what the learner used, what the source supplied and what prior expertise matters to the claim. A teacher-supported correction can satisfy a task that allows that help. An expert’s successful reconstruction and a novice’s difficulty may both be accurately reported. If the novice’s difficulty matters to a repair, use evidence that addresses it.

In NSTD.6, NarrativeRenderingEpiplexity applies C.2.8’s ExtractableStructuralInformation to a narrative account, its expression and an observer. Ask which selected relations this observer could correctly recover under the stated conditions. Once those relations support the task, adding others can increase effort without improving use. A walkthrough can locate a missing relation or available help. For a claim about experienced human effort, identify the person, segment, timing and means of measurement. Learning, retention and transfer have their own evidence.

After a change, recheck the affected connection and what the learner needs at the next task. Retain material that already works with the intended support. For a proposed improvement, E.23 compares the useful result, the costs and the qualities to protect. A shorter explanation or an extra diagram earns its place through what it changes for this use.

Select a task that can reveal the outcome in question.

| Task depth | Example task | What it tests |
| --- | --- | --- |
| Recognition | “Which method addresses this difficulty, and what tells you so?” | Which conditions of use the learner recognized, given the cues available. |
| Reconstruction | “Rebuild the route from the source, forces and solution to the point where you would use another method.” | Which source relations the learner reconstructed. |
| Transfer | “Apply the same reasoning to a different domain case.” | What the learner can apply under the changed conditions. A claim about transfer from earlier learning also needs its earlier basis. |
| Boundary | "When would you use another method, and which one?" | Whether the learner can select a useful alternative. |
| Repair | “Given this NSTD.6 assessment, choose the smallest change that would remedy the loss.” | Whether the learner can use the assessment to select a sufficient repair. |

Keep a story, rhythm, example or analogy when it serves the learning task. If a learner remembers it and misses the relation, check how the device, prior knowledge and available support bear on that difficulty before changing the material.

A short attempt or an earlier account of a learner’s difficulty may answer a local question. For a comparison across runs, preserve the versions, learners, task, assistance and result needed to interpret it. Seek further observations when they could change a conclusion enough to justify obtaining them. To claim that the route evolved through repeated operation, use B.4.

For improvement across runs, use a suitable NSTD.6 assessment of the affected version. E.22 helps define the intended benefit, minimum acceptable result, qualities to protect or evidence needed when any remains unclear. Use E.23 to select and compare a worthwhile change to the content, order, tasks, material, engagement or evaluation. Use G.11 when changed sources, learner observations, teaching results, generated practice or a new FPF edition could alter the route’s basis. B.4 addresses a claim that the route evolved as a whole through repeated operation.

### NSTD.8:5 - Archetypal Grounding



#### NSTD.8:5.1 - Worked learning route: FPF onboarding


A seminar, tutorial or exercise sequence could use the design below. Each teaching move prepares an identifiable learner action.

```text
LearningNarrativeRoute@FPFOnboarding:
  learnerUse: select and apply one FPF pattern under the conditions of a new case
  sourceArchitectureRef: the pattern language, its organization of source patterns, and the collected FPF publication
  sourceSpineRefs:
    - `EntityOfConcern`
    - problem frame
    - forces
    - solution as condition-bound move
    - conformance and checking
    - neighboring exits
    - quality and improvement loop
  unfoldingStructureRefs: A.22.CGUS when the route teaches unfolding from source to next use
  demonstrativeSliceRefs: first pattern-use route through one selected project case
  learningRouteArchitectureRule: revisit one pattern through several cases, keeping its source organization available
  learningStepOrder:
    - failed ordinary use
    - recover object of concern
    - read forces
    - choose solution move
    - check the limit of this use and select a neighbouring method when needed
    - use the assessment to repair one inadequate result
  interleavingPlanRefs:
    - return to `EntityOfConcern` after forces, solution, and quality checks
    - mix cases requiring a choice among the newly introduced and earlier methods
    - revisit source-return boundary in examples from at least two domains
  spacingOrRetrievalScheduleRefs:
    - short delayed retrieval at the start of the next session
    - choose among neighbouring methods after intervening material
    - final transfer task with no block label
  reconstructionTasks:
    - name the source pattern section behind each story beat
    - choose the governing pattern for a new case and use it to produce the result the case calls for
    - state one source-return condition
  useOfEngagement: the failed-use story introduces the problem. A claim about an actual failure needs its own basis.
  evaluationRouteRef: `NSTD.6` learning-route rows
  improvementLoopInputRef: `E.23` when a comparison identifies a worthwhile improvement
```

Here an initially unsuccessful attempt can prepare the discussion. Use the attempted alternatives to show which object the next move concerns and why the other choice would leave this question open. Before asking learners to choose between neighbouring methods, check whether they can access the methods and their distinguishing condition. If a contrast is missing, supply it or make the relevant source accessible. Once it is available, a mixed case can leave the choice to the learner.

For example, NSTD.2 changes presentation order while preserving the needed relations. NSTD.3 examines a connection asserted by an account. Give learners the Readme incident log and the sentence “the change caused the failure.” Ask whether placing the two events in chronological order would settle the sentence, and what the repair would need to establish.

Suppose a learner answers, “Put the change before the failure, so the cause is clear.” The answer gets the dates in order and infers cause from their order. If the necessary distinction was unavailable, explain it and work through the two claims. If the attempt was part of the preparation, use the answer in the ensuing instruction. If both methods were already accessible, return to what the log establishes. A later mixed case can test whether the learner recognizes a new connection claim without a supplied choice.

Connect a later diagram or recap to the next task. A wrong figure link can often be corrected locally. Inspect the new link to establish where it leads. To assess what learners can now recover, use evidence of their work with the revised material and the intended help. The answer above is part of the design example.

For a seminar, add timing, facilitation notes and complete exercises suited to the participants and the intended next use.



#### NSTD.8:5.2 - Worked learning route: repair topic-blocked practice


An engineering team wants a course in narrative methods for engineering explanations. Participants will select and use these methods when explaining designs, incidents and project decisions. Their first outline groups practice by topic:

```text
Lesson 1: all source-structure intake.
Lesson 2: all ordering rules.
Lesson 3: all viewpoint and agency.
Lesson 4: all engagement.
Lesson 5: all evaluation.
```

The headings identify the kind of problem in each block. This can support first practice. In an unfamiliar incident the learner may have to choose whether to check the source, reorder the account, change viewpoint, revise an expressive device, examine how it was generated or test a claimed connection. The blocked exercises alone leave that selection open.

The team could retain the topic map and teach the choice through the following sequence.

```text
LearningNarrativeRoute@NarrativeMethodsForEngineering:
  learnerUse: engineer selects and applies narrative methods to explain different project situations
  sourceArchitectureRef: NSTD topic map and source pattern bodies
  sourceSpineRefs:
    - selected source structure
    - ordering rule
    - viewpoint and agency split
    - engagement boundary
    - narrative rendering quality row
    - where to verify a claim and which practice can answer an open question
  learningRouteArchitectureRule: spaced interleaving around recurring project cases
  learningStepOrder:
    - one motivating project failure
    - source-selection repair
    - different project failure requiring ordering repair
    - return to first failure and add viewpoint risk
    - choose a narrative method in a mixed exercise and use it to repair or explain the engineering account
    - delayed retrieval of source-return boundaries
    - produce an explanation of an unfamiliar engineering case using the method the learner selects
  interleavingPlanRefs:
    - once an earlier method is familiar, mix it with a current method when learners need to distinguish them
    - adjacent failure modes are compared side by side
    - examples rotate across FPF seminar, architecture explanation, homotopy explanation, generated carrier, and live commentary
  spacingOrRetrievalScheduleRefs:
    - after the first session, open a later session with an unlabelled retrieval task on an earlier case
    - recall the object of concern, needed source and appropriate method at increasing delays
    - repair an earlier inadequate result after new material intervenes
  limitOfPractice: a topic-labelled exercise supplies the method name. Independent selection needs a task that leaves it open.
  evaluationRouteRef: `NSTD.6` rows for transfer, source return, and learner reconstruction
```

The NSTD topic map remains available for lookup. Returning to the methods under different cues lets an engineer practise distinguishing source, order and viewpoint problems. To teach engineering design itself, use the relevant engineering operations and a task that calls for them.



#### NSTD.8:5.3 - Worked learning route: homotopy explanation


```text
LearningNarrativeRoute@HomotopyIntro:
  learnerUse: learner distinguishes intuitive deformation picture from formal definition and proof boundary
  sourceSpineRefs:
    - topological space
    - path
    - homotopy relation under constraints
    - invariant
    - example and counterexample
    - proof-status return
  learningStepOrder:
    - image cue
    - show which space the deformation must stay inside
    - return to the formal definition of a continuous deformation
    - example
    - counterexample
    - reconstruction task
  reconstructionTasks:
    - identify the space in which every stage of the deformation must stay and a move that this excludes
    - explain why the drawing alone cannot establish that the loop contracts in that space
    - justify one claim using the formal definition and a relevant invariant
  useOfEngagement: the picture introduces the question. The definition fixes the allowed deformations.
  evaluationRouteRef: `NSTD.6` rows for ordering, language-state precision, and source return
```

For example, draw a loop winding once around a missing point in the plane. Ask whether a continuous deformation inside that space can shrink the loop to a point. Its winding around the missing point prevents this. Fill the point back in and the loop can contract in the full plane. A learner who remembers the drawing can be asked which change in the allowed space changes the answer and why. The formal result supplies the criterion for judging their explanation.



#### NSTD.8:5.4 - Worked learning route: using this pattern language


One short course uses an FPF seminar, a franchise continuation and a homotopy explanation, then turns to live commentary for a new application. The table shows the instructor which methods each case could teach.

| Step | Case | Methods for the instructor | Question for the learner |
| --- | --- | --- | --- |
| 1 | FPF seminar | NSTD.1, NSTD.8 | Which relations from the source will participants need after the seminar? |
| 2 | Franchise continuation | NSTD.1, NSTD.2, NSTD.3, NSTD.7 | What does the existing canon establish, and what can the author propose or invent for the new events? |
| 3 | Homotopy explanation | NSTD.2, NSTD.5, NSTD.6 | Which step needs a definition or proof beyond what the analogy supplies? |
| 4 | Live commentary | NSTD.3, NSTD.6, G.11 | Which claims are supported now, and which would change with a later observation or official correction? |

When learners see the method names, their explanations can show how they use those methods. To assess independent selection and repair in a new situation, give the new case without its method names or an equivalent cue. Ask them to choose, explain the relevant condition and make the repair. Record what help the task allowed and what they used.






#### NSTD.8:5.6 - Evaluating the learning route


Select the task for the intended outcome. Immediate reconstruction, delayed retrieval, discrimination between cases and application to a new case call for different observations. A present response may complete an account of what a learner reconstructed. For durable independent use, compare an earlier demonstration with appropriately delayed work under the permitted support, accounting for relevant intervening practice. Vary the case when the claim includes use under that change.

Use NSTD.6 to distinguish a judgement about the design from the work of a particular learner. For a reading result, identify the task, observer, material, conditions and help relevant to the claim. Account for prior preparation when it affects the inference.



#### NSTD.8:5.7 - Connecting route design to publication and improvement


For framework entry use E.11, for the publication form E.17, and for a separately usable audience unit E.17.AUD. NSTD.5 helps choose an expressive device when interest matters. NSTD.6 evaluates the route for its intended use. E.22 and E.23 support a proposed improvement, and G.11 a review after a relevant change. Keep the design detail a one-off explanation or maintained course needs.

An FPF seminar or tutorial can connect the object of concern, precise relations, pattern bodies, DPF authoring, architectural synthesis, evaluation, improvement and return to sources. The teaching order serves the learner. For reconstruction, ask participants to recover one pattern-use route and its basis. Use the framework itself to establish its architecture.

In the homotopy mini-course, ask learners to identify the permitted space and explain the two outcomes in §5.3. A drawing can introduce the problem, and the mathematical comparison can expose a missing condition. Use the learner’s own explanation to judge what they reconstructed under the support given.

An onboarding sequence could also use an FPF seminar, franchise storycraft and live commentary. Ask learners which source relations NSTD.1 helps recover in each case, which further method each problem needs, and why NSTD.6 evaluates a particular rendering and use. For use in a different setting, give learners the new task and the help allowed there. Prior work can already show a learner performing that task. To attribute the performance to transfer from earlier learning, establish the relevant earlier basis and what the new conditions required.

NSTD.7 helps examine generated teaching material against the source and the intended task. Use NSTD.6 for an assessment that admission or another use needs. C.35 addresses use of the generated material in architectural work.

Distinguish versions when comparing repeated teaching or maintaining materials. The following optional note is useful when the comparison needs these details.

```text
LearningNarrativeRouteVersion@Context:
  routeRef:
  sourceSpineVersionRef:
  learnerRoleRef:
  learningStepOrderingRule:
  carrierRefs:
  reconstructionTaskRefs:
  evaluationResultRef:
  observedConfusionOrTelemetryRefs?:
  changedSliceSincePreviousVersion?:
  refreshCondition:
```

For a comparison, identify which materials and order learners encountered and what differed. Compare the affected outcome with a suitable baseline, including any qualities to preserve, before claiming a gain. If no one tracked a slide change, other evidence may establish which version was used. Review the teaching that depends on a materially changed source.

The following example plan connects subject content, the immediate teaching move and a later use. Adapt its timing and returns to the learner's task.

| Source relation or operation | Immediate teaching move | Later practice when needed |
| --- | --- | --- |
| Pattern entry condition | Practitioner incident, contrasting case or failed-use example. | Return after two other cases and ask which method fits, without naming it. |
| Forces | Tension sequence, stakeholder conflict, or trade-off map. | Compare with a different pattern's forces in a mixed exercise. |
| Solution move | Demonstration, guided reconstruction or worked example. | Reuse the project case with a problem requiring another kind of repair. |
| Boundary and non-use | A counterexample or a case where another method is needed. | In a later session, ask learners to recall when to stop using this method. |
| Relations | Ask which neighbouring method supplies the outstanding contribution. | Mix cases requiring different choices. |
| Quality and improvement | Diagnose an inadequate result and select a repair. | Revisit it after intervening work and ask learners to revise the affected part. |

The last column gives possible later work when the goal includes delayed retrieval or method selection. A response can establish what a learner did at that time and with that support. For a learning claim, establish a change from earlier capability. To credit the route, also establish how it contributed to that change.

Different courses can use the same design questions.

| Course | Source material | Possible narrative devices | What to examine |
| --- | --- | --- | --- |
| FPF onboarding | Pattern entry, object of concern, forces, solution, relations, checks and improvement. | Practitioner problem, contrasting uses, recurring source question. | How the learner chose an applicable method and reconstructed a pattern-use route. |
| Mathematical explanation route | Definitions, examples, theorem prerequisites, proof-status boundaries. | Analogy, diagram story, dependency sequence, counterexample. | Learner marks where analogy stops and returns to formal statement. |
| Architecture explanation route | Candidate structures, characteristics, decisions, trade-offs, telemetry. | Trade-off story, viewpoint over stakeholder role, decision-memory path. | Learner separates architecture description, decision, realized structure, and telemetry. |
| Generated teaching material | The source relations and the intended learner operation. | Generated examples or slides examined through NSTD.7. For architectural work, C.35 also applies. | Compare the material with its sources for fidelity. A learner’s response can show performance on the task. To claim learning, establish a change in capability. To credit this material, establish its contribution to that change. |
| Live debrief route | Event record, provisional interpretation, official correction, source return. | Recap story, tension order, role viewpoint. | Learner distinguishes observation, inference, prediction, and official update. |

A short teaching note can give one needed source relation, an order for explaining it, a reconstruction question and a way back to the source. For a maintained course, identify versions and retain the learner results that a promised comparison needs. Revise the parts for which a change is warranted.

Attendance, applause and satisfaction can tell an organizer about participation or reaction. To establish what learners reconstructed, examine which relation they can explain or apply, which boundary they recognize or how they choose a repair.

### NSTD.8:6 - Bias-Annotation

Learners may take a sequence of lessons or an analogy as the structure of the subject. Give them access to the source relations and show why the lesson uses this particular order.

Modular source publications support reference. Reusing the modules as lessons can leave learners with little practice choosing across them. When they need to distinguish cases, include a comparison. When they need to retrieve a relation later, plan its return and the support permitted then.

### NSTD.8:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD8-1` | The design names the intended learner action and the source relations it requires. |
| `CC-NSTD8-2` | The order serves the learner’s task, and the learner can reach the sources needed for it. |
| `CC-NSTD8-3` | The task lets the learner perform the action promised. For reconstruction, the required source relations can be recovered. For application, the learner can use them for the assigned decision. For design, the learner can select the relevant relations or test with the permitted help before seeing the author’s choice, and can justify the design if the commission requires its grounds. Judge an individual response from that learner’s work. |
| `CC-NSTD8-4` | Lessons, exercises and other learning materials make their needed source relations and tasks available at the point of use. |
| `CC-NSTD8-5` | The comparison supports a claimed improvement on the affected outcome, at acceptable cost and with protected qualities preserved. Use NSTD.6 for the assessment and E.22 or E.23 for the improvement work the case requires. |
| `CC-NSTD8-6` | Distinguish source organization, episode order and reasoning within episodes. The intended learner action determines what to compare, what should remain accessible together and what help is appropriate. For a spaced return, choose separately when it occurs and what learners must retrieve. |
| `CC-NSTD8-7` | At a consequential transition, learners can relate available material to the question and next use. Address a missing connection or prerequisite where it is needed. Follow a deliberate preparatory attempt with instruction that uses the attempted alternatives. |
| `CC-NSTD8-8` | Interpret first and assisted responses under the actual preparation and help. Ground claims about the source, learning and experienced effort in evidence of each. |

### NSTD.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Lesson order mistaken for the subject’s structure | The explanation presents one sequence or analogy as the architecture or order of proof. | Explain the teaching choice and give a usable return to the subject relation. |
| Reference order chosen without examining the learning task | The topic map is copied into lessons without checking what the learner must subsequently recognize, select or use. | Keep a source-aligned introduction when it supplies the needed support. Add contrasts, mixed selection or delayed retrieval when the intended outcome calls for them. |
| Fluent performance in labelled topic blocks | The label supplies the method choice that later work requires learners to make. | Examine an unlabelled or mixed case for selection. Use a suitable change to assess transfer and a suitable delay to assess retention. |
| Remembered examples mistaken for reconstructed relations | The learner can repeat the anecdote, while their command of the relation remains open. | Examine their work on a reconstruction or application task. Use NSTD.6 when an evaluation is needed. |
| Fluent paragraphs with a missing connection | The example reads smoothly, but the learner cannot relate it to the active question or later use. | Inspect the two passages and what is available at that point. If repair is wanted, restore the relation or the return to it. To judge the revised task in use, examine a suitable attempt. |
| Difficulty judged without its instructional purpose | A difficult transition is removed, or an unsuccessful attempt is credited with teaching the relation. | Supply a missing prerequisite. For a preparatory attempt, use its alternatives in the following instruction and check any claimed learning outcome. |
| A local revision described as evolution | One change to a slide is offered as evidence about the course across repeated operation. | Use NSTD.6 to assess a version, E.23 to compare a proposed improvement and G.11 for an affected change of basis. Use B.4 for a claim of evolution through repeated operation. |

### NSTD.8:9 - Consequences

The designer obtains a route connecting source material, available support and intended learner actions. It takes work to build those connections. Evidence of actual responses, retention and transfer costs time when a claim about them is needed.

### NSTD.8:10 - Rationale

Explanation, examples, attempts, feedback and later returns serve different learning aims. Keeping the source structure accessible lets the teacher vary their order while learners can still recover the subject on its own grounds.

A modular source corpus can support lookup and a first introduction while still leaving later selection unpractised. When learners must choose among similar methods without a topic label, the learning route needs those contrasts and selection tasks. When later retrieval matters, it needs an appropriate delay and return. The source organization remains available; whether the learning order should follow it depends on the task and the support already available.

### NSTD.8:11 - SoTA-Echoing

Mengelkamp and colleagues compared factual and inferential responses under different reading goals. Results for those goals varied across their two experiments, and readers’ estimates could exceed their performance. Georgiou and colleagues found that scrambling narrative clauses affected free recall much more than recognition. Hoffmann illustrates how scientific storytelling can sustain a tension and return to its source. Earlier work on practice supplies distinct grounds. Dunlosky and colleagues rated practice testing and distributed practice highly and discussed interleaving for suitable tasks. Rohrer and Taylor found advantages of spaced or mixed practice on later tests of the mathematics problems they studied. Kang reviewed how repeated encounters can be spaced and combined with testing.

[Noetel et al. (2022)](https://journals.sagepub.com/doi/10.3102/00346543211052329) reviewed multimedia design, including signalling, correspondence and pacing. Select the feature that addresses the learner’s difficulty. [Sinha and Kapur (2021)](https://journals.sagepub.com/doi/abs/10.3102/00346543211019105) compared instruction before and after problem solving, with substantial evidence from mathematics and physics. A preparatory task needs subsequent instruction that uses the attempted solutions. [Wesenberg et al. (2025)](https://doi.org/10.1016/j.cedpsych.2024.102328) showed in short units that a worked solution can also fit a misleading rule. Check whether an example distinguishes the intended rule. In [Krieglstein et al. (2025)](https://doi.org/10.1007/s10648-024-09980-0), the complexity of the first unit influenced the overall effort reported after a sequence of three. Identify the person, segment, timing and instrument when interpreting such a rating.

Apply these findings to the particular teaching aim.

- State the learner’s purpose before choosing the tasks. Curiosity, an examination, professional use and framework authoring can call for different responses.
- Compare a learner’s judgement of understanding with their reconstruction or application when the accuracy of that judgement matters.
- Give learners a way back to a needed source relation across a long narrative. Use a recurring prompt when it helps them recover that relation.
- For later retrieval, consider distributing practice and examine performance after the relevant delay, under the stated support.
- Where a topic label normally supplies the choice, compare similar cases or mix problem types to give learners practice selecting the appropriate method.
- Keep the source organization accessible for lookup. Retain its order when that supports a first introduction. Use a different order when later work requires a contrast, mixed selection or a delayed return.
- Preserve an open scientific question when current evidence leaves it open. The tension can itself be part of the teaching.
- Compare the relevant course versions and outcomes when claiming an improvement. A worthwhile change can improve an already adequate result.

Retain a source-aligned segment that already serves its purpose. A missing connection, an unsupported demand or an unpractised choice gives the designer a specific change to consider.

### NSTD.8:12 - Relations

For a human learning route, HCD.10:4.5 helps select grouping or mixing when the comparison and order matter. Keep the material learners need for that comparison accessible at the point of use. HCD.10:4.4 helps select a spaced return, the retrieval to practise and the help permitted there.


For the narrative and its source use A.6.3.NAR, E.6, NSTD.1 and NSTD.2. E.11, E.17 and E.17.AUD support entry and publication. NSTD.5 helps choose a device for interest or motivation. NSTD.6 assesses a particular narrative version for its intended use. Use E.21 when the object to evaluate is an edition of an FPF pattern. E.22 frames an open quality question, and E.23 compares proposed improvements. Use G.11 when a change in sources, learner preparation, task, practice, scheduling, edition or observations alters the basis for use. Use B.4 for evolution through repeated operation. [NSTD.Reference:9](09-nstd-reference-9---architecture-and-narrative-work-bridge.md) addresses source architecture, views and evidence about the realized structure. [NSTD.Reference:10](10-nstd-reference-10---semiotic-and-language-precision-bridge.md) addresses wording, cues, explanation and loss of precision. [NSTD.Sources:1](26-nstd-sources-1---source-use-and-refresh-map.md) helps trace changed teaching, memory or practice evidence to the parts of the course that depended on it. Use [NSTD.Reference:14](14-nstd-reference-14---refresh-the-affected-narrative-use.md) when changed observations of learner work could affect the route’s supported use. When a lesson lacks its subject account, obtain it with EXD.Reference:3. EXD.6:4.1 and HCD.19 help distinguish what the publication supplies, what the learner brings and what the issued task leaves them to do.

### NSTD.8:End
