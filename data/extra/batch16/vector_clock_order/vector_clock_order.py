def relation(u, v):
    le = all(u[i] <= v[i] for i in range(len(u)))
    ge = all(u[i] >= v[i] for i in range(len(u)))
    if le and ge: return "same"
    if le: return "happened before"
    if ge: return "happened after"
    return "concurrent with"

procs = ["a", "b", "c"]
script = [["a", "local", "a1"], ["a", "send", "m1"], ["b", "recv", "m1"], ["b", "local", "b2"], ["c", "local", "c1"], ["b", "send", "m2"], ["c", "recv", "m2"], ["a", "local", "a3"], ["c", "local", "c3"]]
clocks = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
msgs = {}
stamp = {}
for ev in script:
    p = procs.index(ev[0])
    if ev[1] == "recv":
        got = msgs[ev[2]]
        for i in range(3):
            clocks[p][i] = max(clocks[p][i], got[i])
    clocks[p][p] += 1
    if ev[1] == "send":
        msgs[ev[2]] = list(clocks[p])
    label = f"{ev[0]}:recv {ev[2]}" if ev[1] == "recv" else f"{ev[0]}:{ev[2]}"
    stamp[label] = list(clocks[p])
    print(f"{label:<11} {clocks[p]}")
for pair in [["a:a1", "c:c3"], ["a:a3", "c:c3"], ["b:b2", "c:c1"], ["c:recv m2", "a:a1"]]:
    x = stamp[pair[0]]
    y = stamp[pair[1]]
    print(f"{pair[0]} {relation(x, y)} {pair[1]}")
