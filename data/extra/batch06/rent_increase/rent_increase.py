r = 95000
for i, b in enumerate([320, 680, 410, 250, 720, 190]):
    a = min(b, 500); r += r * a // 10000; print(f"year {i + 1}: +{a // 100}.{a % 100:02}%{' (capped)' if b > 500 else ''} -> {r // 100}")
print(f"total rise {(r - 95000) * 100 // 95000}%")
