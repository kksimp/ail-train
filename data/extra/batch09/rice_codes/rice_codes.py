def rice(n, k):
    q = n >> k
    ones = "1" * q
    if k == 0:
        return ones + "0"
    low = n & ((1 << k) - 1)
    bits = f"{low:b}".rjust(k, '0')
    return ones + "0" + bits

deltas = [3, 0, 5, 2, 9, 1, 4, 6, 2, 0, 12, 3]
for n in [0, 3, 6, 12]:
    print(f"{n:>2} with k=2: {rice(n, 2)}")
best_k = 0
best_bits = -1
for k in range(5):
    total = sum(len(rice(d, k)) for d in deltas)
    print(f"k={k}: {total} bits")
    if best_bits < 0 or total < best_bits:
        best_bits = total
        best_k = k
print(f"best k={best_k}: {best_bits} bits against {len(deltas) * 8} as bytes")
