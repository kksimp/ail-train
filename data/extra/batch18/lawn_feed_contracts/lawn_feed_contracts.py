bag = 4000
for n, a, r in [("front", 48, 20), ("back", 75, 25), ("verge", 12, 15), ("orchard", 60, 20)]:
    g = min(a * r, bag); bag -= g; need = a * r
    note = f"short {need - g} g" if g < need else "full dose"
    p = (max(g, 1) + 399) // 400
    print(f"{n:<8} {a:>3} m2: {g:>4} g in {p} passes, {note}")
print(f"left in bag: {bag} g")
