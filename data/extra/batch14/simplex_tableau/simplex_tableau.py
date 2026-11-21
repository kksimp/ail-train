from fractions import Fraction as F
def show(a):
    return f"{a.numerator}" if a.denominator == 1 else f"{a.numerator}/{a.denominator}"
names = ["x", "y", "z", "s1", "s2", "s3"]
t = [[F(v) for v in r] for r in [[2, 3, 1, 1, 0, 0, 5], [4, 1, 2, 0, 1, 0, 11], [3, 4, 2, 0, 0, 1, 8], [-5, -4, -3, 0, 0, 0, 0]]]
basis = [3, 4, 5]
print("maximise 5x + 4y + 3z with 2x + 3y + z <= 5, 4x + y + 2z <= 11, 3x + 4y + 2z <= 8")
while True:
    obj = t[3]
    enter = -1
    for j in range(6):
        if obj[j] < 0 and (enter < 0 or obj[j] < obj[enter]):
            enter = j
    if enter < 0:
        break
    leave = -1
    best = F(0)
    for i in range(3):
        if t[i][enter] > 0:
            ratio = t[i][6] / t[i][enter]
            if leave < 0 or ratio < best:
                leave, best = i, ratio
    print(f"{names[enter]} enters, {names[basis[leave]]} leaves (ratio {show(best)})")
    pivot = t[leave][enter]
    t[leave] = [v / pivot for v in t[leave]]
    for i in range(4):
        if i != leave:
            factor = t[i][enter]
            t[i] = [t[i][j] - factor * t[leave][j] for j in range(7)]
    basis[leave] = enter
for i in range(3):
    print(f"{names[basis[i]]} = {show(t[i][6])}")
print(f"best value {show(t[3][6])}")
