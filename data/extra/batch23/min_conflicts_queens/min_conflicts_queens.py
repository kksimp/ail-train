class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def attacks(rows, col, row):
    count = 0
    for k in range(len(rows)):
        if k != col:
            r = rows[k]
            if r == row or abs(r - row) == abs(k - col):
                count += 1
    return count

def solve(n, rng, steps):
    rows = []
    for _ in range(n):
        rows.append(rng.next(n))
    for step in range(5000):
        bad = [c for c in range(n) if attacks(rows, c, rows[c]) > 0]
        if len(bad) == 0:
            steps[0] = step
            return rows
        col = bad[rng.next(len(bad))]
        least = n + 1
        options = []
        for r in range(n):
            a = attacks(rows, col, r)
            if a < least:
                least = a
                options = [r]
            elif a == least:
                options.append(r)
        rows[col] = options[rng.next(len(options))]
    steps[0] = -1
    return rows

rng = Lcg(12)
steps = [0]
board = solve(8, rng, steps)
print(f"8 queens after {steps[0]} moves:")
for r in range(8):
    print(" ".join("Q" if board[c] == r else "." for c in range(8)))
for n in [16, 32, 64]:
    solve(n, rng, steps)
    print(f"{n} queens: solved after {steps[0]} moves")
