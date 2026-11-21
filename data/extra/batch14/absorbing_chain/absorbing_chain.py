from fractions import Fraction as F
def show(f):
    return f"{f.numerator}" if f.denominator == 1 else f"{f.numerator}/{f.denominator} = {f.numerator / f.denominator:.3f}"
stay = [1, 1, 1]
advance = [7, 8, 8]
names = ["first year", "second year", "third year"]
years = [F(0)] * 4
grad = [F(0), F(0), F(0), F(1)]
for i in range(2, -1, -1):
    years[i] = (1 + F(advance[i], 10) * years[i + 1]) / (1 - F(stay[i], 10))
    grad[i] = F(advance[i], 10) * grad[i + 1] / (1 - F(stay[i], 10))
for k in range(3):
    print(f"from {names[k]:<11} (repeat {stay[k]}/10, advance {advance[k]}/10): years left {show(years[k])}, graduates {show(grad[k])}")
print(f"a new student drops out with chance {show(1 - grad[0])}")
