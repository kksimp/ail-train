def ip(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
S = 11; G = [[0] * S for _ in range(S)]; x = y = S // 2; n = 1; G[y][x] = 1; st = 1; D = [(1, 0), (0, -1), (-1, 0), (0, 1)]; d = 0
while n < S * S:
    for _ in range(2):
        for _ in range(st):
            if n >= S * S: break
            x += D[d][0]; y += D[d][1]; n += 1; G[y][x] = n
        d = (d + 1) % 4
    st += 1
c = 0
for r in G: print("".join("#" if ip(v) else "." for v in r)); c += sum(1 for v in r if ip(v))
print(f"{c} primes up to {S * S}")
