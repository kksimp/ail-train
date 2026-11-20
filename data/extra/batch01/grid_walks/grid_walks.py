D = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
for walk in ["NNEESW", "EEEENNNNWWWWSSSS", "NXNXS", ""]:
    x = y = far = 0; vis = {(0, 0)}
    for c in walk:
        dx, dy = D.get(c, (0, 0)); x += dx; y += dy
        vis.add((x, y)); far = max(far, abs(x) + abs(y))
    print(f"'{walk}': ends at ({x}, {y}), distance {abs(x) + abs(y)}, farthest {far}, {len(vis)} cells")
