import sys

PRICES = {"water": 3, "soda": 4, "juice": 5, "beer": 7, "wine": 22, "chocolate": 6}
totals = {}
skipped = 0
for line in sys.stdin.read().splitlines():
    if line.strip() == "":
        continue
    w = line.split()
    ok = False
    if len(w) == 3 and w[1] in PRICES:
        s = w[2]
        body = s[1:] if s.startswith("-") else s
        if body.isdigit() and body.isascii() and int(s) > 0:
            ok = True
    if not ok:
        skipped += 1
        continue
    totals[w[0]] = totals.get(w[0], 0) + PRICES[w[1]] * int(w[2])
if not totals:
    print("no charges")
else:
    for r in sorted(totals):
        print(f"{r}: {totals[r]}")
    print(f"total: {sum(totals.values())}")
if skipped:
    print(f"skipped: {skipped}")
