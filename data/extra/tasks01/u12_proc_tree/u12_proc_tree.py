import sys

procs = {}
ignored = 0
for raw in sys.stdin.read().splitlines():
    if not raw.strip():
        continue
    w = raw.split()
    try:
        if len(w) < 3:
            raise ValueError
        pid, ppid = int(w[0]), int(w[1])
        if pid < 0 or ppid < 0:
            raise ValueError
    except ValueError:
        ignored += 1
        continue
    if pid in procs:
        ignored += 1
        continue
    procs[pid] = (ppid, " ".join(w[2:]))
kids = {}
for pid, (pp, _) in procs.items():
    if pp != 0 and pp in procs and pp != pid:
        kids.setdefault(pp, []).append(pid)
roots = sorted(p for p, (pp, _) in procs.items() if pp == 0 or pp not in procs)
out = []
seen = set()
depth = 0


def walk(p, d):
    global depth
    seen.add(p)
    depth = max(depth, d + 1)
    out.append("  " * d + f"{p} {procs[p][1]}")
    for c in sorted(kids.get(p, [])):
        walk(c, d + 1)


for r in roots:
    walk(r, 0)
orph = sorted(p for p in procs if p not in seen)
if orph:
    out.append("orphans: " + " ".join(map(str, orph)))
out.append(f"processes={len(procs)} depth={depth} ignored={ignored}")
print("\n".join(out))
