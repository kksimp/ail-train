import sys

def money(c):
    s = "-" if c < 0 else ""
    a = abs(c)
    return f"{s}{a // 100}.{a % 100:02d}"

bud = {}
act = {}
cats = set()
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = [x.strip() for x in line.split(",")]
    if len(f) != 3 or f[0] not in ("budget", "actual") or f[1] == "" or not (f[2].isascii() and f[2].isdigit()):
        print(f"line {i}: invalid")
        continue
    d = bud if f[0] == "budget" else act
    d[f[1]] = d.get(f[1], 0) + int(f[2])
    cats.add(f[1])

tb = ta = 0
for c in sorted(cats, key=lambda s: s.encode()):
    b = bud.get(c, 0)
    a = act.get(c, 0)
    used = "n/a" if b == 0 else f"{a * 100 // b}%"
    st = "OVER" if a > b else "UNDER" if a < b else "MET"
    print(f"{c}: budget={money(b)} actual={money(a)} diff={money(b - a)} used={used} {st}")
    tb += b
    ta += a
print(f"total: budget={money(tb)} actual={money(ta)} diff={money(tb - ta)}")
