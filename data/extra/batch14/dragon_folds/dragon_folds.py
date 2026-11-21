def turn(k):
    low = k & (-k)
    return "R" if (k // low) & 2 == 0 else "L"
def unfold(n):
    s = ""
    for i in range(n):
        s = s + "R" + "".join("L" if c == "R" else "R" for c in reversed(s))
    return s
print(f"turns from bits:   {''.join(turn(k) for k in range(1, 16))}")
print(f"turns by unfolding: {unfold(4)}")
for n in [4, 8, 10, 12]:
    x = y = 0
    dx, dy = 1, 0
    edges = set()
    repeats = 0
    segments = 1 << n
    for k in range(1, segments + 1):
        nx, ny = x + dx, y + dy
        key = (x, y, nx, ny) if (x < nx or (x == nx and y < ny)) else (nx, ny, x, y)
        if key in edges:
            repeats += 1
        edges.add(key)
        x, y = nx, ny
        if k < segments:
            if turn(k) == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
    print(f"{segments:>5} segments end at ({x}, {y}), {repeats} edges reused")
