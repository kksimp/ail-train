def fill(row, h, cur, nxt, ways, out):
    if row >= h:
        out[nxt] += ways
        return
    if ((cur >> row) & 1) == 1:
        fill(row + 1, h, cur, nxt, ways, out)
        return
    fill(row + 1, h, cur, nxt | (1 << row), ways, out)
    if row + 1 < h and ((cur >> (row + 1)) & 1) == 0:
        fill(row + 2, h, cur, nxt, ways, out)

def tilings(h, n):
    size = 1 << h
    dp = [0] * size
    dp[0] = 1
    for col in range(n):
        out = [0] * size
        for m in range(size):
            if dp[m] > 0:
                fill(0, h, m, 0, dp[m], out)
        dp = out
    return dp[0]

for h in range(2, 5):
    counts = [tilings(h, n) for n in range(1, 9)]
    print(f"height {h}: {counts}")
print(f"a 4 by 4 floor: {tilings(4, 4)} ways")
