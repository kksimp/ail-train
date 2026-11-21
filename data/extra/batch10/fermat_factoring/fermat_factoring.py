import math

def isqrt(v):
    y = int(math.sqrt(float(v)))
    while (y + 1) * (y + 1) <= v:
        y += 1
    while y * y > v:
        y -= 1
    return y

def fermat(n):
    a = isqrt(n)
    if a * a < n:
        a += 1
    steps = 1
    while True:
        b2 = a * a - n
        b = isqrt(b2)
        if b * b == b2:
            return (a - b, a + b, steps)
        a += 1
        steps += 1

for n in [5959, 8051, 1342127, 2027651281, 23757, 1000001, 97]:
    small, large, steps = fermat(n)
    kind = "prime" if small == 1 else "composite"
    print(f"{n:>10} = {small} x {large} after {steps} steps ({kind})")
