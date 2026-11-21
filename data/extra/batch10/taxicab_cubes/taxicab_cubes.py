limit = 100000
ways = {}
a = 1
while 2 * a ** 3 <= limit:
    b = a
    while a ** 3 + b ** 3 <= limit:
        ways.setdefault(a ** 3 + b ** 3, []).append(f"{a}^3 + {b}^3")
        b += 1
    a += 1
found = 0
for n in sorted(ways):
    reps = ways[n]
    if len(reps) > 1:
        found += 1
        print(f"{n:>6} = {' = '.join(reps)}")
print(f"{found} numbers below {limit} with two representations; {len(ways)} sums in all")
