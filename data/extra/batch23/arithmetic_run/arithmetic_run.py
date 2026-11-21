def longest(xs):
    maps = []
    best_len = 1
    best_end = 0
    best_gap = 0
    for i in range(len(xs)):
        here = {}
        for j in range(i):
            d = xs[i] - xs[j]
            l = maps[j].get(d, 1) + 1
            if l > here.get(d, 0):
                here[d] = l
            if l > best_len:
                best_len = l
                best_end = i
                best_gap = d
        maps.append(here)
    run = []
    v = xs[best_end] - best_gap * (best_len - 1)
    for k in range(best_len):
        run.append(v)
        v += best_gap
    return run

for xs in [[3, 6, 9, 12], [9, 4, 7, 2, 10], [20, 1, 15, 3, 10, 5, 8], [1, 7, 10, 13, 14, 19], [5, 5, 5, 1, 5], [83, 20, 17, 43, 52, 78, 68, 45]]:
    run = longest(xs)
    gap = run[1] - run[0] if len(run) > 1 else 0
    print(f"{xs} -> {run} (length {len(run)}, step {gap})")
