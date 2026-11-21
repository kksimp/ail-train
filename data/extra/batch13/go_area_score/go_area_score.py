rows = [".B.BW..", "BB.BW.W", "..BWW..", "BBBW.W.", "..BW...", ".BW.WW.", ".BW...."]
g = [list(row) for row in rows]
n = 7
seen = set()
black = white = neutral = 0
for r in range(n):
    for c in range(n):
        if g[r][c] == 'B':
            black += 1
        elif g[r][c] == 'W':
            white += 1
for start in range(n * n):
    if g[start // n][start % n] != '.' or start in seen:
        continue
    todo = [start]
    seen.add(start)
    size = 0
    borders = set()
    while todo:
        cell = todo.pop()
        size += 1
        r, c = cell // n, cell % n
        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < n and 0 <= nc < n:
                v = g[nr][nc]
                if v == '.':
                    if nr * n + nc not in seen:
                        seen.add(nr * n + nc)
                        todo.append(nr * n + nc)
                else:
                    borders.add(v)
    if borders == {'B'}:
        black += size
    elif borders == {'W'}:
        white += size
    else:
        neutral += size
komi = 6.5
w = float(white) + komi
print(f"black area {black}")
print(f"white area {white} + komi {komi} = {w}")
print(f"neutral points {neutral}")
margin = w - float(black)
winner = "white" if margin > 0.0 else "black"
print(f"{winner} wins by {abs(margin)}")
