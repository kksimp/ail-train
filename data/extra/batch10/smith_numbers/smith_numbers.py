def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def factors(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out.append(p)
            x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out

def is_smith(n):
    fs = factors(n)
    if len(fs) < 2:
        return False
    return sum(digit_sum(p) for p in fs) == digit_sum(n)

print(f"Smith numbers below 300: {[n for n in range(2, 300) if is_smith(n)]}")
for n in [4937775, 666, 9985]:
    fs = factors(n)
    print(f"{n} = {' x '.join(str(f) for f in fs)}: digit sums {digit_sum(n)} and {sum(digit_sum(p) for p in fs)}")
count = sum(1 for n in range(2, 10000) if is_smith(n))
print(f"{count} Smith numbers below 10000")
