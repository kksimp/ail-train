#!/usr/bin/env bash
# M1 preflight (PLAN.md section 9): measure each candidate base on this Mac before choosing one.
# Run from the repository root:   tools/preflight.sh
#
# Self-setting-up: makes ~/ail-train-work/venv, installs mlx-lm, downloads each candidate at 4 bits into
# ~/ail-train-work/hf, then per candidate: token counts on the corpus with the core card, a short LoRA smoke run at
# the D9 sequence length (peak memory, tokens per second), and an inference speed check.
# Results: ~/ail-train-work/runs/preflight-STAMP/SUMMARY.md (names the models, so it stays out of git, D6).
#
# Candidates come from the untracked config.local at the repository root (D6), for example:
#   PREFLIGHT_MODELS="org/first-model-4bit org/second-model-4bit org/third-model-4bit"
#   AIL_ROOT="$HOME/ail-train-work/ail-pinned"      # an ail checkout at .ail-version (for the core card and corpus)
# Optional environment: ITERS (default 20), SEQ (default 4096), NUM_LAYERS (LoRA layers, default 16),
# SYSTEM_FILE (system prompt for the smoke data instead of the core card, e.g. tools/preflight/short-system.txt),
# SWAP_ABORT_MB (default 1536), ONLY_CANDIDATE=N (or a list, "1 3").
# 512 MB of swap growth was too tight: macOS pages idle apps out as soon as a 4096-token run loads, before step 1.
#
# Limits (PLAN.md section 3): starts only while load < 8, no Mac gate running and at least 20 GB free disk; one
# candidate at a time; a run is stopped if swap use grows by more than SWAP_ABORT_MB, and marked over the cap if MLX
# peak memory passes 6 GB. bash 3.2 compatible.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
work="$HOME/ail-train-work"
iters="${ITERS:-20}"
seq="${SEQ:-4096}"
swap_abort="${SWAP_ABORT_MB:-1536}"
layers="${NUM_LAYERS:-16}"
only="${ONLY_CANDIDATE:-}"

die() { echo "preflight: $*" >&2; exit 2; }

[ "$(uname -s)" = "Darwin" ] && [ "$(uname -m)" = "arm64" ] || die "runs only on the Apple Silicon Mac"
[ -f "$root/config.local" ] || die "no config.local at $root (set PREFLIGHT_MODELS and AIL_ROOT there)"
# shellcheck disable=SC1091
. "$root/config.local"
[ -n "${PREFLIGHT_MODELS:-}" ] || die "config.local sets no PREFLIGHT_MODELS"
ail_root="${AIL_ROOT:-$work/ail-pinned}"
card="$ail_root/docs/language-card-core.md"
[ -f "$card" ] || die "no core card at $card (AIL_ROOT must be an ail checkout)"
[ -d "$ail_root/corpus" ] || die "no corpus under $ail_root"

load1() { sysctl -n vm.loadavg | awk '{print $2}'; }
swap_used_mb() { sysctl -n vm.swapusage | sed -n 's/.*used = \([0-9.]*\)M.*/\1/p' | awk '{printf "%d", $1}'; }
free_disk_gb() { df -k "$HOME" | awk 'NR==2 {printf "%d", $4 / 1048576}'; }

guard() {
    if pgrep -f "mac-gate[.]sh" >/dev/null 2>&1; then die "the AIL Mac gate is running; try again after it finishes"; fi
    local l
    l="$(load1)"
    awk -v l="$l" 'BEGIN { exit !(l < 8) }' || die "load average is $l (needs < 8)"
    [ "$(free_disk_gb)" -ge 20 ] || die "only $(free_disk_gb) GB free on the internal disk (needs 20)"
}
guard

# Python 3.10 or newer for mlx-lm.
py=""
for c in python3.13 python3.12 python3.11 python3.10 /opt/homebrew/bin/python3 python3; do
    if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(sys.version_info < (3, 10))' 2>/dev/null; then
        py="$(command -v "$c")"
        break
    fi
done
[ -n "$py" ] || die "needs Python 3.10 or newer (for example: brew install python)"

mkdir -p "$work"
venv="$work/venv"
if [ ! -x "$venv/bin/python" ]; then
    "$py" -m venv "$venv" || die "could not make $venv"
fi
"$venv/bin/python" -m pip install --quiet --upgrade pip >/dev/null 2>&1
"$venv/bin/python" -m pip install --quiet --upgrade mlx-lm huggingface_hub || die "pip install mlx-lm failed"
vpy="$venv/bin/python"
export HF_HOME="$work/hf"
export HF_HUB_DISABLE_TELEMETRY=1

stamp="$(date -u +%Y%m%dT%H%M%SZ)"
run="$work/runs/preflight-$stamp"
mkdir -p "$run"
{
    echo "date: $stamp"
    echo "machine: $(sysctl -n machdep.cpu.brand_string), $(($(sysctl -n hw.memsize) / 1073741824)) GB, macOS $(sw_vers -productVersion)"
    echo "free disk: $(free_disk_gb) GB; load: $(load1); swap used: $(swap_used_mb) MB"
    echo "mlx-lm $("$vpy" -c 'import importlib.metadata as m; print(m.version("mlx-lm"))'), mlx $("$vpy" -c 'import importlib.metadata as m; print(m.version("mlx"))'), python $("$vpy" -c 'import platform; print(platform.python_version())')"
    echo "ail: $(cd "$ail_root" && git rev-parse --short HEAD 2>/dev/null || echo unknown); ail-train: $(cd "$root" && git rev-parse --short HEAD)"
    echo "smoke run: $iters steps, sequence $seq, batch 1, LoRA rank 16 on $layers layers, grad checkpoint, prompt masked, system prompt ${SYSTEM_FILE:-core card}"
} > "$run/system.txt"
cat "$run/system.txt"

n=0
for model in $PREFLIGHT_MODELS; do
    n=$((n + 1))
    if [ -n "$only" ]; then case " $only " in *" $n "*) ;; *) continue ;; esac; fi
    d="$run/$n"
    mkdir -p "$d"
    echo "$model" > "$d/model.txt"
    echo "== candidate $n: $model"
    guard

    mdir="$("$vpy" -c 'import sys; from huggingface_hub import snapshot_download; print(snapshot_download(sys.argv[1]))' "$model" 2>"$d/download.log" | tail -1)"
    if [ -z "$mdir" ] || [ ! -d "$mdir" ]; then
        echo "download failed" > "$d/status.txt"
        echo "   download failed; see $d/download.log"
        continue
    fi
    du -skL "$mdir" | awk '{printf "%.1f\n", $1 / 1048576}' > "$d/disk_gb.txt"

    if ! "$vpy" "$root/tools/preflight/smoke_data.py" "$mdir" "${SYSTEM_FILE:-$card}" "$ail_root" "$root" "$d" "$seq" > "$d/tokens.log" 2>&1; then
        echo "token step failed" > "$d/status.txt"
        echo "   token step failed; see $d/tokens.log"
        continue
    fi

    cat > "$d/lora.yaml" <<EOF
model: "$mdir"
train: true
fine_tune_type: lora
data: "$d/data"
seed: 0
num_layers: $layers
batch_size: 1
iters: $iters
val_batches: 2
learning_rate: 1.0e-4
steps_per_report: 1
steps_per_eval: 1000
save_every: 100000
adapter_path: "$d/adapter"
max_seq_length: $seq
grad_checkpoint: true
mask_prompt: true
lora_parameters:
  rank: 16
  dropout: 0.0
  scale: 20.0
EOF
    swap0="$(swap_used_mb)"
    "$venv/bin/mlx_lm.lora" -c "$d/lora.yaml" > "$d/lora.log" 2>&1 &
    pid=$!
    maxswap="$swap0"
    aborted=""
    while kill -0 "$pid" 2>/dev/null; do
        s="$(swap_used_mb)"
        top -l 1 -pid "$pid" -stats mem 2>/dev/null | tail -1 >> "$d/footprint.txt"
        memory_pressure -Q 2>/dev/null | sed -n 's/.*percentage: \([0-9]*\)%.*/\1/p' >> "$d/free_pct.txt"
        [ "$s" -gt "$maxswap" ] && maxswap="$s"
        if [ $((s - swap0)) -gt "$swap_abort" ]; then
            aborted="swap grew by $((s - swap0)) MB"
            kill "$pid" 2>/dev/null
            sleep 2
            kill -9 "$pid" 2>/dev/null
            break
        fi
        sleep 3
    done
    wait "$pid" 2>/dev/null
    rc=$?
    echo $((maxswap - swap0)) > "$d/swap_delta_mb.txt"
    # MLX memory is unified, so the process footprint (top's MEM column) is the peak to hold under 6 GB.
    peak="$(awk '{ v = $1; sub(/[+-]$/, "", v); u = substr(v, length(v)); n = v + 0; if (u == "G") n *= 1024; else if (u == "K") n /= 1024;
        if (n > m) m = n } END { if (m) printf "%.2f", m / 1024 }' "$d/footprint.txt" 2>/dev/null)"
    echo "${peak:-}" > "$d/peak_gb.txt"
    if [ -n "$aborted" ]; then
        echo "stopped: $aborted" > "$d/status.txt"
    elif [ "$rc" -ne 0 ]; then
        echo "train failed (exit $rc)" > "$d/status.txt"
    elif [ -n "$peak" ] && awk -v p="$peak" 'BEGIN { exit !(p > 6.0) }'; then
        echo "over the 6 GB cap" > "$d/status.txt"
    else
        echo "ok" > "$d/status.txt"
    fi
    echo "   train: $(cat "$d/status.txt"), peak ${peak:-?} GB, swap +$(cat "$d/swap_delta_mb.txt") MB"
    rm -rf "$d/adapter"

    if [ -z "$aborted" ]; then
        sleep 20   # let memory settle before the inference check
        "$vpy" "$root/tools/preflight/gen_bench.py" "$mdir" "$card" "$d/gen.json" > "$d/gen.log" 2>&1 \
            || echo "   inference check failed; see $d/gen.log"
    fi
    sleep 30   # cool down between candidates
done

"$vpy" "$root/tools/preflight/summarize.py" "$run" > /dev/null
echo "preflight done: $run/SUMMARY.md"
