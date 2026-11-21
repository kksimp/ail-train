shares = [("water utility", 2.4, 0.02), ("supermarket", 1.1, 0.04), ("software", 0.5, 0.07), ("start-up", 0.2, 0.12)]
r = 0.09
for name, d0, g in shares:
    if g >= r:
        print(f"{name:<14} cannot value: growth {g * 100.0:.1f}% is not below the required {r * 100.0:.1f}%")
        continue
    v = d0 * (1.0 + g) / (r - g)
    yld = d0 * (1.0 + g) / v * 100.0
    print(f"{name:<14} dividend {d0}, growth {g * 100.0:.1f}%: worth {v:.2f} (yield {yld:.2f}%)")
price = 30.0
implied = r - 2.4 * 1.02 / price
print(f"at a price of {price}, the utility implies growth of {implied * 100.0:.2f}%")
