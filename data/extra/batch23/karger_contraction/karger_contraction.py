class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return self.state // 65536 % n

def find(parent, x):
    v = x
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v

def trial(n, edges, rng):
    parent = list(range(n))
    groups = n
    while groups > 2:
        e = edges[rng.next(len(edges))]
        a = find(parent, e[0])
        b = find(parent, e[1])
        if a != b:
            parent[a] = b
            groups -= 1
    cut = 0
    for f in edges:
        fa = find(parent, f[0])
        fb = find(parent, f[1])
        if fa != fb:
            cut += 1
    return cut

edges = []
for i in range(4):
    for j in range(i + 1, 4):
        edges.append([i, j])
        edges.append([i + 4, j + 4])
edges.append([0, 4])
edges.append([3, 7])
edges.append([1, 2])
print(f"8 nodes, {len(edges)} edges: two tight clusters joined by two links")
rng = Lcg(2024)
cuts = []
for _ in range(12):
    cuts.append(trial(8, edges, rng))
best = min(cuts)
hits = sum(1 for c in cuts if c == best)
print(f"cut found by each trial: {cuts}")
print(f"smallest cut {best}, found in {hits} of {len(cuts)} trials")
print("one trial succeeds with chance at least 2/(n(n-1)) = 1/28")
