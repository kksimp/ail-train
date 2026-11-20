def riffle(d):
    h = len(d) // 2
    out = []
    for a, b in zip(d[:h], d[h:]):
        out += [a, b]
    return out
def cyc(n):
    s = list(range(n)); d = riffle(s); c = 1
    while d != s:
        d = riffle(d); c += 1
    return c
print(" ".join(map(str, riffle([1, 2, 3, 4, 5, 6, 7, 8]))))
for n in [2, 4, 8, 10, 14, 52, 64]:
    print(f"{n:>2} cards: {cyc(n)} shuffles")
ev = [n for n in range(2, 41) if n % 2 == 0]
w = ev[0]
for n in ev:
    if cyc(n) > cyc(w): w = n
print(f"most shuffles up to 40 cards: {w} cards, {cyc(w)}")
