import sys


def number(s):
    if s == "" or len(s) > 6 or not all(c in "0123456789" for c in s):
        return None
    return int(s)


stock = {}
rates = {}
used = {}
order = []
revenue = 0
for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    w = line.split()
    if not w:
        continue
    cmd = w[0]
    n = number(w[-1]) if len(w) >= 3 else None
    shape_ok = False
    if n is not None:
        if len(w) == 3 and cmd in ("inventory", "rate"):
            shape_ok = True
        elif len(w) == 4 and cmd == "book" and n > 0:
            shape_ok = True
    if not shape_ok:
        print(f"line {k}: bad line")
    elif cmd == "inventory":
        if w[1] not in stock:
            order.append(w[1])
        stock[w[1]] = n
    elif cmd == "rate":
        rates[w[1]] = n
    else:
        guest, t = w[1], w[2]
        if t not in stock or t not in rates:
            print(f"line {k}: unknown type {t}")
        elif used.get(t, 0) >= stock[t]:
            print(f"{guest}: no {t} room free")
        else:
            used[t] = used.get(t, 0) + 1
            gross = n * rates[t]
            cost = gross - gross // 10 if n >= 7 else gross
            revenue += cost
            print(f"{guest}: {t}-{used[t]}, {n} nights, {cost}")
for t in order:
    print(f"{t}: {used.get(t, 0)}/{stock[t]}")
print(f"revenue: {revenue}")
