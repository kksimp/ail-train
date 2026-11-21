import math

outer = 2.0 * math.sqrt(3.0)
inner = 3.0
sides = 6
pi = 3.141592653589793
while sides <= 6144:
    width = outer - inner
    print(f"{sides:>5} sides: {inner:.8f} < pi < {outer:.8f}  (gap {width:.9f})")
    outer = 2.0 * outer * inner / (outer + inner)
    inner = math.sqrt(outer * inner)
    sides *= 2
print(f"pi = {pi:.8f}")
