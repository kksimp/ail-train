def disc(c, b):
    if c.startswith("SAVE"):
        r = c[4:]
        if not r or not r.isdigit(): return None
        p = int(r)
        if p < 5 or p > 50: return None
        return b * p // 100
    if c == "SHIP-FREE": return 495
    return None
b = 6480; best = 0; bc = "none"
for c in ["SAVE15", "SAVE", "SHIP-FREE", "SAVE80", "save10", "SAVE5", "WELCOME"]:
    d = disc(c, b)
    if d is not None:
        print(f"{c:<10} takes off {d // 100}.{d % 100:02}")
        if d > best: best = d; bc = c
    else: print(f"{c:<10} rejected")
pay = b - best
print(f"best code {bc}: pay {pay // 100}.{pay % 100:02}")
