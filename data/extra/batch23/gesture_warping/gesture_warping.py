def dtw(a, b):
    big = 1000000000
    prev = [0] + [big] * len(b)
    for i in range(1, len(a) + 1):
        cur = [big]
        for j in range(1, len(b) + 1):
            step = abs(a[i - 1] - b[j - 1])
            cur.append(step + min(min(prev[j], cur[j - 1]), prev[j - 1]))
        prev = cur
    return prev[len(b)]

templates = [("wave", [0, 3, 6, 3, 0, -3, -6, -3, 0]), ("push", [0, 1, 4, 9, 9, 9, 4, 1, 0]), ("flick", [0, 8, 0, 0, 0, 0, 0, 0, 0])]
recordings = [("rec1", [0, 2, 3, 5, 6, 6, 3, 1, 0, -2, -4, -6, -5, -3, 0]), ("rec2", [0, 0, 1, 3, 5, 9, 10, 9, 9, 5, 2, 0]), ("rec3", [1, 7, 1, 0, 0])]
for rname, trace in recordings:
    best = ""
    best_cost = -1
    parts = []
    for tname, shape in templates:
        c = dtw(trace, shape)
        parts.append(f"{tname} {c}")
        if best_cost < 0 or c < best_cost:
            best_cost = c
            best = tname
    shown = ", ".join(parts)
    print(f"{rname}: {shown} -> {best}")
print(f"same trace at half speed: {dtw([1, 1, 5, 5, 2, 2], [1, 5, 2])}")
