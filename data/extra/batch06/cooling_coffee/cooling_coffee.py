t = 92.0; d = -1
for m in range(41):
    if m > 0: t = t - 0.045 * (t - 21.0)
    if m % 5 == 0: print(f"{m:>2} min: {t:.1f} C")
    if d < 0 and t <= 60.0: d = m
print(f"drinkable after {d} minutes")
