tray = [[12, 0, 15, 9, 0, 11], [14, 13, 0, 10, 12, 0], [0, 0, 8, 11, 13, 15], [16, 12, 14, 0, 9, 10]]
for r, row in enumerate(tray):
    print(f"row {r + 1}: {sum(1 for h in row if h > 0)}/6 sprouted, tallest {max(row)} mm")
print(f"per column: {[sum(1 for r in range(4) if tray[r][c] > 0) for c in range(6)]}")
resow = []; best = 0; spot = "none"
for r in range(4):
    for c in range(6):
        if tray[r][c] == 0: resow.append(f"r{r + 1}c{c + 1}")
        elif tray[r][c] > best: best = tray[r][c]; spot = f"r{r + 1}c{c + 1}"
print(f"germination {24 - len(resow)} of 24, tallest {best} mm at {spot}")
print(f"resow: {' '.join(resow)}")
