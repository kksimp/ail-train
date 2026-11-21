def h(kind, x):
    return 4.0 / (1.0 + x * x) if kind == 0 else 1.0 / x

def romberg(kind, a, b, rows):
    r = []
    strips = 1
    for n in range(rows):
        width = (b - a) / float(strips)
        s = (h(kind, a) + h(kind, b)) / 2.0
        for i in range(1, strips):
            s += h(kind, a + float(i) * width)
        row = [s * width]
        factor = 4.0
        for m in range(1, n + 1):
            row.append(row[m - 1] + (row[m - 1] - r[n - 1][m - 1]) / (factor - 1.0))
            factor *= 4.0
        r.append(row)
        strips *= 2
    return r

for kind in [0, 1]:
    print("integral of 4/(1+x^2) on [0, 1] = pi" if kind == 0 else "integral of 1/x on [1, 2] = ln 2")
    table = romberg(0, 0.0, 1.0, 5) if kind == 0 else romberg(1, 1.0, 2.0, 5)
    for row in table:
        print("    " + "  ".join(f"{v:.10f}" for v in row))
