def price(F, cr, n, y): return sum(F * cr / (1.0 + y) ** t for t in range(1, n + 1)) + F / (1.0 + y) ** n
for y in [0.03, 0.04, 0.05, 0.06, 0.08]:
    p = price(1000.0, 0.05, 10, y); lab = "premium" if p > 1000.001 else "discount" if p < 999.999 else "at par"
    print(f"yield {y * 100.0:.1f}%: price {p:>8.2f} ({lab}), current yield {50.0 / p * 100.0:.2f}%")
print(f"at 8%: 2-year {price(1000.0, 0.05, 2, 0.08):.2f}, 30-year {price(1000.0, 0.05, 30, 0.08):.2f}")
