def slide(row, score):
    tiles = [x for x in row if x != 0]
    out = []
    i = 0
    while i < len(tiles):
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            out.append(tiles[i] * 2)
            score[0] += tiles[i] * 2
            i += 2
        else:
            out.append(tiles[i])
            i += 1
    while len(out) < len(row):
        out.append(0)
    return out

def transpose(b):
    return [[b[r][c] for r in range(len(b))] for c in range(len(b[0]))]

def apply(b, d, score):
    if d == 'L':
        return [slide(r, score) for r in b]
    if d == 'R':
        return [slide(r[::-1], score)[::-1] for r in b]
    if d == 'U':
        return transpose([slide(r, score) for r in transpose(b)])
    return transpose([slide(r[::-1], score)[::-1] for r in transpose(b)])

b = [[2, 2, 4, 0], [0, 4, 4, 4], [2, 0, 2, 8], [8, 8, 0, 8]]
score = [0]
for d in "LUDRL":
    b = apply(b, d, score)
    rows = " |".join("".join(f"{x:>3}" for x in r) for r in b)
    print(f"{d}:{rows}")
print(f"score {score[0]}, best tile {max(max(r) for r in b)}")
