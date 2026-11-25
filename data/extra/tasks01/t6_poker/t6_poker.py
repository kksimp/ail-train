import sys
RANKS = "23456789TJQKA"
SUITS = "SHDC"
def classify(line):
    cards = line.split()
    if len(cards) != 5:
        return "invalid"
    rs, ss = [], []
    for c in cards:
        if len(c) != 2 or c[0] not in RANKS or c[1] not in SUITS:
            return "invalid"
        rs.append(RANKS.index(c[0]))
        ss.append(c[1])
    if len(set(cards)) != 5:
        return "invalid"
    counts = {}
    for r in rs:
        counts[r] = counts.get(r, 0) + 1
    shape = sorted(counts.values(), reverse=True)
    flush = len(set(ss)) == 1
    distinct = sorted(set(rs))
    straight = len(distinct) == 5 and (distinct[4] - distinct[0] == 4 or distinct == [0, 1, 2, 3, 12])
    if straight and flush:
        return "straight flush"
    if shape == [4, 1]:
        return "four of a kind"
    if shape == [3, 2]:
        return "full house"
    if flush:
        return "flush"
    if straight:
        return "straight"
    if shape == [3, 1, 1]:
        return "three of a kind"
    if shape == [2, 2, 1]:
        return "two pair"
    if shape == [2, 1, 1, 1]:
        return "pair"
    return "high card"
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
for l in lines:
    print(classify(l.rstrip("\r")))
