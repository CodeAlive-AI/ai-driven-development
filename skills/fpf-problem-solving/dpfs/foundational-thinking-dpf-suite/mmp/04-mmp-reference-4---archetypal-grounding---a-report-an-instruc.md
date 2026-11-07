## MMP.Reference:4 - Archetypal Grounding - A report, an instruction and a changed question

The Readme's [observation-to-action entry](_index.md#mmp-observation-to-action---turn-an-observing-model-into-a-workable-instruction) works the connection between MMP.7, MMP.8 and the Core Method-composition construction. One of two requests needs a scarce resource. Allocation follows a report produced through an unrecorded choice of channel.

MMP.7's operation first sums over the channel to obtain the reporting law. In the worked case, following the report succeeds with conditional probabilities 0.8 and 0.7 in the two circumstances. MMP.8 then asks what performance the instruction must supply. At least 0.65 success in each circumstance permits following the report. Zero failure does not. An average-success criterion with one circumstance occurring with probability 0.95 instead favours a fixed allocation among the four deterministic instructions considered.

The calculation changes the proposed way of working: whether to obtain and follow the report depends on the requirement, the circumstances it distinguishes and its cost. The receiving participant must get it before allocation. The complete elementary comparison is in [MMP.8:5.2 - Decide which participant gets a scarce resource](14-mmp-8---formulate-information-dependent-choices-mathematical.md#mmp852---decide-which-participant-gets-a-scarce-resource). The Readme explains the return to the work when observation itself changes the situation. Each changed condition selects the contribution to revise.

### MMP.Reference:4.1 - A total is sufficient until the question changes

Suppose material passes through two cycles in two intermediate buffers. Each incoming portion retains 80% of its amount. Its fractions going to each buffer are unknown but constant across the cycles and independent of the portion's amount. Initially the amounts are `(10, 0)`. Both buffers have sufficient capacity; the material remains there until a receiver is selected and the later transfer begins. Transfer losses are neglected. How much capacity does that receiver need for all the material?

MMP.10 represents one cycle by `x_next = A*x`, where the two components of x are the amounts in the buffers. Nonnegative entries of A express the fractions received; each column sums to 0.8. MMP.11 retains the family defined by those conditions. Direct constraints suffice: choosing one fitted matrix would add information the situation has not supplied.

MMP.9 derives a simpler relation for the total `S = x_1 + x_2`: `S_next = 0.8*S`. After two cycles the total is 6.4, so capacity 7 suffices. The unknown distribution does not need to be resolved for this answer.

Now transfer only from the first buffer. One admissible model, `A = 0.8*I`, leaves 6.4 there. Another, `A = 0.8*[[0,0],[1,1]]`, leaves none there. Both give the same total. Capacity 7 still suffices, but the total alone cannot justify using a cheaper receiver of capacity 4. Return to the retained model family to ask which differences can affect the local amount. A further observation is useful if resolving those differences can change the receiver choice enough to justify its cost; C.16.IR and C.11.DUA support that question. The revised use changes what the model must preserve while leaving the total calculation valid for its original question.

Other bodies show different mathematical work: representing partial functions without distorting the requested count, deriving a bound after removing population detail, and constructing an unknown response while preserving its shape. Use their worked cases to learn the corresponding operations and their limits. The choice among those operations follows the difficulty, not the example's subject.
