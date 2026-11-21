towns = ["Ash", "Birch", "Cedar", "Dale", "Elm", "Fir", "Gorse"]
roads = [(0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)]
parent = list(range(7))
def root(x):
    while parent[x] != x: x = parent[x]
    return x
total = built = 0
for r in sorted(roads, key=lambda r: (r[2], r[0], r[1])):
    a = root(r[0]); b = root(r[1])
    if a == b: print(f"skip {towns[r[0]]}-{towns[r[1]]} ({r[2]} km): would close a loop")
    elif built < 6:
        parent[a] = b; total += r[2]; built += 1; print(f"build {towns[r[0]]}-{towns[r[1]]} ({r[2]} km)")
print(f"{built} roads, {total} km in all")
