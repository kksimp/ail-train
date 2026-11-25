import sys

groups = {}
for line in sys.stdin.read().splitlines():
    w = line.strip().lower()
    if not w:
        continue
    k = "".join(sorted(w))
    s = groups.setdefault(k, [])
    if w not in s:
        s.append(w)
out = sorted(" ".join(sorted(s)) for s in groups.values() if len(s) >= 2)
if out:
    print("\n".join(out))
else:
    print("none")
