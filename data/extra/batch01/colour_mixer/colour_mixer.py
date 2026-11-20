def ph(t):
    if not t.startswith("#") or len(t) != 7:
        return None
    return tuple(int(t[i:i + 2], 16) for i in (1, 3, 5))
def hx(c):
    return "#" + "".join(f"{x:02x}" for x in c)
for a, b in [("#ff0000", "#0000ff"), ("#123456", "#abcdef"), ("#000000", "#ffffff"), ("#fff", "#000000")]:
    ca, cb = ph(a), ph(b)
    if ca is None:
        print(f"bad colour {a}"); continue
    if cb is None:
        print(f"bad colour {b}"); continue
    m = tuple((x + y) // 2 for x, y in zip(ca, cb))
    t = tuple(x + (255 - x) * 50 // 100 for x in m)
    print(f"{a} + {b} = {hx(m)}, tint 50% {hx(t)}")
c = ph("#0A0b0C")
print(f"Rgb(r: {c[0]}, g: {c[1]}, b: {c[2]})")
