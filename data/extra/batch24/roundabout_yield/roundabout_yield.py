cars = [(0, 0, 4), (2, 0, 6), (4, 1, 2), (6, 1, 4), (0, 2, 6), (2, 2, 4), (4, 3, 6), (0, 3, 2), (6, 4, 6), (2, 5, 2)]
ring = [-1] * 8; left = [0] * 8
entered = [-1] * len(cars)
done = 0; waits = [0, 0, 0, 0]; tick = 0
while done < len(cars):
    moved = [-1] * 8; moved_left = [0] * 8
    for cell in range(8):
        if ring[cell] >= 0:
            if left[cell] == 1: done += 1
            else:
                moved[(cell + 1) % 8] = ring[cell]
                moved_left[(cell + 1) % 8] = left[cell] - 1
    ring = moved; left = moved_left
    for e in [0, 2, 4, 6]:
        for i, c in enumerate(cars):
            if c[0] == e and c[1] <= tick and entered[i] < 0:
                if ring[e] < 0 and ring[(e + 7) % 8] < 0:
                    ring[e] = i; left[e] = c[2]; entered[i] = tick
                    waits[e // 2] += tick - c[1]
                break
    tick += 1
for e in range(4):
    print(f"entry at cell {e * 2}: total wait {waits[e]} ticks")
print(f"all {len(cars)} cars through by tick {tick}")
