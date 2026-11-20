def digits(n):
    return [int(c) for c in str(n)]
def additive(n):
    s = 0
    while n >= 10:
        n = sum(digits(n)); s += 1
    return n, s
def mult(n):
    s = 0
    while n >= 10:
        p = 1
        for d in digits(n):
            p *= d
        n = p; s += 1
    return n, s
print(f"{'n':>8} root add mul-root mul")
for n in [0, 7, 39, 999, 2718, 277777788888899]:
    r, a = additive(n)
    mr, m = mult(n)
    print(f"{n:>8} {r:>4} {a:>3} {mr:>8} {m:>3}")
print("persistence 4+ below 1000: " + " ".join(str(n) for n in range(10, 1000) if mult(n)[1] >= 4))
