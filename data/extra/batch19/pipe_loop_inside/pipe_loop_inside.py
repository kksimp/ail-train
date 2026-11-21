EX = {'|': [0, 2], '-': [1, 3], 'L': [0, 1], 'J': [0, 3], '7': [2, 3], 'F': [1, 2]}
def exits(ch):
    return EX.get(ch, [])

rows = ["..........", ".S---7....", ".|...|.F7.", ".|...L-J|.", ".L-7....|.", "...|.F--J.", "...L-J...."]
g = [list(r) for r in rows]
dr = [-1, 0, 1, 0]; dc = [0, 1, 0, -1]
for r in range(len(g)):
    for c in range(len(g[0])):
        if g[r][c] == 'S': sr, sc = r, c
sdirs = []
for d in range(4):
    nr = sr + dr[d]; nc = sc + dc[d]
    if 0 <= nr < len(g) and 0 <= nc < len(g[0]) and (d + 2) % 4 in exits(g[nr][nc]):
        sdirs.append(d)
for ch in "|-LJ7F":
    if exits(ch) == sdirs:
        g[sr][sc] = ch
print(f"S is a {g[sr][sc]} piece")
on_loop = set(); r, c = sr, sc; d = sdirs[0]
while r * 100 + c not in on_loop:
    on_loop.add(r * 100 + c)
    r += dr[d]; c += dc[d]
    came = (d + 2) % 4
    d = [e for e in exits(g[r][c]) if e != came][0]
print(f"loop length {len(on_loop)}")
print(f"part 1: farthest point is {len(on_loop) // 2} steps away")
inside = 0
for y in range(len(g)):
    within = False
    for x in range(len(g[0])):
        if y * 100 + x in on_loop:
            if 0 in exits(g[y][x]):
                within = not within
        elif within:
            inside += 1
print(f"part 2: {inside} tiles are enclosed")
