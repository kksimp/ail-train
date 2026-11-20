lines = ["Ana: -", "Ben: Ana", "Cho: Ana", "Dev: Ben", "Eli: Ben", "Fay: Cho", "Gus: Eli", "Hal: Ana"]
rep, root = {}, ""
for l in lines:
    a, b = l.split(": ")
    if b == "-": root = a
    else: rep.setdefault(b, []).append(a)
def pt(n, lv):
    print("  " * lv + n)
    for r in sorted(rep.get(n, [])): pt(r, lv + 1)
def hc(n): return sum(1 + hc(r) for r in rep.get(n, []))
pt(root, 0)
for m in sorted(rep): print(f"{m} leads {hc(m)}")
