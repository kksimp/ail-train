class Dsu:
    def __init__(s, n):
        s.parent, s.rank, s.history, s.groups = list(range(n)), [0] * n, [], n
    def find(s, x):
        while s.parent[x] != x:
            x = s.parent[x]
        return x
    def union(s, a, b):
        ra, rb = s.find(a), s.find(b)
        if ra == rb:
            return
        if s.rank[ra] < s.rank[rb]:
            ra, rb = rb, ra
        bumped = 1 if s.rank[ra] == s.rank[rb] else 0
        s.parent[rb] = ra
        s.rank[ra] += bumped
        s.history.append([rb, ra, bumped])
        s.groups -= 1
    def rollback(s, mark):
        while len(s.history) > mark:
            h = s.history.pop()
            s.parent[h[0]] = h[0]
            s.rank[h[1]] -= h[2]
            s.groups += 1

d = Dsu(8)
for e in [[0, 1], [2, 3], [1, 2]]:
    d.union(e[0], e[1])
print(f"base links: {d.groups} groups")
for plan in [[[4, 5], [5, 6], [6, 7]], [[3, 4], [0, 7]], [[4, 7], [7, 4]]]:
    mark = len(d.history)
    for e in plan:
        d.union(e[0], e[1])
    joined = "true" if d.find(0) == d.find(7) else "false"
    print(f"try {plan}: {d.groups} groups, 0 and 7 connected {joined}")
    d.rollback(mark)
print(f"after rollbacks: {d.groups} groups, parents {d.parent}")
