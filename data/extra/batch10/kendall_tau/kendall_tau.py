def compare(a, b):
    c = d = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            s = (a[i] - a[j]) * (b[i] - b[j])
            if s > 0:
                c += 1
            elif s < 0:
                d += 1
    return c, d

entries = ["scones", "tart", "trifle", "eclair", "flapjack", "brownie", "crumble", "muffin"]
judges = {"Ada": [1, 2, 3, 4, 5, 6, 7, 8], "Bo": [2, 1, 4, 3, 6, 5, 8, 7], "Cy": [8, 7, 6, 5, 4, 3, 2, 1], "Di": [3, 1, 6, 2, 8, 4, 7, 5]}
n = len(entries)
print(f"{n} entries, {n * (n - 1) // 2} pairs")
names = ["Ada", "Bo", "Cy", "Di"]
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        c, d = compare(judges[names[i]], judges[names[j]])
        t = float(c - d) / float(n * (n - 1) // 2)
        print(f"{names[i]} vs {names[j]}: {c:>2} agree, {d:>2} disagree, tau {t:>7.4f}")
