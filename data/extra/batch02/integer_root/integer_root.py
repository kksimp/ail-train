from math import isqrt
for n in [0, 1, 15, 16, 17, 1000000, 999999999999, 9223372036854775807]:
    r = isqrt(n)
    print(f"isqrt({n}) = {r}, square: {str(r * r == n).lower()}")
print(f"squares below 200: {sum(1 for n in range(1, 200) if isqrt(n) ** 2 == n)}")
print(" ".join(str(isqrt(n)) for n in range(10)))
