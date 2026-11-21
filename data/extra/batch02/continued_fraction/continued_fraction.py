def terms(a, b):
    out = []
    while b: out.append(a // b); a, b = b, a % b
    return out
def conv(ts):
    pp, qp, p, q = 1, 0, ts[0], 1; out = [(p, q)]
    for t in ts[1:]:
        p, pp = t * p + pp, p; q, qp = t * q + qp, q; out.append((p, q))
    return out
for a, b in [(415, 93), (355, 113), (103993, 33102), (13, 8)]:
    ts = terms(a, b)
    print(f"{a}/{b} = {ts}: " + ", ".join(f"{p}/{q}" for p, q in conv(ts)))
g = terms(1597, 987)
print(f"1597/987 has {len(g)} terms, all ones but the last: {str(all(t == 1 for t in g[:-1])).lower()}")
