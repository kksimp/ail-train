hs = [[2, 1, 9], [5, 0, 4], [7, 3, 12], [10, 6, 11]]
vs = [[3, 1, 8], [6, 4, 11], [8, 0, 3], [11, 6, 10], [1, 6, 9]]
events = []
for i, h in enumerate(hs):
    events.append([h[1], 0, i])
    events.append([h[2], 2, i])
for i, v in enumerate(vs):
    events.append([v[0], 1, i])
events.sort(key=lambda e: (e[0], e[1]))
active = []
found = 0
for e in events:
    if e[1] == 0:
        active.append(e[2])
    elif e[1] == 2:
        active = [a for a in active if a != e[2]]
    else:
        v = vs[e[2]]
        hits = [a for a in active if v[1] <= hs[a][0] <= v[2]]
        for a in hits:
            print(f"vertical x={v[0]:<2} crosses horizontal y={hs[a][0]} at ({v[0]}, {hs[a][0]})")
        found += len(hits)
brute = 0
for h in hs:
    for v in vs:
        if h[1] <= v[0] <= h[2] and v[1] <= h[0] <= v[2]:
            brute += 1
print(f"sweep found {found}, checking every pair finds {brute}")
