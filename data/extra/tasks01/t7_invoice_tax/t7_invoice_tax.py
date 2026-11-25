import sys

RATES = {"A": 0, "B": 500, "C": 825, "D": 1000}

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def num(s, lo):
    s = s.strip()
    if not s.isascii() or not s.isdigit():
        return None
    v = int(s)
    return v if v >= lo else None

sub = 0
tax = {}
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = line.split(",")
    ok = len(f) == 4 and f[0].strip() != ""
    if ok:
        q = num(f[1], 1)
        u = num(f[2], 0)
        code = f[3].strip()
        ok = q is not None and u is not None and code in RATES
    if not ok:
        print(f"line {i}: invalid")
        continue
    net = q * u
    t = (net * RATES[code] + 5000) // 10000
    print(f"{f[0].strip()}: net={money(net)} tax={money(t)} ({code})")
    sub += net
    tax[code] = tax.get(code, 0) + t
print(f"subtotal: {money(sub)}")
for c in sorted(tax):
    print(f"tax {c}: {money(tax[c])}")
print(f"total: {money(sub + sum(tax.values()))}")
