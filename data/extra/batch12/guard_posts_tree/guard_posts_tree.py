import sys
def solve(u, frm, adj, take, skip):
    take[u] = 1
    skip[u] = 0
    for v in adj[u]:
        if v != frm:
            solve(v, u, adj, take, skip)
            take[u] += min(take[v], skip[v])
            skip[u] += take[v]

def pick(u, frm, parent_taken, adj, take, skip, chosen):
    me = (not parent_taken) or take[u] < skip[u]
    if me:
        chosen.append(u)
    for v in adj[u]:
        if v != frm:
            pick(v, u, me, adj, take, skip, chosen)

rooms = ["Foyer", "Egypt", "Rome", "Greece", "Mummies", "Coins", "Statues", "Vases", "Shop", "Cafe"]
halls = [[0, 1], [0, 2], [0, 8], [1, 4], [2, 3], [2, 5], [3, 6], [3, 7], [8, 9]]
n = len(rooms)
adj = [[] for _ in range(n)]
take = [0] * n
skip = [0] * n
for h in halls:
    adj[h[0]].append(h[1])
    adj[h[1]].append(h[0])
solve(0, -1, adj, take, skip)
print(f"with a guard in the Foyer: {take[0]}, without: {skip[0]}")
chosen = []
pick(0, -1, True, adj, take, skip, chosen)
names = ", ".join(rooms[i] for i in sorted(chosen))
print(f"{len(chosen)} guards: {names}")
for h in halls:
    ok = h[0] in chosen or h[1] in chosen
    if not ok:
        print(f"unguarded: {rooms[h[0]]}-{rooms[h[1]]}")
print(f"all {len(halls)} corridors watched")
