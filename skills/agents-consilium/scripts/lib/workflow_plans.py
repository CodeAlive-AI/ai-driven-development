#!/usr/bin/env python3
"""Declarative workflow plans for Consilium review fan-out.

Plans are data consumed by workflow_runner.sh / Python helpers rather than
duplicated background-job blocks. Stage order is deterministic. Concurrency is
bounded via CONSILIUM_MAX_PARALLEL (default 0 = unlimited, matching historical
behavior).

Plan ids:
  ask            — parallel one-shot per selected agent (roles from config)
  basic          — security + correctness specialists
  specialists    — five specialist roles
  super          — multi-stage discovery + judge (h9 preset)
  ultra          — multi-stage discovery + probe + judge
"""
from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


@dataclass
class PassSpec:
    agent: str
    role: str
    cap: str = "uncapped"
    prompt: str = ""  # template filename under prompts/, empty = role wrap only
    stage: str = ""
    index: int = 0

    def artifact_key(self) -> str:
        if self.stage:
            return f"{self.stage}.{self.index}.{self.agent}.{self.role}"
        if self.role and self.role != "default":
            return f"{self.agent}.{self.role}"
        return self.agent

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["artifact_key"] = self.artifact_key()
        return d


@dataclass
class StageSpec:
    id: str
    kind: str  # parallel_discovery | sequential | dedup | judge | fanout_agents
    passes: List[PassSpec] = field(default_factory=list)
    # Optional judge/dedup config
    judge_agent: str = ""
    judge_fallback: str = ""
    description: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "kind": self.kind,
            "description": self.description,
            "judge_agent": self.judge_agent,
            "judge_fallback": self.judge_fallback,
            "passes": [p.to_dict() for p in self.passes],
        }


@dataclass
class WorkflowPlan:
    id: str
    mode: str
    stages: List[StageSpec]
    concurrency_default: int = 0  # 0 = unlimited
    description: str = ""

    def all_passes(self) -> List[PassSpec]:
        out: List[PassSpec] = []
        for st in self.stages:
            out.extend(st.passes)
        return out

    def agents_needed(self) -> List[str]:
        seen = []
        for p in self.all_passes():
            if p.agent and p.agent not in seen:
                seen.append(p.agent)
        for st in self.stages:
            if st.judge_agent and st.judge_agent not in seen:
                seen.append(st.judge_agent)
            if st.judge_fallback and st.judge_fallback not in seen:
                seen.append(st.judge_fallback)
        return seen

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "mode": self.mode,
            "description": self.description,
            "concurrency_default": self.concurrency_default,
            "agents_needed": self.agents_needed(),
            "stages": [s.to_dict() for s in self.stages],
        }


def skill_root() -> Path:
    return Path(__file__).resolve().parents[2]


def max_parallel() -> int:
    """Concurrency limit. 0 or unset = unlimited (historical default)."""
    raw = os.environ.get("CONSILIUM_MAX_PARALLEL", "0").strip()
    try:
        n = int(raw)
        return max(0, n)
    except ValueError:
        return 0


def plan_basic() -> WorkflowPlan:
    roles = ["security", "correctness"]
    # Agents are assigned at runtime via round-robin over enabled agents;
    # placeholder agent "*" means "assign from pool".
    passes = [
        PassSpec(agent="*", role=r, stage="code", index=i, prompt="")
        for i, r in enumerate(roles)
    ]
    return WorkflowPlan(
        id="basic",
        mode="review-code-basic",
        description="2 specialists: security + correctness",
        stages=[
            StageSpec(
                id="specialists",
                kind="fanout_roles",
                passes=passes,
                description="parallel specialist passes",
            )
        ],
    )


def plan_specialists() -> WorkflowPlan:
    roles = [
        "security",
        "correctness",
        "performance",
        "architecture",
        "consistency",
    ]
    passes = [
        PassSpec(agent="*", role=r, stage="code", index=i)
        for i, r in enumerate(roles)
    ]
    return WorkflowPlan(
        id="specialists",
        mode="review-code-specialists",
        description="5 specialists modeled on CodeAlive review crew",
        stages=[
            StageSpec(
                id="specialists",
                kind="fanout_roles",
                passes=passes,
            )
        ],
    )


def plan_super(judge_agent: str = "claude-sonnet") -> WorkflowPlan:
    small = [
        ("opencode-go-minimax", "analyst", "uncapped", "broad-analyst.txt"),
        ("opencode-go-qwen37-plus", "analyst", "uncapped", "broad-analyst.txt"),
        ("opencode-go-qwen37-plus", "lateral", "uncapped", "broad-lateral.txt"),
        ("opencode-go-glm", "architecture", "uncapped", "specialist.txt"),
        ("opencode-go-glm", "correctness", "uncapped", "specialist.txt"),
        ("opencode-go-qwen37-max", "architecture", "uncapped", "specialist.txt"),
        ("opencode-go-qwen37-max", "security", "uncapped", "specialist.txt"),
    ]
    frontier = [
        ("opencode", "analyst", "uncapped", "broad-analyst.txt"),
        ("claude-code", "lateral", "uncapped", "broad-lateral.txt"),
    ]
    stages = []
    idx = 0
    small_passes = []
    for agent, role, cap, prompt in small:
        small_passes.append(
            PassSpec(
                agent=agent,
                role=role,
                cap=cap,
                prompt=prompt,
                stage="discovery-small",
                index=idx,
            )
        )
        idx += 1
    stages.append(
        StageSpec(
            id="discovery-small",
            kind="parallel_discovery",
            passes=small_passes,
        )
    )
    front_passes = []
    for agent, role, cap, prompt in frontier:
        front_passes.append(
            PassSpec(
                agent=agent,
                role=role,
                cap=cap,
                prompt=prompt,
                stage="discovery-frontier",
                index=idx,
            )
        )
        idx += 1
    stages.append(
        StageSpec(
            id="discovery-frontier",
            kind="parallel_discovery",
            passes=front_passes,
        )
    )
    stages.append(StageSpec(id="dedup", kind="dedup", description="deterministic union"))
    stages.append(
        StageSpec(
            id="judge",
            kind="judge",
            judge_agent=judge_agent,
            description="LLM judge over unioned findings",
        )
    )
    return WorkflowPlan(
        id="super",
        mode="review-code-super",
        description="superreview h9 preset: discovery + dedup + judge",
        stages=stages,
    )


def plan_ultra(
    judge_agent: str = "claude-sonnet",
    judge_fallback: str = "codex",
) -> WorkflowPlan:
    broad = [
        ("codex", "analyst", "uncapped", "broad-analyst.txt"),
        ("claude-code", "analyst", "uncapped", "broad-analyst.txt"),
        ("opencode", "lateral", "uncapped", "broad-lateral.txt"),
        ("opencode-go-qwen37-max", "analyst", "uncapped", "broad-analyst.txt"),
    ]
    specialist_roles = [
        "security",
        "correctness",
        "performance",
        "architecture",
        "consistency",
    ]
    # Historical ultrareview matrix: 3 OC-Go models × 5 specialist roles = 15.
    specialist_models = [
        "opencode-go-minimax",
        "opencode-go-kimi",
        "opencode-go-qwen37-plus",
    ]
    stages: List[StageSpec] = []
    idx = 0
    # Stage ids match historical ultrareview artifact keys: broad.* / specialists.*
    broad_passes = []
    for agent, role, cap, prompt in broad:
        broad_passes.append(
            PassSpec(
                agent=agent,
                role=role,
                cap=cap,
                prompt=prompt,
                stage="broad",
                index=idx,
            )
        )
        idx += 1
    stages.append(
        StageSpec(id="broad", kind="parallel_discovery", passes=broad_passes)
    )

    # Full cross-product (model outer, role inner) preserves historical ordering
    # and 15 specialist invocations — not one model per role.
    spec_passes = []
    for model in specialist_models:
        for role in specialist_roles:
            spec_passes.append(
                PassSpec(
                    agent=model,
                    role=role,
                    cap="uncapped",
                    prompt="specialist.txt",
                    stage="specialists",
                    index=idx,
                )
            )
            idx += 1
    stages.append(
        StageSpec(
            id="specialists",
            kind="parallel_discovery",
            passes=spec_passes,
        )
    )
    # Probe is its own sequential stage after specialists complete (stage barrier).
    stages.append(
        StageSpec(
            id="probe",
            kind="sequential",
            passes=[
                PassSpec(
                    agent="opencode-go-glm",
                    role="auditor",
                    cap="uncapped",
                    prompt="probe-generic.txt",
                    stage="probe",
                    index=idx,
                )
            ],
        )
    )
    stages.append(StageSpec(id="dedup", kind="dedup"))
    stages.append(
        StageSpec(
            id="judge",
            kind="judge",
            judge_agent=judge_agent,
            judge_fallback=judge_fallback,
        )
    )
    return WorkflowPlan(
        id="ultra",
        mode="review-code-ultra",
        description="ultrareview: broad + specialists + probe + judge",
        stages=stages,
    )


def plan_ask(agent_ids: Sequence[str]) -> WorkflowPlan:
    passes = [
        PassSpec(agent=a, role="default", stage="ask", index=i)
        for i, a in enumerate(agent_ids)
    ]
    return WorkflowPlan(
        id="ask",
        mode="review-ask",
        description="parallel independent opinions",
        stages=[
            StageSpec(id="ask", kind="fanout_agents", passes=passes)
        ],
    )


def get_plan(
    plan_id: str,
    *,
    agents: Optional[Sequence[str]] = None,
    judge_agent: str = "claude-sonnet",
    judge_fallback: str = "codex",
) -> WorkflowPlan:
    pid = plan_id.strip().lower()
    if pid in ("basic", "code-basic", "review-code-basic"):
        return plan_basic()
    if pid in ("specialists", "code-specialists", "review-code-specialists"):
        return plan_specialists()
    if pid in ("super", "superreview", "review-code-super"):
        return plan_super(judge_agent=judge_agent)
    if pid in ("ultra", "ultrareview", "review-code-ultra"):
        return plan_ultra(judge_agent=judge_agent, judge_fallback=judge_fallback)
    if pid in ("ask", "review-ask"):
        return plan_ask(agents or [])
    raise KeyError(f"unknown workflow plan: {plan_id!r}")


def assign_agents_to_roles(
    plan: WorkflowPlan, enabled_agents: Sequence[str]
) -> WorkflowPlan:
    """Fill agent='*' placeholders via round-robin over enabled_agents."""
    if not enabled_agents:
        raise ValueError("no enabled agents for role assignment")
    new_stages = []
    for st in plan.stages:
        new_passes = []
        for p in st.passes:
            if p.agent == "*":
                agent = enabled_agents[p.index % len(enabled_agents)]
                new_passes.append(
                    PassSpec(
                        agent=agent,
                        role=p.role,
                        cap=p.cap,
                        prompt=p.prompt,
                        stage=p.stage or st.id,
                        index=p.index,
                    )
                )
            else:
                new_passes.append(p)
        new_stages.append(
            StageSpec(
                id=st.id,
                kind=st.kind,
                passes=new_passes,
                judge_agent=st.judge_agent,
                judge_fallback=st.judge_fallback,
                description=st.description,
            )
        )
    return WorkflowPlan(
        id=plan.id,
        mode=plan.mode,
        stages=new_stages,
        concurrency_default=plan.concurrency_default,
        description=plan.description,
    )


def _main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="Consilium declarative workflow plans")
    ap.add_argument("plan", help="ask|basic|specialists|super|ultra")
    ap.add_argument("--agents", default="", help="comma-separated agents for ask/basic")
    ap.add_argument("--judge", default="claude-sonnet")
    ap.add_argument("--judge-fallback", default="codex")
    ap.add_argument("--max-parallel", type=int, default=-1,
                    help="echo effective concurrency (-1 = from env)")
    ap.add_argument("--shell", action="store_true",
                    help="Emit shell-friendly pass lines: stage|index|agent|role|cap|prompt|artifact_key")
    args = ap.parse_args()

    agents = [a for a in args.agents.split(",") if a]
    try:
        plan = get_plan(
            args.plan,
            agents=agents,
            judge_agent=args.judge,
            judge_fallback=args.judge_fallback,
        )
        if agents and any(p.agent == "*" for p in plan.all_passes()):
            plan = assign_agents_to_roles(plan, agents)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 4

    if args.shell:
        for st in plan.stages:
            if st.kind in ("dedup", "judge"):
                print(
                    f"#{st.kind}|{st.id}|judge={st.judge_agent}|fallback={st.judge_fallback}"
                )
                continue
            for p in st.passes:
                print(
                    f"{p.stage or st.id}|{p.index}|{p.agent}|{p.role}|{p.cap}|"
                    f"{p.prompt}|{p.artifact_key()}"
                )
        mp = args.max_parallel if args.max_parallel >= 0 else max_parallel()
        print(f"#concurrency|{mp}")
        return 0

    d = plan.to_dict()
    d["concurrency"] = args.max_parallel if args.max_parallel >= 0 else max_parallel()
    print(json.dumps(d, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
