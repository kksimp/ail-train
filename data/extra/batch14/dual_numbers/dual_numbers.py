def f(v, d):
    x3v = v * v * v
    # mirror the dual arithmetic exactly
    xx = (v * v, d * v + v * d)
    xxx = (xx[0] * v, xx[1] * v + xx[0] * d)
    two_x = (2.0 * v, 0.0 * v + 2.0 * d)
    num = (xxx[0] + two_x[0], xxx[1] + two_x[1])
    den = (v + 1.0, d + 0.0)
    return (num[0] / den[0], (num[1] * den[0] - num[0] * den[1]) / (den[0] * den[0]))
def by_hand(x):
    return ((3.0 * x * x + 2.0) * (x + 1.0) - (x * x * x + 2.0 * x)) / ((x + 1.0) * (x + 1.0))
for x in [0.0, 1.0, 2.5, -3.0]:
    rv, rd = f(x, 1.0)
    print(f"x = {x}: f = {rv:.4f}, f' by duals {rd:.4f}, by the quotient rule {by_hand(x):.4f}")
x = 2.0
for step in range(1, 6):
    gg = (x * x, 1.0 * x + x * 1.0)
    ggg = (gg[0] * x, gg[1] * x + gg[0] * 1.0)
    two = (2.0 * x, 0.0 * x + 2.0 * 1.0)
    hv = ggg[0] - two[0] - 5.0
    hd = ggg[1] - two[1] - 0.0
    x = x - hv / hd
    print(f"Newton step {step} on x^3 - 2x - 5: x = {x:.10f}")
