def co(s):
    l = s; t = 0
    for w, r in [(1000000, 3), (1500000, 5), (-1, 8)]:
        p = l if w < 0 or l < w else w; t += p * r // 100; l -= p
        if l <= 0: break
    return t
P = 0
for n, s in [("Ines", 840000), ("Jon", 1000000), ("Kemi", 2150000), ("Lars", 2500000), ("Mia", 4120000)]:
    c = co(s); P += c; print(f"{n:<5} sales {s // 100:>6}: commission {c // 100}.{c % 100:02}")
print(f"total commission {P // 100}.{P % 100:02}")
