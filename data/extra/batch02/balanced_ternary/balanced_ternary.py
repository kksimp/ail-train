def to_bt(n):
    if n == 0: return "0"
    d = []
    while n != 0:
        r = n % 3
        if r == 2:
            d.append("-"); n = (n + 1) // 3
        else:
            d.append("+" if r == 1 else "0"); n = (n - r) // 3
    return "".join(reversed(d))
def from_bt(s):
    n = 0
    for c in s: n = n * 3 + {"+": 1, "-": -1}.get(c, 0)
    return n
for n in [0, 1, 2, 3, 8, -8, 100, -42, 364]:
    t = to_bt(n)
    print(f"{n:>4} = {t:>7} -> {from_bt(t)}")
print(f"round trip failures: {sum(1 for n in range(-200, 201) if from_bt(to_bt(n)) != n)}")
