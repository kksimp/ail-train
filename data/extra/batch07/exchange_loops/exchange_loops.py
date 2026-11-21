N = ["USD", "EUR", "GBP", "JPY"]; R = [[1.0, 0.92, 0.79, 151.2], [1.089, 1.0, 0.862, 164.9], [1.285, 1.162, 1.0, 191.0], [0.00662, 0.00607, 0.00524, 1.0]]; f = 0.0
for a in range(4):
    for b in range(4):
        for c in range(4):
            if a == b or b == c or a == c or a > b or a > c: continue
            e = 1000.0 * R[a][b] * 0.998 * R[b][c] * 0.998 * R[c][a] * 0.998
            if e > 1000.0: f += 1
            print(f"{N[a]}>{N[b]}>{N[c]}>{N[a]}: {e:.2f}{' profit' if e > 1000.0 else ''}")
print(f"{int(f)} profitable loop(s)")
