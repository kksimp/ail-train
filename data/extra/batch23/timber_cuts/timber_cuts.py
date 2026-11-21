def solve(prices, n, best, first):
    best.append(0)
    first.append(0)
    for len_ in range(1, n + 1):
        top = -1
        pick = 0
        for i in range(1, min(len_, len(prices)) + 1):
            v = prices[i - 1] + best[len_ - i]
            if v > top:
                top = v
                pick = i
        best.append(top)
        first.append(pick)

def pieces(first, n):
    parts = []
    left = n
    while left > 0:
        parts.append(f"{first[left]}")
        left -= first[left]
    return "+".join(parts)

prices = [1, 5, 8, 9, 10, 17, 17, 20]
best = []
first = []
solve(prices, 12, best, first)
print(f"price list by length 1..8: {prices}")
for n in range(1, 13):
    plan = pieces(first, n)
    whole = f"{prices[n - 1]}" if n <= len(prices) else "-"
    print(f"length {n:>2}: best {best[n]:>2} by cutting {plan:<7} (uncut sells for {whole})")
