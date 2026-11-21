F = ["North", "East", "South", "West"]
rocks = {(1, 2), (3, 3), (0, 4)}
x = y = 0; f = 0; ref = 0
for i, c in enumerate("FFRFFLFFFLFFRRF"):
    if c == "L": f = (f + 3) % 4
    elif c == "R": f = (f + 1) % 4
    else:
        dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][f]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 5 and 0 <= ny < 5):
            print(f"step {i + 1}: edge ahead"); ref += 1
        elif (nx, ny) in rocks:
            print(f"step {i + 1}: rock at ({nx}, {ny})"); ref += 1
        else:
            x, y = nx, ny
print(f"ends at ({x}, {y}) facing {F[f]}, {ref} refused")
