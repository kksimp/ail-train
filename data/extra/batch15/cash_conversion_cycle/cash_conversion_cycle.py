def days(part, whole): return part / whole * 365.0
firms = [("furniture maker", 4800.0, 3100.0, 730.0, 980.0, 410.0), ("supermarket", 26000.0, 20500.0, 90.0, 1350.0, 2600.0), ("wholesaler", 12000.0, 10400.0, 1900.0, 1500.0, 1100.0)]
for b in firms:
    dso = days(b[3], b[1]); dio = days(b[4], b[2]); dpo = days(b[5], b[2])
    c = days(b[3], b[1]) + days(b[4], b[2]) - days(b[5], b[2])
    note = "suppliers fund the business" if c < 0.0 else f"needs {c * b[2] / 365.0:.0f} of working capital"
    print(f"{b[0]:<15} DSO {dso:>5.1f} + DIO {dio:>5.1f} - DPO {dpo:>5.1f} = {c:>6.1f} days, {note}")
