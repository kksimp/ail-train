pairs = [("Stats 2", "Stats 1"), ("ML", "Stats 2"), ("ML", "Linear Algebra"), ("Data Viz", "Stats 1"), ("Graphics", "Linear Algebra"), ("Robotics", "ML"), ("Robotics", "Mechanics")]
unlocks = {}; needs = {}
for c, p in pairs:
    unlocks.setdefault(p, []).append(c)
    needs.setdefault(c, []).append(p)
for p, cs in unlocks.items():
    print(f"{p} unlocks {', '.join(cs)}")
passed = {"Stats 1", "Linear Algebra"}
op = [c for c, ps in needs.items() if c not in passed and all(p in passed for p in ps)]
print(f"with Stats 1 and Linear Algebra: {', '.join(sorted(op))}")
ranked = sorted(unlocks, key=lambda k: (-len(unlocks[k]), k))
print(f"open the most: {' and '.join(ranked[:2])}")
