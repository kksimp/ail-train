def cv(c): return 11 if c == "A" else 10 if c in "KQJ" else int(c)
def score(h):
    t = sum(cv(c) for c in h); a = h.count("A")
    while t > 21 and a > 0:
        t -= 10; a -= 1
    return t
def verdict(h):
    s = score(h)
    return f"bust ({s})" if s > 21 else "blackjack" if s == 21 and len(h) == 2 else f"{s}"
hands = [["A", "K"], ["A", "A", "9"], ["10", "6", "K"], ["7", "A", "3"], ["A", "A", "A", "A"], ["5", "5", "A", "Q"]]
for h in hands:
    print(f"{' '.join(h):<10} {verdict(h)}")
ok = [h for h in hands if score(h) <= 21]
best = ok[0]
for h in ok:
    if score(h) > score(best): best = h
print("best hand: " + " ".join(best))
