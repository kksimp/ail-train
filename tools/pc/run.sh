#!/usr/bin/env bash
# ail-train on the PC, inside WSL2 Ubuntu. Started by tools/pc/run.ps1 (Windows); can also be run directly in WSL from
# ~/ail-train-work/ail-train:   bash tools/pc/run.sh TASK [small|big] [EXTRA]
#
# Tasks: setup | preflight | build | train small|big | eval small|big [base] | evalloop small|big | export small|big
# config.local (untracked, D6) at the repository root sets the models; no model name is written in a committed file:
#   BASE_MODEL="org/name"   # the autocomplete model, original bf16 weights (not an MLX build)
#   BIG_MODEL="org/name"    # the whole-program model, original weights (loaded at 4 bits for training)
# Optional environment, train: EPOCHS, MAX_STEPS, LR, RANK, ALPHA, LAYERS (0 = all), TARGETS (all | attn | a,b,c),
#   SEQ, BATCH, ACCUM, EVAL_EVERY (optimizer steps), RESUME=1 (continue the newest run of that model), ENGINE
#   (unsloth | hf). build: MAX_TOKENS (default 4096), JOBS. eval: SAMPLES, MAX_GEN, LIMIT, RUN (a run folder);
#   evalloop also ROUNDS (default 3) and FAMILIES (a,b). eval and evalloop: DATA (a .jsonl in the quick-eval
#   format, default data/build/quick-eval.jsonl, e.g. data/build/dev-spec.jsonl) and OUT (the results folder);
#   RESUME_EVAL=1 (with OUT: keep the finished items of OUT/answers.jsonl or revisions.jsonl and continue).
#   eval and export: ADAPTER=best (default: adapter-best, the lowest-validation checkpoint) or ADAPTER=final.
# Work folder: ~/ail-train-work/{venv,hf,ail-pinned,runs,export}. Runs: runs/train-small-STAMP/{summary.txt,log.jsonl,
#   adapter-final/,checkpoint-*/}. Keeps 20 GB of disk free and stops on NaN loss or validation rising twice.
set -u
root="$(cd "$(dirname "$0")/../.." && pwd)"
work="$HOME/ail-train-work"
task="${1:-}"; which="${2:-}"; extra="${3:-}"
die() { echo "run.sh: $*" >&2; exit 2; }
[ "$(uname -s)" = "Linux" ] || die "runs inside WSL2 (or Linux) only"
[ -f "$root/config.local" ] && . "$root/config.local"
venv="$work/venv"
vpy="$venv/bin/python"
export HF_HOME="$work/hf" HF_HUB_DISABLE_TELEMETRY=1 TOKENIZERS_PARALLELISM=false PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
ail_root="${AIL_ROOT:-$work/ail-pinned}"
pin="$(cat "$root/.ail-version")"

free_gb() { df -k "$work" | awk 'NR==2 {printf "%d", $4 / 1048576}'; }

model_for() {
    case "$1" in
        small) [ -n "${BASE_MODEL:-}" ] || die "config.local sets no BASE_MODEL"; echo "$BASE_MODEL" ;;
        big) [ -n "${BIG_MODEL:-}" ] || die "config.local sets no BIG_MODEL"; echo "$BIG_MODEL" ;;
        *) die "say small or big" ;;
    esac
}

# Downloads a model once and refuses any licence other than Apache-2.0 or MIT (AGPL-3.0 compatible; PLAN.md 4).
fetch() {
    "$vpy" - "$1" <<'PY'
import sys
from huggingface_hub import model_info, snapshot_download
name = sys.argv[1]
lic = ""
try:
    info = model_info(name)
    lic = ((info.card_data or {}).get("license") or "").lower()
    lic = lic or next((t[8:] for t in info.tags if t.startswith("license:")), "")
except Exception as e:
    print("could not read the licence of " + name + ": " + str(e), file=sys.stderr)
if lic not in ("apache-2.0", "mit"):
    sys.exit("licence '" + lic + "' is not Apache-2.0 or MIT: not used (AGPL-3.0 compatibility)")
print(snapshot_download(name, allow_patterns=["*.json", "*.safetensors", "*.txt", "*.model", "*.jinja", "*.py", "LICENSE*"]))
PY
}

setup() {
    command -v nvidia-smi >/dev/null || die "no GPU in WSL: update the Windows NVIDIA driver (WSL uses it, no Linux driver)"
    nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
    mkdir -p "$work"
    if [ ! -x "$vpy" ]; then
        python3 -m venv "$venv" || die "python3-venv missing (run.ps1 setup installs it)"
    fi
    "$vpy" -m pip install -q --upgrade pip
    # Unsloth brings matching torch (CUDA), transformers, peft, trl, bitsandbytes and datasets.
    "$vpy" -m pip install -q --upgrade unsloth huggingface_hub || die "pip install failed"
    "$vpy" -c 'import torch; assert torch.cuda.is_available(), "torch sees no GPU"; print("torch", torch.__version__, "cuda", torch.version.cuda, torch.cuda.get_device_name(0), "bf16", torch.cuda.is_bf16_supported())' || die "CUDA check failed"
    "$vpy" -m pip freeze > "$work/pip-freeze.txt"
    if [ ! -d "$ail_root/.git" ]; then
        git clone -q https://github.com/kksimp/ail "$ail_root" || die "could not clone ail"
    fi
    git -C "$ail_root" fetch -q origin && git -C "$ail_root" checkout -q "$pin" || die "could not check out ail $pin"
    (cd "$ail_root" && ./ail doctor) || die "ail doctor failed"
    echo "setup done; free disk $(free_gb) GB"
}

# The adapter of a run that eval and export use: ADAPTER=best (default) is adapter-best, or for runs from before it
# existed the best checkpoint named in result.json; ADAPTER=final is adapter-final. Empty when there is none.
adapter_of() {
    local run="$1"
    if [ "${ADAPTER:-best}" = final ]; then
        [ -d "$run/adapter-final" ] && echo "$run/adapter-final"
        return 0
    fi
    if [ -d "$run/adapter-best" ]; then echo "$run/adapter-best"; return 0; fi
    local b=""
    [ -f "$run/result.json" ] && b="$("$vpy" -c 'import json, sys; print(json.load(open(sys.argv[1])).get("best_checkpoint") or "")' "$run/result.json")"
    if [ -n "$b" ] && [ -f "$b/adapter_config.json" ]; then echo "$b"; return 0; fi
    [ -d "$run/adapter-final" ] && echo "$run/adapter-final"
    return 0
}

guard() {
    [ -x "$vpy" ] || die "run setup first"
    [ "$(free_gb)" -ge 20 ] || die "less than 20 GB free in WSL"
    if pgrep -f "tools/pc/train[.]py" >/dev/null; then die "a training run is going"; fi
}

case "$task" in
setup) setup ;;

preflight)
    guard
    [ -s "$root/data/build/train.jsonl" ] || die "no built data; run build first"
    out="$work/runs/preflight-$(date -u +%Y%m%dT%H%M%SZ)"; mkdir -p "$out"
    # Each line: label, model, extra train.py options. The smoke run takes the longest items, so the peak is the worst case.
    small="$(fetch "$(model_for small)")" || exit 2
    big=""; [ -n "${BIG_MODEL:-}" ] && { big="$(fetch "$BIG_MODEL")" || exit 2; }
    {
        echo "small-r16-s3072-b2|$small|--rank 16 --seq 3072 --batch 2"
        echo "small-r64-s3072-b2|$small|--rank 64 --seq 3072 --batch 2"
        echo "small-r64-s4096-b2|$small|--rank 64 --seq 4096 --batch 2"
        echo "small-r64-s4096-b4|$small|--rank 64 --seq 4096 --batch 4"
        echo "small-r128-s4096-b2|$small|--rank 128 --seq 4096 --batch 2"
        if [ -n "$big" ]; then
            echo "big-r16-s2048-b1|$big|--load-4bit --rank 16 --seq 2048 --batch 1"
            echo "big-r32-s3072-b1|$big|--load-4bit --rank 32 --seq 3072 --batch 1"
            echo "big-r32-s4096-b1|$big|--load-4bit --rank 32 --seq 4096 --batch 1"
        fi
    } | while IFS='|' read -r label mdir opts; do
        echo "== $label"
        # shellcheck disable=SC2086
        "$vpy" "$root/tools/pc/train.py" --model "$mdir" --data "$root/data/build" --out "$out/$label" --smoke 12 \
            --accum 1 $opts > "$out/$label.log" 2>&1
        tail -3 "$out/$label.log"
    done
    "$vpy" - "$out" <<'PY'
import json, os, sys
out = sys.argv[1]
rows = ["| run | peak VRAM GB | tok/s | ok |", "|---|---|---|---|"]
for d in sorted(os.listdir(out)):
    p = os.path.join(out, d, "smoke.json")
    if os.path.isfile(p):
        s = json.load(open(p))
        rows.append("| {} | {:.2f} | {:.0f} | {} |".format(d, s["peak_gb"], s["tok_per_s"], "yes" if s["peak_gb"] < 7.6 else "too close"))
    elif d.endswith(".log"):
        tail = open(os.path.join(out, d), errors="replace").read()[-300:].replace("\n", " ")
        if not os.path.isdir(os.path.join(out, d[:-4])) or not os.path.isfile(os.path.join(out, d[:-4], "smoke.json")):
            rows.append("| {} | - | - | failed: {} |".format(d[:-4], "out of memory" if "out of memory" in tail.lower() else tail[-120:]))
open(os.path.join(out, "SUMMARY.md"), "w").write("\n".join(rows) + "\n")
print("\n".join(rows))
PY
    echo "results: $out/SUMMARY.md"
    ;;

build)
    guard
    [ -x "$ail_root/ail" ] || die "no ail at $ail_root; run setup"
    tok="$(fetch "$(model_for small)")" || exit 2
    args="--ail $ail_root --system ${SYSTEM:-short} --max-tokens ${MAX_TOKENS:-4096} --jobs ${JOBS:-6} --tokenizer $tok"
    # Build twice into staging folders; data/build is replaced only when both builds match and the held-out splits
    # (quick-eval, valid) are byte-identical to data/splits.sha256. The previous data/build is kept in build-prev.
    rm -rf "$work/build-new" "$work/build-again"
    # shellcheck disable=SC2086
    "$vpy" "$root/tools/build_data.py" $args --out "$work/build-new" || die "build failed"
    (cd "$work/build-new" && sed 's#  build/#  #' "$root/data/splits.sha256" | sha256sum --quiet -c -) \
        || die "quick-eval.jsonl or valid.jsonl differs from data/splits.sha256: the held-out splits must not change"
    # shellcheck disable=SC2086
    "$vpy" "$root/tools/build_data.py" $args --out "$work/build-again" >/dev/null || die "second build failed"
    for f in train.jsonl valid.jsonl quick-eval.jsonl dev-spec.jsonl manifest.json; do
        cmp -s "$work/build-new/$f" "$work/build-again/$f" || die "the rebuild differs in $f: the builder is not deterministic"
    done
    if [ -s "$root/data/build/train.jsonl" ]; then
        rm -rf "$work/build-prev" && cp -a "$root/data/build" "$work/build-prev"
    fi
    mkdir -p "$root/data/build" && cp "$work/build-new"/* "$root/data/build/" && rm -rf "$work/build-again"
    echo "deterministic: both builds match; held-out splits unchanged; built: $root/data/build (previous: $work/build-prev)"
    ;;

train)
    guard
    [ -s "$root/data/build/train.jsonl" ] || die "no built data; run build first"
    mdir="$(fetch "$(model_for "$which")")" || exit 2
    if [ "$which" = small ]; then
        # Heavy LoRA on every linear layer of every block, bf16 base (no quantisation: it deploys re-quantised).
        defaults="--rank ${RANK:-64} --seq ${SEQ:-4096} --batch ${BATCH:-2} --accum ${ACCUM:-8} --lr ${LR:-1e-4} --epochs ${EPOCHS:-3}"
    else
        # QLoRA: the base at 4 bits (NF4), the adapter in bf16.
        defaults="--load-4bit --rank ${RANK:-32} --seq ${SEQ:-3072} --batch ${BATCH:-1} --accum ${ACCUM:-16} --lr ${LR:-1e-4} --epochs ${EPOCHS:-2}"
    fi
    opts="$defaults --eval-every ${EVAL_EVERY:-200} --layers ${LAYERS:-0} --targets ${TARGETS:-all} --engine ${ENGINE:-unsloth}"
    [ -n "${ALPHA:-}" ] && opts="$opts --alpha $ALPHA"
    [ -n "${MAX_STEPS:-}" ] && opts="$opts --max-steps $MAX_STEPS"
    if [ -n "${RESUME:-}" ]; then
        run="$(ls -d "$work"/runs/train-"$which"-* 2>/dev/null | sort | tail -1)"
        [ -n "$run" ] || die "no run to resume"
        opts="$opts --resume"
    else
        run="$work/runs/train-$which-$(date -u +%Y%m%dT%H%M%SZ)"
    fi
    mkdir -p "$run"
    {
        echo "model: $which ($(model_for "$which"))"
        echo "data: $(cd "$root" && git rev-parse --short HEAD), $(wc -l < "$root/data/build/train.jsonl") train items, manifest sha256 $(sha256sum < "$root/data/build/manifest.json" | cut -c1-12)"
        echo "options: $opts"
        echo "started: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    } >> "$run/summary.txt"
    cat "$run/summary.txt"
    # shellcheck disable=SC2086
    "$vpy" "$root/tools/pc/train.py" --model "$mdir" --data "$root/data/build" --out "$run" $opts 2>&1 | tee -a "$run/train.log"
    echo "ended: $(date -u +%Y-%m-%dT%H:%M:%SZ) (exit ${PIPESTATUS[0]})" >> "$run/summary.txt"
    cat "$run/summary.txt"
    echo "run folder: $run"
    ;;

eval)
    guard
    data="${DATA:-$root/data/build/quick-eval.jsonl}"
    [ -s "$data" ] || die "no $data; run build first"
    mdir="$(fetch "$(model_for "$which")")" || exit 2
    adapter_args=""; arm="A0"
    if [ "$extra" != base ]; then
        run="${RUN:-$(ls -d "$work"/runs/train-"$which"-* 2>/dev/null | sort | tail -1)}"
        adapter="$(adapter_of "$run")"
        [ -n "$adapter" ] || die "no finished adapter in ${run:-?}"
        echo "adapter: $adapter"
        adapter_args="--adapter $adapter"; arm="C-${ADAPTER:-best}"
    fi
    q=""; [ "$which" = big ] && q="--load-4bit"
    tag=""; [ -n "${DATA:-}" ] && tag="-$(basename "$data" .jsonl)"
    out="${OUT:-$work/runs/eval-$which-$arm$tag-$(date -u +%Y%m%dT%H%M%SZ)}"
    # No expandable_segments for eval: generating on the longest prompt with the big model and its adapter needs a
    # little over 8 GB, and growing a segment then fails in WSL ("CUDA driver error: device not ready ... Failed to
    # create GPU mapping"); the classic allocator lets the driver spill the overflow to shared memory instead.
    # shellcheck disable=SC2086
    env -u PYTORCH_CUDA_ALLOC_CONF "$vpy" "$root/tools/eval_quick.py" --backend hf --ail "$ail_root" --model "$mdir" $adapter_args $q --system short \
        --data "$data" --out "$out" --samples "${SAMPLES:-3}" --max-tokens "${MAX_GEN:-1536}" ${LIMIT:+--limit $LIMIT} \
        ${RESUME_EVAL:+--resume}
    echo "results: $out"
    ;;

evalloop)
    # Arm B: eval as above plus up to ROUNDS (default 3) `ail check` correction rounds per sample (tools/eval_loop.py).
    guard
    data="${DATA:-$root/data/build/quick-eval.jsonl}"
    [ -s "$data" ] || die "no $data; run build first"
    mdir="$(fetch "$(model_for "$which")")" || exit 2
    run="${RUN:-$(ls -d "$work"/runs/train-"$which"-* 2>/dev/null | sort | tail -1)}"
    adapter="$(adapter_of "$run")"
    [ -n "$adapter" ] || die "no finished adapter in ${run:-?}"
    echo "adapter: $adapter"
    q=""; [ "$which" = big ] && q="--load-4bit"
    tag=""; [ -n "${DATA:-}" ] && tag="-$(basename "$data" .jsonl)"
    out="${OUT:-$work/runs/evalloop-$which-${ADAPTER:-best}$tag-$(date -u +%Y%m%dT%H%M%SZ)}"
    # shellcheck disable=SC2086
    env -u PYTORCH_CUDA_ALLOC_CONF "$vpy" "$root/tools/eval_loop.py" --ail "$ail_root" --model "$mdir" --adapter "$adapter" $q \
        --data "$data" --out "$out" --rounds "${ROUNDS:-3}" --samples "${SAMPLES:-3}" --max-tokens "${MAX_GEN:-1536}" \
        ${LIMIT:+--limit $LIMIT} ${FAMILIES:+--families $FAMILIES} ${RESUME_EVAL:+--resume}
    echo "results: $out"
    ;;

export)
    guard
    mdir="$(fetch "$(model_for "$which")")" || exit 2
    run="${RUN:-$(ls -d "$work"/runs/train-"$which"-* 2>/dev/null | sort | tail -1)}"
    adapter="$(adapter_of "$run")"
    [ -n "$adapter" ] || die "no finished adapter in ${run:-?}"
    echo "adapter: $adapter"
    out="$work/export/$which-$(basename "$run")-${ADAPTER:-best}"
    "$vpy" "$root/tools/pc/export.py" --model "$mdir" --adapter "$adapter" --out "$out/merged" || die "merge failed"
    # GGUF through llama.cpp (MIT), built once in ~/ail-train-work/llama.cpp.
    lc="$work/llama.cpp"
    if [ ! -x "$lc/build/bin/llama-quantize" ]; then
        [ -d "$lc/.git" ] || git clone -q --depth 1 https://github.com/ggml-org/llama.cpp "$lc" || die "could not clone llama.cpp"
        "$vpy" -m pip install -q gguf sentencepiece protobuf || die "gguf tools"
        cmake -S "$lc" -B "$lc/build" -DGGML_CUDA=OFF -DLLAMA_CURL=OFF >/dev/null && cmake --build "$lc/build" -j --target llama-quantize >/dev/null || die "llama.cpp build failed"
    fi
    "$vpy" "$lc/convert_hf_to_gguf.py" "$out/merged" --outtype bf16 --outfile "$out/model-bf16.gguf" >/dev/null || die "GGUF convert failed"
    for q in Q8_0 Q4_K_M; do "$lc/build/bin/llama-quantize" "$out/model-bf16.gguf" "$out/model-$q.gguf" "$q" >/dev/null || die "quantize $q failed"; done
    rm -f "$out/model-bf16.gguf"
    ls -lh "$out" "$out/merged"
    echo "export: $out (merged/ for MLX on the Mac: tools/import_mlx.sh; model-*.gguf for llama.cpp)"
    ;;

*) sed -n 2,14p "$0"; exit 2 ;;
esac
