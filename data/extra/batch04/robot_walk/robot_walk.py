D = [(0, 1), (1, 0), (0, -1), (-1, 0)]; N = ["north", "east", "south", "west"]
for cm in ["FFRFFLFRRFFF", "FLFLFLFL", "FFFRBBLFF"]:
    x = y = h = f = 0
    for c in cm:
        if c == "L": h = (h + 3) % 4
        elif c == "R": h = (h + 1) % 4
        else: s = 1 if c == "F" else -1; x += D[h][0] * s; y += D[h][1] * s; f = max(f, abs(x) + abs(y))
    print(f"{cm}: at ({x}, {y}) facing {N[h]}, furthest {f}")
