n = 7; g = [[0] * n for r in range(n)]; g[3][3] = 150; top = 0; busy = True
while busy:
    busy = False
    for r in range(n):
        for c in range(n):
            if g[r][c] >= 4:
                busy = True; top += 1; g[r][c] -= 4
                if r > 0: g[r - 1][c] += 1
                if r < n - 1: g[r + 1][c] += 1
                if c > 0: g[r][c - 1] += 1
                if c < n - 1: g[r][c + 1] += 1
left = 0
for row in g: print(" ".join(str(x) for x in row)); left += sum(row)
print(f"{top} topples, {left} grains left, {150 - left} fell off")
