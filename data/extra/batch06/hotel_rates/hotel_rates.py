def rt(d): b = 14000 if d % 7 in (5, 6) else 11000; return b * 13 // 10 if 150 <= d < 240 else b
for w, a, n in [("Aldo", 10, 3), ("Bea", 160, 6), ("Cruz", 236, 7), ("Dina", 299, 2)]:
    t = 0
    for k in range(n):
        r = rt(a + k)
        if k >= 4: r = r * 9 // 10
        t += r
    print(f"{w}: {n} nights from day {a}, {t // 100}.{t % 100:02}")
