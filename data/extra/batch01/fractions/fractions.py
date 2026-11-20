from fractions import Fraction as F
def show(f): return f"{f.numerator}" if f.denominator == 1 else f"{f.numerator}/{f.denominator}"
a, b = F(1, 2), F(3, -4)
print(f"a = {show(a)}, b = {show(b)}")
print(f"a + b = {show(a + b)}")
print(f"a - b = {show(a - b)}")
print(f"a * b = {show(a * b)}")
print(f"a / b = {show(a / b)}")
print(f"H(6) = {show(sum(F(1, n) for n in range(1, 7)))}")
print(" < ".join(show(f) for f in sorted([F(2, 3), F(1, 6), F(5, 8), F(-1, 3)])))
