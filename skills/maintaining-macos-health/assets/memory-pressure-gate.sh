#!/bin/sh
set -eu

read_free_percent() {
  line=$(memory_pressure | tail -1)
  percent=$(printf '%s\n' "$line" | awk -F '[:%]' \
    '/System-wide memory free percentage:/ {gsub(/[[:space:]]/, "", $2); print $2}')
  case "$percent" in
    ''|*[!0-9]*)
      echo "cannot read system-wide free memory percentage" >&2
      return 1
      ;;
  esac
  printf '%s\n' "$percent"
}

wait_for_headroom() {
  percent=$(read_free_percent)
  while [ "$percent" -lt 30 ]; do
    echo "system-wide free memory is ${percent}%; waiting before native work" >&2
    sleep 5
    percent=$(read_free_percent)
  done
}

check_floor() {
  percent=$(read_free_percent)
  if [ "$percent" -lt 20 ]; then
    echo "system-wide free memory fell to ${percent}%; stopping native work" >&2
    return 1
  fi
}

child_running() {
  state=$(ps -p "$1" -o stat= 2>/dev/null || true)
  case "$state" in
    ''|*Z*) return 1 ;;
    *) return 0 ;;
  esac
}

run_command() {
  wait_for_headroom
  "$@" &
  child=$!
  while child_running "$child"; do
    percent=$(read_free_percent)
    if [ "$percent" -lt 20 ]; then
      echo "system-wide free memory fell to ${percent}%; stopping native work" >&2
      kill -TERM "$child" 2>/dev/null || true
      wait "$child" 2>/dev/null || true
      return 1
    fi
    sleep 1
  done
  set +e
  wait "$child"
  status=$?
  set -e
  check_floor || return 1
  return "$status"
}

case "${1:-}" in
  wait)
    wait_for_headroom
    ;;
  check)
    check_floor
    ;;
  run)
    shift
    if [ "$#" -eq 0 ]; then
      echo "usage: memory-pressure-gate.sh run COMMAND [ARG ...]" >&2
      exit 2
    fi
    run_command "$@"
    ;;
  *)
    echo "usage: memory-pressure-gate.sh wait|check|run" >&2
    exit 2
    ;;
esac
