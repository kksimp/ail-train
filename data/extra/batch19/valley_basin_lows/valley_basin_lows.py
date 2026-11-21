def height(g, r, c):
    return 9 if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]) else g[r][c]

def basin(g, r0, c0):
    seen = {r0 * 100 + c0}; queue = [[r0, c0]]
    while queue:
        p = queue.pop()
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r = p[0] + d[0]; c = p[1] + d[1]
            if height(g, r, c) < 9 and r * 100 + c not in seen:
                seen.add(r * 100 + c); queue.append([r, c])
    return len(seen)

rows = ["3318931946", "3669451918", "2449233914", "9999995799", "2552961794", "4187922987"]
g = [[int(ch) for ch in r] for r in rows]
risk = 0; sizes = []
for r in range(len(g)):
    for c in range(len(g[0])):
        h = g[r][c]
        if h < height(g, r - 1, c) and h < height(g, r + 1, c) and h < height(g, r, c - 1) and h < height(g, r, c + 1):
            size = basin(g, r, c)
            print(f"low point {h} at ({r},{c}), basin of {size}")
            risk += h + 1; sizes.append(size)
print(f"part 1: risk level {risk}")
top = sorted(sizes, reverse=True)
print(f"part 2: {top[0]} x {top[1]} x {top[2]} = {top[0] * top[1] * top[2]}")
