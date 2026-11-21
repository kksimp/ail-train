def ap(t, p, o, m, pf):
    if pf:
        t = t * (100 - p) // 100
        if t >= m: t -= o
    else:
        if t >= m: t -= o
        t = t * (100 - p) // 100
    return t
def ce(c): return f"{c // 100}.{c % 100:02}"
for t, p, o, m in [(5000, 20, 1000, 4000), (4500, 10, 500, 4500), (12000, 25, 1500, 10000), (3000, 15, 700, 2000)]:
    a = ap(t, p, o, m, True); b = ap(t, p, o, m, False)
    print(f"{ce(t)} with {p}% and {ce(o)} off (min {ce(m)}): {ce(a)} vs {ce(b)}, {'percent first' if a <= b else 'fixed first'}")
