## B.5.4 - Recognize a Reusable Concept in a Concrete Situation



> **Type:** Method-description pattern
> **Status:** Candidate
> **Normativity:** Normative unless marked informative

### B.5.4:1 - Problem frame

**Use this when** you understand a concept's explanation but cannot yet connect it to an unfamiliar situation. You need to interpret what is happening before you can explain it, construct a model or choose the next observation.

Begin with the question this interpretation should help answer. Identify what you can point to or describe, recover the relations a candidate concept requires, and construct their correspondence in this case. The first useful result is an interpretation with a consequence that guides the next action.

This requires an accessible domain account and enough background to understand it. If the concept itself is unfamiliar, obtain that explanation first. If the interpretation is settled and only a calculation remains, use the appropriate calculation Method.

### B.5.4:2 - Problem

A familiar textbook question supplies cues that an encountered situation may lack. Knowing what polarization means can coexist with being unable to use it while looking at water. Even recognizing the material leaves the surface, directions and relations to be identified.

The missing contribution is the passage from the encountered situation to a usable interpretation. A correct interpretation should make a difference to an explanation, prediction, construction or action.

### B.5.4:3 - Forces

- A concept directs attention toward particular relations, while the first description of a situation can obscure them.
- A sketch can expose a correspondence; a premature equation can leave its variables uninterpreted.
- A familiar example helps learning, while changed conditions reveal which relations the learner can recover.
- A useful interpretation depends on domain knowledge, whose acquisition may cost more than the immediate recognition work.

### B.5.4:4 - Solution

1. **Name the question.** Say what the interpretation should enable: reducing glare, explaining a changed reading, arranging compatible activities or choosing an observation. This determines which distinctions matter.
2. **Describe the situation at a useful scale.** Indicate the relevant region, objects, time and conditions. Separate available observations from your proposed explanation. Try another boundary or viewpoint when the first description hides an interaction.
3. **Recover the candidate concept through its relations.** Consult its explanation, examples and conditions. Identify its participants, how they are related, and a consequence that distinguishes its application from a plausible alternative. Use the domain account to supply knowledge omitted by a short definition.
4. **Construct the correspondence.** Point to what supplies each participant here and explain the relations between them. Use a sketch, gesture, annotated observation or short account. If mathematics helps, connect each variable or mathematical object to its interpretation and identify consequential simplifications.
5. **Derive and examine a consequence.** Work out what should follow in this situation. Vary one relevant condition and compare the resulting prediction with an available observation, counterexample or inexpensive trial. Where competing interpretations support the same sufficient action, keep that bounded answer.
6. **Return to the question.** Give the explanation, construction, action or next observation now supported. When a consequence fails, revisit the object boundary, relation, condition, representation or candidate concept that produced it. Identify the missing domain contribution if the available account cannot resolve the question.

The result can be an interpreted sketch and a next action. Record the reasoning when another participant or later use needs to recover it.

For capability assessment, separate the correctness of a supplied interpretation from the reader's ability to select and construct it. Give a consequentially changed situation before supplying its decisive conceptual cue; retain the references and assistance allowed in the intended work.

### B.5.4:5 - Archetypal Grounding

#### B.5.4:5.1 - Glare from water

You want to reduce glare in an image. Identify air, water, a selected interface patch, incoming light and the direction from that patch to the camera. Draw the local normal and incidence plane. For unpolarized illumination of a smooth dielectric interface at Brewster incidence, reflected light is polarized perpendicular to that plane. Rotating a linear polarizer before the camera changes the transmitted reflected contribution. This is the domain relation supplied by [Feynman, I.33, §33-4](https://www.feynmanlectures.caltech.edu/I_33.html#Ch33-S4).

The interpretation tells you what to adjust. Moving the viewpoint changes incidence; ripples change local normals, so a single planar sketch may need several patches. Inspect a changed view and determine whether the proposed adjustment still follows.

#### B.5.4:5.2 - Recognize a conflict relation before colouring a graph

A laboratory must place three tests in two simultaneous-run slots. Its operating conditions say that A and B need the same exclusive fixture throughout a run; B and C need the same exclusive power unit; A and C can run together. There are no other constraints in this constructed case.

Represent tests by vertices and a pairwise inability to share a slot by an edge. The observations supply edges AB and BC. The construction in [B.5:5.1][fpf-b5-5-1-ref] produces slots {A,C} and {B}; reading the result back means that neither exclusive resource is double-booked.

Now change the conditions: A and C also require the same observer throughout a run. This adds edge AC. The triangle needs three slots under these conditions; two-colouring no longer supplies an arrangement.

Consider instead three tests with independent fixtures whose shared resource is a 5 A supply. Each draws 2 A. Any pair can run together, but all three exceed the supply's capacity. A graph with no pairwise conflict edges loses that group constraint. Retain the currents and the slot-wise capacity inequality when constructing the arrangement.

### B.5.4:6 - Bias-Annotation

Answer-bearing demonstrations favour recognition from familiar wording. Obtain a changed situation when independent selection matters. Representation familiarity can also encourage premature graph, table or equation use; compare the represented relations with the constraint that actually changes the answer.

When a teacher, colleague or AI supplies the decisive interpretation, retain that contribution in any account of what the learner performed.

### B.5.4:7 - Conformance Checklist

- The concrete question determines which distinctions matter.
- The interpretation identifies the participants, relations and applicable conditions in the encountered situation.
- A consequence connects the interpretation to an explanation, construction or action.
- A consequential change is interpreted using the retained relation and its conditions.
- The domain account, prerequisites and permitted assistance are accessible to the intended reader.
- An independent-recognition claim is supported by an appropriately uncued attempt.

### B.5.4:8 - Common Anti-Patterns and How to Avoid Them

**Definition recitation.** Return to what supplies the definition's participants and relations in this case, then derive a consequence.

**Representation chosen before the constraint.** Compare what the representation preserves with what the use needs. In the laboratory case, pairwise compatibility leaves aggregate current to be handled separately.

**A demonstrated answer credited as independent recognition.** Use the demonstration for learning. For assessment, obtain a changed case with the assistance permitted in later work.

### B.5.4:9 - Consequences

The practitioner obtains an interpretation they can use and revise. A mismatch becomes a particular question about an object, relation, condition or domain account. A later calculation receives identified quantities; a model receives interpretable elements; further inquiry receives a discriminating observation.

The cost is constructing and examining the correspondence. This work can be small when the relevant relations are already clear.

### B.5.4:10 - Rationale

Concepts become useful through their relations to a situation. Recovering these relations and following a consequence connects interpretation to action. Reversing that passage after a failed consequence makes the interpretation correctable. A sketch and an equation can serve this work differently; their usefulness depends on the distinctions they expose.

### B.5.4:11 - SoTA-Echoing

The working question is how to interpret a particular situation when a usable concept account is available but its concrete participants are still missing. For this entry, use the concept-led correspondence in steps 3–4 as a specialization of the broader first-model route in [B.5:4.1.1][fpf-b5-4-1-1-ref]. The broader route remains useful when the relevant relation itself has to be proposed.

Compare the two routes on :5.2 using the same operating conditions, an explanation of graph colouring, and a sketch plus the resource checks. B.5 first asks which tests and resources must remain distinguishable, then asks the engineer to propose their connection. An exclusive-resource conflict supplies AB and BC; a cheap consequence supplies {A,C}/{B}; challenging an omitted interaction can expose the shared-current constraint. That route can solve the case.

Here the reader's stated difficulty lies inside that “propose their connection” move. Steps 3–4 work back from the understood relation: an edge joins two participants that cannot share a slot. Fill the two participants with A and B, and identify the fixture whose exclusive use makes the relation hold; repeat for B and C and check A with C. This supplies both the graph and the reason for each edge before colouring. In the 5 A variant, the same correspondence question asks what the empty graph represents: permission for each pair. Comparing it with the required permission for the whole group exposes the missing sum, 2 + 2 + 2 > 5. Both routes yield the same correct schedule; this specialization supplies the concrete relation and its operating-condition check inside the broader instruction.

The selected trade-off is more explicit participant-by-participant work where the broader instruction leaves that work to the reader. It uses the same domain account and case data; retain it only while constructing the correspondence is the difficulty. When the reader already has that correspondence, :1 returns directly to the calculation. When no usable relation has been selected, B.5's first-model route retains the wider search. These case comparisons establish the additional instruction and its consequence; comparative learning speed and transfer remain empirical questions.

[Sirnoorkar, Bergeron and Laverty (2023), §III](https://journals.aps.org/prper/pdf/10.1103/PhysRevPhysEducRes.19.010118) supplies the target-to-representation, internal-reasoning and interpretation-back account used in steps 4–6. Its discussion of problem assessment, model construction and interpretation makes the broader modeling route a substantive alternative. The adaptation here unfolds the target-to-representation work from the relations in an already understood concept. Its empirical basis is two physics problem-solving cases; the scheduling comparison above is a constructed comparison of the instructions.

[Kashyap and Singh (2026), §II and case B](https://journals.aps.org/prper/abstract/10.1103/j6lc-c5q8) shows redrawing alongside spatial reinterpretation and continuing grounding errors in electrostatics problem solving. Adapt that contribution in step 2 and :5.1: change a viewpoint when it can reveal a needed relation, then check the relation's physical conditions.

Reconsider this choice if an intended reader cannot fill a decisive relation from the available concept account, or if the broader modeling instruction supplies the same recoverable correspondence with less effort. Change the affected instruction or its prerequisite; a comparison showing that the explicit recovery adds no useful contribution would remove the reason to use this specialization. The optics law remains supplied by the linked Feynman account, and the laboratory consequences follow from their stipulated operating conditions.

### B.5.4:12 - Relations

- C.3 supplies kind recovery, classification applicability and judgment when a classification question arises.
- C.29 helps select and interpret a mathematical representation, including its preserved and lost structure.
- B.5 connects the interpreted question to construction, inference, observation and a useful continuation.
- A.7.1 supplies consequence-guided ontological repair when a working claim gives a defeated engineering result.

[fpf-b5-5-1-ref]: B.5-Canonical-Reasoning-Cycle.md#b551---a-counterexample-becomes-a-constructive-mathematical-question
[fpf-b5-4-1-1-ref]: B.5-Canonical-Reasoning-Cycle.md#b5411---propose-a-first-model

### B.5.4:End
