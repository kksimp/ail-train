c = 12000; y0 = (12000 - 2000) // 5; s = d = c; print("year  straight  declining")
for y in range(1, 6): s -= y0; d = d * 70 // 100; print(f"{y:>4} {s:>9} {d:>10}")
print(f"straight-line charge {y0} a year")
