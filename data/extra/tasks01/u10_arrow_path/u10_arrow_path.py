import sys
g = [l for l in sys.stdin.read().split("\n") if l != ""]
if not g:
    print("empty"); sys.exit(0)
D = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
seen = {}
r = c = moves = 0
while True:
    seen[(r, c)] = moves
    ch = g[r][c]
    if ch not in D:
        print(f"stuck at {r},{c} after {moves} moves"); break
    nr, nc = r + D[ch][0], c + D[ch][1]
    if not (0 <= nr < len(g) and 0 <= nc < len(g[0])):
        print(f"exit after {moves + 1} moves"); break
    if (nr, nc) in seen:
        print(f"loop of length {moves + 1 - seen[(nr, nc)]} entered at {nr},{nc} after {moves + 1} moves"); break
    r, c = nr, nc
    moves += 1
