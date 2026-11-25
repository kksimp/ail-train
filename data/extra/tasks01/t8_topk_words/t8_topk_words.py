import re
import sys

lines = sys.stdin.read().splitlines()
if not lines or not re.fullmatch(r"[0-9]+", lines[0].strip()) or int(lines[0].strip()) < 1:
    print("bad k")
    sys.exit(0)
k = int(lines[0].strip())
counts = {}
for w in re.findall(r"[A-Za-z]+", "\n".join(lines[1:])):
    w = w.lower()
    counts[w] = counts.get(w, 0) + 1
for w, n in sorted(counts.items(), key=lambda p: (-p[1], p[0]))[:k]:
    print("%s %d" % (w, n))
