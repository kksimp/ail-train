def so(T):
    N = [t for t in T if t != 0]; inv = sum(1 for i in range(len(N)) for j in range(i + 1, len(N)) if N[i] > N[j]); r = 4 - T.index(0) // 4
    return (inv % 2 == 1 if r % 2 == 0 else inv % 2 == 0), inv, r
for P in [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0], [12, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 13, 6, 3], [6, 13, 7, 10, 8, 9, 11, 0, 15, 2, 12, 5, 14, 3, 1, 4], [3, 9, 1, 15, 14, 11, 4, 6, 13, 0, 10, 12, 2, 7, 8, 5]]:
    r = so(P); print(f"{r[1]} inversions, blank on row {r[2]} from bottom: {'solvable' if r[0] else 'not solvable'}")
