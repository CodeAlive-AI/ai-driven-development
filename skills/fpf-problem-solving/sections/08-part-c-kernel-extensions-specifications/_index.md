# **Part C — Kernel Extensions Specifications**

| §                                            | Pattern                        | Tag | Scope & Exports                                                      |
| -------------------------------------------- | ---------------------------------- | --- | -------------------------------------------------------------------- |
| **Cluster C.I – Core CALs / LOGs / CHRs**    |                                    |     |                                                                      |
| C.1                                          | **Sys‑CAL**                        | CAL | Physical holon composition; conservation invariants; resource hooks. |


## Contents

- [C.2 - Epistemic holon composition (KD-CAL)](01-c-2---epistemic-holon-composition.md) (117 lines) — Scope & exports. A substrate‑neutral calculus for composing epistemic holons (U.Episteme) and reasoning about their motion and equivalence. Exports: (i) three point‑characteristics—Formality F,...
- [C.2.1 - U.Episteme — Epistemes and their slot graph](02-c-2-1---u-episteme-epistemes-and-their-slot-graph.md) (831 lines) — One-line summary. U.Episteme is the holon type for epistemes; its internal ontology is given by U.EpistemeSlotGraph, which replaces the legacy semantic triangle with a typed graph n-ary relation over...
- [C.2.P - Epistemic Precision Restoration](03-c-2-p---epistemic-precision-restoration.md) (636 lines) — Type: Architectural (A), C.2 precision-restoration pattern
- [C.2.2 - Reliability R in the F–G–R triad](04-c-2-2---reliability-r-in-the-f-g-r-triad.md) (375 lines) — Reliability (R) is a conservative, evidence-bound warrant signal for a typed claim under an explicit claim scope (G). Cross-context reuse is Bridge-only: scope may be re-expressed via...
- [C.2.2a - U.LanguageStateSpace - Language-state chart over U.CharacteristicSpace](05-c-2-2a---u-languagestatespace---language-state-chart-over-u.md) (268 lines) — Type: Architectural (A)
- [C.2.3 - Unified Formality Characteristic F](06-c-2-3---unified-formality-characteristic-f.md) (312 lines) — Type: Definitional (D)
- [C.2.LS - U.LanguageStateFacetProfile - Thin profile bundle for language-state facets](07-c-2-ls---u-languagestatefacetprofile---thin-profile-bundle-f.md) (243 lines) — Type: Definitional (D)
- [C.2.4 - U.ArticulationExplicitness](08-c-2-4---u-articulationexplicitness.md) (173 lines) — Type: Definitional (D)
- [C.2.5 - U.LanguageStateClosureDegree](09-c-2-5---u-languagestateclosuredegree.md) (184 lines) — Type: Definitional (D)
- [C.2.6 - U.LanguageStateAnchoringMode](10-c-2-6---u-languagestateanchoringmode.md) (163 lines) — Type: Definitional (D)
- [C.2.7 - U.LanguageStateRepresentationFactorBundle](11-c-2-7---u-languagestaterepresentationfactorbundle.md) (166 lines) — Type: Definitional (D)
- [C.3 - Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)](12-c-3---kinds-intent-extent-and-typed-reasoning.md) (911 lines) — One‑line summary. Establishes U.Kind as the minimal, context‑local intensional carrier of “what a statement is about,” separates intent (KindSignature + its own F) from extent (which instances belong...
- [C.3.1 - U.Kind & SubkindOf (Core)](13-c-3-1---u-kind-subkindof.md) (133 lines) — One‑line summary. Defines U.Kind as a minimal, context‑local intensional carrier for “what a claim is about,” and U.SubkindOf (⊑) as a partial order over kinds. Kinds do not carry Scope. Scope...
- [C.3.2 - KindSignature (+F) & Extension/MemberOf](14-c-3-2---kindsignature-extension-memberof.md) (211 lines) — One‑line summary. Specifies the intent and extent of kinds: (i) a KindSignature(k) (the intensional definition of kind k) that declares its own Formality F; (ii) an Extension(k, slice) ⊆...
- [C.3.3 - KindBridge & CL^k — Cross‑context Mapping of Kinds](15-c-3-3---kindbridge-cl-k-cross-context-mapping-of-kinds.md) (247 lines) — One‑line summary. Defines KindBridge as the normative mechanism for moving kinds (their intent and selected subkind‑of links) between bounded contexts (“Contexts”). A bridge declares how a source...
- [C.3.4 - RoleMask — Contextual Adaptation of Kinds (without cloning)](16-c-3-4---rolemask-contextual-adaptation-of-kinds.md) (234 lines) — One‑line summary. Defines U.RoleMask(kind, Context) as a context‑local adaptation of a U.Kind that (a) adds constraints and/or vocabulary bindings, and (b) may narrow membership deterministically...
- [C.3.5 - KindAT — Intentional Abstraction Facet for Kinds (K0…K3)](17-c-3-5---kindat-intentional-abstraction-facet-for-kinds.md) (171 lines) — One‑line summary. Defines KindAT as an informative facet attached to U.Kind that classifies the intentional abstraction stance of a kind—K0 Instance, K1 Behavioral Pattern, K2 Formal Kind/Class, K3...
- [C.3.A - Typed Guard Macros for Kinds + USM (Annex)](18-c-3-a---typed-guard-macros-for-kinds-usm.md) (764 lines) — One‑line summary. Provides normative guard macros that combine USM Scope (A.2.6) with Kind‑CAL (C.3.x) so authors can gate state changes and compositions that quantify over kinds without conflating...
- [C.11 - Decision Theory (Decsn-CAL)](19-c-11---decision-theory.md) (715 lines) — Normativity: Normative unless marked informative
- [C.13 — Constructional Mereology (Compose‑CAL)](20-c-13-constructional-mereology.md) (199 lines) — Provide a single, generative calculus for part–whole structure so that all structural relations in FPF are constructed (not merely declared) from three primitives and thereby inherit extensional...
- [C.16 - Measurement & Metrics Characterization (MM‑CHR)](21-c-16---measurement-metrics-characterization.md) (422 lines) — Name. Measurement & Metrics Characterization (MM‑CHR). This is a user‑oriented name: in user‑facing narrative we may say metrics; in Tech register we speak Characteristic, Scale, Level, Coordinate,...
- [C.16.P - Characteristic and Scale Precision Restoration](22-c-16-p---characteristic-and-scale-precision-restoration.md) (230 lines) — Type: Characterization precision-restoration pattern
- [C.16.Q - Quality-Term Precision Restoration](23-c-16-q---quality-term-precision-restoration.md) (769 lines) — Type: Characterization precision-restoration pattern
- [C.17 - Characterising Generative Novelty & Value (Creativity‑CHR)](24-c-17---characterising-generative-novelty-value.md) (740 lines) — Status. Mechanism specification (CHR) — normative where stated.
- [C.18 - Open‑Ended Search Calculus (NQD‑CAL)](25-c-18---open-ended-search-calculus.md) (111 lines) — Status. Calculus specification (CAL). Exports Γ_nqd. operators for open‑ended, illumination‑style generation. ΔKernel = 0 (no kernel primitives added). Minting note: this CAL does not mint new...
- [C.18.1 - Scaling‑Law Lens Binding (SLL)](26-c-18-1---scaling-law-lens-binding.md) (101 lines) — One‑screen purpose (manager‑first).
- [C.19 - Explore–Exploit Governor (E/E‑LOG)](27-c-19---explore-exploit-governor.md) (356 lines) — Normativity: Normative
- [C.19.1 - Bitter‑Lesson Preference (BLP)](28-c-19-1---bitter-lesson-preference.md) (104 lines) — One‑screen purpose (manager‑first).
- [C.20 - Composition of U.Discipline (Discipline‑CAL)](29-c-20---composition-of-u-discipline.md) (100 lines) — Builds on. C.2 KD‑CAL (F–G–R & CL routing), A.19/G.0 CG‑Spec (comparability), F.9 Bridges (cross‑Context alignment), E.10 LEX (registers & twin labels). Coordinates with. C.21 (Discipline‑CHR, field...
- [C.21 - Field Health & Structure (Discipline-CHR)](30-c-21---field-health-structure.md) (213 lines) — Purpose. Give FPF a typed, auditable way to speak about the health, maturity, and structure of a scientific/engineering discipline, without collapsing into taste, anecdotes, or single-number scores....
- [C.22 - Problem Typing & TaskSignature Assignment (Problem-CHR)](31-c-22---problem-typing-tasksignature-assignment.md) (215 lines) — Purpose. Give FPF an admissible, minimal, and portable way to type a problem for downstream selector-facing use after the problem-side representation is stable enough for Principles-to-Work,...
- [C.22.1 - Task-family adaptation signature](32-c-22-1---task-family-adaptation-signature.md) (148 lines) — One-screen purpose (manager-first).
- [C.22.2 - ProblemCard@Context](33-c-22-2---problemcard-context.md) (823 lines) — Normativity: Normative
- [C.23 - MethodFamily Evidence & Maturity (Method‑SoS‑LOG)](34-c-23---methodfamily-evidence-maturity.md) (204 lines) — LOG (logic) for deductive shells for admissibility
- [C.24 - Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)](35-c-24---agentic-tool-use-and-call-planning.md) (351 lines) — Normativity: Normative
- [C.25 - Q-Bundle: Authoring "-ilities" as Structured Quality Bundles](36-c-25---q-bundle-authoring--ilities-as-structured-quality-bun.md) (412 lines) — Type: Definitional (D)
- [C.26 - Quantum-Like Modeling Lens](37-c-26---quantum-like-modeling-lens.md) (607 lines) — Type: Architectural pattern
- [C.26.1 - Probe-Coupled Boundary Interaction](38-c-26-1---probe-coupled-boundary-interaction.md) (304 lines) — Type: Architectural pattern
- [C.26.2 - Enacted Distributed State Evidence](39-c-26-2---enacted-distributed-state-evidence.md) (346 lines) — Type: Architectural pattern
- [C.26.3 - Viability-Envelope Boundary Regulation](40-c-26-3---viability-envelope-boundary-regulation.md) (330 lines) — Type: Architectural pattern
- [C.27 - Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change](41-c-27---temporal-claim-adequacy-state-readings-temporal-trend.md) (2069 lines) — Type: Architectural (A)
- [C.28 - CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability](42-c-28---causaluse-cal-causal-use-questions-causality-ladder-r.md) (879 lines) — Normativity: Normative unless explicitly marked informative
- [C.29 - Mathematical Lens Adequacy (MLA)](43-c-29---mathematical-lens-adequacy.md) (1223 lines) — Type: Architectural pattern
- [C.30 - Architecture Description Adequacy (ADA)](44-c-30---architecture-description-adequacy.md) (602 lines) — Type: Architectural pattern
- [C.30.P - Architecture and Structure Precision Restoration](45-c-30-p---architecture-and-structure-precision-restoration.md) (233 lines) — Type: Architectural pattern
- [C.30.ASV - Architecture Structural View Adequacy (ASV)](46-c-30-asv---architecture-structural-view-adequacy.md) (664 lines) — Type: Architectural pattern
- [C.30.LCA - Control Structure View Adequacy (LCA)](47-c-30-lca---control-structure-view-adequacy.md) (253 lines) — Type: Architectural subpattern under C.30
- [C.30.ILC - Cross-Scope Architecture Residual Triage](48-c-30-ilc---cross-scope-architecture-residual-triage.md) (209 lines) — Type: Architectural subpattern under C.30
- [C.30.TGA-FLOW-REL - Architecture/TGA Flow-Structure Relation](49-c-30-tga-flow-rel---architecture-tga-flow-structure-relation.md) (245 lines) — Type: Architectural pattern
