def demurrage(days):
    return sum(75 if d <= 10 else 150 for d in range(6, days + 1))

def detention(days):
    return max(days - 7, 0) * 50

boxes = [("MSKU101", 1, 4, 9), ("TGHU202", 1, 9, 20), ("CMAU303", 3, 16, 21), ("OOLU404", 5, 25, 40)]
total = 0
for bid, dis, pick, ret in boxes:
    port = pick - dis
    out = ret - pick
    dem = demurrage(port)
    det = detention(out)
    total += dem + det
    print(f"{bid}: {port:>2} days at port -> {dem:>4}, {out:>2} days out -> {det:>3}")
print(f"total charges {total}")
