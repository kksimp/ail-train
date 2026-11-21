d = [38, 12, 77, 5, 64, 23, 91, 50, 17, 42, 8]
n = len(d)
print(f"sorted for reference: {sorted(d)}")
for k in [0, 2, n // 4, n // 2, 3 * n // 4, n - 1]: print(f"k={k}: {sorted(d)[k]}")
print(f"original untouched: {d}")
