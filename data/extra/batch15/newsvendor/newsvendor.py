def expected_profit(q, demand, probs, price, cost, salvage):
    total = 0.0
    for i in range(len(demand)):
        sold = demand[i] if demand[i] < q else q
        left = q - sold
        total += probs[i] * (float(sold) * price + float(left) * salvage - float(q) * cost)
    return total
demand = [60, 70, 80, 90, 100, 110, 120]
probs = [0.05, 0.1, 0.2, 0.3, 0.2, 0.1, 0.05]
price = 3.2; cost = 1.1; salvage = 0.3
under = price - cost; over = cost - salvage
ratio = under / (under + over)
print(f"critical ratio {ratio:.3f}")
cdf = 0.0; pick = demand[-1]
for i in range(len(demand)):
    cdf += probs[i]
    if cdf >= ratio:
        pick = demand[i]; break
print(f"order {pick} loaves")
for q in demand:
    e = expected_profit(q, demand, probs, price, cost, salvage)
    mark = " <- best" if q == pick else ""
    print(f"  order {q:>3}: expected profit {e:.2f}{mark}")
