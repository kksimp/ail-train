import sys

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def digits(s):
    return s.isascii() and s.isdigit()

def band(g):
    if g <= 500:
        return "S", 500
    if g <= 2000:
        return "M", 900
    if g <= 5000:
        return "L", 1500
    if g <= 20000:
        return "X", 3000
    return "H", 3000 + 200 * ((g - 20000 + 999) // 1000)

PCT = {1: 100, 2: 125, 3: 160}
cnt = {}
sums = {}
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = [x.strip() for x in line.split(",")]
    if len(f) != 3 or f[0] == "" or not digits(f[1]) or int(f[1]) < 1 or f[2] not in ("1", "2", "3"):
        print(f"line {i}: invalid")
        continue
    g = int(f[1])
    if g > 50000:
        print(f"line {i}: too heavy")
        continue
    z = int(f[2])
    b, base = band(g)
    cost = (base * PCT[z] + 50) // 100
    print(f"{f[0]}: band={b} zone={z} cost={money(cost)}")
    cnt[b] = cnt.get(b, 0) + 1
    sums[b] = sums.get(b, 0) + cost
for b in "SMLXH":
    if b in cnt:
        print(f"band {b}: {cnt[b]} parcels, {money(sums[b])}")
print(f"total: {money(sum(sums.values()))}")
