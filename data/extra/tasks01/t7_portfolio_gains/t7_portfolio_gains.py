import sys

def money(c):
    s = "-" if c < 0 else ""
    a = abs(c)
    return f"{s}{a // 100}.{a % 100:02d}"

def digits(s):
    return s.isascii() and s.isdigit()

pos = {}
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    w = line.rstrip("\r").split()
    if not w:
        continue
    kind = w[0]
    ok = (kind in ("BUY", "SELL") and len(w) == 4 and digits(w[2]) and digits(w[3]) and int(w[2]) >= 1) or \
         (kind == "MARK" and len(w) == 3 and digits(w[2]))
    if not ok:
        print(f"line {i}: invalid")
        continue
    sym = w[1]
    p = pos.setdefault(sym, {"qty": 0, "cost": 0, "real": 0, "last": 0, "mark": None})
    if kind == "MARK":
        p["mark"] = int(w[2])
        continue
    q = int(w[2])
    price = int(w[3])
    if kind == "BUY":
        p["qty"] += q
        p["cost"] += q * price
        p["last"] = price
    else:
        if q > p["qty"]:
            print(f"line {i}: oversell")
            continue
        removed = p["cost"] * q // p["qty"]
        p["real"] += q * price - removed
        p["cost"] -= removed
        p["qty"] -= q
        p["last"] = price

tc = tv = tr = 0
for sym in sorted(pos, key=lambda s: s.encode()):
    p = pos[sym]
    cur = p["mark"] if p["mark"] is not None else p["last"]
    value = p["qty"] * cur
    print(f"{sym}: qty={p['qty']} cost={money(p['cost'])} value={money(value)} unrealized={money(value - p['cost'])} realized={money(p['real'])}")
    tc += p["cost"]
    tv += value
    tr += p["real"]
print(f"total: cost={money(tc)} value={money(tv)} unrealized={money(tv - tc)} realized={money(tr)}")
