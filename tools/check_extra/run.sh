#!/usr/bin/env bash
# Checks every program under data/extra/ with the AIL compiler: `ail check`, `ail run` against NAME.out, `ail test`.
# Run on the Mac from the repository root:   tools/check_extra/run.sh [PATH_TO_AIL_CHECKOUT]
# Writes data/extra/RESULTS.txt (one line per program, then the output of each failure). Exit 1 if any fails.
# One program at a time unless JOBS is set. bash 3.2 compatible.
set -u
export AIL_FIX=0   # never let the checker rewrite training data silently
root="$(cd "$(dirname "$0")/../.." && pwd)"
ail_root="${1:-${AIL_ROOT:-$HOME/Documents/Projects/ail}}"
ail="$ail_root/ail"
if [ ! -x "$ail" ]; then
    echo "no ail at $ail; pass the path of an ail checkout" >&2
    exit 2
fi
want="$(cat "$root/.ail-version" 2>/dev/null || true)"
have="$(cd "$ail_root" && git rev-parse HEAD 2>/dev/null || true)"
if [ -n "$want" ] && [ "$want" != "$have" ]; then
    echo "the ail checkout is at ${have:-unknown}, but .ail-version pins $want; check out that commit first" >&2
    exit 2
fi
work="$HOME/ail-train-work/check_extra"
mkdir -p "$work"
# JOBS=N checks N programs at once (default 1). ONLY="batch09 batch10" checks just those directories and writes
# $work/RESULTS-partial.txt instead of data/extra/RESULTS.txt.
jobs="${JOBS:-1}"
only="${ONLY:-}"
out="$root/data/extra/RESULTS.txt"
if [ -n "$only" ]; then out="$work/RESULTS-partial.txt"; fi
res="$work/res"
rm -rf "$res"
mkdir -p "$res"
list="$work/list.txt"
: > "$list"
for dir in "$root"/data/extra/*/*/; do
    group="$(basename "$(dirname "$dir")")"
    if [ -n "$only" ]; then
        case " $only " in *" $group "*) ;; *) continue ;; esac
    fi
    name="$(basename "$dir")"
    [ -f "$dir$name.ail" ] || continue
    echo "${dir%/}" >> "$list"
done
tr '\n' '\0' < "$list" | xargs -0 -n 1 -P "$jobs" "$root/tools/check_extra/check_one.sh" "$ail" "$res"
pass=0
fail=0
detail="$work/detail.txt"
: > "$detail"
{
    echo "ail commit: $(cd "$ail_root" && git rev-parse --short HEAD 2>/dev/null || echo unknown)"
    echo "checked: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$out"
while IFS= read -r dir; do
    name="$(basename "$dir")"
    status="$(cat "$res/$name.status" 2>/dev/null || echo missing)"
    if [ "$status" = "pass" ]; then
        pass=$((pass + 1))
        echo "pass $name" >> "$out"
    else
        fail=$((fail + 1))
        echo "FAIL $name ($status)" >> "$out"
        cat "$res/$name.detail" >> "$detail" 2>/dev/null
    fi
done < "$list"
{
    echo "total: $pass pass, $fail fail"
    echo
    cat "$detail"
} >> "$out"
echo "$pass pass, $fail fail; see $out"
[ "$fail" -eq 0 ]
