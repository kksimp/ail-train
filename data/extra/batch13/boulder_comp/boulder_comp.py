climbers = [("Garnbret", [1, 2, 0, 1], [1, 1, 3, 1]), ("Mori", [2, 1, 0, 3], [1, 1, 2, 2]), ("Pilz", [1, 0, 0, 2], [1, 4, 1, 1]), ("Raboutou", [3, 2, 0, 1], [2, 1, 1, 1]), ("Meul", [0, 0, 2, 0], [5, 2, 1, 3])]

def key(c):
    tops, zones = c[1], c[2]
    t = sum(1 for a in tops if a > 0)
    z = sum(1 for a in zones if a > 0)
    ta = sum(a for a in tops if a > 0)
    za = sum(a for a in zones if a > 0)
    return [-t, -z, ta, za]

ranked = sorted(climbers, key=key)
print("place climber    T  Z  TA  ZA")
for i, c in enumerate(ranked):
    k = key(c)
    print(f"{i + 1:>5} {c[0]:<9} {-k[0]:>2} {-k[1]:>2} {k[2]:>3} {k[3]:>3}")
hardest = sorted([0, 1, 2, 3], key=lambda p: sum(1 for c in climbers if c[1][p] > 0))[0]
print(f"problem {hardest + 1} was topped least")
