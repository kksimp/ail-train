def compose(a, b):
    return [a[b[i]] for i in range(6)]
def rotations():
    turn = [0, 1, 5, 4, 2, 3]
    roll = [5, 4, 2, 3, 0, 1]
    group = [[0, 1, 2, 3, 4, 5]]
    seen = {str(group[0])}
    i = 0
    while i < len(group):
        for g in [turn, roll]:
            c = compose(g, group[i])
            if str(c) not in seen:
                seen.add(str(c))
                group.append(c)
        i += 1
    return group
def brute(k, group):
    total = k ** 6
    canon = set()
    for code in range(total):
        cols = []
        rest = code
        for i in range(6):
            cols.append(rest % k)
            rest //= k
        best = total
        for g in group:
            moved = [0] * 6
            for f in range(6):
                moved[g[f]] = cols[f]
            c = 0
            for f in range(6):
                c = c * k + moved[5 - f]
            best = min(best, c)
        canon.add(best)
    return len(canon)
def burnside(k):
    return (k ** 6 + 3 * k ** 4 + 12 * k ** 3 + 8 * k ** 2) // 24
group = rotations()
print(f"rotation group of the cube has {len(group)} elements")
for k in range(1, 6):
    print(f"{k} colours: {burnside(k)} distinct cubes")
for k in range(2, 4):
    print(f"brute force with {k} colours: {brute(k, group)}")
