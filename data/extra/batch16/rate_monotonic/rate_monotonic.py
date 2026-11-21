def response(cs, ts, i):
    r = cs[i]
    prev = -1
    while r != prev and r <= ts[i]:
        prev = r
        nxt = cs[i]
        for j in range(i):
            nxt += (prev + ts[j] - 1) // ts[j] * cs[j]
        r = nxt
    return r

def check(label, cs, ts):
    n = len(cs)
    u = 0.0
    for i in range(n):
        u += float(cs[i]) / float(ts[i])
    bound = float(n) * (2.0 ** (1.0 / float(n)) - 1.0)
    verdict = "safe by the bound" if u <= bound else "bound inconclusive"
    print(f"{label}: utilisation {u:.3f}, bound {bound:.3f}, {verdict}")
    for i in range(n):
        r = response(cs, ts, i)
        ok = "meets" if r <= ts[i] else "MISSES"
        print(f"  task C={cs[i]} T={ts[i]:<2} response {r:>2} {ok} its deadline")

check("set 1", [1, 2, 3], [4, 6, 12])
check("set 2", [2, 2, 3], [5, 7, 10])
check("set 3", [1, 1], [4, 5])
