class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def minimax(depth, idx, maxing, leaves, count):
    count[0] += 1
    if depth == 0:
        return leaves[idx]
    best = -1 if maxing else 1000
    for c in range(3):
        v = minimax(depth - 1, idx * 3 + c, not maxing, leaves, count)
        best = max(best, v) if maxing else min(best, v)
    return best

def alphabeta(depth, idx, alpha, beta, maxing, leaves, count):
    count[0] += 1
    if depth == 0:
        return leaves[idx]
    a = alpha
    b = beta
    if maxing:
        high = -1
        for c in range(3):
            v1 = alphabeta(depth - 1, idx * 3 + c, a, b, False, leaves, count)
            high = max(high, v1)
            a = max(a, high)
            if a >= b:
                break
        return high
    low = 1000
    for c in range(3):
        v2 = alphabeta(depth - 1, idx * 3 + c, a, b, True, leaves, count)
        low = min(low, v2)
        b = min(b, low)
        if a >= b:
            break
    return low

for seed in [3, 8, 21]:
    rng = Lcg(seed)
    leaves = [rng.next(100) for _ in range(81)]
    c1 = [0]
    c2 = [0]
    v1 = minimax(4, 0, True, leaves, c1)
    v2 = alphabeta(4, 0, -1, 1000, True, leaves, c2)
    print(f"tree {seed:>2}: value {v1} / {v2}, minimax read {c1[0]} nodes, alpha-beta {c2[0]}")
