def flight(vx, vy, zone):
    x = y = 0; top = 0
    while x <= zone[1] and y >= zone[2]:
        x += vx; y += vy
        if vx > 0: vx -= 1
        vy -= 1
        top = max(top, y)
        if zone[0] <= x <= zone[1] and zone[2] <= y <= zone[3]:
            return top
    return -1

zone = [15, 22, -9, -4]
print(f"target zone x {zone[0]}..{zone[1]}, y {zone[2]}..{zone[3]}")
best = -1; best_v = ""; hits = 0
for vx in range(zone[1] + 1):
    for vy in range(zone[2], -zone[2] + 1):
        h = flight(vx, vy, zone)
        if h >= 0:
            hits += 1
            if h > best:
                best = h; best_v = f"{vx},{vy}"
print(f"part 1: highest arc {best} with velocity {best_v}")
print(f"part 2: {hits} launch velocities hit the zone")
