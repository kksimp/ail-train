def walk(x, y, steps, seen, totals):
    if steps == 0:
        totals[0] += 1
        totals[1] += x * x + y * y
        return
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + d[0]
        ny = y + d[1]
        key = (nx + 50) * 1000 + ny + 50
        if key not in seen:
            seen.add(key)
            walk(nx, ny, steps - 1, seen, totals)
            seen.remove(key)

for n in range(1, 11):
    seen = {50 * 1000 + 50}
    totals = [0, 0]
    walk(0, 0, n, seen, totals)
    mean = float(totals[1]) / float(totals[0])
    ratio = mean / float(n)
    print(f"{n:>2} steps: {totals[0]:>5} walks, mean squared distance {mean:>7.3f} ({ratio:.3f} per step)")
