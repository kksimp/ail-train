F = [("oats", 389.0, 16.9, 66.3, 6.9), ("milk", 64.0, 3.4, 4.8, 3.6), ("banana", 89.0, 1.1, 22.8, 0.3), ("peanut butter", 588.0, 25.0, 20.0, 50.0)]; G = [160.0, 600.0, 240.0, 64.0]; T = [0.0] * 4
for i, f in enumerate(F):
    k = G[i] / 100.0
    for j in range(4): T[j] += f[j + 1] * k
    print(f"{f[0]:<14} {G[i]:>5.0f} g {f[1] * k:>6.1f} kcal")
L = ["kcal", "protein g", "carbs g", "fat g"]
for i in range(4): print(f"{L[i]:<10} total {T[i]:>7.1f}, per serving {T[i] / 4.0:>6.1f}")
