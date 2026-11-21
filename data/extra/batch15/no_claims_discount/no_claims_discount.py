def next_level(level, claimed):
    if claimed: return max(level - 2, 0)
    return min(level + 1, 3)
discounts = [0, 20, 40, 60]
base = 900
history = [False, False, True, False, False, False, True, True, False, False]
level = 0; paid = 0
for i, claimed in enumerate(history):
    premium = base * (100 - discounts[level]) // 100
    paid += premium
    mark = "claim" if claimed else "clean"
    print(f"year {i + 1:>2}: level {level} ({discounts[level]}% off) pays {premium}, {mark}")
    level = next_level(level, claimed)
print(f"paid {paid} over {len(history)} years")
share = [1.0, 0.0, 0.0, 0.0]
for step in range(40):
    nxt = [0.0] * 4
    for l in range(4):
        nxt[next_level(l, True)] += share[l] * 0.1
        nxt[next_level(l, False)] += share[l] * 0.9
    share = nxt
avg = 0.0
for l in range(4):
    avg += share[l] * float(base * (100 - discounts[l]) // 100)
print(f"long run shares {share[0]:.3f} {share[1]:.3f} {share[2]:.3f} {share[3]:.3f}, average premium {avg:.2f}")
