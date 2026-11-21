plan = [(1, 2, 8), (2, 2, 6), (3, 2, 5), (5, 3, 4), (8, 3, 3), (12, 2, 2), (25, 0, 1)]
prev = 0
for i, (r, w, n) in enumerate(plan):
    running = r * n
    total = n * (r + w) - w + 10
    rise = "start" if prev == 0 else f"+{(running - prev) * 100 // prev}%"
    print(f"week {i + 1}: {n} x ({r} run, {w} walk) = {running:>2} min running, {total} min out, {rise}")
    prev = running
print(f"final week: one continuous {max(plan, key=lambda p: p[0])[0]} minute run")
