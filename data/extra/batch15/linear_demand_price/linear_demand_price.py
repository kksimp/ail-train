a = 2000.0; b = 80.0
def qty(p):
    q = a - b * p
    return q if q > 0.0 else 0.0
c = 6.0
rev_p = a / (2.0 * b)
profit_p = (a / b + c) / 2.0
print(f"revenue peaks at {rev_p:.2f}, profit peaks at {profit_p:.2f}")
for p in [8.0, 10.0, 12.0, 12.5, 14.0, 15.5, 18.0]:
    q = qty(p); rev = p * q; profit = (p - c) * q
    mark = " max revenue" if abs(p - rev_p) < 0.001 else " max profit" if abs(p - profit_p) < 0.001 else ""
    print(f"price {p:>5.2f}: sell {q:>6.0f}, revenue {rev:>8.2f}, profit {profit:>8.2f}{mark}")
print(f"nobody buys at {a / b:.2f} or more")
