import math
T = [("Avon", 0.0, 0.0), ("Brook", 3.0, 4.0), ("Cale", 6.0, 1.0), ("Dunn", 2.0, 9.0), ("Esk", 8.0, 7.0)]
d = lambda a, b: math.hypot(a[1] - b[1], a[2] - b[2])
for i in range(1, len(T)):
    print(f"{T[i][0]:<6}" + "".join(f"{d(T[i], T[j]):6.2f}" for j in range(i)))
P = [(i, j) for i in range(len(T)) for j in range(i + 1, len(T))]
n = min(P, key=lambda p: d(T[p[0]], T[p[1]])); f = max(P, key=lambda p: d(T[p[0]], T[p[1]]))
print(f"closest: {T[n[0]][0]}-{T[n[1]][0]} {d(T[n[0]], T[n[1]]):.2f}")
print(f"farthest: {T[f[0]][0]}-{T[f[1]][0]} {d(T[f[0]], T[f[1]]):.2f}")
