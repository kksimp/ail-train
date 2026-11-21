p = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
b = [int(ch) for ch in p]; tries = [0]
def fits(pos, d):
    r, c = divmod(pos, 9)
    for i in range(9):
        if b[r * 9 + i] == d or b[i * 9 + c] == d: return False
    br = r // 3 * 3; bc = c // 3 * 3
    return all(b[(br + i) * 9 + bc + j] != d for i in range(3) for j in range(3))
def solve():
    pos = next((i for i in range(81) if b[i] == 0), -1)
    if pos < 0: return True
    for d in range(1, 10):
        if fits(pos, d):
            b[pos] = d; tries[0] += 1
            if solve(): return True
            b[pos] = 0
    return False
if solve():
    for r in range(9): print("".join(str(x) for x in b[r * 9:r * 9 + 9]))
    print(f"solved after {tries[0]} placements")
else: print("no solution")
