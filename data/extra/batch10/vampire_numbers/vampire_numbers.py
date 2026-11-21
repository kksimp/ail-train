def sorted_digits(n):
    return "".join(sorted(str(n)))

def fangs(lo, hi):
    found = {}
    for x in range(lo, hi):
        for y in range(x, hi):
            n = x * y
            if n < lo * hi or n >= hi * hi:
                continue
            if x % 10 == 0 and y % 10 == 0:
                continue
            if sorted_digits(n) == sorted_digits(x * hi + y):
                found.setdefault(n, []).append(f"{x} x {y}")
    return found

four = fangs(10, 100)
for n in sorted(four):
    print(f"{n} = {', '.join(four[n])}")
six = fangs(100, 1000)
keys = sorted(six)
print(f"{len(keys)} six-digit vampires, the first {keys[:5]}")
for n in keys:
    if len(six[n]) > 1:
        print(f"{n} has two pairs of fangs: {' = '.join(six[n])}")
