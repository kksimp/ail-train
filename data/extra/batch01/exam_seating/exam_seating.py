names = ["Ada", "Ben", "Cal", "Dee", "Eli", "Fay", "Gus", "Hal", "Ivy"]
rows, cols = 4, 4
g = [["."] * cols for _ in range(rows)]
i = 0
for r in range(rows):
    for c in range(cols):
        if (r + c) % 2 == 1 or i >= len(names):
            continue
        g[r][c] = names[i]; i += 1
for r in range(rows):
    print("".join(s.ljust(4) for s in g[r]).rstrip())
for who in ["Eli", "Ivy", "Zoe"]:
    pos = next(((r, c) for r in range(rows) for c in range(cols) if g[r][c] == who), None)
    if pos:
        print(f"{who}: row {pos[0] + 1}, seat {pos[1] + 1}")
    else:
        print(f"{who}: no seat")
seated = sum(1 for row in g for s in row if s != ".")
print(f"seated {seated} of {len(names)}")
