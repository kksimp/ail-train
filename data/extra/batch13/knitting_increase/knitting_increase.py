def instructions(n, k):
    small = n // k
    big = k - n % k
    parts = []
    extra = n % k
    if extra > 0:
        parts.append(f"(k{small + 1}, m1) x{extra}")
    if big > 0:
        parts.append(f"(k{small}, m1) x{big}")
    return ", ".join(parts)

jobs = [[60, 6], [72, 10], [96, 16], [45, 7], [100, 12]]
for n, k in jobs:
    print(f"{n} stitches, add {k}: {instructions(n, k)} -> {n + k} stitches")
sweater = [[80, 8], [88, 8], [96, 12]]
st = 80
for i, j in enumerate(sweater):
    st = j[0] + j[1]
    print(f"yoke round {i + 1}: {instructions(j[0], j[1])}")
print(f"yoke ends with {st} stitches")
