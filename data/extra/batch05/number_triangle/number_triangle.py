T = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3], [1, 6, 2, 8, 4]]; B = [r[:] for r in T]
for r in range(len(T) - 2, -1, -1):
    for c in range(len(T[r])): B[r][c] = T[r][c] + max(B[r + 1][c], B[r + 1][c + 1])
p = []; c = 0
for r in range(len(T)):
    p.append(T[r][c])
    if r + 1 < len(T) and B[r + 1][c + 1] > B[r + 1][c]: c += 1
print(f"max {B[0][0]} = {' + '.join(map(str, p))}")
