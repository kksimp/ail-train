def strips(w, h):
    return (2 * (w + h) + 12 + 39) // 40

def quarters(n):
    return (n * 25 + 89) // 90

def yards(q):
    whole = q // 4
    frac = {1: "1/4", 2: "1/2", 3: "3/4"}.get(q % 4, "")
    if whole == 0:
        return f"{frac} yd"
    if frac == "":
        return f"{whole} yd"
    return f"{whole} {frac} yd"

total_q = 0
for name, w, h in [("baby", 36, 44), ("lap", 50, 65), ("twin", 66, 90), ("queen", 90, 108), ("runner", 14, 72)]:
    n = strips(w, h)
    qs = quarters(n)
    total_q += qs
    print(f"{name:<6} {w}x{h}: {2 * (w + h) + 12} in of binding, {n} strips, buy {yards(qs)}")
print(f"all five: {yards(total_q)}")
