def run(steps, size):
    black, pos, d = set(), (size // 2, size // 2), 0
    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for _ in range(steps):
        if pos in black:
            d = (d + 3) % 4; black.remove(pos)
        else:
            d = (d + 1) % 4; black.add(pos)
        pos = ((pos[0] + mv[d][0]) % size, (pos[1] + mv[d][1]) % size)
    return black, pos
black, pos = run(200, 11)
for r in range(11):
    print("".join("A" if (r, c) == pos else "#" if (r, c) in black else "." for c in range(11)))
print(f"black tiles: {len(black)}")
for n in [10, 100, 500]:
    print(f"after {n}: {len(run(n, 41)[0])} black")
