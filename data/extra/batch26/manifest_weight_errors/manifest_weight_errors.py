def grams(f):
    try:
        n = int(f.strip())
    except ValueError:
        return (None, f"not a number '{f}'")
    if n <= 0: return (None, "weight must be positive")
    return (n, None)
def manifest(lines):
    acc = 0
    for l in lines:
        p = l.split(":")
        if len(p) != 2: return (None, f"no colon in '{l}'")
        w, e = grams(p[1])
        if e: return (None, f"box {p[0]}: {e}")
        acc += w
    return (acc, None)
def shipment(ms):
    acc = 0
    for m in ms:
        w, e = manifest(m)
        if e: return (None, e)
        acc += w
    return (acc, None)
good = ["A1:1200", "A2: 850", "A3:2300"]; typo = ["B1:400", "B2:4OO"]; empty = ["C1:0"]; broken = ["D1 900"]
for m in [good, typo, empty, broken]:
    w, e = manifest(m)
    if e: print(f"manifest rejected: {e}")
    else: print(f"manifest of {len(m)}: {w} g")
t, e = shipment([good, good])
print(f"two good manifests: {t} g")
w, e = shipment([good, typo, broken])
if e:
    print(f"shipment stopped: {e}"); w = 0
print(f"shipment weight {w}")
