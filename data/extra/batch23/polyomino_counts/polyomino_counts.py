def key_of(cells):
    minx = min(c[0] for c in cells)
    miny = min(c[1] for c in cells)
    moved = sorted([[c[0] - minx, c[1] - miny] for c in cells], key=lambda c: (c[0], c[1]))
    return ";".join(f"{c[0]},{c[1]}" for c in moved)

def free_key(cells):
    best = ""
    for t in range(8):
        moved = []
        for c in cells:
            x = -c[0] if t % 2 == 1 else c[0]
            y = -c[1] if (t // 2) % 2 == 1 else c[1]
            moved.append([y, x] if t >= 4 else [x, y])
        k = key_of(moved)
        if best == "" or k < best:
            best = k
    return best

level = {"0,0": [[0, 0]]}
print("size 1: 1 fixed, 1 free")
for size in range(2, 8):
    nxt = {}
    for k, cells in level.items():
        for c in cells:
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                cell = [c[0] + d[0], c[1] + d[1]]
                if cell not in cells:
                    grown = cells + [cell]
                    gk = key_of(grown)
                    if gk not in nxt:
                        nxt[gk] = grown
    free = set()
    for name, shape in nxt.items():
        free.add(free_key(shape))
    print(f"size {size}: {len(nxt)} fixed, {len(free)} free")
    level = nxt
