st = [("soup", 450), ("salad", 550), ("bread", 320)]; mn = [("pasta", 1100), ("fish", 1500), ("curry", 1250)]; ds = [("sorbet", 400), ("tart", 600)]
cs = [(f"{s[0]} + {m[0]} + {d[0]}", s[1] + m[1] + d[1]) for s in st for m in mn for d in ds if s[1] + m[1] + d[1] <= 2000]
for c in sorted(cs, key=lambda c: c[1]): print(f"{c[1] // 100}.{c[1] % 100:02d}  {c[0]}")
print(f"{len(cs)} of 18 fit 20.00")
