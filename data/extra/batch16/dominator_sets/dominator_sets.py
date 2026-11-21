def popcount(x):
    return bin(x).count("1")

def members(mask, names):
    return " ".join(names[i] for i in range(len(names)) if (mask >> i) & 1 == 1)

names = ["entry", "a", "b", "c", "d", "e", "exit"]
edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 1], [4, 5], [5, 6], [3, 6]]
n = len(names)
full = (1 << n) - 1
dom = [1 if i == 0 else full for i in range(n)]
rounds = 0
changed = True
while changed:
    changed = False
    rounds += 1
    for v in range(1, n):
        meet = full
        for e in edges:
            if e[1] == v:
                meet = meet & dom[e[0]]
        updated = meet | (1 << v)
        if updated != dom[v]:
            dom[v] = updated
            changed = True
for v in range(n):
    idom = "-"
    best = 0
    for d in range(n):
        if d != v and (dom[v] >> d) & 1 == 1 and popcount(dom[d]) > best:
            best = popcount(dom[d])
            idom = names[d]
    print(f"{names[v]:<6} dominated by: {members(dom[v], names):<18} idom {idom}")
print(f"stable after {rounds} rounds")
