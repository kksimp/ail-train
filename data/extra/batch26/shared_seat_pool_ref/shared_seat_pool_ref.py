shared = [10, 0]; kiosk = [4, 0]
desks = [("box office", shared), ("website", shared), ("kiosk", kiosk)]
for i, n in [(0, 3), (1, 4), (2, 3), (0, 2), (1, 2), (2, 2), (0, 1)]:
    name, p = desks[i]
    ok = p[0] >= n
    if ok: p[0] -= n; p[1] += n
    print(f"{name:<10} sells {n}: {'ok' if ok else 'refused'}, its pool has {p[0]} left")
print(f"shared pool sold {shared[1]}, left {shared[0]}")
print(f"kiosk pool sold {kiosk[1]}, left {kiosk[0]}")
