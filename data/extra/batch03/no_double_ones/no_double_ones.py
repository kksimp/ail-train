def b(n, p, l, out):
    if len(p) == n: out.append(p); return
    b(n, p + "0", False, out)
    if not l: b(n, p + "1", True, out)
def c(n):
    e0 = e1 = 1
    for _ in range(1, n): e0, e1 = e0 + e1, e0
    return e0 + e1
o = []; b(4, "", False, o)
print(f"length 4: {len(o)}: {' '.join(o)}")
print([c(n) for n in range(1, 13)])
print(f"length 60: {c(60)}")
