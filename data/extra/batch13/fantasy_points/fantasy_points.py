week = [("Quarterback A", 312, 3, 1, 18, 0, 0), ("Runner B", 0, 0, 0, 124, 1, 3), ("Receiver C", 0, 0, 0, 96, 1, 9), ("Tight end D", 0, 0, 0, 58, 0, 7)]

def score(l, per_catch):
    return l[1] // 25 + l[2] * 4 - l[3] * 2 + l[4] // 10 + l[5] * 6 + l[6] * per_catch

for label, per in [("standard", 0), ("PPR", 1)]:
    ranked = sorted(week, key=lambda l: -score(l, per))
    parts = [f"{l[0]} {score(l, per)}" for l in ranked]
    print(f"{label}: {', '.join(parts)}")
print("catches make the difference for Receiver C and Tight end D")
