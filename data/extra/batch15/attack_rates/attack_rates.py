def rate(ill, well): return float(ill) / float(ill + well) * 100.0
dishes = [("chicken salad", 38, 12, 9, 41), ("rice", 30, 30, 17, 23), ("fruit tart", 21, 25, 26, 28), ("garlic bread", 35, 37, 12, 16), ("ice cream", 18, 26, 29, 27)]
best = dishes[0][0]; best_ratio = 0.0
for d in dishes:
    a = rate(d[1], d[2]); b = rate(d[3], d[4])
    ratio = a / b
    if ratio > best_ratio:
        best_ratio = ratio; best = d[0]
    print(f"{d[0]:<14} ate {a:>5.1f}%, did not eat {b:>5.1f}%, ratio {ratio:.2f}")
d = dishes[0]
guests = d[1] + d[2] + d[3] + d[4]
ill = d[1] + d[3]
print(f"{ill} of {guests} guests ill, overall attack rate {rate(ill, guests - ill):.1f}%")
print(f"likely source: {best}")
