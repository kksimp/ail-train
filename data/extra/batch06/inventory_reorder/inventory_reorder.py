o = 0
for n, s, d, l, sf in [("bolts", 420, 35, 5, 60), ("nuts", 900, 40, 5, 80), ("washers", 150, 20, 7, 50), ("hinges", 75, 4, 14, 20), ("screws", 260, 30, 3, 40)]:
    p = d * l + sf
    if s <= p: o += 1; print(f"{n}: stock {s} <= {p}, order {d * 30 + p - s}")
    else: print(f"{n}: stock {s}, reorder in {(s - p) // d} days")
print(f"{o} orders to place")
