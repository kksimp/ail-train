codes = ["C12", "A1", "K4", "B", "J20", "D0", "", "E7x", "H3"]
ok = []
for c in codes:
    if c == "": print(f"rejected seat {c}: empty"); continue
    l = c[0]
    if l < "A" or l > "J": print(f"rejected seat {c}: no row {l}"); continue
    r = c[1:]
    if not r.isdigit(): print(f"rejected seat {c}: seat is not a number"); continue
    n = int(r)
    if n < 1 or n > 20: print(f"rejected seat {c}: seats run 1 to 20"); continue
    ok.append((ord(l) - 65, n))
print(f"{len(ok)} good seats")
for r, n in sorted(ok): print(f"row {r + 1}, seat {n}")
