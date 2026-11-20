#!/usr/bin/env bash
# Checks every program under data/extra/ with the AIL compiler: `ail check`, `ail run` against NAME.out, `ail test`.
# Run on the Mac from the repository root:   tools/check_extra/run.sh [PATH_TO_AIL_CHECKOUT]
# Writes data/extra/RESULTS.txt (one line per program, then the output of each failure). Exit 1 if any fails.
# Light work: one small program at a time. bash 3.2 compatible.
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
out="$root/data/extra/RESULTS.txt"
detail="$work/detail.txt"
: > "$detail"
pass=0
fail=0
{
    echo "ail commit: $(cd "$ail_root" && git rev-parse --short HEAD 2>/dev/null || echo unknown)"
    echo "checked: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$out"
for dir in "$root"/data/extra/*/*/; do
    name="$(basename "$dir")"
    src="$dir$name.ail"
    [ -f "$src" ] || continue
    why=""
    if ! "$ail" check --no-fix "$src" > "$work/check.txt" 2>&1; then
        why="check"
        { echo "== $name: ail check"; cat "$work/check.txt"; } >> "$detail"
    elif ! "$ail" run "$src" > "$work/run.txt" 2> "$work/run.err"; then
        why="run"
        { echo "== $name: ail run"; cat "$work/run.txt" "$work/run.err"; } >> "$detail"
    elif ! diff "$dir$name.out" "$work/run.txt" > "$work/diff.txt" 2>&1; then
        why="output"
        { echo "== $name: output differs (< expected, > got)"; cat "$work/diff.txt"; } >> "$detail"
    elif ! "$ail" test "$src" > "$work/test.txt" 2>&1; then
        why="test"
        { echo "== $name: ail test"; cat "$work/test.txt"; } >> "$detail"
    fi
    if [ -z "$why" ]; then
        pass=$((pass + 1))
        echo "pass $name" >> "$out"
    else
        fail=$((fail + 1))
        echo "FAIL $name ($why)" >> "$out"
    fi
done
{
    echo "total: $pass pass, $fail fail"
    echo
    cat "$detail"
} >> "$out"
echo "$pass pass, $fail fail; see data/extra/RESULTS.txt"
[ "$fail" -eq 0 ]
