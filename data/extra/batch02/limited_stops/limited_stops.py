fl = [("LIS", "MAD", 60), ("MAD", "BER", 90), ("LIS", "BER", 210), ("LIS", "PAR", 70), ("PAR", "AMS", 40), ("AMS", "BER", 30), ("BER", "WAW", 50)]
def ch(src, dst, k):
    cost = {src: 0}
    for _ in range(k + 1):
        prev = dict(cost)
        for a, b, p in fl:
            if a in prev and prev[a] + p < cost.get(b, 10**9):
                cost[b] = prev[a] + p
    return cost.get(dst)
for k in range(4):
    c = ch("LIS", "BER", k)
    print(f"LIS to BER with at most {k} stops: {c if c is not None else 'none'}")
c = ch("LIS", "WAW", 1); print(f"LIS to WAW, 1 stop: {c if c is not None else -1}")
c = ch("BER", "LIS", 5); print(f"BER to LIS: {c if c is not None else -1}")
