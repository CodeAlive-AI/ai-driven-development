#include <cassert>
#include <cstdint>
#include <cstdio>
#include <random>

#include "../core.hpp"

using namespace memoryguard;

namespace {

Sample sample(uint64_t second, uint64_t percent, uint64_t swap = 0, int pressure = 0) {
  Sample result;
  result.second = second;
  result.segments = percent;
  result.segment_limit = 100;
  result.swap_used = swap;
  result.pressure = pressure;
  return result;
}

Candidate tier_a(int pid, int pgid, uint64_t mib, bool frozen = false) {
  Candidate result;
  result.pid = pid;
  result.pgid = pgid;
  result.tier = Tier::a;
  result.footprint = mib * kMiB;
  result.frozen = frozen;
  result.freeze_pending = !frozen;
  result.eligible = true;
  return result;
}

// Implements concise candidates for incident-tier replay fixtures.
Candidate candidate_tier(int pid, Tier tier, uint64_t mib) {
  Candidate result;
  result.pid = pid;
  result.pgid = pid;
  result.tier = tier;
  result.footprint = mib * kMiB;
  result.freeze_pending = tier == Tier::a;
  result.eligible = tier != Tier::protected_process;
  return result;
}

// Implements bounded candidate insertion for replay populations.
size_t append_candidate(Candidate* candidates, size_t& count, Candidate candidate) {
  assert(count < kMaxCandidates);
  candidates[count] = candidate;
  return count++;
}

// Implements action-to-candidate lookup in deterministic replay tests.
Candidate* find_candidate(Candidate* candidates, size_t count, int pid) {
  for (size_t i = 0; i < count; ++i)
    if (candidates[i].pid == pid)
      return &candidates[i];
  return nullptr;
}

// Implements the persistent agent, application-helper and protected incident set.
void add_incident_non_a_candidates(Candidate* candidates, size_t& count) {
  const uint64_t agents[] = {204, 250, 300, 350, 410, 204, 300, 400};
  for (size_t i = 0; i < sizeof(agents) / sizeof(agents[0]); ++i)
    append_candidate(candidates, count, candidate_tier(1000 + static_cast<int>(i), Tier::b,
                                                        agents[i]));
  const uint64_t nodes[] = {400, 600, 800};
  for (size_t i = 0; i < sizeof(nodes) / sizeof(nodes[0]); ++i)
    append_candidate(candidates, count, candidate_tier(1010 + static_cast<int>(i), Tier::b,
                                                        nodes[i]));
  const uint64_t helpers[] = {400, 700, 900, 1100};
  for (size_t i = 0; i < sizeof(helpers) / sizeof(helpers[0]); ++i)
    append_candidate(candidates, count, candidate_tier(1020 + static_cast<int>(i), Tier::c,
                                                        helpers[i]));
  Candidate protected_process = candidate_tier(1030, Tier::protected_process, 2048);
  protected_process.eligible = false;
  append_candidate(candidates, count, protected_process);
}

// Implements one separately tracked Python unit in the incident replay.
void append_python(Candidate* candidates, size_t& count, int& next_pid, uint64_t mib) {
  const int pid = next_pid++;
  append_candidate(candidates, count, tier_a(pid, pid, mib));
}

// Implements the incident's Python arrivals at seconds 0, 11 and 26 through 106.
void add_incident_python(int relative_second, Candidate* candidates, size_t& count,
                         int& next_pid) {
  if (relative_second == 0)
    append_python(candidates, count, next_pid, 3072);
  if (relative_second == 11)
    for (int i = 0; i < 8; ++i)
      append_python(candidates, count, next_pid, 2150);
  const uint64_t later_mib[] = {410, 512, 620, 750, 900, 1100, 1400, 1700, 2100, 2500,
                                3000, 3500, 4000, 4500, 5120, 410, 600, 2200, 4800, 1000};
  for (int i = 0; i < 20; ++i) {
    const int arrival = 26 + i * 80 / 19;
    if (relative_second == arrival)
      append_python(candidates, count, next_pid, later_mib[static_cast<size_t>(i)]);
  }
}

// Implements the measured segment trajectory with and without an effective guard.
uint64_t incident_segments(int relative_second, bool effective) {
  if (relative_second < 0)
    return 12;
  if (effective) {
    if (relative_second < 28)
      return 12;
    return relative_second <= 106 ? 60 : 42;
  }
  if (relative_second < 28)
    return 12;
  if (relative_second <= 80)
    return 12 + static_cast<uint64_t>(relative_second - 28) * 48 / 52;
  if (relative_second <= 120)
    return 60;
  if (relative_second <= 200)
    return 60 + static_cast<uint64_t>(relative_second - 120) * 20 / 80;
  if (relative_second <= 240)
    return 80 + static_cast<uint64_t>(relative_second - 200) * 20 / 40;
  return 100;
}

// Implements the reported swap growth from 0.3 GiB to 7.9 GiB at second 40.
uint64_t incident_swap_bytes(int relative_second, bool effective = false) {
  if (effective && relative_second > 28)
    relative_second = 28;
  if (relative_second < 0)
    return 3 * kGiB / 10;
  if (relative_second < 11)
    return 4 * kGiB / 10 + static_cast<uint64_t>(relative_second) * 6 * kGiB / 110;
  if (relative_second < 26)
    return kGiB + static_cast<uint64_t>(relative_second - 11) * kGiB / 15;
  if (relative_second < 40)
    return 2 * kGiB + static_cast<uint64_t>(relative_second - 26) * 59 * kGiB / 140;
  return 79 * kGiB / 10;
}

// Calm measurements for an hour never produce decisions.
void calm_noise_for_an_hour() {
  State state;
  Candidate candidate = tier_a(1, 1, 700);
  for (uint64_t second = 1; second <= 3600; ++second) {
    const uint64_t percent = 10 + ((second / 120) % 16);
    const Sample current = sample(second, percent, (second % 10) * 1024 * 1024);
    const Actions actions = decide(state, current, &candidate, 1);
    assert(actions.count == 0);
    assert(actions.level == Level::calm);
  }
}

// One high sample cannot change the level or trigger an action.
void one_sample_spike() {
  assert(!at_or_above(1, 100, 0));
  State state;
  Candidate candidate = tier_a(1, 1, 800);
  const Actions actions = decide(state, sample(1, 85), &candidate, 1);
  assert(actions.level == Level::calm && actions.count == 0);
}

// Stable 70 percent freezes A once, then kills only frozen units at 30-second spacing.
void stable_alert_for_an_hour() {
  State state;
  Candidate candidates[] = {tier_a(1, 1, 800, false),
                            tier_a(2, 2, 600, false),
                            tier_a(3, 3, 450, false),
                            candidate_tier(4, Tier::b, 900),
                            candidate_tier(5, Tier::c, 1000),
                            candidate_tier(6, Tier::protected_process, 4096)};
  size_t kills = 0;
  uint64_t previous_kill = 0;
  for (uint64_t second = 1; second <= 3600; ++second) {
    const Actions actions = decide(state, sample(second, 70), candidates, 6);
    for (size_t i = 0; i < actions.count; ++i) {
      const Action& action = actions.items[i];
      if (action.kind == ActionKind::freeze) {
        assert(action.pgid == 1 || action.pgid == 2);
        for (Candidate& candidate : candidates) {
          if (candidate.pgid == action.pgid) {
            candidate.frozen = true;
            candidate.freeze_pending = false;
          }
        }
      } else if (action.kind == ActionKind::kill) {
        assert(action.pgid == 1 || action.pgid == 2);
        assert(candidates[action.pgid - 1].frozen);
        assert(previous_kill == 0 || second - previous_kill >= 30);
        previous_kill = second;
        candidates[action.pgid - 1].eligible = false;
        ++kills;
      } else {
        assert(false);
      }
    }
  }
  assert(state.level == Level::alert);
  assert(kills == 0);
}

// The effective trajectory freezes two units at the initial trend and later resumes them.
void incident_effective_replay() {
  State state;
  Candidate candidates[kMaxCandidates]{};
  size_t count = 0;
  int next_pid = 1;
  int first_alert = -1;
  size_t freezes = 0;
  size_t resumes = 0;
  uint64_t prior_resume_second = 0;
  uint64_t prior_resume_footprint = 0;
  add_incident_non_a_candidates(candidates, count);
  for (int relative = -60; relative <= 600; ++relative) {
    add_incident_python(relative, candidates, count, next_pid);
    const uint64_t second = static_cast<uint64_t>(1000 + relative);
    const Actions actions = decide(
        state, sample(second, incident_segments(relative, true),
                      incident_swap_bytes(relative, true)),
        candidates, count);
    if (actions.level == Level::alert && first_alert < 0)
      first_alert = relative;
    for (size_t i = 0; i < actions.count; ++i) {
      const Action& action = actions.items[i];
      Candidate* candidate = find_candidate(candidates, count, action.pid);
      assert(candidate != nullptr);
      if (action.kind == ActionKind::freeze) {
        assert(candidate->tier == Tier::a && !candidate->frozen);
        candidate->frozen = true;
        candidate->freeze_pending = false;
        ++freezes;
        record_action(state, second);
      } else if (action.kind == ActionKind::resume) {
        assert(candidate->tier == Tier::a && candidate->frozen);
        assert(prior_resume_second == 0 || second - prior_resume_second >= 15);
        assert(candidate->footprint >= prior_resume_footprint);
        candidate->frozen = false;
        prior_resume_second = second;
        prior_resume_footprint = candidate->footprint;
        ++resumes;
      } else {
        assert(false);
      }
    }
  }
  size_t expected_freezes = 0;
  for (size_t i = 0; i < count; ++i) {
    const Candidate& candidate = candidates[i];
    if (candidate.tier == Tier::a && candidate.footprint >= 500 * kMiB) {
      ++expected_freezes;
      assert(!candidate.frozen);
    }
    if (candidate.tier != Tier::a)
      assert(!candidate.frozen);
  }
  assert(first_alert >= 0 && first_alert <= 45);
  assert(freezes == expected_freezes && resumes == expected_freezes);
  assert(state.level == Level::calm);
}

// The unmitigated incident reaches 100 percent at 240 seconds and kills by tier.
void incident_without_effect_replay() {
  State state;
  Candidate candidates[kMaxCandidates]{};
  size_t count = 0;
  int next_pid = 1;
  int last_phase = -1;

  uint64_t last_kill_second = 0;
  size_t kills = 0;
  bool reached_hundred = false;
  add_incident_non_a_candidates(candidates, count);
  for (int relative = -60; relative <= 500; ++relative) {
    add_incident_python(relative, candidates, count, next_pid);
    const uint64_t second = static_cast<uint64_t>(1000 + relative);
    const uint64_t percent = incident_segments(relative, false);
    const Actions actions = decide(
        state, sample(second, percent, incident_swap_bytes(relative)), candidates, count);
    if (relative == 240) {
      assert(percent == 100);
      reached_hundred = true;
    }
    size_t kills_this_decision = 0;
    for (size_t i = 0; i < actions.count; ++i) {
      const Action& action = actions.items[i];
      Candidate* candidate = find_candidate(candidates, count, action.pid);
      assert(candidate != nullptr);
      if (action.kind == ActionKind::freeze) {
        assert(candidate->tier == Tier::a && !candidate->frozen);
        candidate->frozen = true;
        candidate->freeze_pending = false;
        record_action(state, second);
        continue;
      }
      if (action.kind != ActionKind::kill)
        assert(false);
      ++kills_this_decision;
      assert(candidate->eligible && candidate->tier != Tier::protected_process);
      assert(last_kill_second == 0 || second - last_kill_second >= 3);
      last_kill_second = second;
      ++kills;
      const int phase = candidate->frozen
                            ? 0
                            : candidate->tier == Tier::a ? 1
                            : candidate->tier == Tier::b ? 2
                                                         : 3;
      if (actions.level != Level::emergency) assert(candidate->tier == Tier::a);
      last_phase = phase;
      if (candidate->tier == Tier::b)
        assert(at_or_above(percent, 100, 88));
      if (candidate->tier == Tier::c)
        assert(at_or_above(percent, 100, 93));
      candidate->eligible = false;
    }
    assert(kills_this_decision <= 1);
  }
  assert(reached_hundred && state.level == Level::emergency);
  assert(kills > 0 && last_phase == 3);
  for (size_t i = 0; i < count; ++i) {
    const Candidate& candidate = candidates[i];
    const bool kill_eligible = candidate.footprint >= 300 * kMiB &&
                               candidate.tier != Tier::protected_process;
    if (kill_eligible && candidate.eligible) {
      std::fprintf(stderr, "survivor pid=%d tier=%u footprint_mib=%llu frozen=%d\n",
                   candidate.pid, static_cast<unsigned>(candidate.tier),
                   static_cast<unsigned long long>(candidate.footprint / kMiB),
                   candidate.frozen ? 1 : 0);
      assert(!candidate.eligible);
    }
    if (candidate.tier == Tier::protected_process)
      assert(!candidate.eligible);
  }
}

// A trend-only EMERGENCY never opens the segment-gated B and C tiers.
void trend_only_emergency() {
  State state;
  Candidate candidates[] = {tier_a(1, 1, 700, true),
                            tier_a(2, 2, 700),
                            candidate_tier(3, Tier::b, 1024),
                            candidate_tier(4, Tier::c, 1024)};
  Actions last;
  int first_kill = 0;
  for (uint64_t second = 1; second <= 40; ++second) {
    last = decide(state, sample(second, 50 + second), candidates, 4);
    if (last.count != 0 && last.items[0].kind == ActionKind::kill && first_kill == 0)
      first_kill = last.items[0].pid;
  }
  assert(state.level == Level::emergency);
  assert(first_kill == 1);
}

// Action-relative trend history prevents a pre-freeze rise from causing EMERGENCY.
void trend_resets_after_freeze() {
  State state;
  Candidate candidate = tier_a(1, 1, 900);
  for (uint64_t second = 1; second <= 40; ++second) {
    const uint64_t percent = second < 10 ? 45 : 45 + second / 2;
    Actions actions = decide(state, sample(second, percent), &candidate, 1);
    if (actions.count && actions.items[0].kind == ActionKind::freeze) {
      candidate.frozen = true;
      candidate.freeze_pending = false;
      record_action(state, second);
    }
  }
  for (uint64_t second = 41; second <= 90; ++second) {
    const Actions actions = decide(state, sample(second, 65), &candidate, 1);
    assert(actions.level != Level::emergency);
  }
}

// A recovering spike returns to CALM and resumes a stopped unit without killing.
void recovering_spike() {
  State state;
  Candidate candidate = tier_a(1, 1, 700);
  Actions result;
  for (uint64_t second = 1; second <= 3; ++second) {
    result = decide(state, sample(second, second < 3 ? 12 : 70), &candidate, 1);
  }
  result = decide(state, sample(4, 70), &candidate, 1);
  assert(result.count == 1 && result.items[0].kind == ActionKind::freeze);
  candidate.frozen = true;
  candidate.freeze_pending = false;
  bool resumed = false;
  for (uint64_t second = 5; second <= 66; ++second) {
    result = decide(state, sample(second, 20), &candidate, 1);
    if (result.count == 1 && result.items[0].kind == ActionKind::resume) {
      resumed = true;
      candidate.frozen = false;
      candidate.freeze_pending = true;
    }
  }
  assert(state.level == Level::calm);
  assert(resumed);
}

// A unit frozen and resumed in the repeat window is killed at the next ALERT.
void repeat_offender_window() {
  State state;
  Candidate candidate = tier_a(1, 1, 700);
  candidate.repeat_offender = true;
  candidate.last_resume_second = 100;
  decide(state, sample(101, 70), &candidate, 1);
  const Actions killed = decide(state, sample(102, 70), &candidate, 1);
  assert(killed.count == 1 && killed.items[0].kind == ActionKind::freeze);
  State outside;
  candidate.last_resume_second = 100;
  decide(outside, sample(2000, 70), &candidate, 1);
  const Actions frozen = decide(outside, sample(2001, 70), &candidate, 1);
  assert(frozen.count == 1 && frozen.items[0].kind == ActionKind::freeze);
}

// A sustained trend alarm can freeze repeats but cannot escalate until pressure is measured.
void trend_alert_never_kills() {
  Config config;
  config.alert_trend_pct = 50;
  config.alert_trend_min_pct = 45;
  State state;
  Candidate frozen = tier_a(1, 1, 700, true);
  decide(state, sample(1, 45), &frozen, 1, config);
  for (uint64_t second = 31; second <= 331; ++second) {
    Actions actions = decide(state, sample(second, 50), &frozen, 1, config);
    assert(actions.count == 0);
  }
  assert(state.level == Level::alert && state.alert_since == 32);
  Actions killed = decide(state, sample(332, 78), &frozen, 1, config);
  assert(killed.count == 1 && killed.items[0].kind == ActionKind::kill);
  assert(killed.kill_basis == KillBasis::segments);

  State repeat;
  Candidate candidate = tier_a(2, 2, 700);
  candidate.repeat_offender = true;
  candidate.last_resume_second = 10;
  decide(repeat, sample(1, 45), &candidate, 1, config);
  decide(repeat, sample(31, 50), &candidate, 1, config);
  Actions again = decide(repeat, sample(32, 50), &candidate, 1, config);
  assert(again.count == 1 && again.items[0].kind == ActionKind::freeze);
}

// Alternating rises and recovery in the observed 45–58% range never produce kills.
void alternating_trend_replay() {
  State state;
  Candidate candidate = tier_a(1, 1, 700);
  size_t freezes = 0, alerts = 0, calms = 0;
  Level previous = Level::calm;
  for (uint64_t second = 1; second <= 900; ++second) {
    const uint64_t phase = (second - 1) % 180;
    const uint64_t percent = phase < 65 ? 45 + phase / 5 : 45;
    Actions actions = decide(state, sample(second, percent), &candidate, 1);
    if (actions.level != previous) {
      if (actions.level == Level::alert) ++alerts;
      if (actions.level == Level::calm) ++calms;
      previous = actions.level;
    }
    for (size_t i = 0; i < actions.count; ++i) {
      assert(actions.items[i].kind != ActionKind::kill);
      if (actions.items[i].kind == ActionKind::freeze) {
        ++freezes;
        candidate.frozen = true;
        candidate.freeze_pending = false;
      } else if (actions.items[i].kind == ActionKind::resume) {
        candidate.frozen = false;
        candidate.freeze_pending = true;
        candidate.repeat_offender = true;
        candidate.last_resume_second = second;
      }
    }
  }
  assert(freezes == 0 && alerts == 0 && calms == 0);
}

// Swap cannot authorize a kill; qualifying critical pressure can.
void measured_pressure_bases() {
  Candidate candidate = tier_a(1, 1, 700, true);
  State swap;
  swap.level = Level::alert;
  swap.alert_since = 1;
  decide(swap, sample(1, 50), &candidate, 1);
  Sample lowdisk = sample(121, 50, 2 * kGiB);
  lowdisk.disk_free = 19 * kGiB;
  Actions a = decide(swap, lowdisk, &candidate, 1);
  assert(a.count == 0 && a.kill_basis == KillBasis::none);
  State pressure;
  pressure.level = Level::alert;
  pressure.alert_since = 1;
  decide(pressure, sample(1, 45), nullptr, 0);
  pressure.calm_since = 0;
  decide(pressure, sample(119, 50, 0, 4), nullptr, 0);
  decide(pressure, sample(120, 50, 0, 4), nullptr, 0);
  a = decide(pressure, sample(121, 50, 0, 4), &candidate, 1);
  assert(a.count == 1 && a.items[0].kind == ActionKind::kill && a.kill_basis == KillBasis::pressure_rising);

}

// Irregular sample gaps preserve counters and use actual elapsed trend time.
void irregular_sampling() {
  State state;
  const uint64_t seconds[] = {1, 5, 14, 16, 46, 47};
  const uint64_t values[] = {10, 20, 30, 40, 60, 61};
  Actions result;
  for (size_t i = 0; i < 6; ++i) {
    result = decide(state, sample(seconds[i], values[i]), nullptr, 0);
  }
  assert(result.level == Level::alert);
  assert(trend_reaches(state, sample(47, 61), 90, 240, 30));
}

// Invalid input does not alter the active level or emit a decision.
void invalid_sample_preserves_alert() {
  State state;
  Candidate candidate = tier_a(1, 1, 800, true);
  decide(state, sample(1, 70), &candidate, 1);
  decide(state, sample(2, 70), &candidate, 1);
  Sample invalid = sample(3, 70);
  invalid.valid = false;
  const Actions result = decide(state, invalid, &candidate, 1);
  assert(result.count == 0 && result.level == Level::alert);
}

// Classification protects system, app-main, terminal, foreign-user and pattern paths.
void classification_table() {
  ProcessFacts facts;
  facts.path = "/Applications/Editor.app/Contents/MacOS/Editor";
  facts.app_main = true;
  assert(classify(facts) == Tier::protected_process);
  facts = {};
  facts.path = "/Applications/Editor.app/Contents/Frameworks/Nested.app/Contents/X";
  facts.helper_in_app = true;
  assert(classify(facts) == Tier::c);
  facts = {};
  facts.age_seconds = 5 * 60;
  assert(classify(facts) == Tier::a);
  facts.age_seconds = 40 * 60;
  assert(classify(facts) == Tier::b);
  facts = {};
  facts.name = "node";
  facts.age_seconds = 2 * 60;
  assert(classify(facts) == Tier::a);
  facts.protected_name = true;
  assert(classify(facts) == Tier::protected_process);
  facts = {};
  facts.path = "/System/Library/foo";
  assert(classify(facts) == Tier::protected_process);
  facts.path = "/usr/libexec/foo";
  assert(classify(facts) == Tier::protected_process);
  facts = {};
  facts.protected_name = true;
  assert(classify(facts) == Tier::protected_process);
  facts = {};
  facts.uid = 501;
  facts.owner_uid = 502;
  assert(classify(facts) == Tier::protected_process);
  facts = {};
  facts.protected_pattern = true;
  assert(classify(facts) == Tier::protected_process);
  const char* roots[] = {"/usr/sbin/sshd", "/sbin/launchd", "/Library/Apple/foo"};
  for (const char* root : roots) {
    facts = {};
    facts.path = root;
    assert(classify(facts) == Tier::protected_process);
  }
  const char* agents[] = {"claude", "codex", "devin"};
  for (const char* agent : agents) {
    facts = {};
    facts.name = agent;
    facts.agent_runtime = true;
    assert(classify(facts) == Tier::b);
  }
  facts = {};
  facts.age_seconds = 40 * 60;
  facts.footprint = 7 * kGiB;
  facts.runaway_min = 6 * kGiB;
  assert(classify(facts) == Tier::a);
  facts = {};
  facts.helper_in_app = true;
  facts.footprint = 7 * kGiB;
  facts.runaway_min = 6 * kGiB;
  assert(classify(facts) == Tier::a);
  facts = {};
  facts.app_main = true;
  facts.footprint = 7 * kGiB;
  facts.runaway_min = 6 * kGiB;
  assert(classify(facts) == Tier::protected_process);
  facts = {};
  facts.agent_runtime = true;
  facts.footprint = 7 * kGiB;
  facts.runaway_min = 6 * kGiB;
  assert(classify(facts) == Tier::b);
}

// Trend projections below their current-segment floors stay inert.
void calibrated_trend_floors() {
  Config config;
  assert(config.alert_trend_min_pct == 45);
  assert(config.emergency_trend_min_pct == 65);
  State alert_28;
  decide(alert_28, sample(1, 20), nullptr, 0, config);
  const Sample at_28 = sample(31, 28);
  decide(alert_28, at_28, nullptr, 0, config);
  assert(measure_trend(alert_28, at_28, config.trend_horizon,
                       kAlertSlopeWindowSeconds).projected_pct >= 60);
  assert(!alert_now(alert_28, at_28, config));

  State alert_33;
  Sample base_33 = sample(1, 201);
  base_33.segment_limit = 800;
  decide(alert_33, base_33, nullptr, 0, config);
  Sample at_33 = sample(31, 264);
  at_33.segment_limit = 800;
  decide(alert_33, at_33, nullptr, 0, config);
  assert(measure_trend(alert_33, at_33, config.trend_horizon,
                       kAlertSlopeWindowSeconds).projected_pct >= 64);
  assert(!alert_now(alert_33, at_33, config));

  State alert_50;
  Sample base_50 = sample(1, 179);
  base_50.segment_limit = 400;
  decide(alert_50, base_50, nullptr, 0, config);
  Sample at_50 = sample(31, 200);
  at_50.segment_limit = 400;
  decide(alert_50, at_50, nullptr, 0, config);
  assert(measure_trend(alert_50, at_50, config.trend_horizon,
                       kAlertSlopeWindowSeconds).projected_pct >= 70);
  assert(!alert_now(alert_50, at_50, config));

  State emergency_50;
  decide(emergency_50, base_50, nullptr, 0, config);
  const Sample emergency_at_50 = at_50;
  decide(emergency_50, emergency_at_50, nullptr, 0, config);
  assert(!emergency_now(emergency_50, emergency_at_50, config));
}

// A 7 GiB runaway tier-B process freezes in ALERT and leads a 5 GiB A in EMERGENCY.
void runaway_alert_and_emergency_priority() {
  Candidate runaway = candidate_tier(1, Tier::a, 7 * 1024);
  runaway.runaway = true;
  Candidate batch = candidate_tier(2, Tier::a, 5 * 1024);
  Candidate candidates[] = {batch, runaway};
  State alert;
  decide(alert, sample(1, 70), candidates, 2);
  const Actions frozen = decide(alert, sample(2, 70), candidates, 2);
  assert(frozen.count == 2);
  assert(frozen.items[0].kind == ActionKind::freeze && frozen.items[0].pid == 1);
  assert(frozen.items[1].kind == ActionKind::freeze && frozen.items[1].pid == 2);

  State emergency;
  const Actions first = decide(emergency, sample(1, 80), candidates, 2);
  const Actions second = decide(emergency, sample(2, 80), candidates, 2);
  assert(first.count == 0);
  assert(second.level == Level::emergency && second.count == 1);
  assert(second.items[0].kind == ActionKind::kill && second.items[0].pid == 1);
}

// Randomized candidates preserve eligibility, tier gates, and kill cadence invariants.
void randomized_invariants() {
  std::mt19937 random(0x14112026);
  State state;
  Candidate candidates[24]{};
  for (int i = 0; i < 24; ++i) {
    const Tier tier = static_cast<Tier>(i % 4);
    candidates[i] = candidate_tier(i + 1, tier, 100 + random() % 1200);
    candidates[i].growth30 = random() % 100;
  }
  uint64_t second = 0;
  uint64_t last_kill = 0;
  for (size_t step = 0; step < 10000; ++step) {
    second += 1 + random() % 9;
    const uint64_t percent = 10 + random() % 90;
    const Sample current = sample(second, percent);
    const Actions actions = decide(state, current, candidates, 24);
    const bool alerting = alert_now(state, current, Config{});
    const bool emergency = emergency_now(state, current, Config{});
    size_t kills = 0;
    for (size_t i = 0; i < actions.count; ++i) {
      const Action& action = actions.items[i];
      Candidate& candidate = candidates[action.pid - 1];
      assert(candidate.eligible);
      assert(candidate.tier != Tier::protected_process);
      if (action.kind == ActionKind::freeze) {
        assert(candidate.tier == Tier::a && candidate.footprint >= 500 * kMiB);
        assert(alerting || emergency);
        candidate.frozen = true;
        candidate.freeze_pending = false;
      }
      if (action.kind == ActionKind::resume) {
        candidate.frozen = false;
        candidate.freeze_pending = true;
      }
      if (action.kind == ActionKind::kill) {
        ++kills;
        assert(actions.level != Level::calm);
        assert(actions.kill_basis != KillBasis::none);
        if (candidate.tier == Tier::b)
          assert(percent >= 88);
        if (candidate.tier == Tier::c)
          assert(percent >= 93);
        assert(last_kill == 0 || second - last_kill >= 3);
        last_kill = second;
        candidates[action.pid - 1].eligible = false;
      }
    }
    assert(kills <= 1);
  }
}

// EMERGENCY demotes immediately below 80 percent and ALERT never kills unfrozen units.
void emergency_drops_to_alert() {
  State state;
  Candidate candidates[] = {tier_a(1, 1, 900, true), tier_a(2, 2, 850, true),
                            tier_a(3, 3, 800, false), tier_a(4, 4, 700, false)};
  Actions actions = decide(state, sample(1, 85), candidates, 4);
  actions = decide(state, sample(2, 85), candidates, 4);
  assert(actions.level == Level::emergency && actions.items[0].kind == ActionKind::kill);
  candidates[0].eligible = false;
  actions = decide(state, sample(5, 85), candidates, 4);
  assert(actions.count == 1 && actions.items[0].pid == 2);
  candidates[1].eligible = false;
  for (uint64_t second = 6; second < 606; ++second) {
    actions = decide(state, sample(second, 70), candidates, 4);
    assert(actions.level != Level::emergency);
    for (size_t i = 0; i < actions.count; ++i)
      assert(actions.items[i].kind != ActionKind::kill ||
             candidates[actions.items[i].pid - 1].frozen);
  }
}

// The 120-second frozen-kill rule still freezes a new large tier-A unit.
void alert_hold_keeps_freezing() {
  State state;
  Candidate existing = tier_a(1, 1, 800);
  for (uint64_t second = 1; second < 300; ++second) {
    const Actions actions = decide(state, sample(second, 70), &existing, 1);
    for (size_t i = 0; i < actions.count; ++i) {
      if (actions.items[i].kind == ActionKind::freeze) {
        existing.frozen = true;
        existing.freeze_pending = false;
      }
      if (actions.items[i].kind == ActionKind::kill) {
        existing.eligible = false;
        existing.frozen = false;
        existing.freeze_pending = false;
      }
    }
  }
  Candidate arriving = tier_a(2, 2, 2048);
  const Actions actions = decide(state, sample(300, 70), &arriving, 1);
  assert(actions.count == 1 && actions.items[0].kind == ActionKind::freeze);
  assert(actions.items[0].pid == 2);
}

// A fresh CALM state resumes persisted units smallest-first every 15 seconds.
void calm_restart_resumes_frozen_units() {
  State state;
  Candidate candidates[] = {tier_a(1, 1, 900, true), tier_a(2, 2, 500, true),
                            tier_a(3, 3, 700, true)};
  const Actions first = decide(state, sample(1, 12), candidates, 3);
  assert(first.count == 1 && first.items[0].pid == 2);
  candidates[1].frozen = false;
  const Actions early = decide(state, sample(14, 12), candidates, 3);
  assert(early.count == 0);
  const Actions second = decide(state, sample(16, 12), candidates, 3);
  assert(second.count == 1 && second.items[0].pid == 3);
  candidates[2].frozen = false;
  const Actions third = decide(state, sample(31, 12), candidates, 3);
  assert(third.count == 1 && third.items[0].pid == 1);
  State alarming;
  const Actions none = decide(alarming, sample(1, 70), candidates, 3);
  assert(none.count == 0);
}

// EMERGENCY ranks unfrozen units by footprint plus four times 30-second growth.
void emergency_score_order() {
  State state;
  Candidate candidates[] = {tier_a(1, 1, 1000), tier_a(2, 2, 500)};
  candidates[1].growth30 = 200 * kMiB;
  decide(state, sample(1, 85), candidates, 2);
  const Actions actions = decide(state, sample(2, 85), candidates, 2);
  assert(actions.count == 1 && actions.items[0].pid == 2);
}

// Ten seconds of actual post-action sample span enables projection from its oldest sample.
void post_action_trend_starts_at_ten_seconds() {
  State state;
  record_action(state, 1);
  bool early_trend = false;
  for (uint64_t second = 2; second <= 11; ++second) {
    const Sample current = sample(second, 10 + (second - 2) * 10);
    decide(state, current, nullptr, 0);
    if (second < 11)
      early_trend = early_trend || trend_reaches(state, current, 90, 240, 30);
  }
  assert(!early_trend);
  assert(trend_reaches(state, sample(12, 100), 90, 240, 30));
}

// A post-action spike uses the bounded 30-second window after a long flat period.
void post_action_trend_window_is_bounded() {
  Config config;
  config.alert_pct = 75;
  config.alert_trend_pct = 60;
  config.emergency_pct = 80;
  config.emergency_trend_pct = 65;
  config.emergency_trend_min_pct = 60;
  State fast;
  record_action(fast, 100);
  for (uint64_t second = 101; second <= 700; ++second)
    decide(fast, sample(second, 40), nullptr, 0, config);
  decide(fast, sample(715, 45), nullptr, 0, config);
  const Actions first_fast = decide(fast, sample(730, 60), nullptr, 0, config);
  assert(first_fast.level != Level::emergency);
  const Actions second_fast = decide(fast, sample(731, 61), nullptr, 0, config);
  assert(second_fast.level == Level::emergency);

  State slow;
  record_action(slow, 100);
  for (uint64_t second = 101; second <= 600; ++second) {
    const uint64_t percent = 40 + 3 * (second - 100) / 500;
    const Actions actions = decide(slow, sample(second, percent), nullptr, 0, config);
    assert(actions.count == 0);
    assert(actions.level == Level::calm);
  }
}

// ALERT recovery samples do not freeze or kill; the next alarming sample acts.
void alert_actions_wait_for_alarm() {
  State state;
  state.level = Level::alert;
  state.alert_since = 1;
  Candidate arriving = tier_a(2, 2, 2048);
  const Actions recovering = decide(state, sample(10, 30), &arriving, 1);
  assert(recovering.level == Level::alert && recovering.count == 0);
  const Actions alarming = decide(state, sample(11, 70), &arriving, 1);
  assert(alarming.level == Level::alert && alarming.count == 1);
  assert(alarming.items[0].kind == ActionKind::freeze);
  assert(alarming.items[0].pid == 2);
}

// Critical pressure needs its segment floor and two alarming samples.
void dispatched_pressure_levels() {
  State below;
  for (uint64_t second = 1; second <= 10; ++second)
    assert(decide(below, sample(second, 49, 0, 4), nullptr, 0).level == Level::calm);
  State critical;
  for (uint64_t second = 1; second <= 4; ++second) {
    const Actions actions = decide(critical, sample(second, 50, 0, 4), nullptr, 0);
    assert(actions.level == (second < 4 ? Level::calm : Level::alert));
  }

  State warning;
  for (uint64_t second = 1; second <= 100; ++second) {
    const Actions actions = decide(warning, sample(second, 10, 0, 2), nullptr, 0);
    assert(actions.level == Level::calm && actions.count == 0);
  }
}

// A partly frozen process-group unit resumes in CALM and remains kill-eligible in ALERT.
void partial_group_is_frozen_unit() {
  Candidate partial = tier_a(1, 1, 1600, true);
  partial.freeze_pending = false;
  State calm;
  const Actions resumed = decide(calm, sample(1, 10), &partial, 1);
  assert(resumed.count == 1 && resumed.items[0].kind == ActionKind::resume);

  State alert;
  alert.level = Level::alert;
  alert.alert_since = 1;
  const Actions killed = decide(alert, sample(121, 78), &partial, 1);
  assert(killed.count == 1 && killed.items[0].kind == ActionKind::kill);
  assert(killed.items[0].pid == 1);
}

// A 30-to-32 percent rise over four seconds is too short to project into ALERT.
void short_post_action_slope_ignores_noise() {
  State state;
  record_action(state, 100);
  decide(state, sample(106, 30), nullptr, 0);
  const Sample noisy = sample(110, 32);
  decide(state, noisy, nullptr, 0);
  assert(!measure_trend(state, noisy, 240, kAlertSlopeWindowSeconds).available);
  assert(!alert_now(state, noisy, Config{}));
  const Sample settled = sample(116, 32);
  decide(state, settled, nullptr, 0);
  assert(!alert_now(state, settled, Config{}));
}

// Boundary cases for the recalibrated policy and scoring.
void recalibrated_alert_policy() {
  Config config;
  State swap;
  decide(swap, sample(1, 40), nullptr, 0);
  Sample ample = sample(61, 40, 2 * kGiB);
  ample.disk_free = 20 * kGiB;
  assert(!alert_now(swap, ample, config));
  State ample_state;
  decide(ample_state, sample(1, 40), nullptr, 0);
  assert(decide(ample_state, ample, nullptr, 0).level == Level::calm);
  ample.second++;
  assert(decide(ample_state, ample, nullptr, 0).level == Level::calm);
  Sample low = ample;
  low.second = 61;
  low.disk_free = 20 * kGiB - 1;
  assert(alert_basis(swap, low, config) == AlertBasis::swap_lowdisk);
  assert(decide(swap, low, nullptr, 0).level == Level::calm);
  low.second++;
  assert(decide(swap, low, nullptr, 0).level == Level::alert);

  State trend;
  Sample base = sample(1, 430); base.segment_limit = 1000;
  decide(trend, base, nullptr, 0);
  Sample at55 = sample(31, 550); at55.segment_limit = 1000;
  assert(measure_trend(trend, at55, 120, 30).projected_pct >= 95);
  assert(alert_basis(trend, at55, config) == AlertBasis::trend);
  State trend62;
  base.segments = 518;
  decide(trend62, base, nullptr, 0);
  Sample at62 = sample(31, 620); at62.segment_limit = 1000;
  assert(alert_basis(trend62, at62, config) == AlertBasis::segments);
  assert(measure_trend(trend62, at62, 100, 30).projected_pct == 96);

  Candidate units[] = {tier_a(1, 1, 600), tier_a(2, 2, 1000), tier_a(3, 3, 800)};
  units[0].growth30 = 200 * kMiB;
  State state;
  decide(state, sample(1, 70), units, 3);
  Actions first = decide(state, sample(2, 70), units, 3);
  assert(first.count == 2 && first.items[0].pid == 1 && first.items[1].pid == 2);
  units[0].freeze_pending = false;
  units[1].freeze_pending = false;
  Actions next = decide(state, sample(3, 70), units, 3);
  assert(next.count == 1 && next.items[0].pid == 3);
  Candidate repeat = tier_a(4, 4, 900);
  repeat.repeat_offender = true; repeat.last_resume_second = 60;
  State low_state; low_state.level = Level::alert; low_state.alert_since = 1;
  decide(low_state, sample(1, 40), &repeat, 1);
  low.second = 121;
  Actions refreeze = decide(low_state, low, &repeat, 1);
  assert(refreeze.count == 1 && refreeze.items[0].kind == ActionKind::freeze);
}

// Dynamic reserve, measured danger and five-second spacing.
void revised_kill_policy() {
  Config c;
  State s;
  decide(s, sample(1, 40), nullptr, 0);
  Sample growth = sample(61, 40, 5 * kGiB);
  growth.disk_free = 25 * kGiB;
  assert(alert_basis(s, growth, c) == AlertBasis::none);
  growth.disk_free--;
  assert(alert_basis(s, growth, c) == AlertBasis::swap_lowdisk);
  State projected;
  decide(projected, sample(1, 50), nullptr, 0);
  Sample projected_sample = sample(31, 65);
  assert(!trend_reaches(projected, projected_sample, 95, 45, 30));
  assert(emergency_now(projected, projected_sample, c));
  Candidate units[] = {tier_a(1, 1, 800, true), tier_a(2, 2, 1200, true),
                       tier_a(3, 3, 2000)};
  State flat; flat.level = Level::alert; flat.alert_since = 1;
  decide(flat, sample(1, 72), nullptr, 0);
  assert(decide(flat, sample(31, 72), units, 3).kill_basis == KillBasis::none);
  State rising; rising.level = Level::alert; rising.alert_since = 1;
  decide(rising, sample(91, 71), nullptr, 0);
  Actions first = decide(rising, sample(121, 72), units, 3);
  assert(first.kill_basis == KillBasis::segments_rising && first.items[0].pid == 2);
  units[1].eligible = false;
  Actions early = decide(rising, sample(125, 72), units, 3);
  for (size_t i = 0; i < early.count; ++i) assert(early.items[i].kind != ActionKind::kill);
  Actions next = decide(rising, sample(126, 72), units, 3);
  assert(next.items[0].kind == ActionKind::kill && next.items[0].pid == 1);
  State high; high.level = Level::alert; high.alert_since = 1;
  Actions before = decide(high, sample(120, 78), units, 2);
  for (size_t i = 0; i < before.count; ++i) assert(before.items[i].kind != ActionKind::kill);
  Actions a = decide(high, sample(121, 78), units, 2);
  assert(a.count && a.items[0].kind == ActionKind::kill && a.kill_basis == KillBasis::segments);
  State disk;
  Sample baseline = sample(1, 40); baseline.disk_free = 9 * kGiB;
  decide(disk, baseline, nullptr, 0);
  Sample danger = sample(61, 40, kMiB); danger.disk_free = 9 * kGiB;
  assert(decide(disk, danger, nullptr, 0).level == Level::calm);
  danger.second = 62;
  assert(decide(disk, danger, nullptr, 0).level == Level::alert);
  danger.second = 182;
  a = decide(disk, danger, units, 2);
  // Keep a 60-second growth baseline for the later danger sample.
  assert(a.count == 0);
  danger.second = 183; danger.swap_used += kMiB;
  a = decide(disk, danger, units, 2);
  assert(a.count && a.items[0].kind == ActionKind::kill && a.kill_basis == KillBasis::swap_lowdisk);

  Candidate repeat = tier_a(4, 4, 900);
  repeat.repeat_offender = true; repeat.last_resume_second = 100;
  State no_danger;
  decide(no_danger, sample(101, 70), &repeat, 1);
  Actions refrozen = decide(no_danger, sample(102, 70), &repeat, 1);
  assert(refrozen.count == 1 && refrozen.items[0].kind == ActionKind::freeze);
  State repeat_danger;
  decide(repeat_danger, sample(101, 78), &repeat, 1);
  Actions killed = decide(repeat_danger, sample(102, 78), &repeat, 1);
  assert(killed.count == 1 && killed.items[0].kind == ActionKind::kill);
  assert(killed.kill_basis == KillBasis::segments);

  assert(kConsentVersion == 2);
  assert(consent_matches("{\"scope_version\":2,\"accepted\":true}"));
  assert(!consent_matches("{\"scope_version\":3,\"accepted\":true}"));
  assert(!consent_matches("{\"scope_version\":2,\"accepted\":false}"));

}

}  // namespace

int main() {
  revised_kill_policy();
  recalibrated_alert_policy();
  calm_noise_for_an_hour();
  one_sample_spike();
  stable_alert_for_an_hour();
  incident_effective_replay();
  incident_without_effect_replay();
  trend_only_emergency();
  trend_resets_after_freeze();
  recovering_spike();
  repeat_offender_window();
  trend_alert_never_kills();
  alternating_trend_replay();
  measured_pressure_bases();
  irregular_sampling();
  invalid_sample_preserves_alert();
  classification_table();
  calibrated_trend_floors();
  runaway_alert_and_emergency_priority();
  randomized_invariants();
  emergency_drops_to_alert();
  alert_hold_keeps_freezing();
  calm_restart_resumes_frozen_units();
  emergency_score_order();
  post_action_trend_starts_at_ten_seconds();
  post_action_trend_window_is_bounded();
  alert_actions_wait_for_alarm();
  dispatched_pressure_levels();
  partial_group_is_frozen_unit();
  short_post_action_slope_ignores_noise();
  std::puts("30 named core scenarios passed; randomized invariants: 10000 steps");
}
