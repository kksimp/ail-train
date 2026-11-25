import sys
import re

NAME = re.compile(r"^[A-Za-z0-9_-]+$")
adj = {}
nodes = []
edges = set()
bad = 0
for raw in sys.stdin.read().splitlines():
    l = raw.strip()
    if not l or l.startswith("#"):
        continue
    w = l.split()
    if len(w) != 3 or w[1] != "->" or not NAME.match(w[0]) or not NAME.match(w[2]):
        bad += 1
        continue
    for n in (w[0], w[2]):
        if n not in adj:
            adj[n] = []
            nodes.append(n)
    if (w[0], w[2]) not in edges:
        edges.add((w[0], w[2]))
        adj[w[0]].append(w[2])


def reach(s):
    seen = set()
    st = list(adj[s])
    while st:
        n = st.pop()
        if n not in seen:
            seen.add(n)
            st.extend(adj[n])
    return seen


R = {n: reach(n) for n in nodes}
cyc = sorted(n for n in nodes if n in R[n])
groups = []
done = set()
for n in cyc:
    if n in done:
        continue
    g = sorted(m for m in cyc if m == n or (m in R[n] and n in R[m]))
    done.update(g)
    groups.append(g)
cs = set(cyc)
blocked = sorted(n for n in nodes if n not in cs and any(m in cs for m in R[n]))
out = []
for i, g in enumerate(groups, 1):
    out.append(f"deadlock {i}: {' '.join(g)}")
if blocked:
    out.append("blocked: " + " ".join(blocked))
status = "deadlock" if groups else "ok"
out.append(f"status={status} groups={len(groups)} deadlocked={len(cyc)} blocked={len(blocked)} ignored={bad}")
print("\n".join(out))
