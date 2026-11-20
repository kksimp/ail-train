def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]

def windows(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs) - n + 1)]

def window_sums(xs, n):
    return [sum(w) for w in windows(xs, n)]

readings = [4, 9, 2, 7, 7, 1, 8, 3]
for i, page in enumerate(chunks(readings, 3)):
    print(f"page {i + 1}: {' '.join(map(str, page))} (sum {sum(page)})")
print(",".join(map(str, window_sums(readings, 3))))
print(max(window_sums(readings, 3), default=0))
print(max(window_sums(readings, 20), default=0))
print(sum(1 for a, b in windows(readings, 2) if b > a))
print(len(chunks(readings, 8)))
print(len(windows(readings, 8)))
print(len(windows(readings, 9)))
