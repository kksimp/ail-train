import sys


def num(s, lo):
    if s and all(c in "0123456789" for c in s) and int(s) >= lo:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    bad = []
    coupons = []
    sub = 0
    units = 0
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "item" and len(f) == 4 and f[1] and num(f[2], 0) is not None and num(f[3], 1):
            sub += num(f[2], 0) * num(f[3], 1)
            units += num(f[3], 1)
        elif f[0] == "coupon" and len(f) == 2 and f[1]:
            coupons.append(f[1])
        else:
            bad.append("bad %d" % k)
    out = bad
    pct = {"SAVE10": 10, "SAVE20": 20, "BULK": 15}
    accepted = set()
    percent = 0
    fixed = 0
    free = False
    for c in coupons:
        why = None
        if c not in ("SAVE10", "SAVE20", "BULK", "FIVER", "FREESHIP"):
            why = "unknown"
        elif c in accepted:
            why = "duplicate"
        elif c in pct and percent:
            why = "conflict"
        elif c == "SAVE20" and sub < 10000:
            why = "minimum"
        elif c == "FIVER" and sub < 2000:
            why = "minimum"
        elif c == "BULK" and units < 10:
            why = "units"
        if why:
            out.append("%s rejected %s" % (c, why))
            continue
        accepted.add(c)
        if c in pct:
            percent = pct[c]
        elif c == "FIVER":
            fixed = 500
        else:
            free = True
        out.append(c + " ok")
    disc = min(sub, sub * percent // 100 + fixed)
    ship = 0 if free or sub >= 5000 else 599
    out += ["subtotal %d" % sub, "discount %d" % disc, "shipping %d" % ship, "total %d" % (sub - disc + ship)]
    print("\n".join(out))


main()
