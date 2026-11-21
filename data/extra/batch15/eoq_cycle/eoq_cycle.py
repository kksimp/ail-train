import math
def cost(it, q): return it[1] * it[2] / q + it[3] * q / 2.0
def eoq(it): return math.sqrt(2.0 * it[1] * it[2] / it[3])
items = [("printer paper", 2400.0, 40.0, 1.5), ("toner", 360.0, 55.0, 9.0), ("packing tape", 9000.0, 25.0, 0.2)]
for it in items:
    q = eoq(it)
    orders = it[1] / q
    days = 365.0 / orders
    print(f"{it[0]:<14} EOQ {q:>6.1f}, {orders:>5.2f} orders a year, every {days:.1f} days, cost {cost(it, q):.2f}")
paper = items[0]
base = cost(paper, eoq(paper))
for q in [200.0, 300.0, 400.0, 600.0]:
    extra = (cost(paper, q) / base - 1.0) * 100.0
    print(f"  paper in lots of {q:.0f}: cost {cost(paper, q):.2f} ({extra:.1f}% above best)")
