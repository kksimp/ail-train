def step(p, q):
    return 2 * p if 2 * p < q else 2 * q - 2 * p
for p0, q in [[1, 5], [1, 7], [2, 9], [3, 11], [1, 8], [5, 12]]:
    p = p0
    seen = {}
    path = []
    i = 0
    while p not in seen:
        seen[p] = i
        path.append(f"{p}/{q}")
        p = step(p, q)
        i += 1
    start = seen[p]
    print(f"{' -> '.join(path)} -> {p}/{q}: cycle of {i - start} after {start} steps")
for v in [0.1, 0.2, 1.0 / 7.0]:
    x = v
    n = 0
    while x != 0.0 and n < 200:
        x = 2.0 * x if x < 0.5 else 2.0 - 2.0 * x
        n += 1
    print(f"float start {v:.4f}: reaches 0 after {n} steps")
