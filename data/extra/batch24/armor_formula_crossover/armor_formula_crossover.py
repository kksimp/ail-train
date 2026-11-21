def flat(hit, armour): return max(hit - armour, 1)
def percent(hit, armour): return hit * 100 // (100 + 4 * armour)
armour = 10; cross = -1
for hit in [4, 8, 12, 16, 20, 25, 30, 35, 40, 50, 60]:
    f = flat(hit, armour); p = percent(hit, armour)
    better = "flat" if f < p else "percent" if p < f else "same"
    print(f"hit {hit:>2}: flat lets {f:>2} through, percent {p:>2} -> {better}")
    if cross < 0 and p < f: cross = hit
print(f"percentage armour wins from hits of {cross} upwards")
