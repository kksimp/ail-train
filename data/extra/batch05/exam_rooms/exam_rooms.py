R = sorted([("Hall", 120), ("Lab A", 30), ("Lab B", 30), ("Room 5", 60), ("Room 6", 45)], key=lambda r: (r[1], r[0])); U = []
for n, c in sorted([("maths", 110), ("chemistry", 28), ("history", 52), ("art", 12), ("physics", 44), ("latin", 9), ("biology", 58)], key=lambda e: (-e[1], e[0])):
    p = next((i for i, r in enumerate(R) if r[1] >= c), -1)
    if p < 0: U.append(n)
    else: r = R.pop(p); print(f"{n} ({c}) -> {r[0]} ({r[1]}, {r[1] - c} spare)")
if U: print(f"next session: {', '.join(U)}")
