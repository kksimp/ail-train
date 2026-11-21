def ride(g, r, c):
    seen = set(); steps = 0
    while True:
        if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]):
            return ("Out", steps)
        if g[r][c] == '.':
            return ("Parked", steps)
        k = r * 100 + c
        if k in seen:
            return ("Looped", steps)
        seen.add(k)
        ch = g[r][c]
        if ch == '>': c += 1
        elif ch == '<': c -= 1
        elif ch == '^': r -= 1
        else: r += 1
        steps += 1

lines = ["v>v<.^", "^.v>v^", "^<<.v<", "v>^>>v", "<>>v<."]
g = [list(l) for l in lines]
for c in range(len(g[0])):
    k, s = ride(g, 0, c)
    words = {"Out": "leaves the floor", "Parked": "parks", "Looped": "loops"}[k]
    print(f"parcel dropped at top col {c}: {words} after {s} moves")
best = -1; at = ""
for r in range(len(g)):
    for c in range(len(g[0])):
        k, s = ride(g, r, c)
        if s > best:
            best = s; at = f"row {r} col {c}"
print(f"part 2: longest ride is {best} moves, starting at {at}")
