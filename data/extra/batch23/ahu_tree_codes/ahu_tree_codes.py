def children(parents):
    kids = [[] for _ in parents]
    for v in range(len(parents)):
        if parents[v] >= 0:
            kids[parents[v]].append(v)
    return kids

def code(kids, v):
    parts = sorted(code(kids, c) for c in kids[v])
    inner = "".join(parts)
    return f"({inner})"

names = ["A", "B", "C", "D", "E"]
trees = [[-1, 0, 0, 1, 1, 2], [-1, 0, 0, 2, 2, 1], [-1, 0, 1, 2, 2, 0], [-1, 0, 0, 0, 1, 2], [-1, 2, 0, 2, 0, 4]]
groups = {}
for i in range(len(trees)):
    c = code(children(trees[i]), 0)
    print(f"{names[i]}: {c}")
    groups.setdefault(c, []).append(names[i])
for c, members in groups.items():
    shown = " ".join(members)
    print(f"same shape: {shown}")
