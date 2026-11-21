def rank_of(c):
    m = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    if c in m:
        return m[c]
    return int(c) if c.isdigit() else 0

def value(rank):
    return 10 if rank > 10 else rank

def fifteens(ranks):
    ways = 0
    for mask in range(1, 32):
        total = 0
        for i in range(5):
            if (mask >> i) & 1 == 1:
                total += value(ranks[i])
        if total == 15:
            ways += 1
    return ways * 2

def pairs(ranks):
    n = 0
    for i in range(5):
        for j in range(i + 1, 5):
            if ranks[i] == ranks[j]:
                n += 1
    return n * 2

def runs(ranks):
    counts = [0] * 15
    for x in ranks:
        counts[x] += 1
    score = 0
    r = 1
    while r <= 13:
        if counts[r] == 0:
            r += 1
            continue
        length = 0
        ways = 1
        while counts[r] > 0:
            length += 1
            ways *= counts[r]
            r += 1
        if length >= 3:
            score += length * ways
    return score

for h in ["555J5", "45566", "A2345", "789TJ", "QQKK3", "3369T", "77889"]:
    ranks = [rank_of(c) for c in h]
    f = fifteens(ranks)
    p = pairs(ranks)
    r = runs(ranks)
    print(f"{h}: fifteens {f:>2}, pairs {p:>2}, runs {r:>2}, total {f + p + r}")
