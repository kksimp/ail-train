from collections import Counter
def kd(h):
    s = sorted(Counter(r for r, _ in h).values(), reverse=True); rk = sorted(r for r, _ in h); fl = all(c[1] == h[0][1] for c in h); st = len(s) == 5 and rk[4] - rk[0] == 4
    if st and fl: return "straight flush"
    if s[0] == 4: return "four of a kind"
    if s[0] == 3 and s[1] == 2: return "full house"
    if fl: return "flush"
    if st: return "straight"
    if s[0] == 3: return "three of a kind"
    if s[0] == 2 and s[1] == 2: return "two pair"
    if s[0] == 2: return "pair"
    return "high card"
N = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
for h in [[(9, "h"), (9, "s"), (4, "d"), (4, "c"), (12, "h")], [(5, "c"), (6, "d"), (7, "c"), (8, "s"), (9, "h")], [(2, "s"), (8, "s"), (11, "s"), (13, "s"), (5, "s")], [(14, "d"), (14, "h"), (14, "c"), (3, "s"), (3, "d")], [(10, "h"), (2, "c"), (7, "d"), (12, "s"), (6, "h")]]:
    print(" ".join(f"{N[r]}{s}" for r, s in h) + f": {kd(h)}")
