def pay(m, r):
    b = min(m, 2400); h = min(max(m - 2400, 0), 600); d = max(m - 3000, 0)
    return b, h, d, (b * r + h * r * 3 // 2 + d * r * 2) // 60
hrs = lambda m: f"{m // 60}:{m % 60:02d}"
bill = 0
for n, m, r in [("Ana", 2280, 1850), ("Bram", 2730, 2100), ("Chi", 3330, 1600), ("Dov", 0, 2500)]:
    b, h, d, t = pay(m, r); bill += t
    print(f"{n:<5} {hrs(m):>6} = {hrs(b)} + {hrs(h)} x1.5 + {hrs(d)} x2 -> {t // 100}.{t % 100:02d}")
print(f"payroll: {bill // 100}.{bill % 100:02d}")
