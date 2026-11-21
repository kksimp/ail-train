def reactions(span, loads):
    total = 0.0
    for at, kn in loads:
        total = total + kn
    acc = 0.0
    for at, kn in loads:
        acc = acc + kn * at
    rb = acc / span
    return [total - rb, rb]

def shear(x, ra, loads):
    acc = 0.0
    for at, kn in loads:
        if at <= x:
            acc = acc + kn
    return ra - acc

def moment(x, ra, loads):
    acc = 0.0
    for at, kn in loads:
        if at < x:
            acc = acc + kn * (x - at)
    return ra * x - acc

span = 6.0
loads = [(1.5, 10.0), (4.0, 6.0)]
r = reactions(span, loads)
print(f"reactions: A {r[0]:.2f} kN, B {r[1]:.2f} kN")
best = 0.0
best_x = 0.0
for i in range(13):
    x = float(i) * 0.5
    v = shear(x, r[0], loads)
    m = moment(x, r[0], loads)
    if m > best:
        best = m
        best_x = x
    bar = "#" * int(round(m / 2.0))
    print(f"x {x:.1f} m: V {v:>6.2f} kN, M {m:>6.2f} kN m |{bar}")
print(f"largest moment {best:.2f} kN m at {best_x} m")
