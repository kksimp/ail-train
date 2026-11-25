import sys


def number(s):
    if s == "" or len(s) > 6 or not all(c in "0123456789" for c in s):
        return None
    return int(s)


def money(c):
    return f"{c // 100}.{c % 100:02d}"


def ceil_div(a, b):
    return -(-a // b)


cents = {}
per = {}
recipes = []
for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    w = line.split()
    if not w:
        continue
    last = number(w[-1]) if len(w) >= 3 else None
    if last is None:
        last = 0
    if w[0] == "price" and len(w) == 4 and number(w[2]) is not None and last > 0:
        cents[w[1]] = number(w[2])
        per[w[1]] = last
    elif w[0] == "recipe" and len(w) == 3 and last > 0:
        recipes.append([w[1], last, []])
    elif w[0] == "use" and len(w) == 3 and last > 0:
        if not recipes:
            print(f"line {k}: no recipe")
        else:
            recipes[-1][2].append((w[1], last))
    else:
        print(f"line {k}: bad line")
best_name = ""
best = -1
for name, servings, uses in recipes:
    total = 0
    missing = []
    for item, qty in uses:
        if item in cents:
            total += ceil_div(qty * cents[item], per[item])
        elif item not in missing:
            missing.append(item)
    if missing:
        print(f"{name}: missing {', '.join(missing)}")
        continue
    ps = ceil_div(total, servings)
    print(f"{name}: total {money(total)}, per serving {money(ps)}")
    if ps > best:
        best = ps
        best_name = name
if best >= 0:
    print(f"most expensive per serving: {best_name}")
