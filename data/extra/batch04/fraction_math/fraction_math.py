from fractions import Fraction as F
s = lambda f: f"{f.numerator}" if f.denominator == 1 else f"{f.numerator}/{f.denominator}"
a, b = F(3, 4), F(-5, 6)
print(f"{s(a)} + {s(b)} = {s(a + b)}"); print(f"{s(a)} - {s(b)} = {s(a - b)}"); print(f"{s(a)} * {s(b)} = {s(a * b)}"); print(f"{s(a)} / {s(b)} = {s(a / b)}")
print(f"6/-8 reduces to {s(F(6, -8))}")
print(f"1 + 1/2 + ... + 1/10 = {s(sum(F(1, k) for k in range(1, 11)))}")
