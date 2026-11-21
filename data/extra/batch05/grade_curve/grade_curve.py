R = [("Abe", 58), ("Bo", 71), ("Cai", 64), ("Dov", 49), ("Eli", 88), ("Fay", 95), ("Gus", 55), ("Hal", 60)]
def lt(s): return "A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F"
m = sum(p[1] for p in R) // len(R); b = 70 - m; print(f"raw mean {m}, bump {b}"); c = {g: 0 for g in "ABCDF"}
for n, s in R:
    cv = min(100, s + b); g = lt(cv); c[g] += 1; print(f"{n:<4} {s:>3} -> {cv:>3} {g}")
print(" ".join(f"{g}:{c[g]}" for g in "ABCDF"))
