trips = [(1500, 0, False), (1501, 0, False), (8200, 6, True), (0, 0, False), (23000, 15, False)]
def fare(m, w, n):
    base = 390 + (m + 199) // 200 * 55 + w * 60
    x = base * 125 // 100 if n else base
    return (x + 9) // 10 * 10
tot = 0
for i, (m, w, n) in enumerate(trips):
    f = fare(m, w, n); tot += f
    print(f"trip {i + 1}: {m:>6} m, {w:>2} min wait, {'night' if n else 'day':<5} {f // 100}.{f % 100:02d}")
print(f"shift takings: {tot // 100}.{tot % 100:02d}")
