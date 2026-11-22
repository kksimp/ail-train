#!/usr/bin/env bash
# M5: the first LoRA training run on the Mac. Run from the repository root after tools/build_data.sh:
#   tools/train.sh                 # a new run
#   RESUME=~/ail-train-work/runs/train-STAMP tools/train.sh    # continue a stopped run from its last checkpoint
# Reads BASE_MODEL from the untracked config.local (D6). Optional environment: EPOCHS (default 1; run 1 overfit in its second epoch), NUM_LAYERS
# (default 16), SEQ (default 2048), LR (default 1e-4), ACCUM (gradient accumulation, default 8), EVAL_EVERY (default
# 400 optimizer steps), SWAP_ABORT_MB (default 2048).
# Writes ~/ail-train-work/runs/train-STAMP/{adapter.yaml,lora.log,adapter/,val.txt,summary.txt}. Keeps the Mac awake
# with caffeinate. Stops on a swap blow-up or when validation loss rises at two evaluations in a row (PLAN.md 6); the
# adapter checkpoints stay, so a stopped run can be resumed or the best checkpoint used. bash 3.2 compatible.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
work="$HOME/ail-train-work"
die() { echo "train: $*" >&2; exit 2; }
[ "$(uname -s)" = "Darwin" ] && [ "$(uname -m)" = "arm64" ] || die "runs only on the Apple Silicon Mac"
[ -f "$root/config.local" ] || die "no config.local (set BASE_MODEL there)"
. "$root/config.local"
[ -n "${BASE_MODEL:-}" ] || die "config.local sets no BASE_MODEL"
data="$root/data/build"
[ -s "$data/train.jsonl" ] && [ -s "$data/valid.jsonl" ] || die "no built data; run tools/build_data.sh first"
vpy="$work/venv/bin/python"
[ -x "$vpy" ] || die "no venv; run tools/preflight.sh or tools/build_data.sh first"
if pgrep -f "mac-gate.sh" >/dev/null 2>&1; then die "the AIL Mac gate is running"; fi
l="$(sysctl -n vm.loadavg | awk '{print $2}')"
awk -v l="$l" 'BEGIN { exit !(l < 8) }' || die "load average is $l (needs < 8)"
[ "$(df -k "$HOME" | awk 'NR==2 {printf "%d", $4 / 1048576}')" -ge 20 ] || die "less than 20 GB free"
export HF_HOME="$work/hf"
export HF_HUB_DISABLE_TELEMETRY=1
mdir="$("$vpy" -c 'import sys; from huggingface_hub import snapshot_download; print(snapshot_download(sys.argv[1]))' "$BASE_MODEL" 2>/dev/null | tail -1)"
[ -d "$mdir" ] || die "could not find or fetch $BASE_MODEL"

epochs="${EPOCHS:-1}"; layers="${NUM_LAYERS:-16}"; seq="${SEQ:-2048}"; lr="${LR:-1e-4}"; accum="${ACCUM:-8}"
eval_every="${EVAL_EVERY:-400}"; swap_abort="${SWAP_ABORT_MB:-2048}"
items="$(wc -l < "$data/train.jsonl" | tr -d ' ')"
# mlx-lm counts one iteration per batch (batch 1); with accumulation the optimizer steps every ACCUM iterations.
iters=$((epochs * items))
# The learning-rate schedule advances once per optimizer update (every ACCUM iterations), not per iteration.
warmup=$((iters / accum / 50))
adapter="adapter"
if [ -n "${RESUME:-}" ]; then
    run="$RESUME"
    [ -f "$run/adapter.yaml" ] || die "no run at $run"
    # mlx-lm loads only the weights on resume and numbers its checkpoints from 1 again, so each resume writes to its
    # own folder (adapter-r1, adapter-r2, ...) and the iterations already done are the sum over the folders.
    done_iters=0
    last=""
    n=0
    for a in "$run"/adapter "$run"/adapter-r*; do
        [ -d "$a" ] || continue
        f="$(ls "$a"/*_adapters.safetensors 2>/dev/null | sort | tail -1)"
        [ -n "$f" ] || continue
        done_iters=$((done_iters + $(basename "$f" | sed 's/^0*\([0-9]*\)_.*/\1/')))
        last="$f"
        n=$((n + 1))
    done
    [ -n "$last" ] || die "no checkpoint in $run"
    adapter="adapter-r$n"
    resume_line="resume_adapter_file: \"$last\""
    iters=$((iters - done_iters))
    warmup=0   # the optimizer and schedule restart; decay over what is left
    echo "resuming after $done_iters iterations from $last"
else
    run="$work/runs/train-$(date -u +%Y%m%dT%H%M%SZ)"
    mkdir -p "$run"
    resume_line=""
fi
cat > "$run/$adapter.yaml" <<YAML
model: "$mdir"
train: true
fine_tune_type: lora
data: "$data"
seed: 0
num_layers: $layers
batch_size: 1
grad_accumulation_steps: $accum
iters: $iters
val_batches: 100
learning_rate: $lr
lr_schedule:
  name: cosine_decay
  warmup: $warmup
  warmup_init: 1.0e-7
  arguments: [$lr, $((iters / accum - warmup)), 1.0e-6]
steps_per_report: 50
steps_per_eval: $((eval_every * accum))
save_every: $((eval_every * accum))
adapter_path: "$run/$adapter"
max_seq_length: $seq
grad_checkpoint: true
mask_prompt: true
lora_parameters:
  rank: 16
  dropout: 0.05
  scale: 20.0
$resume_line
YAML
{
    echo "base: $BASE_MODEL"
    echo "data: $(cd "$root" && git rev-parse --short HEAD), $items train items; manifest sha256 $(shasum -a 256 < "$data/manifest.json" | cut -c1-12)"
    echo "epochs $epochs, iters $iters, layers $layers, seq $seq, lr $lr, accum $accum, eval every $((eval_every * accum)) iters"
    echo "started: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} >> "$run/summary.txt"
cat "$run/summary.txt"

"$work/venv/bin/mlx_lm.lora" -c "$run/$adapter.yaml" >> "$run/lora.log" 2>&1 &
pid=$!
caffeinate -i -s -w "$pid" &
swap_mb() { sysctl -n vm.swapusage | sed -n 's/.*used = \([0-9.]*\)M.*/\1/p' | awk '{printf "%d", $1}'; }
swap0="$(swap_mb)"
why=""
while kill -0 "$pid" 2>/dev/null; do
    sleep 30
    s="$(swap_mb)"
    if [ $((s - swap0)) -gt "$swap_abort" ]; then why="swap grew by $((s - swap0)) MB"; break; fi
    if pgrep -f "mac-gate.sh" >/dev/null 2>&1; then why="the AIL Mac gate started"; break; fi
    # Validation rows look like "  400    val 0.554    11.36s" (colour codes stripped).
    sed 's/\x1b\[[0-9;]*m//g' "$run/lora.log" | awk '$2 == "val" {print $1, $3}' > "$run/val.txt"
    if [ "$(wc -l < "$run/val.txt")" -ge 3 ] && tail -3 "$run/val.txt" | awk 'NR==1{a=$2} NR==2{b=$2} NR==3{c=$2} END{exit !(b > a && c > b)}'; then
        why="validation loss rose at two evaluations in a row"; break
    fi
done
if [ -n "$why" ]; then
    kill "$pid" 2>/dev/null; sleep 5; kill -9 "$pid" 2>/dev/null
fi
wait "$pid" 2>/dev/null
rc=$?
sed 's/\x1b\[[0-9;]*m//g' "$run/lora.log" | awk '$2 == "val" {print $1, $3}' > "$run/val.txt"
best="$(sort -k2 -n "$run/val.txt" | head -1)"   # iterations count from 1 again in each resumed part
{
    echo "ended: $(date -u +%Y-%m-%dT%H:%M:%SZ); ${why:-finished (exit $rc)}"
    echo "best validation (iter loss): ${best:-none}"
    echo "checkpoints: $(ls "$run"/adapter*/*_adapters.safetensors 2>/dev/null | wc -l | tr -d ' ')"
} >> "$run/summary.txt"
cat "$run/summary.txt"
echo "run folder: $run"
