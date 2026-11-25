import re
import sys

rows = []
bad = False
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    row = []
    for w in line.split():
        if re.fullmatch(r"-?[0-9]+", w):
            row.append(int(w))
        else:
            bad = True
    rows.append(row)
if bad:
    print("invalid")
elif not rows:
    print("empty")
elif any(len(r) != len(rows[0]) for r in rows):
    print("ragged")
else:
    top, bottom, left, right = 0, len(rows) - 1, 0, len(rows[0]) - 1
    out = []
    while top <= bottom and left <= right:
        out += rows[top][left:right + 1]
        top += 1
        for r in range(top, bottom + 1):
            out.append(rows[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                out.append(rows[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                out.append(rows[r][left])
            left += 1
    print(" ".join(map(str, out)))
