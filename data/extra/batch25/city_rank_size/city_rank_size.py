import math

cities = [("Port Alder", 2450000), ("Kingsbridge", 910000), ("Eastholm", 780000), ("Marrow", 455000), ("Fenwick", 402000), ("Saltash", 330000), ("Dunmore", 268000), ("Ollerby", 241000)]
ranked = sorted(cities, key=lambda c: -c[1])
p1 = float(ranked[0][1])
sx = sy = sxx = sxy = 0.0
for i, c in enumerate(ranked):
    r = float(i + 1)
    expect = p1 / r
    share = c[1] / expect * 100.0
    print(f"{i + 1}. {c[0]:<12} {c[1]:>9,}  rule says {expect:>9.0f}  ({share:>5.1f}%)")
    x = math.log(r)
    y = math.log(float(c[1]))
    sx += x
    sy += y
    sxx += x * x
    sxy += x * y
n = float(len(ranked))
slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
primacy = p1 / ranked[1][1]
print(f"primacy ratio {primacy:.2f}, fitted exponent {-slope:.2f} (the rule says 1.00)")
