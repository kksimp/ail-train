neg = -1000000
def step(a, x):
    out = []
    for i in range(len(a)):
        best = neg
        for j in range(len(a)):
            if a[i][j] > neg:
                best = max(best, a[i][j] + x[j])
        out.append(best)
    return out
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
a = [[2, 5, neg], [neg, 3, 6], [4, neg, 1]]
x = [0, 0, 0]
prev = x
for k in range(1, 9):
    x = step(a, x)
    diffs = [x[i] - prev[i] for i in range(3)]
    print(f"round {k}: times {fl(x)}, gaps {fl(diffs)}")
    prev = x
best_n, best_d = 0, 1
cycles = []
for c in [[0], [1], [2], [0, 1], [1, 2], [0, 2], [0, 1, 2], [0, 2, 1]]:
    w = 0
    ok = True
    for i in range(len(c)):
        fr, to = c[i], c[(i + 1) % len(c)]
        if a[to][fr] <= neg:
            ok = False
        else:
            w += a[to][fr]
    if ok:
        cycles.append(f"{fl(c)}:{w}/{len(c)}")
        if w * best_d > best_n * len(c):
            best_n, best_d = w, len(c)
print("cycles " + " ".join(cycles))
print(f"largest cycle mean {best_n}/{best_d}: the timetable repeats every {best_n} time units per {best_d} rounds")
