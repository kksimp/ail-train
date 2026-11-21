def ls(d, df):
    t = 0; b = df
    for x in reversed(d):
        if b: x *= 2; x = x - 9 if x > 9 else x
        t += x; b = not b
    return t
dg = lambda s: [int(c) for c in s if c.isdigit()]
for n in ["4539 1488 0343 6467", "4539 1488 0343 6468", "79927398713", "1234 5678 9012 3456"]: print(f"{n}: {'true' if ls(dg(n), False) % 10 == 0 else 'false'}")
for p in ["7992739871", "453914880343646"]: print(f"{p} + {(10 - ls(dg(p), True) % 10) % 10}")
