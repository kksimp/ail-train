import sys

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def signed(c):
    if c > 0:
        return "+" + money(c)
    if c < 0:
        return "-" + money(-c)
    return "0.00"

bal = {}
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = [x.strip() for x in line.split(",")]
    ok = len(f) == 3 and f[0] != "" and f[1].isascii() and f[1].isdigit() and int(f[1]) >= 1
    if ok:
        ps = [x.strip() for x in f[2].split(";")]
        ok = all(p != "" for p in ps) and len(set(ps)) == len(ps)
    if not ok:
        print(f"line {i}: invalid")
        continue
    amt = int(f[1])
    k = len(ps)
    bal[f[0]] = bal.get(f[0], 0) + amt
    for j, p in enumerate(ps):
        owe = amt // k + (1 if j < amt % k else 0)
        bal[p] = bal.get(p, 0) - owe

names = sorted(bal, key=lambda s: s.encode())
print("balances:")
for n in names:
    print(f"  {n}: {signed(bal[n])}")
print("settlements:")
done = False
any_ = False
while True:
    d = None
    c = None
    for n in names:
        if bal[n] < 0 and (d is None or bal[n] < bal[d]):
            d = n
        if bal[n] > 0 and (c is None or bal[n] > bal[c]):
            c = n
    if d is None or c is None:
        break
    x = min(-bal[d], bal[c])
    print(f"  {d} pays {c} {money(x)}")
    bal[d] += x
    bal[c] -= x
    any_ = True
if not any_:
    print("  none")
