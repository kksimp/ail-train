def rb(x, k):
    r = 0
    for _ in range(k): r = (r << 1) | (x & 1); x >>= 1
    return r
def bi(x, k): return format(x, f"0{k}b")
for x in [1, 6, 11, 13]: r = rb(x, 4); print(f"{x:>2} {bi(x, 4)} -> {bi(r, 4)} {r:>2}")
print("FFT order: " + " ".join(str(rb(i, 4)) for i in range(16)))
print("unchanged: " + " ".join(str(i) for i in range(16) if rb(i, 4) == i))
