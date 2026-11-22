#!/usr/bin/env bash
# Bring a model trained on the PC back to the Mac as a 4-bit MLX model. Run from the repository root:
#   tools/import_mlx.sh FOLDER     # FOLDER: the merged/ folder from `tools\pc\run.ps1 export small` (copied over)
# Writes ~/ail-train-work/mlx/NAME-4bit (NAME = the export folder's name). Then the quick eval of that model:
#   MODEL_DIR=~/ail-train-work/mlx/NAME-4bit ARM=M tools/eval_quick.sh
# Uses the preflight venv (mlx-lm). Not while a training run or the AIL Mac gate runs. bash 3.2 compatible.
set -u
work="$HOME/ail-train-work"
die() { echo "import_mlx: $*" >&2; exit 2; }
[ "$(uname -s)" = "Darwin" ] || die "runs on the Mac"
src="${1:-}"
[ -f "$src/config.json" ] || die "no merged model at '${src}' (needs config.json and *.safetensors)"
[ -x "$work/venv/bin/mlx_lm.convert" ] || die "no venv; run tools/preflight.sh or tools/build_data.sh first"
if pgrep -f "mac-gate[.]sh" >/dev/null 2>&1; then die "the AIL Mac gate is running"; fi
[ "$(df -k "$HOME" | awk 'NR==2 {printf "%d", $4 / 1048576}')" -ge 20 ] || die "less than 20 GB free"
name="$(basename "$(cd "$src/.." && pwd)")"
out="$work/mlx/$name-4bit"
[ -e "$out" ] && die "$out exists already"
mkdir -p "$work/mlx"
"$work/venv/bin/mlx_lm.convert" --hf-path "$src" --mlx-path "$out" -q --q-bits 4 --q-group-size 64 || die "convert failed"
du -sh "$out"
echo "MLX model: $out"
