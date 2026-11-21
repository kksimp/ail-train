import itertools
S = ["Ama", "Bex", "Cho", "Dru", "Eko"]; K = ["back", "breast", "fly", "free"]
T = [[31.2, 36.0, 30.1, 27.8], [30.4, 35.1, 31.0, 28.3], [32.0, 33.9, 29.5, 27.1], [33.5, 34.2, 30.8, 26.9], [31.0, 35.6, 29.9, 28.0]]
b = 1000.0; pk = None
for p in itertools.permutations(range(5), 4):
    t = sum(T[p[i]][i] for i in range(4))
    if t < b - 0.0001: b = t; pk = p
for i in range(4): print(f"{K[i]:<7} {S[pk[i]]} {T[pk[i]][i]:.1f}")
print(f"total {b:.1f}")
