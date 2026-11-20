jobs = [("a", 2, 100), ("b", 1, 19), ("c", 2, 27), ("d", 1, 25), ("e", 3, 15)]
days = [None] * max(j[1] for j in jobs)
for j in sorted(jobs, key=lambda j: -j[2]):
    for d in range(j[1] - 1, -1, -1):
        if days[d] is None:
            days[d] = j[0]; break
tot = 0
for i, d in enumerate(days):
    if d:
        p = next(j[2] for j in jobs if j[0] == d); tot += p
        print(f"day {i + 1}: job {d} ({p})")
    else:
        print(f"day {i + 1}: idle")
print(f"profit: {tot}")
