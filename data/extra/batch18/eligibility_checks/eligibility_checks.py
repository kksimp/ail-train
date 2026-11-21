pool = [("Femi", [72, 88, 65, 91], 21000), ("Greta", [95, 49, 90, 88], 18000), ("Hugo", [70, 75, 80, 84], 25000), ("Isla", [86, 90, 77, 59], 34000), ("Jun", [55, 85, 60, 62], 12000)]
el = lambda a: all(m >= 50 for m in a[1]) and any(m >= 85 for m in a[1]) and a[2] < 30000
for a in pool:
    print(f"{a[0]:<6} fails {sum(1 for m in a[1] if m < 50)}, distinctions {sum(1 for m in a[1] if m >= 85)}: {'eligible' if el(a) else 'not eligible'}")
print(f"{sum(1 for a in pool if el(a))} of {len(pool)} eligible")
f = [a for a in pool if el(a) and a[2] < 15000]
print(f"first priority award: {f[0][0]}")
print(f"everyone passed every module: {str(all(all(m >= 50 for m in a[1]) for a in pool)).lower()}")
