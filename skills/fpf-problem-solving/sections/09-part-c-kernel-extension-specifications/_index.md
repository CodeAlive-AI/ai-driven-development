# **Part C — Kernel Extension Specifications**

| §                                            | Pattern                        | Tag | Scope & Exports                                                      |
| -------------------------------------------- | ---------------------------------- | --- | -------------------------------------------------------------------- |
| **Cluster C.I – Core CALs / LOGs / CHRs**    |                                    |     |                                                                      |
| C.1                                          | **Sys‑CAL**                        | CAL | Physical holon composition; conservation invariants; resource hooks. |


## Contents

- [C.2 - Epistemic holon composition (KD-CAL)](01-c-2---epistemic-holon-composition.md) (109 lines) — Scope & exports. A substrate‑neutral calculus for composing epistemic holons (U.Episteme) and reasoning about their motion and equivalence. Exports: (i) three point‑characteristics—Formality F,...
- [C.2.1 - U.Episteme: Constitution, Empirical Grounding, and Edition Relations](02-c-2-1---u-episteme-constitution-empirical-grounding-and-edit.md) (507 lines) — Normativity: Normative except where a section is explicitly marked informative
- [C.2.P - Epistemic Precision Restoration](03-c-2-p---epistemic-precision-restoration.md) (659 lines) — Type: C.2 precision-restoration pattern for episteme, publication, source wording, and source-relation wording
- [C.2.2 - Reliability R in the F–G–R triad](04-c-2-2---reliability-r-in-the-f-g-r-triad.md) (375 lines) — Reliability (R) is a conservative, evidence-bound warrant signal for a typed claim under an explicit claim scope (G). Cross-context reuse is Bridge-only: scope may be re-expressed via...
- [C.2.2a - U.LanguageStateSpace - Language-state chart over U.CharacteristicSpace](05-c-2-2a---u-languagestatespace---language-state-chart-over-u.md) (264 lines) — Type: Architectural (A)
- [C.2.3 - Unified Formality Characteristic F](06-c-2-3---unified-formality-characteristic-f.md) (312 lines) — Type: Definitional (D)
- [C.2.LS - U.LanguageStateFacetProfile - Thin profile bundle for language-state facets](07-c-2-ls---u-languagestatefacetprofile---thin-profile-bundle-f.md) (252 lines) — Type: Definitional (D)
- [C.2.4 - U.ArticulationExplicitness](08-c-2-4---u-articulationexplicitness.md) (182 lines) — Type: Definitional (D)
- [C.2.5 - U.LanguageStateClosureDegree](09-c-2-5---u-languagestateclosuredegree.md) (193 lines) — Type: Definitional (D)
- [C.2.6 - U.LanguageStateAnchoringMode](10-c-2-6---u-languagestateanchoringmode.md) (175 lines) — Type: Definitional (D)
- [C.2.7 - U.LanguageStateRepresentationFactorBundle](11-c-2-7---u-languagestaterepresentationfactorbundle.md) (175 lines) — Type: Definitional (D)
- [C.2.P.DR - Declarative Representation Precision Restoration](12-c-2-p-dr---declarative-representation-precision-restoration.md) (317 lines) — Type: C.2.P precision-restoration child pattern for declarative-representation overread
- [C.3 - Kinds, Intent and Extent, and Typed Reasoning](13-c-3---kinds-intent-and-extent-and-typed-reasoning.md) (158 lines) — Type: Typed reasoning discipline pattern
- [C.3.1 - U.Kind and U.SubkindOf Core](14-c-3-1---u-kind-and-u-subkindof-core.md) (125 lines) — Type: Typed reasoning core pattern
- [C.3.2 - KindSignature (+F) & Extension/MemberOf](15-c-3-2---kindsignature-extension-memberof.md) (201 lines) — One‑line summary. Specifies the intent and extent of kinds: (i) a KindSignature(k) (the intensional definition of kind k) that declares its own Formality F; (ii) an Extension(k, slice) ⊆...
- [C.3.3 - KindBridge & CL^k — Cross‑context Mapping of Kinds](16-c-3-3---kindbridge-cl-k-cross-context-mapping-of-kinds.md) (236 lines) — One‑line summary. Defines KindBridge as the normative mechanism for moving kinds (their intent and selected subkind‑of links) between bounded contexts (“Contexts”). A bridge declares how a source...
- [C.3.4 - RoleMask — Contextual Adaptation of Kinds (without cloning)](17-c-3-4---rolemask-contextual-adaptation-of-kinds.md) (224 lines) — One‑line summary. Defines U.RoleMask(kind, Context) as a context‑local adaptation of a U.Kind that (a) adds constraints and/or vocabulary bindings, and (b) may narrow membership deterministically...
- [C.3.5 - KindAT — Intentional Abstraction Facet for Kinds (K0…K3)](18-c-3-5---kindat-intentional-abstraction-facet-for-kinds.md) (163 lines) — One‑line summary. Defines KindAT as an informative facet attached to U.Kind that classifies the intentional abstraction stance of a kind—K0 Instance, K1 Behavioral Pattern, K2 Formal Kind/Class, K3...
- [C.3.A - Typed Guard Macros for Kinds + USM (Annex)](19-c-3-a---typed-guard-macros-for-kinds-usm.md) (728 lines) — One‑line summary. Provides normative guard macros that combine USM Scope (A.2.6) with Kind‑CAL (C.3.x) so authors can gate state changes and compositions that quantify over kinds without conflating...
- [C.11 - Decision Theory (Decsn-CAL)](20-c-11---decision-theory.md) (716 lines) — Normativity: Normative unless marked informative
- [C.13 — Constructional Mereology (Compose‑CAL)](21-c-13-constructional-mereology.md) (227 lines) — At a glance. Use C.13 when a structural identity claim needs a constructive trace showing how a whole, collection-as-whole, or aspect is obtained from parts.
- [C.16 - Measurement & Metrics Characterization (MM‑CHR)](22-c-16---measurement-metrics-characterization.md) (454 lines) — Use this pattern when. Use C.16 when a value, score, rating, metric label, QL probe output, dashboard reading, or comparison is being treated as meaningful without a visible characteristic, scale,...
- [C.16.P - Characteristic and Scale Precision Restoration](23-c-16-p---characteristic-and-scale-precision-restoration.md) (250 lines) — Type: Characterization precision-restoration pattern
- [C.16.Q - Quality-Term Precision Restoration](24-c-16-q---quality-term-precision-restoration.md) (777 lines) — Type: Characterization precision-restoration pattern
- [C.17 - Characterising Generative Novelty & Value (Creativity‑CHR)](25-c-17---characterising-generative-novelty-value.md) (720 lines) — Status. Mechanism specification (CHR) — normative where stated.
- [C.18 - Open-Ended Search Archive and Front Stewardship](26-c-18---open-ended-search-archive-and-front-stewardship.md) (225 lines) — Tech-name: OpenEndedSearchArchiveAndFrontStewardship
- [C.18.1 - Scaling‑Law Lens Binding (SLL)](27-c-18-1---scaling-law-lens-binding.md) (135 lines) — Use this pattern when. Use C.18.1 when a generator, selector, method family, benchmark, or comparison claims that behavior changes with scale, budget, data, model capacity, iteration budget, freedom...
- [C.19 - Explore-Exploit Live-Pool Governor](28-c-19---explore-exploit-live-pool-governor.md) (393 lines) — Normativity: Normative
- [C.19.1 - Bitter‑Lesson Preference (BLP)](29-c-19-1---bitter-lesson-preference.md) (141 lines) — One‑screen purpose (manager‑first).
- [C.19.2 - Use-Bounded Apparatus Application](30-c-19-2---use-bounded-apparatus-application.md) (165 lines) — Type: Architectural (A)
- [C.20 - Composition of U.Discipline (Discipline‑CAL)](31-c-20---composition-of-u-discipline.md) (135 lines) — U.Discipline is the root durable holon kind used for field-level practice-and-knowledge wholes. Its EntityOfConcern lets FPF users talk about a discipline as one reusable object without collapsing it...
- [C.21 - Field Health & Structure (Discipline-CHR)](32-c-21---field-health-structure.md) (255 lines) — Purpose. Give FPF a typed, reviewable way to characterize the health, maturity, and structure of a scientific or engineering discipline, without collapsing into taste, anecdotes, dashboard views,...
- [C.22 - Problem Typing & TaskSignature Assignment (Problem-CHR)](33-c-22---problem-typing-tasksignature-assignment.md) (373 lines) — Purpose. Give FPF an admissible, minimal, and portable TaskSignature@Context declaration for selector-facing use after the problem-side representation is stable enough for Principles-to-Work,...
- [C.22.1 - Task-family adaptation signature](34-c-22-1---task-family-adaptation-signature.md) (149 lines) — One-screen purpose (manager-first).
- [C.22.PFR - Problematic-For Relation](35-c-22-pfr---problematic-for-relation.md) (283 lines) — Normativity: Normative unless marked informative
- [C.22.2 - ProblemCard@Context](36-c-22-2---problemcard-context.md) (655 lines) — Normativity: Normative
- [C.23 - MethodFamily Evidence & Maturity (Method‑SoS‑LOG)](37-c-23---methodfamily-evidence-maturity.md) (203 lines) — LOG (logic) for deductive shells for admissibility
- [C.24 - Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)](38-c-24---agentic-tool-use-and-call-planning.md) (350 lines) — Normativity: Normative
- [C.25 - Q-Bundle: Authoring "-ilities" as Structured Quality Bundles](39-c-25---q-bundle-authoring--ilities-as-structured-quality-bun.md) (417 lines) — Type: Definitional (D)
- [C.26 - Quantum-Like Modeling Lens](40-c-26---quantum-like-modeling-lens.md) (597 lines) — Type: Architectural pattern
- [C.26.1 - Probe-Coupled Boundary Interaction](41-c-26-1---probe-coupled-boundary-interaction.md) (300 lines) — Type: Architectural pattern
- [C.26.2 - Enacted Distributed State Evidence](42-c-26-2---enacted-distributed-state-evidence.md) (343 lines) — Type: Architectural pattern
- [C.26.3 - Viability-Envelope Boundary Regulation](43-c-26-3---viability-envelope-boundary-regulation.md) (331 lines) — Type: Architectural pattern
- [C.27 - Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change](44-c-27---temporal-claim-adequacy-state-readings-temporal-trend.md) (1964 lines) — Type: Claim-adequacy pattern
- [C.27.TA - Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness](45-c-27-ta---temporal-aspect-time-windows-rhythm-cadence-and-cu.md) (272 lines) — Type: Definitional pattern
- [C.28 - CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability](46-c-28---causaluse-cal-causal-use-questions-causality-ladder-r.md) (867 lines) — Normativity: Normative unless explicitly marked informative
- [C.29 - Mathematical Lens Use](47-c-29---mathematical-lens-use.md) (1362 lines) — Type: Architectural pattern
- [C.30 - Grounded Architecture and Selected-Structure Adequacy](48-c-30---grounded-architecture-and-selected-structure-adequacy.md) (592 lines) — Type: Architectural pattern
- [C.30.AD - Architecture Description Adequacy](49-c-30-ad---architecture-description-adequacy.md) (402 lines) — Type: Architectural pattern
- [C.30.AD.BA - Built-Asset Architecture Description and Reference Designation](50-c-30-ad-ba---built-asset-architecture-description-and-refere.md) (197 lines) — Type: Architecture-description subpattern under C.30.AD
- [C.30.P - Architecture and Structure Precision Restoration](51-c-30-p---architecture-and-structure-precision-restoration.md) (248 lines) — Type: Architectural pattern
- [C.30.STRAT - Stratification Wording Precision Restoration](52-c-30-strat---stratification-wording-precision-restoration.md) (270 lines) — Type: Architectural precision-restoration subpattern under C.30
- [C.30.ASV - Architecture Structural View Adequacy (ASV)](53-c-30-asv---architecture-structural-view-adequacy.md) (716 lines) — Type: Architectural pattern
- [C.30.LCA - Control Structure View Adequacy (LCA)](54-c-30-lca---control-structure-view-adequacy.md) (269 lines) — Type: Architectural subpattern under C.30
- [C.30.ILC - Cross-Scope Architecture Residual Triage](55-c-30-ilc---cross-scope-architecture-residual-triage.md) (252 lines) — Type: Architectural subpattern under C.30
- [C.30.TFS-REL - Architecture Transformation-Flow Structure Relation](56-c-30-tfs-rel---architecture-transformation-flow-structure-re.md) (361 lines) — Type: Architectural pattern
- [C.31 - Modularity and Reusable Structure Characteristics](57-c-31---modularity-and-reusable-structure-characteristics.md) (367 lines) — Type: Characterization pattern
- [C.31.RSA - Reusable Structure Accounting](58-c-31-rsa---reusable-structure-accounting.md) (381 lines) — Type: Characterization pattern
- [C.31.ASAP - Architecture Scale-Amenability Preference](59-c-31-asap---architecture-scale-amenability-preference.md) (300 lines) — Type: Characterization pattern
- [C.32 - Architecture Candidate Synthesis](60-c-32---architecture-candidate-synthesis.md) (319 lines) — Type: Architectural pattern
- [C.32.P2S - Problem-to-Structure Architecturing Unfolding](61-c-32-p2s---problem-to-structure-architecturing-unfolding.md) (292 lines) — Type: Architectural process pattern under C.32
- [C.32.HCS - Architecture-Bearing Family Characteristic Starter Packs](62-c-32-hcs---architecture-bearing-family-characteristic-starte.md) (201 lines) — Type: Architectural characterization subpattern under C.32
- [C.32.ACS - Architecture Characteristic Criteria Set for Improvement Cycles](63-c-32-acs---architecture-characteristic-criteria-set-for-impr.md) (265 lines) — Type: Architecture characterization pattern under C.32
- [C.32.ACE - Architecture Characteristic Eval Programs](64-c-32-ace---architecture-characteristic-eval-programs.md) (201 lines) — Type: Architecture eval-support subpattern under C.32
- [C.32.CONWAY - Transformer and Transformed Architecture Correspondence](65-c-32-conway---transformer-and-transformed-architecture-corre.md) (252 lines) — Type: Architectural subpattern under C.32
- [C.32.MLAO - Multilevel Architecture Residual Optimization](66-c-32-mlao---multilevel-architecture-residual-optimization.md) (269 lines) — Type: Architectural subpattern under C.32
- [C.32.FAIL - Architecture Failure Recognition and Repair](67-c-32-fail---architecture-failure-recognition-and-repair.md) (236 lines) — Type: Architectural subpattern under C.32
- [C.32.PAD - Project Architecture Decision After Candidate Synthesis](68-c-32-pad---project-architecture-decision-after-candidate-syn.md) (302 lines) — Type: Architecture decision pattern under C.32
- [C.32.ADR - Architecture Decision Record Projection](69-c-32-adr---architecture-decision-record-projection.md) (224 lines) — Type: Architecture publication pattern under C.32
- [C.32.ADA - Architecture Decision Adequacy Scales](70-c-32-ada---architecture-decision-adequacy-scales.md) (265 lines) — Type: Architecture evaluation pattern under C.32
- [C.33 - Structural Information Adequacy for Architecture Capture and Missing-Structure Return](71-c-33---structural-information-adequacy-for-architecture-capt.md) (203 lines) — Type: Architectural pattern
- [C.34 - Structural Correspondence, Equivalence, and Morphism Adequacy](72-c-34---structural-correspondence-equivalence-and-morphism-ad.md) (189 lines) — Type: Architectural pattern
- [C.35 - Structural Synthesis and Discovery Adequacy](73-c-35---structural-synthesis-and-discovery-adequacy.md) (197 lines) — Type: Architectural pattern
- [C.36 - Cultural Evolution and Cultural-Evolution Engineering](74-c-36---cultural-evolution-and-cultural-evolution-engineering.md) (302 lines) — Tech-name: CulturalEvolutionEngineering
- [C.36.P - Cultural-Evolution Wording-Use Precision Restoration](75-c-36-p---cultural-evolution-wording-use-precision-restoratio.md) (146 lines) — Tech-name: CulturalEvolutionWordingUsePrecisionRestoration
