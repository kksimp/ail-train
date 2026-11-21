def ancestors(parents, start):
    seen = set()
    todo = [start]
    while todo:
        c = todo.pop()
        if c not in seen:
            seen.add(c)
            for p in parents.get(c, []):
                todo.append(p)
    return seen

def bases(parents, a, b):
    common = ancestors(parents, a) & ancestors(parents, b)
    best = []
    for c in sorted(common):
        covered = any(d != c and c in ancestors(parents, d) for d in common)
        if not covered:
            best.append(c)
    return best

parents = {"c2": ["c1"], "c3": ["c2"], "c4": ["c2"], "c5": ["c3"], "c6": ["c5", "c4"], "c7": ["c4"], "c8": ["c7"], "c9": ["c6"], "c10": ["c5", "c7"], "c11": ["c7", "c5"]}
for pair in [["c9", "c8"], ["c5", "c7"], ["c3", "c9"], ["c10", "c11"]]:
    a, b = pair
    found = " and ".join(bases(parents, a, b))
    ahead = len(ancestors(parents, a) - ancestors(parents, b))
    behind = len(ancestors(parents, b) - ancestors(parents, a))
    print(f"{a:<3} vs {b:<3}: base {found}, {a} has {ahead} commits {b} lacks, {b} has {behind}")
