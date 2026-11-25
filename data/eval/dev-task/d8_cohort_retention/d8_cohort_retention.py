import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
users = {}
for i, line in enumerate(lines, 1):
    if line == "":
        continue
    f = line.split(" ")
    if len(f) != 2:
        print("line %d: bad format" % i)
        continue
    u, m = f
    if not (1 <= len(u) <= 8 and all(c in "abcdefghijklmnopqrstuvwxyz0123456789" for c in u)):
        print("line %d: bad user" % i)
        continue
    if not (1 <= len(m) <= 2 and all(c in "0123456789" for c in m) and 1 <= int(m) <= 24):
        print("line %d: bad month" % i)
        continue
    users.setdefault(u, set()).add(int(m))
if not users:
    print("no events")
    sys.exit(0)
lo = min(min(s) for s in users.values())
hi = max(max(s) for s in users.values())
cohorts = {}
for u, s in users.items():
    cohorts.setdefault(min(s), []).append(u)
print("\t".join(["cohort", "users"] + ["+%d" % o for o in range(hi - lo + 1)]))
for c in sorted(cohorts):
    size = len(cohorts[c])
    row = ["m%d" % c, str(size)]
    for o in range(hi - lo + 1):
        if c + o > hi:
            row.append("-")
        else:
            act = sum(1 for u in cohorts[c] if (c + o) in users[u])
            row.append("%d%%" % ((act * 200 + size) // (2 * size)))
    print("\t".join(row))
