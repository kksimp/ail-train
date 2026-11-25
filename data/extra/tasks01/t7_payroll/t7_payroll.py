import sys

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def parse(line):
    f = line.split(",")
    if len(f) != 3:
        return None
    name = f[0].strip()
    h = f[1].strip()
    r = f[2].strip()
    if not name or not h.isascii() or not r.isascii() or not h.isdigit() or not r.isdigit():
        return None
    return name, int(h), int(r)

total = 0
count = 0
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    rec = parse(line)
    if rec is None:
        print(f"line {i}: invalid")
        continue
    name, h, r = rec
    reg = min(h, 40) * r
    ot = max(h - 40, 0) * r * 3 // 2
    print(f"{name}: reg={money(reg)} ot={money(ot)} gross={money(reg + ot)}")
    total += reg + ot
    count += 1
print(f"total: {count} employees gross={money(total)}")
