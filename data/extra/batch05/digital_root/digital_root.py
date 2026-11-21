def ds(n): return sum(int(d) for d in str(n))
for n in [7, 38, 999, 123456789, 65536, 1000000007]:
    x = n; r = 0
    while x >= 10: x = ds(x); r += 1
    print(f"{n}: root {x}, {r} rounds, shortcut agrees {'true' if x == 1 + (n - 1) % 9 else 'false'}")
