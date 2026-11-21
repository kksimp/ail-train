def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b

def row(beats, steps):
    every = steps // beats
    return "".join("x" if i % every == 0 else "." for i in range(steps))

for a, b in [[4, 6], [3, 4], [5, 4], [7, 3]]:
    steps = lcm(a, b)
    top = row(a, steps)
    bottom = row(b, steps)
    together = gcd(a, b)
    print(f"{a} against {b} on {steps} steps, together {together} time(s) per bar")
    print(f"  {top}")
    print(f"  {bottom}")
