def re(k, c, a, m): b = 10.0 * k + 6.25 * c - 5.0 * a; return b + 5.0 if m else b - 161.0
for n, k, c, a, m, f in [("Ari", 70.0, 175.0, 30, True, 1.55), ("Bea", 58.0, 164.0, 45, False, 1.375), ("Cole", 95.0, 188.0, 52, True, 1.2), ("Dina", 64.0, 172.0, 24, False, 1.725)]:
    r = re(k, c, a, m); print(f"{n}: resting {r:.0f} kcal, daily {r * f:.0f} kcal")
