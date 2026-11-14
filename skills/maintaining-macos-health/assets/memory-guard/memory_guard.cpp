#include <errno.h>
#include <fcntl.h>
#include <fnmatch.h>
#include <libproc.h>
#include <limits.h>
#include <mach/mach.h>
#include <mach/mach_host.h>
#include <pthread.h>
#include <pwd.h>
#include <signal.h>
#include <spawn.h>
#include <strings.h>
#include <sys/proc.h>
#include <sys/proc_info.h>
#include <sys/resource.h>
#include <sys/stat.h>
#include <sys/sysctl.h>
#include <sys/time.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#include <cstdarg>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include "core.hpp"

using namespace memoryguard;

namespace {

constexpr size_t kMaxProcesses = 4096;
constexpr size_t kMaxFrozen = 4096;
constexpr size_t kMaxPatterns = 32;
constexpr size_t kPathSize = PROC_PIDPATHINFO_MAXSIZE;
constexpr size_t kGrowthSamples = 64;
constexpr int kConsentVersion = 2;
constexpr uint64_t kGrowthRetentionSeconds = 60;

struct Process {
  pid_t pid = 0;
  pid_t ppid = 0;
  pid_t pgid = 0;
  uid_t uid = 0;
  uint64_t start_sec = 0;
  uint64_t start_usec = 0;
  uint64_t footprint = 0;
  uint64_t growth30 = 0;
  Tier tier = Tier::protected_process;
  bool eligible = false;
  bool frozen = false;
  char path[kPathSize]{};
  char name[128]{};
};

struct FrozenProcess {
  pid_t pid = 0;
  uint64_t start_sec = 0;
  uint64_t start_usec = 0;
  pid_t pgid = 0;
  uint64_t freeze_second = 0;
};

struct FootprintSample {
  uint64_t second = 0;
  uint64_t footprint = 0;
};

struct GrowthHistory {
  pid_t pid = 0;
  uint64_t start_sec = 0;
  uint64_t start_usec = 0;
  uint64_t last_seen_second = 0;
  size_t next = 0;
  size_t count = 0;
  FootprintSample samples[kGrowthSamples]{};
};

struct RepeatRecord {
  pid_t pid = 0;
  uint64_t start_sec = 0;
  uint64_t start_usec = 0;
  uint64_t resume_second = 0;
};

struct FreezeAttempt {
  pid_t pid = 0;
  uint64_t start_sec = 0;
  uint64_t start_usec = 0;
  uint64_t alert_since = 0;
};

Process g_processes[kMaxProcesses]{};
Process g_kill_targets[kMaxProcesses]{};
Candidate g_candidates[kMaxProcesses]{};
FrozenProcess g_frozen[kMaxFrozen]{};
GrowthHistory g_growth[kMaxProcesses]{};
RepeatRecord g_repeats[kMaxFrozen]{};
FreezeAttempt g_freeze_attempts[kMaxProcesses]{};
size_t g_process_count = 0;
size_t g_candidate_count = 0;
size_t g_frozen_count = 0;
size_t g_repeat_count = 0;
size_t g_freeze_attempt_count = 0;
size_t g_kill_target_count = 0;
char g_patterns[kMaxPatterns][256]{};
size_t g_pattern_count = 0;
char g_home[PATH_MAX]{};
char g_config_path[PATH_MAX]{};
char g_consent_path[PATH_MAX]{};
char g_state_path[PATH_MAX]{};
char g_log_path[PATH_MAX]{};
char g_alerter_path[PATH_MAX] = "/opt/homebrew/bin/alerter";
int g_log_fd = -1;
int g_metrics_fd = -1;
bool g_act_mode = false;
bool g_test_mode = false;
bool g_test_root_valid = false;
volatile sig_atomic_t g_stop_requested = 0;
pid_t g_test_root = 0;
unsigned g_test_tick_ms = 1000;
uid_t g_owner_uid = 0;
pid_t g_ancestors[64]{};
size_t g_ancestor_count = 0;
uint64_t g_last_metric_log = 0;
uint64_t g_last_notice = 0;
bool g_alert_notified = false;
bool g_freeze_attempts_full = false;
State g_state{};
Config g_config{};

bool persist_frozen_state();

// Implements a local ISO 8601 timestamp with the current UTC offset.
void format_log_timestamp(char* output, size_t capacity) {
  char date[32]{};
  const time_t now = time(nullptr);
  struct tm local{};
  if (localtime_r(&now, &local) == nullptr ||
      strftime(date, sizeof(date), "%Y-%m-%dT%H:%M:%S", &local) == 0) {
    strlcpy(output, "0000-00-00T00:00:00+00:00 ", capacity);
    return;
  }
  const long offset_seconds = local.tm_gmtoff;
  const char sign = offset_seconds < 0 ? '-' : '+';
  const unsigned offset_minutes =
      static_cast<unsigned>((offset_seconds < 0 ? -offset_seconds : offset_seconds) / 60);
  snprintf(output, capacity, "%s%c%02u:%02u ", date, sign, offset_minutes / 60,
           offset_minutes % 60);
}

// Implements timestamped, process-name-only append logging.
void log_line(const char* format, ...) {
  if (g_log_fd < 0)
    return;
  char line[512];
  char timestamp[48];
  format_log_timestamp(timestamp, sizeof(timestamp));
  const size_t prefix_length = strnlen(timestamp, sizeof(timestamp));
  va_list args;
  va_start(args, format);
  const int length = vsnprintf(line + prefix_length, sizeof(line) - prefix_length - 1,
                               format, args);
  va_end(args);
  if (length <= 0)
    return;
  memcpy(line, timestamp, prefix_length);
  size_t bytes = prefix_length + static_cast<size_t>(length);
  if (bytes >= sizeof(line) - 1)
    bytes = sizeof(line) - 2;
  line[bytes++] = '\n';
  (void)write(g_log_fd, line, bytes);
}

// Implements monotonic seconds from CLOCK_UPTIME_RAW.
uint64_t uptime_second() {
  timespec value{};
  if (clock_gettime(CLOCK_UPTIME_RAW, &value) != 0)
    return 0;
  return static_cast<uint64_t>(value.tv_sec);
}

// Implements safe sysctl reads that accept kernel 32-bit or 64-bit values.
bool read_sysctl_u64(const char* name, uint64_t& value) {
  size_t size = sizeof(value);
  if (sysctlbyname(name, &value, &size, nullptr, 0) == 0 && size == sizeof(value))
    return true;
  uint32_t small = 0;
  size = sizeof(small);
  if (sysctlbyname(name, &small, &size, nullptr, 0) != 0 || size != sizeof(small))
    return false;
  value = small;
  return true;
}

// Implements live compressor, swap and pressure sampling.
bool read_live_sample(Sample& sample) {
  uint64_t segments = 0;
  uint64_t limit = 0;
  uint64_t pages = 0;
  uint64_t page_limit = 0;
  if (!read_sysctl_u64("vm.compressor.segment.total", segments) ||
      !read_sysctl_u64("vm.compressor.segment.limit", limit))
    return false;
  const bool has_pages = read_sysctl_u64("vm.compressor.pages_compressed", pages) &&
                         read_sysctl_u64("vm.compressor.pages_compressed_limit", page_limit);
  struct xsw_usage swap{};
  size_t size = sizeof(swap);
  if (sysctlbyname("vm.swapusage", &swap, &size, nullptr, 0) != 0 || size != sizeof(swap))
    return false;
  int pressure = -1;
  size = sizeof(pressure);
  if (sysctlbyname("kern.memorystatus_vm_pressure_level", &pressure, &size, nullptr, 0) != 0 ||
      size != sizeof(pressure))
    pressure = -1;
  sample = {};
  sample.second = uptime_second();
  sample.segments = segments;
  sample.segment_limit = limit;
  sample.compressed_pages = pages;
  sample.compressed_limit = has_pages ? page_limit : 0;
  sample.swap_used = swap.xsu_used;
  sample.pressure = pressure;
  sample.valid = limit > 0 && segments <= limit && (!has_pages || pages <= page_limit);
  return sample.valid;
}

// Implements one-line scripted test metrics, one line per requested tick.
bool read_test_sample(Sample& sample) {
  char line[256];
  if (g_metrics_fd < 0)
    return false;
  size_t used = 0;
  while (used + 1 < sizeof(line)) {
    const ssize_t got = read(g_metrics_fd, line + used, 1);
    if (got == 0)
      return false;
    if (got < 0)
      return false;
    if (line[used++] == '\n')
      break;
  }
  line[used] = 0;
  unsigned long long second = 0;
  unsigned long long segments = 0;
  unsigned long long limit = 0;
  unsigned long long swap = 0;
  int pressure = 0;
  if (sscanf(line, "%llu %llu %llu %llu %d", &second, &segments, &limit, &swap, &pressure) != 5)
    return false;
  sample = {};
  sample.second = second;
  sample.segments = segments;
  sample.segment_limit = limit;
  sample.swap_used = swap;
  sample.pressure = pressure;
  sample.valid = limit > 0 && segments <= limit;
  return true;
}

// Implements process-name protections and the brief's never-touch roots.
bool protected_facts(const Process& process) {
  static const char* exact_names[] = {"launchd",       "loginwindow",
                                      "WindowServer",  "Finder",
                                      "Dock",          "SystemUIServer",
                                      "ControlCenter", "NotificationCenter",
                                      "Terminal",      "iTerm2",
                                      "Warp",          "Ghostty",
                                      "Hyper",         "Tabby",
                                      "kitty",         "WezTerm",
                                      "Alacritty",     "Rio",
                                      "cmux",          "tmux",
                                      "screen",        "sshd",
                                      "ssh-agent"};
  for (const char* name : exact_names)
    if (strcasecmp(process.name, name) == 0)
      return true;
  static const char* protected_tokens[] = {
      "1password",   "agilebits", "bitwarden", "keepass", "lastpass", "dashlane",  "authy",
      "yubico",      "tailscale", "wireguard", "mullvad", "nordvpn",  "protonvpn", "clash",
      "shadowsocks", "v2ray",     "outline",   "amnezia", "blancvpn"};
  for (const char* token : protected_tokens)
    if (strcasestr(process.name, token) != nullptr ||
        strcasestr(process.path, token) != nullptr)
      return true;
  if (strncmp(process.path, "/System/", 8) == 0 ||
      strncmp(process.path, "/usr/libexec/", 13) == 0 ||
      strncmp(process.path, "/usr/sbin/", 10) == 0 || strncmp(process.path, "/sbin/", 6) == 0 ||
      strncmp(process.path, "/Library/Apple/", 15) == 0)
    return true;
  for (size_t i = 0; i < g_pattern_count; ++i)
    if (fnmatch(g_patterns[i], process.path, 0) == 0)
      return true;
  for (size_t i = 0; i < g_ancestor_count; ++i)
    if (g_ancestors[i] == process.pid)
      return true;
  return false;
}

// Implements named-agent recognition for core classification.
bool agent_runtime(const char* name) {
  static const char* names[] = {"claude", "codex", "devin",       "opencode",
                                "gemini", "grok",  "cursor-agent"};
  for (const char* candidate : names)
    if (strcasestr(name, candidate) != nullptr)
      return true;
  return false;
}

// Implements process identity reads through libproc.
bool read_process(pid_t pid, Process& process) {
  struct proc_bsdinfo info{};
  if (pid <= 0 || proc_pidinfo(pid, PROC_PIDTBSDINFO, 0, &info, sizeof(info)) != sizeof(info))
    return false;
  process = {};
  process.pid = pid;
  process.ppid = static_cast<pid_t>(info.pbi_ppid);
  process.pgid = static_cast<pid_t>(info.pbi_pgid);
  process.uid = static_cast<uid_t>(info.pbi_uid);
  process.start_sec = info.pbi_start_tvsec;
  process.start_usec = info.pbi_start_tvusec;
  if (proc_pidpath(pid, process.path, sizeof(process.path)) <= 0)
    return false;
  const char* base = strrchr(process.path, '/');
  base = base == nullptr ? process.path : base + 1;
  strlcpy(process.name, base, sizeof(process.name));
  struct rusage_info_v4 usage{};
  if (proc_pid_rusage(pid, RUSAGE_INFO_V4, reinterpret_cast<rusage_info_t*>(&usage)) == 0)
    process.footprint = usage.ri_phys_footprint;
  return true;
}

// Implements matching the guard's per-process frozen identity records.
int frozen_index(pid_t pid, uint64_t start_sec, uint64_t start_usec) {
  for (size_t i = 0; i < g_frozen_count; ++i)
    if (g_frozen[i].pid == pid && g_frozen[i].start_sec == start_sec &&
        g_frozen[i].start_usec == start_usec)
      return static_cast<int>(i);
  return -1;
}

// Implements stopped-state verification for persisted freezes and the harness.
bool process_stopped(pid_t pid) {
  struct proc_bsdinfo info{};
  if (proc_pidinfo(pid, PROC_PIDTBSDINFO, 0, &info, sizeof(info)) != sizeof(info))
    return false;
  return info.pbi_status == SSTOP;
}

// Implements protection of the guard's own children, such as its notifier. Live incident
// 2026-11-14: unanswered alerter windows piled up in the guard's process group, together
// crossed the freeze floor, and the guard froze its own notifications.
bool descends_from_guard(pid_t pid) {
  const pid_t self = getpid();
  pid_t cursor = pid;
  for (size_t depth = 0; depth < 64 && cursor > 1; ++depth) {
    struct proc_bsdinfo info{};
    if (proc_pidinfo(cursor, PROC_PIDTBSDINFO, 0, &info, sizeof(info)) != sizeof(info))
      return false;
    cursor = static_cast<pid_t>(info.pbi_ppid);
    if (cursor == self)
      return true;
  }
  return false;
}

// Implements the test-root descendant restriction.
bool descends_from_test_root(pid_t pid) {
  if (!g_test_mode)
    return true;
  pid_t cursor = pid;
  for (size_t depth = 0; depth < 64 && cursor > 1; ++depth) {
    if (cursor == g_test_root)
      return true;
    struct proc_bsdinfo info{};
    if (proc_pidinfo(cursor, PROC_PIDTBSDINFO, 0, &info, sizeof(info)) != sizeof(info))
      return false;
    cursor = static_cast<pid_t>(info.pbi_ppid);
  }
  return false;
}

// Implements process age, bundle-main detection and pure core classification.
Tier classify_process(const Process& process, bool& eligible) {
  const bool in_bundle = strstr(process.path, ".app/") != nullptr;
  const bool app_main = in_bundle && strstr(process.path, ".app/Contents/MacOS/") != nullptr;
  ProcessFacts facts{};
  facts.path = process.path;
  facts.name = process.name;
  facts.uid = process.uid;
  facts.owner_uid = g_owner_uid;
  facts.app_main = app_main;
  facts.helper_in_app = in_bundle && !app_main;
  facts.protected_name = protected_facts(process);
  facts.ancestor = false;
  for (size_t i = 0; i < g_ancestor_count; ++i)
    if (g_ancestors[i] == process.pid)
      facts.ancestor = true;
  if (descends_from_guard(process.pid))
    facts.ancestor = true;
  facts.agent_runtime = agent_runtime(process.name);
  struct timeval now{};
  gettimeofday(&now, nullptr);
  const uint64_t started = process.start_sec;
  facts.age_seconds = now.tv_sec > static_cast<time_t>(started)
                          ? static_cast<uint64_t>(now.tv_sec - static_cast<time_t>(started))
                          : 0;
  const Tier tier = classify(facts);
  eligible = tier != Tier::protected_process && descends_from_test_root(process.pid);
  return eligible ? tier : Tier::protected_process;
}

// Implements per-pid footprint growth measured over the real 30-second interval.
uint64_t update_growth(Process& process, uint64_t second) {
  GrowthHistory* history = nullptr;
  for (GrowthHistory& item : g_growth) {
    if (item.pid == process.pid && item.start_sec == process.start_sec &&
        item.start_usec == process.start_usec) {
      history = &item;
      break;
    }
  }
  if (history == nullptr) {
    for (GrowthHistory& item : g_growth)
      if (item.pid == 0) {
        history = &item;
        break;
      }
  }
  if (history == nullptr) {
    for (GrowthHistory& item : g_growth)
      if (item.pid == process.pid) {
        history = &item;
        break;
      }
  }
  if (history == nullptr) {
    for (GrowthHistory& item : g_growth)
      if (item.last_seen_second != 0 && second >= item.last_seen_second &&
          second - item.last_seen_second >= kGrowthRetentionSeconds &&
          (history == nullptr || item.last_seen_second < history->last_seen_second))
        history = &item;
  }
  if (history == nullptr)
    return 0;
  if (history->pid != process.pid || history->start_sec != process.start_sec ||
      history->start_usec != process.start_usec) {
    *history = {};
    history->pid = process.pid;
    history->start_sec = process.start_sec;
    history->start_usec = process.start_usec;
  }
  history->samples[history->next] = {second, process.footprint};
  history->last_seen_second = second;
  history->next = (history->next + 1) % kGrowthSamples;
  if (history->count < kGrowthSamples)
    ++history->count;
  const FootprintSample* baseline = nullptr;
  for (size_t i = 0; i < history->count; ++i) {
    const FootprintSample& sample = history->samples[i];
    if (sample.second <= second && second - sample.second >= 30 &&
        (baseline == nullptr || sample.second > baseline->second))
      baseline = &sample;
  }
  if (baseline == nullptr || process.footprint <= baseline->footprint)
    return 0;
  const uint64_t elapsed = second - baseline->second;
  const uint64_t increase = process.footprint - baseline->footprint;
  return static_cast<uint64_t>(static_cast<long double>(increase) * 30 / elapsed);
}

// Implements the 15-minute resumed-identity test for one process.
bool repeat_resume_second(const Process& process, uint64_t second, uint64_t& resume_second) {
  for (size_t i = 0; i < g_repeat_count; ++i) {
    const RepeatRecord& repeat = g_repeats[i];
    if (repeat.pid == process.pid && repeat.start_sec == process.start_sec &&
        repeat.start_usec == process.start_usec && repeat.resume_second != 0 &&
        second >= repeat.resume_second && second - repeat.resume_second <= g_config.repeat_window) {
      resume_second = repeat.resume_second;
      return true;
    }
  }
  return false;
}

// Implements bounded repeat-history retention.
void prune_repeat_history(uint64_t second) {
  for (size_t i = 0; i < g_repeat_count;) {
    const uint64_t resumed = g_repeats[i].resume_second;
    if (second >= resumed && second - resumed > g_config.repeat_window) {
      g_repeats[i] = g_repeats[--g_repeat_count];
      continue;
    }
    ++i;
  }
}

// Implements one stop attempt per process identity in an ALERT episode.
uint64_t freeze_episode(uint64_t second) {
  return g_state.alert_since == 0 ? second : g_state.alert_since;
}

// Prevents repeated SIGSTOP decisions for members continued during the same episode.
bool freeze_attempted(const Process& process, uint64_t episode) {
  if (g_freeze_attempts_full)
    return true;
  for (size_t i = 0; i < g_freeze_attempt_count; ++i) {
    const FreezeAttempt& attempt = g_freeze_attempts[i];
    if (attempt.pid == process.pid && attempt.start_sec == process.start_sec &&
        attempt.start_usec == process.start_usec && attempt.alert_since == episode)
      return true;
  }
  return false;
}

// Records a successful SIGSTOP for the current alert episode.
void remember_freeze_attempt(const Process& process, uint64_t episode) {
  if (freeze_attempted(process, episode))
    return;
  if (g_freeze_attempt_count == kMaxProcesses) {
    g_freeze_attempts_full = true;
    return;
  }
  g_freeze_attempts[g_freeze_attempt_count++] = {process.pid, process.start_sec,
                                                  process.start_usec, episode};
}

// Implements fresh process enumeration and candidate construction by core tiers.
bool enumerate_processes(uint64_t second) {
  if (g_state.level == Level::calm) {
    g_freeze_attempt_count = 0;
    g_freeze_attempts_full = false;
  }
  prune_repeat_history(second);
  int bytes = proc_listpids(PROC_ALL_PIDS, 0, nullptr, 0);
  if (bytes <= 0 || static_cast<size_t>(bytes) > sizeof(pid_t) * kMaxProcesses)
    return false;
  static pid_t pids[kMaxProcesses];
  const int read_bytes = proc_listpids(PROC_ALL_PIDS, 0, pids, sizeof(pids));
  if (read_bytes <= 0)
    return false;
  g_process_count = 0;
  size_t count = static_cast<size_t>(read_bytes) / sizeof(pid_t);
  if (count > kMaxProcesses)
    count = kMaxProcesses;
  for (size_t i = 0; i < count; ++i) {
    if (g_test_mode && !descends_from_test_root(pids[i]))
      continue;
    Process process{};
    if (!read_process(pids[i], process) || process.uid != g_owner_uid)
      continue;
    if (g_process_count == kMaxProcesses)
      return false;
    process.tier = classify_process(process, process.eligible);
    process.growth30 = update_growth(process, second);
    process.frozen = frozen_index(process.pid, process.start_sec, process.start_usec) >= 0;
    g_processes[g_process_count++] = process;
  }
  const size_t frozen_before_validation = g_frozen_count;
  for (size_t i = 0; i < g_frozen_count;) {
    Process current{};
    const FrozenProcess& entry = g_frozen[i];
    bool eligible = false;
    const Tier tier = read_process(entry.pid, current) ? classify_process(current, eligible)
                                                       : Tier::protected_process;
    const bool matches = tier != Tier::protected_process && eligible &&
                         current.uid == g_owner_uid &&
                         current.start_sec == entry.start_sec &&
                         current.start_usec == entry.start_usec;
    if (!matches || !process_stopped(entry.pid)) {
      g_frozen[i] = g_frozen[--g_frozen_count];
      continue;
    }
    ++i;
  }
  if (g_frozen_count != frozen_before_validation)
    (void)persist_frozen_state();
  for (size_t i = 0; i < g_process_count; ++i)
    g_processes[i].frozen =
        frozen_index(g_processes[i].pid, g_processes[i].start_sec, g_processes[i].start_usec) >= 0;
  g_candidate_count = 0;
  const uint64_t episode = freeze_episode(second);
  for (size_t i = 0; i < g_process_count; ++i) {
    Process& process = g_processes[i];
    if (!process.eligible || process.footprint == 0)
      continue;
    int selected = -1;
    if (process.tier == Tier::a)
      for (size_t j = 0; j < g_candidate_count; ++j)
        if (g_candidates[j].tier == Tier::a && g_candidates[j].pgid == process.pgid) {
          selected = static_cast<int>(j);
          break;
        }
    if (selected < 0) {
      if (g_candidate_count == kMaxProcesses)
        return false;
      selected = static_cast<int>(g_candidate_count++);
      Candidate candidate{};
      candidate.pid = process.tier == Tier::a ? 0 : process.pid;
      candidate.pgid = process.pgid;
      candidate.tier = process.tier;
      candidate.footprint = process.footprint;
      candidate.growth30 = process.growth30;
      candidate.frozen = process.frozen;
      candidate.freeze_pending = process.tier == Tier::a && !process.frozen &&
                                 !process_stopped(process.pid) &&
                                 !freeze_attempted(process, episode);
      candidate.eligible = true;
      candidate.repeat_offender =
          repeat_resume_second(process, second, candidate.last_resume_second);
      g_candidates[static_cast<size_t>(selected)] = candidate;
    } else {
      Candidate& candidate = g_candidates[static_cast<size_t>(selected)];
      candidate.footprint += process.footprint;
      candidate.growth30 += process.growth30;
      candidate.frozen = candidate.frozen || process.frozen;
      candidate.freeze_pending =
          candidate.freeze_pending ||
          (!process.frozen && !process_stopped(process.pid) &&
           !freeze_attempted(process, episode));
      uint64_t resume_second = 0;
      const bool member_repeat = repeat_resume_second(process, second, resume_second);
      if (!member_repeat) {
        candidate.repeat_offender = false;
      } else if (candidate.repeat_offender &&
                 resume_second < candidate.last_resume_second) {
        candidate.last_resume_second = resume_second;
      }
    }
  }
  return true;
}

// Implements ancestor capture and explicit test-root authorization.
void capture_ancestors() {
  pid_t pid = getpid();
  while (pid > 1 && g_ancestor_count < 64) {
    g_ancestors[g_ancestor_count++] = pid;
    struct proc_bsdinfo info{};
    if (proc_pidinfo(pid, PROC_PIDTBSDINFO, 0, &info, sizeof(info)) != sizeof(info))
      break;
    pid = static_cast<pid_t>(info.pbi_ppid);
  }
  if (g_test_mode)
    for (size_t i = 0; i < g_ancestor_count; ++i)
      if (g_ancestors[i] == g_test_root)
        g_test_root_valid = true;
}

// Implements whitespace trimming for readable KEY=VALUE configuration.
char* trim(char* value) {
  while (std::isspace(static_cast<unsigned char>(*value)))
    ++value;
  char* end = value + strlen(value);
  while (end > value && std::isspace(static_cast<unsigned char>(end[-1])))
    *--end = 0;
  return value;
}

// Implements bounded config string copies instead of silently truncating paths.
bool copy_config_string(char* output, size_t capacity, const char* value, const char* key) {
  if (strlen(value) >= capacity) {
    fprintf(stderr, "config value for %s is too long\n", key);
    return false;
  }
  strlcpy(output, value, capacity);
  return true;
}

// Implements strict unsigned configuration parsing without numeric fallback.
bool parse_number(const char* key, const char* value, unsigned long long& number) {
  if (*value == 0 || *value == '-') {
    fprintf(stderr, "invalid numeric config value for %s\n", key);
    return false;
  }
  char* tail = nullptr;
  errno = 0;
  number = strtoull(value, &tail, 10);
  if (errno == ERANGE || tail == value || *tail != 0) {
    fprintf(stderr, "invalid numeric config value for %s\n", key);
    return false;
  }
  return true;
}

// Implements mapping the supported numeric keys onto core configuration fields.
bool set_config_number(const char* key, unsigned long long number) {
  if (strcmp(key, "FREEZE_MIN_MB") == 0) {
    if (number > ULLONG_MAX / kMiB)
      return false;
    g_config.freeze_min = number * kMiB;
  } else if (strcmp(key, "TIER_MIN_MB") == 0) {
    if (number > ULLONG_MAX / kMiB)
      return false;
    g_config.tier_min = number * kMiB;
  } else if (strcmp(key, "SWAP_GROWTH_GIB") == 0) {
    if (number == 0 || number > ULLONG_MAX / kGiB)
      return false;
    g_config.swap_growth = number * kGiB;
  } else {
    if (number > UINT_MAX)
      return false;
    const unsigned value = static_cast<unsigned>(number);
    if (strcmp(key, "ALERT_PCT") == 0)
      g_config.alert_pct = value;
    else if (strcmp(key, "ALERT_TREND_PCT") == 0)
      g_config.alert_trend_pct = value;
    else if (strcmp(key, "TREND_WINDOW") == 0)
      g_config.trend_horizon = value;
    else if (strcmp(key, "EMERGENCY_PCT") == 0)
      g_config.emergency_pct = value;
    else if (strcmp(key, "EMERGENCY_TREND_PCT") == 0)
      g_config.emergency_trend_pct = value;
    else if (strcmp(key, "EMERGENCY_WINDOW") == 0)
      g_config.emergency_horizon = value;
    else if (strcmp(key, "CRITICAL_PRESSURE") == 0)
      g_config.critical_pressure = value;
    else if (strcmp(key, "CRITICAL_SAMPLES") == 0)
      g_config.critical_samples = value;
    else if (strcmp(key, "ALERT_HOLD_SECONDS") == 0)
      g_config.alert_hold = value;
    else if (strcmp(key, "RECOVERY_SECONDS") == 0)
      g_config.recovery_seconds = value;
    else if (strcmp(key, "FREEZE_TWICE_WINDOW_SECONDS") == 0)
      g_config.repeat_window = value;
    else if (strcmp(key, "TIER_B_PCT") == 0)
      g_config.tier_b_pct = value;
    else if (strcmp(key, "TIER_C_PCT") == 0)
      g_config.tier_c_pct = value;
    else
      return false;
  }
  return true;
}

// Implements string-valued mode, path and protection configuration.
bool set_config_string(const char* key, const char* value, bool& handled) {
  handled = true;
  if (strcmp(key, "MODE") == 0) {
    if (strcmp(value, "act") == 0)
      g_act_mode = true;
    else if (strcmp(value, "observe") == 0)
      g_act_mode = false;
    else {
      fprintf(stderr, "invalid MODE: expected observe or act\n");
      return false;
    }
  } else if (strcmp(key, "PROTECT") == 0) {
    if (*value == 0 || g_pattern_count == kMaxPatterns) {
      fprintf(stderr, "invalid or excessive PROTECT pattern\n");
      return false;
    }
    if (!copy_config_string(g_patterns[g_pattern_count], sizeof(g_patterns[0]), value, key))
      return false;
    ++g_pattern_count;
  } else if (strcmp(key, "ALERTER") == 0) {
    return copy_config_string(g_alerter_path, sizeof(g_alerter_path), value, key);
  } else if (strcmp(key, "LOG_PATH") == 0 || strcmp(key, "STATE_PATH") == 0) {
    if (*value == 0) {
      fprintf(stderr, "config path for %s cannot be empty\n", key);
      return false;
    }
    char* output = strcmp(key, "LOG_PATH") == 0 ? g_log_path : g_state_path;
    const size_t capacity = strcmp(key, "LOG_PATH") == 0 ? sizeof(g_log_path)
                                                         : sizeof(g_state_path);
    return copy_config_string(output, capacity, value, key);
  } else {
    handled = false;
  }
  return true;
}

// Implements one strict KEY=VALUE parse without defaulting invalid entries.
bool parse_config_line(char* line) {
  char* entry = trim(line);
  if (*entry == 0 || *entry == '#')
    return true;
  char* equals = strchr(entry, '=');
  if (equals == nullptr) {
    fprintf(stderr, "invalid config line; expected KEY=VALUE\n");
    return false;
  }
  *equals++ = 0;
  char* key = trim(entry);
  char* value = trim(equals);
  bool handled = false;
  if (!set_config_string(key, value, handled))
    return false;
  if (handled)
    return true;
  unsigned long long number = 0;
  if (!parse_number(key, value, number))
    return false;
  if (set_config_number(key, number))
    return true;
  fprintf(stderr, "unknown or out-of-range config value for %s\n", key);
  return false;
}

// Implements percentage, threshold-order and positive-floor validation.
bool config_is_valid() {
  const bool valid = g_config.freeze_min > 0 && g_config.tier_min > 0 &&
                     g_config.alert_pct >= 1 && g_config.alert_pct <= 100 &&
                     g_config.alert_trend_pct >= 1 && g_config.alert_trend_pct <= 100 &&
                     g_config.emergency_pct > g_config.alert_pct &&
                     g_config.emergency_pct <= 100 &&
                     g_config.emergency_trend_pct > g_config.alert_trend_pct &&
                     g_config.emergency_trend_pct <= 100 && g_config.tier_b_pct >= 1 &&
                     g_config.tier_b_pct <= 100 && g_config.tier_c_pct >= 1 &&
                     g_config.tier_c_pct <= 100 && g_config.critical_pressure >= 1 &&
                     g_config.critical_pressure <= 4 &&
                     g_config.critical_samples > 0 && g_config.alert_hold > 0 &&
                     g_config.trend_horizon > 0 && g_config.emergency_horizon > 0 &&
                     g_config.recovery_seconds > 0 && g_config.repeat_window > 0;
  if (!valid)
    fprintf(stderr,
            "invalid config: percentages must be 1..100, emergency above alert, floors > 0\n");
  return valid;
}

// Implements strict config-file loading and supported safety thresholds.
bool read_config(const char* path, bool optional) {
  FILE* file = path == nullptr ? nullptr : fopen(path, "r");
  if (file == nullptr) {
    if (optional && errno == ENOENT)
      return true;
    fprintf(stderr, "cannot open config: %s\n", path == nullptr ? "(none)" : path);
    return false;
  }
  char line[1024];
  while (fgets(line, sizeof(line), file) != nullptr) {
    if (strchr(line, '\n') == nullptr && fgetc(file) != EOF) {
      fprintf(stderr, "config line exceeds 1023 bytes\n");
      fclose(file);
      return false;
    }
    if (!parse_config_line(line)) {
      fclose(file);
      return false;
    }
  }
  fclose(file);
  return config_is_valid();
}

// Implements versioned act-mode consent validation without accepting v1 scope.
bool consent_is_current() {
  FILE* file = fopen(g_consent_path, "r");
  if (file == nullptr)
    return false;
  char data[512];
  const size_t size = fread(data, 1, sizeof(data) - 1, file);
  fclose(file);
  data[size] = 0;
  char expected[64];
  snprintf(expected, sizeof(expected), "\"scope_version\":%d", kConsentVersion);
  return strstr(data, expected) != nullptr && strstr(data, "\"accepted\":true") != nullptr;
}

// Implements secure per-process state loading and stale-identity rejection.
void load_frozen_state(bool persist_stale = true) {
  FILE* file = fopen(g_state_path, "r");
  if (file == nullptr)
    return;
  pid_t pid = 0;
  unsigned long long start_sec = 0;
  unsigned long long start_usec = 0;
  pid_t pgid = 0;
  unsigned long long freeze_second = 0;
  size_t accepted = 0;
  size_t parsed = 0;
  while (g_frozen_count < kMaxFrozen &&
         fscanf(file, "%d %llu %llu %d %llu", &pid, &start_sec, &start_usec, &pgid,
                &freeze_second) == 5) {
    ++parsed;
    Process process{};
    bool eligible = false;
    const Tier tier = read_process(pid, process) ? classify_process(process, eligible)
                                                : Tier::protected_process;
    if (tier == Tier::protected_process || !eligible || process.uid != g_owner_uid ||
        process.start_sec != static_cast<uint64_t>(start_sec) ||
        process.start_usec != static_cast<uint64_t>(start_usec) ||
        process.pgid != pgid || !process_stopped(pid))
      continue;
    g_frozen[g_frozen_count++] = {pid, static_cast<uint64_t>(start_sec),
                                  static_cast<uint64_t>(start_usec), pgid,
                                  static_cast<uint64_t>(freeze_second)};
    ++accepted;
  }
  fclose(file);
  if (persist_stale && accepted != parsed)
    (void)persist_frozen_state();
}

// Implements atomic state replacement after signals have been sent.
bool persist_frozen_state() {
  char temporary[PATH_MAX];
  snprintf(temporary, sizeof(temporary), "%s.tmp.%d", g_state_path, getpid());
  const int fd = open(temporary, O_WRONLY | O_CREAT | O_TRUNC, 0600);
  if (fd < 0)
    return false;
  char data[kMaxFrozen * 96];
  size_t used = 0;
  for (size_t i = 0; i < g_frozen_count; ++i) {
    const FrozenProcess& entry = g_frozen[i];
    const int length = snprintf(data + used, sizeof(data) - used, "%d %llu %llu %d %llu\n",
                                entry.pid, static_cast<unsigned long long>(entry.start_sec),
                                static_cast<unsigned long long>(entry.start_usec), entry.pgid,
                                static_cast<unsigned long long>(entry.freeze_second));
    if (length < 0 || static_cast<size_t>(length) >= sizeof(data) - used) {
      close(fd);
      unlink(temporary);
      return false;
    }
    used += static_cast<size_t>(length);
  }
  const bool written = write(fd, data, used) == static_cast<ssize_t>(used) && fsync(fd) == 0;
  close(fd);
  if (!written || rename(temporary, g_state_path) != 0) {
    unlink(temporary);
    return false;
  }
  return true;
}

// Implements immediate identity, ownership and protection checks before each signal.
bool checked_signal(pid_t pid, uint64_t start_sec, uint64_t start_usec, pid_t pgid, int signal) {
  Process facts{};
  bool eligible = false;
  const Tier tier = read_process(pid, facts) ? classify_process(facts, eligible)
                                               : Tier::protected_process;
  Process current{};
  bool current_eligible = false;
  const Tier current_tier = read_process(pid, current) ? classify_process(current, current_eligible)
                                                       : Tier::protected_process;
  if (tier == Tier::protected_process || !eligible || current_tier == Tier::protected_process ||
      !current_eligible || current.uid != g_owner_uid || current.start_sec != start_sec ||
      current.start_usec != start_usec || current.pgid != pgid) {
    log_line("skip signal=%d pid=%d identity/protection check failed", signal, pid);
    return false;
  }
  if (kill(pid, signal) != 0) {
    log_line("signal=%d pid=%d failed errno=%d", signal, pid, errno);
    return false;
  }
  return true;
}

// Implements names for signal and decision records without arguments or paths.
const char* process_name(pid_t pid, uint64_t start_sec, uint64_t start_usec) {
  for (size_t i = 0; i < g_process_count; ++i)
    if (g_processes[i].pid == pid && g_processes[i].start_sec == start_sec &&
        g_processes[i].start_usec == start_usec)
      return g_processes[i].name;
  return "process";
}

// Implements current footprint lookup for signal records.
uint64_t process_footprint(pid_t pid, uint64_t start_sec, uint64_t start_usec) {
  for (size_t i = 0; i < g_process_count; ++i)
    if (g_processes[i].pid == pid && g_processes[i].start_sec == start_sec &&
        g_processes[i].start_usec == start_usec)
      return g_processes[i].footprint;
  return 0;
}

// Names a process-group unit after its largest eligible member.
const char* candidate_name(const Candidate& candidate) {
  const Process* largest = nullptr;
  for (size_t i = 0; i < g_process_count; ++i) {
    const Process& process = g_processes[i];
    const bool member = candidate.pid == 0
                            ? process.pgid == candidate.pgid && process.tier == Tier::a
                            : process.pid == candidate.pid;
    if (!member || !process.eligible)
      continue;
    if (largest == nullptr || process.footprint > largest->footprint)
      largest = &process;
  }
  return largest == nullptr ? "process" : largest->name;
}

// Implements state insertion after a successful guard-issued SIGSTOP.
void remember_frozen(const Process& process, uint64_t second) {
  if (frozen_index(process.pid, process.start_sec, process.start_usec) >= 0 ||
      g_frozen_count == kMaxFrozen)
    return;
  g_frozen[g_frozen_count++] = {process.pid, process.start_sec, process.start_usec, process.pgid,
                                second};
}

// Implements resumed-offender history for the 15-minute repeat rule.
void remember_resumed(const FrozenProcess& frozen, uint64_t second) {
  RepeatRecord* record = nullptr;
  for (size_t i = 0; i < g_repeat_count; ++i)
    if (g_repeats[i].pid == frozen.pid && g_repeats[i].start_sec == frozen.start_sec &&
        g_repeats[i].start_usec == frozen.start_usec)
      record = &g_repeats[i];
  if (record == nullptr && g_repeat_count < kMaxFrozen)
    record = &g_repeats[g_repeat_count++];
  if (record != nullptr) {
    record->pid = frozen.pid;
    record->start_sec = frozen.start_sec;
    record->start_usec = frozen.start_usec;
    record->resume_second = second;
  }
}

// Implements readable process/tier/footprint action lines and notification throttling.
void notify(const char* text) {
  const uint64_t now = uptime_second();
  if (now < g_last_notice || now - g_last_notice < 30)
    return;
  if (access(g_alerter_path, X_OK) != 0) {
    log_line("notification unavailable: alerter not executable");
    g_last_notice = now;
    return;
  }
  char* const arguments[] = {g_alerter_path,
                             const_cast<char*>("--title"),
                             const_cast<char*>("Memory guard"),
                             const_cast<char*>("--message"),
                             const_cast<char*>(text),
                             const_cast<char*>("--timeout"),
                             const_cast<char*>("1800"),
                             nullptr};
  char* const environment[] = {nullptr};
  // At most one notifier window: the newest message replaces an unanswered older one, so
  // a long episode cannot pile up notifier processes. Only our own child is signalled.
  static pid_t previous = 0;
  if (previous > 0) {
    struct proc_bsdinfo info{};
    if (proc_pidinfo(previous, PROC_PIDTBSDINFO, 0, &info, sizeof(info)) == sizeof(info) &&
        static_cast<pid_t>(info.pbi_ppid) == getpid())
      (void)kill(previous, SIGTERM);
    previous = 0;
  }
  pid_t child = 0;
  const int result = posix_spawn(&child, g_alerter_path, nullptr, nullptr, arguments, environment);
  if (result != 0)
    log_line("notification spawn failed errno=%d", result);
  else
    previous = child;
  g_last_notice = now;
}

// Implements process-name-only notification text for one ALERT episode action.
void action_notification(const Actions& actions, const Level prior_level) {
  for (size_t i = 0; i < actions.count; ++i) {
    if (actions.items[i].kind == ActionKind::kill) {
      const Action& action = actions.items[i];
      const char* name = "eligible work";
      for (size_t j = 0; j < g_candidate_count; ++j)
        if (g_candidates[j].pid == action.pid && g_candidates[j].pgid == action.pgid) {
          name = candidate_name(g_candidates[j]);
          break;
        }
      char message[256];
      snprintf(message, sizeof(message), "Memory guard terminated %s.", name);
      notify(message);
      return;
    }
  }
  if (actions.level == Level::alert && !g_alert_notified) {
    for (size_t i = 0; i < actions.count; ++i)
      if (actions.items[i].kind == ActionKind::freeze) {
        char names[160]{};
        size_t used = 0;
        size_t shown = 0;
        for (size_t action_index = i; action_index < actions.count; ++action_index) {
          const Action& action = actions.items[action_index];
          if (action.kind != ActionKind::freeze)
            continue;
          const char* name = "eligible work";
          for (size_t j = 0; j < g_candidate_count; ++j)
            if (g_candidates[j].pid == action.pid && g_candidates[j].pgid == action.pgid) {
              name = candidate_name(g_candidates[j]);
              break;
            }
          if (shown != 0 && used + 2 < sizeof(names)) {
            names[used++] = ',';
            names[used++] = ' ';
          }
          const int length = snprintf(names + used, sizeof(names) - used, "%s", name);
          if (length <= 0 || static_cast<size_t>(length) >= sizeof(names) - used)
            break;
          used += static_cast<size_t>(length);
          ++shown;
          if (shown == 4)
            break;
        }
        char message[256];
        snprintf(message, sizeof(message), "Memory guard froze %s.",
                 shown == 0 ? "eligible work" : names);
        notify(message);
        g_alert_notified = true;
        return;
      }
  }
  if (prior_level != Level::calm && actions.level == Level::calm) {
    notify("Memory guard returned to calm and is resuming frozen work.");
    g_alert_notified = false;
  }
}

// Implements individual-pid SIGSTOP with a verified process identity.
bool freeze_unit(const Action& action, uint64_t second) {
  bool signalled = false;
  const uint64_t episode = freeze_episode(second);
  for (size_t i = 0; i < g_process_count; ++i) {
    Process& process = g_processes[i];
    const bool member = action.pid > 0 ? process.pid == action.pid
                                       : process.pgid == action.pgid && process.tier == Tier::a;
    if (!member || !process.eligible || process.frozen || process_stopped(process.pid) ||
        freeze_attempted(process, episode))
      continue;
    if (checked_signal(process.pid, process.start_sec, process.start_usec, process.pgid, SIGSTOP)) {
      remember_freeze_attempt(process, episode);
      remember_frozen(process, second);
      record_action(g_state, second);
      log_line("signal=SIGSTOP name=%s pid=%d tier=%c footprint=%llu", process.name, process.pid,
               'A' + static_cast<int>(process.tier),
               static_cast<unsigned long long>(process.footprint));
      if (!persist_frozen_state())
        log_line("state persistence failed after SIGSTOP pid=%d", process.pid);
      signalled = true;
    }
  }
  return signalled;
}

// Implements one-unit SIGCONT and identity-safe removal from persistent freeze state.
bool resume_unit(const Action& action, uint64_t second) {
  bool resumed = false;
  for (size_t i = 0; i < g_frozen_count;) {
    FrozenProcess frozen = g_frozen[i];
    if (action.pid > 0 ? frozen.pid != action.pid : frozen.pgid != action.pgid) {
      ++i;
      continue;
    }
    if (checked_signal(frozen.pid, frozen.start_sec, frozen.start_usec, frozen.pgid, SIGCONT)) {
      remember_resumed(frozen, second);
      log_line("signal=SIGCONT name=%s pid=%d tier=A footprint=%llu",
               process_name(frozen.pid, frozen.start_sec, frozen.start_usec), frozen.pid,
               static_cast<unsigned long long>(process_footprint(
                   frozen.pid, frozen.start_sec, frozen.start_usec)));
      resumed = true;
      g_frozen[i] = g_frozen[--g_frozen_count];
      continue;
    }
    ++i;
  }
  if (resumed)
    (void)persist_frozen_state();
  return resumed;
}

// Implements bounded SIGTERM, identity recheck, then SIGKILL of surviving unit members.
bool kill_unit(const Action& action, uint64_t second) {
  bool terminated = false;
  g_kill_target_count = 0;
  for (size_t i = 0; i < g_process_count; ++i) {
    const Process& process = g_processes[i];
    const bool member = action.pid > 0 ? process.pid == action.pid
                                       : process.pgid == action.pgid && process.tier == Tier::a;
    if (!member || !process.eligible)
      continue;
    if (checked_signal(process.pid, process.start_sec, process.start_usec, process.pgid, SIGTERM)) {
      g_kill_targets[g_kill_target_count++] = process;
      terminated = true;
      record_action(g_state, second);
      log_line("signal=SIGTERM name=%s pid=%d tier=%c footprint=%llu", process.name, process.pid,
               'A' + static_cast<int>(process.tier),
               static_cast<unsigned long long>(process.footprint));
    }
  }
  if (!terminated)
    return false;
  timespec grace{1, 500000000};
  while (!g_stop_requested && nanosleep(&grace, &grace) != 0 && errno == EINTR) {
  }
  if (g_stop_requested)
    return true;
  (void)enumerate_processes(uptime_second());
  for (size_t i = 0; i < g_kill_target_count; ++i) {
    const Process& process = g_kill_targets[i];
    if (checked_signal(process.pid, process.start_sec, process.start_usec, process.pgid, SIGKILL)) {
      record_action(g_state, second);
      log_line("signal=SIGKILL name=%s pid=%d tier=%c footprint=%llu", process.name, process.pid,
               'A' + static_cast<int>(process.tier),
               static_cast<unsigned long long>(process.footprint));
    }
  }
  (void)persist_frozen_state();
  return true;
}

// Implements action execution only after the decision has been logged.
void apply_actions(const Actions& actions, uint64_t second) {
  bool changed_state = false;
  for (size_t i = 0; i < actions.count; ++i) {
    const Action& action = actions.items[i];
    if (action.kind == ActionKind::freeze)
      changed_state = freeze_unit(action, second) || changed_state;
    else if (action.kind == ActionKind::resume)
      changed_state = resume_unit(action, second) || changed_state;
    else if (action.kind == ActionKind::kill)
      changed_state = kill_unit(action, second) || changed_state;
  }
  if (changed_state && !persist_frozen_state())
    log_line("state persistence failed after signal action");
}

// Implements safe shutdown by resuming every still-matching frozen identity.
void shutdown_resume(int) {
  g_stop_requested = true;
}

// Implements resume-and-clear behavior on SIGTERM or SIGINT.
void finish_shutdown() {
  for (size_t i = 0; i < g_frozen_count; ++i) {
    const FrozenProcess& frozen = g_frozen[i];
    if (checked_signal(frozen.pid, frozen.start_sec, frozen.start_usec, frozen.pgid, SIGCONT))
      log_line("signal=SIGCONT name=%s pid=%d tier=A footprint=%llu",
               process_name(frozen.pid, frozen.start_sec, frozen.start_usec), frozen.pid,
               static_cast<unsigned long long>(process_footprint(
                   frozen.pid, frozen.start_sec, frozen.start_usec)));
  }
  g_frozen_count = 0;
  (void)persist_frozen_state();
}

// Implements parent-directory creation for logs, state and consent artifacts.
void ensure_parent(const char* target) {
  char path[PATH_MAX];
  strlcpy(path, target, sizeof(path));
  char* slash = strrchr(path, '/');
  if (slash == nullptr)
    return;
  *slash = 0;
  for (char* cursor = path + 1; *cursor != 0; ++cursor)
    if (*cursor == '/') {
      *cursor = 0;
      (void)mkdir(path, 0700);
      *cursor = '/';
    }
  (void)mkdir(path, 0700);
}

// Implements process-name-only metrics and frozen-process status output.
int command_status() {
  Sample sample{};
  if (!read_live_sample(sample)) {
    fprintf(stderr, "primary compressor metric unavailable\n");
    return 1;
  }
  capture_ancestors();
  (void)enumerate_processes(sample.second);
  load_frozen_state(false);
  const char* level = "CALM";
  FILE* log = fopen(g_log_path, "r");
  if (log != nullptr) {
    char line[512];
    while (fgets(line, sizeof(line), log) != nullptr) {
      char* transition = strstr(line, "transition=");
      char* arrow = transition == nullptr ? nullptr : strstr(transition, "->");
      if (arrow != nullptr) {
        static char changed_level[16];
        if (sscanf(arrow + 2, "%15[A-Z]", changed_level) == 1)
          level = changed_level;
      }
      char* marker = strstr(line, "level=");
      if (marker != nullptr) {
        static char last_level[16];
        if (sscanf(marker + 6, "%15[A-Z]", last_level) == 1)
          level = last_level;
      }
    }
    fclose(log);
  }
  printf("segments %llu/%llu (%llu%%); ",
         static_cast<unsigned long long>(sample.segments),
         static_cast<unsigned long long>(sample.segment_limit),
         static_cast<unsigned long long>(pct(sample.segments, sample.segment_limit)));
  if (sample.compressed_limit != 0)
    printf("compressed pages %llu/%llu (%llu%%); ",
           static_cast<unsigned long long>(sample.compressed_pages),
           static_cast<unsigned long long>(sample.compressed_limit),
           static_cast<unsigned long long>(pct(sample.compressed_pages, sample.compressed_limit)));
  printf("swap %llu MiB; pressure %d; level %s\n",
         static_cast<unsigned long long>(sample.swap_used / kMiB), sample.pressure,
         level);
  for (size_t i = 0; i < g_frozen_count; ++i)
    printf("frozen name=%s pid=%d pgid=%d\n",
           process_name(g_frozen[i].pid, g_frozen[i].start_sec, g_frozen[i].start_usec),
           g_frozen[i].pid, g_frozen[i].pgid);
  return 0;
}

// Implements read-only candidate ranking without exposing arguments or paths.
int command_explain() {
  Sample sample{};
  capture_ancestors();
  if (!read_live_sample(sample) || !enumerate_processes(sample.second))
    return 1;
  const Actions actions = decide(g_state, sample, g_candidates, g_candidate_count, g_config);
  printf("level %s; would-be actions %zu\n",
         actions.level == Level::calm    ? "CALM"
         : actions.level == Level::alert ? "ALERT"
                                         : "EMERGENCY",
         actions.count);
  bool shown[kMaxProcesses]{};
  const size_t show_count = g_candidate_count < 20 ? g_candidate_count : 20;
  for (size_t shown_count = 0; shown_count < show_count; ++shown_count) {
    size_t selected = g_candidate_count;
    for (size_t i = 0; i < g_candidate_count; ++i) {
      if (shown[i])
        continue;
      if (selected == g_candidate_count ||
          candidate_score(g_candidates[i]) > candidate_score(g_candidates[selected]))
        selected = i;
    }
    if (selected == g_candidate_count)
      break;
    shown[selected] = true;
    const Candidate& candidate = g_candidates[selected];
    const char* name = candidate_name(candidate);
    printf("tier=%c frozen=%s footprint=%llu MiB growth30=%llu MiB name=%s\n",
           'A' + static_cast<int>(candidate.tier), candidate.frozen ? "yes" : "no",
           static_cast<unsigned long long>(candidate.footprint / kMiB),
           static_cast<unsigned long long>(candidate.growth30 / kMiB), name);
  }
  for (size_t i = 0; i < actions.count; ++i) {
    const Action& action = actions.items[i];
    const char* name = "process";
    uint64_t footprint = 0;
    Tier tier = Tier::a;
    const Candidate* target = nullptr;
    for (size_t j = 0; j < g_candidate_count; ++j)
      if (g_candidates[j].pid == action.pid && g_candidates[j].pgid == action.pgid) {
        target = &g_candidates[j];
        footprint = g_candidates[j].footprint;
        tier = g_candidates[j].tier;
        break;
      }
    if (target != nullptr)
      name = candidate_name(*target);
    printf("would action=%d name=%s pid=%d tier=%c footprint=%llu\n",
           static_cast<int>(action.kind), name, action.pid, 'A' + static_cast<int>(tier),
           static_cast<unsigned long long>(footprint));
  }
  return 0;
}

// Implements read-only signal and metric capability checks.
int command_doctor() {
  Sample sample{};
  if (!read_live_sample(sample)) {
    fprintf(stderr, "primary compressor metric unavailable\n");
    return 1;
  }
  printf("segments: readable (%llu/%llu)\n", static_cast<unsigned long long>(sample.segments),
         static_cast<unsigned long long>(sample.segment_limit));
  printf("swap: readable; pressure: %d; process enumeration: ", sample.pressure);
  pid_t ids[1]{};
  printf("%s\n", proc_listpids(PROC_ALL_PIDS, 0, ids, sizeof(ids)) > 0 ? "readable" : "unreadable");
  return proc_listpids(PROC_ALL_PIDS, 0, ids, sizeof(ids)) > 0 ? 0 : 1;
}

// Implements timestamped reasons and measurements for each level transition.
void log_level_change(Level previous, Level current, const Sample& sample) {
  if (previous == current)
    return;
  const TrendMeasurement alert_trend =
      measure_trend(g_state, sample, g_config.trend_horizon, kAlertSlopeWindowSeconds);
  const TrendMeasurement emergency_trend =
      measure_trend(g_state, sample, g_config.emergency_horizon, kEmergencySlopeWindowSeconds);
  const Sample* swap_old = find_ago(g_state, sample.second, kSwapGrowthWindowSeconds, 0);
  const uint64_t swap_growth = swap_old != nullptr && sample.swap_used >= swap_old->swap_used
                                   ? (sample.swap_used - swap_old->swap_used) / kMiB
                                   : 0;
  const bool segment_alert =
      at_or_above(sample.segments, sample.segment_limit, g_config.alert_pct);
  const bool alert_trend_hit =
      alert_trend.available &&
      alert_trend.projected_segments >=
          static_cast<long double>(sample.segment_limit) * g_config.alert_trend_pct / 100.0L;
  const bool swap_alert =
      swap_old != nullptr && sample.swap_used >= swap_old->swap_used &&
      sample.swap_used - swap_old->swap_used >= g_config.swap_growth;
  const bool pressure_alert = g_state.critical_streak >= g_config.critical_samples;
  const bool segment_emergency =
      at_or_above(sample.segments, sample.segment_limit, g_config.emergency_pct);
  const bool emergency_trend_hit =
      emergency_trend.available &&
      emergency_trend.projected_segments >=
          static_cast<long double>(sample.segment_limit) * g_config.emergency_trend_pct / 100.0L;
  const long long alert_pct = alert_trend.available
                                  ? static_cast<long long>(alert_trend.projected_pct)
                                  : -1;
  const long long alert_age = alert_trend.available
                                  ? static_cast<long long>(alert_trend.baseline_age)
                                  : -1;
  const long long emergency_pct = emergency_trend.available
                                      ? static_cast<long long>(emergency_trend.projected_pct)
                                      : -1;
  const long long emergency_age = emergency_trend.available
                                      ? static_cast<long long>(emergency_trend.baseline_age)
                                      : -1;
  const char* previous_name = previous == Level::calm    ? "CALM"
                              : previous == Level::alert ? "ALERT"
                                                         : "EMERGENCY";
  const char* current_name = current == Level::calm    ? "CALM"
                            : current == Level::alert ? "ALERT"
                                                      : "EMERGENCY";
  log_line("level_change transition=%s->%s segments_pct=%llu segment_alert=%d "
           "alert_trend_pct=%lld alert_trend_age_s=%lld alert_trend_hit=%d "
           "swap_window_valid=%d swap_growth_mib=%llu swap_alert=%d pressure=%d "
           "pressure_streak=%u/%u pressure_alert=%d emergency_trend_pct=%lld "
           "emergency_trend_age_s=%lld emergency_trend_hit=%d segment_emergency=%d "
           "alert_now=%d emergency_now=%d",
           previous_name, current_name,
           static_cast<unsigned long long>(pct(sample.segments, sample.segment_limit)),
           segment_alert, alert_pct, alert_age, alert_trend_hit, swap_old != nullptr,
           static_cast<unsigned long long>(swap_growth), swap_alert, sample.pressure,
           g_state.critical_streak, g_config.critical_samples, pressure_alert, emergency_pct,
           emergency_age, emergency_trend_hit, segment_emergency,
           alert_now(g_state, sample, g_config), emergency_now(g_state, sample, g_config));
}

// Implements cadence-limited metrics lines and decision/action name records.
void log_decision(const Sample& sample, const Actions& actions) {
  const bool due = actions.level != Level::calm || g_last_metric_log == 0 ||
                   sample.second < g_last_metric_log || sample.second - g_last_metric_log >= 60;
  if (due) {
    log_line("metrics segments=%llu/%llu percent=%llu swap=%llu pressure=%d level=%s",
             static_cast<unsigned long long>(sample.segments),
             static_cast<unsigned long long>(sample.segment_limit),
             static_cast<unsigned long long>(pct(sample.segments, sample.segment_limit)),
             static_cast<unsigned long long>(sample.swap_used), sample.pressure,
             actions.level == Level::calm    ? "CALM"
             : actions.level == Level::alert ? "ALERT"
                                             : "EMERGENCY");
    g_last_metric_log = sample.second;
  }
  for (size_t i = 0; i < actions.count; ++i) {
    const Action& action = actions.items[i];
    const char* kind = action.kind == ActionKind::freeze   ? "freeze"
                       : action.kind == ActionKind::resume ? "resume"
                                                           : "kill";
    if (!g_act_mode)
      kind = action.kind == ActionKind::freeze   ? "would_freeze"
             : action.kind == ActionKind::resume ? "would_resume"
                                                 : "would_kill";
    const char* name = "process";
    uint64_t footprint = 0;
    Tier tier = Tier::a;
    const Candidate* target = nullptr;
    for (size_t j = 0; j < g_candidate_count; ++j)
      if (g_candidates[j].pid == action.pid && g_candidates[j].pgid == action.pgid) {
        target = &g_candidates[j];
        footprint = g_candidates[j].footprint;
        tier = g_candidates[j].tier;
        break;
      }
    if (target != nullptr)
      name = candidate_name(*target);
    log_line("decision=%s name=%s pid=%d tier=%c footprint=%llu", kind, name, action.pid,
             'A' + static_cast<int>(tier), static_cast<unsigned long long>(footprint));
  }
}

// Implements the one-second decision loop and explicit fail-closed sampling errors.
int run_loop() {
  if (g_act_mode && !g_test_mode && !consent_is_current()) {
    fprintf(stderr, "act mode requires consent --accept for current scope v2\n");
    return 1;
  }
  if (g_act_mode && !g_test_mode && command_doctor() != 0)
    return 1;
  capture_ancestors();
  if (g_test_mode && !g_test_root_valid) {
    fprintf(stderr, "test root must be one of this guard's own ancestors\n");
    return 1;
  }
  if (g_test_mode && g_metrics_fd < 0) {
    fprintf(stderr, "test metrics could not be opened\n");
    return 1;
  }
  ensure_parent(g_state_path);
  ensure_parent(g_log_path);
  pthread_set_qos_class_self_np(QOS_CLASS_USER_INTERACTIVE, 0);
  (void)signal(SIGCHLD, SIG_IGN);
  struct sigaction handler{};
  handler.sa_handler = shutdown_resume;
  sigemptyset(&handler.sa_mask);
  (void)sigaction(SIGTERM, &handler, nullptr);
  (void)sigaction(SIGINT, &handler, nullptr);
  g_log_fd = open(g_log_path, O_WRONLY | O_CREAT | O_APPEND, 0600);
  if (g_log_fd < 0) {
    perror("log open");
    return 1;
  }
  load_frozen_state();
  while (!g_stop_requested) {
    Sample sample{};
    const bool sample_ok = g_test_mode ? read_test_sample(sample) : read_live_sample(sample);
    if (!sample_ok) {
      if (g_test_mode)
        break;
      log_line("invalid metrics; no action this tick");
      sleep(1);
      continue;
    }
    if (!enumerate_processes(sample.second)) {
      log_line("process enumeration failed; no action this tick");
      usleep(g_test_tick_ms * 1000);
      continue;
    }
    const Level previous = g_state.level;
    const Actions actions = decide(g_state, sample, g_candidates, g_candidate_count, g_config);
    log_level_change(previous, actions.level, sample);
    if (g_test_mode)
      log_line("test sample=%llu candidates=%zu level=%s actions=%zu",
               static_cast<unsigned long long>(sample.second), g_candidate_count,
               actions.level == Level::calm    ? "CALM"
               : actions.level == Level::alert ? "ALERT"
                                               : "EMERGENCY",
               actions.count);
    if (g_test_mode)
      for (size_t i = 0; i < g_candidate_count; ++i)
        log_line("test candidate pid=%d pgid=%d tier=%c footprint=%llu frozen=%d eligible=%d",
                 g_candidates[i].pid, g_candidates[i].pgid,
                 'A' + static_cast<int>(g_candidates[i].tier),
                 static_cast<unsigned long long>(g_candidates[i].footprint), g_candidates[i].frozen,
                 g_candidates[i].eligible);
    log_decision(sample, actions);
    if (g_act_mode)
      apply_actions(actions, sample.second);
    if (g_act_mode)
      action_notification(actions, previous);
    if (g_test_mode)
      usleep(g_test_tick_ms * 1000);
    else
      sleep(1);
  }
  if (g_act_mode)
    finish_shutdown();
  if (g_metrics_fd >= 0)
    close(g_metrics_fd);
  close(g_log_fd);
  g_log_fd = -1;
  return 0;
}

// Implements scope-v2 consent reporting and versioned persistence.
int consent_command(const char* option) {
  if (strcmp(option, "--show") == 0) {
    FILE* file = fopen(g_consent_path, "r");
    if (file == nullptr) {
      puts("no consent recorded");
      return 0;
    }
    char line[512];
    while (fgets(line, sizeof(line), file) != nullptr)
      fputs(line, stdout);
    fclose(file);
    return 0;
  }
  if (strcmp(option, "--revoke") == 0) {
    if (unlink(g_consent_path) != 0 && errno != ENOENT)
      return 1;
    puts("consent revoked");
    return 0;
  }
  if (strcmp(option, "--accept") != 0)
    return 2;
  ensure_parent(g_consent_path);
  puts(
      "Consent v2: ALERT freezes tier-A units >=500 MiB. After 120 s from ALERT entry, "
      "while alert conditions persist, frozen units are killed largest-first, one every 30 s; "
      "new eligible tier-A units continue to freeze. EMERGENCY kills one unit, "
      "then waits at least 3 s: frozen, tier A >=300 MiB, tier B >=300 MiB only at 88% "
      "segments, tier C >=300 MiB only at 93%. A tier-A unit resumed by the guard "
      "within 15 minutes is killed on the next alarm instead of frozen. "
      "Each process is identity-checked; protected "
      "and foreign processes are never signalled. CALM resumes frozen units smallest-first, "
      "15 s apart. SIGTERM is followed by SIGKILL after 1.5 s to surviving matching pids.");
  char temporary[PATH_MAX];
  snprintf(temporary, sizeof(temporary), "%s.tmp.%d", g_consent_path, getpid());
  const int fd = open(temporary, O_WRONLY | O_CREAT | O_EXCL, 0600);
  if (fd < 0)
    return 1;
  char record[128];
  const int length =
      snprintf(record, sizeof(record), "{\"scope_version\":%d,\"accepted\":true,\"time\":%lld}\n",
               kConsentVersion, static_cast<long long>(time(nullptr)));
  const bool ok = write(fd, record, static_cast<size_t>(length)) == length && fsync(fd) == 0;
  close(fd);
  if (!ok || rename(temporary, g_consent_path) != 0) {
    unlink(temporary);
    return 1;
  }
  return 0;
}

// Implements exact argument validation for test-only isolation switches.
int main_run(int argc, char** argv) {
  const char* config = g_config_path;
  bool config_explicit = false;
  const char* metrics = nullptr;
  bool have_root = false;
  bool have_test_tick = false;
  for (int i = 2; i < argc; ++i) {
    if (strcmp(argv[i], "--config") == 0 && i + 1 < argc) {
      config = argv[++i];
      config_explicit = true;
    } else if (strcmp(argv[i], "--test-metrics") == 0 && i + 1 < argc)
      metrics = argv[++i];
    else if (strcmp(argv[i], "--test-root") == 0 && i + 1 < argc) {
      g_test_root = static_cast<pid_t>(strtol(argv[++i], nullptr, 10));
      have_root = true;
    } else if (strcmp(argv[i], "--test-tick-ms") == 0 && i + 1 < argc) {
      have_test_tick = true;
      g_test_tick_ms = static_cast<unsigned>(strtoul(argv[++i], nullptr, 10));
      if (g_test_tick_ms == 0 || g_test_tick_ms > 10000)
        return 2;
    } else {
      fprintf(stderr, "unknown run option: %s\n", argv[i]);
      return 2;
    }
  }
  if ((metrics == nullptr) != !have_root) {
    fprintf(stderr, "--test-metrics and --test-root must be used together\n");
    return 2;
  }
  g_test_mode = metrics != nullptr && have_root;
  if (have_test_tick && !g_test_mode) {
    fprintf(stderr, "--test-tick-ms requires --test-metrics and --test-root\n");
    return 2;
  }
  if (g_test_mode) {
    g_metrics_fd = open(metrics, O_RDONLY);
    if (g_metrics_fd < 0) {
      perror("test metrics open");
      return 1;
    }
    g_act_mode = false;
    if (config_explicit && !read_config(config, false))
      return 2;
  } else if (!read_config(config, !config_explicit)) {
    return 2;
  }
  if (g_test_mode && g_act_mode)
    g_act_mode = true;
  return run_loop();
}

}  // namespace

// Implements command dispatch without touching user state for read-only commands.
int main(int argc, char** argv) {
  g_owner_uid = getuid();
  struct passwd* account = getpwuid(g_owner_uid);
  if (account == nullptr)
    return 1;
  strlcpy(g_home, account->pw_dir, sizeof(g_home));
  snprintf(g_config_path, sizeof(g_config_path), "%s/.config/mac-health/memory-guard.conf", g_home);
  snprintf(g_consent_path, sizeof(g_consent_path),
           "%s/.config/mac-health/memory-guard-consent.json", g_home);
  snprintf(g_state_path, sizeof(g_state_path), "%s/.local/state/mac-health/memory-guard.state",
           g_home);
  snprintf(g_log_path, sizeof(g_log_path), "%s/Library/Logs/mac-health/memory-guard.log", g_home);
  if (argc < 2) {
    fprintf(stderr, "usage: mac-memory-guard run|status|explain|resume|doctor|consent\n");
    return 2;
  }
  if (strcmp(argv[1], "run") == 0)
    return main_run(argc, argv);
  if (strcmp(argv[1], "doctor") == 0)
    return command_doctor();
  if (strcmp(argv[1], "status") == 0) {
    if (!read_config(g_config_path, true))
      return 2;
    return command_status();
  }
  if (strcmp(argv[1], "explain") == 0) {
    if (!read_config(g_config_path, true))
      return 2;
    return command_explain();
  }
  if (strcmp(argv[1], "consent") == 0)
    return argc > 2 ? consent_command(argv[2]) : 2;
  if (strcmp(argv[1], "resume") == 0) {
    if (!read_config(g_config_path, true))
      return 2;
    const bool all = argc < 3 || strcmp(argv[2], "--all") == 0;
    const pid_t wanted = all ? 0 : static_cast<pid_t>(strtol(argv[2], nullptr, 10));
    if (!all && wanted <= 0) {
      fprintf(stderr, "resume requires --all or a positive PGID\n");
      return 2;
    }
    capture_ancestors();
    load_frozen_state();
    for (size_t i = 0; i < g_frozen_count;) {
      const FrozenProcess frozen = g_frozen[i];
      if (all || frozen.pgid == wanted) {
        if (checked_signal(frozen.pid, frozen.start_sec, frozen.start_usec, frozen.pgid, SIGCONT)) {
          remember_resumed(frozen, uptime_second());
          g_frozen[i] = g_frozen[--g_frozen_count];
          continue;
        }
      }
      ++i;
    }
    return persist_frozen_state() ? 0 : 1;
  }
  fprintf(stderr, "unknown command\n");
  return 2;
}
