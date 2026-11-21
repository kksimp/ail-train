def group(b, r0, c0, cells):
    colour = b[r0][c0]
    seen = {r0 * 7 + c0}
    libs = set()
    stack = [[r0, c0]]
    while stack:
        cur = stack.pop()
        cells.append(cur)
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r = cur[0] + d[0]; c = cur[1] + d[1]
            if 0 <= r < 7 and 0 <= c < 7:
                if b[r][c] == '.':
                    libs.add(r * 7 + c)
                elif b[r][c] == colour and (r * 7 + c) not in seen:
                    seen.add(r * 7 + c)
                    stack.append([r, c])
    return len(libs)

def play(b, r, c, me):
    b[r][c] = me
    foe = 'O' if me == 'X' else 'X'
    taken = 0
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nr = r + d[0]; nc = c + d[1]
        if 0 <= nr < 7 and 0 <= nc < 7 and b[nr][nc] == foe:
            cells = []
            if group(b, nr, nc, cells) == 0:
                for cell in cells:
                    b[cell[0]][cell[1]] = '.'
                taken += len(cells)
    return taken

b = [['.'] * 7 for _ in range(7)]
moves = [[2, 2], [2, 3], [1, 3], [3, 3], [3, 2], [2, 4], [6, 6], [3, 4], [4, 3], [1, 4], [0, 4], [5, 5], [1, 5], [6, 5], [2, 5], [5, 6], [3, 5], [6, 0], [4, 4]]
caps = [0, 0]
for i, m in enumerate(moves):
    me = 'X' if i % 2 == 0 else 'O'
    got = play(b, m[0], m[1], me)
    caps[i % 2] += got
    if got > 0:
        print(f"move {i + 1}: {me} at ({m[0]}, {m[1]}) captures {got}")
for row in b:
    print("".join(row))
print(f"captures: X {caps[0]}, O {caps[1]}")
