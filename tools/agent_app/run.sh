#!/usr/bin/env bash
# The agentic-coding test (tools/agent_app/agent_app.py): one app, built in AIL and in Python by an API model.
# Run on the Mac from the repository root:   tools/agent_app/run.sh
# Needs: config.local (untracked) setting BUILDER_MODEL and HELPER_MODEL; an Anthropic API key in ANTHROPIC_API_KEY or
# in ~/.config/ail-train/anthropic-key (asked once and saved there, mode 600, never in git).
# Optional environment: CAP_TOTAL (USD, default 15), RUN_DIR (resume a run), AIL_ROOT (default ~/ail-train-work/ail-pinned).
# Results: runs/agent-app/STAMP/REPORT.md (runs/ is not in git). A rerun resumes the newest unfinished run, skipping finished phases.
set -u
root="$(cd "$(dirname "$0")/../.." && pwd)"
work="$HOME/ail-train-work"
die() { echo "run.sh: $*" >&2; exit 2; }
[ -f "$root/config.local" ] && . "$root/config.local"
[ -n "${BUILDER_MODEL:-}" ] || die "config.local sets no BUILDER_MODEL"
[ -n "${HELPER_MODEL:-}" ] || die "config.local sets no HELPER_MODEL"
command -v python3 >/dev/null || die "python3 not found"

keyfile="$HOME/.config/ail-train/anthropic-key"
if [ -z "${ANTHROPIC_API_KEY:-}" ] && [ -s "$keyfile" ]; then
    ANTHROPIC_API_KEY="$(cat "$keyfile")"
fi
if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    [ -t 0 ] || die "no API key: set ANTHROPIC_API_KEY or run this once in a terminal"
    printf "Anthropic API key (saved to %s, not shown): " "$keyfile"
    read -rs ANTHROPIC_API_KEY
    echo
    [ -n "$ANTHROPIC_API_KEY" ] || die "no key given"
    mkdir -p "$(dirname "$keyfile")"
    (umask 077; printf "%s" "$ANTHROPIC_API_KEY" > "$keyfile")
fi
export ANTHROPIC_API_KEY

# The AIL compiler at the pinned commit, in its own worktree so the main ail checkout is never moved.
pin="$(cat "$root/.ail-version")"
ail_root="${AIL_ROOT:-$work/ail-pinned}"
if [ ! -d "$ail_root" ]; then
    src="$HOME/Documents/Projects/ail"
    [ -d "$src/.git" ] || die "no ail checkout at $src to make $ail_root from"
    mkdir -p "$work"
    git -C "$src" fetch -q origin || true
    git -C "$src" worktree add -q --detach "$ail_root" "$pin" || die "could not make the pinned worktree"
fi
have="$(git -C "$ail_root" rev-parse HEAD 2>/dev/null || true)"
[ "$have" = "$pin" ] || die "$ail_root is at ${have:-unknown}, but .ail-version pins $pin"
echo "warming the AIL compiler (the first build can take a few minutes)"
"$ail_root/ail" check "$ail_root/examples/hello.ail" >/dev/null 2>&1 || "$ail_root/ail" check "$ail_root/examples/hello.ail" \
    || die "ail check on examples/hello.ail failed"

# The current anthropic SDK needs Python 3.10 or newer; macOS ships 3.9. Use a newer one, installing it with Homebrew if needed.
py_ok() { "$1" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; }
find_py() {
    for p in python3.14 python3.13 python3.12 python3.11 python3.10 /opt/homebrew/bin/python3 /usr/local/bin/python3 python3; do
        c="$(command -v "$p" 2>/dev/null)" || continue
        py_ok "$c" && { echo "$c"; return 0; }
    done
    return 1
}
py="$(find_py)"
if [ -z "$py" ]; then
    brew="$(command -v brew || echo /opt/homebrew/bin/brew)"
    [ -x "$brew" ] || die "needs Python 3.10 or newer and no Homebrew to install it; install Python from python.org"
    echo "installing Python 3.12 with Homebrew"
    "$brew" install python@3.12 >/dev/null || die "brew install python@3.12 failed"
    py="$(find_py)" || true
    [ -n "$py" ] || py="$("$brew" --prefix python@3.12)/bin/python3.12"
    py_ok "$py" || die "no Python 3.10 or newer after installing"
fi
venv="$work/venv-agent-app"
if [ -x "$venv/bin/python" ] && ! py_ok "$venv/bin/python"; then
    rm -rf "$venv"
fi
if [ ! -x "$venv/bin/python" ]; then
    "$py" -m venv "$venv" || die "could not make $venv"
fi
"$venv/bin/python" -m pip -q install --upgrade pip >/dev/null 2>&1 || true
"$venv/bin/python" -m pip -q install --upgrade "anthropic>=2.14" >/dev/null || die "could not install the anthropic SDK"

# Resume the newest run that has no REPORT.md yet (its spend.json keeps counting toward the cap), else start a new one.
last="$(ls -d "$root"/runs/agent-app/*/ 2>/dev/null | tail -1)"
if [ -z "${RUN_DIR:-}" ] && [ -n "$last" ] && [ ! -f "$last/REPORT.md" ]; then RUN_DIR="${last%/}"; echo "resuming $RUN_DIR"; fi
run_dir="${RUN_DIR:-$root/runs/agent-app/$(date +%Y%m%d-%H%M%S)}"
mkdir -p "$run_dir"
echo "run folder: $run_dir"
export RUN_DIR="$run_dir" AIL_ROOT="$ail_root" TRAIN_ROOT="$root" BUILDER_MODEL HELPER_MODEL
keep=""; command -v caffeinate >/dev/null && keep="caffeinate -i"
$keep "$venv/bin/python" "$root/tools/agent_app/agent_app.py" 2>&1 | tee -a "$run_dir/console.log"
status="${PIPESTATUS[0]}"
[ -f "$run_dir/REPORT.md" ] && echo "report: $run_dir/REPORT.md"
exit "$status"
