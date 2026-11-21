def charge(a, l):
    if l < a: return None, "leaves before arriving"
    if l >= 1440: return None, "past midnight"
    s = l - a
    if s <= 20: return 0, None
    return min(((s + 29) // 30) * 150, 1200), None
ck = lambda m: f"{m // 60:02d}:{m % 60:02d}"
t = 0
for a, l in [(540, 555), (540, 600), (545, 640), (480, 1200), (700, 650), (1000, 1500)]:
    c, e = charge(a, l)
    if e: print(f"{ck(a)}: rejected ({e})")
    else:
        t += c; print(f"{ck(a)}-{ck(l)}: {c // 100}.{c % 100:02d}")
print(f"takings {t // 100}.{t % 100:02d}")
