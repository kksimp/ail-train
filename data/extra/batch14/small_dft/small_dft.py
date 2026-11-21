import math
def tidy(v):
    return 0.0 if abs(v) < 0.0005 else v
x = [4.0, 8.0, 6.0, 2.0, 4.0, 8.0, 6.0, 2.0]
n = len(x)
two_pi = 2.0 * 3.141592653589793
re, im = [], []
for k in range(n):
    a = 0.0
    b = 0.0
    for t in range(n):
        ang = two_pi * (k * t) / n
        a += x[t] * math.cos(ang)
        b -= x[t] * math.sin(ang)
    re.append(a)
    im.append(b)
    mag = math.sqrt(a * a + b * b)
    print(f"bin {k}: magnitude {tidy(mag):.3f}")
back = []
for t in range(n):
    s = 0.0
    for k in range(n):
        ang = two_pi * (k * t) / n
        s += re[k] * math.cos(ang) - im[k] * math.sin(ang)
    back.append(f"{tidy(s / n):.3f}")
print("inverse: " + ", ".join(back))
print("only bins 0, 2 and 6 are lit: the pattern repeats every 4 samples")
