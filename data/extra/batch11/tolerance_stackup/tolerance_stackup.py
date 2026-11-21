import math
parts = [("bearing", 12000, 20), ("spacer", 8500, 50), ("gear", 15000, 30), ("circlip", 1200, 40)]
housing = 37000
housing_tol = 60
stack = sum(p[1] for p in parts)
gap = housing - stack
worst = housing_tol + sum(p[2] for p in parts)
squares = housing_tol * housing_tol
for p in parts:
    squares += p[2] * p[2]
    print(f"{p[0]:<8} {p[1]:>6} um +- {p[2]} um")
rss = math.sqrt(float(squares))
print(f"nominal gap {gap} um")
print(f"worst case: {gap - worst} to {gap + worst} um")
lo = float(gap) - rss
hi = float(gap) + rss
print(f"root sum square: {lo:.1f} to {hi:.1f} um")
print("always fits" if gap - worst >= 0 else "may jam in the worst case")
