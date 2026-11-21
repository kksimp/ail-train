def ga(H, n):
    u = d = 0; b = H[0]
    for h in H[1:]:
        df = h - b
        if df >= n: u += df; b = h
        elif -df >= n: d -= df; b = h
    return u, d
T = [212, 214, 213, 220, 231, 229, 240, 238, 241, 255, 251, 248, 236, 239, 230, 218, 219, 214]
for n in [1, 3, 5, 10]: g = ga(T, n); print(f"threshold {n:>2} m: up {g[0]} m, down {g[1]} m")
print(f"start {T[0]} m, peak {max(T)} m, finish {T[-1]} m")
