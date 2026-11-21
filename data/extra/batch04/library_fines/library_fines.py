def fi(d, r):
    l = r - d - 1
    if l <= 0: return 0
    return min(500, sum(20 if k <= 7 else 40 for k in range(1, l + 1)))
t = 0
for n, d, b in [("Dune", 10, 10), ("Emma", 10, 12), ("Ulysses", 5, 13), ("Beloved", 3, 20), ("Walden", 1, 40)]:
    f = fi(d, b); t += f; print(f"{n:<8} {b - d:>3} days late: {f // 100}.{f % 100:02}")
print(f"total: {t // 100}.{t % 100:02}")
