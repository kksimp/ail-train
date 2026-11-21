C = {1: "Ada", 2: "Bea", 3: "Cyd"}
O = [(101, 1, 2500), (102, 3, 900), (103, 4, 1200), (104, 1, 300), (105, 2, 4100), (106, 5, 50)]
print("inner join:")
for i, c, x in O:
    if c in C: print(f"  {i} {C[c]:<4} {x // 100}.{x % 100:02d}")
print("left join:")
for i, c, x in O: print(f"  {i} {C.get(c, '(none)'):<6} {x // 100}.{x % 100:02d}")
print(f"orders with no customer: {[o[0] for o in O if o[1] not in C]}")
sp = {}
for i, c, x in O:
    if c in C: sp[C[c]] = sp.get(C[c], 0) + x
for n in sorted(sp): print(f"{n}: {sp[n]}")
