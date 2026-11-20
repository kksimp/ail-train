key = "BCADDACB"
sheets = [("Ama", "BCADDACB"), ("Bo", "BCDDDACA"), ("Cy", "ACADBACB"), ("Di", "BCA")]
misses = {}
for name, ans in sheets:
    got = sum(1 for k, a in zip(key, ans) if k == a)
    pct = got * 100 // len(key)
    print(f"{name:<4}{got}/{len(key)} {pct:>3}%")
    for i, (k, a) in enumerate(zip(key, ans)):
        if k != a:
            misses[i + 1] = misses.get(i + 1, 0) + 1
hard = sorted(misses, key=lambda q: (-misses[q], q))
print("hardest: " + " ".join(f"Q{q}" for q in hard[:2]))
print(f"unanswered by Di: {len(key) - len(sheets[3][1])}")
