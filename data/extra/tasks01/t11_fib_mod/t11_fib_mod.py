import re, sys

def pint(s):
    return int(s) if re.fullmatch(r'-?[0-9]+', s) else None

def fib(n, m):
    a, b = 0, 1 % m
    for bit in bin(n)[2:] if n else '':
        c = a * ((2 * b - a) % m) % m
        d = (a * a + b * b) % m
        a, b = (d, (c + d) % m) if bit == '1' else (c, d)
    return a

for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    w = t.split()
    if len(w) != 2:
        print("error"); continue
    n, m = pint(w[0]), pint(w[1])
    if n is None or m is None or n < 0 or n > 10**18 or m < 1 or m > 10**9:
        print("error"); continue
    print(n, m, fib(n, m))
