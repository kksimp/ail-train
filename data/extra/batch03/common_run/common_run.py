def ls(a, b):
    t = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]; best = e = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
                if t[i][j] > best: best = t[i][j]; e = i
    return a[e - best:e]
for x, y in [("the quick brown fox jumps over the lazy dog", "a quick brown fox jumps high"), ("we will meet at the old mill at noon", "meet me at the old mill tomorrow"), ("red green blue", "cyan magenta yellow")]:
    r = ls(x.split(" "), y.split(" "))
    print("nothing shared" if not r else f"{len(r)} words: {' '.join(r)}")
