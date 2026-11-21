def wy(n, b):
    w = [0] * (n + 1); w[0] = 1
    for i in range(1, n + 1):
        if i in b: continue
        for s in (1, 2, 3):
            if i - s >= 0: w[i] += w[i - s]
    return w[n]
for n in range(1, 11): print(f"{n:>2} stairs: {wy(n, set())} ways")
print(f"10 stairs with step 3 broken: {wy(10, {3})}")
