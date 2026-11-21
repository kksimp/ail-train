face = 10000.0
bills = [(91, 9880.0), (182, 9765.0), (364, 9520.0)]
for days, price in bills:
    d = (face - price) / face * 360.0 / float(days) * 100.0
    e = (face - price) / price * 365.0 / float(days) * 100.0
    f = ((face / price) ** (365.0 / float(days)) - 1.0) * 100.0
    print(f"{days:>3} days at {price:.2f}: discount {d:.3f}%, bond-equivalent {e:.3f}%, effective {f:.3f}%")
for q in [4, 5]:
    rate = float(q) / 100.0
    price = face * (1.0 - rate * 182.0 / 360.0)
    print(f"quoted at {q}% discount for 182 days: price {price:.2f}")
