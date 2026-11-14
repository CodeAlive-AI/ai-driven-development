#pragma once

#include <sys/types.h>

#include <array>
#include <cstddef>
#include <cstdint>
#include <cstring>

namespace memoryguard {

constexpr uint64_t kMiB = 1024ULL * 1024ULL;
constexpr uint64_t kGiB = 1024ULL * 1024ULL * 1024ULL;
constexpr size_t kHistorySize = 512;
constexpr size_t kMaxActions = 64;
constexpr size_t kMaxCandidates = 4096;
constexpr unsigned kTrendHistorySeconds = 10;
constexpr unsigned kAlertSlopeWindowSeconds = 30;
constexpr unsigned kEmergencySlopeWindowSeconds = 30;
constexpr unsigned kKillSpacingSeconds = 3;
constexpr unsigned kFrozenKillSpacingSeconds = 30;
constexpr unsigned kResumeSpacingSeconds = 15;
constexpr unsigned kRepeatWindowSeconds = 15 * 60;
constexpr unsigned kSwapGrowthWindowSeconds = 60;
constexpr unsigned kAgentAgeThresholdSeconds = 30 * 60;

enum class Level : uint8_t { calm, alert, emergency };
enum class Tier : uint8_t { a, b, c, protected_process };
enum class ActionKind : uint8_t { none, freeze, resume, kill };

struct Sample {
  uint64_t second = 0;
  uint64_t segments = 0;
  uint64_t segment_limit = 0;
  uint64_t compressed_pages = 0;
  uint64_t compressed_limit = 0;
  uint64_t swap_used = 0;
  int pressure = 0;
  bool valid = true;
};

struct Candidate {
  int pid = 0;
  int pgid = 0;
  Tier tier = Tier::protected_process;
  uint64_t footprint = 0;
  uint64_t growth30 = 0;
  bool frozen = false;
  bool freeze_pending = false;
  bool eligible = false;
  uint64_t last_resume_second = 0;
  bool repeat_offender = false;
};

struct Config {
  unsigned alert_pct = 60;
  unsigned alert_trend_pct = 90;
  unsigned alert_hold = 120;
  unsigned trend_horizon = 240;
  unsigned emergency_pct = 80;
  unsigned emergency_trend_pct = 95;
  unsigned emergency_horizon = 45;
  unsigned tier_b_pct = 88;
  unsigned tier_c_pct = 93;
  uint64_t swap_growth = 2 * kGiB;
  unsigned critical_pressure = 4;
  unsigned critical_samples = 5;
  uint64_t freeze_min = 500 * kMiB;
  uint64_t tier_min = 300 * kMiB;
  unsigned recovery_seconds = 60;
  unsigned repeat_window = kRepeatWindowSeconds;
};

struct Action {
  ActionKind kind = ActionKind::none;
  int pid = 0;
  int pgid = 0;
};

struct Actions {
  Level level = Level::calm;
  std::array<Action, kMaxActions> items{};
  size_t count = 0;
};

struct State {
  Level level = Level::calm;
  uint64_t last_second = 0;
  uint64_t alert_since = 0;
  uint64_t last_kill = 0;
  uint64_t last_frozen_kill = 0;
  uint64_t last_resume = 0;
  uint64_t calm_since = 0;
  uint64_t action_second = 0;
  unsigned alert_streak = 0;
  unsigned emergency_streak = 0;
  unsigned critical_streak = 0;
  std::array<Sample, kHistorySize> history{};
  size_t count = 0;
  size_t next = 0;
};

struct ProcessFacts {
  const char* path = "";
  const char* name = "";
  uint64_t age_seconds = 0;
  uid_t uid = 0;
  uid_t owner_uid = 0;
  bool app_main = false;
  bool helper_in_app = false;
  bool ancestor = false;
  bool protected_name = false;
  bool protected_pattern = false;
  bool agent_runtime = false;
};

inline bool at_or_above(uint64_t n, uint64_t d, unsigned percent) {
  if (percent == 0)
    return false;
  if (d == 0 || n > UINT64_MAX / 100 || d > UINT64_MAX / percent)
    return false;
  return n * 100 >= d * percent;
}

inline uint64_t pct(uint64_t numerator, uint64_t denominator) {
  return denominator == 0 ? 0 : numerator * 100 / denominator;
}

// Implements the classification table: safety exclusions precede A/B/C rules.
inline Tier classify(const ProcessFacts& facts) {
  const char* path = facts.path;
  const bool system = strncmp(path, "/System/", 8) == 0 ||
                      strncmp(path, "/usr/libexec/", 13) == 0 ||
                      strncmp(path, "/usr/sbin/", 10) == 0 || strncmp(path, "/sbin/", 6) == 0 ||
                      strncmp(path, "/Library/Apple/", 15) == 0;
  if (facts.uid != facts.owner_uid || facts.ancestor || facts.app_main || facts.protected_name ||
      facts.protected_pattern || system) {
    return Tier::protected_process;
  }
  if (facts.helper_in_app)
    return Tier::c;
  if (facts.agent_runtime)
    return Tier::b;
  if (facts.age_seconds >= kAgentAgeThresholdSeconds)
    return Tier::b;
  return Tier::a;
}

inline const Sample* find_ago(const State& state, uint64_t now, uint64_t seconds, uint64_t since) {
  const Sample* best = nullptr;
  for (size_t i = 0; i < state.count; ++i) {
    const Sample& sample = state.history[i];
    if (sample.second < since || sample.second > now || now - sample.second < seconds) {
      continue;
    }
    if (best == nullptr || sample.second > best->second)
      best = &sample;
  }
  return best;
}

struct TrendMeasurement {
  bool available = false;
  uint64_t projected_pct = 0;
  uint64_t baseline_age = 0;
  long double projected_segments = 0;
};

// Implements the newest bounded pre-action or eligible post-action trend baseline.
inline const Sample* trend_baseline(const State& state, const Sample& sample,
                                   unsigned window) {
  const Sample* old = nullptr;
  if (state.action_second != 0) {
    if (sample.second < state.action_second + kTrendHistorySeconds)
      return nullptr;
    for (size_t i = 0; i < state.count; ++i) {
      const Sample& candidate = state.history[i];
      if (candidate.second <= state.action_second || candidate.second >= sample.second ||
          sample.second - candidate.second < window)
        continue;
      if (old == nullptr || candidate.second > old->second)
        old = &candidate;
    }
    if (old == nullptr) {
      for (size_t i = 0; i < state.count; ++i) {
        const Sample& candidate = state.history[i];
        if (candidate.second <= state.action_second || candidate.second >= sample.second)
          continue;
        if (old == nullptr || candidate.second < old->second)
          old = &candidate;
      }
    }
  } else {
    old = find_ago(state, sample.second, window, 0);
  }
  if (old != nullptr && state.action_second != 0 &&
      sample.second - old->second < kTrendHistorySeconds)
    return nullptr;
  return old;
}

// Implements a trend projection and the baseline details used for decision logging.
inline TrendMeasurement measure_trend(const State& state, const Sample& sample,
                                      unsigned horizon, unsigned window) {
  TrendMeasurement result{};
  const Sample* old = trend_baseline(state, sample, window);
  if (old == nullptr || sample.second <= old->second || sample.segment_limit == 0 ||
      sample.segments < old->segments)
    return result;
  const uint64_t elapsed = sample.second - old->second;
  const uint64_t rise = sample.segments - old->segments;
  result.projected_segments = static_cast<long double>(sample.segments) +
                              static_cast<long double>(rise) * horizon / elapsed;
  const long double projected_pct =
      result.projected_segments * 100.0L / sample.segment_limit;
  result.projected_pct = projected_pct >= static_cast<long double>(UINT64_MAX)
                             ? UINT64_MAX
                             : static_cast<uint64_t>(projected_pct);
  result.baseline_age = elapsed;
  result.available = true;
  return result;
}

// Implements bounded pre-action and post-action slope windows.
inline bool trend_reaches(const State& state, const Sample& sample, unsigned threshold,
                          unsigned horizon, unsigned window) {
  const TrendMeasurement trend = measure_trend(state, sample, horizon, window);
  if (!trend.available)
    return false;
  const long double target = static_cast<long double>(sample.segment_limit) * threshold / 100.0L;
  return trend.projected_segments >= target;
}

// Implements alert_now and emergency_now from the v2 thresholds.
inline bool alert_now(const State& state, const Sample& sample, const Config& config) {
  const Sample* swap_old = find_ago(state, sample.second, kSwapGrowthWindowSeconds, 0);
  return at_or_above(sample.segments, sample.segment_limit, config.alert_pct) ||
         trend_reaches(state, sample, config.alert_trend_pct, config.trend_horizon,
                       kAlertSlopeWindowSeconds) ||
         (swap_old != nullptr && sample.swap_used >= swap_old->swap_used &&
          sample.swap_used - swap_old->swap_used >= config.swap_growth) ||
         state.critical_streak >= config.critical_samples;
}

inline bool emergency_now(const State& state, const Sample& sample, const Config& config) {
  return at_or_above(sample.segments, sample.segment_limit, config.emergency_pct) ||
         trend_reaches(state, sample, config.emergency_trend_pct, config.emergency_horizon,
                       kEmergencySlopeWindowSeconds);
}

inline bool add(Actions& actions, ActionKind kind, const Candidate& candidate) {
  if (actions.count == actions.items.size())
    return false;
  actions.items[actions.count++] = {kind, candidate.pid, candidate.pgid};
  return true;
}

inline bool eligible_floor(const Candidate& candidate, uint64_t floor) {
  return candidate.eligible && candidate.tier != Tier::protected_process &&
         candidate.footprint >= floor;
}

// Implements the bounded footprint-plus-growth candidate score.
inline uint64_t candidate_score(const Candidate& candidate) {
  const uint64_t growth = candidate.growth30 > UINT64_MAX / 4
                              ? UINT64_MAX
                              : candidate.growth30 * 4;
  return candidate.footprint > UINT64_MAX - growth ? UINT64_MAX
                                                   : candidate.footprint + growth;
}

// Implements frozen-first EMERGENCY ordering and one decision per three seconds.
inline void emergency_actions(State& state, const Sample& sample, const Candidate* candidates,
                              size_t count, const Config& config, Actions& actions) {
  if (state.last_kill != 0 && sample.second - state.last_kill < kKillSpacingSeconds)
    return;
  int selected = -1;
  for (size_t i = 0; i < count; ++i) {
    const Candidate& candidate = candidates[i];
    bool allowed = candidate.eligible && candidate.tier != Tier::protected_process &&
                   (candidate.frozen || eligible_floor(candidate, config.tier_min));
    if (!candidate.frozen && candidate.tier == Tier::b &&
        !at_or_above(sample.segments, sample.segment_limit, config.tier_b_pct))
      allowed = false;
    if (!candidate.frozen && candidate.tier == Tier::c &&
        !at_or_above(sample.segments, sample.segment_limit, config.tier_c_pct))
      allowed = false;
    if (!allowed)
      continue;
    const int rank = candidate.frozen ? 0 : static_cast<int>(candidate.tier) + 1;
    if (selected < 0) {
      selected = static_cast<int>(i);
      continue;
    }
    const Candidate& prior = candidates[static_cast<size_t>(selected)];
    const int prior_rank = prior.frozen ? 0 : static_cast<int>(prior.tier) + 1;
    const uint64_t score = candidate_score(candidate);
    const uint64_t prior_score = candidate_score(prior);
    const bool score_order = !candidate.frozen && !prior.frozen;
    if (rank < prior_rank ||
        (rank == prior_rank &&
         (score_order ? score > prior_score : candidate.footprint > prior.footprint))) {
      selected = static_cast<int>(i);
    }
  }
  if (selected >= 0 && add(actions, ActionKind::kill, candidates[static_cast<size_t>(selected)])) {
    state.last_kill = sample.second;
  }
}

// Implements alarming ALERT freezes, repeat kills and frozen-only escalation.
inline void alert_actions(State& state, const Sample& sample, const Candidate* candidates,
                          size_t count, const Config& config, bool alarming, Actions& actions) {
  if (!alarming)
    return;
  if (state.alert_since != 0 &&
      sample.second >= state.alert_since + config.alert_hold) {
    const bool kill_ready = state.last_frozen_kill == 0 ||
                            sample.second - state.last_frozen_kill >= kFrozenKillSpacingSeconds;
    if (kill_ready) {
      int selected = -1;
      for (size_t i = 0; i < count; ++i) {
        if (!candidates[i].eligible || !candidates[i].frozen)
          continue;
        if (selected < 0 ||
            candidates[i].footprint > candidates[static_cast<size_t>(selected)].footprint) {
          selected = static_cast<int>(i);
        }
      }
      if (selected >= 0 &&
          add(actions, ActionKind::kill, candidates[static_cast<size_t>(selected)])) {
        state.last_frozen_kill = sample.second;
        state.last_kill = sample.second;
      }
    }
  }
  std::array<bool, kMaxCandidates> used{};
  const size_t limit = count < used.size() ? count : used.size();
  while (actions.count < kMaxActions) {
    int selected = -1;
    uint64_t best_score = 0;
    for (size_t i = 0; i < limit; ++i) {
      const Candidate& candidate = candidates[i];
      if (!eligible_floor(candidate, config.freeze_min) || candidate.tier != Tier::a ||
          !candidate.freeze_pending)
        continue;
      if (used[i])
        continue;
      const uint64_t score = candidate_score(candidate);
      if (selected < 0 || score > best_score) {
        selected = static_cast<int>(i);
        best_score = score;
      }
    }
    if (selected < 0)
      break;
    used[static_cast<size_t>(selected)] = true;
    const Candidate& candidate = candidates[static_cast<size_t>(selected)];
    const uint64_t last_resume = candidate.last_resume_second;
    if (candidate.repeat_offender && last_resume != 0 && sample.second >= last_resume &&
        sample.second - last_resume <= config.repeat_window) {
      bool kill_selected = false;
      for (size_t i = 0; i < actions.count; ++i)
        if (actions.items[i].kind == ActionKind::kill)
          kill_selected = true;
      if (kill_selected ||
          (state.last_kill != 0 && sample.second - state.last_kill < kKillSpacingSeconds))
        continue;
      add(actions, ActionKind::kill, candidate);
      state.last_kill = sample.second;
      break;
    } else {
      add(actions, ActionKind::freeze, candidate);
    }
  }
}

// Implements hysteresis; invalid samples leave all state and counters untouched.
inline Actions decide(State& state, const Sample& sample, const Candidate* candidates, size_t count,
                      const Config& config = Config{}) {
  Actions actions{};
  actions.level = state.level;
  if (!sample.valid || sample.segment_limit == 0 || sample.segments > sample.segment_limit)
    return actions;
  const unsigned prior_critical = state.critical_streak;
  state.last_second = sample.second;
  state.history[state.next] = sample;
  state.next = (state.next + 1) % state.history.size();
  if (state.count < state.history.size())
    ++state.count;
  state.critical_streak =
      sample.pressure >= static_cast<int>(config.critical_pressure) ? prior_critical + 1 : 0;
  const bool alert = alert_now(state, sample, config);
  const bool emergency = emergency_now(state, sample, config);
  state.alert_streak = alert ? state.alert_streak + 1 : 0;
  state.emergency_streak = emergency ? state.emergency_streak + 1 : 0;
  if (state.level == Level::emergency && !emergency) {
    state.level = Level::alert;
    if (state.alert_since == 0)
      state.alert_since = sample.second;
  }
  if (state.emergency_streak >= 2) {
    state.level = Level::emergency;
  } else if (state.level == Level::calm &&
             (state.alert_streak >= 2 || state.critical_streak >= config.critical_samples)) {
    state.level = Level::alert;
    if (state.alert_since == 0)
      state.alert_since = sample.second;
  }
  if (alert || emergency) {
    state.calm_since = 0;
  } else {
    if (state.level == Level::alert) {
      if (state.calm_since == 0)
        state.calm_since = sample.second;
      if (sample.second - state.calm_since >= config.recovery_seconds) {
        state.level = Level::calm;
        state.alert_since = 0;
      }
    }
  }
  actions.level = state.level;
  if (state.level == Level::emergency) {
    emergency_actions(state, sample, candidates, count, config, actions);
  } else if (state.level == Level::alert) {
    alert_actions(state, sample, candidates, count, config, alert, actions);
  } else if (state.level == Level::calm && !alert &&
             (state.last_resume == 0 ||
              sample.second - state.last_resume >= kResumeSpacingSeconds)) {
    int selected = -1;
    for (size_t i = 0; i < count; ++i) {
      if (candidates[i].eligible && candidates[i].frozen &&
          (selected < 0 ||
           candidates[i].footprint < candidates[static_cast<size_t>(selected)].footprint)) {
        selected = static_cast<int>(i);
      }
    }
    if (selected >= 0 &&
        add(actions, ActionKind::resume, candidates[static_cast<size_t>(selected)])) {
      state.last_resume = sample.second;
    }
  }
  return actions;
}

// Implements action-relative trend history reset after this guard changes memory use.
inline void record_action(State& state, uint64_t second) {
  state.action_second = second;
}

}  // namespace memoryguard
