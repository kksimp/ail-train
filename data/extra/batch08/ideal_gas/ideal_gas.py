absolute = 220.0 + 101.3; ck = 273.15 + 5.0
for c in [-10.0, 5.0, 20.0, 35.0, 60.0]:
    print(f"tyre at {c:>5.1f} C: {absolute * (273.15 + c) / ck - 101.3:>6.1f} kPa gauge")
for n, v, kpa, c in [("party balloon", 0.014, 101.3, 20.0), ("weather balloon", 4.2, 101.3, 15.0), ("scuba tank", 0.012, 20000.0, 20.0)]:
    print(f"{n:<15} {kpa * 1000.0 * v / (8.314 * (273.15 + c)):>8.2f} mol of gas")
