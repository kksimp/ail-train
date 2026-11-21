def spiral(n):
    order = []
    lo, hi = 1, n
    while lo <= hi:
        order.append(hi)
        if lo < hi:
            order.append(lo)
        lo += 1
        hi -= 1
    return order

def period(n):
    order = spiral(n)
    start = list(range(1, n + 1))
    cur = start
    steps = 0
    while True:
        cur = [cur[k - 1] for k in order]
        steps += 1
        if cur == start:
            break
    return steps

words = ["night", "river", "stone", "bread", "window", "hands"]
first = words
order = spiral(6)
for s in range(1, 7):
    print(f"stanza {s}: {' '.join(words)}")
    words = [words[k - 1] for k in order]
print(f"stanza 7 would repeat stanza 1: {'true' if words == first else 'false'}")
good = [n for n in range(1, 13) if period(n) == n]
print(f"spirals with period n up to 12: [{', '.join(str(g) for g in good)}]")
