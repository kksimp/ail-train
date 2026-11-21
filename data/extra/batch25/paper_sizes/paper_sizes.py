import math

def halve(s):
    return [s[1] // 2, s[0]]

a = [841, 1189]
b = [1000, 1414]
root2 = math.sqrt(2.0)
print("size  A (mm)       B (mm)       C (mm)     A ratio")
for n in range(8):
    cw = int(math.floor(math.sqrt(float(a[0] * b[0])) + 0.5))
    ch = int(math.floor(math.sqrt(float(a[1] * b[1])) + 0.5))
    ratio = a[1] / a[0]
    aa = f"{a[0]}x{a[1]}"
    bb = f"{b[0]}x{b[1]}"
    cc = f"{cw}x{ch}"
    print(f"{n:>4}  {aa:<12} {bb:<12} {cc:<10} {ratio:.4f}")
    a = halve(a)
    b = halve(b)
print(f"root 2 is {root2:.4f}; an A0 sheet holds {1 << 4} A4 sheets")
