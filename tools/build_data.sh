#!/usr/bin/env bash
# M2: build the training data on the Mac. Run from the repository root:   tools/build_data.sh
# Self-setting-up: uses the preflight venv (~/ail-train-work/venv, made if missing). Reads the untracked config.local:
#   AIL_ROOT="$HOME/ail-train-work/ail-pinned"   # an ail checkout at .ail-version
#   BASE_MODEL="org/model-4bit"                  # optional: its tokenizer measures lengths (else an estimate)
# Optional environment: SYSTEM (short | core | FILE, default short), MAX_TOKENS (default 2048), JOBS (default 4).
# Builds twice and compares the outputs byte for byte (the second build reads the compiler cache, so it is quick).
# Output: data/build/{train,valid,quick-eval}.jsonl and manifest.json (git-ignored). bash 3.2 compatible.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
work="$HOME/ail-train-work"
die() { echo "build_data: $*" >&2; exit 2; }
[ -f "$root/config.local" ] && . "$root/config.local"
ail_root="${AIL_ROOT:-$work/ail-pinned}"
[ -x "$ail_root/ail" ] || die "no ail at $ail_root (set AIL_ROOT in config.local)"
if pgrep -f "mac-gate.sh" >/dev/null 2>&1; then die "the AIL Mac gate is running; try again after it finishes"; fi
venv="$work/venv"
if [ ! -x "$venv/bin/python" ]; then
    py=""
    for c in python3.13 python3.12 python3.11 python3.10 /opt/homebrew/bin/python3 python3; do
        if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(sys.version_info < (3, 10))' 2>/dev/null; then
            py="$(command -v "$c")"; break
        fi
    done
    [ -n "$py" ] || die "needs Python 3.10 or newer"
    "$py" -m venv "$venv" && "$venv/bin/python" -m pip install --quiet mlx-lm huggingface_hub || die "venv setup failed"
fi
vpy="$venv/bin/python"
export HF_HOME="$work/hf"
export HF_HUB_DISABLE_TELEMETRY=1
tokdir=""
if [ -n "${BASE_MODEL:-}" ]; then
    tokdir="$("$vpy" -c 'import sys; from huggingface_hub import snapshot_download; print(snapshot_download(sys.argv[1]))' "$BASE_MODEL" 2>/dev/null | tail -1)"
    [ -d "$tokdir" ] || die "could not find or fetch $BASE_MODEL"
fi
args="--ail $ail_root --system ${SYSTEM:-short} --max-tokens ${MAX_TOKENS:-2048} --jobs ${JOBS:-4}"
[ -n "$tokdir" ] && args="$args --tokenizer $tokdir"
out="$root/data/build"
again="$work/build-again"
# shellcheck disable=SC2086
"$vpy" "$root/tools/build_data.py" $args --out "$out" || die "build failed"
rm -rf "$again"
# shellcheck disable=SC2086
"$vpy" "$root/tools/build_data.py" $args --out "$again" > /dev/null || die "second build failed"
for f in train.jsonl valid.jsonl quick-eval.jsonl manifest.json; do
    a="$(shasum -a 256 < "$out/$f")"; b="$(shasum -a 256 < "$again/$f")"
    [ "$a" = "$b" ] || die "the rebuild differs in $f: the builder is not deterministic"
done
echo "deterministic: both builds match"
echo "built: $out (see manifest.json)"
