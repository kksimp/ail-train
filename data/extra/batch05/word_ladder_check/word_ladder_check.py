D = {"cold", "cord", "card", "ward", "warm", "word", "worm", "corm", "core", "care"}
def oa(a, b): return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1
for l in [["cold", "cord", "card", "ward", "warm"], ["cold", "cord", "word", "worm", "warm"], ["cold", "cord", "core", "care", "card"], ["cold", "colt", "cord"], ["cold", "card", "ward"]]:
    v = "ok"
    for i, w in enumerate(l):
        if w not in D: v = f"{w} is not a word"; break
        if i > 0 and not oa(l[i - 1], w): v = f"{l[i - 1]} -> {w} changes more than one letter"; break
    print(f"{' > '.join(l)}: {v}")
