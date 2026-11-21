def pour(rock, floor, has_floor):
    filled = set(rock); count = 0
    while 2000 not in filled:
        x, y = 20, 0
        moving = True
        while moving:
            if y + 1 == floor:
                if not has_floor:
                    return count
                moving = False
            elif x * 100 + y + 1 not in filled:
                y += 1
            elif (x - 1) * 100 + y + 1 not in filled:
                x -= 1; y += 1
            elif (x + 1) * 100 + y + 1 not in filled:
                x += 1; y += 1
            else:
                moving = False
        filled.add(x * 100 + y); count += 1
    return count

paths = ["14,5 -> 18,5", "22,7 -> 22,4 -> 26,4", "17,10 -> 23,10", "16,7 -> 19,7"]
rock = set(); lowest = 0
for p in paths:
    pts = [[int(v) for v in t.split(",")] for t in p.split(" -> ")]
    for i in range(1, len(pts)):
        a = pts[i - 1]; b = pts[i]
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                rock.add(x * 100 + y); lowest = max(lowest, y)
print(f"{len(rock)} rock cells, lowest ledge at depth {lowest}")
print(f"part 1: {pour(rock, lowest + 2, False)} grains rest before the spill")
print(f"part 2: {pour(rock, lowest + 2, True)} grains until the spout is buried")
