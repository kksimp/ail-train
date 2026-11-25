import sys

PLANS = {"basic": 1000, "pro": 2500, "team": 6000}

def money(c):
    s = "-" if c < 0 else ""
    a = abs(c)
    return f"{s}{a // 100}.{a % 100:02d}"

def digits(s):
    return s.isascii() and s.isdigit()

def part(price, days, cyc):
    return (price * days * 2 + cyc) // (2 * cyc)

billed = 0
net = 0
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = [x.strip() for x in line.split(",")]
    ok = len(f) == 5 and f[0] != "" and f[1] in PLANS and f[2] in PLANS and digits(f[3]) and digits(f[4])
    if ok:
        day, cyc = int(f[3]), int(f[4])
        ok = 28 <= cyc <= 31 and 1 <= day <= cyc
    if not ok:
        print(f"line {i}: invalid")
        continue
    old = part(PLANS[f[1]], day - 1, cyc)
    new = part(PLANS[f[2]], cyc - day + 1, cyc)
    total = old + new
    delta = total - PLANS[f[1]]
    print(f"{f[0]}: old={money(old)} new={money(new)} total={money(total)} delta={money(delta)}")
    billed += total
    net += delta
print(f"billed: {money(billed)}")
print(f"net change: {money(net)}")
