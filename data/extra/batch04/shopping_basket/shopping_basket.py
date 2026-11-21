P = {"apple": 40, "milk": 115, "bread": 180, "jam": 250}; O = ["apple", "jam"]
c = {"apple": 7, "milk": 1, "jam": 3}
for k in sorted(c): l = c[k] * P[k]; print(f"{k:<6} x{c[k]} {l // 100}.{l % 100:02d}")
f = sum(c[k] * P[k] for k in c); t = sum((n - n // 3 if k in O else n) * P[k] for k, n in c.items())
print(f"subtotal {f // 100}.{f % 100:02d}, offers -{(f - t) // 100}.{(f - t) % 100:02d}, total {t // 100}.{t % 100:02d}")
