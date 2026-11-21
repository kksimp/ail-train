def power(mine, theirs):
    mult = [[2, 4, 1], [1, 2, 4], [4, 1, 2]]
    return sum(mine[i] * theirs[j] * mult[i][j] for i in range(3) for j in range(3))
def edges(mine, mixes): return [power(mine, e) - power(e, mine) for e in mixes]
def worst(mine, mixes): return min(edges(mine, mixes))
mixes = [[10, 6, 4], [4, 10, 6], [12, 2, 6]]
options = [[s, h, 20 - s - h] for s in range(21) for h in range(21 - s)]
ranked = sorted(options, key=lambda a: -worst(a, mixes))
for k in range(4):
    a = ranked[k]
    print(f"{a[0]:>2} spear, {a[1]:>2} horse, {a[2]:>2} bow: edges {edges(a, mixes)}, worst {worst(a, mixes)}")
bows = [0, 0, 20]
print(f"all bows: edges {edges(bows, mixes)}, worst {worst(bows, mixes)}")
