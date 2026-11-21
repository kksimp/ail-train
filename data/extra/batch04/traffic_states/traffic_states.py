st = ("red", 2)
def tick(s, b, f):
    if f: return ("flashing", 0)
    k, n = s
    if k == "red": return ("red", n - 1) if n > 1 else ("green", 5)
    if k == "green":
        if b and n > 2: return ("green", 2)
        return ("green", n - 1) if n > 1 else ("amber", 2)
    if k == "amber": return ("amber", n - 1) if n > 1 else ("red", 4)
    return s
for t in range(1, 17):
    st = tick(st, t == 4, t == 15)
    print(f"t={t:>2} " + ("flashing" if st[0] == "flashing" else f"{st[0]} {st[1]}"))
