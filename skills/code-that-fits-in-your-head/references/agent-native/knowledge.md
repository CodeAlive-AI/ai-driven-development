# ⚠️ Agent-Native Amendments — NOT from the Book

> **This folder is not Seemann's.** These files address agent-specific concerns absent from the 2021 book. Treat them as editorial guidance and do not attribute them to Mark Seemann.

## Canonical Topics

| File | Canonical concern |
|---|---|
| `hallucination-debugging.md` | Invented APIs, version drift, package hallucination, and dependency provenance |
| `types-as-guardrails.md` | Types, schemas, tests, and executable contracts as complementary constraints |
| `reviewability.md` | Evidence-based review, risk classification, and accountable human ownership |

Large tasks are explicitly allowed. Agent work spanning tens of thousands of lines can be sound when it follows a coherent architecture and has clear acceptance criteria, reliable verification, and recoverable checkpoints. These files constrain unverifiable or architecturally incoherent work—not size by itself.

## Status

- **Editorial, not book content.** Connections to book chapters are stated explicitly.
- **One canonical home per rule.** Book-derived themes link here instead of duplicating cross-cutting agent guidance.
- **Evolving defaults.** Prefer observable outcomes and repository policy over model- or language-specific rankings.

## How to Use This Folder

- Start with the relevant book-derived theme for general design guidance.
- Load one agent-native file when agent authorship creates an additional failure mode.
- Verification integrity (checkpoints, independent oracles, never weakening a gate) is not here: it is `pragmatic-verification`'s subject.
- Do not load the whole folder by default.
