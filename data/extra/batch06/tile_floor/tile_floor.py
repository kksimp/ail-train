T = 0
for n, w, l in [("kitchen", 3400, 2800), ("bathroom", 2100, 1700), ("hall", 4600, 1100)]:
    a = -(-w // 303); d = -(-l // 303); wh = (w // 303) * (l // 303); t = a * d; T += t; print(f"{n}: {t} tiles ({wh} whole, {t - wh} cut)")
s = (T * 11 + 9) // 10; print(f"total {T}, with 10% spare {s}, {-(-s // 12)} boxes")
