o = 1; t = 0; p = 0
for sq in range(1, 41):
    t += o
    if p == 0 and t * 0.025 >= 1000000.0: p = sq
    if sq <= 4 or sq % 8 == 0: print(f"square {sq:>2}: {o} grains, total {t}")
    o *= 2
print(f"total passes one tonne at square {p}"); print(f"after 40 squares: {t * 0.025 / 1000.0:.0f} kg")
