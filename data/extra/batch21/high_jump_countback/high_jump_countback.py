heights = [150, 155, 160, 165, 170]
field = [("Ama", ["o", "o", "xo", "xxo", "xxx"]), ("Bea", ["-", "o", "o", "xxo", "xxx"]), ("Cleo", ["o", "xo", "o", "o", "xxx"]), ("Dina", ["o", "o", "o", "xxx"]), ("Eve", ["xo", "o", "xxo", "xxx"]), ("Fay", ["o", "o", "xxo", "-", "xxx"])]
results = []
for name, marks in field:
    best = at_best = total = 0
    for i, m in enumerate(marks):
        total += m.count("x")
        if m.endswith("o"):
            best = heights[i]
            at_best = m.count("x")
    results.append((name, best, at_best, total))
ranked = sorted(results, key=lambda r: (-r[1], r[2], r[3]))
for i, r in enumerate(ranked):
    print(f"{i + 1}. {r[0]:<5} {r[1]} cm, {r[2]} misses there, {r[3]} in all")
print(f"{sum(1 for r in ranked if r[1] == ranked[0][1])} athletes cleared the winning height")
