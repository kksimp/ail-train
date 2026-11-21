def bk(r, p, x, adj, out):
    if not p and not x:
        out.append(r)
        return
    cand = list(p)
    done = list(x)
    for v in p:
        r2 = r + [v]
        p2 = [w for w in cand if adj[v][w]]
        x2 = [w for w in done if adj[v][w]]
        bk(r2, p2, x2, adj, out)
        cand = [w for w in cand if w != v]
        done.append(v)

names = ["Amy", "Ben", "Cat", "Dev", "Eli", "Fay", "Gus", "Hal"]
pairs = [[0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6], [6, 7], [5, 7], [4, 7], [2, 5]]
adj = [[False] * 8 for _ in range(8)]
for a, b in pairs:
    adj[a][b] = True
    adj[b][a] = True
out = []
bk([], list(range(8)), [], adj, out)
biggest = 0
for c in out:
    who = ", ".join(names[i] for i in c)
    print(f"maximal group of {len(c)}: {who}")
    biggest = max(biggest, len(c))
print(f"{len(out)} maximal groups, clique number {biggest}")
