w = d = l = gf = ga = run = best = 0
for r in ["2-1", "0-0", "3-3", "1-2", "4-0", "2-2", "1-0", "0-1", "2-0", "1-1", "3-1"]:
    a, b = map(int, r.split("-")); gf += a; ga += b
    if a > b: w += 1
    elif a == b: d += 1
    else: l += 1
    if a >= b: run += 1; best = max(best, run)
    else: run = 0
print(f"W{w} D{d} L{l}, {w * 3 + d} points, goals {gf}-{ga} ({gf - ga:+})"); print(f"longest unbeaten run: {best}")
