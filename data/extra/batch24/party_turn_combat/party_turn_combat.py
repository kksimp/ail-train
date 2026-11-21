def damage(i, rnd):
    if i == 0: return 9
    if i == 1: return 15 if rnd % 3 == 0 else 5
    return 22 if rnd % 2 == 0 else 0
labels = ["knight", "archer", "mage"]
hp = [60, 35, 30]; boss = 230; dealt = [0, 0, 0]; rnd = 0
while boss > 0 and any(h > 0 for h in hp):
    rnd += 1
    for i in range(3):
        if hp[i] > 0:
            d = damage(i, rnd); boss -= d; dealt[i] += d
    if boss <= 0: break
    target = (rnd - 1) % 3
    while hp[target] <= 0: target = (target + 1) % 3
    hp[target] = max(hp[target] - 14, 0)
    if hp[target] == 0: print(f"turn {rnd}: the {labels[target]} falls")
result = "boss defeated" if boss <= 0 else "party defeated"
print(f"{result} in turn {rnd}, hp left {hp}")
for i in range(3):
    print(f"{labels[i]:<7} dealt {dealt[i]}")
