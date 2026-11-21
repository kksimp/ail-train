def penalty(over):
    for top, f, p in zip([10, 20, 30], [0, 100, 250], [0, 3, 4]):
        if over <= top: return [f, p]
    return [500, 6]
pts = {}
for plate, limit, speed in [("AB1", 50, 54), ("CD2", 50, 63), ("AB1", 30, 49), ("EF3", 80, 112), ("CD2", 100, 128), ("GH4", 30, 36)]:
    allowed = limit + limit * 10 // 100 + 2
    pts.setdefault(plate, 0)
    if speed <= allowed:
        print(f"{plate} {speed} in a {limit}: within tolerance"); continue
    p = penalty(speed - limit)
    pts[plate] += p[1]
    action = "warning letter" if p[0] == 0 else f"fine {p[0]}, {p[1]} points"
    print(f"{plate} {speed} in a {limit}: {speed - limit} over, {action}")
for plate, n in pts.items():
    print(f"{plate}: {n} points{' - driving ban' if n >= 6 else ''}")
