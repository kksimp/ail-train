def zone(x, y):
    if x == 0 and y == 0: return "on the dock"
    if x == 0: return f"against the west wall at y {y}"
    if y == 0: return f"against the south wall at x {x}"
    if x == y: return f"on the diagonal at {x}"
    return "open floor"
d = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
x = y = 0; walls = 0
for m in ["E", "E", "N", "N", "N", "W", "W", "S", "S", "S"]:
    x += d[m][0]; y += d[m][1]
    z = zone(x, y)
    if z.startswith("against"): walls += 1
    print(f"{m} -> ({x}, {y}) {z}")
print(f"touched a wall {walls} times")
