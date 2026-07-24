# ACP evaluation for agents-consilium

Date: 2026-07-24

## Decision

Keep direct headless CLI invocation as the production transport for
`agents-consilium`. Do not migrate the skill to ACP now, do not add a hybrid
ACP/CLI path, and do not create a separate `grok-acp`.

ACP is a good editor-to-agent protocol and provides a cleaner common event
model. For this skill's short-lived batch workload, however, it would move
rather than remove complexity:

- consilium would need a bidirectional ACP client, not just a stream parser;
- permissions, authentication, session lifecycle, cancellation, and server
  shutdown would become client responsibilities;
- review safety and delegate YOLO behavior would still require
  harness-specific configuration;
- Codex and Claude Code require adapter processes;
- multi-agent fan-out, judging, artifacts, timeouts, and result aggregation
  remain outside ACP.

The current direct CLI design better matches the required contract: one-shot
execution, explicit safety argv, live progress on stderr, final output on
stdout, artifacts, and an actionable process exit status.

## What ACP standardizes

ACP v1 uses JSON-RPC between an agent and a client. It standardizes:

- initialization and capability negotiation;
- session creation with a working directory;
- streaming message, reasoning, plan, and tool-call updates;
- permission requests and responses;
- cancellation;
- explicit prompt-turn completion with a `stopReason`;
- optional client-provided filesystem and terminal capabilities.

This is valuable for IDEs and interactive clients. It does not provide
multi-agent orchestration, shared state, workflow graphs, voting, judging, or
artifact management.

## Security finding

ACP does not itself create a sandbox.

Session modes are defined by each agent. They may change prompts, available
tools, or whether permissions are requested, but a mode named `plan`,
`read-only`, or `code` is not a protocol-level security boundary. The
dedicated session-mode API is also being superseded by flexible session config
options.

An agent may send `session/request_permission`; a client can accept, reject, or
automatically answer it. This is consent mediation, not filesystem or process
isolation. An agent can also execute its own tools rather than use
client-mediated `fs/*` or `terminal/*` methods.

Consequences for consilium:

- **review** still needs harness or OS enforcement such as Codex/Grok sandbox
  flags, plan agents, and tool allow/deny lists;
- **delegate** still needs harness-specific unrestricted modes in addition to
  automatically accepting permission requests;
- a uniform ACP permission policy cannot replace the existing backend-specific
  safety matrix.

## Harness support matrix

The local CLI versions inspected during the evaluation were:

- Codex CLI `0.145.0`
- Claude Code `2.1.218`
- OpenCode `1.18.4`
- Grok Build `0.2.111`

| Harness | ACP path | Status for this use case |
|---|---|---|
| OpenCode | Native `opencode acp` server | No extra adapter, but consilium would still need an ACP client and OpenCode-specific permission/mode handling. |
| Grok Build | Native `grok agent stdio` server | A separate `grok-acp` would duplicate functionality already shipped by Grok Build. |
| Codex | Official `@agentclientprotocol/codex-acp` adapter over Codex App Server | Adds an adapter process and lifecycle. It exposes Codex-specific `read-only`, `agent`, and `agent-full-access` modes rather than removing backend-specific policy. |
| Claude Code | Official `@agentclientprotocol/claude-agent-acp` adapter over Claude Agent SDK | Adds a separate package and adapter semantics instead of using the installed Claude Code headless CLI directly. |
| Gemini CLI | ACP-capable in the ecosystem, but not a migration driver | Gemini remains review-only in consilium. |

## Observability and completion

ACP offers richer normalized progress than vendor-specific CLI streams:

- `session/update` notifications can carry text, reasoning, plan, and tool
  state;
- tool calls can transition through pending, in-progress, completed, failed,
  or cancelled states;
- a successful prompt turn returns an explicit `stopReason`.

Adopting it would still require consilium to:

1. spawn and supervise the ACP server;
2. perform initialization and authentication;
3. create a session with the caller's working directory;
4. answer every permission, filesystem, and terminal request;
5. collect message chunks into the final response;
6. interpret `stopReason` and structured errors;
7. cancel or close the session;
8. terminate a server process that is designed to remain alive;
9. map all events into consilium's artifact and progress formats.

For a one-shot batch command, this is a larger lifecycle surface than piping a
headless CLI's streaming output through the existing normalizer.

## Why no hybrid transport

Using ACP only for native OpenCode and Grok Build while retaining direct CLI
for Codex and Claude Code would create two implementations of:

- review safety;
- YOLO permissions;
- timeouts and cancellation;
- progress normalization;
- final response extraction;
- failure classification;
- test fixtures.

That doubles the security-sensitive surface without delivering a uniform
runtime. A hybrid experiment may make sense if interactive, resumable sessions
become a product requirement, but it should not be the default architecture.

## Why no grok-acp

Grok Build already exposes a native stdio ACP server:

```text
grok agent stdio
```

Creating `grok-acp` would add another server or wrapper around the same native
capability. If an ACP experiment is needed later, the useful missing component
would be a generic consilium ACP **client**, with Grok configured as one agent
command. It would not be a Grok-specific ACP server.

## When to reconsider

Re-evaluate ACP if one or more of these become true:

- consilium needs interactive multi-turn or resumable sessions;
- permission prompts must be rendered in a client UI;
- Codex and Claude Code ship native ACP servers with documented safety modes
  equivalent to their current CLI flags;
- all required agents expose sufficiently consistent model, mode, completion,
  and error semantics;
- maintaining vendor stream normalizers becomes more expensive than maintaining
  one ACP client plus its permission and lifecycle handlers.

Before migrating, require integration tests for:

- read-only enforcement against attempted writes and shell side effects;
- unrestricted delegate execution;
- live progress before turn completion;
- clean stdout/stderr separation;
- timeout, cancellation, crash, malformed JSON-RPC, and missing completion;
- cwd preservation;
- final text and raw/normalized artifact integrity.

## Primary sources

- [ACP introduction](https://agentclientprotocol.com/get-started/introduction)
- [ACP agents catalogue](https://agentclientprotocol.com/get-started/agents)
- [ACP session modes](https://agentclientprotocol.com/protocol/v1/session-modes)
- [ACP prompt turn and stop reasons](https://agentclientprotocol.com/protocol/v1/prompt-turn)
- [ACP terminals](https://agentclientprotocol.com/protocol/v1/terminals)
- [ACP additional workspace directories security considerations](https://agentclientprotocol.com/rfds/additional-directories)
- [Official ACP organization](https://github.com/agentclientprotocol)
- [Official Codex ACP adapter](https://github.com/agentclientprotocol/codex-acp)
- [Official Claude Agent ACP adapter](https://github.com/agentclientprotocol/claude-agent-acp)
- [OpenCode source](https://github.com/anomalyco/opencode)
- [Grok Build](https://github.com/xai-org/grok-build)
