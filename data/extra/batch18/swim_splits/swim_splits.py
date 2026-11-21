def fmt(cs): return f"{cs // 6000}:{(cs // 100) % 60:02}.{cs % 100:02}"
swims = [("Ana", [3150, 3420, 3501, 3388]), ("Bea", [3099, 3466, 3550, 3290]), ("Cleo", [3205, 3380, 3412, 3310])]
for n, sp in swims: print(f"{n}: {fmt(sum(sp))} (fastest split {fmt(min(sp))})")
r = sorted(swims, key=lambda s: sum(s[1]))
for i, (n, sp) in enumerate(r): print(f"{i + 1}. {n} {fmt(sum(sp))}")
print(f"winning margin {fmt(sum(r[1][1]) - sum(r[0][1]))}")
