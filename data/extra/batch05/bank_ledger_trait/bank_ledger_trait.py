c = 250000; s = 500000
for m in range(1, 13):
    c -= 450; s += s * 450 // 120000
    if m % 4 == 0: print(f"month {m:>2}: current {c}, savings {s}")
g = s - 500000; print(f"savings interest {g // 100}.{g % 100:02}")
