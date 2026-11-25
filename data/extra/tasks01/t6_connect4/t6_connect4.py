import sys
def verdict(line):
    cols, rows = 7, 6
    board = [["."] * cols for _ in range(rows)]
    won = False
    n = 0
    for ch in line:
        if won:
            return "invalid"
        if ch not in "1234567":
            return "invalid"
        c = int(ch) - 1
        r = 0
        while r < rows and board[r][c] != ".":
            r += 1
        if r == rows:
            return "invalid"
        p = "R" if n % 2 == 0 else "Y"
        board[r][c] = p
        n += 1
        for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
            cnt = 1
            for s in (1, -1):
                rr, cc = r + s * dr, c + s * dc
                while 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == p:
                    cnt += 1
                    rr += s * dr
                    cc += s * dc
            if cnt >= 4:
                won = True
        if won:
            winner, at = p, n
    if won:
        return "%s wins at move %d" % (winner, at)
    if n == 42:
        return "draw"
    return "in progress"
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
for l in lines:
    print(verdict(l.rstrip("\r")))
