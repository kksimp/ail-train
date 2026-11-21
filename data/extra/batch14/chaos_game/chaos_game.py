corners = [[0, 0], [1024, 0], [512, 1024]]
seed = 2026
x, y = 300, 700
grid = [[False] * 32 for r in range(13)]
in_hole = 0
for step in range(6000):
    seed = (seed * 1103515245 + 12345) % 2147483648
    k = (seed >> 16) % 3
    x = (x + corners[k][0]) // 2
    y = (y + corners[k][1]) // 2
    if step >= 20:
        grid[12 - y * 13 // 1025][x * 32 // 1025] = True
        if y > 16 and y < 496 and abs(2 * x - 1024) < y - 16:
            in_hole += 1
lit = 0
for r in range(13):
    print("".join("#" if b else "." for b in grid[r]))
    lit += sum(1 for b in grid[r] if b)
print(f"{lit} of 416 cells lit, {in_hole} points inside the central hole")
