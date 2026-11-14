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

// Stable 62 percent freezes A once, then kills only frozen units at 30-second spacing.
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
    const Actions actions = decide(state, sample(second, 62), candidates, 6);
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
  assert(kills == 2);
}

// The effective incident freezes each fat Python unit and resumes without killing.
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
        assert(second >= 1167);
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
  uint64_t previous_score[4] = {UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX};
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
      assert(phase >= last_phase);
      const uint64_t score = candidate_score(*candidate);
      if (phase > last_phase)
        previous_score[phase] = UINT64_MAX;
      assert(score <= previous_score[phase]);
      previous_score[phase] = score;
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
    const uint64_t percent = second < 10 ? 50 : 50 + second / 2;
    Actions actions = decide(state, sample(second, percent), &candidate, 1);
    if (actions.count && actions.items[0].kind == ActionKind::freeze) {
      candidate.frozen = true;
      candidate.freeze_pending = false;
      record_action(state, second);
    }
  }
  for (uint64_t second = 41; second <= 90; ++second) {
    const Actions actions = decide(state, sample(second, 70), &candidate, 1);
    assert(actions.level != Level::emergency);
  }
}

// A recovering spike returns to CALM and resumes a stopped unit without killing.
void recovering_spike() {
  State state;
  Candidate candidate = tier_a(1, 1, 700);
  Actions result;
  for (uint64_t second = 1; second <= 3; ++second) {
    result = decide(state, sample(second, second < 3 ? 12 : 62), &candidate, 1);
  }
  result = decide(state, sample(4, 62), &candidate, 1);
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
  decide(state, sample(101, 62), &candidate, 1);
  const Actions killed = decide(state, sample(102, 62), &candidate, 1);
  assert(killed.count == 1 && killed.items[0].kind == ActionKind::kill);
  State outside;
  candidate.last_resume_second = 100;
  decide(outside, sample(2000, 62), &candidate, 1);
  const Actions frozen = decide(outside, sample(2001, 62), &candidate, 1);
  assert(frozen.count == 1 && frozen.items[0].kind == ActionKind::freeze);
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
  decide(state, sample(1, 62), &candidate, 1);
  decide(state, sample(2, 62), &candidate, 1);
  Sample invalid = sample(3, 62);
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
        assert(candidate.frozen || candidate.repeat_offender || emergency);
        assert(alerting || emergency);
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
    const Actions actions = decide(state, sample(second, 62), &existing, 1);
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
  const Actions actions = decide(state, sample(300, 62), &arriving, 1);
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
  const Actions none = decide(alarming, sample(1, 62), candidates, 3);
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
  const Actions alarming = decide(state, sample(11, 62), &arriving, 1);
  assert(alarming.level == Level::alert && alarming.count == 1);
  assert(alarming.items[0].kind == ActionKind::freeze);
  assert(alarming.items[0].pid == 2);
}

// Five dispatched critical samples enter ALERT while warning samples never do.
void dispatched_pressure_levels() {
  State critical;
  for (uint64_t second = 1; second <= 5; ++second) {
    const Actions actions = decide(critical, sample(second, 10, 0, 4), nullptr, 0);
    if (second < 5)
      assert(actions.level == Level::calm);
    else
      assert(actions.level == Level::alert);
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
  for (uint64_t second = 2; second < 121; ++second) {
    const Actions actions = decide(alert, sample(second, 62), &partial, 1);
    assert(actions.count == 0);
  }
  const Actions killed = decide(alert, sample(121, 62), &partial, 1);
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

}  // namespace

int main() {
  calm_noise_for_an_hour();
  one_sample_spike();
  stable_alert_for_an_hour();
  incident_effective_replay();
  incident_without_effect_replay();
  trend_only_emergency();
  trend_resets_after_freeze();
  recovering_spike();
  repeat_offender_window();
  irregular_sampling();
  invalid_sample_preserves_alert();
  classification_table();
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
  std::puts("23 named core scenarios passed; randomized invariants: 10000 steps");
}
