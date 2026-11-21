import math
def area(d):
    pi = 3.141592653589793
    return pi * d * d / 4.0
def flow(dp, d1, d2, rho):
    a1 = area(d1); a2 = area(d2); beta = a2 / a1
    return a2 * math.sqrt(2.0 * dp / (rho * (1.0 - beta * beta)))
d1 = 0.1; d2 = 0.05; rho = 998.0
print("pipe 100 mm, throat 50 mm, water")
for dp in [500.0, 2000.0, 8000.0, 18000.0, 32000.0]:
    q = flow(dp, d1, d2, rho)
    v = q / area(d2)
    litres = q * 1000.0
    print(f"dp {dp:>7.0f} Pa: {litres:>6.2f} L/s, throat speed {v:.2f} m/s")
ratio = flow(8000.0, d1, d2, rho) / flow(2000.0, d1, d2, rho)
print(f"flow ratio for 4x the pressure drop: {ratio:.3f}")
