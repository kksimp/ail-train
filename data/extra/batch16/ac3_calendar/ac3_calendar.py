def allowed(kind, x, y):
    if kind == "lt": return x < y
    if kind == "gt": return x > y
    return x != y

def flip(kind):
    return "gt" if kind == "lt" else ("lt" if kind == "gt" else "ne")

names = ["kickoff", "design", "review", "retro", "demo"]
doms = [[9, 10, 11], [9, 10, 11, 12, 13], [9, 10, 11, 12, 13], [12, 13], [11, 12, 13]]
rules = [[0, 1, 0], [1, 2, 0], [2, 4, 0], [2, 3, 1], [3, 4, 1]]
arcs = []
for r in rules:
    arcs.append([r[0], r[1], r[2], 0])
    arcs.append([r[1], r[0], r[2], 1])
queue = list(arcs)
removed = 0
while queue:
    arc = queue[0]
    queue = queue[1:]
    base = "lt" if arc[2] == 0 else "ne"
    kind = flip(base) if arc[3] == 1 else base
    x, y = arc[0], arc[1]
    keep = [a for a in doms[x] if any(allowed(kind, a, b) for b in doms[y])]
    if len(keep) < len(doms[x]):
        removed += len(doms[x]) - len(keep)
        print(f"{names[x]:<7} loses {len(doms[x]) - len(keep)} hour(s) because of {names[y]}: now {keep}")
        doms[x] = keep
        for other in arcs:
            if other[1] == x and other[0] != y:
                queue.append(other)
print(f"{removed} hours removed")
for i in range(len(names)):
    print(f"{names[i]:<7} {doms[i]}")
