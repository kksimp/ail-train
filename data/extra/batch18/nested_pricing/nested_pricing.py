def euros(c): return f"{c // 100}.{c % 100:02}"
def total(p):
    k = p[0]
    if k == "f": return p[1]
    if k == "kg": return p[1] * p[2] // 1000
    if k == "b": return sum(total(x) for x in p[1])
    full = total(p[2]); return full - full * p[1] // 100
def depth(p):
    if p[0] == "b": return 1 + max(depth(x) for x in p[1])
    if p[0] == "off": return 1 + depth(p[2])
    return 1
cheese = ("kg", 2400, 350); olives = ("kg", 1290, 200); bread = ("f", 320)
picnic = ("off", 10, ("b", [cheese, olives, bread]))
for n, p in [("cheese", cheese), ("olives", olives), ("bread", bread), ("picnic box", picnic), ("two boxes", ("b", [picnic, picnic]))]:
    print(f"{n:<10} {euros(total(p)):>6} (depth {depth(p)})")
