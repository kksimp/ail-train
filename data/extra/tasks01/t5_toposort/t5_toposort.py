import sys


def clean(s):
    return s != "" and " " not in s


nodes = set()
seen = set()
after = {}
indeg = {}
for raw in sys.stdin.read().splitlines():
    line = raw.strip()
    if not line:
        continue
    parts = line.split(" -> ")
    if len(parts) == 2 and clean(parts[0]) and clean(parts[1]):
        a, b = parts
        nodes.add(a)
        nodes.add(b)
        if (a, b) not in seen:
            seen.add((a, b))
            after.setdefault(a, []).append(b)
            indeg[b] = indeg.get(b, 0) + 1
    elif len(parts) == 1 and clean(line):
        nodes.add(line)
ready = [n for n in sorted(nodes) if indeg.get(n, 0) == 0]
order = []
while ready:
    m = min(ready)
    ready.remove(m)
    order.append(m)
    for nb in after.get(m, []):
        indeg[nb] -= 1
        if indeg[nb] == 0:
            ready.append(nb)
if len(order) == len(nodes):
    print("order: " + " ".join(order) if order else "order:")
else:
    placed = set(order)
    print("cycle: " + " ".join(n for n in sorted(nodes) if n not in placed))
