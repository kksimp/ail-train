def mul(s, o):
    a, b, c, d = s
    oa, ob, oc, od = o
    return (a * oa + b * oc, a * ob + b * od, c * oa + d * oc, c * ob + d * od)
def apply(t, p):
    return (t[0] * p[0] + t[1] * p[1], t[2] * p[0] + t[3] * p[1])
def show(t, pts):
    return " ".join(f"({x}, {y})" for x, y in (apply(t, p) for p in pts))
arrow = [(2, 0), (0, 1), (0, -1)]
q = (0, -1, 1, 0); flip = (-1, 0, 0, 1); ident = (1, 0, 0, 1)
for name, t in [("as drawn", ident), ("quarter", q), ("half", mul(q, q)), ("flip", flip), ("flip, then quarter", mul(q, flip))]:
    print(f"{name:<18} {show(t, arrow)}")
acc = q; k = 1
while acc != ident:
    acc = mul(acc, q); k += 1
print(f"quarter turns until back: {k}")
print(f"flip twice is identity: {'true' if mul(flip, flip) == ident else 'false'}")
