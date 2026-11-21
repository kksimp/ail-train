def weight(x):
    return bin(x).count("1")
codes = [("repetition (5,1)", 5, [31]), ("even parity (6,5)", 6, [33, 18, 12, 6, 3]), ("Hamming (7,4)", 7, [112, 76, 42, 105]), ("extended Hamming (8,4)", 8, [225, 153, 85, 255]), ("short code (6,3)", 6, [35, 21, 14])]
for name, n, gens in codes:
    k = len(gens)
    dist = {}
    d = n + 1
    for mask in range(1 << k):
        word = 0
        for i in range(k):
            if (mask >> i) & 1:
                word ^= gens[i]
        w = weight(word)
        dist[w] = dist.get(w, 0) + 1
        if w > 0:
            d = min(d, w)
    shown = " ".join(f"{w}:{dist[w]}" for w in range(n + 1) if w in dist)
    print(f"{name:<23} weights {shown}; d = {d}, detects {d - 1}, corrects {(d - 1) // 2}")
