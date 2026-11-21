inbox = []
def insert(xs, x):
    i = 0
    while i < len(xs) and xs[i] <= x: i += 1
    xs.insert(i, x); return i
for m in [(2, 5, "lunch plans"), (1, 9, "server down"), (3, 11, "newsletter"), (1, 2, "invoice overdue"), (2, 5, "budget review")]:
    print(f"{m[2]} -> position {insert(inbox, m)}")
for p, mi, s in inbox: print(f"p{p} {mi:>2}m {s}")
t = []
for x in [40, 12, 33, 12, 7]: insert(t, x)
print(f"tickets {t}")
