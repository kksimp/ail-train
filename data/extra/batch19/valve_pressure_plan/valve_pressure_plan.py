class Valve:
    def __init__(self, name, rate, links):
        self.name, self.rate, self.links = name, rate, links

def parse(line):
    head = line.split(" -> ")
    left = head[0].split(" rate=")
    return Valve(left[0], int(left[1]), head[1].split(", "))

def bfs(adj, frm):
    d = [-1 for v in adj]
    d[frm] = 0
    queue = [frm]; h = 0
    while h < len(queue):
        u = queue[h]; h += 1
        for w in adj[u]:
            if d[w] < 0:
                d[w] = d[u] + 1; queue.append(w)
    return d

def explore(pos, left, mask, flow, useful, rates, dist, best):
    if flow > best.get(mask, 0):
        best[mask] = flow
    for i, v in enumerate(useful):
        bit = 1 << i
        if (mask & bit) == 0:
            t = left - dist[pos][v] - 1
            if t > 0:
                explore(v, t, mask | bit, flow + t * rates[v], useful, rates, dist, best)

lines = ["Hub rate=0 -> Elm, Oak", "Elm rate=14 -> Hub, Fir", "Oak rate=5 -> Hub, Fir, Yew", "Fir rate=0 -> Elm, Oak, Ash", "Ash rate=21 -> Fir", "Yew rate=9 -> Oak, Pine", "Pine rate=17 -> Yew"]
valves = [parse(l) for l in lines]
index = {v.name: i for i, v in enumerate(valves)}
adj = [[index[n] for n in v.links] for v in valves]
dist = [bfs(adj, i) for i in range(len(valves))]
rates = [v.rate for v in valves]
useful = [i for i in range(len(valves)) if rates[i] > 0]
print(f"{len(useful)} valves worth opening, Hub to Pine is {dist[0][6]} tunnels")
solo = {}
explore(0, 24, 0, 0, useful, rates, dist, solo)
print(f"part 1, alone for 24 minutes: {max(solo.values()) if solo else 0}")
duo = {}
explore(0, 18, 0, 0, useful, rates, dist, duo)
pair = max(duo.values()) if duo else 0
for a, va in duo.items():
    for b, vb in duo.items():
        if (a & b) == 0 and va + vb > pair:
            pair = va + vb
print(f"part 2, with a helper for 18 minutes: {pair}")
print(f"{len(duo)} valve sets reachable in 18 minutes")
