import sys

RATES = {"USD": 10000, "EUR": 9200, "GBP": 7900, "JPY": 1500000, "CAD": 13600}

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def conv(a, f, t):
    return (2 * a * RATES[t] + RATES[f]) // (2 * RATES[f])

def digits(s):
    return s.isascii() and s.isdigit()

totals = {}
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    w = line.rstrip("\r").split()
    if not w:
        continue
    if w[0] == "table" and len(w) == 3 and digits(w[1]):
        if w[2] not in RATES:
            print(f"line {i}: unknown currency")
            continue
        a = int(w[1])
        print(f"{money(a)} {w[2]}:")
        for c in sorted(RATES):
            print(f"  {c}: {money(conv(a, w[2], c))}")
        continue
    if len(w) != 3 or not digits(w[0]):
        print(f"line {i}: invalid")
        continue
    if w[1] not in RATES or w[2] not in RATES:
        print(f"line {i}: unknown currency")
        continue
    a = int(w[0])
    r = conv(a, w[1], w[2])
    print(f"{money(a)} {w[1]} = {money(r)} {w[2]}")
    totals[w[2]] = totals.get(w[2], 0) + r
for c in sorted(totals):
    print(f"total {c}: {money(totals[c])}")
