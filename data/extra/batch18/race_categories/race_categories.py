field = [("Rosa", "V40", 1512), ("Tom", "Open", 1288), ("Ines", "V50", 1730), ("Kofi", "Open", 1342), ("Lena", "V40", 1460), ("Paul", "V50", 1655), ("Ade", "Open", 1199)]
def clock(s): return f"{s // 60}:{s % 60:02}"
cur = ""; place = 0
for n, c, s in sorted(field, key=lambda f: (f[1], f[2])):
    if c != cur:
        cur = c; place = 0; print(f"== {cur}")
    place += 1
    print(f"{place}. {n:<5} {clock(s)}")
w = min(field, key=lambda f: f[2])
print(f"fastest overall: {w[0]} in {clock(w[2])}")
