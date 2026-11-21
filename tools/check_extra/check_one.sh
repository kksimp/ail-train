#!/usr/bin/env bash
# Checks one program directory for run.sh: check_one.sh AIL RESDIR DIR. Writes RESDIR/NAME.status ("pass" or the failed
# step) and RESDIR/NAME.detail (the failure output). bash 3.2 compatible.
set -u
export AIL_FIX=0
ail="$1"
res="$2"
dir="$3"
name="$(basename "$dir")"
src="$dir/$name.ail"
tmp="$res/$name.tmp"
mkdir -p "$tmp"
why=""
detail="$res/$name.detail"
: > "$detail"
if ! "$ail" check --no-fix "$src" > "$tmp/check.txt" 2>&1; then
    why="check"
    { echo "== $name: ail check"; cat "$tmp/check.txt"; } >> "$detail"
elif ! "$ail" run "$src" > "$tmp/run.txt" 2> "$tmp/run.err"; then
    why="run"
    { echo "== $name: ail run"; cat "$tmp/run.txt" "$tmp/run.err"; } >> "$detail"
elif ! diff "$dir/$name.out" "$tmp/run.txt" > "$tmp/diff.txt" 2>&1; then
    why="output"
    { echo "== $name: output differs (< expected, > got)"; cat "$tmp/diff.txt"; } >> "$detail"
elif ! "$ail" test "$src" > "$tmp/test.txt" 2>&1; then
    why="test"
    { echo "== $name: ail test"; cat "$tmp/test.txt"; } >> "$detail"
fi
rm -rf "$tmp"
if [ -z "$why" ]; then echo pass > "$res/$name.status"; else echo "$why" > "$res/$name.status"; fi
