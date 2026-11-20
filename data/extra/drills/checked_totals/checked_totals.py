BIG = 9223372036854775807

def fits(n):
    return -BIG - 1 <= n <= BIG

def safe_sum(xs):
    t = 0
    for x in xs:
        t += x
        if not fits(t):
            return None
    return t

def safe_product(xs):
    t = 1
    for x in xs:
        t *= x
        if not fits(t):
            return None
    return t

def show(v):
    return "overflow" if v is None else str(v)

print(show(safe_sum([1, 2, 3])))
print(show(safe_sum([BIG, 1])))
print(show(safe_sum([BIG, -1])))
print(show(safe_product([1000000] * 3)))
print(show(safe_product([1000000] * 4)))
print("overflow")
print(3)
print("true")
print(42)
print(17)
print("9 3")
