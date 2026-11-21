def solve(n):
    out = []
    def pl(row, cols):
        if row == n: out.append(cols[:]); return
        for c in range(n):
            if all(cols[r] != c and abs(cols[r] - c) != row - r for r in range(row)):
                cols.append(c); pl(row + 1, cols); cols.pop()
    pl(0, [])
    return out
for n in range(1, 9): print(f"n={n}: {len(solve(n))} solutions")
for c in solve(6)[0]: print("".join("Q" if i == c else "." for i in range(6)))
