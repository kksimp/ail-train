def square(r, c):
    return f"{chr(97 + c)}{8 - r}"

def chains(board, r, c, path, out):
    extended = False
    for dc in [-1, 1]:
        mr, mc = r - 1, c + dc
        lr, lc = r - 2, c + dc * 2
        if lr >= 0 and lc >= 0 and lc < 8:
            if board[mr][mc] == 'b' and board[lr][lc] == '.':
                nxt = [row[:] for row in board]
                nxt[r][c] = '.'
                nxt[mr][mc] = '.'
                nxt[lr][lc] = 'w'
                chains(nxt, lr, lc, f"{path}x{square(lr, lc)}", out)
                extended = True
    if not extended and "x" in path:
        out.append(path)

rows = ["........", "..b.b...", "........", "..b.b...", "...w....", "........", ".w...b..", "w.w....."]
board = [list(row) for row in rows]
all_chains = []
for r in range(8):
    for c in range(8):
        if board[r][c] == 'w':
            chains(board, r, c, square(r, c), all_chains)
longest = 0
for ch in all_chains:
    n = ch.count("x")
    print(f"{ch} takes {n}")
    if n > longest:
        longest = n
best = [ch for ch in all_chains if ch.count("x") == longest]
print(f"must play one of: {', '.join(best)}")
