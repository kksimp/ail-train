def wt(c, p): return (c * (100 + p) + 50) // 100
def show(c): return f"{c // 100}.{c % 100:02d}"
for c, p, n in [(8650, 15, 3), (12000, 10, 4), (999, 20, 7), (4321, 0, 2)]:
    t = wt(c, p)
    base, extra = divmod(t, n)
    s = [base + (1 if i < extra else 0) for i in range(n)]
    print(f"{show(c)} +{p}% = {show(t)}: " + " ".join(show(x) for x in s))
