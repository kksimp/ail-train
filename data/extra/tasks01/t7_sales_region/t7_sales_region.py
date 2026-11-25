import sys

def money(c):
    s = "-" if c < 0 else ""
    a = abs(c)
    return f"{s}{a // 100}.{a % 100:02d}"

def isint(s):
    t = s[1:] if s.startswith("-") else s
    return t.isascii() and t.isdigit()

cell = {}
months = {}
skipped = 0
for line in sys.stdin.read().split("\n"):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = line.split(",")
    if len(f) != 3 or f[0].strip() == "" or not isint(f[1].strip()) or not isint(f[2].strip()):
        skipped += 1
        continue
    m = int(f[1].strip())
    if m < 1 or m > 12:
        skipped += 1
        continue
    r = f[0].strip()
    a = int(f[2].strip())
    cell[(r, m)] = cell.get((r, m), 0) + a
    months[m] = months.get(m, 0) + a

if not cell:
    print("no sales")
else:
    regions = sorted({r for r, _ in cell}, key=lambda s: s.encode())
    for r in regions:
        ms = sorted(m for rr, m in cell if rr == r)
        print(f"{r}: {money(sum(cell[(r, m)] for m in ms))}")
        for m in ms:
            print(f"  {m:02d}: {money(cell[(r, m)])}")
    print(f"all regions: {money(sum(months.values()))}")
    best = None
    for m in sorted(months):
        if best is None or months[m] > months[best]:
            best = m
    print(f"best month: {best:02d} ({money(months[best])})")
if skipped:
    print(f"skipped: {skipped}")
