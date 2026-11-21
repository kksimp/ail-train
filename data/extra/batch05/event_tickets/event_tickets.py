T = [["early", 2500, 5], ["standard", 3500, 8], ["late", 4500, 6]]; rev = 0
for w, n in [("Ola", 3), ("Pat", 4), ("Quin", 2), ("Raj", 6), ("Sue", 5), ("Tom", 2)]:
    ps = []; c = 0
    for t in T:
        if n == 0 or t[2] == 0: continue
        k = min(n, t[2]); t[2] -= k; n -= k; c += k * t[1]; ps.append(f"{k} {t[0]}")
    rev += c
    if not ps: print(f"{w}: sold out")
    else: print(f"{w}: {' + '.join(ps)}, {n} short, pays {c // 100}" if n > 0 else f"{w}: {' + '.join(ps)}, pays {c // 100}")
print(f"revenue {rev // 100}")
