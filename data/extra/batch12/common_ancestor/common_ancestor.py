def lca(up, depth, a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    k = 0
    while diff > 0:
        if (diff & 1) == 1:
            a = up[k][a]
        diff >>= 1
        k += 1
    if a == b:
        return a
    j = len(up) - 1
    while j >= 0:
        if up[j][a] != up[j][b]:
            a = up[j][a]
            b = up[j][b]
        j -= 1
    return up[0][a]

names = ["Rose", "Alan", "Beth", "Carl", "Dina", "Eve", "Finn", "Gail", "Hugo", "Ivy"]
parent = [0, 0, 0, 1, 1, 2, 3, 3, 5, 6]
depth = [0]
for i in range(1, len(names)):
    depth.append(depth[parent[i]] + 1)
up = [parent]
for k in range(1, 4):
    prev = up[k - 1]
    up.append([prev[prev[i]] for i in range(len(names))])
print(f"depths: {depth}")
print(f"grandparents: {up[1]}")
pairs = [[6, 7], [8, 4], [9, 7], [8, 9], [2, 5], [9, 9]]
for p in pairs:
    c = lca(up, depth, p[0], p[1])
    print(f"{names[p[0]]} and {names[p[1]]}: {names[c]}")
