g = [[(r * 3 + r // 3 + c) % 9 + 1 for c in range(9)] for r in range(9)]
W = list(range(1, 10))
def bad(g):
    for i in range(9):
        if sorted(g[i]) != W: return f"row {i + 1}"
        if sorted(g[r][i] for r in range(9)) != W: return f"column {i + 1}"
        br, bc = i // 3 * 3, i % 3 * 3
        if sorted(g[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)) != W: return f"box {i + 1}"
    return None
print("".join(map(str, g[0]))); print("".join(map(str, g[1])))
print(f"valid: {str(bad(g) is None).lower()}")
g[4][4] = g[4][5]
print(f"after change: {bad(g) or 'valid'}")
