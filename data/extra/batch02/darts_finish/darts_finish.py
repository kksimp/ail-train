th = []
for n in range(1, 21):
    th += [(f"S{n}", n), (f"D{n}", 2 * n), (f"T{n}", 3 * n)]
th += [("SB", 25), ("DB", 50)]
dbl = [t for t in th if t[0].startswith("D")]
def fin(s):
    out = [[d[0]] for d in dbl if d[1] == s]
    out += [[a[0], d[0]] for a in th for d in dbl if a[1] + d[1] == s]
    out += [[a[0], b[0], d[0]] for a in th for b in th for d in dbl if a[1] + b[1] + d[1] == s]
    return out
for s in [2, 40, 50, 99, 170, 169]:
    fs = fin(s)
    print(f"{s}: {len(fs)} finishes, fewest darts {min(map(len, fs)) if fs else 0}")
