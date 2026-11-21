from math import gcd
def frac(n, d):
    g = gcd(n, d)
    return f"{n // g}" if d // g == 1 else f"{n // g}/{d // g}"
def solve(name, cons, px, py):
    print(f"{name}: maximise {px}x + {py}y")
    seen = set()
    best, best_n, best_d = "", -1, 1
    for i in range(len(cons)):
        for j in range(i + 1, len(cons)):
            a, b = cons[i], cons[j]
            det = a[0] * b[1] - b[0] * a[1]
            if det == 0:
                continue
            xn = a[2] * b[1] - b[2] * a[1]
            yn = a[0] * b[2] - b[0] * a[2]
            if det < 0:
                det, xn, yn = -det, -xn, -yn
            if not all(c[0] * xn + c[1] * yn <= c[2] * det for c in cons):
                continue
            point = f"({frac(xn, det)}, {frac(yn, det)})"
            if point in seen:
                continue
            seen.add(point)
            vn = px * xn + py * yn
            print(f"    corner {point} gives {frac(vn, det)}")
            if vn * best_d > best_n * det:
                best_n, best_d, best = vn, det, point
    print(f"    best: {best} with {frac(best_n, best_d)}")
solve("doors and windows", [[1, 0, 4], [0, 2, 12], [3, 2, 18], [-1, 0, 0], [0, -1, 0]], 3, 5)
solve("feed mix", [[1, 2, 7], [3, 1, 9], [-1, 0, 0], [0, -1, 0]], 2, 3)
