def encode(n, edges):
    deg = [0] * n
    for e in edges:
        deg[e[0]] += 1
        deg[e[1]] += 1
    code = []
    for _ in range(n - 2):
        leaf = 0
        while deg[leaf] != 1:
            leaf += 1
        nb = -1
        for e in edges:
            if e[0] == leaf and deg[e[1]] > 0:
                nb = e[1]
            elif e[1] == leaf and deg[e[0]] > 0:
                nb = e[0]
        deg[leaf] = 0
        deg[nb] -= 1
        code.append(nb)
    return code

def decode(code):
    n = len(code) + 2
    deg = [1] * n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = 0
        while deg[leaf] != 1:
            leaf += 1
        edges.append([min(leaf, x), max(leaf, x)])
        deg[leaf] -= 1
        deg[x] -= 1
    last = [i for i in range(n) if deg[i] == 1]
    edges.append([last[0], last[1]])
    return sorted(edges)

edges = [[0, 3], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [5, 7]]
code = encode(8, edges)
print(f"tree edges: {edges}")
print(f"code: {code}")
back = decode(code)
print(f"decoded: {back}")
print(f"round trip ok: {str(back == sorted(edges)).lower()}")
star = decode([2, 2, 2, 2])
print(f"code [2, 2, 2, 2] is a star: {star}")
path = decode([1, 2, 3, 4])
print(f"code [1, 2, 3, 4] is a path: {path}")
