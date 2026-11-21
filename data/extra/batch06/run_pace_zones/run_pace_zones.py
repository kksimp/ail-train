def zs(r, m):
    b = [50, 60, 70, 80, 90, 100]; v = m - r; return [(r + v * b[i] // 100, r + v * b[i + 1] // 100) for i in range(5)]
Z = zs(58, 186)
for i, z in enumerate(Z): print(f"zone {i + 1}: {z[0]}-{z[1]} bpm")
for h in [110, 132, 150, 168, 181, 95]:
    l = "below zones"
    for i, z in enumerate(Z):
        if z[0] <= h < z[1]: l = f"zone {i + 1}"
    if h >= Z[4][1]: l = "max"
    print(f"{h} bpm: {l}")
