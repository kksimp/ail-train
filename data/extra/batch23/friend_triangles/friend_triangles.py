names = ["Ana", "Ben", "Cleo", "Dev", "Eve", "Finn", "Gia", "Hugo"]
edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6], [6, 7], [2, 4], [1, 7]]
deg = [0 for p in names]
linked = set()
for e in edges:
    linked.add(e[0] * 100 + e[1])
    linked.add(e[1] * 100 + e[0])
    deg[e[0]] += 1
    deg[e[1]] += 1
out = {}
for e in edges:
    a = e[0]
    b = e[1]
    if deg[a] < deg[b] or (deg[a] == deg[b] and a < b):
        out.setdefault(a, []).append(b)
    else:
        out.setdefault(b, []).append(a)
tri = [0 for q in names]
checks = 0
found = []
for v in range(len(names)):
    outs = out.get(v, [])
    for i in range(len(outs)):
        for j in range(i):
            checks += 1
            x = outs[i]
            y = outs[j]
            if x * 100 + y in linked:
                tri[v] += 1
                tri[x] += 1
                tri[y] += 1
                found.append(f"{names[v]}-{names[x]}-{names[y]}")
shown = ", ".join(found)
print(f"{len(found)} triangles after {checks} pair checks: {shown}")
for v in range(len(names)):
    pairs = deg[v] * (deg[v] - 1) // 2
    print(f"{names[v]:<5} friends {deg[v]}, triangles {tri[v]} of {pairs} friend pairs")
