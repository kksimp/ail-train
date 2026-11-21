best = ("", -1)
for n, r in [("read", "11011111101111"), ("run", "10101010101010"), ("water", "11111111111111"), ("journal", "00011101110111")]:
    m = [c == "1" for c in r]; s = len(r) - len(r.rstrip("1")); p = sum(m) * 100 // len(m)
    print(f"{n:<8} {''.join('x' if x else '.' for x in m)} {p:>3}% streak {s}")
    if s > best[1]: best = (n, s)
print(f"best streak: {best[0]} ({best[1]} days)")
