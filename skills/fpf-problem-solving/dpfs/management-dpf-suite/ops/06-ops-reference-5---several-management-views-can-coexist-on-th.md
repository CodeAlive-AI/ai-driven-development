## OPS.Reference:5 - Several management views can coexist on the same Work


A project view can expose time-bounded commitments, WorkPlan content, decisions, dates, allocations, and closure. A process view can expose recurring Method, inputs, results, order, and controls. A case view can expose changing subject state, new facts, exceptions, permissible next Work, and closure. A queueing view can expose membership, waiting, order or service relation, and resource demand. A control-structure view can expose observation, actuation, reference, supervision, feedback, and unlike rates.

These views need not be isomorphic. Co-use requires subject and grain correspondence, governing commitments, state correspondence, handoff or coexistence conditions, update and decision rules, conflicts, and stops.

**Constituent actions in ongoing work.** For example, inspecting a returned item can constitute part of resolving its service case, while resolving that case constitutes part of operating a repair service. All three can be under way during the inspection. A change from cosmetic acceptance to a requirement about intermittent failure changes the inspection needed in that case; faster visual checks alone cannot establish the new result. The operative must have the diagnostic capability and access the case requires, and shared test equipment must fit the combined operating demand. OPS.19 examines simultaneous work and conflicts, using FPF B.1.5.EW to recover these constituent connections when needed.
