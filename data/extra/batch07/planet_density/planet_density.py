P = [("Mercury", 330.1, 2439.7), ("Venus", 4867.0, 6051.8), ("Earth", 5972.0, 6371.0), ("Mars", 641.7, 3389.5), ("Jupiter", 1898000.0, 69911.0), ("Saturn", 568300.0, 58232.0)]; D = []
for n, me, rk in P:
    m = me * 1000000000000000000000.0
    r = rk * 1000.0; v = 4.0 / 3.0 * 3.141592653589793 * r * r * r; d = m / v; D.append((n, d))
    print(f"{n:<8} {d:>7.0f} kg/m3, {d / 1000.0:.2f}x water{' (would float)' if d < 1000.0 else ''}")
print(" > ".join(x[0] for x in sorted(D, key=lambda x: -x[1])))
