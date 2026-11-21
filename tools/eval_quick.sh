#!/usr/bin/env bash
# M5 quick eval on the Mac. Run from the repository root:
#   ARM=A tools/eval_quick.sh     # base model, core card as the system prompt (PLAN.md 7, arm A)
#   ARM=A0 tools/eval_quick.sh    # base model, the one-line prompt the training used
#   ARM=C tools/eval_quick.sh     # base model + the newest run's adapter, the one-line prompt (arm C)
# Optional environment: ADAPTER (an adapter folder; default the newest ~/ail-train-work/runs/train-*/adapter*),
# SAMPLES (default 3), LIMIT (first N items, for a smoke test). Reads AIL_ROOT and BASE_MODEL from config.local.
# Output: ~/ail-train-work/runs/eval-ARM-STAMP/{answers.jsonl,summary.json}. Not while a training run or gate runs.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
work="$HOME/ail-train-work"
die() { echo "eval_quick: $*" >&2; exit 2; }
[ -f "$root/config.local" ] && . "$root/config.local"
[ -n "${BASE_MODEL:-}" ] || die "config.local sets no BASE_MODEL"
ail_root="${AIL_ROOT:-$work/ail-pinned}"
arm="${ARM:-}"
case "$arm" in A) system=core ;; A0|C) system=short ;; *) die "set ARM=A, A0 or C" ;; esac
if pgrep -f "mlx_lm.lora" >/dev/null 2>&1; then die "a training run is going; wait for it"; fi
if pgrep -f "mac-gate.sh" >/dev/null 2>&1; then die "the AIL Mac gate is running"; fi
[ -s "$root/data/build/quick-eval.jsonl" ] || die "no data/build/quick-eval.jsonl; run tools/build_data.sh"
vpy="$work/venv/bin/python"
export HF_HOME="$work/hf" HF_HUB_DISABLE_TELEMETRY=1
mdir="$("$vpy" -c 'import sys; from huggingface_hub import snapshot_download; print(snapshot_download(sys.argv[1]))' "$BASE_MODEL" 2>/dev/null | tail -1)"
[ -d "$mdir" ] || die "could not find $BASE_MODEL"
adapter_args=""
if [ "$arm" = "C" ]; then
    adapter="${ADAPTER:-$(ls -d "$work"/runs/train-*/adapter* 2>/dev/null | sort | tail -1)}"
    [ -f "$adapter/adapters.safetensors" ] || die "no adapter at ${adapter:-?}"
    adapter_args="--adapter $adapter"
fi
out="$work/runs/eval-$arm-$(date -u +%Y%m%dT%H%M%SZ)"
# shellcheck disable=SC2086
caffeinate -i "$vpy" "$root/tools/eval_quick.py" --ail "$ail_root" --model "$mdir" $adapter_args --system "$system" \
    --out "$out" --samples "${SAMPLES:-3}" ${LIMIT:+--limit $LIMIT}
echo "results: $out"
