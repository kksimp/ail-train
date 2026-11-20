g = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
R, C = len(g), len(g[0])
diags = [[g[r][d - r] for r in range(R) if 0 <= d - r < C] for d in range(R + C - 1)]
for line in diags:
    print(f"{' '.join(map(str, line)):<10} sum {sum(line)}")
z = []
for i, line in enumerate(diags):
    z.extend(line[::-1] if i % 2 == 0 else line)
print(",".join(map(str, z)))
print(1)
