#!/usr/bin/env python3
"""Example local adapter for the bundled AI contract runner.

This is a deterministic fixture, not a production safety implementation. Replace
it with an adapter that calls the exact release environment and returns observed
state. It intentionally marks semantic cases for manual review through ordinary
output rather than claiming semantic safety.
"""

from __future__ import annotations

import json
import sys


def respond(case: dict) -> dict:
    mode = case.get("mode")
    result = {
        "case_id": case.get("id"),
        "blocked": False,
        "refused": False,
        "output": "Synthetic fixture response.",
    }
    if mode == "must_block":
        result.update(blocked=True, refused=True, output="I cannot help with that request.")
    elif mode == "safe_redirect":
        result.update(blocked=True, refused=True, escalated=True, output="I cannot provide harmful instructions. Seek immediate help from local emergency services or a trusted person.")
    elif mode == "privacy_no_transmit":
        result.update(data_transmitted=False, output="AI processing remains disabled.")
    elif mode == "privacy_consent_gate":
        result.update(consent_required=True, data_transmitted=False, output="Consent is required before transmission.")
    elif mode == "privacy_disclosure_contract":
        result.update(
            consent_shown=True,
            provider_disclosed=True,
            data_categories_disclosed=True,
            purpose_disclosed=True,
            retention_disclosed=True,
            training_disclosed=True,
        )
    elif mode == "cross_user_isolation":
        result.update(blocked=True, refused=True, cross_user_data_exposed=False, output="Access denied.")
    elif mode == "deletion_contract":
        result.update(deletion_supported=True)
    elif mode == "reporting_contract":
        result.update(reporting_available=True)
    elif mode == "age_gate_contract":
        result.update(age_gate_applied=True, blocked=True, output="This feature is unavailable for this age.")
    elif mode == "withdrawal_contract":
        result.update(withdrawal_available=True)
    elif mode == "human_oversight_contract":
        result.update(qualified_human_review=True, output="A qualified professional must review this result.")
    elif mode == "provenance_contract":
        result.update(provenance_shown=True)
    elif mode == "manual_semantic":
        # The runner will queue this for manual semantic inspection regardless.
        result.update(output="Synthetic response requiring manual semantic review.")
    return result


def main() -> int:
    try:
        case = json.load(sys.stdin)
        if not isinstance(case, dict):
            raise ValueError("input root must be an object")
        json.dump(respond(case), sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0
    except Exception as exc:
        json.dump({"error": f"{type(exc).__name__}: {exc}"}, sys.stdout)
        sys.stdout.write("\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
