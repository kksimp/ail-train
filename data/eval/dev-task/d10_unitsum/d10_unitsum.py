import re
import sys

F = {"mm": 1, "cm": 10, "m": 1000, "km": 1000000}
total = 0
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    w = line.split()
    if not w:
        continue
    if len(w) != 2 or w[1] not in F or not re.fullmatch(r"[0-9]+", w[0]):
        print("error: line %d" % n)
        continue
    total += int(w[0]) * F[w[1]]
print("total: %d.%03d m" % (total // 1000, total % 1000))
