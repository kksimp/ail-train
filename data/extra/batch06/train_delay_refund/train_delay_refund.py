def rp(d): return 100 if d >= 60 else 50 if d >= 30 else 25 if d >= 15 else 0
B = {}
for w, p, d in [("Uma", 2450, 12), ("Vic", 3800, 35), ("Uma", 1990, 61), ("Wes", 5600, 15), ("Vic", 1200, 29), ("Wes", 2200, 5)]:
    pc = rp(d); a = p * pc // 100; B[w] = B.get(w, 0) + a; print(f"{w}: {d} min late, {pc}% of {p // 100}.{p % 100:02} = {a // 100}.{a % 100:02}")
for w in sorted(B): print(f"{w} total {B[w] // 100}.{B[w] % 100:02}")
