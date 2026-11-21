def kolakoski(count):
    s = [1, 2, 2]
    i = 2
    while len(s) < count:
        nxt = 3 - s[-1]
        for _ in range(s[i]):
            s.append(nxt)
        i += 1
    return s[:count]

def run_lengths(xs):
    out = []
    run = 1
    for i in range(1, len(xs)):
        if xs[i] == xs[i - 1]:
            run += 1
        else:
            out.append(run)
            run = 1
    out.append(run)
    return out

s = kolakoski(40)
print(f"first 40: {''.join(str(x) for x in s)}")
runs = run_lengths(s)
whole = len(runs) - 1
same = runs[:whole] == s[:whole]
print(f"run lengths: {''.join(str(x) for x in runs)}")
print(f"complete runs repeat the sequence: {str(same).lower()}")
for n in [100, 1000, 10000, 100000]:
    k = kolakoski(n)
    ones = k.count(1)
    share = float(ones) / float(n)
    print(f"first {n:>6}: {ones} ones, share {share:.4f}")
