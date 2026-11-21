class Iv:
    def __init__(s, lo, hi):
        s.lo, s.hi = lo, hi
    def __add__(s, o):
        return Iv(s.lo + o.lo, s.hi + o.hi)
    def __sub__(s, o):
        return Iv(s.lo - o.hi, s.hi - o.lo)
    def __mul__(s, o):
        ps = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return Iv(min(ps), max(ps))
    def __truediv__(s, o):
        return s * Iv(1.0 / o.hi, 1.0 / o.lo)
    def text(s):
        return f"[{s.lo:.2f}, {s.hi:.2f}]"
def tol(v, pct):
    return Iv(v * (100.0 - pct) / 100.0, v * (100.0 + pct) / 100.0)
r1 = tol(100.0, 5.0)
r2 = tol(220.0, 5.0)
print(f"R1 = {r1.text()} ohm, R2 = {r2.text()} ohm")
print(f"in series: {(r1 + r2).text()}")
print(f"parallel as R1 R2 / (R1 + R2): {(r1 * r2 / (r1 + r2)).text()}  (too wide)")
one = Iv(1.0, 1.0)
tight = one / (one / r1 + one / r2)
print(f"parallel as 1 / (1/R1 + 1/R2): {tight.text()}  (exact range)")
v = Iv(11.5, 12.5)
print(f"current through R1 at {v.text()} volt: {(v / r1).text()} amp")
x = Iv(1.0, 2.0)
print(f"x = {x.text()}: x - x = {(x - x).text()}, x * x = {(x * x).text()}")
