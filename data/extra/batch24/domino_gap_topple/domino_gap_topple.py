import math
row = [(0.0, 4.0), (3.0, 4.0), (6.5, 5.0), (10.0, 5.0), (14.5, 6.0), (18.0, 3.0), (20.5, 3.0), (24.0, 4.0)]
t = 0.0; fallen = 1
print("domino 1 pushed at 0.000 s")
for i in range(len(row) - 1):
    gap = row[i + 1][0] - row[i][0]
    if gap >= row[i][1]:
        print(f"domino {i + 1} falls short: gap {gap:.1f} is not less than its height {row[i][1]:.1f}")
        break
    t += 0.1 * math.sqrt(row[i][1]) * gap / row[i][1]
    fallen += 1
    print(f"domino {i + 2} hit at {t:.3f} s")
print(f"{fallen} of {len(row)} dominoes fell")
