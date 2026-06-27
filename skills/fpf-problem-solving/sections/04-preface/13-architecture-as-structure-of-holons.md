## Architecture As Structure Of Holons

FPF treats architecture as selected structure of a holon in a context, not as a diagram, document, approval, promise, or implementation plan.

For a first reader, this means: before asking whether the architecture is good, name the thing whose structure matters. The thing may be a product, machine, organization, method, publication system, body of knowledge, AI-agent arrangement, local framework, or FPF itself. Then ask which structures are unknown, candidate, selected, expected, actual, captured in a description, lost in a view, or returned from operation.

This makes architecture broad without making it vague. Architecture descriptions, structural views, viewpoints, diagrams, models, ADR-like records, and publication forms are descriptions or publications about architecture. They are valuable, but they do not replace the architecture itself. A decision record can preserve why a structure was selected; it is not proof that the structure was realized. A measurement can show stress or improvement; it is not the decision. A work plan can tell people how to act; it is not performed work.

The architecture patterns make the whole flow usable. `C.30` grounds an architecture claim over selected structures. `A.22` governs structure and structural views. `C.32.P2S` carries architecture-relevant pressure into candidate structures, selected structures, architecture decisions, work that realizes structures, and actual-structure feedback. `C.32` governs candidate synthesis. `C.32.PAD` governs project architecture decisions. `C.32.ADR` governs ADR-like publication. `C.33`, `C.34`, and `C.35` govern what structural content is captured, preserved, lost, or generated before architecture work relies on it.

This matters because architecture work is not only "draw the diagram". It is also "which holon is changing", "which structure matters", "what characteristic changes", "what alternatives must remain alive", "which decision closes enough for work", "which method or role can realize the selected structure", "what actual structure appeared", and "what feedback reopens the work".

When one holon changes another holon, FPF also asks whether the changing holon can produce the desired structure of the changed holon. A team, toolchain, work method, evidence practice, or supplier network has its own architecture. If that transformer architecture cannot realize the transformed holon's selected structure, the project has an architecture problem on both sides.

Epiplexity is one important architecture characteristic. It names structural entanglement that makes a holon hard to understand, change, control, reuse, or improve. A low-epiplexity design is not merely simpler in ordinary speech. It is structurally easier to reason about under declared characteristics and concerns, and its descriptions usually lose less critical structure.

The same architecture thinking now applies to the FPF ecosystem itself. FPF Core, domain principle frameworks, local practice frameworks, source packs, relation records, publication units, quality loops, and refresh routes are different objects. The public adoption path is not "copy all of FPF into your project." It is usually: depend on FPF Core, create a domain or local framework when needed, publish it for your readers, and keep its quality and refresh route explicit.

