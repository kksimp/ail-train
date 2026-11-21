import math
def total_cost(d, s, q, price, rate): return d * price + d * s / q + rate * price * q / 2.0
demand = 5000.0; setup = 60.0; rate = 0.25
tiers = [(1, 5.0), (500, 4.8), (1500, 4.6), (4000, 4.4)]
best_q = 0.0; best_cost = 1000000000.0
for mn, price in tiers:
    e = math.sqrt(2.0 * demand * setup / (rate * price))
    q = float(mn) if e < float(mn) else e
    c = total_cost(demand, setup, q, price, rate)
    note = f"raised to {mn}" if e < float(mn) else "EOQ fits"
    print(f"from {mn:>4} at {price:.2f}: EOQ {e:>5.1f}, order {q:>6.1f} ({note}), yearly cost {c:.2f}")
    if c < best_cost:
        best_cost = c; best_q = q
print(f"order {best_q:.0f} at a time for {best_cost:.2f} a year")
