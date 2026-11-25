import re
import sys

lines = [l for l in sys.stdin.read().split("\n") if l != ""]
if not lines:
    print("empty")
    sys.exit(0)

header = lines[0].split(",")
totals = [0] * len(header)
numeric = [True] * len(header)
skipped = 0
for line in lines[1:]:
    cells = line.split(",")
    if len(cells) != len(header):
        skipped += 1
        continue
    for i, cell in enumerate(cells):
        if not numeric[i]:
            continue
        if re.fullmatch(r"-?[0-9]+", cell):
            totals[i] += int(cell)
        else:
            numeric[i] = False

for i, name in enumerate(header):
    print(f"{name}: {totals[i]}" if numeric[i] else f"{name}: -")
if skipped:
    print(f"skipped: {skipped}")
